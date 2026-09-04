---
id: CG-105
title: Test suite should isolate/unset GARDEN_ROOT so worker sandboxing doesn't masquerade as test failures
status: cancelled
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- context-garden/phase-01-bootstrap/specs/scheduler.md
discovered_from: CG-061
created: '2026-09-04T21:17:22+00:00'
updated: '2026-09-04T21:19:46+00:00'
---

## Goal

When a worker's environment has GARDEN_ROOT set to a nonexistent sentinel path (intentional, to stop workers from running `garden` commands against the live garden), running `.venv/bin/pytest` produces ~23 failures in tests that invoke the CLI in-process (CliRunner), because `find_root()` reads `GARDEN_ROOT` from the process environment and raises before ever reaching the test's own tmp-path garden.

## Context

Discovered while verifying CG-061: the pre-PR check run in this task's log (`pre-PR checks failed (tests)`) was actually this artifact, not a real regression, and it cost time to confirm. A `conftest.py` fixture that pops `GARDEN_ROOT` from `os.environ` for the test session (or monkeypatches it per-test) would make the suite deterministic regardless of the calling environment.

## Provenance

Discovered by CG-061 (Review runs whose task moved on are reaped, not left running forever) during run `20260904T211412Z-work`.

## Log

- 2026-09-04T21:17:22+00:00 discovered by CG-061
- 2026-09-04T21:19:46+00:00 cancelled (web)
