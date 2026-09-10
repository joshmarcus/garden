---
id: CG-559
title: An unmerged scripted SVG is served without CSP sandboxing and can execute in the
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:security:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Apply CSP sandboxing to every raw design response, add nosniff, and serve unsupported formats as downloads.

## Context

Raised by the security persona review (Design artifact serving). persona:security:context-garden/phase-05.
