---
id: CG-239
title: resolve_reading refuses absolute and parent paths, and the fence hashes the clone's git config
  and hooks
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: Goal 3 claims trust matches the mechanism and the phase runs overnight with automerge
  on for itself; the security persona verified on git 2.53 that a worker can execute code in the scheduler
  with the operator's credentials, and that a worker-filed task can inline the gh token into the next
  brief.
retro_blocking: true
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:05:56+00:00'
---

## Goal

In resolve_reading refuse absolute paths and any resolved path not under its base, and report it in brief_gaps. At dispatch hash the clone's .git/config, its hooks directory, the worktree's .git file and .git/worktrees/<id>/, and at reap refuse to run any git in that clone if they changed. Run scheduler-side git with core.hooksPath pointed at an empty directory and core.fsmonitor=false via GIT_CONFIG_COUNT in the one gitops.git wrapper. Tests: a worktree config write is attributed and blocks git at reap; a ../ reading entry is a gap.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: Goal 3 claims trust matches the mechanism and the phase runs overnight with automerge on for itself; the security persona verified on git 2.53 that a worker can execute code in the scheduler with the operator's credentials, and that a worker-filed task can inline the gh token into the next brief.

## Log

- 2026-09-05T23:05:56+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
