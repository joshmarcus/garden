---
id: CG-247
title: Make completion honor the product base branch
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
freeze_exception: true
freeze_exception_reason: The current Mark done action contradicts CG-228's delivered completion invariant
  and can tell the owner that unshipped work is finished.
retro_blocking: true
created: '2026-09-05T23:15:10+00:00'
updated: '2026-09-05T23:59:48+00:00'
---

## Goal

Implement one Scheduler.mark_done path through the shared transition mechanism and use it from web, CLI and other completion actions. For PR-backed tasks, require verified inclusion in the product base branch before reporting done; remove the primary in-review shortcut that bypasses this rule. Preserve legitimate explicitly manual-task completion with visible provenance and separate any administrative override from verified merged completion. Test stacked PRs, unmerged PRs and terminal-state cleanup.

## Context

Filed by the context-garden/phase-04 retro `reopen` verdict: it must land before the phase can close. Reason: The current Mark done action contradicts CG-228's delivered completion invariant and can tell the owner that unshipped work is finished.

## Log

- 2026-09-05T23:15:10+00:00 filed by the context-garden/phase-04 retro reopen verdict (blocking)
- 2026-09-05T23:58:01+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-05T23:59:48+00:00 approved by the retro reopen verdict
