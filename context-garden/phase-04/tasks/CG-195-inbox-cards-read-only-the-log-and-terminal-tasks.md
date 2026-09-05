---
id: CG-195
title: Inbox cards read only the log, and terminal tasks drop needs-you and automerge notes in every view
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: easy
reading: []
branch: garden/cg-195-inbox-cards-read-only-the-log-and-terminal-tasks
pr: https://github.com/joshmarcus/context-garden/pull/161
discovered_from: retro:context-garden/phase-03
attempts: 1
last_dispatched_at: '2026-09-05T14:59:48+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T15:17:12+00:00'
---

## Goal

**User value:** no Inbox card ends in a '] Tests cover' fragment, no done task wears a 'needs you' badge on the Board, and a merged task page no longer says automerge is held.

**Why now:** eight of thirteen Inbox cards and three done tasks are wrong on the walkthrough pages a person opens first; all seven personas list it.

**Size:** easy. **Depends on:** CG-175 (merged) for the transition cleanup; add a one-tick sweep of existing terminal tasks and gate the templates on a non-terminal status, with a walkthrough test that a fresh draft renders no fragment.

## Context

Proposed at the context-garden/phase-03 retro. Cheap, visible on every page and the top finding of the designer, usability and user personas.

## Log

- 2026-09-05T10:31:17+00:00 approved (web)
- 2026-09-05T13:14:53+00:00 dispatched work run 20260905T131445Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4367 tokens)
- 2026-09-05T13:16:00+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:16:17+00:00 dispatched work run 20260905T131617Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4468 tokens)
- 2026-09-05T13:17:48+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:47+00:00 reset to ready by hand
- 2026-09-05T14:34:02+00:00 dispatched work run 20260905T143402Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4754 tokens)
- 2026-09-05T14:37:34+00:00 reset to ready by hand
- 2026-09-05T14:59:48+00:00 dispatched work run 20260905T145948Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4887 tokens)
- 2026-09-05T15:07:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/161 (base main): Verified the prior attempt's three commits fully implement CG-195: split_log() is the single reader of a task's Log section (used by Inbox, board, task page, phase page) so checklist bullets from Acceptance criteria/Out of scope never surface as log fragments; _transition now clears needs_human/pending_feedback/automerge_blocked on any terminal status (done, cancelled, wont_do), with a one-tick _sweep_terminal_state backstop for pre-existing stale state; and the task page template gates its Continue-the-loop button, pending-feedback panel and automerge note on `not task.status.terminal`. Full suite (703 passed, 3 skipped) and ruff both pass; no code changes were needed this round. cost=$0.57
- 2026-09-05T15:11:37+00:00 automated review: approve — All three symptoms (Inbox log fragments, stale needs-you badges, stale automerge-held notes) are fixed with a shared split_log reader, a terminal-status clear in _transition, a one-tick sweep backstop, and template gates; tests (703 passed, 3 skipped) and ruff pass. cost=$0.43
- 2026-09-05T15:17:12+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
