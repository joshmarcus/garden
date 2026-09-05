---
id: CG-172
title: test_retro.py has a bare NameError from the CG-152 in-process-runner rebase
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
discovered_from: CG-161
created: '2026-09-05T04:21:17+00:00'
updated: '2026-09-05T05:05:27+00:00'
---

tests/test_retro.py::test_retro_waits_for_every_persona_report_before_reconciling calls `wait_for_runs(sched)` at line 287, but that helper isn't defined/imported anywhere in the file (grep confirms). It fails with `NameError: name 'wait_for_runs' is not defined` on the base branch already, introduced in commit d08d17a (merged PR #100, the CG-152 in-process runner work) -- this predates CG-161 and CG-148. `.venv/bin/pytest -q -x` and `ruff check` both fail on this line independent of any code change. Needs a look at what the pre-rebase call intended (likely just deleting the line, per the pattern in commit 248dba5 which dropped a similar leftover `wait_for_runs` call elsewhere).

## Provenance

Discovered by CG-161 (garden plan does not check a frozen phase (only closed)) during run `20260905T041549Z-work`.

## Log

- 2026-09-05T04:21:17+00:00 discovered by CG-161
- 2026-09-05T05:05:27+00:00 already fixed by PR #104 (04:12Z)
