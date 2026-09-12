## Owner guidance: learn from review style feedback, 2026-09-09

The operator's recurring Inbox sweep also checks whether functionally sound work is being sent back for cosmetic preferences, stale findings or low-value comments. Preserve original verdicts and real check failures while reconciling current source and existing evidence. Do not demand missing optional artifacts or repeat already-resolved findings.

For useful recurring style feedback, improve the author brief upstream: record the concrete pattern and why it helps, with a small before/after example when supported by actual review evidence. Put code conventions near relevant code/task guidance, UI/copy conventions in product/design guidance, and general reporting guidance in the shared digest. Keep examples scoped, concise and free of reviewer-specific arbitrary preferences. Apply guidance to future briefs; do not restart active work or create a revision merely to enforce a new cosmetic rule. Owner-specific tradeoffs remain explicit decisions; ordinary clarity and consistency are handled by the worker/operator.
## Current owner policy: agent judgment and proportionate PR verification, 2026-09-09

Owner merge policy, September 9: merge an approved pull request when its current reviewed commit has passing applicable CI and GitHub reports it mergeable without conflicts. Do not force a rebase or another build solely because main advanced. Preserve current-head identity checks, substantive review rejection, actual failed checks, dependency constraints and atomic merge head guards. Latest-main validation may be an explicit opt-in policy; it is not the owner's default requirement. This is a requested scheduler implementation change; do not claim it is active in an installed immutable release until the new version is deployed.

The owner explicitly requests thoroughly relaxing PR requirements and letting workers and reviewers judge for themselves. Agents choose verification appropriate to the actual change and may supply relevant evidence or a clear, honest attestation of what they tested or inspected and the result. Reuse trustworthy existing checks. Focused tests, CLI checks, code inspection, CI, browser interaction, or a small integration exercise may each be sufficient according to the agent's judgment. Explain material uncertainty briefly; do not invent tests, observations, or success.

When a worker has not attached an artifact, assume the artifact is not included. Do not mention its absence in the review, summary, findings, nits, caveats, or revision feedback. Review the code and checks actually performed. Artifact absence alone is not material uncertainty and does not require an apology, limitation, or follow-up. Discuss a specific observed defect, failed applicable check, contradictory claim, or unmet explicit functional requirement when one exists; do not turn an unavailable optional attachment into such a finding.

Running-app journeys, generic HTTP replays, screenshots at prescribed widths/themes, empty and failure/recovery scenarios, scalability/load measurements, artifact manifests, exact evidence schemas, preflight checklists, and PR-description style are not blanket PR prerequisites. Missing such items alone must not block review or merge or trigger an unchanged implementation revision. File paths and keyword matches do not establish that these forms of evidence are required. A reviewer who needs more verification should identify the concrete changed behavior or unresolved correctness concern and choose a proportionate way to check it; a clear attestation is acceptable without prescribed artifact fields. Historical evidence may remain archived without creating new work.

Actual defects, actual failed applicable checks, contradictory claimed results/source identity, and genuinely unmet functional outcomes remain actionable. Distinguish them from optional presentation or evidence-form suggestions. Preserve full original findings and results, document current judgments separately, and respect current-head CI, versioned release/deployment rules, resource limits, AWS budget/deadlines, and explicit phase holds CG402/403/407/408. No production fault injection is implied. This policy supersedes earlier blanket verification, screenshot, running-app, lifecycle-state, or reporting-checklist language below. Reviewers need no further owner approval to exercise this judgment.

# The agent loop, and where tokens go

The loop is: human writes goals and specs -> planner emits tasks -> human approves ->
scheduler dispatches workers -> workers open PRs -> human reviews -> scheduler dispatches
revisions -> PR merges -> dependents unblock.

Only three steps spend tokens: planning, working, revising. Everything else (waiting for
workers, polling PRs, ordering the queue) is deterministic Python with no model in the loop.
An agent session used as a scheduler burns tokens *while waiting*; a Python process does not.

## Cost controls

- **Brief budget.** `garden brief <id> --stats` shows the exact prompt and its size. Keep
  the fixed sections small, and keep reading lists to what the worker needs.
- **One PR per task.** Workers do not push or open PRs; the runner does, deterministically.
- **Bounded retries.** `max_attempts` and `max_revisions` cap runaway loops.
- **Revisions carry only the delta.** A revise brief adds the review comments since the
  last dispatch, not the whole thread.
- **Planning is one call.** The planner sees goals, specs and the existing task list once
  and emits JSON. Humans edit the resulting files by hand.
