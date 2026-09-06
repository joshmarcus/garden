---
id: CG-236
title: A trial winner's PR enters the review queue on its own, like any pushed revision
status: in_review
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler/trials.py
- src/garden/scheduler/poll.py
- src/garden/scheduler/review.py
branch: garden/cg-236-a-trial-winner-s-pr-enters-the-review-queue-on-i
pr: https://github.com/joshmarcus/context-garden/pull/205
attempts: 1
last_dispatched_at: '2026-09-06T00:47:05+00:00'
created: '2026-09-05T20:56:29+00:00'
updated: '2026-09-06T01:49:05+00:00'
---

## Goal

When a trial comparison names a winner, the winning PR is reviewed by the loop the way every other PR is: the next tick queues an automated review round, and the card says so. Nobody has to press `review` to move a trial winner along.

## Context

Observed 2026-09-05: CG-225's winner (codex terra, PR #184) sat in `in_review` for 45 minutes with "no review yet" until the operator pressed review; CG-030's winner waited 51 minutes the same way. A PR pushed by a work run goes through `pushed revision` → review request; the trial path ends at `trial won by ...` and never enqueues the round. The winner's PR is otherwise indistinguishable from a work PR (CI, automerge hold, revisions).

## Acceptance criteria

- [ ] After `trial won by`, the next tick dispatches an automated review round for the winning PR unless one is already recorded for its head (patch-id, CG-210).
- [ ] The card for a fresh trial winner reads "review queued", not "no review yet".
- [ ] Test: a trial whose comparison names a winner leads to a review dispatch on the following tick; a work-run PR's path is unchanged.

## Folded in at approval (operator, 2026-09-06)

- [ ] Widened by the joined retro: any PR with no review recorded for its head is queued on the next tick on every runner, including the manual runner; `resume` means the same on every runner.
- [ ] A recorded verdict whose head has moved is discarded, and a review whose task went terminal is cancelled rather than swept by reap_orphaned after it finishes (from CG-278).

## Log

- 2026-09-06T00:24:03+00:00 approved (cli)
- 2026-09-06T00:47:05+00:00 dispatched work run 20260906T004649Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~12178 tokens)
- 2026-09-06T01:49:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/205 (base main): Trial conclusion now dispatches a real automated review round for the winner's PR (mirroring the normal work-run push path) instead of treating the model comparison as a stand-in for review, and the Inbox card reads 'review queued' instead of 'no review yet' while that round is in flight. cost=$4.12
