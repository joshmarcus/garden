---
id: CG-196
title: Rebase runs, the new event kinds and the merge queue have a surface
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: medium
reading: []
branch: garden/cg-196-rebase-runs-the-new-event-kinds-and-the-merge-qu
pr: https://github.com/joshmarcus/context-garden/pull/165
discovered_from: retro:context-garden/phase-03
attempts: 1
last_dispatched_at: '2026-09-05T15:05:54+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T15:32:09+00:00'
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
- 2026-09-05T14:34:02+00:00 dispatched work run 20260905T143402Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4754 tokens)
- 2026-09-05T14:34:42+00:00 reset to ready by hand
- 2026-09-05T15:05:54+00:00 dispatched work run 20260905T150554Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4846 tokens)
- 2026-09-05T15:10:09+00:00 worker says nothing to change: Reviewed the prior attempt's commit (19d3ae0) against the task's three stated criteria and the actual event/state producers in scheduler/rebase.py, scheduler/queue.py, scheduler/poll.py, scheduler/retro.py and cli/scaffold.py — every event kind and field the templates render is emitted with matching names/fields, and dedicated tests (test_timeline_formats_the_new_event_kinds, test_run_page_mechanical_rebase, test_inbox_shows_the_merge_queue) cover each. Full suite (700 passed, 3 skipped) and ruff both pass with a clean working tree, so there is nothing to change. cost=$0.40
- 2026-09-05T15:18:43+00:00 no-change accepted by the person (accepted by the operator: the earlier attempt's commit completes the task; push the branch and open the PR); resuming the round without a new work run
- 2026-09-05T15:20:55+00:00 opened https://github.com/joshmarcus/context-garden/pull/165 (base main): The existing commit on this branch already fully implements CG-196: the Timeline formats rebase/merge_head/feedback_ignored/retro_failed/rebased_stale_base/phase_frozen with phase links for task-less events, mechanical rebase runs get a dedicated no-model/no-cost page with diff stat and check result, and the Inbox shows the merge queue head, CI-wait status, candidates, and last drop reason. All tests and lint pass; no gaps found against the brief.
- 2026-09-05T15:26:23+00:00 automated review: approve — All three criteria are met and independently verified against the actual event/state producers, not just the diff; tests and lint pass. cost=$0.60
- 2026-09-05T15:32:09+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
