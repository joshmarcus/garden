---
id: CG-088
title: Trellis and phase page can hide completed tasks
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/trellis.html
- src/garden/graph.py
created: '2026-09-04T19:48:28+00:00'
updated: '2026-09-04T19:48:28+00:00'
---

## Goal

The Trellis page and the phase page's task table each have a "hide done" control that removes tasks that are done or cancelled, so a phase with dozens of finished tasks still shows the live structure: what is ready, running, in review, and what waits on what.

## Context

Asked during the first live run, when phase 2 had 30 done tasks and 25 open ones and the trellis had become a wall. Hide is a query parameter (`?hide=done` or `?open=1`) remembered in the page's link from the rail and the phase page; hidden tasks still count for dependencies (an open task whose only dependency is hidden shows as unblocked, with the dependency named on hover), and the SVG is re-laid out without them rather than leaving gaps. The phase page's task table gets the same toggle, with the done count shown next to it ("hide 35 done") so the total is still visible; the phase header's figures are unaffected. Default stays "show all"; the Board already filters by state and needs nothing. Remember the choice per page in the query string and in localStorage so it survives the live refresh. Consider the same control on the mermaid and json outputs of `garden trellis`.

## Acceptance criteria

- [ ] a "hide completed" toggle on the Trellis that removes done and cancelled tasks from the drawing and re-lays it out; the choice survives navigation from the rail and phase page.
- [ ] the phase page's task table has the same toggle with the hidden count, surviving the live refresh.
- [ ] dependencies on hidden tasks are still honoured and visible on hover.
- [ ] `garden trellis --open` gives the same filter on the CLI; a test for the filter.

## Log

- 2026-09-04T19:48:28+00:00 approved
