---
id: CG-245
title: Isolate planner execution from operator state
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-245-isolate-planner-execution-from-operator-state
pr: https://github.com/joshmarcus/context-garden/pull/202
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: A stated phase trust goal remains unshipped, and model-written documents currently
  drive an edit-capable process in the live garden with operator credentials.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-06T01:51:54+00:00'
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-06T01:56:33+00:00'
---

## Goal

Route synchronous planning through the worker environment and a scratch directory with only the capabilities needed to read approved context and return a plan. Do not inherit operator HOME or unrestricted tokens, and enforce the common brief gate on generated work. Cover planner and synchronous kickoff paths with malicious document input and assertions about environment, filesystem and allowed operations.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: A stated phase trust goal remains unshipped, and model-written documents currently drive an edit-capable process in the live garden with operator credentials.

## Log

- 2026-09-05T23:15:10+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:58:00+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-05T23:59:48+00:00 approved by the retro reopen verdict
- 2026-09-06T00:01:43+00:00 dispatched work run 20260906T000127Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~5776 tokens)
- 2026-09-06T00:19:15+00:00 environment stop (quota): quota limit hit on claude; not counted as an attempt; dispatch paused for claude until a probe succeeds
- 2026-09-06T00:36:20+00:00 dispatched work run 20260906T003620Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~6573 tokens)
- 2026-09-06T00:44:33+00:00 opened https://github.com/joshmarcus/context-garden/pull/202 (base main): Rebased the prior attempt's CG-245 commits onto main (resolving divergence from two since-merged security PRs, no code conflicts) and verified the isolation work: run_planner now executes in a scratch, worker-scrubbed environment and import_plan enforces the brief gate on generated tasks. cost=$0.66
- 2026-09-06T00:55:30+00:00 automated review: approve — Planner and synchronous kickoff now run in a scratch, worker-scrubbed environment with the brief gate enforced on generated tasks; verified against the actual scrubbed_env/fence code path, full test suite (981 passed/3 skipped) and ruff both clean. cost=$0.60
- 2026-09-06T00:56:52+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-06T00:57:53+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated
- 2026-09-06T01:01:02+00:00 dispatch failed: [Errno 28] No space left on device: '/tmp/garden-empty-hooks-t1a7s47d'
- 2026-09-06T01:46:22+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T01:51:54+00:00 dispatched revise run 20260906T015153Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~7798 tokens)
- 2026-09-06T01:56:31+00:00 worker says nothing to change: This is a revision round on PR #202, but the PR has already been merged into main — HEAD (570ebad) is the second parent of main's merge commit 7cfcda6, and there is no diff between origin/main and HEAD. The failing pre-PR check (`test_triage_notify_waits_for_review_verdict`, OSError: No space left on device) is an environment condition, not a code issue: disk now shows 946G free, the specific test passes in isolation, and the full suite (983 passed, 3 skipped) plus ruff both pass cleanly. The planner and synchronous-kickoff isolation work itself is intact and tested: `run_planner` executes in a `tempfile.TemporaryDirectory` scratch through `scrubbed_env`, denies the live garden root as a write target, and forces a sentinel `GARDEN_ROOT`; `import_plan` runs every generated task through `brief_gaps` before promoting draft to ready. There is nothing left to change on this branch. cost=$0.41
- 2026-09-06T01:56:33+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/202
