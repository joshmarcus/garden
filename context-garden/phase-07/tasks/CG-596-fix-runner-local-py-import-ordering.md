---
id: CG-596
title: Fix runner/local.py import ordering
status: cancelled
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/config.py
- src/garden/scheduler/dispatch.py
- src/garden/store.py
discovered_from: CG-586
created: '2026-09-10T17:52:08+00:00'
updated: '2026-09-10T18:09:32+00:00'
file: src/garden/runner/local.py
error: 'ruff I001: Import block is un-sorted or un-formatted'
---

The required repository-wide Ruff command reports I001 because the workload_identity import follows the local .base import block. Reorder that unchanged module's imports in a separate cleanup.

## Provenance

Discovered by CG-586 (Configure sequential phase execution, one phase at a time) during run `20260910T173951Z-work`.
## Log
- 2026-09-10T17:52:08+00:00 discovered by CG-586
- 2026-09-10T18:09:32+00:00 Duplicate of approved CG-593, which already owns this exact merged-main workload_identity import-order failure and its current-head CI repair. Preserve this original discovery/provenance; coordinate downstream rebase onto593 after actual merge instead of implementing another copy.
