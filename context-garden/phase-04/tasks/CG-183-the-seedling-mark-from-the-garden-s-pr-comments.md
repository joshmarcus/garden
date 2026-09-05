---
id: CG-183
title: The seedling mark from the garden's PR comments sits left of the wordmark in the web header, and
  is the favicon
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/base.html
- src/garden/plants.py
- src/garden/github.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
branch: garden/cg-183-the-seedling-mark-from-the-garden-s-pr-comments
pr: https://github.com/joshmarcus/context-garden/pull/141
attempts: 1
last_dispatched_at: '2026-09-05T12:15:39+00:00'
created: '2026-09-05T10:03:57+00:00'
updated: '2026-09-05T12:47:32+00:00'
---

## Goal

The mark the garden puts on its own PR comments (`🌱 context-garden`, `github.mark_garden_comment`) appears in the web header too: a small seedling to the left of the wordmark in the upper left, drawn in the herbarium's line style, and the same mark serves as the favicon so the tab is recognisable.

## Context

Asked by the user on 2026-09-05: "can we get the little context-garden icon we put in the PR comments to the left of the CONTEXT-GARDEN title in the upper left?" The header today is `<a class="wordmark" href="/">{{ garden_name }}<small>context garden</small></a>` in `base.html`, with no mark and no favicon. `plants.py` already has growth-stage glyphs (seed, sprout, leaf, bud, flower, fruit) as SVG symbols; GitHub comments cannot render those, which is why the comment uses the emoji. On the web the drawing is the better fit for the botanical theme (`botanical-theme.md`: plants and glyphs are drawings, copy stays plain).

## Acceptance criteria

- [ ] `base.html` renders the sprout glyph from `plants.py` (or a new seedling symbol in the same style) at about 18px to the left of the wordmark, vertically centred, with `aria-hidden` and the wordmark text unchanged; it inherits the ink colour and works in both themes.
- [ ] The same mark is served as the favicon (an SVG route or a static file, linked from `base.html`).
- [ ] A test renders a page and checks the header contains the mark and the favicon link.
- [ ] The PR comment marker is unchanged.

## Log

- 2026-09-05T10:31:14+00:00 approved (web)
- 2026-09-05T12:15:39+00:00 dispatched work run 20260905T121530Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~11358 tokens)
- 2026-09-05T12:22:23+00:00 opened https://github.com/joshmarcus/context-garden/pull/141 (base main): Added a seedling mark (the sprout growth-stage glyph) to the left of the web header's wordmark and serve the same drawing as the favicon at /favicon.svg, with a test covering both. cost=$1.10
- 2026-09-05T12:23:56+00:00 automated review: approve — The seedling mark sits left of the wordmark and serves as the /favicon.svg, drawn from one shared _SPROUT_PATHS source; all four acceptance criteria are met with a covering test, and tests and lint pass. cost=$0.58
- 2026-09-05T12:43:37+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T12:47:32+00:00 automated review: approve — Reuses the sprout glyph via a shared _SPROUT_PATHS source for a header mark and the /favicon.svg favicon; all four acceptance criteria are met with a covering test, and web tests plus lint pass. cost=$0.58
