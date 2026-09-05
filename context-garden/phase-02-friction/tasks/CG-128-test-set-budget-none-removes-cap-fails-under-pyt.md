---
id: CG-128
title: test_set_budget_none_removes_cap fails under Python 3.14
status: draft
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- docs/worker-protocol.md
discovered_from: CG-062
created: '2026-09-05T00:07:08+00:00'
updated: '2026-09-05T00:07:08+00:00'
---

## Goal

`tests/test_coordination.py::test_set_budget_none_removes_cap` fails on clean `main` when run under Python 3.14 (asserts 2 dispatched, gets 0). CI pins Python 3.12 where it passes, so it's currently invisible, but it points at a real behavioral difference (likely dict/timing ordering) worth pinning down before the CI Python floor moves up.

## Context

Reproduce: `python3.14 -m pytest tests/test_coordination.py::test_set_budget_none_removes_cap`. Fails identically on `origin/main`.

## Provenance

Discovered by CG-062 (A worker silent for too long is flagged and stopped before the timeout) during run `20260905T000226Z-revise`.

## Log

- 2026-09-05T00:07:08+00:00 discovered by CG-062
