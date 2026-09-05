---
id: CG-164
title: Pre-PR and CI checks run in the scrubbed worker environment
status: in_review
product: context-garden
phase: phase-03
depends_on:
- CG-154
priority: 1
difficulty: easy
reading: []
branch: garden/cg-164-pre-pr-and-ci-checks-run-in-the-scrubbed-worker
pr: https://github.com/joshmarcus/context-garden/pull/109
discovered_from: CG-154
attempts: 1
last_dispatched_at: '2026-09-05T04:16:06+00:00'
created: '2026-09-05T04:01:03+00:00'
updated: '2026-09-05T04:24:26+00:00'
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
- 2026-09-05T04:16:06+00:00 dispatched work run 20260905T041557Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-154-trust-at-the-edges-pr-feedback-only-from-trusted stacked on CG-154, ~3892 tokens)
- 2026-09-05T04:24:24+00:00 pre-PR check(s) test, lint failed at the stale base 55a935290123; the base branch `garden/cg-154-trust-at-the-edges-pr-feedback-only-from-trusted` had moved, so rebased onto it and the checks pass now — no revise round
- 2026-09-05T04:24:26+00:00 opened https://github.com/joshmarcus/context-garden/pull/109 (base garden/cg-154-trust-at-the-edges-pr-feedback-only-from-trusted): checks.run_check now builds a command check's subprocess environment from runner.base.scrubbed_env (with an optional config argument for worker_env.pass) instead of raw os.environ, closing the credential leak in pre-PR/CI checks that run a branch's own code; python: checks remain in-process and documented as unscrubbed. cost=$1.53
