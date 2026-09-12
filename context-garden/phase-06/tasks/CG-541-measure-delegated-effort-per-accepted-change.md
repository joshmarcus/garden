---
id: CG-541
title: Measure delegated effort per accepted change
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-536
  after: merge
- id: CG-336
  after: merge
- id: CG-375
  after: merge
priority: 2
difficulty: hard
reading:
- src/garden/costs.py
- src/garden/events.py
- src/garden/operator_spend.py
- src/garden/now1.py
branch: garden/cg-541-measure-delegated-effort-per-accepted-change
pr: https://github.com/joshmarcus/context-garden/pull/464
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T18:52:04+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T19:11:38+00:00'
---

## Goal

User value: judge whether unattended development saves total effort and cost. Why now: accepted stabilization and task throughput do not establish economic benefit. Size: hard. Dependencies: corrected phase/cohort accounting, CG-336/375 and existing intervention events; show owner versus operator actions, recovery causes, lead time and priced/unpriced coverage.

## Context

Proposed at the context-garden/phase-05 retro. Measure total operating effort before claiming savings or expanding model and infrastructure experiments.


## Reviewed scope and verification

Build on CG-536 after merge. Define attributable human-owner and delegated-operator actions, recovery causes, elapsed time and priced/unpriced coverage for the same accepted cohort. Preserve unavailable values and historical uncertainty; do not extrapolate savings from throughput or accepted stabilization. Reuse existing event/accounting records and verify cohort/source cutoffs with representative deterministic data.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:32:14+00:00 dispatched work run 20260910T173214Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16816 tokens)
- 2026-09-10T17:38:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:41:31+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.80
- 2026-09-10T18:34:14+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:16+00:00 opened https://github.com/joshmarcus/context-garden/pull/464 (base main): Added accepted-change effort accounting using the existing base-merge cohort, including owner/delegated/automated/unknown actions, recovery causes, lead time, and priced/unpriced operator and run coverage. Verified with 79 focused tests and changed-file lint; repository-wide lint has one pre-existing import-order failure also present on main.
- 2026-09-10T18:34:16+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:43:35+00:00 automated review requested changes: Accepted-cohort cost, lead-time, and incomplete-price handling are implemented, but action attribution misclassifies known human and automated actions as unknown. cost=$0.34
- 2026-09-10T18:44:03+00:00 dispatched revise run 20260910T184402Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17877 tokens)
- 2026-09-10T18:46:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:48:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/464: Corrected accepted-cohort action attribution so known owner, delegated-operator, and automated-scheduler actions are separated while genuinely unattributed legacy events remain unknown. Verified with 31 focused tests and clean repository-wide Ruff lint; committed as 78e8348f. cost=$0.61
- 2026-09-10T18:51:45+00:00 automated review requested changes: Accepted-cohort cost and lead-time accounting works, but phase/global operating actions are silently omitted from effort totals. cost=$0.40
- 2026-09-10T18:52:04+00:00 dispatched revise run 20260910T185204Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~18015 tokens)
- 2026-09-10T18:56:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:58:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/464: Accepted-change effort now includes matching phase controls and global taskless operating actions within the cohort envelope, while preserving unmatched actions as unattributed coverage. Web-emitted controls are classified as human-owner actions; committed as 882a87df. cost=$0.55
- 2026-09-10T19:00:59+00:00 automated review: approve — Delegated-effort reporting correctly combines accepted-task runs, attributed operator spend, action provenance, recovery causes, and lead time while preserving unknown time and incomplete prices. cost=$0.43
- 2026-09-10T19:08:14+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T19:11:38+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/464
