---
id: CG-075
title: 'Runs page: the table and the scheduler log stay inside their panels'
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/runs.html
- src/garden/web/templates/_runs.html
- src/garden/web/templates/base.html
branch: garden/cg-075-runs-page-the-table-and-the-scheduler-log-stay-i
pr: https://github.com/joshmarcus/context-garden/pull/32
attempts: 1
last_dispatched_at: '2026-09-04T18:52:02+00:00'
created: '2026-09-04T18:52:02+00:00'
updated: '2026-09-04T18:59:58+00:00'
---

## Goal

On `/runs`, the runs table and the scheduler log never draw outside their white panel: wide content scrolls inside the panel, and the page body never scrolls sideways.

## Context

Reported during the first live run: the runs table's text runs to the right of the panel background. The table has several `nowrap` mono columns (run id such as `20260904T184338Z-revise`, model, brief tokens, in / out, cost), so it is wider than the panel, and unlike the phase page it is not wrapped in the `.scroll` container that gives `overflow-x: auto`. The scheduler log below it is a `.log` block of long single lines with the same problem. Wrap the table in `.scroll` (in `runs.html` and the `_runs.html` partial the live region swaps in), let the run id and title cells wrap or truncate with a title attribute, and give `.log` `overflow-x: auto` with `overflow-wrap: anywhere`. Check the Inbox's and task page's tables and log blocks for the same omission while there.

## Acceptance criteria

- [ ] at 1280px and 900px wide, nothing on `/runs` paints outside a panel; wide content scrolls inside it.
- [ ] the live-region partial keeps the wrapper after a refresh.
- [ ] the same holds for every other table and `.log` block in the web UI.

## Log

- 2026-09-04T18:52:02+00:00 dispatched work run 20260904T185202Z-work via manual [human] (fresh session, base main, ~8631 tokens)
- 2026-09-04T18:55:49+00:00 opened https://github.com/joshmarcus/context-garden/pull/32 (base main): Wide content now scrolls inside its panel: the page shell no longer widens for the board, the runs table is wrapped, bare tables in panels scroll, and the log wraps long tokens.
- 2026-09-04T18:59:58+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/32
