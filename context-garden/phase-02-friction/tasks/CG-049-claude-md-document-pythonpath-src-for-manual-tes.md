---
id: CG-049
title: 'CLAUDE.md: document PYTHONPATH=src for manual test runs in worktrees'
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/runner/local.py
- src/garden/checks.py
- garden.yaml
discovered_from: CG-034
created: '2026-09-04T17:34:19+00:00'
updated: '2026-09-04T17:34:19+00:00'
---

When running tests manually in a worktree with `pytest -q`, the `.venv` editable install loads from the main repo, not the worktree. The pre-PR check sets `PYTHONPATH=src` correctly, but this is not mentioned in CLAUDE.md. A one-liner noting `PYTHONPATH=src .venv/bin/pytest -q` prevents workers (and humans) from running tests that silently cover the wrong code.

## Provenance

Discovered by CG-034 (Windows: run the harness by its resolved path and give pre-PR checks a shell) during run `20260904T172445Z-work`.

## Log

- 2026-09-04T17:34:19+00:00 discovered by CG-034
