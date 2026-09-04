---
id: CG-027
title: First live run of the loop on itself
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
estimate: M
difficulty: easy
reading:
- docs/worker-protocol.md
- context-garden/phase-02-friction/specs/friction-log.md
branch: garden/cg-027-first-live-run-of-the-loop-on-itself
pr: https://github.com/joshmarcus/context-garden/pull/8
runner: manual
attempts: 1
last_dispatched_at: '2026-09-04T17:08:28+00:00'
created: '2026-09-04T14:02:28+00:00'
updated: '2026-09-04T17:24:40+00:00'
---

## Goal

Run one task, CG-012, through the whole loop with a real harness and a real GitHub, and write down every point of friction.

## Context

This is a human-driven task (`runner: manual`): take it with `garden take CG-027`, do the steps below on a machine that has `claude`, `gh` and this repository, and hand the notes back with `garden finish CG-027 --result '{...}'` so they land through the same path as everything else. Everything so far has been proven only against the fake harness in `tests/`; this is the first time the brief, the result contract, the review prompt, draft PRs and triage meet the real thing.

Steps:

1. `garden doctor`: `claude` and `gh` found, the repo clean, no graph errors. `garden brief CG-012 --stats` should be under 3k tokens.
2. The phase budget is set in `garden.yaml` (25 USD). Leave it unless the run needs more.
3. `garden approve CG-012`, then `garden serve` (or `garden watch`) and leave it running.
4. Watch each step on the Inbox and the task page, and note anything that took longer, cost more, or needed a hand: dispatch (model chosen, brief tokens); the worker's run (`garden log CG-012`, `garden runs CG-012`); the result line (did the worker end with `GARDEN_RESULT`?); the push and the draft PR (title and body quality); the automated review (verdict, findings, whether the description check was right); triage from the Inbox; the merge and the transition to done.
5. Write the notes into `context-garden/phase-02-friction/docs/friction.md` under a heading "First live run": one bullet per step with what happened, and the run's cost from `garden usage CG-012`.
6. File each concrete friction item as a task: list it under `discovered` in the finish result (the garden files it with provenance), or use `garden new-task`.
7. Approve CG-008 and CG-009 so the loop runs them next. Leave CG-010 unapproved: it is reserved for the model trial (CG-028).

## Acceptance criteria

- [ ] CG-012 is `done` and got there through `garden tick`: dispatched by the scheduler, draft PR opened by the garden, automated review posted, triaged from the Inbox, merged on GitHub.
- [ ] `docs/friction.md` has a "First live run" section with one entry per step and the run's cost.
- [ ] Every friction item that needs code is a task file in this phase.
- [ ] CG-008 and CG-009 are `ready`; CG-010 is still `draft`.

## Out of scope

- Fixing the friction in this task; file it.
- The work environment; this run is at home, where GitHub Actions is available.

## Log

- 2026-09-04T16:06:35+00:00 dispatched work run 20260904T160635Z-work via manual [human] (fresh session, base main, ~6486 tokens)
- 2026-09-04T17:03:10+00:00 discovered work filed: CG-032, CG-033, CG-034, CG-035, CG-036, CG-037, CG-038, CG-039, CG-040, CG-041, CG-042
- 2026-09-04T17:03:32+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/8 (base main): CG-012 ran through the whole loop on a real harness and GitHub and merged; every step and its cost are in docs/friction.md under First live run, and eleven concrete friction items are filed as tasks.
- 2026-09-04T17:05:25+00:00 automated review requested changes: Friction documentation is thorough and accurate, but acceptance criterion 4 (approving CG-008/009, leaving CG-010 draft) is not verified in the diff or task log. Request explicit confirmation that this step was completed. cost=$0.08
- 2026-09-04T17:05:48+00:00 dispatched revise run 20260904T170548Z-revise via manual [human] (fresh session, base main, ~6952 tokens)
- 2026-09-04T17:06:36+00:00 pre-PR checks failed (tests); revise run will fix before the PR is updated
- 2026-09-04T17:08:28+00:00 dispatched revise run 20260904T170828Z-revise via manual [human] (fresh session, base main, ~7765 tokens)
- 2026-09-04T17:08:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/8: Answered the review: the approvals and the filed tasks are garden state, now stated in the PR body and in a closing bullet of the notes.
- 2026-09-04T17:08:50+00:00 stalled: revise run 20260904T170828Z-revise produced no change to the diff; needs a human (garden retry to resume)
- 2026-09-04T17:12:53+00:00 automated review: request_changes — Friction documentation is thorough, accurate, and well-scoped. Acceptance criteria 1–3 are met and evidenced in the diff. Criterion 4 (CG-008, CG-009 ready; CG-010 draft) is claimed but not verifiable from the diff—this is acknowledged as friction around manual tasks. A human reviewer must verify these state changes independently by checking the task files or asking the person to confirm. cost=$0.17
- 2026-09-04T17:24:40+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/8
