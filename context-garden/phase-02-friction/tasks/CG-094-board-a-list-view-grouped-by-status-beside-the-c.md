---
id: CG-094
title: 'Board: a list view grouped by status beside the columns'
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: medium
reading:
- src/garden/web/templates/board.html
- src/garden/web/templates/_board.html
- src/garden/web/app.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
created: '2026-09-04T21:01:27+00:00'
updated: '2026-09-04T21:01:27+00:00'
---

## Goal

The Board offers a list orientation as well as the columns: one clean vertical list of tasks grouped by status, in the order the loop moves them, readable at a glance on a laptop screen without sideways scrolling.

## Context

Asked during the first live run. The Board is ten columns of cards; at fifty tasks it is wide, and the states a person cares about at a given moment (what needs me, what is running, what is waiting) are hard to read across columns. Add a view switch (columns | list, remembered in the query string and localStorage) and a list layout: a section per status in loop order (needs a person first: waiting, awaiting triage, changes requested, failed; then running, in review, ready, draft, done, cancelled), each with its count and growth-stage glyph in the heading, and one row per task: id, title, tier, priority, the one fact that matters for that state (the question, the PR link and review verdict, the elapsed time, the blocker), and the same actions the card offers. Empty sections collapse to a heading. The herbarium look applies (the botanical theme spec): plain type, rules between sections, the stage glyphs at the left, no new colours. The existing filters (phase, product) and the live refresh keep working in both views.

## Acceptance criteria

- [ ] a columns/list switch on the Board; the list groups tasks by status in loop order with counts, the key fact per state, and the card actions; empty states collapse.
- [ ] at 1280px wide the list view needs no horizontal scrolling; at 900px rows wrap without losing the id, title or actions.
- [ ] the choice survives navigation and the live refresh; the partial renders both views; tests for the route with each view.

## Out of scope

- Drag and drop between states.

## Log

- 2026-09-04T21:01:27+00:00 approved
