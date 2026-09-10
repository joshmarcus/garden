---
id: CG-540
title: Reconcile deferred notices and attention ownership
status: draft
product: context-garden
phase: phase-06
depends_on:
- id: CG-437
  after: merge
- id: CG-480
  after: merge
priority: 2
difficulty: medium
reading:
- src/garden/inbox.py
- src/garden/web/pages/inbox.py
- src/garden/web/pages/task.py
- src/garden/scheduler/human.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

User value: a saved deferral stops demanding a decision while preserving the execution hold. Why now: persona observations disagree across snapshots. Size: medium. Dependencies: CG-437, CG-480 and current shared attention logic; first establish which current states are wrong, then align notices, badges and reconsider actions.

## Context

Proposed at the context-garden/phase-05 retro. Resolve observed ownership inconsistencies with current behavior rather than replaying an older UI assessment.


## Reviewed scope and verification

First reproduce a concrete discrepancy on current accepted source: compare saved deferral, current effective policy/source, badge count, next action and execution hold. Preserve separately owned holds and allow deliberate reconsideration. Consolidate CG-552 effective-rule/source clarity here, coordinating existing CG-514 policy ownership rather than adding another review-count mechanism. Make only demonstrated corrections, or record the finding as already resolved with source-specific evidence.
