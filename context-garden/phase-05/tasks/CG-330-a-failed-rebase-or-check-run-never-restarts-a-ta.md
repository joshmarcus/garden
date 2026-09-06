---
id: CG-330
title: 'A failed rebase or check run never restarts a task''s work from scratch: the PR stays, the rebase
  or check is retried, and only a failed work or revise run counts as an attempt'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 2
difficulty: medium
reading:
- src/garden/scheduler/reap.py
- src/garden/scheduler/rebase.py
- src/garden/scheduler/checkruns.py
- src/garden/scheduler/dispatch.py
- tests/scheduler/test_reap.py
branch: garden/cg-330-a-failed-rebase-or-check-run-never-restarts-a-ta
pr: https://github.com/joshmarcus/context-garden/pull/236
attempts: 1
last_dispatched_at: '2026-09-06T19:27:57+00:00'
created: '2026-09-06T06:24:13+00:00'
updated: '2026-09-06T20:10:49+00:00'
---

## Goal

Auxiliary runs fail on their own terms. When a rebase run, a check run or an edit run ends without a result (killed, timed out, no GARDEN_RESULT), the task keeps its PR and its branch, the failure is logged on the task with the run id and cause, and the same auxiliary run is retried once on the next tick before the task is parked with a needs-human card. Attempts, and the "attempt N failed, will retry" path that dispatches a fresh work run from the base branch, apply only to work and revise runs.

## Context

2026-09-06 06:16Z, CG-308 (the Now 1 build, PR #218 open with a full build on its branch): its conflict-rebase run ended without a result under machine load; the reaper logged "attempt 1 failed: no GARDEN_RESULT in worker output; will retry" and dispatched a fresh *work* run on fable from the design branch, which would rebuild the page from scratch beside an open PR that already had it. The same minute CG-307's pre-merge check ended with no output after 40 minutes and pushed the task past its revision cap. Under load, auxiliary runs fail more than work runs, and each such failure must not multiply the work.

## Acceptance criteria

- [ ] A rebase run that ends without a result is retried once on the next tick and then parks the task in review with a needs-human card naming the conflict; the task's PR, branch and attempt count are untouched; a test with the fake harness covers the retry and the park.
- [ ] A check run that ends without any check result (killed, timeout, no output) is recorded as "check did not run" with the cause and retried once; it never counts as a failed check against the revision cap; a test covers a killed check.
- [ ] `attempt N failed ... will retry` and the fresh-work-run path fire only for work and revise runs; a source-level test asserts the reap path for rebase, check and edit modes never calls the work dispatcher.

## Log
- 2026-09-06T06:24:16+00:00 approved (cli)
- 2026-09-06T11:36:45+00:00 dispatched work run 20260906T112700Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~25030 tokens)
- 2026-09-06T12:51:35+00:00 pre-PR checks failed (test) (still failing after a rebase onto `main`); no PR opened yet; revise run will fix cost=$1.13
- 2026-09-06T13:04:41+00:00 dispatched revise run 20260906T130437Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~14537 tokens)
- 2026-09-06T13:07:05+00:00 revision failed: no GARDEN_RESULT in worker output (see final.md)

## Operator recovery, 2026-09-06

The WSL restart interrupted the prior revise. Its unfinished changes are preserved in this task worktree in the stash named `operator-recovery-20260906-CG330` (check `git stash list`; restore by its verified identifier before continuing). It preserves the structured killed-check summary in checkruns.py and its test; also contains the pre-existing design snapshot. Continue the existing implementation, run checks, commit and open its PR. Do not discard the saved work. The previous suite error involved a vanished /tmp fixture; the worker temp target is now restored.
- 2026-09-06T13:19:31+00:00 reset to ready by hand
- 2026-09-06T13:46:58+00:00 priority 1 -> 0
- 2026-09-06T19:14:20+00:00 dispatched work run 20260906T191418Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~14937 tokens)
- 2026-09-06T19:27:49+00:00 opened https://github.com/joshmarcus/context-garden/pull/236 (base main): Auxiliary rebase, validation, and edit failures now retry independently once, preserve task context, and park with a human stop after a repeat failure. Work dispatch is blocked for human-stopped tasks. cost=$0.71
- 2026-09-06T19:27:55+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/dispatch.py); a rebase agent will resolve it
- 2026-09-06T19:27:57+00:00 dispatched rebase run 20260906T192755Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8320 tokens)
- 2026-09-06T19:34:21+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 8842552190ef, not because of this branch; waiting for the base to go green, no revise round cost=$0.03
- 2026-09-06T19:35:28+00:00 automated review: request_changes — Auxiliary rebase, check, and edit failures retry independently without consuming work attempts, and the focused tests pass. Remove the unrelated generated snapshot and clean the final commit story before merge. cost=$0.25
- 2026-09-06T19:43:12+00:00 nothing to fix; resumed to in review by hand

19:43 operator diagnosis: branch check193106 ended SIGTERM; base probe193318 did not execute Python at all (/bin/sh .venv/bin/python not found, exit127). This is an environment/setup failure, not evidence that main8842552 is broken. Snapshot review finding removed/preserved in31b2db9. Resume through normal review/CI without treating missing interpreter as a source regression. Preserve PR/worktree.

## Follow-up acceptance: clean-base environment classification

- [ ] A clean-base probe whose configured interpreter is absent or whose test is terminated is classified as setup/interruption, never as proof that main is source-broken. Preserve work, surface the concrete missing prerequisite, and exercise missing executable and SIGTERM regression cases without rerunning ordinary work from scratch.
- 2026-09-06T20:10:49+00:00 PR236 merged after current-head CI and removal of unrelated snapshot; auxiliary retry semantics reviewed and passed.
