---
id: CG-664
title: Fence canonical checkout recovery until writers stop
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T16:57:41+00:00'
---

## Goal

User value: retries cannot overlap a timed-out reconciliation writer and damage a shared checkout. Why now: the staff review's harmless probe and current exception path establish a concrete ownership gap. Size: hard. Dependencies: existing CG-406 checkout leases and process supervision. Terminate and reap owned descendants before releasing the lease; retain an actionable fenced state when cleanup cannot be confirmed.

## Context

Proposed at the context-garden/phase-07 retro. This closes a demonstrated data-integrity gap before users rely on opt-in canonical execution.
