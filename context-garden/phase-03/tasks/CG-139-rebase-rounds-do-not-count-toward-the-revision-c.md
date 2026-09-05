---
id: CG-139
title: Rebase rounds do not count toward the revision cap
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- tests/test_scheduler.py
branch: garden/cg-139-rebase-rounds-do-not-count-toward-the-revision-c
pr: https://github.com/joshmarcus/context-garden/pull/105
attempts: 1
last_dispatched_at: '2026-09-05T04:29:11+00:00'
created: '2026-09-05T01:19:30+00:00'
updated: '2026-09-05T04:32:28+00:00'
---

## Goal

`max_revisions` bounds the rounds a worker spends fixing its own work. A round whose only cause is a conflict with the base branch (a rebase round) or a stale base (CG-131) does not count, so a PR that waits while ten others merge under it does not end up "needs a human" for having been rebased three times.

## Context

Found at the end of the first live run. With thirty reviewed PRs merging in one evening, CG-111 and CG-079 each reached the cap on rebase rounds alone and stopped with "revision cap reached; needs a human"; the person reset the counter by hand each time. Count only rounds triggered by review findings, failed checks that fail on the branch but not at its base, or a person's send-back. Rebase and stale-base rounds keep their own counter for the log ("rebased 3 times") and never block.

The same for the review cap (`review.max_rounds`): a review that follows a conflict rebase re-reads code the reviewer already approved and must not count toward the cap. Tonight nine PRs reached the review cap this way at once (01:41), every one of them clean, and the loop stopped until the person pressed "one more review" nine times.

## Acceptance criteria

- [ ] a conflict rebase round leaves `revisions` unchanged; a test with three consecutive rebases never sets `needs_human`.
- [ ] review-driven and send-back rounds still count; the cap still fires for them.
- [ ] the task log shows the rebase count separately.
- [ ] a review after a conflict rebase does not count toward `review.max_rounds`.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-03 at the phase-02 close (deferred by the freeze)
- 2026-09-05T01:20:00+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03; cleared by hand when it happens
- 2026-09-05T03:01:20+00:00 approved (web)
- 2026-09-05T03:05:55+00:00 back to draft: approved by mistake during the phase 02 freeze; carried into phase 03
- 2026-09-05T03:19:58+00:00 approved (web)
- 2026-09-05T03:57:42+00:00 dispatched work run 20260905T035733Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8154 tokens)
- 2026-09-05T04:13:02+00:00 opened https://github.com/joshmarcus/context-garden/pull/105 (base main): Conflict and stale-base rebase rounds now increment a separate rebase_rounds counter instead of revisions, are never capped/never set needs_human on their own, and a review following such a round no longer counts toward review.max_rounds. cost=$3.42
- 2026-09-05T04:19:01+00:00 automated review: approve — Rebase rounds are cleanly separated into their own rebase_rounds counter and exempted from both the revision and review caps; all four acceptance criteria are met with targeted tests, and the full suite plus lint pass. cost=$0.86
- 2026-09-05T04:19:52+00:00 CI failure
- 2026-09-05T04:20:05+00:00 dispatched revise run 20260905T042004Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8729 tokens)
- 2026-09-05T04:28:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/105: Rebased the CG-139 branch onto main (it had fallen behind CG-152's in-process test runner) and removed the now-obsolete wait_for_runs calls the two new CG-139 tests still made, which is what ruff's F821 was actually flagging; full suite (469 passed) and lint are clean. cost=$1.33
- 2026-09-05T04:29:01+00:00 PR conflicts with main (src/garden/scheduler/dispatch.py, src/garden/scheduler/poll.py); revise run will rebase and resolve
- 2026-09-05T04:29:11+00:00 dispatched revise run 20260905T042911Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~8866 tokens)
- 2026-09-05T04:32:28+00:00 no active run found; back to ready — expected run 20260905T043128Z-review but it is running (mode review): (no closer recorded)
