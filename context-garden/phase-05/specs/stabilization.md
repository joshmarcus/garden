# Stabilization and adoption evidence gate

Owner approved on 2026-09-06: defer additional features until the core loop is dependable, and review actual application journeys. This overrides feature-expansion scheduling in older goals. Phase 06 remains frozen until the evidence below is accepted. Finishing a PR or an empty inbox is not sufficient evidence.

## Required outcomes

1. A developer can onboard a repository other than context-garden, describe a useful change, understand the plan, and inspect an accepted working result. Use a disposable non-Python repository for repeatable checks; report it honestly as fixture evidence. A named existing project and maintainer acceptance are required before claiming real-user adoption. If no such project is available, report that gate as unproven rather than inventing a user.
2. Eight consecutive hours on a recorded pinned build, with at least ten completed representative tasks and no routine human or agent-operator repairs. Tasks must include useful implementation and revision work rather than ten artificial no-ops. Log all interventions, failures, recoveries, costs, resource pressure, head SHAs and final outcomes. Legitimate product decisions are reported separately; do not count operator requeue/status edits as unattended success. No productive queue means no successful soak claim. Run observation mechanically; never hold an expensive model session open for eight hours.
3. A disposable garden exercises worker interruption, failed checks, no_change both justified and ignoring feedback, quota/environment recovery, changed PR heads, and restart recovery. Changes remain intact, completed work reaches review/merge, and no stale or impossible human question remains. Fault injection never targets the owner's live garden.
4. A reviewer walks the actual running application through onboarding, planning, approval, progress, a real decision, failure, recovery and completion. Start with the user objective, not a click script or implementation walkthrough. Record actions, observed page state and consequences, plus captures. Screenshots alone cannot establish usable interaction. Every human prompt must explain the decision, why it is needed, recommendation and consequences. Missing questions, internal-status questions, wrong counts, and actions that strand work fail the gate.
5. Record available memory, swap activity, temp headroom, worker/check/review counts and effective limits throughout the soak. No resource-exhaustion cascade; limits and paused/draining states are understandable. Record actual end-to-end cost, operator interventions, regressions/reopened work, and lead time. Preserve existing cost/first-pass targets, report sample sizes and unpriced usage, and do not weaken reviews to meet a percentage.

## Review policy

For a PR affecting UI, decisions, scheduler state, or lifecycle behavior, exercise the affected flow in a disposable running application, plus an empty state and a relevant failure/recovery state. Review evidence is tied to the actual PR head/build. A screenshot or a unit test assertion alone is insufficient for an interaction claim. Pure non-UI changes retain proportionate focused validation. A fresh code review and behavior evaluation are complementary; additional identical review rounds are not a replacement for behavior evidence.

Until automatic enforcement lands, the operator applies this policy to applicable pending PRs. A failing journey blocks the relevant PR or milestone. Existing merged work is evaluated in the milestone run; do not retroactively claim it passed.

## Admission and completion

Phase 05 admits stability, safety, recovery, understandable decisions, evidence collection and the onboarding demonstration. Unrelated features and design consolidation stay in frozen phase 06. Record every finding, but merge duplicates and explicitly defer nonblocking scope; filing is not automatic phase admission. Already-running bounded work may finish through normal validation.

The evidence report states PASS, FAIL or UNPROVEN for each outcome, links artifacts/run ids/build SHAs, and lists remaining defects. Unproven is not pass. All required outcomes must pass before closing stabilization or unfreezing phase 06; operator exceptions require a new explicit owner decision.
