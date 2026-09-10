---
id: CG-542
title: Index durable remote claim request identities
status: draft
product: context-garden
phase: phase-06
depends_on:
- id: CG-491
  after: merge
- id: CG-495
  after: merge
- id: CG-496
  after: merge
priority: 3
difficulty: hard
reading:
- src/garden/runs.py
- src/garden/remote_worker.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

User value: keep idle polling responsive as history grows. Why now: historical evidence suggests a residual request-identity lookup cost that must be measured on current accepted source. Size: hard. Dependencies: CG-491/495 and current durable lease/replay rules; preserve rejection of stale, expired and replaced generations while avoiding terminal-history materialization.

## Context

Proposed at the context-garden/phase-05 retro. Measure and remove any remaining material historical lookup cost without weakening idempotency or expanding the worker fleet.


## Reviewed scope and verification

CG-495 already removed the unconditional full-history deep copy from active selection. First measure the remaining current-source claim/request-identity and replay lookup, including index refresh boundaries; report the source and which path scales with historical runs. If a material residual cost remains, index the required durable identities and preserve restart, stale/expired/replaced generations, collision handling and exactly-once accepted results. Use a bounded history-growth regression; do not restate the obsolete unconditional-copy finding or weaken fencing. Retire with evidence if current accepted source already satisfies the intended bound.
