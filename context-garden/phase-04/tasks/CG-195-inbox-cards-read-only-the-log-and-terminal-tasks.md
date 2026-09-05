---
id: CG-195
title: Inbox cards read only the log, and terminal tasks drop needs-you and automerge notes in every view
status: ready
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 3
difficulty: easy
reading: []
branch: garden/cg-195-inbox-cards-read-only-the-log-and-terminal-tasks
discovered_from: retro:context-garden/phase-03
last_dispatched_at: '2026-09-05T13:16:17+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T14:33:47+00:00'
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
