---
id: CG-580
title: Align QA request timeouts with advertised deadlines
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/interaction_replay.py
- src/garden/config.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

Check the reported thirty-second flow deadline versus ten-second request timeout on current source. Make the documented deadline and effective request budget consistent, preserving a finite bound and reporting which deadline expired. Retire the finding without a code change if the mismatch is already corrected.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Reproduce the named advertised-versus-effective timeout mismatch on current source, identify the flow and individual request deadline owners, and keep an explicit finite budget with accurate expiry diagnostics. If already aligned, retain source-specific verification and retire without an implementation rewrite. Use bounded fake clock/HTTP verification for a demonstrated correction.
