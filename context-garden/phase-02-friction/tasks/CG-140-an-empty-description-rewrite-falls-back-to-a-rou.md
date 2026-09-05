---
id: CG-140
title: An empty description rewrite falls back to a round; pending feedback never sits on an in_review
  task
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/review.py
- tests/test_review.py
branch: garden/cg-140-an-empty-description-rewrite-falls-back-to-a-rou
pr: https://github.com/joshmarcus/context-garden/pull/95
attempts: 1
last_dispatched_at: '2026-09-05T01:54:50+00:00'
created: '2026-09-05T01:53:36+00:00'
updated: '2026-09-05T02:04:14+00:00'
---

## Goal

When the reviewer approves the code and flags the description, the scheduler applies `description_rewrite` when present (or dispatches the easy-tier description round when it is empty, CG-109) and stores nothing as pending; it never leaves `pending_feedback` set on a task that stays `in_review`, because nothing dispatches from that state and automerge holds on "feedback is pending a revise run" forever.

## Context

Found on the first live run half an hour after CG-136 (#93) went live. CG-083 (#81) was approved with `description_ok: false` and a rewrite present; the scheduler stored the description feedback as `pending_feedback` anyway, left the task `in_review`, and the poll then held automerge on that feedback every tick while `dispatch_ready` (which queues revise rounds only for `changes_requested`) never saw it. Three other approvals in the same minute had rewrites and merged. The person cleared it with a retry. Rule: a stored `pending_feedback` always comes with the `changes_requested` transition (or the rewrite is applied and nothing is stored); add the case to the tick audit from CG-106 so an `in_review` task with pending feedback and no run is flagged as stuck rather than silent.

## Acceptance criteria

- [ ] an approve verdict with `description_ok: false` and a rewrite applies the rewrite and stores no pending feedback; with an empty rewrite it dispatches a description round; tests for both with the fake harness.
- [ ] no code path stores `pending_feedback` without transitioning to `changes_requested`; the tick audit flags the state if it ever appears.

## Log

- 2026-09-05T01:54:50+00:00 dispatched work run 20260905T015441Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~5347 tokens)
- 2026-09-05T02:04:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/95 (base main): reap_review now applies the reviewer's description_rewrite (or dispatches an easy-tier description-only revise round when it's empty) on an approve verdict with description_ok false, not just on request_changes; the tick audit flags an in_review task that ends up carrying pending_feedback anyway. cost=$3.46
