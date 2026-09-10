---
id: CG-561
title: Malformed state JSON silently becomes an empty side-store and can be overwritten
status: cancelled
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
duplicate_of: CG-534
---

## Goal

Preserve corrupt state, refuse scheduling mutations with an actionable diagnosis, and add load-time and save-time corruption regressions.

## Context

Raised by the staff-engineer persona review (State integrity). persona:staff-engineer:context-garden/phase-05.


## Reviewed disposition

Consolidated into CG-534 by the delegated operator after independent retro review. The original finding above remains preserved; its canonical owner carries the relevant correction or verification, so this does not create another implementation. CG-533 uses existing CG-517/518/519 and CG-504; CG-537 owns closing provenance and the actual owner decision.

## Log

- 2026-09-10T13:28:27.335304+00:00 cancelled as duplicate of CG-534; original finding retained.
