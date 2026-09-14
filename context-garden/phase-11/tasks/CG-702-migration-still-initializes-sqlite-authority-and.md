---
id: CG-702
title: Migration still initializes SQLite authority, and standalone export does not che
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

Replace the coordinator-dependent preview/commit/export paths in src/garden/migration.py:131-173,218-225,257-266 with the accepted Git protocol. Normal enrollment clears coordinator_url, while preview requires it and startup rejects it. Make reversal require authoritative Git quiescence and preserve unresolved obligations. Add CLI-boundary tests for Git-only migration, interrupted commit recovery, and refusal to export while another installation retains a pending permit.

## Context

Raised by the staff-engineer persona review (Migration and recovery). persona:staff-engineer:context-garden/phase-10.
