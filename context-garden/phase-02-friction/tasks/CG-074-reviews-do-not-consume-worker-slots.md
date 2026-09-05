---
id: CG-074
title: Reviews do not consume worker slots
status: done
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
last_dispatched_at: '2026-09-05T02:11:15+00:00'
created: '2026-09-04T18:51:13+00:00'
updated: '2026-09-05T02:18:30+00:00'
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
- 2026-09-05T00:22:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/71: No code changes needed this round; rewrote the PR description per review feedback to present the retry() fix as an intentional part of the change (mirroring cancel()) rather than revision-round narration, and trimmed the Friction note's reference to how the revision brief framed it. cost=$0.66
- 2026-09-05T00:22:30+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-074` for one more round, or review on GitHub
- 2026-09-05T00:29:08+00:00 PR conflicts with main (src/garden/cli.py, src/garden/scheduler.py, src/garden/web/app.py, src/garden/web/templates/inbox.html, tests/test_scheduler.py); revision cap reached; needs a human
- 2026-09-05T01:42:49+00:00 revision counter reset (web)
- 2026-09-05T01:42:49+00:00 re-enabled by hand; revise run will follow
- 2026-09-05T01:43:24+00:00 dispatched revise run 20260905T014323Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~7021 tokens)
- 2026-09-05T01:52:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/71: Rebased onto main (which moved twice during the session) resolving conflicts in cli.py, scheduler.py, web/app.py, inbox.html and test_scheduler.py, reconciling this branch's worker/review slot split with main's new live max_parallel override; updated one stale test for the new status output format. cost=$3.62
- 2026-09-05T01:52:20+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-074` for one more round, or review on GitHub
- 2026-09-05T02:04:59+00:00 triage: marked ready for review
- 2026-09-05T02:11:05+00:00 automated review: approve — Splits max_parallel into worker vs. review accounting with a queue-and-drain for a full review_parallel; all three acceptance criteria met, 410 tests pass, ruff clean. The retry() slot-squat fix is sound and topical. cost=$1.05
- 2026-09-05T02:11:08+00:00 PR conflicts with main (src/garden/web/templates/inbox.html); revise run will rebase and resolve
- 2026-09-05T02:11:15+00:00 dispatched revise run 20260905T021114Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~7546 tokens)
- 2026-09-05T02:15:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/71: Rebased onto latest main, resolving conflicts in web/app.py and inbox.html by keeping main's inbox_count/flash additions alongside this branch's workers_running/reviews_running KPI split; full suite (434 passed) and ruff pass. cost=$1.29
- 2026-09-05T02:15:39+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-074` for one more round, or review on GitHub
- 2026-09-05T02:17:55+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/71
- 2026-09-05T02:17:58+00:00 triage: marked ready for review
- 2026-09-05T02:18:30+00:00 #71 was merged by the garden at 02:17:55; a triage-ready pressed three seconds later moved it back by mistake
