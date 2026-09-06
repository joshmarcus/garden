---
id: CG-314
title: 'Design Now 2: astra''s take on the Now page, information architecture, visual system, motion,
  and a static mock of every state'
status: done
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
branch: garden/cg-314-design-now-2-astra-s-take-on-the-now-page-inform
pr: https://github.com/joshmarcus/context-garden/pull/215
harness: codex
model: gpt-6-astra
attempts: 1
last_dispatched_at: '2026-09-06T04:26:55+00:00'
created: '2026-09-06T02:06:03+00:00'
updated: '2026-09-06T05:19:02+00:00'
---

## Goal

A design document and a static HTML mock for the Now page (specs/now-page.md): the layout and hierarchy of the four regions (Now, Next, Where we are, The last period) at projector and phone widths, the visual system drawn from the herbarium (plates, plant glyphs, type, colour used only for state, one accent for movement), the motion language for a run arriving, advancing, finishing and leaving and for the phase's plant growing, the empty and quiet states, and the data each element needs from the store, run records, events and metrics. The mock is rendered from real state of this garden and reviewed by the designer and usability personas; the build task (the one that depends on this) follows it.

## Context

This is the second of two designs the owner asked for (2026-09-06): Fable designs Now 1 (CG-307), astra designs Now 2 here, and each is built by its designer as /now1 and /now2 (spec section "Two Nows"). Work from the same spec and brief as CG-307; do not read or copy its output. Name your files now-2.

The owner asked for an operational dashboard that is the gem of the experience and the demo, with beauty and data visualization as the point. The garden has a herbarium visual language (context-garden/phase-01-bootstrap/specs/botanical-theme.md, src/garden/plants.py, the plates), server-rendered SVG charts (src/garden/charts.py, the Costs page) and an events stream; nothing today shows what is happening now or what comes next in one place, and the Board and Inbox are for acting, not for watching. Design first, so the build has one target.

## Acceptance criteria

- [ ] docs/design/now-2.md (in the product repo) describes each region, its hierarchy, its data, its states (running, finishing, held, paused, failed, empty, quiet) and the motion for each transition, with the reasons
- [ ] A static mock at src/garden/web/static/mock/now-2.html (or under docs/design/) renders every region from a real snapshot of this garden's state and looks right at 1280 and at 390 wide, in light and dark
- [ ] The design names the elements that update live and the event kinds that drive each, and the metrics each number comes from, so the build needs no further design decision
- [ ] garden persona-review with the designer and usability-expert personas on this PR returns no high finding, or the PR answers each in the document
- [ ] The PR description states the design's goal and the choices made, not the process

- [ ] The last-period region shows the difficulty-by-model tables (rows easy, medium, hard; a column per model that did work in the window; cells with n) for mean total cost per accepted task, work-run cost, first-pass approval, revise rounds and median lead time, with a metric picker or one compact table per metric, from the same computation as `garden metrics`, and the design chooses how they read at a glance (owner, 2026-09-06 02:30Z).

- [ ] Every running card carries a live elapsed clock that ticks in the browser from the run's start time (seconds, then m:ss, then h:mm:ss), with the typical duration for its mode and tier as a quiet filling mark and a plain "longer than usual" past it; a new card counts up from zero as it slides in; the page's clock is offset once against the server's so the figure matches the run page; a test renders a card with a start time and asserts the data attribute the clock reads (owner, 2026-09-06 02:35Z).

- [ ] Every table of numbers shades its cells within each row from a light green ground for the best value to a light red for the worst (direction per metric: lower is better for cost, revise rounds and lead time; higher for first-pass approval), cells with n under three shaded faintly and marked, legible in light and dark, with a small mark on best and worst so colour is never the only signal (owner, 2026-09-06 02:45Z).

- [ ] The worker looked at its own page: captures at 1280 and 390, light and dark, taken with the Edge recipe in the product overview, read back and iterated on, and listed in the PR; the design departs from the spec's layout wherever it has a better idea and says why (owner, 2026-09-06 03:40Z: new and beautiful ideas, not the prescription followed precisely).

## Log

- 2026-09-06T02:08:00+00:00 filed by the operator: the astra contender of the CG-307 trial died in the /tmp outage and the trial relaunch only re-dispatched the fable side; astra designs Now 2 as its own task
- 2026-09-06T02:06:03+00:00 approved (cli)
- 2026-09-06T02:46:57+00:00 dispatched work run 20260906T024636Z-work via local [codex model=gpt-6-astra] (fresh session, base main, ~7470 tokens)
- 2026-09-06T03:10:10+00:00 worker asks: Can the runner return 1280px and 390px light/dark browser captures, designer and usability-expert persona reports, and confirmation of the supplied snapshot's metric computation provenance? cost=$9.91
- 2026-09-06T03:15:07+00:00 dispatched resume run 20260906T031506Z-resume via local [codex model=gpt-6-astra] (fresh session, base main, ~7975 tokens)
- 2026-09-06T03:34:42+00:00 opened https://github.com/joshmarcus/context-garden/pull/215 (base main): Preserved the snapshot-rendered Now 2 design and mock, added inspected Edge captures with explicit visual limitations, and updated validation evidence. Delivered for runner review; outstanding acceptance evidence is listed below. cost=$4.22
- 2026-09-06T03:35:11+00:00 triage: changes requested by hand: The owner grants the data: a real, sanitized snapshot of this garden (the same one Fable's Now 1 mock was rendered from,
- 2026-09-06T03:37:00+00:00 automated review: request_changes — Request changes: the branch explicitly lacks required phone/dark visual validation, both persona reviews, and proof that the displayed matrices use the same computation as garden metrics. Focused tests pass, but these are acceptance blockers. cost=$0.29
- 2026-09-06T03:41:24+00:00 dispatched revise run 20260906T034122Z-revise via local [codex model=gpt-6-astra] (fresh session, base main, ~9124 tokens)
- 2026-09-06T03:53:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/215: Clarified the real-snapshot field handoff while preserving the existing design. Added and inspected full-page Edge captures at 1280 and 390 in light and dark; persona verdicts and shared-metrics provenance remain outstanding. cost=$4.95
- 2026-09-06T03:55:06+00:00 automated review requested changes: The design and responsive mock are substantial and the focused checks pass, but required persona-review evidence and shared-metrics provenance remain explicitly unfinished. The PR description and capture notes also retain process narration instead of presenting a clean final artifact. cost=$0.28
- 2026-09-06T03:57:51+00:00 persona designer review: score 7/10, 3 finding(s)
- 2026-09-06T03:57:51+00:00 persona usability-expert review: score 7/10, 3 finding(s)
- 2026-09-06T04:02:53+00:00 dispatched revise run 20260906T040250Z-revise via local [codex model=gpt-6-astra] (fresh session, base main, ~9733 tokens)
- 2026-09-06T04:13:50+00:00 worker asks: Can you supply the snapshot’s generator and sanitized task/run/event inputs so I can reproduce its matrices through the shared metrics computation? cost=$8.28
- 2026-09-06T04:26:52+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply bbca90d989386ea956bb8768546059c971cc501e` in /home/joshua/work/worktrees/CG-314 to recover them (garden:CG-314:2026-09-06T04:26:52+00:00)
- 2026-09-06T04:26:53+00:00 kept 2 local-only commit(s) on `backup/20260906T042651Z-resume` before syncing to origin/garden/cg-314-design-now-2-astra-s-take-on-the-now-page-inform's head: 03f955a docs: refresh inspected Now 2 captures and validation evidence; 4b2c9ac design: clarify Now 2 recovery paths and cost cohorts
- 2026-09-06T04:26:55+00:00 dispatched resume run 20260906T042651Z-resume via local [codex model=gpt-6-astra] (fresh session, base main, ~9817 tokens)
- 2026-09-06T04:52:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/215: Completed the Now 2 design handoff with persona responses, fixed-snapshot provenance, matrix fidelity tests and inspected desktop/phone captures in both themes. All changes are committed on the assigned branch. cost=$9.67
- 2026-09-06T04:54:53+00:00 automated review: approve — The Now 2 design provides a complete, implementation-ready specification, a snapshot-backed responsive mock, inspected visual evidence, and documented responses to all persona findings. Focused tests and lint pass. cost=$0.44
- 2026-09-06T05:04:33+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-06T05:04:47+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-06T05:14:11+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-06T05:19:02+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/215
