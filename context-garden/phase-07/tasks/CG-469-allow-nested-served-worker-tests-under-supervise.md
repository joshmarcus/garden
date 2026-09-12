---
id: CG-469
title: Allow nested served-worker tests under supervised full-suite validation
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-469-allow-nested-served-worker-tests-under-supervise
discovered_from: CG-396
attempts: 1
last_dispatched_at: '2026-09-09T13:52:05+00:00'
created: '2026-09-09T10:59:32+00:00'
updated: '2026-09-09T15:52:40+00:00'
file: tests/test_remote_worker.py
error: test_remote_lifecycle_over_served_http times out at worker("check") only inside an enclosing supervised
  validation
---

The ordinary suite's served remote-worker lifecycle tests launch checks that wait on the same host validation lease held by the enclosing garden.validation run, causing their 30-second subprocess timeout. Provide an isolated lock namespace or safe inherited owner identity for these test subprocesses so AWS full-suite validation can execute them under supervision.

## Provenance

Discovered by CG-396 (Use pluggable exact-head CI status for review and merge eligibility) during run `20260909T094731Z-revise`.
## Log
- 2026-09-09T10:59:32+00:00 discovered by CG-396
- 2026-09-09T12:46:09+00:00 approved (web)
- 2026-09-09T13:52:05+00:00 dispatched work run 20260909T135201Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12050 tokens)
- 2026-09-09T13:55:31+00:00 preserved uncommitted worktree changes from run 20260909T135201Z-work outside the PR: `git stash apply 945f0405d0e2c7f578d8bcdc9beb58c823bc9c79` in /home/joshua/work/worktrees/CG-469 (garden:CG-469:20260909T135201Z-work:reap)
- 2026-09-09T13:55:31+00:00 worker found no change to make: The requested behavior is already implemented on the task base, so an additional diff would be redundant.; reconciling with checks and a fresh review
- 2026-09-09T13:56:52+00:00 branch pushed but PR failed (pull request create failed: GraphQL: Head sha can't be blank, Base sha can't be blank, No commits between main and garden/cg-469-allow-nested-served-worker-tests-under-supervise, Head ref must be a branch (createPullRequest)); open it by hand and run `garden pr CG-469 <url>` cost=$0.38
- 2026-09-09T14:06:40+00:00 automated review: approve — The requested behavior is already implemented at the reviewed head by merged CG-468; this branch equals origin/main and needs no additional diff. cost=$0.37
- 2026-09-09T15:52:40+00:00 No-change closure: approved current-base review verified the requested nested validation behavior is already supplied by merged CG-468 / PR 369; no CG-469 source or PR was needed.
