---
id: CG-197
title: Split cli.py into a cli/ package and fold the four rebase copies into one recorded helper
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-182
priority: 4
difficulty: medium
reading: []
branch: garden/cg-197-split-cli-py-into-a-cli-package-and-fold-the-fou
discovered_from: retro:context-garden/phase-03
attempts: 1
last_dispatched_at: '2026-09-05T11:22:54+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T11:22:54+00:00'
---

## Goal

**User value:** the next collision file is gone before phase 04 opens many PRs, and garden metrics counts every rebase because each path records a run.

**Why now:** cli.py is 1995 lines against the 800-line cap and absorbed seven commands this phase; the rebase sequence exists four times with only two copies recording a run, so the definition-of-done metric is undercounted. Also scope the metrics rebase block to the phase filter and split mechanical from agent rebases.

**Size:** medium. **Depends on:** nothing; run early and alone like CG-137 did.

## Context

Proposed at the context-garden/phase-03 retro. Phase 03 showed that structure first and alone removes conflicts for the rest of the phase, and the metric the phase is judged by is currently wrong.

## Log

- 2026-09-05T10:31:18+00:00 approved (web)
- 2026-09-05T11:22:54+00:00 dispatched work run 20260905T112245Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-182-the-tick-never-blocks-the-ui-actions-do-not-wait stacked on CG-182, ~4521 tokens)
