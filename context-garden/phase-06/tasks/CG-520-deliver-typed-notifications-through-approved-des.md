---
id: CG-520
title: Deliver typed notifications through approved destination adapters
status: done
product: context-garden
phase: phase-06
depends_on:
- CG-398
- CG-480
priority: 2
difficulty: hard
reading:
- src/garden/notify.py
- src/garden/config.py
- src/garden/events.py
- src/garden/inbox.py
- docs/architecture.md
- context-garden/phase-06/specs/context-garden-stripe-environment.md
branch: garden/cg-520-deliver-typed-notifications-through-approved-des
pr: https://github.com/joshmarcus/context-garden/pull/436
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T15:17:21+00:00'
created: '2026-09-10T11:18:53+00:00'
updated: '2026-09-10T15:31:50+00:00'
---

## Goal

Deliver meaningful Garden events through trusted, typed notification adapters using logical destination references, bounded retries and destination-aware disclosure. Worker-authored text must never become an executable command or leak raw diagnostics to a broader audience.

## Context

CG-398 demonstrates safe private notification construction and CG-480 distinguishes operator work from user decisions. A reusable destination adapter and delivery-state contract remains separate from that profile-specific path.

## Acceptance criteria

- [ ] Define a versioned adapter interface receiving typed event fields and a logical destination reference from trusted local configuration; task text and worker results cannot select adapters or recipients.
- [ ] Apply per-destination field policy, redaction and safe structured argument handling. Never interpolate worker-authored content into a shell command or expose credentials, physical hosts or raw private diagnostics.
- [ ] Bound delivery time, retry and backoff; coalesce unchanged events while delivering meaningful failure, recovery and required-action transitions once per identity.
- [ ] Persist delivery success/failure separately from task state. A failed notification remains visible and retryable without rolling back or corrupting the underlying transition.
- [ ] Synthetic adapters cover timeout, transient and permanent failure, duplicate events, restart, unsafe text, revoked destination and disclosure filtering. No external message is sent by tests.

enterprise_capability_key: enterprise-notification-adapters

## Log

- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T12:52:08+00:00 dispatched work run 20260910T125207Z-work-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~13026 tokens)
- 2026-09-10T13:02:48+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:04:26+00:00 opened https://github.com/joshmarcus/context-garden/pull/436 (base main): Added versioned typed notification delivery with trusted logical destinations, redaction, safe argv JSON delivery, bounded retries, coalescing, and a separate durable ledger. Focused notification tests and repository lint pass. cost=$0.84
- 2026-09-10T13:07:36+00:00 automated review requested changes: Typed delivery, bounded retries, coalescing, and scheduler integration are present, but the implementation retains unredacted diagnostics and never emits typed recovery/failure kinds. cost=$0.29
- 2026-09-10T13:08:14+00:00 dispatched revise run 20260910T130814Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14338 tokens)
- 2026-09-10T13:12:08+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:13:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/436: Hardened typed notification persistence and lifecycle classification. Verified with 19 focused notification/scheduler tests and repository lint. cost=$0.40
- 2026-09-10T13:18:06+00:00 automated review requested changes: Typed delivery and lifecycle handling are substantially implemented, but malformed destination retry/timeout settings can escape the notification boundary and crash a scheduler tick. cost=$0.31
- 2026-09-10T13:18:33+00:00 dispatched revise run 20260910T131833Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14471 tokens)
- 2026-09-10T13:22:20+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:23:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/436: Malformed timeout, retry-count, and backoff policies now remain inside the notification boundary, record a visible permanent ledger outcome, and cannot abort scheduler delivery. Verified with 20 focused notification/scheduler tests, Ruff, compileall, and final diff inspection. cost=$0.35
- 2026-09-10T13:26:46+00:00 automated review: approve — Typed destination delivery, disclosure filtering, bounded retries, lifecycle classification, durable retry state, and scheduler integration satisfy the task. cost=$0.24
- 2026-09-10T14:02:24+00:00 triage: changes requested by hand: Both current-head CI34482236949 and34482232421 fail test_configuration::test_cli_saved_project_edit_and_locked_bypass_us
- 2026-09-10T14:03:13+00:00 difficulty medium -> hard after 2 substantive revisions; model gpt-5.6-terra -> gpt-5.6-sol
- 2026-09-10T14:03:13+00:00 dispatched revise run 20260910T140313Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14578 tokens)
- 2026-09-10T14:22:19+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:23:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/436: Fixed the shared configuration mutation boundary so scheduler-owned notification runtime metadata no longer causes false stale-revision failures. Verified 37 focused configuration/notification tests, Ruff, compileall, and an isolated passing rerun of the full suite's single unrelated transient failure. cost=$2.46
- 2026-09-10T14:23:48+00:00 PR conflicts with main; rebase onto main conflicts (docs/architecture.md); a rebase agent will resolve it
- 2026-09-10T14:23:55+00:00 dispatched rebase run 20260910T142355Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2047 tokens)
- 2026-09-10T14:27:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/436: Resolved docs/architecture.md conflict and completed the rebase onto origin/main. cost=$0.01
- 2026-09-10T14:30:01+00:00 automated review requested changes: Typed notification behavior is well covered, but notification-ledger I/O failures are not contained and can crash scheduler delivery. cost=$0.33
- 2026-09-10T14:30:19+00:00 dispatched revise run 20260910T143019Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15159 tokens)
- 2026-09-10T14:45:15+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:46:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/436: Contained notification-ledger read, decode, and write failures at the delivery boundary with safe diagnostics, preserving scheduler transitions when notification persistence is unavailable. Verified 22 focused notification/scheduler tests, repository lint, and an isolated passing rerun of the full suite's single unrelated transient failure; the full run otherwise passed 2,489 tests. cost=$0.88
- 2026-09-10T14:49:17+00:00 automated review requested changes: Typed notification delivery is substantially implemented, but malformed durable ledger records can escape the notification boundary and abort scheduler ticks. cost=$0.35
- 2026-09-10T14:50:53+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:51:49+00:00 dispatched revise run 20260910T145148Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15710 tokens)
- 2026-09-10T14:57:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:59:12+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/436: Validated durable notification ledger records before field access, safely discarding malformed siblings while preserving valid retries and scheduler task state. Committed as 205e9bf8; 24 focused tests, repository Ruff, and compileall passed. cost=$0.82
- 2026-09-10T15:01:41+00:00 automated review requested changes: Focused tests and lint pass, but a non-UTF-8 notification ledger can still abort every scheduler tick during pending-retry processing. cost=$0.30
- 2026-09-10T15:16:17+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T15:17:21+00:00 dispatched revise run 20260910T151720Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15957 tokens)
- 2026-09-10T15:20:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:22:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/436: Pending notification retries now contain Unicode decoding failures without aborting scheduler ticks or exposing private ledger content. Committed as 4fca5c11; 25 focused notification/scheduler tests, repository Ruff, compileall, and final diff inspection passed. cost=$0.51
- 2026-09-10T15:24:43+00:00 automated review: approve — Typed notification adapters, disclosure filtering, bounded delivery/retries, lifecycle coalescing, and durable isolated outcomes satisfy CG-520. cost=$0.33
- 2026-09-10T15:30:18+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T15:31:50+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/436
