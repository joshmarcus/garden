---
id: CG-066
title: garden usage shows the phase header and brief estimates before any run
status: running
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/cli.py
- src/garden/brief.py
branch: garden/cg-066-garden-usage-shows-the-phase-header-and-brief-es
attempts: 1
last_dispatched_at: '2026-09-04T23:13:34+00:00'
created: '2026-09-04T18:35:09+00:00'
updated: '2026-09-04T23:13:34+00:00'
---

## Goal

`garden usage product/phase` prints the phase's fixed-cost header and one row per task with its brief estimate even when no run has happened yet, so context bloat is visible before dispatch.

## Context

Codex review on PR #7 (CG-012), dropped at the time: the header and the estimates are produced inside the loop over `RunStore.usage_by_task()`, so a phase with no run records prints neither, and unrun tasks never appear. Derive the header from the selected phase and iterate the phase's tasks, joining usage where it exists.

## Acceptance criteria

- [ ] on a phase with no runs, the header and every task's brief estimate are printed.
- [ ] tasks with runs keep their actual tokens and cost beside the estimate.
- [ ] a test with an empty run store.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T23:13:34+00:00 dispatched work run 20260904T231325Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~5830 tokens)
