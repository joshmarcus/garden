---
id: CG-334
title: 'Close the review findings left open by the hand merges of 2026-09-06: ghost records with terminal
  tasks, the persona replay test, design routes per product, the snapshot''s queue data, Now 2''s per-goal
  status marks, Now 1''s empty-period gate'
status: ready
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
created: '2026-09-06T12:43:08+00:00'
updated: '2026-09-06T12:43:09+00:00'
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
