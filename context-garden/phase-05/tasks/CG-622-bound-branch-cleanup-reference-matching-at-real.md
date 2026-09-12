---
id: CG-622
title: Bound branch cleanup reference matching at real scheduler state scale
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-599
- CG-619
priority: 0
difficulty: hard
reading:
- context-garden/phase-05/docs/cleanup-reference-scaling-diagnosis.md
branch: garden/cg-622-bound-branch-cleanup-reference-matching-at-real
pr: https://github.com/joshmarcus/context-garden/pull/488
runner: remote
retro_blocking: true
attempts: 2
last_dispatched_at: '2026-09-11T06:02:30+00:00'
created: '2026-09-11T05:44:06+00:00'
updated: '2026-09-11T06:52:27+00:00'
---

## Goal

Restore bounded scheduler cleanup CPU work at actual state/run scale while retaining CG619 exact reference safety and every deletion guard. The required diagnosis records the installed RC20 stack and original failure; this is distinct from completed CG599 remote inventory work.

## Acceptance criteria

- [ ] Preserve exact literal boundary matching for native IDs, same-second suffixes, longer IDs, nested recovery and backup paths, artifact filenames, stash names, punctuation, Unicode and regex metacharacters; never release a truly referenced branch. No index survives a mutable snapshot.
- [ ] Avoid one full state regex scan per native run ID; use a fresh one-pass reference index or an equally bounded implementation. Make single-branch rechecks avoid irrelevant recovery matching without dropping global active-run or stack-base claims.
- [ ] Add differential correctness coverage against prior semantics, deterministic scaling coverage and a synthetic approximately13MB/5000-run benchmark. Preserve original evidence and report measured before/after with fixture construction excluded. Do not publish private scheduler state.
- [ ] Preserve fresh open-PR and dependency checks, active/recovery ownership, worktrees, protected/default branches, preserved source and compare-and-delete identity checks. Do not disable cleanup or weaken retention. Run focused cleanup and scheduler regressions, Ruff, current exact-head CI and independent review. Use portable APIs and report Linux/macOS/Windows-through-WSL coverage truthfully.

## Scope and ownership

P0 reopened Phase05 closing repair. Root owns guarded operator recovery and temporary supported cleanup batch1 mitigation, later restored to20 after accepted activation. Implement the source repair through this native remote task. Preserve all current work, history, fleet limits, budgets and absolute deadlines. No runtime hotpatch or invented stabilization/canary gate.


## Source locations

Read current product source src/garden/branch_cleanup.py, src/garden/scheduler/cleanup.py and tests/test_branch_cleanup.py. The controller product checkout predates these files, so the mandatory context diagnosis supplies exact installed-source evidence; the worker must inspect its current task source.

## Log

- 2026-09-11T05:48:05+00:00 approved (operator: observed RC20 cleanup CPU stall during authorized reopened Phase05 stabilization)
- 2026-09-11T05:48:29+00:00 dispatched work run 20260911T054829Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2530 tokens)
- 2026-09-11T06:02:11+00:00 attempt 1 failed: worker exited 1: {'message': 'Selected model is at capacity. Please try a different model.'}; will retry
- 2026-09-11T06:02:30+00:00 dispatched work run 20260911T060230Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2530 tokens)
- 2026-09-11T06:13:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T06:24:43+00:00 opened https://github.com/joshmarcus/context-garden/pull/488 (base main): Implemented a fresh one-pass recovery-reference index while retaining exact literal boundary semantics and all branch deletion guards. Focused cleanup tests, scheduler regressions, Ruff, the requested scale benchmark, and independent review passed on commit 9e2b01c8. cost=$1.08
- 2026-09-11T06:35:56+00:00 automated review: approve — The bounded matcher preserves prior Staff Reyn exact-boundary behavior and cleanup guards. Exact-head CI remains a controller-enforced pending merge gate. cost=$0.26
- 2026-09-11T06:47:01+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T06:52:27+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/488
