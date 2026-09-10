---
id: CG-541
title: Measure delegated effort per accepted change
status: draft
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
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

User value: judge whether unattended development saves total effort and cost. Why now: accepted stabilization and task throughput do not establish economic benefit. Size: hard. Dependencies: corrected phase/cohort accounting, CG-336/375 and existing intervention events; show owner versus operator actions, recovery causes, lead time and priced/unpriced coverage.

## Context

Proposed at the context-garden/phase-05 retro. Measure total operating effort before claiming savings or expanding model and infrastructure experiments.


## Reviewed scope and verification

Build on CG-536 after merge. Define attributable human-owner and delegated-operator actions, recovery causes, elapsed time and priced/unpriced coverage for the same accepted cohort. Preserve unavailable values and historical uncertainty; do not extrapolate savings from throughput or accepted stabilization. Reuse existing event/accounting records and verify cohort/source cutoffs with representative deterministic data.
