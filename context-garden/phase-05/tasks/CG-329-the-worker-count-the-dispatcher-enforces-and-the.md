---
id: CG-329
title: 'The worker count the dispatcher enforces and the count the rail shows are the same number: checks,
  reviews and edit runs either take a slot visibly or not at all'
status: in_review
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
last_dispatched_at: '2026-09-06T19:00:53+00:00'
created: '2026-09-06T05:26:49+00:00'
updated: '2026-09-06T19:43:11+00:00'
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
