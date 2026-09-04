---
id: CG-114
title: Per-worktree test environment so pytest imports the local src
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/inbox.py
- src/garden/web/templates/inbox.html
- docs/worker-protocol.md
discovered_from: CG-112
created: '2026-09-04T21:53:33+00:00'
updated: '2026-09-04T22:03:22+00:00'
---

## Goal

Running `pytest` in a task worktree imports `garden` from whichever worktree the editable install last pointed at (observed: `.garden/worktrees/CG-042/src/garden`), and `.venv/bin/pytest` referenced in CLAUDE.md does not exist in a fresh worktree. Workers can unknowingly test against stale code.

## Context

Seen while running CG-112's checks: coordination tests appeared to fail and new methods appeared missing until `PYTHONPATH=src` was forced. Consider a prepared per-worktree venv, or a `conftest.py` that prepends the worktree `src` to `sys.path`, plus aligning the CLAUDE.md test command with what the harness actually prepares.

## Provenance

Discovered by CG-112 (A worker's discovery can be a decision for the person, not only a new task) during run `20260904T214026Z-work`.

## Log

- 2026-09-04T21:53:33+00:00 discovered by CG-112
- 2026-09-04T22:03:22+00:00 covered by CG-081 (PR #48): the per-product setup block prepares each worktree's environment, including the tests importing the worktree's own src
