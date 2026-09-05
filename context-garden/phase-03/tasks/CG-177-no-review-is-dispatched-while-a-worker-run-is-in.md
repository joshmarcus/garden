---
id: CG-177
title: No review is dispatched while a worker run is in flight, and the reap finds a task's worker run
  by mode, so a review record can never send a running task back to ready
status: done
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
branch: garden/cg-177-no-review-is-dispatched-while-a-worker-run-is-in
pr: https://github.com/joshmarcus/context-garden/pull/126
attempts: 2
last_dispatched_at: '2026-09-05T09:34:11+00:00'
created: '2026-09-05T05:55:53+00:00'
updated: '2026-09-05T09:52:16+00:00'
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
- 2026-09-05T05:58:03+00:00 dispatched work run 20260905T055755Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4135 tokens)
- 2026-09-05T09:32:51+00:00 attempt 1 failed: no GARDEN_RESULT in worker output (see final.md); will retry
- 2026-09-05T09:34:11+00:00 dispatched work run 20260905T093410Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~24410 tokens)
- 2026-09-05T09:47:41+00:00 opened https://github.com/joshmarcus/context-garden/pull/126 (base main): reap now selects a running task's active run among worker modes only, and review dispatch is deferred while a worker run is in flight, so a review record can no longer send a running task back to ready. Added two scheduler tests and verified the full suite (588 passed) and ruff. cost=$5.63
- 2026-09-05T09:50:03+00:00 automated review: approve — Correct, well-scoped two-part fix (worker-mode-only reap selection via latest_worker_run, plus deferral of review dispatch under an in-flight worker) with tests for both acceptance scenarios; suite and ruff green. cost=$1.15
- 2026-09-05T09:50:06+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T09:51:04+00:00 rebased; diff unchanged; verdict kept
- 2026-09-05T09:52:16+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/126
