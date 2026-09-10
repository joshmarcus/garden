---
id: CG-576
title: Deliver controller-owned CI diagnostics to isolated workers
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/checks.py
- src/garden/github.py
- src/garden/brief.py
- src/garden/scheduler/poll.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

Preserve credential isolation while making the actual failing node, command, source and readable diagnostic excerpt available to the assigned worker. Coordinate CG-396 status policy and CG-506 transport; address the specific repeated inaccessible-log failure, not another CI provider implementation. An authentication error alone must not be presented as a source-test failure.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Transfer only bounded sanitized diagnostic excerpts with the exact source/check/attempt identity through the current accepted worker briefing or diagnostic channel. Preserve credentials, token redaction and provider error typing; an authentication/transport failure is not a source-test failure. Coordinate CG-396 provider ownership and the owner-deferred CG-506 storage design without waiting for a new full-transcript transport or duplicating either implementation. Verify a failing check reaches its assigned isolated worker and cannot leak secrets or stale-source diagnostics.
