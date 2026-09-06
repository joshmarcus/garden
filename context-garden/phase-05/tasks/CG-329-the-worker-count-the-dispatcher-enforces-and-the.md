---
id: CG-329
title: 'The worker count the dispatcher enforces and the count the rail shows are the same number: checks,
  reviews and edit runs either take a slot visibly or not at all'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/review.py
- src/garden/web/common.py
- src/garden/web/templates/base.html
- tests/scheduler/test_dispatch.py
created: '2026-09-06T05:26:49+00:00'
updated: '2026-09-06T05:26:49+00:00'
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
