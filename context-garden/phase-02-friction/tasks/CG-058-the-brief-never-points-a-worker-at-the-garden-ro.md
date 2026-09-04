---
id: CG-058
title: The brief never points a worker at the garden root
status: changes_requested
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/brief.py
branch: garden/cg-058-the-brief-never-points-a-worker-at-the-garden-ro
pr: https://github.com/joshmarcus/context-garden/pull/29
attempts: 1
last_dispatched_at: '2026-09-04T17:53:36+00:00'
created: '2026-09-04T17:53:36+00:00'
updated: '2026-09-04T17:58:22+00:00'
---

## Goal

Nothing in a worker's brief names or describes the garden's own checkout; every path is relative to the worker's current directory, which is its worktree.

## Context

During the first live run, workers for CG-043 and CG-045 edited `src/garden/inbox.py`, `scheduler.py`, `cli.py` and tests in the live checkout at `/home/joshua/context-garden` instead of in `.garden/worktrees/<id>`; one of them ran `git stash` there, which swept every task-file change the scheduler had made that day, and another re-pointed the shared `.venv`. Their briefs said, in the "read these" section: "Read them (paths relative to the context garden root `/home/joshua/context-garden`) before starting". A worker does what it is told: it changes directory to that root and works there. The fix is in `build_brief`: say "paths relative to your current directory" and never print the root. Add a rule to the operating rules: "Work only in the directory you were started in; do not change into any other checkout of this repository." CG-054 covers the harder boundary (root discovery, environment); this task removes the invitation.

## Acceptance criteria

- [ ] no brief contains the garden root path or the words "context garden root"; a test builds a brief with a large reading file and asserts.
- [ ] the operating rules tell the worker to stay in its starting directory.
- [ ] `docs/worker-protocol.md` says paths in the brief are relative to the worktree.

## Out of scope

- Root-discovery and environment isolation (CG-054).

## Log

- 2026-09-04T17:53:36+00:00 dispatched work run 20260904T175336Z-work via manual [human] (fresh session, base main, ~5168 tokens)
- 2026-09-04T17:57:33+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/29 (base main): The brief no longer names the garden root: reading-list paths are relative to the worker's current directory, the rules say to stay in it, and a test asserts no brief carries the root path.
- 2026-09-04T17:58:22+00:00 CI failure
