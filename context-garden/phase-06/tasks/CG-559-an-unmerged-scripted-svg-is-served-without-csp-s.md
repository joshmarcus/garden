---
id: CG-559
title: An unmerged scripted SVG is served without CSP sandboxing and can execute in the
status: cancelled
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:security:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
duplicate_of: CG-533
---

## Goal

Apply CSP sandboxing to every raw design response, add nosniff, and serve unsupported formats as downloads.

## Context

Raised by the security persona review (Design artifact serving). persona:security:context-garden/phase-05.


## Reviewed disposition

Consolidated into CG-533 by the delegated operator after independent retro review. The original finding above remains preserved; its canonical owner carries the relevant correction or verification, so this does not create another implementation. CG-533 uses existing CG-517/518/519 and CG-504; CG-537 owns closing provenance and the actual owner decision.

## Log

- 2026-09-10T13:28:27.335304+00:00 cancelled as duplicate of CG-533; original finding retained.
