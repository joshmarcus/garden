---
id: CG-057
title: A PR that conflicts with its base gets a rebase round
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/github.py
branch: garden/cg-057-a-pr-that-conflicts-with-its-base-gets-a-rebase
attempts: 1
last_dispatched_at: '2026-09-04T19:12:19+00:00'
created: '2026-09-04T17:47:51+00:00'
updated: '2026-09-04T19:12:19+00:00'
---

## Goal

When GitHub reports a task's PR as conflicting with its base, the poll notices and dispatches a revise round whose brief says to rebase onto the base and resolve the conflicts, the same way a stacked child is handled when its parent merges.

## Context

Asked during the first live run when PR #20 (CG-040) showed a merge conflict after other PRs landed on main. `GitHub.get_pr` already fetches `mergeable` (`MERGEABLE`, `CONFLICTING`, `UNKNOWN`) into `PRInfo`, but nothing in `Scheduler.poll` reads it; conflicts are only handled for stacked children in `_restack` (which fetches, tries the rebase, and on conflict writes feedback naming the files and asking the next run to resolve them). A plain PR that conflicts with `origin/main` sits there: no transition, no revise run, no card, and the person finds out on GitHub.

In `poll`, when `pr.mergeable == "CONFLICTING"` and the task is not already in `changes_requested`: try the rebase in the worktree the way `_restack` does; if it applies cleanly, force-push with lease and leave the state alone; if not, abort the rebase and set the same conflict feedback `_restack` uses, so a revise run resolves it. Record a `conflict` event and show it on the task page. Count it as a revision round. When several PRs from one phase touch the same files, this will fire after every merge, which is the cost of parallel work on one codebase.

## Acceptance criteria

- [ ] a PR reported `CONFLICTING` by GitHub gets either a clean automatic rebase and force-push, or a revise run with the conflicting files named.
- [ ] the task page and Inbox show the conflict while it is unresolved.
- [ ] a test with the fake GitHub reporting `CONFLICTING` and a fake origin that actually conflicts.

## Out of scope

- Choosing merge order to avoid conflicts; the trellis and stacking are for that.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T19:12:19+00:00 dispatched work run 20260904T191218Z-work via local [claude model=sonnet] (fresh session, base main, ~6443 tokens)
