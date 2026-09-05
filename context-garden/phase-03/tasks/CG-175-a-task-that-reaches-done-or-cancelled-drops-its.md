---
id: CG-175
title: A task that reaches done or cancelled drops its needs-human stop so the Inbox never counts a finished
  task
status: in_review
product: context-garden
phase: phase-03
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler/__init__.py
- src/garden/scheduler/poll.py
- src/garden/scheduler/review.py
- src/garden/inbox.py
branch: garden/cg-175-a-task-that-reaches-done-or-cancelled-drops-its
pr: https://github.com/joshmarcus/context-garden/pull/125
attempts: 1
last_dispatched_at: '2026-09-05T05:14:47+00:00'
created: '2026-09-05T05:05:28+00:00'
updated: '2026-09-05T05:33:00+00:00'
---

## Goal

`_transition` to a terminal status (`done`, `cancelled`) clears the task's `needs_human` stop, `pending_feedback` and `automerge_blocked` in state, so a finished task never shows as a decision on the Inbox or in `garden inbox`'s count.

## Context

On 2026-09-05 at 05:04 `garden inbox` said "13 need you" while three of those were `done` tasks (CG-142, CG-164) still carrying a `review_cap` stop: the rebase round set the card in the same tick in which automerge merged the PR (the last verdict was approve, so the gate passed), and the merge transition left the stop in place. CG-139 had the same card while a run was queued.

## Acceptance criteria

- [ ] A transition to `done` or `cancelled` removes `needs_human`, `pending_feedback` and `automerge_blocked` from the task's state entry and logs nothing extra.
- [ ] The Inbox and `garden inbox` count only non-terminal tasks; a test merges a PR on a task that has a `review_cap` stop and sees no card.
- [ ] A review-cap stop is not set in a tick in which the automerge gate passes for the same task.

## Log

- 2026-09-05T05:05:28+00:00 approved (web)
- 2026-09-05T05:14:47+00:00 dispatched work run 20260905T051438Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~5771 tokens)
- 2026-09-05T05:28:23+00:00 opened https://github.com/joshmarcus/context-garden/pull/125 (base main): _transition now clears needs_human/pending_feedback/automerge_blocked from state when a task reaches done or cancelled, and _automerge_gate fails closed when a needs-human stop is present so a rebase-triggered review-cap hit can no longer be masked by a same-tick merge on the stale pre-rebase verdict. cost=$2.34
- 2026-09-05T05:33:00+00:00 automated review: approve — Correctly clears needs_human/pending_feedback/automerge_blocked on a terminal transition and fails the automerge gate closed when a needs-human stop is set, preventing a merge on a stale pre-rebase verdict. All three acceptance criteria are met and tested; full suite (551) and lint pass. cost=$1.10
