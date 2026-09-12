---
id: CG-580
title: Align QA request timeouts with advertised deadlines
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: medium
reading:
- src/garden/interaction_replay.py
- src/garden/config.py
branch: garden/cg-580-align-qa-request-timeouts-with-advertised-deadli
pr: https://github.com/joshmarcus/context-garden/pull/469
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T19:42:18+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T19:59:31+00:00'
---

## Goal

Check the reported thirty-second flow deadline versus ten-second request timeout on current source. Make the documented deadline and effective request budget consistent, preserving a finite bound and reporting which deadline expired. Retire the finding without a code change if the mismatch is already corrected.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Reproduce the named advertised-versus-effective timeout mismatch on current source, identify the flow and individual request deadline owners, and keep an explicit finite budget with accurate expiry diagnostics. If already aligned, retain source-specific verification and retire without an implementation rewrite. Use bounded fake clock/HTTP verification for a demonstrated correction.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:50:57+00:00 dispatched work run 20260910T175057Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~13899 tokens)
- 2026-09-10T17:54:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:58:27+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$0.06
- 2026-09-10T18:34:27+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:29+00:00 opened https://github.com/joshmarcus/context-garden/pull/469 (base main): Aligned QA request budgets with advertised flow deadlines and added expiry diagnostics. Verified with 10 passing tests and changed-file lint.
- 2026-09-10T18:34:29+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T19:11:33+00:00 automated review requested changes: The shared flow budget is correctly propagated to requests, but timeout diagnostics misidentify expiry at the flow boundary. cost=$0.26
- 2026-09-10T19:11:48+00:00 dispatched revise run 20260910T191147Z-revise via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~14913 tokens)
- 2026-09-10T19:15:33+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:17:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/469: Clarified QA timeout diagnostics so request timeouts using the shared flow budget report flow expiry during the request. Committed as f9eeada2. cost=$0.03
- 2026-09-10T19:23:40+00:00 automated review requested changes: Remaining time is passed to HTTPX, but this does not enforce the advertised wall-clock flow deadline. cost=$0.22
- 2026-09-10T19:24:00+00:00 dispatched revise run 20260910T192359Z-revise via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~15138 tokens)
- 2026-09-10T19:28:54+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:30:21+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/469: Enforced finite wall-clock QA request deadlines and added regression coverage for trickle responses. Verified with 11 passing tests and clean repository lint. cost=$0.05
- 2026-09-10T19:32:48+00:00 automated review requested changes: The request budget and diagnostics are aligned, but the advertised wall-clock flow deadline is still not enforced during a stalled response read. cost=$0.24
- 2026-09-10T19:42:17+00:00 difficulty easy -> medium after 2 substantive revisions; model gpt-5.6-luna -> gpt-5.6-terra
- 2026-09-10T19:42:18+00:00 dispatched revise run 20260910T194217Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15213 tokens)
- 2026-09-10T19:46:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T19:48:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/469: QA response reads are bounded by the advertised flow deadline, including a stall after an initial chunk. Verified with the focused QA suite (11 passed) and repository lint. cost=$0.44
- 2026-09-10T19:50:48+00:00 automated review: approve — QA requests now share and enforce the advertised finite flow deadline, including stalled streamed responses, with accurate flow-expiry diagnostics. cost=$0.25
- 2026-09-10T19:59:31+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/469
