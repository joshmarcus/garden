---
id: CG-543
title: Make brief paths and validation scope truthful
status: draft
product: context-garden
phase: phase-06
depends_on:
- id: CG-293
  after: merge
- id: CG-294
  after: merge
- id: CG-483
  after: merge
priority: 2
difficulty: medium
reading:
- src/garden/brief.py
- src/garden/scheduler/dispatch.py
- src/garden/validation.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

User value: workers spend time on implementation rather than locating context that is already supplied. Why now: late CG-434/437 reports persist after brief-gate work. Size: medium. Dependencies: CG-293/294/483 and existing scope planning; distinguish inlined, controller-owned and checkout-readable content and refresh scope when behavior changes.

## Context

Proposed at the context-garden/phase-05 retro. Repeated late-phase context errors show that presence checks alone are insufficient.


## Reviewed scope and verification

Make the brief distinguish inlined content, checkout-readable files and controller-owned references, with a usable source/context location for each. Keep a genuinely absent required input actionable and preserve configured validation scope. Verify representative garden and product references, unavailable paths, inlined large files and scope refresh without requesting nonexistent checkout paths or requiring unrelated evidence.
