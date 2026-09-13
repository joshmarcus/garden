---
id: CG-667
title: Make command CI asynchronous and resource bounded
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T16:57:41+00:00'
---

## Goal

User value: a slow or noisy adapter cannot stall unrelated work or consume unbounded controller memory. Why now: queries run synchronously under the controller lock and output is capped only after buffering. Size: hard. Dependencies: existing command-CI exact-head contract and detached-work/process supervision. Consume bounded stdout and stderr, terminate owned processes on timeout or overflow, and accept results only for the unchanged source and provider policy.

## Context

Proposed at the context-garden/phase-07 retro. Enterprise adapter failures should remain isolated while exact-head merge protection stays intact.
