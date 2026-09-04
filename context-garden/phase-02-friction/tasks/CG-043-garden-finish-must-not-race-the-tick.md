---
id: CG-043
title: garden finish must not race the tick
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/cli.py
- src/garden/runner/manual.py
branch: garden/cg-043-garden-finish-must-not-race-the-tick
pr: https://github.com/joshmarcus/context-garden/pull/28
attempts: 1
last_dispatched_at: '2026-09-04T17:38:14+00:00'
created: '2026-09-04T17:09:28+00:00'
updated: '2026-09-04T18:06:17+00:00'
---

## Goal

A manual run that is being finished is never mistaken for a missing run by a concurrent tick.

## Context

During CG-027, `garden finish CG-027` marked the manual revise run `done` and wrote `exit_code`, then ran the pre-PR checks (about 20 seconds of pytest). A `garden serve` tick fired inside that window, found the task `running` with no run in `running` status, and logged "no active run found; back to ready" (`reap`, the first guard). Finish's own `finalize` then wrote `changes_requested` over that from its stale in-memory task, so the log carries both lines and the state depended on who saved last. Either finish should keep the run `running` until finalize has transitioned the task (write `exit_code` last), or the tick should skip tasks whose latest run has `runner: manual` and no `finished_at`, or finish should hold a lock the tick respects. The same window exists for detached runs between `exit_code` appearing and the reap, but there the reaper is the only writer.

## Acceptance criteria

- [ ] a tick during `garden finish` leaves the task's status alone.
- [ ] a test: start a manual run, mark it finished the way finish does, run a tick before finalize, assert no transition.
- [ ] the task log shows one transition for the finish, not two.

## Out of scope

- Locking between two ticks; see the architecture note on overlapping ticks.

## Provenance

Filed by hand during CG-027 after `garden finish` had already opened its PR.

## Log

- 2026-09-04T17:23:55+00:00 approved (web)
- 2026-09-04T17:38:14+00:00 dispatched work run 20260904T173813Z-work via local [claude model=sonnet] (fresh session, base main, ~2577 tokens)
- 2026-09-04T17:55:57+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/28 (base main): Fixed the race between `garden finish` and a concurrent tick by making `Scheduler.reap()` skip manual runs entirely. The tick now returns False immediately when the latest run has `runner=="manual"`, so neither of the two race windows (exit_code written before finalize, or run saved as done before task transition) can cause a spurious status revert. Added a test that writes exit_code the way `ManualRunner.finish` does, fires a tick, and asserts no transition occurs. cost=$3.67
- 2026-09-04T17:58:11+00:00 automated review: approve — Fix is correct and minimal: returning False early in reap() for manual runs eliminates both race windows. Test covers window 1 explicitly; all checks pass. cost=$0.24
- 2026-09-04T18:06:17+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/28
