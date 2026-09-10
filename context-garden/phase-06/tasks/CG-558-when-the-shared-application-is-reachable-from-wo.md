---
id: CG-558
title: 'When the shared application is reachable from worker networks, requests without '
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
duplicate_of: CG-517
---

## Goal

Expose only authenticated worker endpoints to worker networks and require separate operator authentication for all other routes.

## Context

Raised by the security persona review (Remote controller access). persona:security:context-garden/phase-05.


## Reviewed disposition

Consolidated into CG-533 by the delegated operator after independent retro review. The original finding above remains preserved; its canonical owner carries the relevant correction or verification, so this does not create another implementation. CG-533 uses existing CG-517/518/519 and CG-504; CG-537 owns closing provenance and the actual owner decision.

## Log

- 2026-09-10T13:28:27.335304+00:00 cancelled as duplicate of CG-533; original finding retained.

- 2026-09-10T13:37:40.049556+00:00 owner cancelled CG-533 on the web; canonical implementation ownership now points directly to CG-517, with final accepted-source verification in CG-537. Preserve both cancellations and all original findings.
