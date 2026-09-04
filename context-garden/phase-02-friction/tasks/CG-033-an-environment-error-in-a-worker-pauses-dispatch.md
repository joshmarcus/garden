---
id: CG-033
title: An environment error in a worker pauses dispatch instead of burning attempts
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/harness.py
branch: garden/cg-033-an-environment-error-in-a-worker-pauses-dispatch
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T17:45:10+00:00'
created: '2026-09-04T17:03:09+00:00'
updated: '2026-09-04T17:53:24+00:00'
---

## Goal

When a run fails for a reason no retry can fix (harness not logged in, binary not found, git identity missing, API auth error), the scheduler stops dispatching and flags the garden for a human instead of retrying and marking the task failed.

## Context

`Harness.parse` already turns `is_error` into `error`, but `_run_failed` treats every error the same: retry while `attempts < max_attempts`, then `failed`. A logged-out harness returns "Not logged in · Please run /login" in under a second, so two attempts burn in two ticks and the task is dead. Recognise a small set of environment errors (by exit code and message) and record a `_env` entry in state that the Inbox shows and that dispatch checks; clear it with `garden doctor` passing or `garden retry`.

## Acceptance criteria

- [ ] an environment error does not count as an attempt and leaves the task `ready`.
- [ ] dispatch is paused with the reason on the Inbox and in `garden status`.
- [ ] a test with the fake harness returning the not-logged-in shape.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:09+00:00 discovered by CG-027
- 2026-09-04T17:23:51+00:00 approved (web)
- 2026-09-04T17:24:45+00:00 dispatched work run 20260904T172444Z-work via local [claude model=sonnet] (fresh session, base main, ~4521 tokens)
- 2026-09-04T17:35:40+00:00 environment error (not an attempt): Done. All 117 tests pass, lint is clean, single commit on the branch.

GARDEN_RESULT: {"status": "done", "summary": "Environment errors (not-logged-in, binary not found, auth failure, git identity mis
- 2026-09-04T17:45:10+00:00 dispatched work run 20260904T174510Z-work via local [claude model=sonnet] (fresh session, base main, ~4623 tokens)
- 2026-09-04T17:53:24+00:00 attempt 1 failed: no GARDEN_RESULT in worker output (see final.md); will retry
