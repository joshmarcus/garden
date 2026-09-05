---
id: CG-142
title: Task actions refuse a task that is done or cancelled
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/scheduler.py
- src/garden/cli.py
created: '2026-09-05T02:18:30+00:00'
updated: '2026-09-05T02:18:30+00:00'
---

## Goal

Every task action (web and CLI) that changes a task's state refuses a task that is `done` or `cancelled`, with a message that names the state and what happened (for example "CG-074 is done: #71 was merged at 02:17:55"), instead of moving it back into the loop.

## Context

Found on the first live run. Automerge merged #71 at 02:17:55; three seconds later a "one more review" press (triage-ready then review) on the same task landed, moved CG-074 from `done` back to `in_review`, and dispatched a review run on a merged PR. The person put it back by hand. `triage()`, `dispatch_review()`, `retry()` and `answer()` check some preconditions but not terminal status. Add one guard used by all of them, and let CG-086's flash-message path show the refusal; the CLI prints the same sentence and exits 1. A merged PR is the strongest signal: when the poll has recorded the merge, nothing but `garden set-status` with `--force` may leave `done`.

## Acceptance criteria

- [ ] each state-changing action on a done or cancelled task is refused with the state and the reason; tests for web and CLI.
- [ ] a review is never dispatched for a task whose PR is merged.

## Log
- 2026-09-05T02:19:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
