---
id: CG-331
title: 'The tick-responsiveness test measures against the machine, not the clock: it fails a PR only when
  a web action waits on the tick, never because the box is busy'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- tests/test_web.py
- src/garden/web/app.py
- src/garden/scheduler/checkruns.py
branch: garden/cg-331-the-tick-responsiveness-test-measures-against-th
pr: https://github.com/joshmarcus/context-garden/pull/258
attempts: 1
last_dispatched_at: '2026-09-07T04:21:40+00:00'
created: '2026-09-06T07:19:24+00:00'
updated: '2026-09-07T04:47:28+00:00'
---

## Goal

`tests/test_web.py::test_action_and_get_stay_fast_while_a_tick_runs_a_slow_check` proves what it claims, that a web action does not wait on the tick's lock, without a wall-clock threshold that a loaded machine breaks. It asserts ordering (the action completes while the tick is provably still inside the slow check) or compares the action's latency with a baseline measured in the same process, and it is marked so a slow box skips the absolute timing rather than failing.

## Context

2026-09-06 07:09Z: Fable's Now 1 design PR (docs and a mock, no scheduler change) failed its pre-PR check on this one test, "POST waited 1.91s for the tick", with 1055 others passing, because the machine was running four other suites. It was the third time that PR was sent back for reasons that were not its own. A responsiveness test with an absolute one-second bound is a load detector, not a regression detector.

## Acceptance criteria

- [ ] The test fails when the action is served only after the tick releases its lock (a regression of CG-182) and passes on a loaded machine where everything is merely slow; a test of the test demonstrates both with a fake slow check.
- [ ] Audit related responsiveness assertions for load-sensitive false positives and use deterministic ordering/barriers for synchronization contracts. Preserve separately identified measured performance budgets and benchmarks; do not add a global grep ban on timeouts or weaken actual responsiveness regression coverage. Operational page tolerance is currently4s, not a reason to replace every test deadline with4s.

## Log
- 2026-09-06T07:19:25+00:00 approved (cli)
- 2026-09-06T13:13:25+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:39+00:00 reset to ready by hand

## Web-incident retro clarification, 2026-09-06

Keep the deterministic lock-order regression objective, but do not suppress evidence of real overloaded application latency. Pair the unit check with CG-339's separate controlled served-performance workload; a loaded host can reveal an actual availability failure even when the tick lock is correct. Counterfactual: separate architectural correctness from service performance instead of dismissing slow pages as merely environmental.
- 2026-09-07T03:59:41+00:00 Prioritize as throughput fix: false timing failures waste CI/revision rounds. Remove proposed blanket grep policy; retain causal synchronization regression and separately measured performance checks.
- 2026-09-07T03:59:41+00:00 priority 2 -> 1 (web)
- 2026-09-07T04:02:46+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply 39d582ff9c0fa8a356af514f1b157cd481fe2d59` in /home/joshua/work/worktrees/CG-331 to recover them (garden:CG-331:20260907T040246Z-work:pre-dispatch, run 20260907T040246Z-work)
- 2026-09-07T04:03:16+00:00 dispatched work run 20260907T040246Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~11285 tokens)
- 2026-09-07T04:15:40+00:00 preserved uncommitted worktree changes from run 20260907T040246Z-work outside the PR: `git stash apply 9af7390cd51816fb7907ffb6239e31a6d4b82a50` in /home/joshua/work/worktrees/CG-331 (garden:CG-331:20260907T040246Z-work:reap)
- 2026-09-07T04:17:12+00:00 opened https://github.com/joshmarcus/context-garden/pull/258 (base main): Replaced wall-clock responsiveness assertions with deterministic tick barriers. Verified locally and in CI. cost=$0.08
- 2026-09-07T04:19:36+00:00 automated review requested changes: The new barrier removes the fragile wall-clock budget, but it only exercises the healthy implementation. Add the required counterfactual proving that requests remain blocked when made to share the tick lock. cost=$0.32
- 2026-09-07T04:21:40+00:00 dispatched revise run 20260907T042139Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12065 tokens)
- 2026-09-07T04:32:54+00:00 preserved uncommitted worktree changes from run 20260907T042139Z-revise outside the PR: `git stash apply a3827c1a24732e4ed8e44d60f105a16daa54712e` in /home/joshua/work/worktrees/CG-331 (garden:CG-331:20260907T042139Z-revise:reap)
- 2026-09-07T04:35:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/258: Added healthy and shared-lock counterfactual probes using deterministic barriers. Removed the obsolete sleep-based setup; focused tests, lint, and exact-commit CI pass. cost=$0.07
- 2026-09-07T04:38:20+00:00 description rewritten by the reviewer cost=$0.25
- 2026-09-07T04:40:04+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T04:41:06+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T04:47:28+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/258
