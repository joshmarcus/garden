---
id: CG-582
title: Separate expected SSE shutdown from application errors
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-524
  after: merge
priority: 4
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/pages/events.py
- src/garden/events.py
branch: garden/cg-582-separate-expected-sse-shutdown-from-application
pr: https://github.com/joshmarcus/context-garden/pull/471
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T17:55:26+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T19:30:29+00:00'
---

## Goal

Reduce benign cancellation traceback noise during controlled disposal of servers with open event streams. Preserve real application failures and enforce bounded shutdown. Coordinate with CG-524's existing historical harness consolidation rather than introducing another task-specific capture framework.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Reproduce controlled shutdown with an open event stream on current source and distinguish expected cancellation/disconnect from real handler exceptions. Suppress only benign diagnostics while preserving actionable failures and bounded termination. Coordinate the existing harness consolidation and validate the actual affected shutdown path with a disposable server.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:55:26+00:00 dispatched work run 20260910T175525Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~13833 tokens)
- 2026-09-10T18:02:44+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:05:35+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.10
- 2026-09-10T18:34:32+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/471 (base main): Separated expected SSE disconnect and cancellation from application errors at the streaming response boundary. Verified with 36 Now tests, 169 web tests, changed-file lint, and diff checks.
- 2026-09-10T18:34:35+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T19:25:03+00:00 automated review: approve — The narrow SSE response boundary quietly handles server cancellation and Starlette-normalized client disconnects while allowing unexpected exceptions to propagate. cost=$0.23
- 2026-09-10T19:28:58+00:00 automated review: approve — The SSE-specific boundary suppresses expected cancellation and normalized disconnect signals while preserving unexpected exceptions. cost=$0.31
- 2026-09-10T19:30:29+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/471
