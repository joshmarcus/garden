---
id: CG-539
title: Show check commands and outcomes on run pages
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/web/pages/runs.py
- src/garden/checkrun.py
- src/garden/checks.py
- src/garden/runs.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

User value: distinguish a finished process from successful validation and see the next action. Why now: generic transcript fallback hides the result of ordinary checks. Size: medium. Dependencies: existing check records and CG-506 for remote transport where needed; reuse available diagnostics without requiring new artifact formats.

## Context

Proposed at the context-garden/phase-05 retro. Actionable check results remove repeated investigation from the most common recovery journey.


## Reviewed scope and verification

Use existing accepted check records to show command, source identity, exit/conclusion, useful diagnostics and available next action. Distinguish process completion from check success and retain uncertainty for incomplete records. This display change does not wait for CG-506: the owner deferred that transcript-storage design. Reuse current records and expose a compatible boundary for any future accepted transport. Verify success/failure/incomplete check pages proportionately.
