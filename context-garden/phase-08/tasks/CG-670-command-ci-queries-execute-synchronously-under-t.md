---
id: CG-670
title: Command CI queries execute synchronously under the controller lock, so an unavai
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T16:57:41+00:00'
---

## Goal

Move command observations outside the controller critical section using the existing detached-work approach, then consume results bound to provider policy and exact SHA. src/garden/ci_status.py:269 defaults to a 120-second query budget and permits 3600 seconds; tick-level caching does not bound a pass across distinct heads. Add a small deterministic test proving a stalled adapter does not delay unrelated result collection or a locked operator action, and that late results cannot qualify a changed head.

## Context

Raised by the staff-engineer persona review (Controller responsiveness). persona:staff-engineer:context-garden/phase-07.
