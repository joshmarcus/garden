---
id: CG-307
title: 'Design the Now page: information architecture, visual system, motion, and a static mock of every
  state'
status: in_review
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
last_dispatched_at: '2026-09-06T04:29:47+00:00'
created: '2026-09-06T00:53:24+00:00'
updated: '2026-09-06T07:19:24+00:00'
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

- [ ] The worker looked at its own page: captures at 1280 and 390, light and dark, taken with the Edge recipe in the product overview, read back and iterated on, and listed in the PR; the design departs from the spec's layout wherever it has a better idea and says why (owner, 2026-09-06 03:40Z: new and beautiful ideas, not the prescription followed precisely).

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
- 2026-09-06T02:55:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/206: Added the difficulty-by-model tables and the live elapsed clock to the Now 1 design and mock, re-took the snapshot from the live garden, wrote tests for the clock attributes and the tables' computation, and added a persona-review section answering the designer and usability lenses. The persona-review command itself could not be run in the worker. cost=$9.20
- 2026-09-06T02:55:05+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-307` for one more round, or review on GitHub
- 2026-09-06T03:01:55+00:00 persona usability-expert review: score 6/10, 3 finding(s)
- 2026-09-06T03:04:18+00:00 persona designer review: score 6/10, 3 finding(s)
- 2026-09-06T03:20:54+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T03:30:06+00:00 automated review: request_changes — The design is substantial and the focused checks pass, but required row-relative table shading/marks are missing, the model tables do not yet use the garden metrics computation, and the real-state mock contains a contradictory review-capacity explanation. Visual verification at the required viewport/theme combinations is also not evidenced. cost=$0.50
- 2026-09-06T03:37:50+00:00 dispatched revise run 20260906T033749Z-revise via local [claude model=claude-fable-5-1] (fresh session, base main, ~8905 tokens)
- 2026-09-06T04:04:15+00:00 fenced: worker wrote outside its worktree; the writes it made were reverted. Touched the live garden: wrote context-garden/phase-05/specs/now-page.md and 10 commit(s) [56fdbd1 garden: update task state; b8d7355 garden: update task state; 605caf8 Now page: hand merges, rebase split and operator share join the last-period numbers; 9616773 garden: update task state; 600705e Criteria naming a file or
- 2026-09-06T04:28:21+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T04:29:46+00:00 kept 39 local-only commit(s) on `backup/20260906T042939Z-revise` before syncing to origin/garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1's head: f380b4f Now 1 design: the heat-map rule, the review gates, titles first, the captures, the persona record; e3ddf78 Now 1 mock: row-relative shading, honest waiting reasons, titles first, a run link; 7dc2537 The difficulty-by-model tables computed once, in events, for garden metrics and the Now page; ae5acfc Merge branch 'main' into garden/cg-307-design-the-now-page-information-architecture-vis-trial-claude-claude-fable-5-1; 429a6b1 Merge pull request #213 from joshmarcus/garden/docs-screenshots-through-edge; 88faf74 Docs: how a worker looks at pages, screenshots through Windows Edge from WSL; 6df1a9c Merge pull request #207 from joshmarcus/garden/cg-237-the-not-logged-in-check-reads-a-worker-s-prose-a; 5818407 Merge pull request #209 from joshmarcus/garden/cg-310-worker-temp-files-live-on-disk-and-are-pruned-tm; f8fd072 Make terminal storage cleanup resilient; fc73206 Keep temp directories isolated; 46662a0 Route worker temp files to work storage; 32040a2 Replay discarded persona outputs in auth tests; f5edbb6 Ignore auth markers in parsed worker results; 6e3d802 Narrow auth detection to CLI output; b240f29 Merge pull request #201 from joshmarcus/garden/cg-292-every-status-write-goes-through-transition-sched; 076a59b Preserve approval gates in status transitions; 66648eb Restore review-card done escape hatch; 3157966 Route task status writes through transitions; 00f7129 Merge pull request #204 from joshmarcus/garden/cg-249-garden-dispatch-id-cli-allows-dispatching-a-draf; 17a35b0 Merge pull request #196 from joshmarcus/garden/cg-244-reserve-retro-task-ids-and-survive-duplicate-rec; b70f1dd Merge pull request #205 from joshmarcus/garden/cg-236-a-trial-winner-s-pr-enters-the-review-queue-on-i; 99b4779 Merge remote-tracking branch 'origin/main' into garden/cg-244-reserve-retro-task-ids-and-survive-duplicate-rec; f3be704 Merge pull request #200 from joshmarcus/garden/cg-291-each-worker-gets-a-private-harness-config-dir-ho; c88701a Merge pull request #198 from joshmarcus/garden/cg-251-cost-per-accepted-task-and-first-pass-approval-p; 7cfcda6 Merge pull request #202 from joshmarcus/garden/cg-245-isolate-planner-execution-from-operator-state; bb35fc4 Merge pull request #194 from joshmarcus/garden/cg-243-preserve-task-actions-across-concurrent-ticks-an; e25913a CG-236: leftover changes from worker run 20260906T004649Z-work; 5ef80c7 garden dispatch checks the approve gate before starting work on a draft; 570ebad CG-245: cover the synchronous kickoff path and update the isolation docs; 0a53f53 CG-245: run the planner and synchronous kickoff in a scratch, worker-scrubbed environment; 9c859cb CG-291 preserve live fence state updates; 60d54c7 Attribute accepted task support costs; a49b584 CG-291 cover harness config fence targets; 6141835 CG-291 isolate harness config and fence garden writes; d3cf321 Add accepted-task cost outcomes; 163d31e Let the planner allocate ids under the reservation lock; 03f5c64 Test id reservations and duplicate quarantine; document the ledger; dba76e9 Merge task-file saves under a lock instead of clobbering the whole file; b8f4981 Reserve retro draft ids durably and quarantine duplicate task ids
- 2026-09-06T04:29:47+00:00 dispatched revise run 20260906T042939Z-revise via local [claude model=claude-fable-5-1] (fresh session, base main, ~10269 tokens)
- 2026-09-06T04:45:08+00:00 revision failed: no GARDEN_RESULT in worker output (see final.md)
- 2026-09-06T04:56:25+00:00 operator: the revise finished its work and committed (55 commits after a rebase onto main) but ended before pushing while waiting on the test run; pushed by hand with a lease
- 2026-09-06T04:59:47+00:00 description rewritten by the reviewer cost=$0.55
- 2026-09-06T05:11:59+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-06T05:21:17+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-06T05:25:21+00:00 pre-PR checks failed (test) and 3 revision rounds already used; needs a human
- 2026-09-06T05:34:36+00:00 nothing to fix; resumed to in review by hand
- 2026-09-06T05:35:34+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-06T06:16:05+00:00 pre-PR checks failed (test) and 3 revision rounds already used; needs a human
- 2026-09-06T06:52:50+00:00 nothing to fix; resumed to in review by hand
- 2026-09-06T06:54:21+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-06T07:09:42+00:00 pre-PR checks failed (test) and 3 revision rounds already used; needs a human
- 2026-09-06T07:19:24+00:00 nothing to fix; resumed to in review by hand
