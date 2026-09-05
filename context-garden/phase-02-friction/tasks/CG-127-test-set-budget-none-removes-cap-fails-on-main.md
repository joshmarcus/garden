---
id: CG-127
title: test_set_budget_none_removes_cap fails on main
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/config.py
discovered_from: CG-074
created: '2026-09-05T00:04:19+00:00'
updated: '2026-09-05T00:04:19+00:00'
---

`tests/test_coordination.py::test_set_budget_none_removes_cap` fails on unmodified origin/main (4d3199b) with `assert 0 == 2` on the second tick after `sched.retry(t)` — looks like retry() routes a task with an open PR into the revise/CHANGES_REQUESTED path instead of a fresh dispatch, and the second tick's revise dispatch isn't happening as the test expects. Unrelated to CG-074; worth a dedicated task.

## Provenance

Discovered by CG-074 (Reviews do not consume worker slots) during run `20260904T235956Z-revise`.

## Log

- 2026-09-05T00:04:19+00:00 discovered by CG-074
