---
id: CG-530
title: Add Last week to Now and share its cost graphs on Costs
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-536
  after: merge
priority: 1
difficulty: medium
reading:
- src/garden/now1.py
- src/garden/costs.py
- src/garden/charts.py
- src/garden/web/pages/now1.py
- src/garden/web/pages/costs.py
- src/garden/web/templates/_now1_period.html
- src/garden/web/templates/costs.html
branch: garden/cg-530-add-last-week-to-now-and-share-its-cost-graphs-o
pr: https://github.com/joshmarcus/context-garden/pull/461
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T18:48:56+00:00'
created: '2026-09-10T12:56:25+00:00'
updated: '2026-09-10T19:05:36+00:00'
---

## Goal

Add a Last week period to the Now cost graphs and make Now's cost visualizations available on the Costs page, using shared calculation and rendering so the two views agree for equivalent filters.

## Context

Owner request: "Can we add a last week to the now cost graphs? Can we bring the now cost graphs to Costs?" Now currently offers last hour, today, last 24 hours and this phase. Costs already has a 7d option and a spend-over-time chart, but does not expose the same complete cost-comparison presentation as Now. Reuse existing chart and table components; do not add a redundant second copy of the existing Costs time-series graph. Coordinate with CG-351's completed cost comparison work and any accepted-task cohort/pricing fixes.

## Acceptance criteria

- [ ] Add Last week to Now as a clearly described rolling seven-day window, using consistent UTC boundaries and suitable daily buckets. The selected period survives full-page and partial refreshes, links and applicable CLI/text views.
- [ ] Bring Now's cost-by-activity and harness/model/difficulty cost comparison visualizations to Costs through shared components or helpers, preserving the useful existing Costs controls and breakdowns. Equivalent windows, filters and grouping produce matching values, legends and sample counts across the views.
- [ ] Make the Costs window label Last week consistent with Now and retain existing query compatibility, other ranges and deep links. Every displayed comparison must make its selected cohort clear and honor applicable filters; unknown pricing must not become a confidently displayed zero.
- [ ] Keep empty, sparse and operator-only data meaningful. Preserve accessible labels, readable light/dark rendering and the existing mobile/desktop layout without overflow or duplicate chart sections.
- [ ] Verify seven-day boundaries, refresh selection, equivalent Now/Costs data and filter behavior with focused tests and inspect representative rendered pages at desktop and narrow widths. Keep data preparation proportionate to avoid a full-history scan for every chart refresh.

owner_request_key: owner-now-cost-week-and-costs-20260910


Build presentation on CG-536's accepted shared cohort/pricing contract after merge; CG-536 owns calculation correctness, and this task owns the requested seven-day selector and shared charts.

## Log

- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:32:13+00:00 dispatched work run 20260910T173212Z-work-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~22295 tokens)
- 2026-09-10T17:39:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:43:14+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.71
- 2026-09-10T18:34:07+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:09+00:00 opened https://github.com/joshmarcus/context-garden/pull/461 (base main): Added the rolling seven-day Last week window to Now and shared Now's cost comparison presentation with Costs while retaining Costs controls. Focused Now/Costs tests passed (63); focused lint passed, while full lint reports one unrelated existing import-order issue in src/garden/runner/local.py.
- 2026-09-10T18:34:09+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:37:50+00:00 automated review requested changes: Last week is added correctly and the shared presentation renders, but Costs comparisons ignore the session filter and display unpriced runs as known $0.00 costs. cost=$0.40
- 2026-09-10T18:38:15+00:00 dispatched revise run 20260910T183815Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~23793 tokens)
- 2026-09-10T18:45:08+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:46:36+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/461: Fixed Costs comparison cohort filtering for sessions and made shared comparison totals/cells explicitly partial when any run lacks pricing. Verified with focused Now/Costs tests (65 passed) and `.venv/bin/ruff check src tests scripts`. cost=$0.73
- 2026-09-10T18:48:19+00:00 automated review requested changes: Last week and shared Costs comparisons are implemented, including session filtering and partial-price labeling. However, the branch breaks three existing difficulty-comparison contract tests. cost=$0.37
- 2026-09-10T18:48:56+00:00 dispatched revise run 20260910T184856Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~23543 tokens)
- 2026-09-10T18:51:37+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:54:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/461: Restored the established complete-pricing comparison cell shape while retaining explicit cost_complete:false markers for incomplete pricing. Focused Now/Costs coverage passed (77 tests), including the previously failing difficulty-comparison contracts; required lint passed. cost=$0.22
- 2026-09-10T18:57:58+00:00 automated review: approve — Last week and shared filtered cost comparisons are correctly implemented, with incomplete pricing explicitly marked partial and established comparison contracts preserved. cost=$0.41
- 2026-09-10T19:05:36+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/461
