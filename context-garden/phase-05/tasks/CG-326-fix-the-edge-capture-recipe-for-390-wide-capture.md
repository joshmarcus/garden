---
id: CG-326
title: 'Fix the Edge capture recipe for 390-wide captures: frame the page in a 390 px iframe'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/walkthrough.py
- tests/test_walkthrough.py
discovered_from: CG-308
created: '2026-09-06T04:18:52+00:00'
updated: '2026-09-06T13:20:33+00:00'
---

Edge headless on this machine has a window floor of about 496 px, so the product overview's `--window-size=390` recipe lays the page out at 496 and every phone capture looks cut off at the right (measured from the page: clientWidth 496). A local HTML file with a `<iframe src="http://localhost:PORT/page" style="width:390px;height:5400px;border:0">` captured at a 600-wide window gives a true 390 viewport (clientWidth 390, scrollWidth 390). Update the recipe in the product overview and have CG-315's check use the wrapper for its narrow captures.

## Provenance

Discovered by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) during run `20260906T034805Z-revise`.

## Log

- 2026-09-06T04:18:52+00:00 discovered by CG-308

## Operator scope clarification, 2026-09-06

The operator is correcting the garden-local product overview separately. Keep worker changes in the product worktree: make the UI capture/check path verify the actual content viewport is 390 CSS pixels. For Edge fallback, a wider outer window with a 390px iframe is an available approach, not a required implementation. Document the verified recipe in product-owned documentation. Do not edit the live garden repository.

## Acceptance criteria

- [ ] Narrow captures verify a 390 CSS pixel content viewport rather than trusting outer window dimensions; preserve light/dark captures and document evidence.
- 2026-09-06T13:20:33+00:00 approved (cli)
