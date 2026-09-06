---
id: CG-308
title: 'Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where
  the phase is, and the last period'
status: in_review
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
branch: garden/cg-308-build-now-1-at-now1-from-the-fable-design-live-v
pr: https://github.com/joshmarcus/context-garden/pull/218
harness: claude
model: claude-fable-5-1
attempts: 2
last_dispatched_at: '2026-09-06T06:17:04+00:00'
created: '2026-09-06T00:53:25+00:00'
updated: '2026-09-06T07:19:24+00:00'
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

- [ ] The worker looked at its own page: captures at 1280 and 390, light and dark, taken with the Edge recipe in the product overview, read back and iterated on, and listed in the PR; the design departs from the spec's layout wherever it has a better idea and says why (owner, 2026-09-06 03:40Z: new and beautiful ideas, not the prescription followed precisely).

- [ ] The last-period region also shows hand merges, rebase rounds per merge split into mechanical and agent, and the operator's spend and share of the total from the operator ledger, so the phase's definition-of-done numbers read from the Now page (owner, 2026-09-06 03:55Z).

## Log

- 2026-09-06T00:53:26+00:00 approved (cli)
- 2026-09-06T00:57:47+00:00 operator: back to draft until both designs are on main under their final names (now-1, now-2); approved again then
- 2026-09-06T02:14:26+00:00 approved (cli)
- 2026-09-06T02:48:48+00:00 also found by CG-307 (Design the Now page: information architecture, visual system, motion, and a static mock of every state) during run `20260906T022844Z-revise`
- 2026-09-06T02:58:27+00:00 dispatched work run 20260906T025753Z-work via local [claude model=claude-fable-5-1] (fresh session, base garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1 stacked on CG-307, ~29307 tokens)
- 2026-09-06T03:40:39+00:00 opened https://github.com/joshmarcus/context-garden/pull/218 (base garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1): Now 1 is built at /now1 from Fable's design: the four regions rendered from a new now1 module, live over a server-sent-events stream that never holds the hub lock, a browser clock on every running card, the difficulty-by-model tables computed in events.metrics with heat-map shading, garden now --page 1 and a walkthrough capture. Full suite and lint pass. cost=$18.47
- 2026-09-06T03:42:28+00:00 automated review requested changes: The implementation is broadly complete and its focused tests pass, but two explicit acceptance criteria remain unmet: all numeric tables must follow the row-based heat-map convention, and four compliant screenshots must be inspected and listed. cost=$0.70
- 2026-09-06T03:48:06+00:00 dispatched revise run 20260906T034805Z-revise via local [claude model=claude-fable-5-1] (fresh session, base garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1, ~26896 tokens)
- 2026-09-06T04:28:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/218: The runs-by-harness-and-model table is now a per-row heat-map table computed in the now module and rendered by the same macro as the difficulty tables; the four captures of the live page at 1280 and 390, light and dark, were taken, read back, iterated on (a phone overflow and a too-narrow column fixed) and filed under docs/screenshots; the merge queue's round limit reads the scheduler's default. cost=$9.81
- 2026-09-06T04:34:42+00:00 automated review requested changes: The Now 1 implementation is otherwise broad and well tested, including live updates, clocks, shaded tables, text output, and responsive captures. It cannot merge because the last-period region omits required hand-merge, rebase-round, and operator-spend metrics. cost=$1.11
- 2026-09-06T04:45:49+00:00 dispatched revise run 20260906T044547Z-revise via local [claude model=claude-fable-5-1] (fresh session, base garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1, ~27583 tokens)
- 2026-09-06T05:37:05+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/218: The last-period region now shows hand merges, rebase rounds per merge split into mechanical and agent, and the operator's spend and share, computed in the now1 module from the window's events and the operator ledger, worded once for the page and garden now, tested, and recaptured at both widths in both themes. cost=$7.29
- 2026-09-06T05:37:58+00:00 PR conflicts with garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1; rebase onto garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1 conflicts (src/garden/events.py); a rebase agent will resolve it
- 2026-09-06T05:41:25+00:00 dispatched rebase run 20260906T054112Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1, conflict only; easy tier, ~11182 tokens)
- 2026-09-06T06:16:05+00:00 attempt 1 failed: no GARDEN_RESULT in worker output (see final.md); will retry
- 2026-09-06T06:17:04+00:00 dispatched work run 20260906T061702Z-work via local [claude model=claude-fable-5-1] (fresh session, base garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1 stacked on CG-307, ~28340 tokens)
- 2026-09-06T06:57:29+00:00 attempt 2 failed: no GARDEN_RESULT in worker output (see final.md); giving up
- 2026-09-06T07:19:24+00:00 operator: the fresh work run was a load casualty; PR #218 carries the build; back to review so the queue rebases it once the design merges
