---
id: CG-124
title: test_feedback_triggers_revise_round commit-collision flake (already tracked as CG-064)
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/runs.py
discovered_from: CG-083
created: '2026-09-04T23:19:07+00:00'
updated: '2026-09-04T23:19:07+00:00'
---

Already fixed in this PR as a blocking prerequisite (see commit 86db97f). Flagging only so the scheduler is aware CG-064 and this PR now contain duplicate fixes for the same test-harness bug, and one will need a trivial conflict resolution when merged after the other.

## Provenance

Discovered by CG-083 (A reap is atomic: a restart mid-tick never loses a finished run) during run `20260904T230950Z-revise`.

## Log

- 2026-09-04T23:19:07+00:00 discovered by CG-083
