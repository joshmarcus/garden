---
id: CG-054
title: A worker's worktree must never act on the live garden
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
branch: garden/cg-054-a-worker-s-worktree-must-never-act-on-the-live-g
attempts: 1
last_dispatched_at: '2026-09-04T18:59:59+00:00'
created: '2026-09-04T17:42:42+00:00'
updated: '2026-09-04T18:59:59+00:00'
---

## Goal

Code running inside a worker's worktree (the worker itself, its tests, the pre-PR checks) can never find and mutate the live garden's `.garden/` state and task files.

## Context

During the first live run, at 17:37:40 UTC the live garden logged "environment error (not an attempt)" for CG-032 and moved it back to ready. That string exists in no code the running `garden serve` had loaded; it exists only in the CG-033 worker's worktree, where that feature was being written. Worktrees live at `.garden/worktrees/<id>` inside the garden, so `find_root()` walking upward from a worktree (from a `Store()` with no path, from `garden` run by a worker to try its feature, from a test that forgets to pass a root) lands on the real garden, and the unreviewed code in the worktree then reaps real runs and writes real task files. The same route explains a pre-PR test failing under load: tests in worktrees share one live root if any of them resolves it.

Fixes, all of them: (1) `find_root()` stops at a `.garden/worktrees` boundary and refuses to return a root that contains the starting path under `.garden/`; (2) the runner sets `GARDEN_ROOT` for the worker to an explicit, non-existent or sandbox path unless the brief says otherwise, and `Store` honours it; (3) the brief's rules say plainly: do not run `garden` commands against this garden; run the test suite only; (4) the pre-PR checks run with the same guard. A test creates a worktree under a temp garden's `.garden/worktrees/x` and asserts `find_root()` from inside it raises.


A second route, seen an hour later: a worker ran `pip install -e .` inside its worktree (the product overview tells workers how to install), which re-pointed the garden's shared `.venv` editable install at `.garden/worktrees/CG-041/src`. When that worktree was removed after its merge, `garden` itself failed to import and `garden serve` answered 500 until the install was repaired by hand. Another worker installed playwright into the same venv. Workers must get their own environment (a venv inside the worktree, or `uv run` with an isolated project), and the pre-PR checks must not depend on the shared `.venv` being untouched.

## Acceptance criteria

- [ ] `find_root()` from inside `.garden/worktrees/<id>` does not return the enclosing garden.
- [ ] workers get `GARDEN_ROOT` pointing away from the live garden, and `garden` run in a worktree refuses with a clear message.
- [ ] the brief tells workers not to run the garden against itself.
- [ ] a test for the boundary.
- [ ] a worker cannot change the garden's own `.venv`: workers run with their own environment and the brief says so.

## Out of scope

- Remote (ssh) worktrees, which live outside the garden already.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T18:59:59+00:00 dispatched work run 20260904T185958Z-work via local [claude model=sonnet] (fresh session, base main, ~2483 tokens)
