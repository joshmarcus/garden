---
id: CG-177
title: No review is dispatched while a worker run is in flight, and the reap finds a task's worker run
  by mode, so a review record can never send a running task back to ready
status: ready
product: context-garden
phase: phase-03
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/poll.py
- src/garden/scheduler/review.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/__init__.py
- tests/scheduler/test_reap.py
created: '2026-09-05T05:55:53+00:00'
updated: '2026-09-05T05:55:53+00:00'
---

## Goal

A task with a worker run in flight (work, revise, resume, rebase) never gets a review dispatched under it, and the reap identifies a running task's active run by its mode, so a review record can never make the reap conclude "no active run found" and send the task back to `ready`.

## Context

CG-139 on 2026-09-05: 04:28:58 a revise run pushed a rebase to PR #105; 04:29:01 the poll found a new conflict and moved the task to `changes_requested`; 04:29:11 a second revise run was dispatched (task `running`). At 04:31:28 the poll dispatched an automated review for the task, apparently because the PR head had changed since the last review, although a revise run was in flight. At 04:32:28 the reap of the running task found the review record as the task's latest run, logged `no active run found; back to ready — expected run 20260905T043128Z-review but it is running (mode review)`, and moved the task to `ready` with its PR open. The in-flight revise run finished its rebase on its own and was never reaped; the operator closed its record by hand, put the task back with `garden pr`, and a later revise redid the same rebase. Same family as CG-116 (phase 02).

## Acceptance criteria

- [ ] The poll's review dispatch (head changed, feedback, drain of deferred reviews) is skipped, and the review deferred, while the task has a worker-mode run in flight; a log line says so once.
- [ ] `reap` looks for the task's active run among worker modes only; a review or persona record for a running task is left to `reap_review`, and never produces the `no active run found` transition.
- [ ] A test dispatches a revise run, forces a review dispatch on the same task, ticks, and sees the task still `running` and the revise run reaped normally when it finishes.

## Log

- 2026-09-05T05:55:53+00:00 approved (web)
