---
id: CG-334
title: 'Close the review findings left open by the hand merges of 2026-09-06: ghost records with terminal
  tasks, the persona replay test, design routes per product, the snapshot''s queue data, Now 2''s per-goal
  status marks, Now 1''s empty-period gate'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/reap.py
- src/garden/harness.py
- src/garden/web/pages/api.py
- tests/test_harness.py
- tests/test_web.py
branch: garden/cg-334-close-the-review-findings-left-open-by-the-hand
pr: https://github.com/joshmarcus/context-garden/pull/255
attempts: 1
last_dispatched_at: '2026-09-07T01:53:56+00:00'
created: '2026-09-06T12:43:08+00:00'
updated: '2026-09-07T15:18:12+00:00'
---

## Goal

The blocking findings the reviewers left open on six PRs the owner chose to merge by hand on 2026-09-06 (to drain the queue for a /tmp remount) are closed, each as a small, tested change, so nothing merged that day is carrying a known defect:

- CG-316 (PR #212): the orphan sweep leaves pid-less run records active when their task is terminal; close them too.
- CG-237 (PR #214): the persona regression test synthesizes output; replay the four surviving result texts in tests/fixtures/persona-replay instead.
- CG-318 (PR #217): design routes always use the first configured product; the snapshot reads a nonexistent `_queue` entry so it omits the real merge and dispatch queue; the 1280/390 light/dark captures for the changed surfaces were never taken.
- CG-309 (PR #227): every phase goal shows "Progress not mapped" instead of merged, in flight or not started.
- CG-308 (PR #218): the runs-or-merges gate renders an operator-only or annotation-only period as empty, hiding recorded spend and marks.

## Context

The owner: "anything that's not terrible, let's merge" (12:30Z), while draining workers to move /tmp back to tmpfs. Each finding above was the reviewer's blocking item on the last round; none breaks main, all are real. Split into one PR per bullet if that lands faster.

## Acceptance criteria

- [ ] Each bullet above has a test that fails before and passes after, and the fix is in place; the task's result lists the six findings by PR with the commit that closed each.
- [ ] `garden now --page 1` and `--page 2` render a window with only operator spend and a phase with mapped goals, respectively.

## Log
- 2026-09-06T12:43:09+00:00 approved (cli)
- 2026-09-06T13:13:03+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:47+00:00 reset to ready by hand
- 2026-09-07T01:53:36+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply 63bde01317d0105f18b1a39112a08ec4c2ce0e6e` in /home/joshua/work/worktrees/CG-334 to recover them (garden:CG-334:20260907T015336Z-work:pre-dispatch, run 20260907T015336Z-work)
- 2026-09-07T01:53:56+00:00 dispatched work run 20260907T015336Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15226 tokens)
- 2026-09-07T02:16:04+00:00 preserved uncommitted worktree changes from run 20260907T015336Z-work outside the PR: `git stash apply ffe32832348b4e6b76f3c648e0695eabf8da1c00` in /home/joshua/work/worktrees/CG-334 (garden:CG-334:20260907T015336Z-work:reap)
- 2026-09-07T02:18:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/255 (base main): Closed terminal pid-less launched run records, exposed real queue data in design snapshots, and routed design artifacts by product. The already-integrated persona and Now regressions remain covered by their replay and rendering tests. cost=$2.07
- 2026-09-07T13:01:04+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/255
- 2026-09-07T15:18:12+00:00 automated review could not start: CG-334 is done: #255 was merged at 13:01:04
