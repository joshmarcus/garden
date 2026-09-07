---
id: CG-332
title: A task parked by a harness environment stop is dispatched again as soon as the harness resumes,
  without a hand
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-326
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/quota.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/reap.py
- tests/scheduler/test_quota.py
branch: garden/cg-332-a-task-parked-by-a-harness-environment-stop-is-d
pr: https://github.com/joshmarcus/context-garden/pull/252
runner: manual
attempts: 1
last_dispatched_at: '2026-09-07T01:50:06+00:00'
created: '2026-09-06T08:11:54+00:00'
updated: '2026-09-07T02:23:35+00:00'
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
- 2026-09-07T01:28:17+00:00 dispatched work run 20260907T012758Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~15642 tokens)
- 2026-09-07T01:46:18+00:00 opened https://github.com/joshmarcus/context-garden/pull/252 (base main): Harness-stopped ready tasks now show an explicit resume hold and are automatically dispatched after probe recovery. Quota and auth stops are covered. cost=$0.34
- 2026-09-07T01:49:50+00:00 automated review requested changes: Both acceptance criteria are implemented and covered by focused tests. The ready-status guards prevent stale hold metadata from appearing after a task leaves the parked state. cost=$0.24
- 2026-09-07T01:50:06+00:00 dispatched revise run 20260907T015006Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~16412 tokens)
- 2026-09-07T02:02:14+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/252: Harness-paused tasks now clear their hold metadata on probe recovery and are redispatched automatically. Added CLI and task-page regression assertions for both parked and cleared states. cost=$0.14
- 2026-09-07T02:06:15+00:00 stalled: review finding repeated after a revise round: ui captures not read for: board, board-list, config, events, herbarium, inbox, n; run `garden triage CG-332 --changes "<feedback>" to unblock`
- 2026-09-07T02:23:32+00:00 Owner-delegated queue disposition: Implementation review met both criteria; available capture directories contain zero PNGs. Preserve PR252. Operator-owned evidence hold until CG326 restores real captures; then generate valid captures and review the existing implementation. No unrelated implementation revision or fabricated screenshot approval.
- 2026-09-07T02:23:33+00:00 nothing to fix; resumed to in review by hand
- 2026-09-07T02:23:35+00:00 Implementation review met both criteria; available capture directories contain zero PNGs. Preserve PR252. Operator-owned evidence hold until CG326 restores real captures; then generate valid captures and review the existing implementation. No unrelated implementation revision or fabricated screenshot approval.
