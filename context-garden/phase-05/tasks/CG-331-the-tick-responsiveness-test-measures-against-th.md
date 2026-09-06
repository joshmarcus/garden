---
id: CG-331
title: 'The tick-responsiveness test measures against the machine, not the clock: it fails a PR only when
  a web action waits on the tick, never because the box is busy'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- tests/test_web.py
- src/garden/web/app.py
- src/garden/scheduler/checkruns.py
created: '2026-09-06T07:19:24+00:00'
updated: '2026-09-06T13:14:39+00:00'
---

## Goal

`tests/test_web.py::test_action_and_get_stay_fast_while_a_tick_runs_a_slow_check` proves what it claims, that a web action does not wait on the tick's lock, without a wall-clock threshold that a loaded machine breaks. It asserts ordering (the action completes while the tick is provably still inside the slow check) or compares the action's latency with a baseline measured in the same process, and it is marked so a slow box skips the absolute timing rather than failing.

## Context

2026-09-06 07:09Z: Fable's Now 1 design PR (docs and a mock, no scheduler change) failed its pre-PR check on this one test, "POST waited 1.91s for the tick", with 1055 others passing, because the machine was running four other suites. It was the third time that PR was sent back for reasons that were not its own. A responsiveness test with an absolute one-second bound is a load detector, not a regression detector.

## Acceptance criteria

- [ ] The test fails when the action is served only after the tick releases its lock (a regression of CG-182) and passes on a loaded machine where everything is merely slow; a test of the test demonstrates both with a fake slow check.
- [ ] No other test in the suite asserts an absolute wall-clock bound under one second; a grep-based test enforces it.

## Log
- 2026-09-06T07:19:25+00:00 approved (cli)
- 2026-09-06T13:13:25+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:39+00:00 reset to ready by hand
