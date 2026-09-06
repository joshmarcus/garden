---
id: CG-330
title: 'A failed rebase or check run never restarts a task''s work from scratch: the PR stays, the rebase
  or check is retried, and only a failed work or revise run counts as an attempt'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler/reap.py
- src/garden/scheduler/rebase.py
- src/garden/scheduler/checkruns.py
- src/garden/scheduler/dispatch.py
- tests/scheduler/test_reap.py
created: '2026-09-06T06:24:13+00:00'
updated: '2026-09-06T06:24:16+00:00'
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
