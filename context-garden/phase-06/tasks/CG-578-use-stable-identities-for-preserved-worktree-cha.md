---
id: CG-578
title: Use stable identities for preserved worktree changes
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 3
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-05
created: '2026-09-10T13:10:37+00:00'
updated: '2026-09-10T13:10:37+00:00'
---

## Goal

Audit remaining preservation paths for positional shared-stash references. Use stable object identities and verify the restored content while preserving unrelated work. CG-483 reduces generated snapshot churn but does not remove Git's shared stash namespace.

## Context

A follow-up carried into phase-06 by the context-garden/phase-05 retro verdict.
