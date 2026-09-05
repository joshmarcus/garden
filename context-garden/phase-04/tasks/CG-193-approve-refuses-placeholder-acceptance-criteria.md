---
id: CG-193
title: Approve refuses placeholder acceptance criteria and unresolved reading-list paths
status: in_review
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
attempts: 2
last_dispatched_at: '2026-09-05T15:10:35+00:00'
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T15:19:35+00:00'
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
- 2026-09-05T12:52:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/149: Resolved the src/garden/inbox.py rebase conflict by merging main's move-to-phase/drop actions for draft tasks (CG-162) with this branch's brief_gaps() check and 'why' annotation; inbox.html merged cleanly. Full test suite (632 passed, 3 skipped) and ruff both clean after rebase. cost=$0.23
- 2026-09-05T12:56:38+00:00 automated review: approve — Approve now refuses placeholder acceptance criteria and unresolved reading-list paths via a shared brief_gaps() check, and the Inbox card surfaces the gap; all criteria are tested, full suite and ruff are green. cost=$0.53
- 2026-09-05T13:00:27+00:00 automated review: approve — Approve now refuses placeholder acceptance criteria and unresolved reading-list paths via a shared brief_gaps() check, and the Inbox card surfaces the gap. All three criteria are tested; full suite (632 passed) and ruff are green; description is clean. cost=$0.47
- 2026-09-05T13:11:34+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py); a rebase agent will resolve it
- 2026-09-05T13:13:11+00:00 dispatched rebase run 20260905T131311Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~6768 tokens)
- 2026-09-05T13:14:19+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:14:44+00:00 dispatched work run 20260905T131444Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~5054 tokens)
- 2026-09-05T13:16:00+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:46+00:00 re-enabled by hand; revise run will follow
- 2026-09-05T14:34:10+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-193`) or send it back (`garden triage CG-193 --changes "..."`)
- 2026-09-05T15:10:01+00:00 nothing to fix; resumed to in review by hand
- 2026-09-05T15:10:16+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py, src/garden/web/templates/inbox.html); a rebase agent will resolve it
- 2026-09-05T15:10:35+00:00 dispatched rebase run 20260905T151035Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~9673 tokens)
- 2026-09-05T15:19:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/149: Rebased onto origin/main, resolving conflicts in src/garden/inbox.py, src/garden/web/templates/inbox.html, and tests/fake_claude.py (kept both sides in each). Full suite then surfaced 2 failures in tests/test_approve_phase.py (a CG-186 test file merged from main whose draft fixtures hit this branch's new brief_gaps() approve gate); fixed by applying this branch's own existing complete_brief() test helper to those two tests, in a separate commit. Full suite: 713 passed, 3 skipped; ruff clean. cost=$0.82
- 2026-09-05T15:19:35+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-193` for one more round, or review on GitHub
