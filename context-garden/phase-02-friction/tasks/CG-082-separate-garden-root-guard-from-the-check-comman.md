---
id: CG-082
title: Separate GARDEN_ROOT (guard) from the check-command venv path variable
status: running
product: context-garden
phase: phase-02-friction
depends_on:
- CG-054
priority: 0
difficulty: easy
reading:
- src/garden/store.py
- src/garden/runner/local.py
- src/garden/brief.py
branch: garden/cg-082-separate-garden-root-guard-from-the-check-comman
discovered_from: CG-054
attempts: 1
last_dispatched_at: '2026-09-04T19:36:27+00:00'
created: '2026-09-04T19:18:10+00:00'
updated: '2026-09-04T19:38:28+00:00'
---

## Goal

`check_ctx` sets `GARDEN_ROOT` to the live garden so check commands can use `$GARDEN_ROOT/.venv/bin/python`. This dual use (venv locator + find_root guard) is fragile. Introduce a dedicated `GARDEN_EXEC_ROOT` (or similar) in `check_ctx` for the venv path, set `GARDEN_ROOT` to a non-existent sentinel for pre-PR check subprocesses too, and update the default check command template and documentation.

## Context

The current workaround (ignore valid GARDEN_ROOT in find_root) is correct but creates a subtle asymmetry: GARDEN_ROOT is documented as a redirect but only works as a raise-guard now. Cleaning this up requires changing the check command in garden.yaml, which is user config outside the tool source.

## Provenance

Discovered by CG-054 (A worker's worktree must never act on the live garden) during run `20260904T190809Z-revise`.

## Log

- 2026-09-04T19:18:10+00:00 discovered by CG-054
- 2026-09-04T19:24:42+00:00 approved (web)
- 2026-09-04T19:32:47+00:00 dispatched work run 20260904T193247Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8324 tokens)
- 2026-09-04T19:34:51+00:00 worker blocked: CG-082 depends on the GARDEN_ROOT guard from CG-054, which only exists on the still-open, unmerged PR #35 (branch garden/cg-054-...); main and this branch have no GARDEN_ROOT handling in find_root() at all, so there is nothing to separate yet. cost=$1.04
- 2026-09-04T19:35:06+00:00 reset to ready by hand
- 2026-09-04T19:36:27+00:00 dispatched work run 20260904T193626Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-054-a-worker-s-worktree-must-never-act-on-the-live-g stacked on CG-054, ~8590 tokens)
- 2026-09-04T19:38:28+00:00 parent CG-054 merged; will rebase onto main when the current run finishes
