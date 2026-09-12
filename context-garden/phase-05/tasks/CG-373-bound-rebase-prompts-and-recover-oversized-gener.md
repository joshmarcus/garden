---
id: CG-373
title: Bound rebase prompts and recover oversized generated-file conflicts
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-373-bound-rebase-prompts-and-recover-oversized-gener
pr: https://github.com/joshmarcus/context-garden/pull/283
attempts: 1
last_dispatched_at: '2026-09-07T11:47:38+00:00'
created: '2026-09-07T09:14:33+00:00'
updated: '2026-09-07T12:03:41+00:00'
---

## Goal

Bound rebase prompts and recover oversized generated-file conflicts.

## Context

CG294 twice sent ~1.595 million characters against a1048576 limit because docs/design/snapshot.json dominated a conflict-only brief. Owner requested prevention tickets after resolving the human queue.

## Acceptance criteria

- [ ] Budget serialized prompt size before harness invocation; oversized inputs never reach turn/start.
- [ ] Represent large generated-file conflicts with bounded summaries and artifact paths; preserve original blobs and salvage stashes.
- [ ] Recover this deterministic input failure without duplicate retries or asking an owner to resolve generated data; cover a >1MiB conflict fixture.

## Log

- 2026-09-07T09:14:34+00:00 approved (web)
- 2026-09-07T09:33:37+00:00 dispatched work run 20260907T093244Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~8913 tokens)
- 2026-09-07T09:55:00+00:00 preserved uncommitted worktree changes from run 20260907T093244Z-work outside the PR: `git stash apply c30992558fd44abd66586388c19e62fee195a5f6` in /home/joshua/work/worktrees/CG-373 (garden:CG-373:20260907T093244Z-work:reap)
- 2026-09-07T09:57:52+00:00 opened https://github.com/joshmarcus/context-garden/pull/283 (base main): Bounds serialized prompts before runner startup and replaces oversized rebase conflict payloads with summaries backed by durable artifacts. Generated conflict blobs remain recoverable without consuming duplicate rebase retries. cost=$1.45
- 2026-09-07T10:00:41+00:00 automated review requested changes: Prompt dispatch is bounded, but the implementation stores a lossy rendered conflict file rather than the original Git conflict blobs, and the oversized-conflict test stops after dispatch instead of proving unattended recovery. cost=$0.47
- 2026-09-07T10:16:19+00:00 dispatched revise run 20260907T101616Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9867 tokens)
- 2026-09-07T10:32:11+00:00 preserved uncommitted worktree changes from run 20260907T101616Z-revise outside the PR: `git stash apply e739d47d58c48571ab09114afc14f00f56232e8b` in /home/joshua/work/worktrees/CG-373 (garden:CG-373:20260907T101616Z-revise:reap)
- 2026-09-07T10:34:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/283: Preserves byte-exact Git conflict stages as hashed artifacts and verifies bounded, unattended recovery for an oversized invalid-UTF-8 fixture. Commit 6f5c9c0482d76b51a1c6855ac7413941c8f3f5fc passed GitHub CI. cost=$2.17
- 2026-09-07T10:37:15+00:00 PR conflicts with main; rebase onto main conflicts (tests/scheduler/test_dispatch.py); a rebase agent will resolve it
- 2026-09-07T10:38:20+00:00 automated review: request_changes — Prompt bounding and the tested >1 MiB base-rebase recovery work, but conflicts during remote-branch synchronization still lose their Git stages before dispatch. The PR description also needs to connect this recovery work to phase-05 stabilization. cost=$0.36
- 2026-09-07T10:41:01+00:00 dispatched rebase run 20260907T104059Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~7265 tokens)
- 2026-09-07T10:46:51+00:00 preserved uncommitted worktree changes from run 20260907T104059Z-rebase outside the PR: `git stash apply 3a4b120452975f43e57e9fe3ecbaf3591a509e44` in /home/joshua/work/worktrees/CG-373 (garden:CG-373:20260907T104059Z-rebase:reap)
- 2026-09-07T11:33:56+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.01
- 2026-09-07T11:47:38+00:00 dispatched revise run 20260907T114736Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10323 tokens)
- 2026-09-07T11:58:14+00:00 preserved uncommitted worktree changes from run 20260907T114736Z-revise outside the PR: `git stash apply b02124622a69e279cd53c055b9ee43c0a063476f` in /home/joshua/work/worktrees/CG-373 (garden:CG-373:20260907T114736Z-revise:reap)
- 2026-09-07T11:59:31+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/283: Preserved byte-exact Git stages for remote synchronization conflicts as well as base rebases, while keeping resolver prompts bounded. Fixed the reported import-order lint failure and validated the final commit in GitHub CI. cost=$0.66
- 2026-09-07T12:02:08+00:00 automated review: approve — The PR bounds prompts before runner startup, preserves byte-exact conflict stages for both rebase paths, and demonstrates unattended recovery of a >1 MiB invalid-UTF-8 conflict. Focused tests and lint pass. cost=$0.29
- 2026-09-07T12:02:21+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-07T12:03:41+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/283
