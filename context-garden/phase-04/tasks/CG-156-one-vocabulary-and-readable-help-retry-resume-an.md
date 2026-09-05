---
id: CG-156
title: 'One vocabulary and readable help: retry, resume and decide named once; help panels; --version;
  garden status at 80 columns'
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
branch: garden/cg-156-one-vocabulary-and-readable-help-retry-resume-an
pr: https://github.com/joshmarcus/context-garden/pull/138
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T12:01:53+00:00'
created: '2026-09-05T03:14:37+00:00'
updated: '2026-09-05T12:22:21+00:00'
---

## Goal

One vocabulary and readable help: retry, resume and decide named once; help panels; --version; garden status at 80 columns.

## Context

From the phase-02 retro's open list (item 10), reconciled against what merged on 2026-09-05: "Vocabulary and help: retry named four ways, decision means three things, flat help, no --version, garden status unreadable at 80 columns, cards that say edit garden.yaml or Mark done". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log

- 2026-09-05T03:25:00+00:00 moved to phase-04: user-facing work, not structure
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 10)
- 2026-09-05T10:31:13+00:00 approved (web)
- 2026-09-05T12:01:53+00:00 dispatched work run 20260905T120144Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4406 tokens)
- 2026-09-05T12:19:43+00:00 opened https://github.com/joshmarcus/context-garden/pull/138 (base main): Gave the CLI one vocabulary and readable help: grouped ~50 commands into named help panels, added a --version flag, made garden status fit 80 columns with a new wont_do column, unified the retry label across CLI/web/TUI, and split the overloaded resume into unpause (dispatch) and resume ID (task). Full suite (602) and ruff pass. cost=$7.21
- 2026-09-05T12:22:21+00:00 automated review: approve — Delivers the derived CG-156 criteria (one retry label, help panels, --version, 80-col status with wont_do, unpause/resume split) with tests; ruff and the related suites pass. cost=$0.84
