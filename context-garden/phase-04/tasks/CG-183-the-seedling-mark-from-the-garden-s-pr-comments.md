---
id: CG-183
title: The seedling mark from the garden's PR comments sits left of the wordmark in the web header, and
  is the favicon
status: ready
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
created: '2026-09-05T10:03:57+00:00'
updated: '2026-09-05T10:31:14+00:00'
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
