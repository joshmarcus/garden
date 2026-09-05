---
id: CG-224
title: 'Phase kickoff: before a phase starts, flag topics that need design, goals without a definition
  of done, questions for the owner, and docs that need attention'
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/planner.py
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/discovered.py
- src/garden/web/pages/phase.py
- src/garden/cli/planning.py
branch: garden/cg-224-phase-kickoff-before-a-phase-starts-flag-topics
pr: https://github.com/joshmarcus/context-garden/pull/174
attempts: 1
last_dispatched_at: '2026-09-05T17:05:21+00:00'
created: '2026-09-05T17:04:17+00:00'
updated: '2026-09-05T17:57:59+00:00'
---

## Goal

Before a phase starts, the garden pauses for one deliberate look: `garden kickoff <product/phase>` (and a "Kick off" button on the phase page) runs a planner-tier review of the phase as written and produces a readiness report with four lists: topics that need design before a task can be safely dispatched, goals that lack a definition of done or measurable outcome, questions only the owner can answer (raised as decision cards, CG-189), and docs that are thin, stale or missing for the work ahead (the product overview against the tree, the architecture map, specs the tasks cite). The phase page shows the report and its open items; approving the phase's first task without a kickoff shows a warning, not a refusal.

## Context

The user on 2026-09-05: "add a moment before a phase starts to flag topics that need more design, set goals, input from the user, docs that could use attention or fleshing out." Phase 03 started with a goals document written by the operator and tasks whose criteria the retro later called placeholders (CG-193); phase 04 started from a stub the retro rewrote after the fact; phase 05 and 06 are stubs now. The retro looks backward (CG-178, CG-181, CG-189); this is the same machinery pointed forward, before spend. The approve gate (CG-193) catches thin criteria one task at a time; the kickoff catches the phase-level gaps: a goal with no task, a task with no goal, a design question shared by several tasks, a doc every brief will inline that is out of date.

## Design

- `garden kickoff <phase>` dispatches one run (`retro.difficulty` tier by default, the same tier as the retro) with the phase goals, the task drafts, the previous phase's retro and verdict, the product overview, the docs the tasks cite, and the walkthrough index; it returns a `GARDEN_KICKOFF` block: `design_needed` (topic, why, which tasks, suggested spike), `goals_gaps` (goal, what is missing), `questions` (question, context, options), `docs` (path, what is thin or stale, which tasks need it), and a `ready` verdict with a one-paragraph summary.
- On reap: the report is written to `<phase>/docs/kickoff.md`; questions become decision cards (CG-189's mechanism); each `design_needed` topic becomes a draft task tagged `spike` with the owner's decision on whether to run it; each `docs` item becomes a draft in the phase or a note in the report if trivial; `goals_gaps` are appended to `goals.md` under "## Open" for the owner to edit.
- The phase page shows a Kickoff panel: the summary, the four lists with their tasks and cards, and the verdict; the freeze and approve flows link to it. `garden status` names phases with tasks approved and no kickoff.
- `garden plan` runs the kickoff first when the phase has no report, unless `--no-kickoff`.

## Acceptance criteria

- [ ] `garden kickoff` and the phase page button produce `docs/kickoff.md` with the four lists and the verdict; a test with the fake harness covers a phase with one gap of each kind.
- [ ] Questions become decision cards, design topics become spike drafts, docs items become drafts or notes, goal gaps land in `goals.md`; each carries `discovered_from: kickoff:<phase>`.
- [ ] Approving a task in a phase with no kickoff shows a warning naming the command; the phase page's Kickoff panel shows the report and the state of every item it raised.
- [ ] Running it on phase 05 as it stands produces a report the owner can act on (checked by hand as part of review).

## Log

- 2026-09-05T17:04:17+00:00 approved (web)
- 2026-09-05T17:05:21+00:00 dispatched work run 20260905T170505Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~25529 tokens)
- 2026-09-05T17:42:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/174 (base main): Implemented `garden kickoff`: a planner-tier review dispatched before a phase starts that flags design gaps, unmeasurable goals, owner questions, and stale docs, writing docs/kickoff.md and filing spike/doc drafts, question decision cards, and goals.md gaps; wired into approve's warning, garden plan, garden status, the phase page, and the Inbox. cost=$9.58
- 2026-09-05T17:46:38+00:00 automated review: approve — Kickoff review is implemented end to end (brief, dispatch, reap, filing, approve warning, phase panel) with solid test coverage; all tests and lint pass and the diff stays in scope. cost=$0.98
- 2026-09-05T17:53:34+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T17:56:27+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-05T17:57:59+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/174
