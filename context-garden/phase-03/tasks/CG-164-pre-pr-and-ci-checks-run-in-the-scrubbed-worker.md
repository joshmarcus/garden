---
id: CG-164
title: Pre-PR and CI checks run in the scrubbed worker environment
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-154
priority: 1
difficulty: easy
reading: []
discovered_from: CG-154
created: '2026-09-05T04:01:03+00:00'
updated: '2026-09-05T04:05:54+00:00'
---

## Goal

`checks.run_check` builds a command check's environment from `os.environ`, so the branch's own test suite (code a worker wrote) runs with the scheduler's GitHub token, cloud credentials and ssh agent. Apply `runner.base.worker_env` there too, keeping `GARDEN_EXEC_ROOT` and the `GARDEN_<KEY>` context, and note that a `python:` check runs in-process regardless.

## Context

CG-154 scrubbed the worker and its setup command; checks were left out to keep the diff focused. See `src/garden/checks.py` and the module docstring's environment contract.

## Provenance

Discovered by CG-154 (Trust at the edges: PR feedback only from trusted authors, a scrubbed worker environment, sanitised HTML and an origin check on POSTs) during run `20260905T034729Z-work`.

## Log

- 2026-09-05T04:01:03+00:00 discovered by CG-154
- 2026-09-05T04:05:54+00:00 approved (web)
