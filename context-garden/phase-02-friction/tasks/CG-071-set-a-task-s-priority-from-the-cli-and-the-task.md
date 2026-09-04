---
id: CG-071
title: Set a task's priority from the CLI and the task page
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/cli.py
- src/garden/web/app.py
created: '2026-09-04T18:45:31+00:00'
updated: '2026-09-04T18:45:31+00:00'
---

## Goal

`garden priority <id> <n>` and a priority control on the task page and the Board, so reordering the queue does not mean editing frontmatter by hand.

## Context

Asked during the first live run. Priority is a frontmatter integer (lower dispatches first, ties by id) that a person may edit, but there is no command and no control in the UI; `garden new-task --priority` is the only way to set it. Add the command (writes the field through the store, logs "priority 2 -> 1" in the task log, emits an event), a small form on the task page, and up/down controls on the Board's ready column. `garden ready` already shows the order; keep it as the check.

## Acceptance criteria

- [ ] `garden priority CG-054 0` changes the field, logs it, and `garden ready` shows the new order.
- [ ] the task page and Board offer the same change.
- [ ] tests for the command and the route.

## Log

- 2026-09-04T18:45:31+00:00 approved
