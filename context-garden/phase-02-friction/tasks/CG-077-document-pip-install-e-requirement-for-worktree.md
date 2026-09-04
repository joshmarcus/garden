---
id: CG-077
title: Document pip install -e requirement for worktree development
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/cli.py
- src/garden/github.py
- src/garden/runner/local.py
discovered_from: CG-032
created: '2026-09-04T19:02:59+00:00'
updated: '2026-09-04T19:07:27+00:00'
---

## Goal

CLAUDE.md for the worktree says to run tests with `.venv/bin/pytest` but workers find the garden's `.garden/.venv` doesn't have the worktree code installed editably. Add a note that `pip install -e '.[dev]'` must be run against the garden's venv before running tests in a worktree, or change the approach to use a separate venv per worktree.

## Provenance

Discovered by CG-032 (Doctor checks that gh and the harness are logged in and git has an identity) during run `20260904T185152Z-revise`.

## Log

- 2026-09-04T19:02:59+00:00 discovered by CG-032
- 2026-09-04T19:07:27+00:00 cancelled (web)
