---
id: CG-198
title: A restart reaps finished-but-unreaped runs of every mode before its first tick, and a dispatch
  onto a dirty worktree stashes and continues
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
branch: garden/cg-198-a-restart-reaps-finished-but-unreaped-runs-of-ev
attempts: 1
last_dispatched_at: '2026-09-05T12:48:16+00:00'
created: '2026-09-05T10:30:00+00:00'
updated: '2026-09-05T12:48:16+00:00'
---

## Goal

Two restarts on 2026-09-05 lost a review verdict the old process had reaped in its last tick (CG-150 at 05:00, CG-176 at 10:01) and each needed a fresh review. After the WSL outage, CG-176's next dispatch failed with `git merge --ff-only … Your local changes` because the killed worker left uncommitted edits. Also: `finalize` emits `run_finished` before the first terminal `run.save()`, so a kill during the fence check re-emits it (staff engineer).

## Provenance

From the phase-03 persona reviews of 2026-09-05 (product-manager:medium, user:low, staff-engineer:medium); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] On start the scheduler walks run records of every mode, reaps those whose process is gone and whose output is complete, applies verdicts and results as a normal reap would, and only then ticks; a test kills a scheduler after a review finishes and starts another.
- [ ] A dispatch that finds a dirty worktree stashes the edits under a named stash, logs it on the task, and proceeds; the stash is listed on the task page.
- [ ] `run_finished` is emitted once per run, after the terminal save.

## Log

- 2026-09-05T10:31:18+00:00 approved (web)
- 2026-09-05T12:48:16+00:00 dispatched work run 20260905T124807Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4500 tokens)
