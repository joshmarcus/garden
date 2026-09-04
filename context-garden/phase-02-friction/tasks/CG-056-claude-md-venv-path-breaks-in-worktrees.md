---
id: CG-056
title: CLAUDE.md venv path breaks in worktrees
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/plants.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
discovered_from: CG-031
created: '2026-09-04T17:46:05+00:00'
updated: '2026-09-04T21:26:18+00:00'
---

The CLAUDE.md `Tests:` line says `.venv/bin/pytest -q`, which assumes the reader is in the repo root. In a git worktree the `.venv` symlink does not exist, so the command fails with 'No such file or directory'. The fix is to use an absolute path or note that workers should look for the venv at the repo root.

## Provenance

Discovered by CG-031 (Draw the done stage as a red apple) during run `20260904T173916Z-work`.

## Log

- 2026-09-04T17:46:05+00:00 discovered by CG-031
- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T21:26:18+00:00 folded into CG-049: both are the CLAUDE.md test line in a worktree; CG-049 now waits for CG-081, which prepares the worktree environment
