---
id: CG-148
title: A frozen or closed phase refuses approvals and dispatch; a freeze is a phase state, not a note
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/web/app.py
- src/garden/model.py
- src/garden/cli.py
created: '2026-09-05T03:07:37+00:00'
updated: '2026-09-05T03:19:59+00:00'
---

## Goal

A phase can be frozen (`garden freeze product/phase`, or `frozen: <date>` in its goals frontmatter, shown on the phase page and the rail). In a frozen phase the approve action, `garden approve` and `dispatch` refuse a task unless it carries `freeze_exception: true` with a reason, with a message that says the phase is frozen; discovered tasks are filed as drafts marked deferred; the retro and close-out commands keep working. A closed phase refuses everything but reading.

## Context

Found at the phase-02 close on the first live run. The freeze was a paragraph in `goals.md`; nothing enforced it. At 03:01 fourteen drafts were approved from the web in one pass, five dispatched at once, including the scheduler split that must run alone, and the person's agent had to pause dispatch, stop the workers and set them back by hand. The freeze should be state the scheduler and the UI read, the way `closed` is (CG-078, CG-121), with the same guards and one explicit exception path for the fixes a wrap-up needs.

## Acceptance criteria

- [ ] `garden freeze` and `unfreeze` set and clear the state; the phase page and rail show it.
- [ ] approve and dispatch refuse a task in a frozen phase without the exception flag; a test for the web action and the CLI.
- [ ] a discovered task in a frozen phase lands as a draft with "deferred by the freeze" in its log.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T03:08:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T03:19:59+00:00 approved (web)
