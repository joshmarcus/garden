---
id: CG-074
title: Reviews do not consume worker slots
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/config.py
created: '2026-09-04T18:51:13+00:00'
updated: '2026-09-04T18:51:13+00:00'
---

## Goal

`max_parallel` bounds workers (work, revise, resume, trial) and a separate `review_parallel` bounds review, persona and comparison runs, so a low worker limit chosen to avoid merge conflicts does not also throttle the two-minute reviews that gate every PR.

## Context

Asked during the first live run. `free_slots()` is `max_parallel` minus every active run, reviews included. With `max_parallel: 3` (chosen because conflicts are not yet handled, CG-057), each PR's automated review takes a worker slot for its duration, and a queue of 24 tasks moves at roughly four an hour. Reviews are short, read-only and cannot conflict with anything, so they deserve their own limit. Add `review_parallel` (default: same as `max_parallel`), count only worker modes against `max_parallel`, and show both counts in the Inbox header.

## Acceptance criteria

- [ ] a review run starts while `max_parallel` worker slots are full, up to `review_parallel`.
- [ ] `garden status` and the Inbox show workers and reviews separately.
- [ ] tests for the two limits.

## Log

- 2026-09-04T18:51:13+00:00 approved
