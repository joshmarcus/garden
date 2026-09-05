---
id: CG-139
title: Rebase rounds do not count toward the revision cap
status: draft
product: context-garden
phase: phase-03
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- tests/test_scheduler.py
created: '2026-09-05T01:19:30+00:00'
updated: '2026-09-05T03:05:55+00:00'
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
