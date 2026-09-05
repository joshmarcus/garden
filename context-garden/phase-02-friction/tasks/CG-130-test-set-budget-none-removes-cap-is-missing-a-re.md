---
id: CG-130
title: test_set_budget_none_removes_cap is missing a reap tick
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/trellis.html
- src/garden/graph.py
discovered_from: CG-088
created: '2026-09-05T00:07:34+00:00'
updated: '2026-09-05T00:07:34+00:00'
---

In tests/test_coordination.py, test_set_budget_none_removes_cap dispatches 2 tasks, calls wait_for_runs, then immediately calls sched.retry(t) for each task without an intervening sched.tick() to reap the finished runs first. The two nearly-identical tests above it (test_phase_budget_pauses_dispatch, test_set_budget_override_reloads_without_restart) both have that extra tick() call. Without it, retry() forces status back to READY but the run records are never reaped, so the following tick() dispatches 0 tasks instead of 2. Fix: add a `sched.tick()` call after `wait_for_runs(sched)` and before the retry loop, matching the pattern in the two tests above.

## Provenance

Discovered by CG-088 (Trellis and phase page can hide completed tasks) during run `20260905T000109Z-revise`.

## Log

- 2026-09-05T00:07:34+00:00 discovered by CG-088
