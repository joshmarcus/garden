---
id: CG-113
title: Drop the `env -u GARDEN_ROOT` stopgap from the live garden's tests check
status: ready
product: context-garden
phase: phase-02-friction
depends_on:
- CG-098
priority: 1
difficulty: easy
reading:
- tests/conftest.py
- tests/test_cli.py
- src/garden/checks.py
- src/garden/config.py
runner: manual
discovered_from: CG-098
created: '2026-09-04T21:42:29+00:00'
updated: '2026-09-04T22:03:22+00:00'
---

The live garden's own `garden.yaml` (in the joshmarcus/garden repo, not this codebase) prepends `env -u GARDEN_ROOT` to the pre_pr `tests` check command as a stopgap. Now that this repo's test suite clears both `GARDEN_ROOT` and `GARDEN_EXEC_ROOT` itself via an autouse fixture, that stopgap is redundant and can be removed from the live garden.yaml.

## Provenance

Discovered by CG-098 (Tests do not read the developer's GARDEN_ROOT; the check command need not unset it) during run `20260904T213518Z-work`.

## Log

- 2026-09-04T21:42:29+00:00 discovered by CG-098
- 2026-09-04T22:03:22+00:00 manual: the change is in the live garden.yaml, which no worker checks out; a person drops the stopgap after CG-098 (PR #54) merges
