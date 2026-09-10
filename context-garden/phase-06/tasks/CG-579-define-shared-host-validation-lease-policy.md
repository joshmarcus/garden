---
id: CG-579
title: Define shared-host validation lease policy
status: draft
product: context-garden
phase: phase-06
depends_on:
- id: CG-365
  after: merge
priority: 3
difficulty: hard
reading:
- src/garden/validation.py
- src/garden/config.py
- src/garden/scheduler/resources.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

Specify one authoritative capacity policy for gardens sharing a user and lock namespace, including clear mismatch handling and a safe migration path. Preserve current process ownership and resource limits; do not raise capacity as part of the change.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Define the supported shared namespace identity, authority for capacity, behavior for conflicting configurations, owner-visible diagnosis and migration/recovery rules before changing enforcement. Preserve active leases and current aggregate caps across multiple gardens. Do not silently increase capacity or reinterpret another garden's lock. Test the agreed contract with isolated competing clients.
