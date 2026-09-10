---
id: CG-582
title: Separate expected SSE shutdown from application errors
status: draft
product: context-garden
phase: phase-06
depends_on:
- id: CG-524
  after: merge
priority: 4
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/pages/events.py
- src/garden/events.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

Reduce benign cancellation traceback noise during controlled disposal of servers with open event streams. Preserve real application failures and enforce bounded shutdown. Coordinate with CG-524's existing historical harness consolidation rather than introducing another task-specific capture framework.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Reproduce controlled shutdown with an open event stream on current source and distinguish expected cancellation/disconnect from real handler exceptions. Suppress only benign diagnostics while preserving actionable failures and bounded termination. Coordinate the existing harness consolidation and validate the actual affected shutdown path with a disposable server.
