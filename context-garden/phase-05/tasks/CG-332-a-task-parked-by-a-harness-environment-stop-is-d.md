---
id: CG-332
title: A task parked by a harness environment stop is dispatched again as soon as the harness resumes,
  without a hand
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/quota.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/reap.py
- tests/scheduler/test_quota.py
created: '2026-09-06T08:11:54+00:00'
updated: '2026-09-06T13:14:43+00:00'
---

## Goal

When a harness pause lifts (the probe succeeds and `dispatch_resumed` fires), every task that the pause parked (an environment stop that returned it to ready with "dispatch paused for <harness> until a probe succeeds") is dispatched again in the normal priority order on the next tick, and the Inbox shows nothing for it. A parked task is never left in `ready` behind a free slot.

## Context

2026-09-06 06:48Z: CG-309's astra work run was stopped as an environment error (a load casualty read as a login failure) and the codex harness paused. The pause cleared within the hour, the Inbox showed no pause, a worker slot stayed free from 06:50 to 08:10, and CG-309 sat in `ready` for eighty minutes until the operator ran `garden dispatch CG-309` by hand, which started it at once. Whatever the dispatcher checks for a parked task after the resume did not clear.

## Acceptance criteria

- [ ] With the fake harness: a task parked by a quota or auth environment stop is dispatched on the first tick after the harness's probe succeeds, with no operator action; the test covers both stop kinds.
- [ ] `garden status` and the task page show a parked task as "waiting for <harness> to resume" while the pause holds, and as plain ready with no hold after it lifts.

## Log
- 2026-09-06T08:11:54+00:00 approved (cli)
- 2026-09-06T13:12:58+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:43+00:00 reset to ready by hand
