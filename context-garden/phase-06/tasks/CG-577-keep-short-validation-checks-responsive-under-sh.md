---
id: CG-577
title: Keep short validation checks responsive under shared admission
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Measure and distinguish queue wait from execution time for short lint and focused checks. Reuse existing resource controls and investigate bounded admission or lease scoping so waiting for external CI does not monopolize local capacity. Preserve all host caps and avoid stress workloads in ordinary tests.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.
