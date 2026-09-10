---
id: CG-579
title: Define shared-host validation lease policy
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: hard
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Specify one authoritative capacity policy for gardens sharing a user and lock namespace, including clear mismatch handling and a safe migration path. Preserve current process ownership and resource limits; do not raise capacity as part of the change.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.
