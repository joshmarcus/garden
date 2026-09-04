---
id: CG-031
title: Draw the done stage as a red apple
status: awaiting_triage
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/plants.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
branch: garden/cg-031-draw-the-done-stage-as-a-red-apple
pr: https://github.com/joshmarcus/context-garden/pull/26
attempts: 1
last_dispatched_at: '2026-09-04T17:39:16+00:00'
created: '2026-09-04T16:44:17+00:00'
updated: '2026-09-04T17:52:15+00:00'
---

## Goal

Replace the `done` growth-stage glyph (`st-fruit`, four berries) with a red apple: one round fruit, a short stem, one leaf, drawn well enough to sit beside the other stage glyphs in the herbarium style.

## Context

The stage glyphs are inline SVG `<g id="st-...">` symbols in `src/garden/plants.py`, placed with `<use>` everywhere a task's status is shown (Inbox, Board, Trellis, task and phase pages). Colours come from CSS variables; the berries use `--berry`. The apple needs a red that reads in both the light and dark themes, so add an `--apple` variable next to `--berry` rather than hard-coding a hex colour. The glyph's title text ("in fruit") stays as it is; the botanical theme spec says the stage word is never carried by the drawing alone. Keep the 24-unit viewBox and the ink outline weight the other glyphs use.

## Acceptance criteria

- [ ] `st-fruit` is an apple: one body, a stem, a leaf, ink outline, red fill from a CSS variable.
- [ ] It renders at the same size and alignment as the other stage glyphs on the Inbox, Board and Trellis in both themes.
- [ ] The glyph's title and the `done` stage name are unchanged; tests for the plants module pass.

## Out of scope

- Changing any other stage glyph or the phase plants.

## Log

- 2026-09-04T17:23:50+00:00 approved (web)
- 2026-09-04T17:39:16+00:00 dispatched work run 20260904T173916Z-work via local [claude model=sonnet] (fresh session, base main, ~3006 tokens)
- 2026-09-04T17:46:05+00:00 discovered work filed: CG-056
- 2026-09-04T17:46:27+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/26 (base main): Replaced the st-fruit glyph (four berries) with a red apple: one round body drawn as a closed Bezier path using a new --apple CSS variable, a short stem, a leaf in var(--leaf), and a crease suggesting the apple's top groove. Added --apple (#c0383a light, #d95252 dark) to the pressed-specimen palette in base.html. All 119 tests pass, lint clean. cost=$0.96
- 2026-09-04T17:52:15+00:00 automated review: approve — All three acceptance criteria met; plants and graph tests pass cleanly. Two coordination test failures are stale-branch artifacts (CG-038 changed the scheduler API after this branch was cut) and are not caused by this PR's changes. cost=$0.40
