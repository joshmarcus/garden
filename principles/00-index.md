## Owner guidance: useful style feedback belongs in the brief, 2026-09-09

Apply relevant style feedback before submitting work: follow nearby code and the product's existing UI/copy conventions, and describe the concrete problem, resulting behavior and actual validation plainly. Prefer a small, consistent change over a new stylistic pattern. During self-review, check clarity and consistency in the changed area.

Lessons from recent reviews: describe lasting product behavior rather than the review process (for example, “Remote UI checks also…” instead of “The revision also…”). Keep the title, description and changed code focused on the same task; unrelated code or failing leftover tests are scope defects, while prose polish is advisory. UI labels must reflect current state: resolved findings must not say “Findings to address.” State which source was actually validated and distinguish reused older evidence; do not imply a check covered a newer head. These lessons improve clarity without requiring another revision solely for cosmetic wording.
When reviews reveal a recurring useful style lesson, the operator should add a short, concrete example or rule to the relevant task/product brief, scoped to that kind of work. Base it on actual feedback and established conventions; do not turn one reviewer's preference into a universal rule or paste whole review threads into every brief. Cosmetic preferences remain advisory. Request another revision only for a concrete defect, usability/accessibility problem, violated explicit requirement or applicable failed check. Do not create an extra review gate or require a style checklist/report.
## Current owner policy: agent judgment and proportionate PR verification, 2026-09-09

Owner merge policy, September 9: merge an approved pull request when its current reviewed commit has passing applicable CI and GitHub reports it mergeable without conflicts. Do not force a rebase or another build solely because main advanced. Preserve current-head identity checks, substantive review rejection, actual failed checks, dependency constraints and atomic merge head guards. Latest-main validation may be an explicit opt-in policy; it is not the owner's default requirement. This is a requested scheduler implementation change; do not claim it is active in an installed immutable release until the new version is deployed.

The owner explicitly requests thoroughly relaxing PR requirements and letting workers and reviewers judge for themselves. Agents choose verification appropriate to the actual change and may supply relevant evidence or a clear, honest attestation of what they tested or inspected and the result. Reuse trustworthy existing checks. Focused tests, CLI checks, code inspection, CI, browser interaction, or a small integration exercise may each be sufficient according to the agent's judgment. Explain material uncertainty briefly; do not invent tests, observations, or success.

When a worker has not attached an artifact, assume the artifact is not included. Do not mention its absence in the review, summary, findings, nits, caveats, or revision feedback. Review the code and checks actually performed. Artifact absence alone is not material uncertainty and does not require an apology, limitation, or follow-up. Discuss a specific observed defect, failed applicable check, contradictory claim, or unmet explicit functional requirement when one exists; do not turn an unavailable optional attachment into such a finding.

Running-app journeys, generic HTTP replays, screenshots at prescribed widths/themes, empty and failure/recovery scenarios, scalability/load measurements, artifact manifests, exact evidence schemas, preflight checklists, and PR-description style are not blanket PR prerequisites. Missing such items alone must not block review or merge or trigger an unchanged implementation revision. File paths and keyword matches do not establish that these forms of evidence are required. A reviewer who needs more verification should identify the concrete changed behavior or unresolved correctness concern and choose a proportionate way to check it; a clear attestation is acceptable without prescribed artifact fields. Historical evidence may remain archived without creating new work.

Actual defects, actual failed applicable checks, contradictory claimed results/source identity, and genuinely unmet functional outcomes remain actionable. Distinguish them from optional presentation or evidence-form suggestions. Preserve full original findings and results, document current judgments separately, and respect current-head CI, versioned release/deployment rules, resource limits, AWS budget/deadlines, and explicit phase holds CG402/403/407/408. No production fault injection is implied. This policy supersedes earlier blanket verification, screenshot, running-app, lifecycle-state, or reporting-checklist language below. Reviewers need no further owner approval to exercise this judgment.

## Current owner policy: bounded validation and capture infrastructure, September8

Owner requests 120 seconds per ordinary test and 900 seconds per validation command. Keep stress/load tests opt-in. Use focused tests first. An AWS full ordinary suite is at most one attempt per unchanged source/environment; if it reveals a shared failure, preserve the exact failing node/log and compare the focused failing test with base in the same environment. Do not repeatedly run the same full suite or repair unrelated implementation inside this PR. Confirmed shared/environment failures go to the matching recovery task; genuine PR regressions still block. Local WSL workers use focused tests only.

Until native supervisor deadline enforcement is deployed, use `timeout --signal=TERM --kill-after=10s 900 "$GARDEN_VALIDATION_RUNNER" -m garden.validation -- .venv/bin/python -m pytest --timeout=120 --timeout-method=thread <affected test files> -q`. The setup installs pinned pytest-timeout. Keep execution in the foreground and report timeout/interruption honestly; never substitute pass or silently deselect a failing test. Queue-wait/environment interruption is not automatically an implementation failure.

Screenshot capture/return infrastructure failures are temporarily advisory. Try scoped captures for material visual changes when the browser/artifact path works; preserve available PNG/HTML/text evidence. Do not add review commentary about artifacts that were not attached. A missing browser, controller-only path or artifact-return failure alone must not force request_changes or another unchanged author revision. Focused behavior tests and actual affected UI/HTTP behavior remain required as appropriate. Observed UI defects, application/render failures, functional test regressions, mismatched source claims and genuinely unverified requested outcomes still block. This supersedes earlier absolute screenshot language; the explicit mechanical advisory switch is being implemented separately and is not yet claimed deployed.

Review feedback must keep the full substantive findings/fixes and criterion-specific reasons alongside any operator recovery summary. A short triage note supplements those findings, rather than silently replacing them. Historical/negated mentions of scalability, stress or performance do not add load criteria to a task that makes no such acceptance claim. Keep the actual frozen functional criteria; reuse equivalent evidence and do not demand diagnosis of an unrelated whole-system incident.

## Owner remote validation and GitHub polling policy, 2026-09-08

External workers should run the full ordinary test suite on their AWS host, after focused iteration, with stress/load experiments excluded: `"$GARDEN_VALIDATION_RUNNER" -m garden.validation -- .venv/bin/python -m pytest -q`. Use actual named test paths for focused iteration. Local resource-constrained workers use focused tests. Do not run scripts/check_ci.py or push a worker branch solely to trigger/poll GitHub full-suite CI: product setup.worker_push is disabled, and the controller owns branch publication and remaining authenticated GitHub status reads. Report the exact tested commit, command, selection and result truthfully; missing or rate-limited external status is an operator/environment follow-up, not a reason to rerun implementation. CG-396 implements authoritative saved AWS-check receipts as the review/merge gate and removes duplicate full-suite GitHub runs; until that is deployed the controller still enforces its existing actual check/review gates. Never invent a passing result or copy controller credentials into a worker.

## Owner test policy, 2026-09-08

Stress/load/pressure experiments must not run as part of ordinary tests or routine CI. Use focused functional regressions and exact-head normal CI. Large-history latency benchmarks, generated CPU/memory load, and concurrent overload probes are separate, explicitly opt-in, bounded disposable experiments. Do not run them merely to obtain acceptance metadata or diagnose unrelated CI failures. CG-426 implements default test selection; older branches must explicitly exclude the known stress nodes until this fix is integrated.

# Principles digest

Inlined into every agent brief. Keep it short; long-form reasoning lives in the sibling files.

## Owner clarification: verification and implementer latitude, 2026-09-08

Missing artifact metadata alone is advisory and must not block a useful change whose substantive verification passes. Do not mention unattached artifacts or missing optional artifact metadata in the review, and do not demand another implementation round solely for formatting, filenames, omitted metadata fields or wording differences. Do not claim missing evidence was observed: actual failed tests, contradictory source identity, genuine bugs and materially unverified requested outcomes remain blockers.

Implementers may choose the mechanism and equivalent meaningful verification that prove the requested outcome while respecting explicit constraints. A named file, helper, test or prescribed sequence is guidance unless it encodes an explicit compatibility or correctness constraint. Reviewers must explain the concrete defect or unmet outcome behind a blocking finding and reuse valid inspectable evidence. Report evidence where the brief directs: source commit, actual command/check and result, observed actions/consequences, durable artifact paths and material limitations; never invent a result. Specific phase holds still require their stated evidence.


## Working style
- Ship small vertical slices. Every merged PR leaves the product working and tested.
- Read what the brief points at, then explore only the code you must change. Do not wander the context garden; if the brief is missing something, say so in your report so the task gets fixed.
- Follow existing conventions in the repo before inventing new ones. Match the surrounding style.
- Tests are part of the change. Run the project's fast checks before you finish; fix what you broke.
- Prefer boring, dependency-light solutions. New dependencies need a one-line justification in the PR body.
- A PR description frames the work by its goal and outcome and the general motivation: what a reader gets and why it was worth doing, then how, then what was verified. It reads as if written once, in the present tense, for someone who never saw the task or the review: no scar tissue (no round-by-round narration, no "addressed reviewer feedback", no references to earlier attempts or to what was tried and abandoned). Follow-ups go in one short section at the end.
- Optimise for cognitive complexity. At every level of abstraction the code should be as easy to understand as makes sense there: a reader of a module sees what it is for, a reader of a function sees what it does without holding the rest of the file in their head. Prefer one clear path over a clever one, names that say what a thing is, and small units with a single reason to change; do not spread one idea across layers or fold three ideas into one function. See `cognitive-complexity.md`.

## Reporting
- Be precise about what you did, what you verified, and what you did not do.
- If blocked on a human decision, stop early and ask one precise question rather than guessing.
- Note friction (missing context, confusing spec, tooling pain) in the `friction` field of your result, one short item each; it is filed on the phase and never goes in the PR body.

## Scope
- Do not widen the task. Follow-ups go in the PR body, not in the diff.
- Do not edit task files under `**/tasks/`; the scheduler owns them.
- Never rewrite history on shared branches; never disable or skip tests to get green.

## Design work is an invitation, not a prescription

When a task asks for a page, a mock or a visual system, the spec states the problem and what must be present; how it looks, reads and moves is yours to invent. We want new and beautiful ideas, not the requirements list laid out as boxes; depart from the prescription when you have a better idea and say why. Inspect the changed visual behavior using a suitable method and attest to what you checked; choose widths, themes, and captures according to the change rather than a mandatory matrix. (Owner, 2026-09-06.)

## Acceptance criteria are outcomes with evidence, never implementation

A criterion says what is true when the work is done and how anyone can see it: a page that answers, a test that proves, a number that reads. Prefer outcomes over mechanisms: a file, a function or a field named in a criterion is guidance for the worker, not a binding check, and the reviewer judges the outcome it points at rather than the name. Three to five lines, each verifiable. A worker who finds a criterion wrong or impossible as written reports a proposed replacement and reason in `criteria_amended`; the scheduler owns task-file edits. Equivalent means of meeting the intended outcome need no criterion rewrite. A reviewer marks each criterion met only with evidence it can point to. A task may carry no criteria at all: then the Goal is the contract, the worker states in its result what it verified and how, and the reviewer judges the goal on that evidence; the gate refuses a placeholder checklist, never an absent one. (Owner, 2026-09-06, from 304 reviews: a third of send-backs turn on a criterion; every misfire was a criterion that named an implementation detail.)

## Verify the intended outcome

Agents choose appropriate verification for each change under the current owner policy above. A running application and every empty/failure/recovery state are not universal requirements. Keep actual functional goals and phase-05 closure evidence separate from routine PR review. Phase-05 closure still requires specs/stabilization.md evidence, including productive unattended operation with agent-operator repairs counted as interventions; merged PRs alone do not satisfy that goal.

## Self-review before declaring completion

Owner instruction, 2026-09-06: Before reporting `done` or `no_change`, review your final diff against the base and the task's intended outcome as if you were its reviewer. Check correctness, failure/recovery paths, scope, unintended/generated changes, and whether your evidence supports each claimed outcome. If self-review finds an issue within scope, fix it, rerun affected checks, and review the corrected result again before declaring completion. Do not declare done while a known blocking defect remains; if you cannot resolve it, use the existing blocked/needs-input protocol. For UI and lifecycle changes, apply the actual-application interaction policy above. Keep this proportionate; it is a worker self-review, not another agent review round.

Self-review is an internal completion step: do not add a self-review report, checklist or result field to the final response or PR. Continue providing the ordinary required verification evidence and material limitations. For `no_change`, establish from evidence that no edit is needed. Never claim checks or interactions you did not perform. Self-review supplements the existing reviewer and does not replace it outside owner-authorized fast-forward.


## Snapshots are scoped to visual changes

Owner clarification, 2026-09-07: screenshots and design snapshots are not required for every PR. Require screenshots only for materially changed rendered appearance or an explicitly visual acceptance criterion, limited to affected pages/states. Backend/API/authentication, scheduling, tests, docs, and nonvisual refactors use relevant functional evidence; touching web/app.py or another shared module alone does not justify all-page screenshots. HTTP or lifecycle interaction evidence does not imply screenshot evidence. Shared visual styling/layout changes justify representative affected consumers, expanding only for distinct visual risks. Generated snapshots/capture artifacts are evidence outputs, not new UI inputs, and must not recursively trigger capture requirements. A reviewer must identify the changed visual behavior before blocking on missing snapshots. Preserve existing evidence and do not rewrite active task scope; flag overly broad mechanical requirements for operator correction.
