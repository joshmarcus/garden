---
id: CG-502
title: Find redundant or low-value expensive tests
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- pyproject.toml
- tests/conftest.py
- .github/workflows/ci.yml
- docs/architecture.md
branch: garden/cg-502-find-redundant-or-low-value-expensive-tests
pr: https://github.com/joshmarcus/context-garden/pull/419
attempts: 1
last_dispatched_at: '2026-09-10T10:50:14+00:00'
created: '2026-09-10T02:36:47+00:00'
updated: '2026-09-10T11:22:12+00:00'
---

## Goal

Find expensive tests whose additional regression value is low or duplicates other coverage. Produce a prioritized, evidence-backed plan to reduce validation cost while preserving meaningful correctness checks.

## Context

Owner request: find redundant or low value expensive tests. Examine the current suite rather than assuming slow tests are useless. Include cost from repeated invocation across worker checks, review validation and CI, fixture setup/teardown, subprocess/browser startup and unnecessary sleeps or repeated full-suite runs. Coordinate with CG426 default-suite stress separation, CG441 bounded runner regression and CG468/CG469 nested validation recovery; do not duplicate completed fixes.

## Acceptance criteria

- [ ] Inventory test and fixture costs from recent real CI/validation duration data, supplementing gaps with bounded representative measurements. Record source head, environment, repetitions, wall time and available CPU/memory or setup cost. Distinguish one slow outlier from repeatably expensive behavior and report missing data honestly. Estimate aggregate recurring cost from actual invocation frequency, with explicit assumptions.
- [ ] For each leading candidate, explain the behavior and failure mode it protects, why its marginal value may be low, and which other test or proposed cheaper check preserves that protection. Identify duplication, overbroad integration setup, implementation-mirroring assertions, cosmetic or source-text assertions, polling/sleep costs and repeated equivalent scenarios. Do not rank only by runtime or use line coverage alone as proof of redundancy.
- [ ] Produce a concise ranked report with evidence, estimated savings, confidence, correctness risk and recommended action: retain, consolidate, narrow, replace, move to an explicit optional suite, or remove. Include useful expensive tests that should be retained and explain why. Link each recommendation to concrete test/fixture locations and deduplicate related existing tasks.
- [ ] Validate the highest-value recommendations with a bounded disposable experiment where useful: compare equivalent before/after behavior and runtime, and demonstrate that representative known regressions still fail the replacement coverage. Avoid expensive broad mutation campaigns or extra full-suite repetitions without a specific question to answer.
- [ ] File focused follow-up tasks for worthwhile changes, with the preserved coverage contract and supporting evidence. This task is an audit and recommendation, not permission to delete or disable tests merely to improve timings or make failing CI green. Preserve original failures and applicable exact-head release/merge checks.
- [ ] Use configurable paths and portable measurement methods on Linux, macOS and Windows through WSL. Report environments actually measured, limits, uncertainty and untested platforms. Run experiments in disposable fixtures and avoid disrupting active workers or live workloads.

## Log

- 2026-09-10T03:08:55+00:00 approved (delegated operator reviewed owner-requested draft during Inbox sweep)
- 2026-09-10T10:50:14+00:00 dispatched work run 20260910T105011Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17646 tokens)
- 2026-09-10T10:58:33+00:00 discovered work filed: CG-509, CG-510, CG-511, CG-512
- 2026-09-10T10:58:33+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T10:59:47+00:00 opened https://github.com/joshmarcus/context-garden/pull/419 (base main): Produced a ranked, evidence-backed validation-cost audit using recent two-run AWS suite data and two bounded current-head WSL repetitions. Identified four follow-ups while retaining expensive tests with unique correctness value; committed as 3151e7f6 and verified lint and diff checks. cost=$1.18
- 2026-09-10T11:01:01+00:00 automated review: approve — The audit provides a well-supported, risk-aware ranking of validation-cost reductions without weakening the suite in this PR. cost=$0.31
- 2026-09-10T11:22:12+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/419
