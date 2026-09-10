---
id: CG-561
title: Malformed state JSON silently becomes an empty side-store and can be overwritten
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

Preserve corrupt state, refuse scheduling mutations with an actionable diagnosis, and add load-time and save-time corruption regressions.

## Context

Raised by the staff-engineer persona review (State integrity). persona:staff-engineer:context-garden/phase-05.
