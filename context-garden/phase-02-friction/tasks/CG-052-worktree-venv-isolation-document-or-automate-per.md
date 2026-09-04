---
id: CG-052
title: 'Worktree venv isolation: document or automate per-worktree install'
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/review.py
discovered_from: CG-038
created: '2026-09-04T17:38:41+00:00'
updated: '2026-09-04T17:38:41+00:00'
---

## Goal

Workers in new worktrees silently test against whatever version of garden is installed in the shared `.venv`, not their own changes. This caused a confusing test run where all tests appeared to pass even though the code changes had not been picked up.

## Context

The shared `.venv` at the garden root is installed editable against whichever worktree last ran `pip install -e .`. A new worktree must create its own `.venv` to test its own changes. CLAUDE.md says `uv venv && uv pip install -e ".[dev]"` but does not clarify that this must be done *inside the worktree*, and `uv` is not always on PATH.

Possible fixes: add a note to CLAUDE.md, add a `check_env.sh` that detects the mismatch, or have the garden runner create the worktree venv automatically.

## Provenance

Discovered by CG-038 (Stall detection judges a description-only round by the description) during run `20260904T172447Z-work`.

## Log

- 2026-09-04T17:38:41+00:00 discovered by CG-038
