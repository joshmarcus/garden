---
id: CG-308
title: 'Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where
  the phase is, and the last period'
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-307
priority: 1
difficulty: hard
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
harness: claude
model: claude-fable-5-1
created: '2026-09-06T00:53:25+00:00'
updated: '2026-09-06T02:14:26+00:00'
---

## Goal

The /now1 page ("Now 1" in the nav) and garden now --page 1, built to the design in docs/design/now-1.md (Fable's design from the CG-307 trial, with its mock now-1.html) and specs/now-page.md: the four regions, live updates from the events stream without a reload, the phase's plant growing as tasks land, the last-period metrics with a selectable window and annotation marks, the empty and quiet states, and a garden now text view of the same data. Read-only, thin route and template, logic in a now module (garden/now.py, or now1.py if sharing would block Now 2 landing in parallel), nothing on the tick's critical path. Now 2 (CG-309) is built in parallel from astra's design at /now2; do not touch its files, and keep shared edits (nav, events plumbing) minimal so both merge.

## Context

The owner's request of 2026-09-06: a 'what's happening now' operational dashboard that creates a real sense of movement and progress, beautiful, the page for demos and for the operator's second screen. Follows the design task it depends on; the spec is context-garden/phase-05/specs/now-page.md.

## Acceptance criteria

- [ ] /now1 shows every run in flight with task, mode, harness and model, elapsed against typical duration for its mode and tier, the worker's latest line and spend so far; a finished run stays one beat with its verdict; held merges, paused harnesses and needs-you cards are visible on the page
- [ ] The Next region lists ready tasks in the scheduler's actual dispatch order and the merge queue's heads with their state, each with the reason it is where it is
- [ ] The Where-we-are region shows the open phase's plant at its stage, done against total, a mark per goal, and the retro verdict when one exists; closed phases appear as specimens
- [ ] The last-period region offers last hour, today, 24 hours and this phase, and reports tasks merged, first-pass approval, cost by activity, cost per accepted task, runs by harness and model, and throughput, from garden metrics and run records, with annotation marks from the Costs page's source
- [ ] Live updates arrive over the existing events stream and change only the affected elements; the page never polls and never holds the hub lock; a test drives an event through the stream and asserts the DOM fragment it produces
- [ ] garden now --page 1 prints the same four regions in text; garden walkthrough captures /now1; tests cover the now module's typical-duration and window computations with the fake harness

## Log

- 2026-09-06T00:53:26+00:00 approved (cli)
- 2026-09-06T00:57:47+00:00 operator: back to draft until both designs are on main under their final names (now-1, now-2); approved again then
- 2026-09-06T02:14:26+00:00 approved (cli)
