---
id: CG-199
title: 'Discovered work is deduplicated before it is filed: the same finding from several workers becomes
  one draft'
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading: []
branch: garden/cg-199-discovered-work-is-deduplicated-before-it-is-fil
pr: https://github.com/joshmarcus/context-garden/pull/152
attempts: 1
last_dispatched_at: '2026-09-05T12:48:25+00:00'
created: '2026-09-05T10:30:00+00:00'
updated: '2026-09-05T13:27:50+00:00'
---

## Goal

Six discovered drafts were filed for one red-main fix on 2026-09-05 and cancelled by hand. When a worker reports discovered work, compare its title and body with open tasks in the phase (and the next phase) by normalised title and by the file and symptom named; a near-duplicate becomes a note on the existing task (`also found by CG-xxx`) instead of a new draft, with a `discovered_duplicate` event.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (project-manager:medium); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] A discovered item whose normalised title matches an open task, or whose body names the same file and error, is attached to that task and not filed.
- [ ] The existing task's page lists who else found it.
- [ ] A test files the same discovery from three workers and sees one draft.

## Log

- 2026-09-05T10:31:18+00:00 approved (web)
- 2026-09-05T12:48:25+00:00 dispatched work run 20260905T124816Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~4419 tokens)
- 2026-09-05T13:02:15+00:00 opened https://github.com/joshmarcus/context-garden/pull/152 (base main): Discovered `task` items are now deduplicated against open tasks in the reporting task's phase and the next one, by normalised title or shared file+error, attaching a note instead of filing a near-duplicate draft. cost=$2.18
- 2026-09-05T13:05:12+00:00 automated review: approve — Dedup of discovered work by normalised title or file+symptom against open tasks in the phase and the next, attaching an 'also found by' note plus a discovered_duplicate event instead of filing a near-duplicate draft. All three acceptance criteria met and tested; full suite and lint green. cost=$0.56
- 2026-09-05T13:17:57+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T13:22:04+00:00 automated review produced no verdict (worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_messa) cost=$0.00
- 2026-09-05T13:26:25+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-05T13:27:50+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/152
