---
id: CG-538
title: Explain accepted completion before historical reviews
status: draft
product: context-garden
phase: phase-06
depends_on:
- id: CG-362
  after: merge
- id: CG-487
  after: merge
- id: CG-536
  after: merge
priority: 1
difficulty: medium
reading:
- src/garden/web/pages/task.py
- src/garden/web/templates/task.html
- src/garden/scheduler/human.py
- src/garden/runs.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

User value: understand why a task is complete without reconstructing its timeline. Why now: three personas found historical rejection presented as current. Size: medium. Dependencies: existing completion provenance, CG-362/487 and the canonical acceptance correction; retain complete dated, source-specific findings.

## Context

Proposed at the context-garden/phase-05 retro. Clear completion provenance makes the existing workflow understandable without weakening review history.


## Reviewed scope and verification

Present the current accepted completion and its source/reason first, then retain historical reviews, failures and interventions as dated history. Distinguish reviewed/merged acceptance, explicit owner acceptance and forced status completion according to CG-536. Verify that historical rejection does not falsely describe the current outcome, while every original finding remains accessible. Absorb CG-551 completion presentation; check-run presentation remains CG-539.
