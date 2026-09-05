---
id: CG-193
title: Approve refuses placeholder acceptance criteria and unresolved reading-list paths
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
branch: garden/cg-193-approve-refuses-placeholder-acceptance-criteria
pr: https://github.com/joshmarcus/context-garden/pull/149
discovered_from: retro:context-garden/phase-03
attempts: 1
last_dispatched_at: '2026-09-05T12:48:06+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T12:48:06+00:00'
---

## Goal

**User value:** a task cannot be dispatched with 'to be written at planning' criteria or a reading list that names a missing file; the Inbox approve card shows the gap so the person fixes the brief before spending a run.

**Why now:** four tasks shipped with placeholder criteria and six with stale reading lists this phase; the project-manager persona calls it half the phase's friction, and CG-179 (results speak to each criterion) is empty without real criteria.

**Size:** medium. **Depends on:** CG-149 (merged) for path verification; prerequisite for CG-179.

## Context

Proposed at the context-garden/phase-03 retro. The recurring brief defects have a single chokepoint, approve, and fixing it there makes every later task cheaper.

## Log

- 2026-09-05T10:31:17+00:00 approved (web)
- 2026-09-05T12:34:17+00:00 dispatched work run 20260905T123408Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4368 tokens)
- 2026-09-05T12:47:44+00:00 opened https://github.com/joshmarcus/context-garden/pull/149 (base main): approve now refuses a draft whose brief has placeholder acceptance criteria or a reading-list path that resolves to no file, via a shared brief_gaps() check; the Inbox approve card lists the gaps so the person fixes the brief before spending a run. cost=$4.76
- 2026-09-05T12:47:55+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py); a rebase agent will resolve it
- 2026-09-05T12:48:06+00:00 dispatched rebase run 20260905T124806Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~6294 tokens)
