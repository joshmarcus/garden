---
id: CG-049
title: 'CLAUDE.md: document PYTHONPATH=src for manual test runs in worktrees'
status: done
product: context-garden
phase: phase-02-friction
depends_on:
- CG-081
priority: 2
difficulty: easy
reading:
- src/garden/runner/local.py
- src/garden/checks.py
- garden.yaml
branch: garden/cg-049-claude-md-document-pythonpath-src-for-manual-tes
pr: https://github.com/joshmarcus/context-garden/pull/62
discovered_from: CG-034
attempts: 1
last_dispatched_at: '2026-09-04T22:21:39+00:00'
created: '2026-09-04T17:34:19+00:00'
updated: '2026-09-04T23:58:12+00:00'
---

When running tests manually in a worktree with `pytest -q`, the `.venv` editable install loads from the main repo, not the worktree. The pre-PR check sets `PYTHONPATH=src` correctly, but this is not mentioned in CLAUDE.md. A one-liner noting `PYTHONPATH=src .venv/bin/pytest -q` prevents workers (and humans) from running tests that silently cover the wrong code.

CG-056 is folded in here: the `Tests:` line also assumes `.venv/bin/pytest` exists in the checkout, which it does not in a worktree. Write both lines after CG-081 lands, since CG-081 defines how a worktree's environment is prepared (`setup` block) and the doc should describe that, not a venv.

## Provenance

Discovered by CG-034 (Windows: run the harness by its resolved path and give pre-PR checks a shell) during run `20260904T172445Z-work`.

## Log

- 2026-09-04T17:34:19+00:00 discovered by CG-034
- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T22:21:39+00:00 dispatched work run 20260904T222130Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~7295 tokens)
- 2026-09-04T22:26:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/62 (base main): Updated CLAUDE.md's Tests line to use `PYTHONPATH=src .venv/bin/pytest -q`, and added a Worktrees bullet noting a worktree has no `.venv` until the product's `setup.command` runs (CG-081), folding in CG-056. cost=$1.13
- 2026-09-04T22:28:34+00:00 automated review: approve — One-line CLAUDE.md doc change documenting PYTHONPATH=src for manual worktree test runs and folding in CG-056; accurate, in scope, clean description. cost=$0.40
- 2026-09-04T23:58:12+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/62
