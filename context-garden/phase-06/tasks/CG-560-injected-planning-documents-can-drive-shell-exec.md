---
id: CG-560
title: Injected planning documents can drive shell execution with controller filesystem
status: cancelled
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:security:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:37:40.049556+00:00'
duplicate_of: CG-518
---

## Goal

Run planning in a dedicated enforced sandbox that cannot access controller state or credentials, and reject bypass permission modes for planning.

## Context

Raised by the security persona review (Planner isolation). persona:security:context-garden/phase-05.


## Reviewed disposition

Consolidated into CG-533 by the delegated operator after independent retro review. The original finding above remains preserved; its canonical owner carries the relevant correction or verification, so this does not create another implementation. CG-533 uses existing CG-517/518/519 and CG-504; CG-537 owns closing provenance and the actual owner decision.

## Log

- 2026-09-10T13:28:27.335304+00:00 cancelled as duplicate of CG-533; original finding retained.

- 2026-09-10T13:37:40.049556+00:00 owner cancelled CG-533 on the web; canonical implementation ownership now points directly to CG-518, with final accepted-source verification in CG-537. Preserve both cancellations and all original findings.
