# Cost-Aware Model Routing for Codex Tasks

_Spec written by the user on 2026-09-05 for the OpenRouter work in phase 05 (CG-213). Kept as written; the operator's notes on how it maps onto the garden today are at the end._

## Goal

Add support for running Codex-harness tasks through OpenRouter with different underlying models based on task difficulty and observed execution success.

The intent is to dramatically reduce agent execution cost without materially reducing task success rate.

Rather than using an expensive frontier model for every task, start with a cheaper model appropriate to the expected difficulty and automatically escalate when the task fails verification or appears stuck.

## Background

Current coding-model pricing varies by orders of magnitude, while recent coding-agent benchmarks suggest several inexpensive models are competitive on straightforward and medium-difficulty software-engineering tasks.

Initial candidates worth evaluating:

| Tier | Candidate | Intended Use |
|---|---|---|
| Easy | `deepseek/deepseek-v4-flash-0731` | Mechanical/simple implementation work |
| Medium | `z-ai/glm-5.3-flash` | Default implementation model |
| Codex-native value option | `openai/gpt-5.6-luna` | Cheap model with strongest expected Codex compatibility |
| Hard | `openai/gpt-5.6-sol` | Difficult implementation/debugging/reasoning |
| Escalation | Claude Opus-class model | Tasks that remain unsolved after normal escalation |

Approximate current OpenRouter pricing suggests that DeepSeek V4 Flash and GLM-5.3-Flash may cost a tiny fraction of GPT-5.6 Sol or Claude-class models.

The important optimization metric should therefore not be raw token price or benchmark score. It should be:

**cost per successfully accepted task**

A model that is 10× cheaper but requires repeated retries may not actually be cheaper.

## Proposed Architecture

Separate these concepts:

1. Task/context
2. Agent harness
3. Model
4. Verification
5. Escalation policy

Conceptually:

```
context-garden task
        |
        v
 difficulty / routing policy
        |
        v
    Codex harness
        |
        +--> OpenRouter --> cheap model
        |
        +--> OpenRouter --> medium model
        |
        +--> OpenAI/OpenRouter --> frontier model
        |
        v
 verification
        |
   success? ---- yes ---> complete
        |
        no
        v
 escalate model and retry
```

Codex remains the standardized execution harness: repository access, shell commands, patches, tests, AGENTS.md/context, MCP tools, etc.

The model should be independently selectable.

## Initial Routing Policy

Start with a deliberately simple policy.

### Easy

Use DeepSeek V4 Flash for tasks such as:

* straightforward file edits
* renames
* configuration changes
* documentation
* adding simple validation
* writing obvious unit tests
* mechanical refactors
* small functions with a clear specification
* fixing simple, localized test failures

Example:

```yaml
model_tier: easy
model: deepseek/deepseek-v4-flash-0731
```

### Medium

Use GLM-5.3-Flash as the initial default for most implementation tasks, including:

* normal feature implementation
* multi-file changes
* moderate refactoring
* debugging with a reasonably bounded problem
* writing tests plus implementation
* following an existing architectural pattern
* tasks requiring some repository exploration

Example:

```yaml
model_tier: medium
model: z-ai/glm-5.3-flash
```

This is likely the most important tier to evaluate. Current price/performance data suggests GLM-5.3-Flash could potentially handle a large majority of routine agent work extremely cheaply.

### Hard

Use GPT-5.6 Sol for tasks involving:

* architecture changes
* ambiguous bugs
* difficult debugging
* unfamiliar or complex subsystems
* cross-cutting changes
* concurrency/distributed-systems reasoning
* large refactors
* tasks where previous agents have failed
* tasks requiring substantial planning before implementation

Example:

```yaml
model_tier: hard
model: openai/gpt-5.6-sol
```

GPT models should also have the safest compatibility with the Codex harness because Codex increasingly uses richer Responses API/tool semantics.

### Escalation

Do not depend entirely on correctly predicting task difficulty.

Instead, make escalation an explicit part of execution.

For example:

```yaml
agent:
  initial_model: z-ai/glm-5.3-flash
  escalation:
    - after: 2_failed_iterations
      model: openai/gpt-5.6-sol
    - after: failed_final_verification
      model: anthropic/claude-opus-5
```

Possible escalation triggers:

* tests continue to fail
* lint/typecheck remains broken
* agent reports inability to proceed
* agent repeats effectively the same attempted fix
* maximum iteration count reached
* verification agent rejects the result
* expected files were not changed
* task-specific acceptance criteria are not met

Prefer objective signals over asking the model whether it thinks it is stuck.

## Codex Compatibility Testing

Do not assume every model advertised as supporting tool calls works correctly in Codex.

Build a small compatibility suite that checks:

- [ ] read repository files
- [ ] search repository
- [ ] execute shell command
- [ ] edit a file
- [ ] apply a patch
- [ ] run tests
- [ ] process tool failures
- [ ] continue through multiple tool-call iterations
- [ ] survive large repository context
- [ ] compaction / long-session behavior
- [ ] invoke MCP tools, if applicable
- [ ] use subagents, if applicable

Keep an allowlist of models known to work reliably with the current Codex version.

A model that performs well on coding benchmarks but frequently produces malformed or unsupported Codex tool calls should not receive production traffic.

## Benchmark / Evaluation Harness

Create a representative context-garden evaluation set.

Start with approximately 20–50 historical or synthetic tasks spanning:

* easy
* medium
* hard
* debugging
* new feature
* refactoring
* tests
* documentation/config
* repository exploration

Run the same tasks through each candidate model.

Capture at minimum:

```yaml
result:
  task_id:
  model:
  success:
  tests_passed:
  verification_passed:
  human_accepted:
  input_tokens:
  output_tokens:
  cached_tokens:
  cost_usd:
  wall_clock_seconds:
  agent_iterations:
  tool_calls:
  tool_errors:
  escalation_required:
```

Calculate:

* success rate
* human acceptance rate
* median cost per task
* cost per accepted task
* median runtime
* iterations per accepted task
* escalation frequency
* tool-call failure rate

The most important comparison is:

**total model spend / accepted tasks**

rather than:

$/million tokens

## Suggested Initial Experiment

Benchmark only a small set first:

* `deepseek/deepseek-v4-flash-0731`
* `z-ai/glm-5.3-flash`
* `openai/gpt-5.6-luna`
* `openai/gpt-5.6-sol`

Optionally add a Claude Opus-class model as an expensive quality control.

Avoid evaluating dozens of models until the evaluation framework itself is working.

## Configuration

Model routing should be configuration-driven rather than hard-coded.

For example:

```yaml
models:
  easy:
    provider: openrouter
    model: deepseek/deepseek-v4-flash-0731
  medium:
    provider: openrouter
    model: z-ai/glm-5.3-flash
  hard:
    provider: openrouter
    model: openai/gpt-5.6-sol
  escalation:
    provider: openrouter
    model: anthropic/claude-opus-5
```

Allow individual tasks to override the default tier or exact model.

Example:

```yaml
task:
  id: implement-query-cache
  difficulty: medium
agent:
  model_tier: medium
```

Or:

```yaml
agent:
  model: openai/gpt-5.6-sol
```

## Future Direction: Automatic Routing

Initially, assign difficulty using task metadata or simple heuristics.

Later, the scheduler could estimate difficulty using signals such as:

* task description length
* number of requested components
* expected files/subsystems involved
* whether the task is debugging vs. mechanical implementation
* historical difficulty of similar tasks
* prior failed attempts
* architectural keywords
* planner-generated complexity estimate

However, automatic classification should remain advisory.

Failure-driven escalation is likely more reliable than trying to perfectly classify task difficulty up front.

## Future Direction: Continuous Model Evaluation

The model market changes quickly.

Treat the evaluation corpus as part of context-garden infrastructure.

When an interesting new low-cost coding model appears:

```
new model
   |
   v
run context-garden eval corpus
   |
   v
compare $ / accepted task
   |
   +--> better --> add to routing pool
   |
   +--> worse --> ignore
```

This allows model selection to become empirical rather than driven by vendor benchmarks.

Potentially run this evaluation periodically or when explicitly requested.

## Acceptance Criteria

Phase 1 is complete when:

* Codex can run against OpenRouter using at least two configurable models.
* A task can specify a model or model tier.
* Easy/medium/hard defaults are configurable.
* Execution records model, tokens, cost, runtime, and result.
* Failed tasks can be retried using a higher model tier.
* A small Codex compatibility test suite exists.
* At least 20 representative tasks can be run across multiple models.
* Results include cost-per-accepted-task comparisons.
* The system can identify a recommended default model for easy, medium, and hard tasks based on measured results.

## Initial Hypothesis

The starting hypothesis to test is:

```
Easy
  DeepSeek V4 Flash
       |
       v
Medium/default
  GLM-5.3-Flash
       |
       v
Hard / escalation
  GPT-5.6 Sol
       |
       v
Exceptional escalation
  Claude Opus-class model
```

Do not lock this routing policy in permanently.

The objective of the work is to build enough measurement and routing infrastructure that context-garden can continuously determine the best model for each class of work based on real repository tasks.

---

## Operator's notes: how this maps onto the garden today (2026-09-05)

- **Tiers and per-task overrides exist.** `harnesses.<h>.models` maps easy/medium/hard to model ids per harness, and a task's `difficulty`, `harness` and (via trials) `model` already override; the codex harness runs `codex exec` with the CLI's default model today (`models: {}`). This spec's `models:` block with a `provider` field and an `escalation` tier is the shape CG-213 should adopt, with `provider: openrouter` selecting the base URL and key.
- **Escalation has a seam.** `_run_failed` retries while `attempts < max_attempts` and the revise loop counts `revisions` against a cap; the pre-PR checks, CI and the automated review are the objective signals the spec asks for. An escalation policy is a change to what `retry` and `revise` dispatch with: the next tier's model instead of the same one, recorded on the run.
- **Trials are the evaluation seed.** `garden trial <task> -c harness:model ...` runs contenders on their own branches and a comparison run scores them (two are running today: CG-030 easy and CG-225 medium, claude sonnet 5 against codex). The evaluation harness here is that mechanism over a fixed corpus of 20–50 tasks with the result record above, plus `garden metrics` per model.
- **Cost per accepted task is measurable now.** Every `run_finished` event carries cost and usage, tasks carry difficulty, and the costs page (CG-214) slices by model; the missing pieces are `human_accepted`, `tool_calls`, `tool_errors` and `escalation_required` on the run record, and codex's cost, which its JSON does not report (derive from usage and OpenRouter's pricing).
- **Compatibility suite.** `garden qa --scripted` and the fake harnesses are the pattern; a `garden harness-check <harness:model>` that runs the checklist above against a throwaway repo would gate a model into the routing pool.
- **Related tasks:** CG-213 (OpenRouter harness), CG-221 (the efficient-to-fast slider, whose stops would carry these tier maps), CG-214 (costs page), CG-212 (quota pauses), CG-217 (harness config dirs; codex needs `CODEX_HOME`).
