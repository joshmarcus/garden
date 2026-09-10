---
id: CG-581
title: Prevent folded rail stretching on short pages
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 4
difficulty: easy
reading:
- src/garden/web/templates/base.html
- src/garden/web/pages/now1.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

Check the specific tall-viewport short-page grid behavior reported by CG-308. If it persists, keep the rail at its intended content height without changing normal scrolling or mobile layout. Verify the affected short-page rendering proportionately rather than recapturing every page.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Reproduce the precise folded-rail stretch on a short page in a tall viewport against current accepted source. If present, repair that layout while preserving ordinary scrolling and the mobile layout; inspect only representative affected views. If current source already fixes it, retire with the observed source/page result and no unnecessary rewrite.
