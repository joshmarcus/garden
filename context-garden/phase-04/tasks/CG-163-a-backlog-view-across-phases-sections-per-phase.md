---
id: CG-163
title: 'A backlog view across phases: sections per phase, drag a task to reorder it or to move it to another
  phase'
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-162
- CG-182
- CG-197
priority: 3
difficulty: medium
reading:
- src/garden/web/pages/board.py
- src/garden/web/templates/board.html
- src/garden/web/actions/tasks.py
- src/garden/graph.py
- src/garden/scheduler/dispatch.py
branch: garden/cg-163-a-backlog-view-across-phases-sections-per-phase
last_dispatched_at: '2026-09-05T13:16:17+00:00'
created: '2026-09-05T03:58:24+00:00'
updated: '2026-09-05T14:33:46+00:00'
---

## Goal

One screen shows several phases of a product as stacked sections, the way a Jira backlog shows sprints. Dragging a task within a section changes its order; dragging it into another section moves it to that phase. Every drop is one request and the page keeps working without JavaScript through the existing pulldowns and buttons.

## Context

Requested by the user on 2026-09-05 during phase 03, right after CG-162 (move a task between phases). The Board already has a list view (CG-094) and a priority pulldown in words (CG-099); this is that list view with a phase selector that admits more than one phase, plus drag and drop on top of the move and priority actions. The user's own words: "maybe this is the list view if you enable multiple phases".

Design:

- The Board's phase selector becomes multi-select (all open phases of the product by default; closed phases stay in the Herbarium). Each selected phase is a section headed by its name, plant glyph and freeze marker, with its tasks as rows in dispatch order.
- Order inside a phase: `priority` stays the coarse tier in words. A new `order:` frontmatter field (an integer rank, absent means "by id") breaks ties inside a priority band, and `ready()` and `dispatch_ready` sort by `(priority, order, id)`. A drop within a section writes `order` for the moved row only, renumbering neighbours when two ranks collide, and, when the row crosses a priority band, sets `priority` to the band it landed in.
- A drop into another section calls the move from CG-162 and refuses the same cases (a run in flight, a closed phase), showing the refusal as a flash message and snapping the row back.
- Native HTML5 drag and drop, one small inline script, no library. Each drop posts to `POST /tasks/<id>/order` (new) or `POST /tasks/<id>/move` (CG-162) and swaps the affected sections through HTMX. Keyboard users get "move up", "move down" and the phase pulldown on every row; those are also the no-JavaScript path.
- Running and in-review tasks can be reordered but not moved; the row says why on hover.

## Acceptance criteria

- [ ] The Board list view can show two or more open phases of a product as sections, in phase order, with the freeze marker on frozen ones.
- [ ] Dragging a row within a section persists `order` (and `priority` when it crosses a band) with one request, and the ready set and dispatch respect that order; a test covers the sort key.
- [ ] Dragging a row into another section moves the task through the CG-162 path; the refusals from that path appear as flash messages and the row snaps back.
- [ ] Every drag action has a button or pulldown equivalent that works without JavaScript.
- [ ] Tests cover the order action, the multi-phase render and the refusal path.

## Log

- 2026-09-05T10:31:13+00:00 approved (web)
- 2026-09-05T10:31:20+00:00 priority 2 -> 3 (web)
- 2026-09-05T13:10:25+00:00 dispatched work run 20260905T131016Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~14651 tokens)
- 2026-09-05T13:16:00+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:16:17+00:00 dispatched work run 20260905T131617Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~14752 tokens)
- 2026-09-05T13:17:48+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:46+00:00 reset to ready by hand
