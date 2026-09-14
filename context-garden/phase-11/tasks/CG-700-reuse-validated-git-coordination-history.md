---
id: CG-700
title: Reuse validated Git coordination history
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 3
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

User value: authority checks remain responsive as the garden accumulates operations. Why now: every refresh validates history from its root. Size: medium. Dependencies: CG-631 and bounded transport. Cache immutable validated ancestry, batch reads and retain rewrite detection; define checkpoint and retention constraints that preserve ambiguous-operation resolution.

## Context

Proposed at the context-garden/phase-10 retro. Addressing demonstrable history-dependent work early avoids changing the coordination architecture later.
