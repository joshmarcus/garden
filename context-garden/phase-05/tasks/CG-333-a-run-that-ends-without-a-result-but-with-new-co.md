---
id: CG-333
title: A run that ends without a result but with new commits in its worktree is reaped as a pushed revision,
  not a failed attempt
status: done
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
branch: garden/cg-333-a-run-that-ends-without-a-result-but-with-new-co
pr: https://github.com/joshmarcus/context-garden/pull/253
attempts: 1
last_dispatched_at: '2026-09-07T01:40:23+00:00'
created: '2026-09-06T09:09:18+00:00'
updated: '2026-09-07T01:59:12+00:00'
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

## Related web-incident prevention

CG-359 owns provenance-safe handling of unrelated dirty files during leftover recovery. Coordinate: salvage intended existing commits here, but do not infer permission to commit all dirty artifacts. CG-357's excluded snapshot was reintroduced twice by scheduler salvage during outage recovery.
- 2026-09-07T01:40:03+00:00 stashed leftover changes from a prior run before redispatch: `git stash apply d87f7b4fd345580a97676b347b2d088886eadb42` in /home/joshua/work/worktrees/CG-333 to recover them (garden:CG-333:20260907T014003Z-work:pre-dispatch, run 20260907T014003Z-work)
- 2026-09-07T01:40:23+00:00 dispatched work run 20260907T014003Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11991 tokens)
- 2026-09-07T01:49:50+00:00 preserved uncommitted worktree changes from run 20260907T014003Z-work outside the PR: `git stash apply 93bdf05829f5c6d0da7c4d44ec771a0def067dd1` in /home/joshua/work/worktrees/CG-333 (garden:CG-333:20260907T014003Z-work:reap)
- 2026-09-07T01:51:11+00:00 opened https://github.com/joshmarcus/context-garden/pull/253 (base main): Salvages committed work or revise runs that end without a result status, preserving the final worker message for reviewers while retaining failure handling for runs without commits. cost=$0.84
- 2026-09-07T01:52:53+00:00 description rewritten by the reviewer cost=$0.26
- 2026-09-07T01:57:11+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-07T01:59:12+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/253
