---
id: CG-070
title: Auto-approve every discovered task, not only blocking ones
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/config.py
created: '2026-09-04T18:41:57+00:00'
updated: '2026-09-04T21:26:18+00:00'
---

## Goal

A configuration switch that creates every discovered task as `ready`, so a garden run in a fully automatic mode never waits on a person to approve work its own workers proposed.

## Context

Asked during the first live run: "please autoapprove all proposed work". Today `plan.auto_approve` covers the planner's output and `discovered.auto_approve_blocking` covers only items a worker marks blocking; every other discovered item, and everything filed with `garden new-task` or the friction form (CG-044), is created `draft` and waits on the Inbox. Add `discovered.auto_approve: false` (all discovered items become `ready` when true) and a `new_task.auto_approve: false` for the CLI and web forms; when either is on, the Inbox's "Approve planned or discovered work" group is empty by design and the digest says how many tasks were auto-approved, so the person still sees what the garden took on.

## Acceptance criteria

- [ ] with `discovered.auto_approve: true`, a non-blocking discovered item is created `ready` and dispatched on the next tick.
- [ ] with `new_task.auto_approve: true`, `garden new-task` and the web form create `ready` tasks unless `--draft` is given.
- [ ] the digest reports auto-approved tasks; README documents both keys, off by default.

## Log

- 2026-09-04T18:41:57+00:00 approved
- 2026-09-04T21:26:18+00:00 not a good default: on 2026-09-04 seven discovered tasks were duplicates or already fixed and were cancelled by hand (CG-095, 097, 102, 103, 105, 107, 108); auto-approving them would have dispatched that work
