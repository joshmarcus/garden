---
id: CG-168
title: Fix undefined `wait_for_runs` in test_retro_waits_for_every_persona_report_before_reconciling
status: cancelled
product: context-garden
phase: phase-03
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/retro.py
- src/garden/cli.py
- src/garden/scheduler.py
discovered_from: CG-160
created: '2026-09-05T04:14:07+00:00'
updated: '2026-09-05T04:16:09+00:00'
---

`tests/test_retro.py::test_retro_waits_for_every_persona_report_before_reconciling` calls `wait_for_runs(sched)` which is not imported or defined anywhere in the test file, causing a `NameError`. This pre-exists on `main` (confirmed independent of CG-160's change) and is presumably a leftover from the CG-152 in-process-runner migration that renamed/removed a helper. Needs a real fix, not a workaround.

## Provenance

Discovered by CG-160 (garden retro --skip-personas can dispatch reconciliation with an empty persona-reviews section) during run `20260905T040848Z-work`.

## Log

- 2026-09-05T04:14:07+00:00 discovered by CG-160
- 2026-09-05T04:16:09+00:00 already fixed by hand: PR #104 (merged 04:12Z) removed the wait_for_runs call; three workers found the same red main
