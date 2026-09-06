---
id: CG-333
title: A run that ends without a result but with new commits in its worktree is reaped as a pushed revision,
  not a failed attempt
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/reap.py
- src/garden/runner/local.py
- src/garden/gitops.py
- tests/scheduler/test_reap.py
created: '2026-09-06T09:09:18+00:00'
updated: '2026-09-06T13:14:45+00:00'
---

## Goal

The reaper reads the worktree before it reads the transcript. When a work or revise run ends with no `GARDEN_RESULT` (or a result block that names no status) but the run's branch has new commits since dispatch, the reaper pushes the branch with a lease, opens or updates the PR, logs "result missing; N commits reaped from the worktree", and sends the PR to review, with the worker's last message quoted on the task so the reviewer knows what the worker believed was left. Only a run with no new commits and no result is a failed attempt.

## Context

2026-09-06: five Fable runs (CG-234 once, CG-307 twice, CG-308 twice; about $45 of work) ended "successfully" from the CLI's point of view with a last message like "everything is committed; the only open item is the full suite, which the monitor will report", because the model backgrounded the eleven-minute suite and waited for a notification a headless run never gets. Each time the work sat committed and unpushed in the worktree, the reaper recorded "no GARDEN_RESULT" and failed the attempt, and the operator pushed by hand (once with 91 commits) and put the task in review. The docs now tell workers the run ends when they stop; this task makes the reaper salvage the work regardless.

## Acceptance criteria

- [ ] With the fake harness: a work run that exits with commits on its branch and no result is reaped as a pushed revision with a PR and a review queued, the task log names the commit count and quotes the last message; a run with no commits and no result is still a failed attempt.
- [ ] The same for a revise run: the commits are pushed with a lease onto the PR's branch and the review is queued; the revision counter advances as for a normal push.
- [ ] A result block that says `blocked` or `wont_do` is honoured as before; salvage applies only when the status is absent.

## Log
- 2026-09-06T09:09:19+00:00 approved (cli)
- 2026-09-06T13:13:01+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:45+00:00 reset to ready by hand
