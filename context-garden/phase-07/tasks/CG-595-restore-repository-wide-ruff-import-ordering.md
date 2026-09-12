---
id: CG-595
title: Restore repository-wide Ruff import ordering
status: cancelled
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/runs.py
- src/garden/scheduler/fence.py
- src/garden/scheduler/state.py
- src/garden/config.py
discovered_from: CG-583
created: '2026-09-10T17:47:17+00:00'
updated: '2026-09-10T18:09:32+00:00'
file: src/garden/runner/local.py
error: 'Ruff I001: import block is unsorted'
---

Move the `workload_identity` import above the relative `.base` import block in `src/garden/runner/local.py` so the repository-wide Ruff command is clean. The defect is present unchanged on origin/main and is unrelated to CG-583.

## Provenance

Discovered by CG-583 (Archive and deduplicate run history without losing recovery or accounting) during run `20260910T172402Z-revise`.
## Log
- 2026-09-10T17:47:17+00:00 discovered by CG-583
- 2026-09-10T18:09:32+00:00 Duplicate of approved CG-593, which already owns this exact merged-main workload_identity import-order failure and its current-head CI repair. Preserve this original discovery/provenance; coordinate downstream rebase onto593 after actual merge instead of implementing another copy.
