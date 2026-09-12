---
id: CG-440
title: Stabilize ordinary-suite onboarding and local-runner tests
status: cancelled
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/remote_worker.py
- src/garden/runner/remote.py
- src/garden/managed_worker.py
- src/garden/runs.py
- tests/test_remote_worker.py
- tests/test_managed_worker.py
- docs/worker-protocol.md
discovered_from: CG-428
created: '2026-09-08T16:21:10+00:00'
updated: '2026-09-08T17:12:01+00:00'
file: tests/test_onboard.py
error: One assertion failure followed by a persistent local-runner supervisor hang during `.venv/bin/python
  -m pytest -q`.
---

The AWS ordinary suite fails `tests/test_onboard.py::test_onboard_this_repository_uses_documented_setup_and_ci_tests` because the generated report lacks `GitHub repository metadata`, then hangs in `tests/test_runners.py::test_local_runner_launch_flips_to_running_only_after_pid` with a supervisor running `sleep 0.5; cat`. Diagnose these baseline validation failures so the ordinary suite completes deterministically.

## Provenance

Discovered by CG-428 (Keep remote worker runs alive across controller redeploys) during run `20260908T154233Z-work`.
## Log
- 2026-09-08T16:21:10+00:00 discovered by CG-428
- 2026-09-08T17:12:01+00:00 Consolidated into CG-432, CG-433 with full discovery and reporter provenance preserved; no implementation discarded.
