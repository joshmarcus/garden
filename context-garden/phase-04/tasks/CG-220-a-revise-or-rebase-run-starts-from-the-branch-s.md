---
id: CG-220
title: A revise or rebase run starts from the branch's head on origin and pushes with a lease, and the
  queue never rewrites a branch with a worker run in flight
status: running
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/rebase.py
- src/garden/scheduler/reap.py
- src/garden/gitops.py
- tests/scheduler/test_dispatch.py
branch: garden/cg-220-a-revise-or-rebase-run-starts-from-the-branch-s
pr: https://github.com/joshmarcus/context-garden/pull/172
attempts: 1
last_dispatched_at: '2026-09-05T17:45:26+00:00'
created: '2026-09-05T16:49:39+00:00'
updated: '2026-09-05T17:45:26+00:00'
---

## Goal

Two writers never race on one branch. Before a revise, rebase or resume run starts, the worktree is synced to the branch's head on origin (fetch, then reset to it, keeping any local-only commits on a `backup/<run>` ref and noting them on the task); every push after a run uses `--force-with-lease` against the head the run started from, so a rejected push names the cause instead of failing the task; and the merge queue, the stale-base probe and the conflict rebase skip a task that has a worker-mode run in flight, the way CG-182 fences check runs.

## Context

2026-09-05 16:34 to 16:46, CG-178: a review requested changes and a revise run started from the worktree; meanwhile the branch on origin gained six commits (the queue's rebase and an earlier revise's push). The revise finished three commits ahead of a stale base, its `git push -u origin HEAD:<branch>` was rejected as non-fast-forward, and the task went `failed` with the push error as its only note. Rebasing the three commits onto the branch head conflicted in three files because both revises had fixed the same review item. The operator reset the worktree to origin's head, kept the stale commits on a backup branch and retried. CG-177 stopped reviews being dispatched under a running task; this is the same rule for branch writers.

## Acceptance criteria

- [ ] Dispatch of a revise, rebase or resume run fetches and resets the worktree to `origin/<branch>` first; local-only commits go to `backup/<run-id>` and a log line names them.
- [ ] Pushes after a run use `--force-with-lease=<branch>:<start-head>`; a lease failure is logged with both heads and the run is re-dispatched once from the new head instead of failing the task.
- [ ] The merge queue's pre-merge rebase, the stale-base probe and the conflict rebase do not touch a task whose active run is a worker mode; a test starts a revise, moves main, ticks, and sees no rebase on that task until the revise reaps.

## Log

- 2026-09-05T16:49:39+00:00 approved (web)
- 2026-09-05T16:50:26+00:00 dispatched work run 20260905T165010Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~23607 tokens)
- 2026-09-05T17:26:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/172 (base main): Dispatch of a revise/rebase/resume run now syncs the worktree to origin's head first (backing up any local-only commits), pushes after such a run use a lease naming the head they started from with automatic mechanical-rebase recovery on rejection, and the PR-conflict rebase now refuses a task with a worker run in flight (the merge queue and stale-base probe already did, via existing gates). cost=$7.36
- 2026-09-05T17:33:38+00:00 automated review: approve — All three acceptance criteria are implemented and tested correctly; full suite (783 passed) and ruff are green, and the diff is scoped exactly to the task. cost=$1.22
- 2026-09-05T17:43:41+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T17:45:06+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated
- 2026-09-05T17:45:26+00:00 dispatched revise run 20260905T174526Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~27192 tokens)
