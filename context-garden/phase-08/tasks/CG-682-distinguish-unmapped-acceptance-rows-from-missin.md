---
id: CG-682
title: Distinguish unmapped acceptance rows from missing evidence
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 2
difficulty: medium
reading:
- context-garden/phase-08/goals.md
- src/garden/criteria.py
- src/garden/review.py
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T17:06:27+00:00'
---

## Goal

Correct generated acceptance summaries so absent structured row mappings are not automatically presented as an absence of verification. Reference accepted narrative evidence, attestations or justified amendments where available, while keeping genuinely unmet criteria and contradictory evidence visible. Use the preserved CG-628 record as a rendering regression; do not invent mappings or rerun accepted implementation solely to improve presentation. File as a frozen Phase 08 draft.

## Context

A follow-up carried into phase-08 by the context-garden/phase-07 retro verdict.

## Acceptance criteria

- [ ] Distinguish an unmapped structured acceptance row from absent or failing verification. Link or summarize credible accepted narrative evidence and justified amendments where available.
- [ ] Preserve honest missing/contradictory evidence and failed outcomes; do not fabricate verification or reopen accepted implementation solely to fill a display field.
- [ ] Exercise the actual rendering path with a CG628-shaped narrative-rich/unmapped result and genuine missing/failing controls, using proportionate evidence.

## Planning boundary

Retrospective draft in frozen Phase08; no implementation approval, runtime activation, private-data access, new workers or spending is implied. Address each outcome with meaningful observations; alternate evidence and reasoned criteria amendments are welcome. Preserve substantive findings and avoid process-only author rounds.
