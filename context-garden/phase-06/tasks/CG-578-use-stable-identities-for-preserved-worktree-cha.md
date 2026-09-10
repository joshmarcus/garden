---
id: CG-578
title: Use stable identities for preserved worktree changes
status: draft
product: context-garden
phase: phase-06
depends_on:
- id: CG-359
  after: merge
- id: CG-483
  after: merge
priority: 3
difficulty: medium
reading:
- src/garden/gitops.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/fence.py
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:28:27.335304+00:00'
---

## Goal

Audit remaining preservation paths for positional shared-stash references. Use stable object identities and verify the restored content while preserving unrelated work. CG-483 reduces generated snapshot churn but does not remove Git's shared stash namespace.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.


## Reviewed scope and verification

Find every preservation path that consumes a shared positional stash reference. Retain a stable commit/object/ref identity through save, retry, restore and cleanup, verify the restored content, and never drop another attempt's stash. Use disposable Git repositories to check concurrent/unrelated stashes and interrupted restoration. Existing stable paths need no rewrite.
