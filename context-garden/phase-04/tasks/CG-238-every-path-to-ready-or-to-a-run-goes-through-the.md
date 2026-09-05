---
id: CG-238
title: 'Every path to ready or to a run goes through the approve gate: Dispatch now on a draft, the new-task
  form''s approve-now, and garden take'
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/web/actions/control.py
- src/garden/web/actions/tasks.py
- src/garden/scheduler/human.py
- src/garden/cli/planning.py
- src/garden/cli/state.py
- tests/test_web.py
- tests/test_cli.py
branch: garden/cg-238-every-path-to-ready-or-to-a-run-goes-through-the
pr: https://github.com/joshmarcus/context-garden/pull/192
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: The definition of done says no task is dispatched with placeholder criteria,
  and three personas showed it is false in the shipped build; the gate is this phase's goal 2.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-05T23:12:18+00:00'
created: '2026-09-05T23:05:55+00:00'
updated: '2026-09-05T23:39:10+00:00'
---

## Goal

Dispatch now on a draft dispatches a placeholder brief silently and a second press orphans the first run; the phase page's New task form with approve-now writes status ready directly; garden take flips a draft to ready by hand. Route all three through Scheduler.approve so brief_gaps and phase_refusal apply, hide Dispatch now on a draft, refuse dispatch when a run is in flight, flash the dispatched run id, and on a form refusal keep the task a draft and flash the gap with the file path. Tests for each path.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: The definition of done says no task is dispatched with placeholder criteria, and three personas showed it is false in the shipped build; the gate is this phase's goal 2.

## Acceptance criteria

- [ ] `Dispatch now` on a draft is not offered; on a ready task it refuses while a run is in flight and flashes the dispatched run id otherwise.
- [ ] The New task form's approve-now and `garden take` go through `Scheduler.approve`: a brief gap (placeholder criteria, unresolved reading path) or a phase refusal leaves the task a draft and reports the gap with the file path.
- [ ] Tests for each of the three paths, with the fake harness: a refused form submission, a refused take, and a draft with no dispatch button.

## Log

- 2026-09-05T23:05:55+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:10:30+00:00 approved (cli)
- 2026-09-05T23:12:18+00:00 dispatched work run 20260905T231202Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~17213 tokens)
- 2026-09-05T23:31:30+00:00 opened https://github.com/joshmarcus/context-garden/pull/192 (base main): Hid the draft-only "Dispatch now" button, made the web dispatch action refuse a task that already has a run in flight, and routed the new-task form's approve-now checkbox and `garden take` through Scheduler.approve so brief_gaps/phase_refusal apply and a refusal leaves the task a draft with the gap and file path flashed/printed. cost=$3.57
- 2026-09-05T23:37:32+00:00 automated review: approve — Routes dispatch-from-draft, the new-task form's approve-now, and garden take through Scheduler.approve as specified; tests and lint pass and the diff is tightly scoped. cost=$0.84
- 2026-09-05T23:37:37+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-05T23:39:10+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/192
