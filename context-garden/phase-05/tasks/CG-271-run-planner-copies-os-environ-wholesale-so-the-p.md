---
id: CG-271
title: run_planner copies os.environ wholesale so the planner still sees the operator's
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-05T23:58:13+00:00'
updated: '2026-09-05T23:58:13+00:00'
discovered_from: persona:project-manager:context-garden/phase-04
---

## Goal

Route the planner call through runner.base.scrubbed_env with the harness config-dir defaults, and add a test asserting HOME is not the operator's.

## Context

Raised by the project-manager persona review (trust). persona:project-manager:context-garden/phase-04.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-260 (renumbered by the operator: two reconcile runs drew ids from one counter)
