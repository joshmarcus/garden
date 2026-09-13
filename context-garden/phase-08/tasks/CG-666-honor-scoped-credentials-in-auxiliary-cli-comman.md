---
id: CG-666
title: Honor scoped credentials in auxiliary CLI commands
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T16:57:41+00:00'
---

## Goal

User value: doctor tests the identity the product will actually use and friction collection cannot silently read under another identity. Why now: source and the Security persona's mocked probe show ambient gh fallback. Size: medium. Dependencies: existing CG-395/CG-515 scoped client construction. Reuse that construction and test missing or revoked scoped credentials with ambient gh present.

## Context

Proposed at the context-garden/phase-07 retro. Consistent credential selection closes an avoidable authority mismatch across existing entry points.
