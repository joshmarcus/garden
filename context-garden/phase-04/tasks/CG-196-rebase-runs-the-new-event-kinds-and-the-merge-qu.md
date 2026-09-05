---
id: CG-196
title: Rebase runs, the new event kinds and the merge queue have a surface
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: medium
reading: []
branch: garden/cg-196-rebase-runs-the-new-event-kinds-and-the-merge-qu
discovered_from: retro:context-garden/phase-03
last_dispatched_at: '2026-09-05T13:18:09+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T14:33:48+00:00'
---

## Goal

**User value:** a mechanical rebase run page says 'mechanical rebase onto main, no model, no cost' with what git did and the check result; the timeline formats rebase, merge_head, feedback_ignored, retro_failed, rebased_stale_base and phase_frozen; the Board or Inbox shows the queue head, whether it waits on CI, and the last drop reason.

**Why now:** every state phase 03 added reached the UI unlabelled, and the operator cannot see why nothing merges.

**Size:** medium. **Depends on:** CG-141 and CG-176 (merged). Pairs with CG-184 but is a different set of pages.

## Context

Proposed at the context-garden/phase-03 retro. The queue and rebase mode are the phase's main mechanisms and are invisible, so the operator cannot trust them unattended.

## Log

- 2026-09-05T10:31:17+00:00 approved (web)
- 2026-09-05T13:16:26+00:00 dispatched work run 20260905T131618Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4368 tokens)
- 2026-09-05T13:17:48+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:18:09+00:00 dispatched work run 20260905T131809Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4469 tokens)
- 2026-09-05T13:19:15+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:48+00:00 reset to ready by hand
