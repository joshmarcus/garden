---
id: CG-293
title: A brief never ships with an empty or unresolved reading list, and a revise brief restates the criteria
  and the concrete blocker
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-05T23:58:18+00:00'
discovered_from: retro:context-garden/phase-04
---

## Goal

The brief builder refuses an empty reading list, drops entries that do not resolve and says so as a gap, and builds the inlined files from the task's base rather than a dirty worktree. A revise brief restates the acceptance criteria, inlines the actual review comments and the failing check's stack trace, and when GitHub has nothing to address says the blocker is the rebase conflict. Seventeen phase-04 friction items.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-282 (renumbered by the operator: two reconcile runs drew ids from one counter)
