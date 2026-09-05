---
id: CG-161
title: garden plan does not check a frozen phase (only closed)
status: failed
product: context-garden
phase: phase-03
depends_on:
- CG-148
priority: 1
difficulty: easy
reading:
- src/garden/scheduler.py
- src/garden/web/app.py
- src/garden/model.py
- src/garden/cli.py
branch: garden/cg-161-garden-plan-does-not-check-a-frozen-phase-only-c
pr: https://github.com/joshmarcus/context-garden/pull/108
discovered_from: CG-148
attempts: 1
last_dispatched_at: '2026-09-05T04:15:57+00:00'
created: '2026-09-05T03:55:13+00:00'
updated: '2026-09-05T04:31:25+00:00'
---

## Goal

`plan_phase` (web) and `garden plan` only refuse a closed phase; a frozen phase still accepts new planner-created drafts. Drafts still can't be approved without a freeze exception, so this is low-risk, but for full parity with the freeze's intent (no new work materializing during a freeze) planning could also be blocked, or explicitly documented as allowed.

## Context

Noticed while implementing CG-148; left out to keep that task's scope to approve/dispatch/discovered-work as specified in its acceptance criteria.

## Provenance

Discovered by CG-148 (A frozen or closed phase refuses approvals and dispatch; a freeze is a phase state, not a note) during run `20260905T033732Z-work`.

## Log

- 2026-09-05T03:55:13+00:00 discovered by CG-148
- 2026-09-05T03:57:42+00:00 approved (web)
- 2026-09-05T04:15:57+00:00 dispatched work run 20260905T041549Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-148-a-frozen-or-closed-phase-refuses-approvals-and-d stacked on CG-148, ~6379 tokens)
- 2026-09-05T04:21:17+00:00 discovered work filed: CG-171, CG-172
- 2026-09-05T04:22:51+00:00 pre-PR check(s) test, lint failed at the stale base 55a935290123; the base branch `garden/cg-148-a-frozen-or-closed-phase-refuses-approvals-and-d` had moved, so rebased onto it and the checks pass now — no revise round
- 2026-09-05T04:22:54+00:00 opened https://github.com/joshmarcus/context-garden/pull/108 (base garden/cg-148-a-frozen-or-closed-phase-refuses-approvals-and-d): garden plan (CLI) and the web plan_phase action now refuse a frozen phase outright (unfreeze first), matching the closed-phase guard; --dry-run still works. Added tests to test_freeze_phase.py and updated the frozen banner copy. cost=$0.98
- 2026-09-05T04:29:07+00:00 PR closed without merging: https://github.com/joshmarcus/context-garden/pull/108
- 2026-09-05T04:30:17+00:00 parent CG-148 merged; rebased onto main and retargeted the PR
- 2026-09-05T04:30:19+00:00 PR closed without merging: https://github.com/joshmarcus/context-garden/pull/108
- 2026-09-05T04:31:25+00:00 PR closed without merging: https://github.com/joshmarcus/context-garden/pull/108
