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
updated: '2026-09-06T02:48:48+00:00'
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

- [ ] The last-period region shows the difficulty-by-model tables (rows easy, medium, hard; a column per model that did work in the window; cells with n) for mean total cost per accepted task, work-run cost, first-pass approval, revise rounds and median lead time, with a metric picker or one compact table per metric, from the same computation as `garden metrics`, and the design chooses how they read at a glance (owner, 2026-09-06 02:30Z).

- [ ] Every running card carries a live elapsed clock that ticks in the browser from the run's start time (seconds, then m:ss, then h:mm:ss), with the typical duration for its mode and tier as a quiet filling mark and a plain "longer than usual" past it; a new card counts up from zero as it slides in; the page's clock is offset once against the server's so the figure matches the run page; a test renders a card with a start time and asserts the data attribute the clock reads (owner, 2026-09-06 02:35Z).

- [ ] Every table of numbers shades its cells within each row from a light green ground for the best value to a light red for the worst (direction per metric: lower is better for cost, revise rounds and lead time; higher for first-pass approval), cells with n under three shaded faintly and marked, legible in light and dark, with a small mark on best and worst so colour is never the only signal (owner, 2026-09-06 02:45Z).

## Log

- 2026-09-06T00:53:26+00:00 approved (cli)
- 2026-09-06T00:57:47+00:00 operator: back to draft until both designs are on main under their final names (now-1, now-2); approved again then
- 2026-09-06T02:14:26+00:00 approved (cli)
- 2026-09-06T02:48:48+00:00 also found by CG-307 (Design the Now page: information architecture, visual system, motion, and a static mock of every state) during run `20260906T022844Z-revise`
