---
id: CG-329
title: 'The worker count the dispatcher enforces and the count the rail shows are the same number: checks,
  reviews and edit runs either take a slot visibly or not at all'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 1
difficulty: easy
reading:
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/review.py
- src/garden/web/common.py
- src/garden/web/templates/base.html
- tests/scheduler/test_dispatch.py
branch: garden/cg-329-the-worker-count-the-dispatcher-enforces-and-the
pr: https://github.com/joshmarcus/context-garden/pull/233
attempts: 1
last_dispatched_at: '2026-09-07T10:10:18+00:00'
created: '2026-09-06T05:26:49+00:00'
updated: '2026-09-07T10:20:38+00:00'
---

## Goal

One definition of a worker slot. `max_parallel` counts the runs that occupy a slot, the rail's "workers: n/m" shows exactly that count, and the Config page says which modes count. Reviews keep their own cap (`reviews`), and checks and edit runs either have their own small cap or are excluded from the worker count; whichever rule is chosen, the dispatcher and the display agree.

## Context

2026-09-06 05:20Z: the rail showed "workers: 4/7" for twenty minutes while five priority-1 tasks sat ready and no work dispatched; a hand `garden dispatch` started one at once. The dispatcher's count evidently included the check and review runs in flight (two checks and a review made seven), while the display counted work runs only. The owner had raised the cap to seven expecting seven workers and got four.

## Acceptance criteria

- [ ] The rail, the Config page and `garden status` show the same occupancy the dispatcher uses, and the Config page names the modes that take a slot.
- [ ] Checks and edit runs do not consume worker slots (they are short and machine-bound), or they have their own visible cap; a test asserts a ready task dispatches while checks are running and the worker count is under the cap.

## Log
- 2026-09-06T05:26:49+00:00 approved (cli)
- 2026-09-06T13:13:23+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:38+00:00 reset to ready by hand
- 2026-09-06T13:46:59+00:00 priority 2 -> 0
- 2026-09-06T17:21:40+00:00 reordered in context-garden/phase-05 (order 1 -> 2) (web)
- 2026-09-06T17:21:46+00:00 reordered in context-garden/phase-05 (order 2 -> 0) (web)
- 2026-09-06T17:43:31+00:00 dispatched work run 20260906T174248Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~17587 tokens)
- 2026-09-06T18:16:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/233 (base main): Aligned dispatcher and UI worker-slot accounting around worker modes only. Checks and edit runs remain visible but do not consume max_parallel slots. cost=$0.17
- 2026-09-06T18:21:25+00:00 automated review requested changes: Worker occupancy is aligned across the dispatcher and displays, but edit dispatch still depends on worker-slot availability despite edits being documented as slot-free. cost=$0.26
- 2026-09-06T19:00:53+00:00 dispatched revise run 20260906T190051Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~18375 tokens)
- 2026-09-06T19:10:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/233: Slot-free edit runs now dispatch even when all worker slots are occupied, with regression coverage. Existing worker/review/check accounting remains aligned across scheduler and UI. cost=$0.05
- 2026-09-06T19:13:15+00:00 stalled: review finding repeated after a revise round: ui captures not read for: board, board-list, config, events, herbarium, inbox, n; run `garden triage CG-329 --changes "<feedback>" to unblock`
- 2026-09-06T19:43:11+00:00 nothing to fix; resumed to in review by hand
- 2026-09-06T20:11:35+00:00 Operator safety hold until CG-338 shared admission and descendant ownership land: removing check/edit slot gates without their own bound risks the observed suite contention. Preserve PR233, revisit when CG-338 is verified. Correctness tests approved; not a request to redo worker-slot implementation.
- 2026-09-07T04:13:52+00:00 Owner explicitly released the operator safety hold. Resume normal validation of preserved PR233. Current shared cap4/reviewer1 and OS resource limits remain in force; do not confuse worker-mode display exclusions with bypassing shared resource admission.
- 2026-09-07T04:13:52+00:00 approved (web)
- 2026-09-07T04:13:54+00:00 triage: changes requested by hand: Owner released safety hold. Preserve PR233 implementation; reconcile with current main and shared resource admission now
- 2026-09-07T04:14:39+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-329`) or send it back (`garden triage CG-329 --changes "..."`)
- 2026-09-07T04:22:06+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T04:41:43+00:00 dispatched revise run 20260907T044141Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~19670 tokens)
- 2026-09-07T04:50:48+00:00 preserved uncommitted worktree changes from run 20260907T044141Z-revise outside the PR: `git stash apply 9bd0cbfaeb125a671f361b927e1b707501f9068b` in /home/joshua/work/worktrees/CG-329 (garden:CG-329:20260907T044141Z-revise:reap)
- 2026-09-07T04:50:48+00:00 worker blocked: Worker-slot accounting and shared resource admission are covered and pushed. Exact-head CI did not register a run, so completion cannot be claimed. cost=$0.11
- 2026-09-07T09:13:15+00:00 triage: changes requested by hand: Owner hold is released. Preserve implemented slot accounting and shared-resource admission. Integrate current main (old
- 2026-09-07T09:13:16+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T09:13:52+00:00 dispatched revise run 20260907T091349Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~19858 tokens)
- 2026-09-07T09:29:26+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/233: Worker occupancy now uses worker modes consistently across dispatch, rail, Config, and garden status. Checks and edits remain outside max_parallel while still participating in shared host admission. cost=$0.15
- 2026-09-07T09:32:25+00:00 description rewritten by the reviewer cost=$0.81
- 2026-09-07T09:59:32+00:00 rebasing before merge; rebase onto main conflicts (src/garden/now1.py, src/garden/scheduler/__init__.py); a rebase agent will resolve it
- 2026-09-07T09:59:35+00:00 dispatched rebase run 20260907T095933Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~21030 tokens)
- 2026-09-07T10:03:22+00:00 preserved uncommitted worktree changes from run 20260907T095933Z-rebase outside the PR: `git stash apply d8e5eb8dc7144978511d24dc4e0f4f6ac7d887c7` in /home/joshua/work/worktrees/CG-329 (garden:CG-329:20260907T095933Z-rebase:reap)
- 2026-09-07T10:04:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/233: Rebased CG-329 onto origin/main and resolved all conflicts while preserving both sides' intent. cost=$0.02
- 2026-09-07T10:09:45+00:00 description rewritten by the reviewer cost=$0.96
- 2026-09-07T10:10:10+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/runs.py); a rebase agent will resolve it
- 2026-09-07T10:10:18+00:00 dispatched rebase run 20260907T101016Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~10865 tokens)
- 2026-09-07T10:11:30+00:00 preserved uncommitted worktree changes from run 20260907T101016Z-rebase outside the PR: `git stash apply f3c3c7d791b89e1dd440ed126bb9a1c8f3f3d082` in /home/joshua/work/worktrees/CG-329 (garden:CG-329:20260907T101016Z-rebase:reap)
- 2026-09-07T10:13:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/233: Rebased CG-329 onto origin/main and resolved the runs.py conflict. cost=$0.02
- 2026-09-07T10:15:55+00:00 automated review: approve — Worker-slot occupancy is consistently defined as worker modes across dispatch, the rail, Config, Now views, and garden status; checks and edits remain subject to separately visible shared host admission. Focused verification passed (55 tests and Ruff), and all listed captures were inspected. cost=$0.72
- 2026-09-07T10:19:15+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-07T10:20:38+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/233
