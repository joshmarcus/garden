---
id: CG-698
title: Verify the supported Git multiplayer journey
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 2
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

User value: confidence that normal migration, startup and two independent schedulers work together. Why now: CG-640's headline journeys still inject HTTP/SQLite authority. Size: hard. Dependencies: Git migration repair and delivered CG-631 through CG-640. Use independent roots and a disposable bare remote through supported configuration and scheduler entry points, covering contention, restart, partition, late results, acknowledged handoff and phase closure.

## Context

Proposed at the context-garden/phase-10 retro. A bounded integrated journey connects strong protocol tests to the product users actually start.
