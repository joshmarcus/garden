---
id: CG-119
title: test_happy_path_dispatch_reap_pr_merge flakes intermittently in CI
status: in_review
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
branch: garden/cg-119-test-happy-path-dispatch-reap-pr-merge-flakes-in
pr: https://github.com/joshmarcus/context-garden/pull/68
discovered_from: CG-098
attempts: 1
last_dispatched_at: '2026-09-04T22:33:18+00:00'
created: '2026-09-04T22:07:19+00:00'
updated: '2026-09-04T22:41:33+00:00'
---

Failed twice in GitHub Actions on PR #54 (assertion on DM-002 status after merge-triggered dispatch) but passes reliably locally (3 full-suite runs + 5 targeted runs, all green) and touches no code in this PR's diff. Worth a dedicated look at timing/ordering in the merge -> reap -> dispatch path in scheduler.py, possibly CI-runner-speed-dependent. May already overlap with CG-113 filed during this task's first attempt — check before filing a duplicate.

## Provenance

Discovered by CG-098 (Tests do not read the developer's GARDEN_ROOT; the check command need not unset it) during run `20260904T220015Z-revise`.

## Log

- 2026-09-04T22:07:19+00:00 discovered by CG-098
- 2026-09-04T22:08:04+00:00 approved (web)
- 2026-09-04T22:08:17+00:00 priority 1 -> 1
- 2026-09-04T22:33:18+00:00 dispatched work run 20260904T223310Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-064-make-test-feedback-triggers-revise-round-determi stacked on CG-064, ~11482 tokens)
- 2026-09-04T22:39:40+00:00 opened https://github.com/joshmarcus/context-garden/pull/68 (base garden/cg-064-make-test-feedback-triggers-revise-round-determi): test_happy_path_dispatch_reap_pr_merge flaked in CI because, with stacking enabled, DM-002 stack-dispatched onto DM-001's open PR at tick 2; the final 'DM-002 running after merge' assertion then depended on whether that stacked worker was still running at the merge tick, which lost the race on slower CI runners. Disabled stacking in this one test so the merge is what unblocks and dispatches DM-002 (matching the test's own comment); stacking keeps its coverage in test_feedback_triggers_revise_round. cost=$1.97
- 2026-09-04T22:41:33+00:00 automated review: approve — Minimal, correct test-determinism fix: disabling stacking for this one test removes the background-worker race and restores the test's stated merge→unblock→dispatch intent, with stacking coverage retained elsewhere. Target test and ruff pass; diff and description are clean. cost=$0.63
