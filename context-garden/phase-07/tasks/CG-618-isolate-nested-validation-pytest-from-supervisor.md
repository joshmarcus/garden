---
id: CG-618
title: Isolate nested validation pytest from supervisor PYTEST_ADDOPTS
status: cancelled
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/scheduler/retro.py
- src/garden/scheduler/persona.py
- src/garden/scheduler/__init__.py
- src/garden/config.py
- src/garden/cli/planning.py
- src/garden/retro.py
discovered_from: CG-529
created: '2026-09-11T01:33:46+00:00'
updated: '2026-09-11T01:34:01+00:00'
file: tests/test_validation.py
error: test_old_branch_can_explicitly_opt_in_to_known_stress returns 0 instead of 1 when PYTEST_ADDOPTS
  is inherited
---

The validation-policy regression for explicit stress opt-in inherits the supervising worker's PYTEST_ADDOPTS. This deselects the nested fixture stress nodes and changes the expected failure into success. Make the nested subprocess environment explicit so the test measures resolve_validation behavior independently of its parent runner.

## Provenance

Discovered by CG-529 (Automatically start the phase closing review when prerequisites are met) during run `20260911T004511Z-revise`.
## Log
- 2026-09-11T01:33:46+00:00 discovered by CG-529
- 2026-09-11T01:34:01+00:00 Duplicate of existing CG-601, already approved from the same explicit stress opt-in synthetic fixture reproduction. Preserve this finding and original report; use CG-601 for the distinct correction.
