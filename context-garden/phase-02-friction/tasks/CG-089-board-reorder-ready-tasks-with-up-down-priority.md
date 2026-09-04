---
id: CG-089
title: 'Board: reorder ready tasks with up/down priority controls'
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/cli.py
- src/garden/web/app.py
discovered_from: CG-071
created: '2026-09-04T19:51:41+00:00'
updated: '2026-09-04T20:16:10+00:00'
---

## Goal

The Board's ready column has up and down controls that change a task's priority relative to its neighbours, using the priority action from CG-071.

## Context

Split out of CG-071, which delivered the CLI commands and the task-page controls.

## Acceptance criteria

- [ ] up/down on a ready card swaps its priority with the neighbour and the column re-sorts.
- [ ] a test for the route.

## Provenance

Discovered by CG-071 (Set a task's priority and difficulty from the CLI and the task page) during run `20260904T194657Z-work`.

## Log

- 2026-09-04T19:51:41+00:00 discovered by CG-071
- 2026-09-04T20:16:10+00:00 approved (web)
