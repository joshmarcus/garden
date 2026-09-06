---
id: CG-307
title: 'Design the Now page: information architecture, visual system, motion, and a static mock of every
  state'
status: running
product: context-garden
phase: phase-05
depends_on: []
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
branch: garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1
pr: https://github.com/joshmarcus/context-garden/pull/206
harness: claude
model: claude-fable-5-1
last_dispatched_at: '2026-09-06T02:28:45+00:00'
created: '2026-09-06T00:53:24+00:00'
updated: '2026-09-06T02:28:45+00:00'
---

## Goal

A design document and a static HTML mock for the Now page (specs/now-page.md): the layout and hierarchy of the four regions (Now, Next, Where we are, The last period) at projector and phone widths, the visual system drawn from the herbarium (plates, plant glyphs, type, colour used only for state, one accent for movement), the motion language for a run arriving, advancing, finishing and leaving and for the phase's plant growing, the empty and quiet states, and the data each element needs from the store, run records, events and metrics. The mock is rendered from real state of this garden and reviewed by the designer and usability personas; the build task (the one that depends on this) follows it.

## Context

The owner asked for an operational dashboard that is the gem of the experience and the demo, with beauty and data visualization as the point. The garden has a herbarium visual language (context-garden/phase-01-bootstrap/specs/botanical-theme.md, src/garden/plants.py, the plates), server-rendered SVG charts (src/garden/charts.py, the Costs page) and an events stream; nothing today shows what is happening now or what comes next in one place, and the Board and Inbox are for acting, not for watching. Design first, so the build has one target.

## Acceptance criteria

- [ ] docs/design/now-page.md (in the product repo) describes each region, its hierarchy, its data, its states (running, finishing, held, paused, failed, empty, quiet) and the motion for each transition, with the reasons
- [ ] A static mock at src/garden/web/static/mock/now.html (or under docs/design/) renders every region from a real snapshot of this garden's state and looks right at 1280 and at 390 wide, in light and dark
- [ ] The design names the elements that update live and the event kinds that drive each, and the metrics each number comes from, so the build needs no further design decision
- [ ] garden persona-review with the designer and usability-expert personas on this PR returns no high finding, or the PR answers each in the document
- [ ] The PR description states the design's goal and the choices made, not the process

- [ ] The last-period region shows the difficulty-by-model tables (rows easy, medium, hard; a column per model that did work in the window; cells with n) for mean total cost per accepted task, work-run cost, first-pass approval, revise rounds and median lead time, with a metric picker or one compact table per metric, from the same computation as `garden metrics`, and the design chooses how they read at a glance (owner, 2026-09-06 02:30Z).

- [ ] Every running card carries a live elapsed clock that ticks in the browser from the run's start time (seconds, then m:ss, then h:mm:ss), with the typical duration for its mode and tier as a quiet filling mark and a plain "longer than usual" past it; a new card counts up from zero as it slides in; the page's clock is offset once against the server's so the figure matches the run page; a test renders a card with a start time and asserts the data attribute the clock reads (owner, 2026-09-06 02:35Z).

- [ ] Every table of numbers shades its cells within each row from a light green ground for the best value to a light red for the worst (direction per metric: lower is better for cost, revise rounds and lead time; higher for first-pass approval), cells with n under three shaded faintly and marked, legible in light and dark, with a small mark on best and worst so colour is never the only signal (owner, 2026-09-06 02:45Z).

## Log

- 2026-09-06T00:53:25+00:00 approved (cli)
- 2026-09-06T00:55:57+00:00 dispatched trial run 20260906T005540Z-trial via local [claude model=claude-fable-5-1] (fresh session, base main, ~27815 tokens)
- 2026-09-06T00:56:13+00:00 dispatched trial run 20260906T005557Z-trial via local [codex model=gpt-6-astra] (fresh session, base main, ~27853 tokens)
- 2026-09-06T00:56:13+00:00 trial started with claude:claude-fable-5-1, codex:gpt-6-astra
- 2026-09-06T01:53:11+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply c2cc330d1e9be866075960b4e4f709250f2e8b1c` in /home/joshua/work/worktrees/CG-307-trial-claude-claude-fable-5-1 to recover them (garden:CG-307:2026-09-06T01:53:11+00:00)
- 2026-09-06T01:53:12+00:00 dispatched trial run 20260906T015311Z-trial via local [claude model=claude-fable-5-1] (fresh session, base main, ~28176 tokens)
- 2026-09-06T02:14:26+00:00 trial inconclusive (only one contender produced a PR; the trial is inconclusive, not a win); kept claude:claude-fable-5-1's PR: https://github.com/joshmarcus/context-garden/pull/206
- 2026-09-06T02:25:27+00:00 automated review requested changes: The Now 1 design and real-state mock are substantial, but required persona evidence, difficulty-by-model tables, and the live-clock contract/test are missing. The PR also includes unrelated CG-248/CG-250 changes and its description contains process narration. cost=$0.30
- 2026-09-06T02:28:45+00:00 dispatched revise run 20260906T022844Z-revise via local [claude model=claude-fable-5-1] (fresh session, base main, ~29440 tokens)
