---
id: CG-582
title: Separate expected SSE shutdown from application errors
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 4
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Reduce benign cancellation traceback noise during controlled disposal of servers with open event streams. Preserve real application failures and enforce bounded shutdown. Coordinate with CG-524's existing historical harness consolidation rather than introducing another task-specific capture framework.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.
