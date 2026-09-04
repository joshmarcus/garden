---
id: CG-051
title: Worktree tests need PYTHONPATH or a per-worktree venv
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/inbox.py
- src/garden/cli.py
discovered_from: CG-035
created: '2026-09-04T17:35:40+00:00'
updated: '2026-09-04T18:41:38+00:00'
---

Running `.venv/bin/pytest` fails in worktrees because there is no `.venv` under the worktree. Tests must be run with `PYTHONPATH=<worktree>/src /home/joshua/context-garden/.venv/bin/pytest`. The brief and CLAUDE.md both say `.venv/bin/pytest -q` without noting this worktree limitation. Consider adding a `conftest.py` or `pytest.ini` path config, or a `Makefile` target that handles it.

**Why:** Workers running from worktrees hit confusing import errors.

**How to apply:** Fix by adding `pythonpath = src` to `pyproject.toml`'s `[tool.pytest.ini_options]` so `pytest` from any directory finds the worktree source.

## Provenance

Discovered by CG-035 (Inbox and digest show what actually happened to a task) during run `20260904T172446Z-work`.

## Log

- 2026-09-04T17:35:40+00:00 discovered by CG-035
- 2026-09-04T18:41:38+00:00 approved
