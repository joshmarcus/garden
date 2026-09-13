---
id: CG-669
title: Local reconciliation can leave a child running after timeout while the scheduler
status: draft
product: context-garden
phase: phase-08
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-07
created: '2026-09-13T16:57:41+00:00'
updated: '2026-09-13T16:57:41+00:00'
---

## Goal

In src/garden/canonical.py:114, supervise reconciliation descendants and confirm termination before returning a timeout; in Scheduler.prepare_canonical_run, retain ownership if cleanup is uncertain. Extend tests/test_canonical.py beyond exception and lease-reuse assertions to prove a timed-out child cannot continue writing after replacement admission. A read-only probe confirmed reconciliation returned after 1.0 second while its harmless child remained alive; the probe explicitly terminated that child.

## Context

Raised by the staff-engineer persona review (Canonical checkout recovery). persona:staff-engineer:context-garden/phase-07.
