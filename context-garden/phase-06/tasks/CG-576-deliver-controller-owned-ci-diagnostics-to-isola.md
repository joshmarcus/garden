---
id: CG-576
title: Deliver controller-owned CI diagnostics to isolated workers
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: hard
reading:
- src/garden/checks.py
- src/garden/github.py
- src/garden/brief.py
- src/garden/scheduler/poll.py
branch: garden/cg-576-deliver-controller-owned-ci-diagnostics-to-isola
pr: https://github.com/joshmarcus/context-garden/pull/458
runner: remote
discovered_from: retro:context-garden/phase-05
attempts: 1
last_dispatched_at: '2026-09-10T18:26:05+00:00'
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T18:50:20+00:00'
---

## Goal

Preserve credential isolation while making the actual failing node, command, source and readable diagnostic excerpt available to the assigned worker. Coordinate CG-396 status policy and CG-506 transport; address the specific repeated inaccessible-log failure, not another CI provider implementation. An authentication error alone must not be presented as a source-test failure.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Transfer only bounded sanitized diagnostic excerpts with the exact source/check/attempt identity through the current accepted worker briefing or diagnostic channel. Preserve credentials, token redaction and provider error typing; an authentication/transport failure is not a source-test failure. Coordinate CG-396 provider ownership and the owner-deferred CG-506 storage design without waiting for a new full-transcript transport or duplicating either implementation. Verify a failing check reaches its assigned isolated worker and cannot leak secrets or stale-source diagnostics.

## Log

- 2026-09-10T13:48:51+00:00 approved (delegated operator; accepted retro PR4 and independent duplicate/brief review)
- 2026-09-10T17:31:42+00:00 delegated operator routed approved portable work to the existing six renewed remote workers after owner reported idle fleet; native priority/dependency/admission/review gates and absolute fleet deadline preserved
- 2026-09-10T17:38:20+00:00 dispatched work run 20260910T173819Z-work-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15404 tokens)
- 2026-09-10T17:50:29+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T17:52:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/458 (base main): Delivered controller-owned CI diagnostic execution with bounded redaction and exact-source feedback handoff to revision workers. Verified focused scheduler/GitHub/environment tests (115 passed), CI-check regressions (47 passed), and Ruff. cost=$1.66
- 2026-09-10T17:58:24+00:00 automated review requested changes: Controller-owned diagnostics are correctly routed locally and bound to the failing head, but not every diagnostic field copied into the isolated-worker brief is sanitized. cost=$0.45
- 2026-09-10T17:58:48+00:00 dispatched revise run 20260910T175848Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~16286 tokens)
- 2026-09-10T18:01:15+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:02:44+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/458: Sanitized every analyser-controlled CI feedback field before rendering it into an isolated worker brief. Verified with tests/scheduler/test_feedback_handoff.py (18 passed) and Ruff; this project has no configured typecheck command. cost=$0.27
- 2026-09-10T18:05:34+00:00 automated review requested changes: Controller-owned diagnostics are head-bound, bounded, and sanitized, but their launch path breaks credential isolation by resolving trusted modules from the untrusted PR worktree. cost=$0.36
- 2026-09-10T18:05:56+00:00 dispatched revise run 20260910T180556Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~16694 tokens)
- 2026-09-10T18:12:21+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:13:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/458: Pinned privileged controller CI diagnostic module resolution to controller-owned code and added a regression proving a shadow garden package in the PR worktree cannot execute or read a controller secret. Verified the focused shadow-package test, CI feedback handoff tests (18 passed), and Ruff. cost=$0.49
- 2026-09-10T18:16:30+00:00 automated review requested changes: Controller-owned diagnostics are isolated, redacted, bounded, and head-bound, but the GitHub analyser still omits required command and attempt identity. cost=$0.32
- 2026-09-10T18:16:48+00:00 difficulty medium -> hard after 2 substantive revisions; model gpt-5.6-terra -> gpt-5.6-sol
- 2026-09-10T18:16:48+00:00 dispatched revise run 20260910T181648Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~16954 tokens)
- 2026-09-10T18:20:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:21:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/458: GitHub Actions diagnostics now include exact workflow attempt identity and bounded failed-job command records alongside workflow, run, source, and diagnostic details. Verified commit 5367e200 with 115 focused tests, Ruff, and git diff --check. cost=$0.53
- 2026-09-10T18:25:47+00:00 automated review requested changes: Controller-owned diagnostics are locally isolated, bounded, and head-bound, but authorization headers can still leak credential values into worker briefs. cost=$0.34
- 2026-09-10T18:26:05+00:00 dispatched revise run 20260910T182604Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~17181 tokens)
- 2026-09-10T18:29:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:31:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/458: Authorization header values are now fully redacted before controller-owned CI diagnostics reach isolated worker briefs, including Bearer and Basic scheme-plus-credential forms. Verified on commit 1435618f901f851d9166f4a54f662c754f8c9f6f with 242 focused tests, Ruff, git diff --check, and final diff inspection; no typecheck command is configured. cost=$0.44
- 2026-09-10T18:31:39+00:00 PR conflicts with main; rebased onto main mechanically and force-pushed
- 2026-09-10T18:46:46+00:00 automated review: approve — Controller-owned CI diagnostics are safely delivered to isolated revision workers with bounded, sanitized, exact-head output and distinct authentication/transport error handling. cost=$0.38
- 2026-09-10T18:48:23+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T18:50:20+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/458
