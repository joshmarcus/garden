---
id: CG-332
title: A task parked by a harness environment stop is dispatched again as soon as the harness resumes,
  without a hand
status: done
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
attempts: 1
last_dispatched_at: '2026-09-08T15:35:11+00:00'
created: '2026-09-06T08:11:54+00:00'
updated: '2026-09-08T17:30:03+00:00'
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
- 2026-09-07T08:51:38+00:00 CG326 capture prerequisite merged9d0c213; removed manual runner hold for preserved-branch integration and fresh validation, not implementation redo.
- 2026-09-07T08:51:38+00:00 triage: changes requested by hand: CG326/PR250 merged9d0c213 with reviewed56/56 real captures; manual capture-prerequisite hold released. Preserve accepted
- 2026-09-07T08:51:40+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T08:56:50+00:00 dispatched revise run 20260907T085648Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~16992 tokens)
- 2026-09-07T09:10:31+00:00 preserved uncommitted worktree changes from run 20260907T085648Z-revise outside the PR: `git stash apply 8f6fee50e3328dcd523eeae2581f659bbdf7dd88` in /home/joshua/work/worktrees/CG-332 (garden:CG-332:20260907T085648Z-revise:reap)
- 2026-09-07T09:12:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/252: Harness-paused tasks now clear their hold and redispatch automatically after probe recovery, covering quota and auth stops. Current responsive light/dark Inbox and task-page captures were added. cost=$0.10
- 2026-09-07T15:22:05+00:00 automated review requested changes: The code and focused regression tests satisfy both criteria, but the required served interaction cannot be verified because its replay manifest is missing. Fresh evidence must cover the held state, empty state, and failure followed by recovery at this exact head. cost=$0.42
- 2026-09-07T16:37:55+00:00 Temporary operator incident admission hold to reserve next drained slot for P0 CG385 recovery; preserve all work. Restore original runner from docs/incidents/cg385-recovery-admission-holds.json after CG385 starts.
- 2026-09-07T16:39:06+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-332`) or send it back (`garden triage CG-332 --changes "..."`)
- 2026-09-07T17:01:39+00:00 Operator restored original runner after CG385 recovery repair acquired actual execution slot. Shared cap remains1.
- 2026-09-07T18:59:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T18:59:47+00:00 Delegated operator Inbox audit: cleared stale manual-hold stop after verified normal runner restoration; existing implementation, PR and pending review feedback retained. No owner decision required.
- 2026-09-07T20:57:44+00:00 dispatched revise run 20260907T205741Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~18566 tokens)
- 2026-09-07T21:32:06+00:00 pre-PR checks failed (ui, UI captures); revise run will fix before the PR is updated cost=$0.13
- 2026-09-07T21:43:03+00:00 dispatched revise run 20260907T214301Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~18322 tokens)
- 2026-09-07T22:00:41+00:00 preserved uncommitted worktree changes from run 20260907T214301Z-revise outside the PR: `git stash apply 2e664d42dfb3d47134c9b895ea0472cf332b1428` in /home/joshua/work/worktrees/CG-332 (garden:CG-332:20260907T214301Z-revise:reap)
- 2026-09-07T22:03:09+00:00 pre-PR checks failed (ui, UI captures); revise run will fix before the PR is updated cost=$0.12
- 2026-09-07T22:03:30+00:00 dispatched revise run 20260907T220327Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~18468 tokens)
- 2026-09-07T22:19:08+00:00 pre-PR checks failed (ui, UI captures); revise run will fix before the PR is updated cost=$0.15
- 2026-09-07T22:19:44+00:00 dispatched revise run 20260907T221941Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~18550 tokens)
- 2026-09-07T22:48:20+00:00 pre-PR checks failed (ui, UI captures) and 6 revision rounds already used; needs a human cost=$0.18
- 2026-09-08T12:35:50+00:00 triage: changes requested by hand: Operator audit: preserved local branch and fast-forwarded it to its existing remote053f3899. Recheck current code and th
- 2026-09-08T12:35:50+00:00 Delegated operator Inbox review: preserved PR/worktree and queued one concrete continuation within current 4 AWS + 1 local limits.
- 2026-09-08T15:35:11+00:00 dispatched revise run 20260908T153509Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~20348 tokens)
- 2026-09-08T15:50:36+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/252: Preserved implementation verified and refreshed the served task-page recovery evidence at the final head. Quota/auth redispatch and parked-task UI behavior pass focused tests. cost=$0.10
- 2026-09-08T16:00:15+00:00 automated review requested changes: Implementation and focused checks satisfy both criteria, but the required exact-head served interaction replay exercises unrelated generic flows and does not verify the harness-pause lifecycle. cost=$0.41
- 2026-09-08T16:00:38+00:00 stuck: 6 revision rounds already used; resume with one more round (`garden retry CG-332`) or send it back (`garden triage CG-332 --changes "..."`)


## Operator repeat-loop audit, 2026-09-08T16:04:51.955690+00:00

Six revisions and four reviews have accumulated. Latest implementation criteria passed, but scheduler replay covered unrelated generic behavior. CG-436 now owns the replay-selection/evidence-handoff defect. Keep the existing revision stop until the affected replay is concrete; do not grant another generic implementation retry. Preserve current author artifacts and branch.


## Delegated Inbox decision, 2026-09-08T16:15:35.229474+00:00

Owner delegated this input. Decision: investigate the verification handoff under CG436 before authorizing more implementation retries; retain current branch, PR, current-head tests, report and actual unresolved outcome checks. This is now an operator-owned investigation, not a request for Josh to reset the cap or guess whether to merge. Installed rc5 cannot yet render a dedicated investigation card (CG437); keep the protective stop until evidence or its protocol repair is concrete.
- 2026-09-08T17:30:03+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/252
