---
id: CG-119
title: test_happy_path_dispatch_reap_pr_merge flakes intermittently in CI
status: ready
product: context-garden
phase: phase-02-friction
depends_on:
- CG-064
priority: 1
difficulty: medium
reading:
- tests/conftest.py
- tests/test_cli.py
- src/garden/checks.py
- src/garden/config.py
discovered_from: CG-098
created: '2026-09-04T22:07:19+00:00'
updated: '2026-09-04T22:08:17+00:00'
---

Failed twice in GitHub Actions on PR #54 (assertion on DM-002 status after merge-triggered dispatch) but passes reliably locally (3 full-suite runs + 5 targeted runs, all green) and touches no code in this PR's diff. Worth a dedicated look at timing/ordering in the merge -> reap -> dispatch path in scheduler.py, possibly CI-runner-speed-dependent. May already overlap with CG-113 filed during this task's first attempt — check before filing a duplicate.

## Provenance

Discovered by CG-098 (Tests do not read the developer's GARDEN_ROOT; the check command need not unset it) during run `20260904T220015Z-revise`.

## Log

- 2026-09-04T22:07:19+00:00 discovered by CG-098
- 2026-09-04T22:08:04+00:00 approved (web)
- 2026-09-04T22:08:17+00:00 priority 1 -> 1
