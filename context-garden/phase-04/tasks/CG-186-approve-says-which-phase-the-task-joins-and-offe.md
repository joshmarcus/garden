---
id: CG-186
title: 'Approve says which phase the task joins and offers another: an Approve button with a phase pulldown
  beside it, on the Inbox card and the task page'
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-162
- CG-182
- CG-197
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/inbox.html
- src/garden/web/templates/task.html
- src/garden/web/actions/tasks.py
- src/garden/inbox.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
branch: garden/cg-186-approve-says-which-phase-the-task-joins-and-offe
pr: https://github.com/joshmarcus/context-garden/pull/143
attempts: 1
last_dispatched_at: '2026-09-05T12:22:48+00:00'
created: '2026-09-05T10:18:25+00:00'
updated: '2026-09-05T13:09:53+00:00'
---

## Goal

Approving a draft says where it goes. The Approve control on an Inbox draft card and on a draft's task page reads "Approve into phase-03" (the task's current phase) and carries a small pulldown of the product's other open phases beside it; picking another phase moves the task there and approves it in one press. The look stays as it is now: one primary button, one quiet pulldown, no extra rows.

## Context

Asked by the user on 2026-09-05: "Approve should indicate what phase to add it to (the current phase) e.g. 'Add to phase-03' and have a control to add to another phase. Maybe it's 'Approve' and there's a drop down for which phase to add it to? I like the way it looks now but maybe there's a way to elegantly organize it." The common case behind it: a discovered draft lands in the running phase but belongs to the next one, and during a freeze (CG-148) the running phase refuses approvals, so today the operator moves files by hand first. CG-162 adds the move itself (CLI and a task-page pulldown); this task is the approve-time shape of it. The priority and tier pulldowns from CG-099 set the pattern: apply on change, no Set button.

## Design

- The button label is "Approve into <phase>" where <phase> is the pulldown's current value, defaulting to the task's phase; the pulldown lists the product's open phases in order, marks a frozen phase "(frozen)" and hides closed ones. Changing the pulldown updates the label without a request; pressing the button posts `approve` with a `phase` field.
- The `approve` action accepts `phase`: when it differs from the task's phase it calls the move from CG-162 first (same refusals, shown as a flash), then approves. When the target phase is frozen the action refuses with the freeze message unless the task carries an exception.
- On the task page the same control replaces the plain Approve button for drafts; everywhere else (ready and later statuses) nothing changes.
- Keyboard and no-JavaScript: the pulldown is a real `<select>` inside the form, so the post works without the label script.

## Acceptance criteria

- [ ] A draft's Inbox card and task page show "Approve into <phase>" with a pulldown of the product's open phases beside it; the label follows the pulldown.
- [ ] Approving into another phase moves then approves in one request, with CG-162's refusals surfaced as flashes; approving into a frozen phase without an exception is refused with the freeze message.
- [ ] The control fits the current card layout with no new row; the walkthrough page for the Inbox shows it.
- [ ] Tests for the default phase, a move-and-approve, and the frozen refusal.

## Log

- 2026-09-05T10:31:15+00:00 approved (web)
- 2026-09-05T12:22:48+00:00 dispatched work run 20260905T122239Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-162-move-a-task-to-another-phase-from-the-task-page stacked on CG-162, ~21006 tokens)
- 2026-09-05T12:32:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/143 (base garden/cg-162-move-a-task-to-another-phase-from-the-task-page): Draft tasks' Approve control on the Inbox card and task page now reads 'Approve into <phase>' with a pulldown of the product's open phases (frozen ones marked, closed ones hidden); choosing another phase moves then approves in one request, reusing CG-162's move refusals, and a frozen target without a freeze exception is refused with the freeze message. cost=$2.20
- 2026-09-05T12:35:28+00:00 PR conflicts with garden/cg-162-move-a-task-to-another-phase-from-the-task-page; rebased onto garden/cg-162-move-a-task-to-another-phase-from-the-task-page mechanically and force-pushed
- 2026-09-05T12:35:30+00:00 stack parent CG-162 merging; retargeted this PR to main before the parent branch is deleted
- 2026-09-05T12:36:39+00:00 rebased; diff unchanged; verdict kept
- 2026-09-05T12:36:44+00:00 parent CG-162 merged; rebased onto main and retargeted the PR
- 2026-09-05T12:37:58+00:00 automated review: approve — Cleanly implements the Approve-into-phase control on the Inbox card and task page, reusing CG-162's move with its refusals; all four acceptance criteria are met and tested, full suite and lint pass. cost=$1.14
- 2026-09-05T13:09:53+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/143
