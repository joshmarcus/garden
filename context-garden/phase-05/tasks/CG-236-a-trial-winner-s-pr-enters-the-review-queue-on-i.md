---
id: CG-236
title: A trial winner's PR enters the review queue on its own, like any pushed revision
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler/trials.py
- src/garden/scheduler/poll.py
- src/garden/scheduler/review.py
created: '2026-09-05T20:56:29+00:00'
updated: '2026-09-05T20:56:29+00:00'
---

## Goal

When a trial comparison names a winner, the winning PR is reviewed by the loop the way every other PR is: the next tick queues an automated review round, and the card says so. Nobody has to press `review` to move a trial winner along.

## Context

Observed 2026-09-05: CG-225's winner (codex terra, PR #184) sat in `in_review` for 45 minutes with "no review yet" until the operator pressed review; CG-030's winner waited 51 minutes the same way. A PR pushed by a work run goes through `pushed revision` → review request; the trial path ends at `trial won by ...` and never enqueues the round. The winner's PR is otherwise indistinguishable from a work PR (CI, automerge hold, revisions).

## Acceptance criteria

- [ ] After `trial won by`, the next tick dispatches an automated review round for the winning PR unless one is already recorded for its head (patch-id, CG-210).
- [ ] The card for a fresh trial winner reads "review queued", not "no review yet".
- [ ] Test: a trial whose comparison names a winner leads to a review dispatch on the following tick; a work-run PR's path is unchanged.

