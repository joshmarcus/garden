---
id: CG-295
title: Validate persona-run provenance and scrub notifications
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

Validate persona footer run IDs and enforce containment within runs.dir, persist explicit phase identity for persona lookup, and run notify.command with a scrubbed environment plus explicitly supplied GARDEN variables. Preserve phase history without trusting arbitrary markdown-derived paths. Coordinate notification delivery policy with the cancelled CG-206 rather than silently resurrecting it.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
