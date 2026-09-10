---
id: CG-543
title: Make brief paths and validation scope truthful
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

User value: workers spend time on implementation rather than locating context that is already supplied. Why now: late CG-434/437 reports persist after brief-gate work. Size: medium. Dependencies: CG-293/294/483 and existing scope planning; distinguish inlined, controller-owned and checkout-readable content and refresh scope when behavior changes.

## Context

Proposed at the context-garden/phase-05 retro. Repeated late-phase context errors show that presence checks alone are insufficient.
