---
id: CG-252
title: Make operating profiles harness-aware and consistently named
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

User value: a profile switch selects runnable models on the user's configured harness and clearly describes its effect. Why now: built-in Claude identifiers are applied to Codex gardens and economy's hard-tier choice lacks outcome evidence. Size: medium. Dependencies: merged CG-221 and the cost baseline. Reference per-harness tier maps, reject incompatible combinations, retain safe defaults, distinguish operating profile from observation feed, remove task IDs from copy and reconcile the retro column and live/restart lists.

## Context

Proposed at the context-garden/phase-04 retro. Profiles must be valid for the installed harness before users can safely use the operating-point control.
