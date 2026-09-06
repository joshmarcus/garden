---
id: CG-326
title: 'Fix the Edge capture recipe for 390-wide captures: frame the page in a 390 px iframe'
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- context-garden/phase-05/specs/now-page.md
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
- src/garden/web/templates/base.html
- src/garden/web/templates/board.html
- src/garden/web/templates/costs.html
- src/garden/web/templates/herbarium.html
- src/garden/web/templates/runs.html
- src/garden/web/pages/costs.py
- src/garden/web/pages/board.py
- src/garden/web/pages/trellis.py
- src/garden/charts.py
- src/garden/events.py
- src/garden/plants.py
- src/garden/scheduler/queue.py
- src/garden/web/app.py
- src/garden/web/common.py
discovered_from: CG-308
created: '2026-09-06T04:18:52+00:00'
updated: '2026-09-06T04:18:52+00:00'
---

Edge headless on this machine has a window floor of about 496 px, so the product overview's `--window-size=390` recipe lays the page out at 496 and every phone capture looks cut off at the right (measured from the page: clientWidth 496). A local HTML file with a `<iframe src="http://localhost:PORT/page" style="width:390px;height:5400px;border:0">` captured at a 600-wide window gives a true 390 viewport (clientWidth 390, scrollWidth 390). Update the recipe in the product overview and have CG-315's check use the wrapper for its narrow captures.

## Provenance

Discovered by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) during run `20260906T034805Z-revise`.

## Log

- 2026-09-06T04:18:52+00:00 discovered by CG-308
