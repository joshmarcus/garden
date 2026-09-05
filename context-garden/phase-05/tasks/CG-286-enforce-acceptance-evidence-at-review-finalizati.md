---
id: CG-286
title: Enforce acceptance evidence at review finalization
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:15:10+00:00'
---

## Goal

A reviewer criterion with met:false or missing evidence must mechanically request changes rather than count as an approving round. Keep original criteria available to revisions and distinguish execution failures from product findings. Add regression cases based on CG-217's unevidenced criterion and CG-158's placeholder; depend on the common admission gate.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
