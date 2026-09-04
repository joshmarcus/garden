---
id: CG-076
title: Push with lease when the worker rebased its branch
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/gitops.py
branch: garden/cg-076-push-with-lease-when-the-worker-rebased-its-bran
pr: https://github.com/joshmarcus/context-garden/pull/33
attempts: 1
last_dispatched_at: '2026-09-04T19:03:27+00:00'
created: '2026-09-04T18:52:58+00:00'
updated: '2026-09-04T19:11:09+00:00'
---

## Goal

When a worker has rebased its branch (the worktree's history has diverged from `origin/<branch>`), the scheduler pushes with `--force-with-lease` instead of failing the run.

## Context

Seen at 18:51 UTC on CG-009: a revise brief asked the worker to rebase onto main, it did, and `finalize` ran a plain `git push`, which GitHub rejected as non-fast-forward. The run was marked failed ($1.77 spent), the task went to `failed`, and the rebased work sat in the worktree until a person force-pushed it and reset the status by hand. `finalize` only force-pushes when `state[task].force_push` is set, which happens after the scheduler's own restack. Two more tasks in the same tick were rebasing on instruction and would have failed the same way; their state was flagged by hand.

Before pushing, compare: if `origin/<branch>` exists and is not an ancestor of HEAD, but `origin/<base>` is, the branch was rebased; push with `--force-with-lease=<branch>:<origin sha>` and log "rebased branch force-pushed". If the branch was neither fast-forward nor a rebase onto the base (history rewritten some other way), keep failing with the message. CG-057 (rebase rounds on conflict) depends on this.

## Acceptance criteria

- [ ] a worktree rebased onto the base pushes with lease and the PR updates; the log says so.
- [ ] a fast-forward push is unchanged; a diverged branch that is not on the base still fails with the git message.
- [ ] tests with the fake origin for all three.

## Log

- 2026-09-04T18:52:58+00:00 approved
- 2026-09-04T19:03:27+00:00 dispatched work run 20260904T190326Z-work via local [claude model=sonnet] (fresh session, base main, ~2170 tokens)
- 2026-09-04T19:09:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/33 (base main): Added rebase detection to `gitops.push`: when the worker rebases its branch onto origin/base, the push now uses `--force-with-lease=<branch>:<origin-sha>` instead of failing. Other divergences still fail with git's own message. The scheduler logs 'rebased branch force-pushed' when detection triggers. Three tests cover all three cases. cost=$1.10
- 2026-09-04T19:11:09+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/33
