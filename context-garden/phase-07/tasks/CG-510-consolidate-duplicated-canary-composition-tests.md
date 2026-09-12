---
id: CG-510
title: Consolidate duplicated canary composition tests
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/canary.py
- tests/test_canary.py
- tests/test_qa.py
branch: garden/cg-510-consolidate-duplicated-canary-composition-tests
pr: https://github.com/joshmarcus/context-garden/pull/432
runner: remote
discovered_from: CG-502
attempts: 1
last_dispatched_at: '2026-09-10T11:52:29+00:00'
created: '2026-09-10T10:58:32+00:00'
updated: '2026-09-10T12:56:41+00:00'
file: tests/test_canary.py
error: Composition and failure-reporting assertions rerun QA and already-covered scenarios.
---

Replace the full-work reruns in `test_self_check_passes_on_the_current_build` and `test_exits_non_zero_when_a_scenario_fails` with injected QA/scenario result orchestration checks. Retain the real scripted QA journey and both real canary scenarios so CG-173 child-retarget and CG-176 pending-rollup regressions still fail. CG-502 measured the duplicated tests at 13.96–14.17s total per suite; an equivalent failure-propagation check took 0.19–0.20s.

## Provenance

Discovered by CG-502 (Find redundant or low-value expensive tests) during run `20260910T105011Z-work`.
## Log
- 2026-09-10T10:58:32+00:00 discovered by CG-502

## Acceptance criteria

- [ ] Retain one real scripted QA journey and both real canary scenarios that cover CG-173 child retargeting and CG-176 pending-rollup behavior.
- [ ] Test canary composition and nonzero failure propagation with injected QA/scenario results, without recursively rerunning the already-covered journeys.
- [ ] Preserve scenario ordering, diagnostics and exit semantics for pass, failure and malformed result cases.
- [ ] Show the two orchestration tests no longer account for the measured 13.96–14.17 seconds of duplicate work while the retained real journeys and repository lint pass.
- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:52:29+00:00 dispatched work run 20260910T115229Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~19224 tokens)
- 2026-09-10T11:56:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:59:55+00:00 opened https://github.com/joshmarcus/context-garden/pull/432 (base main): Consolidated duplicated canary composition tests and committed the change. Retained real QA/scenario coverage passes, injected orchestration checks pass, and lint is clean. cost=$0.04
- 2026-09-10T12:54:55+00:00 automated review: approve — The duplicated full-work reruns are replaced by fast injected orchestration tests while dedicated real QA and canary scenario coverage remains intact. cost=$0.21
- 2026-09-10T12:56:41+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/432
