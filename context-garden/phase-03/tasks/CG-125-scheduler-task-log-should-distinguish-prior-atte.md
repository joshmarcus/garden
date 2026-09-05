---
id: CG-125
title: Scheduler/task log should distinguish 'prior attempt made real progress but didn't report' from
  a clean restart
status: running
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 3
difficulty: medium
reading:
- src/garden/store.py
- src/garden/scaffold.py
- src/garden/platefetch.py
- src/garden/cli.py
branch: garden/cg-125-scheduler-task-log-should-distinguish-prior-atte
pr: https://github.com/joshmarcus/context-garden/pull/120
discovered_from: CG-065
attempts: 1
last_dispatched_at: '2026-09-05T05:14:38+00:00'
created: '2026-09-04T23:25:21+00:00'
updated: '2026-09-05T05:14:38+00:00'
---

This task's log showed 'no active run found; back to ready' after a prior dispatch, but that prior run had actually committed 3 of 5 fixes plus tests before being interrupted. A fresh worker had to re-derive that state by reading git log/diff rather than it being visible from the task file or brief. Might be worth surfacing partial-completion state (e.g. commits made during an interrupted run) more explicitly so re-dispatched workers don't have to reverse-engineer prior progress.

## Provenance

Discovered by CG-065 (Plates and plants: positional assignment, invalid --plant, --out, atomic publish, one-line source rows) during run `20260904T232304Z-work`.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)

- 2026-09-04T23:25:21+00:00 discovered by CG-065
- 2026-09-05T00:04:53+00:00 approved (web)
- 2026-09-05T00:34:27+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T03:01:04+00:00 approved (web)
- 2026-09-05T03:05:55+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T03:19:57+00:00 approved (web)
- 2026-09-05T05:01:53+00:00 dispatched work run 20260905T050145Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~9012 tokens)
- 2026-09-05T05:11:33+00:00 opened https://github.com/joshmarcus/context-garden/pull/120 (base main): The scheduler now distinguishes an interrupted attempt that made real, unreported progress from a clean restart: reap notes when the worktree holds commits ahead of base (with the count on the no_active_run event), and dispatch lists those commits in the brief for every re-dispatched round so the next worker builds on prior progress instead of reverse-engineering git. cost=$3.71
- 2026-09-05T05:13:27+00:00 PR conflicts with main; rebase onto main conflicts (tests/scheduler/test_dispatch.py); a rebase agent will resolve it
- 2026-09-05T05:14:38+00:00 dispatched rebase run 20260905T051438Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~3858 tokens)
