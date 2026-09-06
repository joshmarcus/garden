---
id: CG-307
title: 'Design the Now page: information architecture, visual system, motion, and a static mock of every
  state'
status: ready
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
harness: claude
model: claude-fable-5-1
created: '2026-09-06T00:53:24+00:00'
updated: '2026-09-06T00:53:25+00:00'
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

## Log

- 2026-09-06T00:53:25+00:00 approved (cli)
