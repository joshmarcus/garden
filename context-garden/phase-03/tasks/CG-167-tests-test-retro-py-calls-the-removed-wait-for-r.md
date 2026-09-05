---
id: CG-167
title: tests/test_retro.py calls the removed wait_for_runs helper; main's tests and lint are red
status: cancelled
product: context-garden
phase: phase-03
depends_on: []
priority: 1
difficulty: easy
reading: []
discovered_from: CG-154
created: '2026-09-05T04:10:01+00:00'
updated: '2026-09-05T04:16:09+00:00'
---

CG-145 (merged as PR #98) added `test_retro_waits_for_every_persona_report_before_reconciling`, which calls `wait_for_runs(sched)` at `tests/test_retro.py:287`. CG-152 (PR #100) removed that helper from `tests/conftest.py` because workers now run in process and a dispatching tick also finishes the run. On main the test fails with NameError and `ruff check` reports F821. Fix: delete the `wait_for_runs(sched)` line (the following `sched.tick()` reaps the finished run). Until this lands every open PR's tests and lint checks fail.

## Provenance

Discovered by CG-154 (Trust at the edges: PR feedback only from trusted authors, a scrubbed worker environment, sanitised HTML and an origin check on POSTs) during run `20260905T040535Z-revise`.

## Log

- 2026-09-05T04:10:01+00:00 discovered by CG-154 (blocking)
- 2026-09-05T04:16:09+00:00 already fixed by hand: PR #104 (merged 04:12Z) removed the wait_for_runs call; three workers found the same red main
