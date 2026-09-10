---
id: CG-581
title: Prevent folded rail stretching on short pages
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 4
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Check the specific tall-viewport short-page grid behavior reported by CG-308. If it persists, keep the rail at its intended content height without changing normal scrolling or mobile layout. Verify the affected short-page rendering proportionately rather than recapturing every page.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.
