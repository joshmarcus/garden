---
id: CG-078
title: Closed phases leave the rail and live in a browsable herbarium
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/web/app.py
- src/garden/web/templates/base.html
- src/garden/web/templates/phase.html
- src/garden/store.py
- src/garden/model.py
- src/garden/cli.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
branch: garden/cg-078-closed-phases-leave-the-rail-and-live-in-a-brows
pr: https://github.com/joshmarcus/context-garden/pull/73
attempts: 1
last_dispatched_at: '2026-09-04T22:43:49+00:00'
created: '2026-09-04T19:05:18+00:00'
updated: '2026-09-04T23:58:19+00:00'
---

## Goal

A phase can be closed. A closed phase is unmistakably finished wherever it appears, no longer sits in the left rail among the phases being worked, and can still be browsed, with everything it produced, from one place.

## Context

Asked during the first live run. Phase 1 has had all nineteen tasks done for a day and still shows in the rail beside phase 2 with the same drawer, plate and copy, and nothing in the UI or the data model says it is over. There is no phase status: `Phase.meta` is the `goals.md` frontmatter and today carries only `plant`. This task is marked hard because it touches the data model, the CLI, the rail, the phase page and a new page, and the herbarium look has to stay coherent (see the botanical theme spec: a pressed specimen is the theme's word for something finished; titles and copy stay plain).

Design to follow, adjusting where the code argues:

1. **Model.** `closed: <date>` in `goals.md` frontmatter marks a closed phase; `Phase.closed` exposes it. `garden close-phase <product/phase>` sets it when every task is `done` or `cancelled` (otherwise refuses and lists what is open; `--force` overrides), records an event, and is what the phase-closing task (CG-029) runs at its end. `garden reopen-phase` clears it. The scheduler never dispatches into a closed phase and `new-task` refuses it without `--reopen`.
2. **Rail.** Only open phases are listed as drawers. Below them one entry, "Herbarium", with the count of closed phases, links to `/herbarium`. If a product has no open phase the rail says so and points at planning.
3. **Herbarium page.** Every closed phase as a pressed specimen: the plate, the phase name and dates (first dispatch to close), tasks done, cost, lead time and first-pass rate from `metrics`, and links to the phase page, its `docs/friction.md` and the closing document if CG-029 wrote one. Sorted by close date, newest first, grouped by product when there is more than one.
4. **Phase page of a closed phase: a closing header instead of the working one.** The open-phase header (spend against budget, PRs tracked, brief cost, approve-all and dispatch controls) is replaced by a header that reads as the record of what the phase did:
   - **Outcomes**: the goals from `goals.md` with, for each, the tasks that delivered it and their state; then the figures from `metrics` (tasks done, PRs merged, lead time, revise rounds, first-pass rate, cost by tier, dates from first dispatch to close).
   - **Persona reviews, prominent**: every report under `docs/reviews/` with its persona, date and headline findings, above the fold, with a link to each report and to the tasks it produced.
   - **Artifacts**: the closing document (CG-029's output), `docs/friction.md`, the specs the phase added or changed, the plates it added, and the trial records for the phase, each linked.
   - **PRs**: every merged PR of the phase in a table (number, title, task, size, merged date), and any closed unmerged with why.
   - The plate rendered as a pressed specimen; no dispatch, approve or triage controls; the task table stays below as a reference.
   The Board and Trellis default to open phases with a control to include closed ones.
5. **Status.** `garden status` shows closed phases in one summary line, not one row each, unless `--all`.

## Acceptance criteria

- [ ] `garden close-phase` and `reopen-phase` work as described, with tests, and CG-029's brief names the command.
- [ ] a closed phase is absent from the rail and present on `/herbarium` with the figures above.
- [ ] its phase page shows the closing header: outcomes against the goals, persona reviews above the fold, artifacts and merged PRs linked, no working controls.
- [ ] the scheduler and `new-task` refuse a closed phase; a test covers each.
- [ ] phase 1 of this garden closes cleanly with the command and appears in the herbarium.
- [ ] the plates and the pressed look follow the botanical theme spec; copy is plain.

## Out of scope

- Archiving task files or moving them on disk; a closed phase stays where it is.

## Log

- 2026-09-04T19:05:18+00:00 approved
- 2026-09-04T22:43:49+00:00 dispatched work run 20260904T224340Z-work via local [claude model=fable] (fresh session, base main, ~15822 tokens)
- 2026-09-04T22:59:04+00:00 discovered work filed: CG-120, CG-121
- 2026-09-04T22:59:40+00:00 opened https://github.com/joshmarcus/context-garden/pull/73 (base main): Phases can now be closed: closed: in goals.md frontmatter, close-phase/reopen-phase CLI, dispatch and new-task guards, a /herbarium page of pressed specimens, a closing header on closed phase pages, and open-by-default Board/Trellis. 9 new tests; full suite green. cost=$15.94
- 2026-09-04T23:03:17+00:00 automated review: approve — Closed-phase feature is fully implemented for everything reachable from a worker worktree, thoroughly tested (295 pass, ruff clean), with a clean, well-contextualized PR description. Two acceptance criteria (CG-029 brief edit, closing the live phase 1) are structurally out of a worker's reach and are clearly flagged as human/scheduler follow-ups. cost=$1.03
- 2026-09-04T23:04:04+00:00 CI failure judged flaky by checks; reran instead of dispatching a revise run
- 2026-09-04T23:58:19+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/73
