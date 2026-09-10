---
id: CG-580
title: Align QA request timeouts with advertised deadlines
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Check the reported thirty-second flow deadline versus ten-second request timeout on current source. Make the documented deadline and effective request budget consistent, preserving a finite bound and reporting which deadline expired. Retire the finding without a code change if the mismatch is already corrected.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.
