---
id: CG-074
title: Reviews do not consume worker slots
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/config.py
branch: garden/cg-074-reviews-do-not-consume-worker-slots
pr: https://github.com/joshmarcus/context-garden/pull/71
attempts: 1
last_dispatched_at: '2026-09-05T00:19:32+00:00'
created: '2026-09-04T18:51:13+00:00'
updated: '2026-09-05T00:19:32+00:00'
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
- 2026-09-04T22:41:55+00:00 dispatched work run 20260904T224146Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4523 tokens)
- 2026-09-04T22:53:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/71 (base main): Split max_parallel into worker vs. review accounting: reviews/personas/comparisons no longer consume worker slots, get their own review_parallel cap with a queue-and-drain when full, and both counts now show in garden status/doctor and the web Inbox. cost=$7.43
- 2026-09-04T22:55:12+00:00 automated review: approve — Splits max_parallel into worker vs. review accounting with a queue-and-drain for a full review_parallel; all three acceptance criteria are met and the two new tests pass. Slot partitioning covers every run mode and deferred reviews persist correctly across ticks. cost=$0.98
- 2026-09-04T23:59:45+00:00 PR conflicts with main (src/garden/scheduler.py); revise run will rebase and resolve
- 2026-09-04T23:59:56+00:00 dispatched revise run 20260904T235956Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~5639 tokens)
- 2026-09-05T00:04:19+00:00 discovered work filed: CG-127
- 2026-09-05T00:04:33+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated cost=$1.51
- 2026-09-05T00:04:53+00:00 dispatched revise run 20260905T000452Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~6753 tokens)
- 2026-09-05T00:11:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/71: Fixed the pre-PR test failure flagged by review: retry() now kills and closes a task's still-active run before resetting it to ready, so a run that finished but hadn't yet been reaped can't permanently squat a worker slot. All acceptance criteria for the review_parallel split remain met; full suite (351 passed) and ruff pass. cost=$2.44
- 2026-09-05T00:15:28+00:00 automated review requested changes: All three acceptance criteria are met with passing tests, lint clean, and correct queue/drain logic; the retry() slot-squat fix is sound and topical. Requesting changes only to remove scar tissue from the PR description. cost=$0.85
- 2026-09-05T00:19:32+00:00 dispatched revise run 20260905T001932Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~6487 tokens)
