---
id: CG-289
title: Make check continuations explicit and recoverable
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:15:10+00:00'
---

## Goal

Introduce a typed continuation with a stage enum and serialization checks, retain check_run until successful handling, and surface handler failure as a recoverable task state. Consolidate mirrored post-check and reprobe tails. Add interruption and handler-failure coverage and document run.save, event emission and state.save ordering.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
