---
id: CG-697
title: Bound Git transport and recover ambiguous pushes
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

User value: a slow remote produces a recoverable state instead of a frozen scheduler. Why now: Git subprocesses have no deadlines. Size: hard. Dependencies: CG-631 and CG-632. Apply total operation deadlines, noninteractive authentication and descendant cleanup; reconcile interrupted pushes through their existing operation IDs before permitting effects.

## Context

Proposed at the context-garden/phase-10 retro. The existing recovery protocol cannot help until stalled transport returns control.
