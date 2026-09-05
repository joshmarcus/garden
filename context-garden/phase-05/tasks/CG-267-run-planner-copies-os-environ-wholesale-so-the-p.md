---
id: CG-267
title: run_planner copies os.environ wholesale so the planner still sees the operator's
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:project-manager:context-garden/phase-04
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:15:10+00:00'
---

## Goal

Route the planner call through runner.base.scrubbed_env with the harness config-dir defaults, and add a test asserting HOME is not the operator's.

## Context

Raised by the project-manager persona review (trust). persona:project-manager:context-garden/phase-04.
