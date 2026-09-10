---
id: CG-560
title: Injected planning documents can drive shell execution with controller filesystem
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

Run planning in a dedicated enforced sandbox that cannot access controller state or credentials, and reject bypass permission modes for planning.

## Context

Raised by the security persona review (Planner isolation). persona:security:context-garden/phase-05.
