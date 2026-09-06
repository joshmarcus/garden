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
harness: codex
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-06T00:50:21+00:00'
---

## Goal

The brief builder refuses an empty reading list, drops entries that do not resolve and says so as a gap, and builds the inlined files from the task's base rather than a dirty worktree. A revise brief restates the acceptance criteria, inlines the actual review comments and the failing check's stack trace, and when GitHub has nothing to address says the blocker is the rebase conflict. Seventeen phase-04 friction items.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Suggestions

- [ ] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-282 (renumbered by the operator: two reconcile runs drew ids from one counter)
