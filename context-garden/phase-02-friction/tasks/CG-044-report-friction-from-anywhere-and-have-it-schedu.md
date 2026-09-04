---
id: CG-044
title: Report friction from anywhere, and have it scheduled
status: awaiting_triage
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/inbox.py
- src/garden/web/app.py
- src/garden/cli.py
- context-garden/phase-02-friction/specs/friction-log.md
branch: garden/cg-044-report-friction-from-anywhere-and-have-it-schedu
pr: https://github.com/joshmarcus/context-garden/pull/25
attempts: 1
last_dispatched_at: '2026-09-04T17:38:14+00:00'
created: '2026-09-04T17:21:39+00:00'
updated: '2026-09-04T17:49:14+00:00'
---

## Goal

A person can file a friction report about the process from wherever they are (the Inbox, a task page, the CLI, a chat session) in one step, and every report becomes something the loop schedules: a line in the phase's `docs/friction.md` and a draft task with provenance.

## Context

During the first live run (CG-027) the only ways to record friction were: write it into `docs/friction.md` on a branch, list it under `discovered` in a finish result, or run `garden new-task` and fill the template by hand. None is available from the page where the friction is noticed, and none records what the person was looking at. The request from the person driving the run: "we should always have the ability to capture friction reports about this overall process to be scheduled."

Provide: a "Report friction" form on the Inbox and on every task page (text plus the current page and task as provenance); `garden friction-report <product/phase> "text"` for the CLI and for chat sessions; both append to `docs/friction.md` under a "Reported" heading with date, task and page, and create a draft task titled from the first line with the report as its Context. The planner already reads `docs/*.md`, so reports also reach the next planning round. CG-008's harvester must leave the "Reported" section alone.

## Acceptance criteria

- [ ] a form on the Inbox and task pages files a report in one submit; the CLI command does the same.
- [ ] each report appends to `docs/friction.md` with provenance and creates a draft task linked to it.
- [ ] `garden friction` (the harvester) preserves reported entries.
- [ ] tests for the CLI path and the web path.

## Out of scope

- Chatting about a report inside the UI; see the task on attention cards for the decision context.

## Log

- 2026-09-04T17:23:57+00:00 approved (web)
- 2026-09-04T17:38:14+00:00 dispatched work run 20260904T173814Z-work via local [claude model=sonnet] (fresh session, base main, ~9649 tokens)
- 2026-09-04T17:45:47+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/25 (base main): Added friction reporting from three surfaces: the CLI (`garden friction-report <product/phase> "text"`), the web Inbox, and every task page. Each report appends to `docs/friction.md` under a `## Reported` section with date and provenance, creates a draft task from the report, and the `garden friction` harvester now preserves the Reported section when regenerating the file. All 126 tests pass, lint clean. cost=$2.07
- 2026-09-04T17:49:14+00:00 automated review: approve — All four acceptance criteria met, 41 tests pass, lint clean. One dead-code guard in _extract_reported_section and a minor multi-product usability quirk in the inbox form are both harmless in the common single-product case. cost=$0.53
