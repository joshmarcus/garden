---
id: CG-435
title: Investigate LocalRunner supervisor completion hang
status: cancelled
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
discovered_from: CG-411
created: '2026-09-08T15:50:43+00:00'
updated: '2026-09-08T16:05:24+00:00'
file: src/garden/run_supervisor.py
error: Supervised full pytest remained blocked for more than eight minutes in the LocalRunner completion
  test until terminated.
---

The full ordinary suite hangs in `tests/test_runners.py::test_local_runner_launch_flips_process_finished`: its `sleep 0.5; cat` child exits, but `garden.run_supervisor` remains in its descendant wait loop without children. Establish why completion is not recorded and add bounded regression coverage.

## Provenance

Discovered by CG-411 (Adopt an existing PR with its verified branch and revision identity) during run `20260908T153212Z-work`.
## Log
- 2026-09-08T15:50:43+00:00 discovered by CG-411
- 2026-09-08T16:05:24+00:00 Duplicate investigation consolidated into CG433, including CG411 discovery and no-children supervisor observation.
