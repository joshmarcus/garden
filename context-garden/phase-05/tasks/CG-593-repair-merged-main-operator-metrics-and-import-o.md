---
id: CG-593
title: Repair merged-main operator metrics and import-order regressions
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-536
- CG-516
kind: bug
priority: 0
difficulty: medium
reading:
- src/garden/runner/local.py
- src/garden/events.py
- tests/test_now1_design.py
branch: garden/cg-593-repair-merged-main-operator-metrics-and-import-o
pr: https://github.com/joshmarcus/context-garden/pull/457
runner: remote
discovered_from: CG-516
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T18:12:44+00:00'
created: '2026-09-10T17:34:18+00:00'
updated: '2026-09-10T18:31:35+00:00'
---

## Goal

Restore passing CI on accepted main after the CG-536 operator-cost payload expansion and the CG-516 conflict rebase, preserving the corrected accounting and workload-identity/sandbox behavior.

## Observed failures

Main CI34506319516 at5b481b7c01c91762df4f20c91d9010e87d0eede0 fails exactly tests/test_now1_design.py::test_metrics_count_exact_head_ci_states_without_dropping_existing_totals: the test expects the old two-field operator dictionary, while the accepted metrics contract includes priced/unpriced and unattributed-coverage fields (2560 passed,1 failed). CG528 actual CI34507460167 inherits the same single failure with2604 passed. Update that stale contract assertion precisely while retaining exact-head CI counts and meaningful coverage assertions; do not remove new coverage fields or weaken unknown-price accounting.

Main CI34507795714 atbcc8419c2dde10ff022621a8a73d37bebdb8d1bc and CG516 exact-head CI34507718299 at01766a88918b738ce8ed42c31ca030090e8af557 fail Ruff I001 atsrc/garden/runner/local.py:4: the ..workload_identity import was placed after the .base import block during conflict resolution. This is an import-order correction, not a new runner implementation.

## Acceptance criteria

- [ ] Reproduce both recorded failures against current accepted source before correcting the stale test expectation and the unsorted import. Preserve original CI links and source identities.
- [ ] Preserve CG536's operator/cohort/unpriced data contract, actual exact-head CI counting, and CG516/518 workload-identity delivery, pre-persistence redaction, supervisor output ownership and sandbox behavior. Keep the diff limited to the demonstrated integration regression.
- [ ] Run the affected Now metrics/design tests and repository Ruff sequentially; obtain passing actual current-head full CI and independent review. Report all failures and exact tested source. Do not claim a clean release from a passing focused test alone.
- [ ] Use portable code/test expectations for Linux, macOS and Windows through WSL; explicitly state untested native platforms. No deployment, live fleet change, target waiver or historical acceptance rewrite is part of this repair.

## Closing account

CG537 is being authored through a manual external context worktree. Its report must record these post-merge failures and the eventual repair source before recommending release. Do not edit CG537, restart its run or rewrite any original review report.

owner_request_key: main-post-536-516-ci-regressions-20260910

## Log

- 2026-09-10T17:34:19+00:00 approved (delegated operator verified real main CI failures)
- 2026-09-10T17:38:19+00:00 dispatched work run 20260910T173819Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~21955 tokens)
- 2026-09-10T17:41:09+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:43:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/457 (base main): Reproduced both recorded failures, updated the operator metrics contract assertion, and corrected the local runner import order. Final focused tests and Ruff pass on commit 074e687cd64ccc061b55e28ae45927ed175d9ed4. cost=$0.03
- 2026-09-10T17:47:11+00:00 automated review: approve — The narrowly scoped changes correctly repair both merged-main regressions without altering production behavior. Exact-head full CI remains in progress and must pass before merge. cost=$0.39


## Newly exposed integrated CI failures, 2026-09-10T17:51Z

After the initial two corrections, fullCI34509734223 reports2622passes and two failures: missing workload_identity.py in the architecture map, and the sandbox final-publication test asserting the obsolete literal cp command instead of the accepted supervisor-owned output channel. Include these concrete integrated-main regressions in this same repair, preserving security/result-delivery behavior and validating it with actual executable evidence.
- 2026-09-10T17:51:26+00:00 triage: changes requested by hand: Preserve the approved metrics contract and import-order corrections at074e687c. Actual fullCI34509734223 now exposes two
- 2026-09-10T17:53:51+00:00 dispatched revise run 20260910T175351Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~23080 tokens)
- 2026-09-10T18:06:58+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:08:26+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/457: Committed integrated repair 5116fda1694233fdce685d385380d58ffe8f47db. Focused sandbox/runner, workload-identity, Now design/metrics, and architecture checks plus Ruff pass; fresh current-head full CI and independent review remain for the scheduler/PR gate. cost=$0.86
- 2026-09-10T18:12:21+00:00 automated review requested changes: The integration repairs are correct and narrowly scoped, with no code defect found. Exact-head full CI remains in progress, leaving an explicit frozen acceptance criterion unmet. cost=$0.50
- 2026-09-10T18:12:44+00:00 dispatched revise run 20260910T181243Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~23241 tokens)
- 2026-09-10T18:28:27+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:29:56+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/457: Validated repair head 5116fda1694233fdce685d385380d58ffe8f47db: focused integration tests (46 passed), repository Ruff, and the supervised full pytest suite (exit 0) pass. Existing independent review on this same head found no code defect; native macOS and Windows were not exercised. cost=$0.67
- 2026-09-10T18:31:26+00:00 automated review: approve — The narrowly scoped patch repairs all four integrated regressions while preserving the expanded metrics and supervisor-owned sandbox result path. cost=$0.23
- 2026-09-10T18:31:35+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/457
