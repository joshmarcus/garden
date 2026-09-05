---
id: CG-140
title: An empty description rewrite falls back to a round; pending feedback never sits on an in_review
  task
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/review.py
- tests/test_review.py
created: '2026-09-05T01:53:36+00:00'
updated: '2026-09-05T01:53:36+00:00'
---

## Goal

When the reviewer approves the code but its `description_rewrite` is empty, the scheduler either dispatches the description round (easy tier, CG-109) or applies the reviewer's `description_feedback` some other way; it never leaves `pending_feedback` set on a task that stays `in_review`, because nothing dispatches from that state and automerge holds on "feedback is pending a revise run" forever.

## Context

Found on the first live run half an hour after CG-136 (#93) went live. CG-083 (#81) was approved with `description_ok: false` and no rewrite; the scheduler stored the description feedback as `pending_feedback`, left the task `in_review`, and the poll then held automerge on that feedback every tick while `dispatch_ready` (which queues revise rounds only for `changes_requested`) never saw it. Three other approvals in the same minute had rewrites and merged. The person cleared it with a retry. Rule: a stored `pending_feedback` always comes with the `changes_requested` transition (or the rewrite is applied and nothing is stored); add the case to the tick audit from CG-106 so an `in_review` task with pending feedback and no run is flagged as stuck rather than silent.

## Acceptance criteria

- [ ] an approve verdict with `description_ok: false` and an empty rewrite dispatches a description round; a test with the fake harness.
- [ ] no code path stores `pending_feedback` without transitioning to `changes_requested`; the tick audit flags the state if it ever appears.
