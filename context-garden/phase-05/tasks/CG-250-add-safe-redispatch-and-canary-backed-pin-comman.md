---
id: CG-250
title: Add safe redispatch and canary-backed pin commands
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

User value: replace recurring hand sequences with observable operations that preserve work and prevent competing workers. Why now: a superseded worker reportedly spent $4.34 without a PR. Size: medium. Dependencies: merged CG-180, CG-198 and CG-220, plus the phase-04 dispatch-concurrency blocker. Plan two sequenced slices: redispatch terminates and confirms exit of the previous process tree before reuse; pin checks the candidate, installs it and restarts at a tick boundary with failure recovery.

## Context

Proposed at the context-garden/phase-04 retro. These commands eliminate demonstrated operator effort and wasted runs after their safety prerequisites land.
