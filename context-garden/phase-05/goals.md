# phase-05 goals (draft)

_Drafted by `garden retro` from context-garden/phase-04; edit before planning._

# phase-05 goals draft

## Purpose
After phase-04's security, data-integrity and admission-control blockers land, help a second team bring an existing repository into a working garden, with cost per accepted task measured before routing changes. This adoption headline is provisional pending the owner's decision; measurement is required under either headline.

## Entry conditions
Phase 04 remains reopened until the blocking work is complete. Reuse CG-238 and CG-239 rather than duplicating them. Confirm regression evidence for reading containment, safe scheduler git, held untrusted reloads, isolated planning and worker control state, concurrent task saves, reserved retro IDs, single-run admission and base-branch completion. Performance misses alone do not prolong phase 04, but its closing document must label them honestly.

## 1. Measure accepted outcomes before optimizing
Ship cost per accepted task and first-pass approval by model, tier and harness before CG-213 or CG-230 experiments. Define accepted as merged into the product base, include failed and revision work, state mixed-model attribution and distinguish unpriced usage from zero cost. Report hand merges with reasons, mechanical and agent rebases separately, tick mean/max and operator spend with explicit product/phase attribution. Reconcile the reported phase-04 baseline: 16/57 hand merges, $5.04 per easy task, 1.57 rebase rounds per merge and 71–79% first-pass approval. Retrieve an exact operator-share comparison rather than repeating inconsistent historical estimates. Proposed next-phase targets, pending owner approval: accepted easy-task cost at most $4 and first-pass approval at least 90% on a stated comparable cohort; retain zero unexplained hand merges and the under-ten-second tick and under-one-second action goals.

## 2. Complete the unattended review path
Widen existing CG-236 to every eligible PR with no review for its current head, including trial winners and manual runners. Align manual resume semantics, prevent duplicate review dispatch and discard stale-head verdicts. Cancel obsolete review processes promptly. Classify environment failures from harness error results rather than quoted worker prose; inspect the referenced CG-237 before assigning overlapping work. Test quota recovery without spending attempts on environment failures and without an infinite false-positive pause loop.

## 3. Make onboarding the adoption slice
Keep CG-215 as the existing onboarding task. Its output must pass doctor on a non-Python repository fixture without hand edits and produce criteria and reading paths accepted by the common gate. Use the isolated planner. Name a second team and repository for an observed onboarding session; if none is available, explicitly limit the acceptance claim to fixture validation. Fix brief repair and first-run guidance where they obstruct that journey.

## 4. Make routing valid, then test it
Make operating profiles reference compatible per-harness tier maps and use one vocabulary for operating profile versus observation feed. Do not send Claude model IDs to a Codex harness or claim economy is cheaper without accepted-outcome evidence. Then evaluate existing CG-230's harness/model pool with member attribution and paused-member avoidance. Keep CG-213 to an adapter around an existing compatible CLI if pursued; do not build another tool-calling loop in this phase.

## 5. Reduce the cost of operating and planning
Add safe redispatch and canary-backed pin operations as separate sequenced slices. Build briefs from explicit criteria, current source revisions, real diagnostic feedback and inlined retro evidence. At planning, sequence shared schema and behavior work rather than relying on unmerged siblings. Mechanically refuse approving reviews with missing or negative criterion evidence. Document recovery ordering and make check continuations and shared scheduler interfaces explicit.

## 6. Make the next retro trustworthy and manageable
Capture a current walkthrough before personas, including Costs, Backlog and Retro, and fix text extraction so hidden content and attributes do not become phantom UI findings. Add execution coverage for notification and kickoff interactions. Every finding remains visible with provenance and an existing-task link where applicable; automatic draft severity and cap remain governed by the owner's decision. Do not silently replace CG-187's policy. File each approved feature or follow-up once, deduplicating persona findings, feature entries and kickoff output.

## Surface and documentation completion
Use one needs-you predicate across interfaces; make incomplete-brief cards lead to repair; remove task IDs, redundant controls and contradictory restart guidance. Keep kickoff subordinate to active work. Align watch and serve configuration behavior, operator skill templates, design and roadmap claims and the architecture map. Enforce the module-size limit and remove implementation-only tests and test-only production wrappers where behavior coverage replaces them.

## Scope accounting and non-goals
Record CG-206 as cancelled and decide separately whether unattended notifications remain required. Use the final task list for CG-189 and CG-225 despite the earlier persona snapshot describing cancellation. Confirm phase-05 statuses for CG-213, CG-215, CG-216 and CG-230, and resolve CG-222's unknown disposition; do not invent statuses. Defer CG-216's HTTP remote-worker service until a named team needs it. No hosted multi-user expansion, new agent loop, broad evaluation corpus or default TUI-parity program. Do not raise concurrency merely to finish faster before accepted-outcome measurements support the change.

## Closure evidence
The phase-04 closing record must include the exact live metric command outputs or explicit unavailable markers, operator spend numerator and denominator, all hand-merge and outside-tick exceptions, final blocker task IDs, current walkthrough and owner policy answers. Phase 05 closes against the same documented definitions, with its current walkthrough captured before review and its known limitations stated explicitly.

## Features for the next phase

- CG-248: Measure cost per accepted task and first-pass approval
- CG-249: Keep retro triage within a visible draft budget
- CG-250: Add safe redispatch and canary-backed pin commands
- CG-251: Make retros capture and measure their own evidence
- CG-252: Make operating profiles harness-aware and consistently named

## Follow-ups carried from the retro verdict

- CG-284: Build revision briefs from current criteria and failure evidence
- CG-285: Sequence tasks that share a behavior or schema
- CG-286: Enforce acceptance evidence at review finalization
- CG-287: Classify harness failures from structured error results
- CG-288: Cancel obsolete review runs when tasks finish
- CG-289: Make check continuations explicit and recoverable
- CG-290: Enforce scheduler interfaces and the module-size cap
- CG-291: Unify actionable counts and brief-repair controls
- CG-292: Finish phase-page and CLI interaction consistency
- CG-293: Test notification and kickoff behavior in a browser
- CG-294: Align config reload behavior and operating documentation
- CG-295: Validate persona-run provenance and scrub notifications

## Decisions

- **Does the reopen carry all three blocking items, or only the brief-gate closure, with the two security fixes moved to phase 05 as its first tasks?** — answered: All of them. With the user's standing authority: CG-238 is merged and CG-239 is in review, so the reopen carries both; nothing moves to phase 05. Astra's reconcile has since filed CG-240 to CG-247 as further blocking items; which of those block and which become phase-05 follow-ups is settled by the joined retro. (by cli at 2026-09-05T23:43:16+00:00)
- **Is phase 05 about adoption (a second team on its own machines) or about cost per accepted task?** — answered: Adoption is the headline: phase 05 is the garden running in someone else's environment (onboarding CG-215, any model CG-213, shared quotas CG-230, any machine CG-216). Cost per accepted task is measured from the phase's first task as a prerequisite, not the headline (user's stub, 2026-09-05). (by cli at 2026-09-05T23:45:33+00:00)
- **Should phase 05 make onboarding the headline, with cost measurement as its first prerequisite, or make cost reduction the headline?** — answered: Adoption is the headline: phase 05 is the garden running in someone else's environment (onboarding CG-215, any model CG-213, shared quotas CG-230, any machine CG-216). Cost per accepted task is measured from the phase's first task as a prerequisite, not the headline (user's stub, 2026-09-05). (by cli at 2026-09-05T23:45:34+00:00)
- **How many drafts may a retro file, and at what severity?** — answered: Every finding is filed as a draft at its severity, no cap (user, 2026-09-05: do not schedule only two high items per review and toss the rest). The kickoff and the operator prune at approval; a finding that is not worth a task is cancelled with a reason, not dropped silently. (by cli at 2026-09-05T23:45:36+00:00)
- **Should retros keep filing every finding, or automatically file only high findings with an eight-draft cap and retain all others for explicit filing?** — answered: Every finding is filed as a draft at its severity, no cap (user, 2026-09-05: do not schedule only two high items per review and toss the rest). The kickoff and the operator prune at approval; a finding that is not worth a task is cancelled with a reason, not dropped silently. (by cli at 2026-09-05T23:45:38+00:00)
