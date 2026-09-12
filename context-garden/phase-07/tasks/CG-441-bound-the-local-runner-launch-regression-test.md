---
id: CG-441
title: Bound the local runner launch regression test
status: cancelled
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: easy
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
discovered_from: CG-404
created: '2026-09-08T16:46:47+00:00'
updated: '2026-09-08T17:12:01+00:00'
file: tests/test_runners.py
error: Full pytest stalled at test_local_runner_launch_flips_process_finished with the detached run supervisor
  still waiting after more than six minutes.
---

The ordinary suite can hang indefinitely in `test_local_runner_launch_flips_process_finished` because it calls blocking `os.waitpid(run.pid, 0)` without a timeout. During CG-404 validation, its `sleep 0.5; cat` supervisor remained alive for more than six minutes and prevented pytest from reporting the suite's earlier failure detail. Replace the unbounded wait with bounded polling/cleanup while preserving end-to-end launch coverage.

## Provenance

Discovered by CG-404 (Add command-backed host acquisition readiness and warm reuse to the shared lifecycle) during run `20260908T162136Z-revise`.
## Log
- 2026-09-08T16:46:47+00:00 discovered by CG-404
- 2026-09-08T17:12:01+00:00 Consolidated into CG-433 with full discovery and reporter provenance preserved; no implementation discarded.
