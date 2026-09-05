---
id: CG-196
title: Rebase runs, the new event kinds and the merge queue have a surface
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 3
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-03
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T10:26:55+00:00'
---

## Goal

**User value:** a mechanical rebase run page says 'mechanical rebase onto main, no model, no cost' with what git did and the check result; the timeline formats rebase, merge_head, feedback_ignored, retro_failed, rebased_stale_base and phase_frozen; the Board or Inbox shows the queue head, whether it waits on CI, and the last drop reason.

**Why now:** every state phase 03 added reached the UI unlabelled, and the operator cannot see why nothing merges.

**Size:** medium. **Depends on:** CG-141 and CG-176 (merged). Pairs with CG-184 but is a different set of pages.

## Context

Proposed at the context-garden/phase-03 retro. The queue and rebase mode are the phase's main mechanisms and are invisible, so the operator cannot trust them unattended.
