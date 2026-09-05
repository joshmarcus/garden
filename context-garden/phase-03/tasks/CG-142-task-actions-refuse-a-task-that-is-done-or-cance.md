---
id: CG-142
title: Task actions refuse a task that is done or cancelled
status: in_review
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/scheduler.py
- src/garden/cli.py
branch: garden/cg-142-task-actions-refuse-a-task-that-is-done-or-cance
pr: https://github.com/joshmarcus/context-garden/pull/112
attempts: 1
last_dispatched_at: '2026-09-05T04:40:56+00:00'
created: '2026-09-05T02:18:30+00:00'
updated: '2026-09-05T04:49:15+00:00'
---

## Goal

Every task action (web and CLI) that changes a task's state refuses a task that is `done` or `cancelled`, with a message that names the state and what happened (for example "CG-074 is done: #71 was merged at 02:17:55"), instead of moving it back into the loop.

## Context

Found on the first live run. Automerge merged #71 at 02:17:55; three seconds later a "one more review" press (triage-ready then review) on the same task landed, moved CG-074 from `done` back to `in_review`, and dispatched a review run on a merged PR. The person put it back by hand. `triage()`, `dispatch_review()`, `retry()` and `answer()` check some preconditions but not terminal status. Add one guard used by all of them, and let CG-086's flash-message path show the refusal; the CLI prints the same sentence and exits 1. A merged PR is the strongest signal: when the poll has recorded the merge, nothing but `garden set-status` with `--force` may leave `done`.

## Acceptance criteria

- [ ] each state-changing action on a done or cancelled task is refused with the state and the reason; tests for web and CLI.
- [ ] a review is never dispatched for a task whose PR is merged.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T02:19:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T03:01:24+00:00 approved (web)
- 2026-09-05T03:05:54+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T03:19:58+00:00 approved (web)
- 2026-09-05T04:20:14+00:00 dispatched work run 20260905T042005Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~3971 tokens)
- 2026-09-05T04:39:58+00:00 opened https://github.com/joshmarcus/context-garden/pull/112 (base main): Added a shared ensure_open() guard so every task action (web, CLI, and the scheduler's own automated review/persona dispatch) refuses a done or cancelled task with a message naming the state and what happened; set-status now requires --force to leave those states. cost=$6.27
- 2026-09-05T04:40:48+00:00 PR conflicts with main (src/garden/scheduler/dispatch.py, src/garden/scheduler/human.py); revise run will rebase and resolve
- 2026-09-05T04:40:56+00:00 dispatched revise run 20260905T044056Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~5260 tokens)
- 2026-09-05T04:45:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/112: Rebased CG-142 onto main, resolving conflicts in scheduler/dispatch.py, scheduler/human.py, and web/actions/tasks.py by keeping both this branch's ensure_open guard and main's phase_refusal guard; all tests (515 passed, 3 skipped) and ruff pass. cost=$0.89
- 2026-09-05T04:49:15+00:00 automated review: approve — Clean, well-tested implementation: a shared ensure_open() guard refuses done/cancelled tasks across every scheduler entry point, the web dispatcher, and the CLI, with set-status --force as the sanctioned escape hatch. Both acceptance criteria are met and covered by tests; full suite and ruff pass. cost=$0.92
