---
id: CG-097
title: Worktree setup sometimes skips creating .venv, breaking pre-PR checks
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
discovered_from: CG-090
created: '2026-09-04T21:03:37+00:00'
updated: '2026-09-04T21:10:47+00:00'
---

This task's worktree (CG-090) had no `.venv` directory at all, causing the pre-PR `tests`/`lint` checks to fail with exit 127 (`.venv/bin/pytest`/`.venv/bin/ruff` not found) even though the actual code fix was correct. Sibling worktrees (e.g. CG-037, CG-091) had a `.venv` created via `python3 -m venv .venv` at checkout time. Worth investigating whatever step provisions a task worktree's venv to see why it was skipped here, so future revision rounds don't get a spurious tooling failure unrelated to the task's code.

## Provenance

Discovered by CG-090 (State.save() never clears dirty keys after a successful write) during run `20260904T205855Z-revise`.

## Log

- 2026-09-04T21:03:37+00:00 discovered by CG-090
- 2026-09-04T21:10:47+00:00 cancelled (web)
