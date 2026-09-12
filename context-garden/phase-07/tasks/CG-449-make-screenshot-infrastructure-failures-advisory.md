---
id: CG-449
title: Make screenshot infrastructure failures advisory without hiding UI defects
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
order: -103
difficulty: hard
reading:
- src/garden/scheduler/checkruns.py
- src/garden/preflight.py
- src/garden/review.py
- src/garden/walkthrough.py
branch: codex/capture-infrastructure-advisory
pr: https://github.com/joshmarcus/context-garden/pull/332
runner: local
discovered_from: Owner approved screenshot infrastructure advisory policy while reviewing PR328
last_dispatched_at: '2026-09-08T22:16:27+00:00'
created: '2026-09-08T18:48:28+00:00'
updated: '2026-09-08T22:56:08+00:00'
---

## Goal

Implement the owner-approved temporary capture-infrastructure advisory policy with an explicit config switch and truthful preserved results.

## Acceptance criteria

- [ ] Default strict behavior remains available; owner-selected advisory capture policy survives dispatch/check/review and is visible.
- [ ] Only trusted screenshot browser/path/return infrastructure failures are advisory; retain their original errors and artifacts without manufacturing PNGs or pass results.
- [ ] Observed UI/application/render defects, functional failures, contradictory source/artifacts and truly unmet requested outcomes remain blocking.
- [ ] Small focused tests prove generation, collection/preflight and reviewer behavior; no repeated renderer revision solely for inaccessible infrastructure.

## Operator ownership

Owner explicitly requested this policy on September8. Sol subagent capture_policy_sol is implementing in isolated codex/capture-infrastructure-advisory. Do not duplicate. CG439/PR328 remains separate routing repair; CG443 separately classifies unrelated limitations.


## Implemented source and validation

Sol implementation commit 3976809c080057017a19ad740f6f51ce027e78b9 is in https://github.com/joshmarcus/context-garden/pull/332. Bounded supervised validation:40focused tests,4capture-transport tests,13application/render guards and Ruff passed. Receipts /home/joshua/work/operator-test-tmp/capture-policy-sol-validation. Root inspected the final diff; normal current-head automated review and CI remain required. Original capture errors are preserved, and visual limitations must be stated.

## Log

- 2026-09-08T19:15:15+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/332 (pr_number none -> 332)
- 2026-09-08T19:47:41+00:00 automated review could not start: git worktree add /home/joshua/work/worktrees/CG-449 codex/capture-infrastructure-advisory (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/capture-infrastructure-advisory')
fatal: 'codex/capture-infrastructure-advisory' is already used by worktree at '/home/joshua/work/operator-test-tmp/capture-policy-sol'
- 2026-09-08T20:51:58+00:00 automated review requested changes: The focused tests and lint pass, but advisory mode incorrectly treats a missing proposed-head source tree as capture infrastructure, and the required exact-head full suite failed without a same-environment base comparison. The saved generic interaction replay also does not exercise capture-policy behavior. cost=$0.50
- 2026-09-08T21:06:35+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-449`) or send it back (`garden triage CG-449 --changes "..."`)
- 2026-09-08T21:43:52+00:00 dispatched revise run 20260908T214352Z-revise-2 via manual [human] (fresh session, base main, ~12889 tokens)
- 2026-09-08T21:48:13+00:00 external PR attached at codex/capture-infrastructure-advisory; existing CI is PENDING
- 2026-09-08T21:56:13+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: observed ui/applicat; run `garden triage CG-449 --changes "<feedback>" to unblock`
- 2026-09-08T22:02:36+00:00 triage: changes requested by hand: Full applicable review 20260908T215048Z-review at 8cc6b7bc8b385bd8bfb759e9b4c3e66de01745a4

blocking src/garden/schedule
- 2026-09-08T22:04:01+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-449`) or send it back (`garden triage CG-449 --changes "..."`)
- 2026-09-08T22:04:08+00:00 dispatched revise run 20260908T220408Z-revise via manual [human] (fresh session, base main, ~13494 tokens)
- 2026-09-08T22:08:47+00:00 external PR attached at codex/capture-infrastructure-advisory; existing CI is PENDING
- 2026-09-08T22:16:27+00:00 dispatched revise run 20260908T221627Z-revise via manual [human] (fresh session, base main, ~12677 tokens)
- 2026-09-08T22:19:12+00:00 external PR attached at codex/capture-infrastructure-advisory; existing CI is PENDING
- 2026-09-08T22:27:46+00:00 automated review: approve — The advisory policy is narrowly bound to controller-generated screenshot checks, preserves failed records and fallback artifacts, and keeps source, application, renderer, functional, interaction, and contradictory-evidence failures blocking. Focused exact-head tests and lint pass; controller-owned exact-head CI remains a separate merge gate. cost=$0.53
- 2026-09-08T22:32:16+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-08T22:32:38+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:42:00+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:43:30+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:45:24+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:47:02+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:48:32+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:50:02+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:51:32+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:53:00+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T22:54:04+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-08T22:56:08+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/332
