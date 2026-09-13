---
id: CG-666
title: Honor scoped credentials in auxiliary CLI commands
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: medium
reading:
- context-garden/phase-08/goals.md
- src/garden/cli/planning.py
- src/garden/cli/diagnostics.py
- src/garden/github.py
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T17:05:13+00:00'
---

## Goal

User value: doctor tests the identity the product will actually use and friction collection cannot silently read under another identity. Why now: source and the Security persona's mocked probe show ambient gh fallback. Size: medium. Dependencies: existing CG-395/CG-515 scoped client construction. Reuse that construction and test missing or revoked scoped credentials with ambient gh present.

## Context

Proposed at the context-garden/phase-07 retro. Consistent credential selection closes an avoidable authority mismatch across existing entry points.

## Acceptance criteria

- [ ] Route friction collection and product doctor checks through the same explicit host/token policy as ordinary scheduler operations. The requested scoped credential is the one actually used.
- [ ] With a scoped token missing/revoked and ambient gh authenticated, these entry points fail closed with a useful diagnostic instead of falling back to the ambient identity; legacy unscoped use remains supported.
- [ ] Exercise the actual CLI client-construction paths with synthetic credentials/transport observations without contacting private services, exposing tokens or widening permissions.

## Planning boundary

Retrospective draft in frozen Phase08; no implementation approval, runtime activation, private-data access, new workers or spending is implied. Address each outcome with meaningful observations; alternate evidence and reasoned criteria amendments are welcome. Preserve substantive findings and avoid process-only author rounds.
