---
id: CG-042
title: Say when the garden's own state edits get committed
status: awaiting_triage
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- docs/architecture.md
- src/garden/store.py
branch: garden/cg-042-say-when-the-garden-s-own-state-edits-get-commit
pr: https://github.com/joshmarcus/context-garden/pull/23
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T17:36:40+00:00'
created: '2026-09-04T17:03:10+00:00'
updated: '2026-09-04T17:46:49+00:00'
---

## Goal

The task-file edits the scheduler makes in the main checkout (status, attempts, log lines) reach git on purpose, not by accident.

## Context

On CG-027 `set-status`, `take`, `approve` and every tick edited task files in the main checkout, which sat uncommitted the whole run; worker branches are cut from `origin/main`, so those edits never ride a PR. Moving to a second machine lost the first machine's history, and nothing in the docs says when a person should commit `tasks/`. Decide: a `garden commit` (or `--commit` on tick) that commits task-file changes to the base branch with a fixed message, or a documented rule that the human commits after each session. Write it into `docs/architecture.md`.

## Acceptance criteria

- [ ] one documented way for task-file state to reach git.
- [ ] if it is a command, a test; if it is a rule, the Inbox or `garden status` shows uncommitted task files.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:10+00:00 discovered by CG-027
- 2026-09-04T17:23:54+00:00 approved (web)
- 2026-09-04T17:36:40+00:00 dispatched work run 20260904T173639Z-work via local [claude model=sonnet] (fresh session, base main, ~9018 tokens)
- 2026-09-04T17:43:56+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/23 (base main): Added `garden commit` command that stages modified task files (under **/tasks/*.md) and commits them with message 'garden: update task state'. `garden status` now warns when task files have uncommitted changes. Documented the pattern in docs/architecture.md under a new '### Committing task state' subsection. cost=$1.41
- 2026-09-04T17:46:49+00:00 automated review: approve — All acceptance criteria met: `garden commit` command with 10 passing tests, `garden status` warning, and `docs/architecture.md` documentation. Full suite (129 tests) passes with no regressions. cost=$0.26
