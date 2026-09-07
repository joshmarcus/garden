---
id: CG-371
title: Fix phase and runs narrow layout overflow
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/walkthrough.py
- tests/test_walkthrough.py
discovered_from: CG-326
created: '2026-09-07T05:14:12+00:00'
updated: '2026-09-07T09:13:20+00:00'
---

The strict capture check now exposes existing responsive overflow on seeded phase and runs pages: phase scrollWidth 898px and runs scrollWidth 646px at a 390px content viewport. Address those page-layout defects separately from the capture mechanism.

## Provenance

Discovered by CG-326 (Fix the Edge capture recipe for 390-wide captures: frame the page in a 390 px iframe) during run `20260907T050248Z-revise`.
## Log
- 2026-09-07T05:14:12+00:00 discovered by CG-326
- 2026-09-07T09:13:20+00:00 Duplicate of CG370/PR267, merged77169d7; exact Phase/Runs overflow fixed and CG326 subsequently passed56/56 captures.
