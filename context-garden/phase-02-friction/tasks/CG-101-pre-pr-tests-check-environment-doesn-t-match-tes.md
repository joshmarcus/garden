---
id: CG-101
title: Pre-PR `tests` check environment doesn't match test suite assumptions
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
branch: garden/cg-101-pre-pr-tests-check-environment-doesn-t-match-tes
pr: https://github.com/joshmarcus/context-garden/pull/49
discovered_from: CG-090
attempts: 1
last_dispatched_at: '2026-09-04T21:15:20+00:00'
created: '2026-09-04T21:10:52+00:00'
updated: '2026-09-04T21:26:53+00:00'
---

checks.run_check() forces GARDEN_ROOT to a non-existent sentinel for every pre-PR `command` check subprocess (added by CG-082 to keep custom check scripts off the live garden). This is correct for user-authored checks but also applies to this repo's own `tests` check, which runs the pytest suite as that subprocess — so any test calling find_root() without explicitly managing GARDEN_ROOT breaks. Fixed here with an autouse conftest fixture, but worth a follow-up doc note (or a dedicated check-runner mode) so this isn't rediscovered per-task.

## Provenance

Discovered by CG-090 (State.save() never clears dirty keys after a successful write) during run `20260904T210543Z-revise`.

## Log

- 2026-09-04T21:10:52+00:00 discovered by CG-090
- 2026-09-04T21:12:38+00:00 approved (web)
- 2026-09-04T21:15:20+00:00 dispatched work run 20260904T211520Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8497 tokens)
- 2026-09-04T21:18:21+00:00 discovered work filed: CG-108
- 2026-09-04T21:18:50+00:00 opened https://github.com/joshmarcus/context-garden/pull/49 (base main): Added an autouse conftest fixture that strips ambient GARDEN_ROOT before each test, fixing find_root()-dependent tests (e.g. test_find_root_normal) that broke when the pre-PR `tests` check ran pytest with GARDEN_ROOT forced to a non-existent sentinel. Reproduced the failure before the fix and confirmed the full suite (218 passed, 3 skipped) and ruff pass after it, both normally and under the simulated check environment. cost=$1.44
- 2026-09-04T21:21:35+00:00 automated review: approve — Minimal, correct autouse conftest fixture that strips ambient GARDEN_ROOT so the pre-PR tests check's sentinel no longer breaks find_root()-dependent tests. Verified full suite passes (218/3) under the simulated check environment. cost=$0.54
- 2026-09-04T21:26:53+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/49
