---
id: CG-542
title: Index durable remote claim request identities
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

User value: keep idle polling responsive as history grows. Why now: active-run filtering still follows a full-history request-identity lookup. Size: hard. Dependencies: CG-491/495 and current durable lease/replay rules; preserve rejection of stale, expired and replaced generations while avoiding terminal-history materialization.

## Context

Proposed at the context-garden/phase-05 retro. Remove the demonstrated historical scan without weakening idempotency or expanding the worker fleet.
