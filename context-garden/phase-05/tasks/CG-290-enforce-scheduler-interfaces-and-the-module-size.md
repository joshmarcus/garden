---
id: CG-290
title: Enforce scheduler interfaces and the module-size cap
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:15:10+00:00'
---

## Goal

Declare the shared scheduler helper interface, enforce the under-800-line goal, move continuation-related reprobe code into checkruns, and remove production wrappers retained only for old setup tests. Test behavior rather than literal CSS tokens, and keep the architecture module map current.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
