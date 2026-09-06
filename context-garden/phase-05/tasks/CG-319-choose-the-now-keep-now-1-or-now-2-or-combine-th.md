---
id: CG-319
title: 'Choose the Now: keep Now 1 or Now 2, or combine the best aspects of both into /now, and retire
  the other page'
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-308
- CG-309
priority: 2
difficulty: medium
reading:
- context-garden/phase-05/specs/now-page.md
- src/garden/web/app.py
- src/garden/web/templates/base.html
- tests/test_web.py
created: '2026-09-06T02:40:45+00:00'
updated: '2026-09-06T13:20:32+00:00'
---

## Goal

One Now page at `/now`, chosen after the owner has lived with Now 1 (Fable's design) and Now 2 (astra's): either one of them as it stands, or a combination that takes the best aspects of each (a region, the motion, the tables, the empty states) into one page. The other page is retired: its route redirects to `/now`, its templates and helpers are removed, the nav shows one "Now", and the walkthrough captures it. The design document for the chosen page records what came from where.

## Context

The owner asked for both designs to ship as Now 1 and Now 2 (2026-09-06 01:00Z) and then said "we can also choose to combine aspects from both designs if they're good" (02:40Z). Josh delegated resolution of all attention cards to the operator on 2026-09-06. Operator decision: combine the strongest aspects of the two pages, with the selection supported by side-by-side live captures and usability evidence after both builds land. Record the chosen regions and their origins before implementation; retain both routes until that comparison is complete.

## Acceptance criteria

- [ ] The delegated choice is a combination grounded in a comparison of both landed pages. Before implementing, record the selected regions, their origins and the usability evidence supporting them; do not claim an unobserved owner preference.
- [ ] `/now` serves the chosen page; `/now1` and `/now2` redirect to it; one nav entry; the retired page's templates, routes and helpers are gone and no test references them.
- [ ] The design document at docs/design/now.md names the origin of each region and interaction; the walkthrough captures /now.

## Log
- 2026-09-06T13:20:32+00:00 approved (cli)
