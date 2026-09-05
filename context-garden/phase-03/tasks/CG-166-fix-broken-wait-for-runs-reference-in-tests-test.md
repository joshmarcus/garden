---
id: CG-166
title: Fix broken wait_for_runs reference in tests/test_retro.py on main
status: cancelled
product: context-garden
phase: phase-03
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/web/app.py
- src/garden/model.py
- src/garden/cli.py
discovered_from: CG-148
created: '2026-09-05T04:07:45+00:00'
updated: '2026-09-05T04:16:09+00:00'
---

`tests/test_retro.py::test_retro_waits_for_every_persona_report_before_reconciling` calls `wait_for_runs(sched)` but that helper no longer exists in `tests/conftest.py` — confirmed broken on `origin/main` itself (not introduced by this branch), most likely because CG-152's in-process-runner refactor removed `wait_for_runs` (a run now finishes synchronously inside `tick()`) while CG-145's retro work landed in parallel and still called it. Both `pytest` and `ruff` fail on this line. Fix is likely just deleting the call, matching the pattern already used elsewhere (e.g. `tests/test_discovered_kinds.py`), but should be checked against what the retro test is actually asserting at that point.

## Provenance

Discovered by CG-148 (A frozen or closed phase refuses approvals and dispatch; a freeze is a phase state, not a note) during run `20260905T040214Z-revise`.

## Log

- 2026-09-05T04:07:45+00:00 discovered by CG-148
- 2026-09-05T04:16:09+00:00 already fixed by hand: PR #104 (merged 04:12Z) removed the wait_for_runs call; three workers found the same red main
