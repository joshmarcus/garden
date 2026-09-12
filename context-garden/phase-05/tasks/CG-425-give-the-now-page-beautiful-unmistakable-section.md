---
id: CG-425
title: Give the Now page beautiful, unmistakable section hierarchy
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading:
- context-garden/phase-05/specs/now-page.md
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
- src/garden/web/templates/now1.html
- src/garden/web/templates/_now1_head.html
- src/garden/web/templates/_now1_next.html
- src/garden/web/templates/_now1_where.html
branch: garden/cg-425-give-the-now-page-beautiful-unmistakable-section
pr: https://github.com/joshmarcus/context-garden/pull/338
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T19:19:28+00:00'
created: '2026-09-08T11:22:11+00:00'
updated: '2026-09-09T03:42:32+00:00'
---

# Goal
Make the Now page feel beautifully composed and easy to scan, with section headings that clearly announce where each area begins.

## Owner feedback
2026-09-08: The “Next” and “WHERE WE ARE” headings are easy to miss. They may need larger or bolder type, and the different areas may need more visual division. “Whatever is beautiful on the page … do something beautiful here.”

## Design direction
Start with the existing Now page at `/now1`, where “Where we are” is currently a small eyebrow in the region header, and consider the page as a whole. Give the implementer substantial visual latitude: typography, weight, scale, spacing, rules, contrast, background treatment or another coherent solution may establish the hierarchy. Choose what belongs in the existing botanical/editorial design; do not mechanically add boxes or make every label loud. The intended outcome matters more than a prescribed CSS technique.

## Acceptance criteria
- [ ] “Next” and “Where we are” are immediately recognizable as major sections when scanning the page, with a clear relationship between section heading, supporting label and content.
- [ ] The main areas have an intentional visual rhythm and enough separation to feel distinct while forming one beautiful page. The chosen treatment fits the existing visual language and preserves readable, accessible hierarchy.
- [ ] The design remains composed at desktop and phone widths and in light and dark appearances; inspect the affected page at representative populated and sparse states, preserve its controls and information, and report any material limitation. Existing inspectable captures and equivalent meaningful visual verification are acceptable; missing artifact metadata alone is advisory.

## Scope
A focused visual hierarchy/composition pass on the Now page. No new data, scheduler behavior or unrelated page redesign. The designer may adjust surrounding spacing and typography when necessary for the whole composition.

## Log

- 2026-09-08T11:22:44+00:00 Owner requested a design task for stronger Next/Where-we-are headings and beautiful section division; implementation technique intentionally left open.
- 2026-09-08T12:28:59+00:00 approved (web)
- 2026-09-08T19:19:28+00:00 dispatched work run 20260908T191928Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~17227 tokens)
- 2026-09-08T19:27:18+00:00 opened https://github.com/joshmarcus/context-garden/pull/338 (base main): Strengthened the Now page's editorial section hierarchy with semantic headings, restrained rules, and responsive spacing while preserving all live content and controls. Committed as fad448f511063b9bd3486096788684061a748985. cost=$0.69
- 2026-09-09T00:36:08+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/338
- 2026-09-09T03:42:32+00:00 automated review could not start: CG-425 is done: #338 was merged at 00:36:08
