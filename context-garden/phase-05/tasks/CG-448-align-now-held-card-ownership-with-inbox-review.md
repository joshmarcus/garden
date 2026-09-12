---
id: CG-448
title: Align Now held-card ownership with Inbox review queues
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-381
priority: 1
difficulty: easy
reading:
- src/garden/inbox.py
- src/garden/web/app.py
- tests/test_attention.py
branch: garden/cg-448-align-now-held-card-ownership-with-inbox-review
pr: https://github.com/joshmarcus/context-garden/pull/339
runner: remote
discovered_from: CG-381
attempts: 1
last_dispatched_at: '2026-09-09T00:38:07+00:00'
created: '2026-09-08T18:30:54+00:00'
updated: '2026-09-09T01:35:47+00:00'
file: src/garden/now1.py
error: Served Now fixture showed “1 card waiting on you” and a prior review-cap card while Inbox correctly
  showed zero owner actions and an automated-review queue notice.
---

Make Now use the same scheduler-owned queued-review predicate as Inbox so a queued automated review with a stale review-cap stop does not appear as a card waiting on a person.

## Provenance

Discovered by CG-381 (Make Inbox human-action counts and advice match actual ownership) during run `20260908T174807Z-revise`.
## Log
- 2026-09-08T18:30:54+00:00 discovered by CG-381


## Current source and acceptance

RC6 consolidated Now; use current src/garden/now.py and present page module, not removed now1.py. Preserve the actual reported mismatch; reuse the shared predicate from CG381 after merge.

## Acceptance criteria

- [ ] Now and Inbox agree that queued/running automatic review is owned by automation, even with a stale prior review-cap record.
- [ ] Actual unresolved owner decisions remain counted and link to the correct decision.
- [ ] A small served affected-page fixture and focused tests verify count/text/link agreement in queued, running and real-owner-decision states.
- 2026-09-08T19:24:45+00:00 approved (owner-delegated-hourly-audit)
- 2026-09-08T19:26:10+00:00 dispatched work run 20260908T192609Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base garden/cg-381-make-inbox-human-action-counts-and-advice-match stacked on CG-381, ~17424 tokens)
- 2026-09-08T19:32:17+00:00 opened https://github.com/joshmarcus/context-garden/pull/339 (base garden/cg-381-make-inbox-human-action-counts-and-advice-match): Now and Inbox now agree that queued or running automated reviews remain scheduler-owned, including stale review-cap stops. Genuine owner decisions remain visible and linked correctly. cost=$0.07
- 2026-09-08T21:50:29+00:00 automated review: approve — Now and Inbox consistently treat queued or running automated reviews as automation-owned while preserving genuine owner decisions. Focused tests, lint, and an independent disposable served replay passed at the reviewed head. cost=$0.44
- 2026-09-08T22:08:14+00:00 PR conflicts with garden/cg-381-make-inbox-human-action-counts-and-advice-match; rebase onto garden/cg-381-make-inbox-human-action-counts-and-advice-match conflicts (src/garden/inbox.py, src/garden/web/templates/inbox.html, tests/test_attention.py, tests/test_cli.py); a rebase agent will resolve it
- 2026-09-08T22:08:24+00:00 dispatched rebase run 20260908T220824Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base garden/cg-381-make-inbox-human-action-counts-and-advice-match, conflict only; easy tier, ~7823 tokens)
- 2026-09-08T22:30:41+00:00 base branch `garden/cg-381-make-inbox-human-action-counts-and-advice-match` is itself broken — pre-PR check(s) lint fail at its own commit 871e73b03e59, not because of this branch; waiting for the base to go green, no revise round cost=$0.03
- 2026-09-08T22:36:59+00:00 base branch `garden/cg-381-make-inbox-human-action-counts-and-advice-match` recovered (moved to a46ba12471e3); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-08T22:37:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/339: Now and Inbox now agree that queued or running automated reviews remain scheduler-owned, including stale review-cap stops. Genuine owner decisions remain visible and linked correctly.
- 2026-09-08T22:37:01+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-08T23:52:58+00:00 PR conflicts with garden/cg-381-make-inbox-human-action-counts-and-advice-match; rebase onto garden/cg-381-make-inbox-human-action-counts-and-advice-match conflicts (src/garden/inbox.py, tests/test_attention.py, tests/test_cli.py); a rebase agent will resolve it
- 2026-09-08T23:53:11+00:00 dispatched rebase run 20260908T235311Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base garden/cg-381-make-inbox-human-action-counts-and-advice-match, conflict only; easy tier, ~4236 tokens)
- 2026-09-08T23:58:14+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/339: Resolved the Inbox, attention-test, and CLI-test rebase conflicts while preserving both branches' review-ownership behavior. cost=$0.02
- 2026-09-09T00:37:53+00:00 PR conflicts with garden/cg-381-make-inbox-human-action-counts-and-advice-match; rebase onto garden/cg-381-make-inbox-human-action-counts-and-advice-match conflicts (src/garden/inbox.py, src/garden/scheduler/review.py, tests/test_attention.py, tests/test_cli.py); a rebase agent will resolve it
- 2026-09-09T00:38:07+00:00 dispatched rebase run 20260909T003807Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base garden/cg-381-make-inbox-human-action-counts-and-advice-match, conflict only; easy tier, ~4568 tokens)
- 2026-09-09T00:42:03+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/339: Rebased CG-448 and resolved all four conflicts. cost=$0.01
- 2026-09-09T01:00:10+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T01:10:15+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/339
- 2026-09-09T01:35:47+00:00 automated review could not start: CG-448 is done: #339 was merged at 01:10:15
