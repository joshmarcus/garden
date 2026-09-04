---
id: CG-085
title: Workers' checkouts live in a configurable work_dir outside the garden
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/config.py
- src/garden/scheduler.py
- src/garden/runner/local.py
branch: garden/cg-085-workers-checkouts-live-in-a-configurable-work-di
pr: https://github.com/joshmarcus/context-garden/pull/39
attempts: 1
last_dispatched_at: '2026-09-04T19:31:59+00:00'
created: '2026-09-04T19:31:59+00:00'
updated: '2026-09-04T19:36:26+00:00'
---

## Goal

The product clones and the per-task worktrees the workers run in live under a directory of the person's choosing, `work_dir` in `garden.yaml`, entirely outside the garden's own directory, so nothing a worker does by walking up from its checkout can reach the garden, its venv or its state.

## Context

Asked during the first live run after three workers re-pointed the garden's own `.venv` from inside `.garden/worktrees/<id>` (the garden's venv is three directories up from a worktree). `Config.garden_dir` is hard-coded to `<root>/.garden` and `Scheduler.repo_for` and `worktree_for` put `repos/` and `worktrees/` under it. Add `work_dir` (absolute, or relative to the garden root; default `.garden`, so nothing changes for existing gardens); `repos/` and `worktrees/` (including trial worktrees) go under it, while `state.json`, `events.jsonl`, `runs/` and `trials.jsonl` stay in `.garden`. For a worktree that already exists at the old location, keep using it until it is removed, so the setting can change while workers run. `garden doctor` prints the work dir and warns if it is inside the garden. `run.json` already records each run's worktree path.

## Acceptance criteria

- [ ] with `work_dir` set, new clones and worktrees are created there and reaped from there; existing worktrees under `.garden/worktrees` keep working until cleanup.
- [ ] `garden doctor` shows the work dir; README documents the key.
- [ ] tests for the new location and the fallback.

## Log

- 2026-09-04T19:31:59+00:00 dispatched work run 20260904T193159Z-work via manual [human] (fresh session, base main, ~4398 tokens)
- 2026-09-04T19:34:18+00:00 opened https://github.com/joshmarcus/context-garden/pull/39 (base main): work_dir in garden.yaml puts product clones and per-task worktrees outside the garden; worktrees already under .garden keep working; doctor shows the work dir.
- 2026-09-04T19:36:24+00:00 automated review: approve — work_dir cleanly relocates clones and worktrees outside the garden with a correct old-location fallback for running workers; doctor and README updated; tests and lint pass. cost=$0.53
- 2026-09-04T19:36:26+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/39
