---
id: CG-209
title: Brief gate for blocking discovered tasks
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-193
priority: 2
difficulty: easy
reading: []
branch: garden/cg-209-brief-gate-for-blocking-discovered-tasks
pr: https://github.com/joshmarcus/context-garden/pull/157
discovered_from: CG-193
attempts: 1
last_dispatched_at: '2026-09-05T13:07:06+00:00'
created: '2026-09-05T12:46:14+00:00'
updated: '2026-09-05T13:37:39+00:00'
---

## Goal

Blocking discovered tasks (`discovered.auto_approve_blocking`) are created straight to `ready` in `scheduler/discovered.py`, bypassing the `approve` gate and so the CG-193 brief_gaps check. Decide whether an auto-approved discovered task with placeholder criteria or an unresolved reading path should be held as a draft (or flagged) rather than dispatched.

## Context

CG-193 put the placeholder/reading check in `approve`; this is the one ready-transition that does not pass through it.

## Provenance

Discovered by CG-193 (Approve refuses placeholder acceptance criteria and unresolved reading-list paths) during run `20260905T123408Z-work`.

## Log

- 2026-09-05T12:46:14+00:00 discovered by CG-193
- 2026-09-05T12:50:55+00:00 approved (web)
- 2026-09-05T13:07:06+00:00 dispatched work run 20260905T130656Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-193-approve-refuses-placeholder-acceptance-criteria stacked on CG-193, ~4492 tokens)
- 2026-09-05T13:12:50+00:00 opened https://github.com/joshmarcus/context-garden/pull/157 (base garden/cg-193-approve-refuses-placeholder-acceptance-criteria): Blocking discovered tasks now run through brief_gaps before going straight to ready: one with placeholder acceptance criteria or an unresolved reading path is filed as a draft with the gap logged, instead of dispatching a run. Added a fake-worker mode and coordination test covering the held-draft path, and completed the acceptance criteria in the existing discover fixture so its unrelated test still exercises the ready path. cost=$0.83
- 2026-09-05T13:14:23+00:00 automated review produced no verdict (worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_messa) cost=$0.00
- 2026-09-05T13:37:39+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/157
