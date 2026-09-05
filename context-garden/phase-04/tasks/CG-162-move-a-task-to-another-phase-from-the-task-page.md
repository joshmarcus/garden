---
id: CG-162
title: Move a task to another phase from the task page and the CLI, keeping its id, history and state
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading:
- src/garden/store.py
- src/garden/cli.py
- src/garden/web/actions/tasks.py
- src/garden/web/pages/task.py
- src/garden/inbox.py
created: '2026-09-05T03:56:09+00:00'
updated: '2026-09-05T10:31:13+00:00'
---

## Goal

A task can be moved to another phase of the same product from the task page and from the CLI. It keeps its id, its run history, its `state.json` entry and its dependencies; only the file location and the `phase:` field change.

## Context

Requested by the user on 2026-09-05 during phase 03, after the phase-02 wrap-up moved fourteen drafts into phases 03 and 04 by hand: `git mv` of each task file, editing `phase:` in the frontmatter, and `garden set-status`. Nothing in the UI or the CLI does this, and it is a routine need: a discovered draft lands in the running phase but belongs to the next one, a feature freeze (CG-148) leaves new ideas homeless, and the retro produces tasks for a later phase.

Design:

- CLI: `garden move <id> <product>/<phase>` moves the task file into `<phase>/tasks/`, sets `phase:`, appends a log line and emits a `moved` event. It refuses a task with a run in flight (its worktree and run record are live) and refuses a closed phase, each with a plain one-line message. A move into a frozen phase is allowed for drafts only.
- Web: the task page gets a phase pulldown listing the product's open phases, applied on change with no Set button, the same way the tier pulldown works (CG-099); the page reloads at the same URL because ids are stable. The Inbox draft card offers "move to <next phase>" when the task's own phase is frozen, since that is the common case.
- The graph already spans phases, so dependencies keep working by id. A task whose dependency now sits in a later phase gets a warning on its page, because it can never become ready in the earlier one.
- Cost follows the task: phase cost reports are computed from the task's current phase, so the move shows up in both phases' logs.

## Acceptance criteria

- [ ] `garden move <id> <product>/<phase>` moves the file, updates `phase:`, logs and emits an event; it refuses a task with a run in flight and refuses a closed phase, each with a plain message.
- [ ] The task page has a phase pulldown of the product's open phases that moves the task on change, with no Set button; the Inbox draft card offers a move when the task's phase is frozen.
- [ ] State, run history and dependencies survive the move; a dependency that now points into a later phase is shown as a warning on the task page.
- [ ] Tests cover the CLI and the web action, including both refusals.

## Log

- 2026-09-05T10:31:13+00:00 approved (web)
