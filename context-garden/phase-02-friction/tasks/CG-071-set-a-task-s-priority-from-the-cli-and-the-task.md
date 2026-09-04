---
id: CG-071
title: Set a task's priority and difficulty from the CLI and the task page
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/cli.py
- src/garden/web/app.py
branch: garden/cg-071-set-a-task-s-priority-and-difficulty-from-the-cl
attempts: 1
last_dispatched_at: '2026-09-04T19:46:57+00:00'
created: '2026-09-04T18:45:31+00:00'
updated: '2026-09-04T19:46:57+00:00'
---

## Goal

`garden priority <id> <n>` and `garden difficulty <id> <tier>`, with a priority control and a difficulty selector on the task page (and priority on the Board), so reordering the queue or moving a task to another model tier does not mean editing frontmatter by hand. Difficulty picks the model tier at dispatch, so changing it on a ready task changes which model runs it.

## Context

Asked during the first live run. Priority is a frontmatter integer (lower dispatches first, ties by id) that a person may edit, but there is no command and no control in the UI; `garden new-task --priority` is the only way to set it. Add the command (writes the field through the store, logs "priority 2 -> 1" in the task log, emits an event), a small form on the task page, and up/down controls on the Board's ready column. `garden ready` already shows the order; keep it as the check.

## Acceptance criteria

- [ ] `garden priority CG-054 0` and `garden difficulty CG-054 hard` change the fields, log them, and `garden ready` / `garden show` reflect them.
- [ ] the task page has a difficulty selector (easy, medium, hard) and a priority control; changing either is logged.
- [ ] the task page and Board offer the same change.
- [ ] tests for the command and the route.

## Log

- 2026-09-04T18:45:31+00:00 approved
- 2026-09-04T19:46:57+00:00 dispatched work run 20260904T194657Z-work via manual [human] (fresh session, base main, ~2295 tokens)
