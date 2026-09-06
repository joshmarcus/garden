---
id: CG-328
title: Accepting a worker's no-change call on a revise round returns the task to review and queues the
  round; it never lands in waiting_human with no question
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler/human.py
- src/garden/scheduler/review.py
- src/garden/inbox.py
- tests/scheduler/test_human.py
created: '2026-09-06T05:26:03+00:00'
updated: '2026-09-06T13:14:37+00:00'
---

## Goal

When a person accepts a worker's "nothing to change" on a revise round, the task goes back to `in_review` and the next review round is queued (or the PR merges if the last verdict already approved and nothing moved). The task never sits in `waiting_human` with "(no question recorded)".

## Context

2026-09-06 05:22Z, CG-311: the revise worker reported nothing to change; `garden accept` logged "no-change accepted by the person; resuming the round without a new work run" and left the task in `waiting_human` with an Inbox card offering `garden answer` for a question nobody asked. The operator set the status back to in_review by hand and pressed review. The accept path for a first-round no-change (wont_do / no_change on the work run) is fine; the revise-round path is the one that misroutes.

## Acceptance criteria

- [ ] Accepting a no-change on a revise round moves the task to in_review and queues a review round (or merges when the recorded verdict for the head is approve); a test with the fake harness covers it.
- [ ] No accept path produces a waiting_human task without a question; the Inbox never shows "(no question recorded)".

## Log
- 2026-09-06T05:26:03+00:00 approved (cli)
- 2026-09-06T13:13:22+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:37+00:00 reset to ready by hand
