---
id: CG-562
title: Reading absent maintenance state marks an empty entry dirty, allowing a stale ti
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Make maintenance inspection read-only, create entries only during explicit mutations, and test the interleaved tick/request/save sequence.

## Context

Raised by the staff-engineer persona review (Maintenance concurrency). persona:staff-engineer:context-garden/phase-05.
