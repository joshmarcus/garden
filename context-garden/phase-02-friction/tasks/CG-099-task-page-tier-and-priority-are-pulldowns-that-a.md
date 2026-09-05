---
id: CG-099
title: 'Task page: tier and priority are pulldowns that apply on change, with priority in words'
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/task.html
- src/garden/web/app.py
- src/garden/model.py
branch: garden/cg-099-task-page-tier-and-priority-are-pulldowns-that-a
pr: https://github.com/joshmarcus/context-garden/pull/77
attempts: 1
last_dispatched_at: '2026-09-05T00:41:23+00:00'
created: '2026-09-04T21:09:47+00:00'
updated: '2026-09-05T00:46:29+00:00'
---

## Goal

On the task page the tier and priority controls are pulldowns that apply as soon as they change, with no Set button, and priority is chosen by words that make the order plain.

## Context

Asked during the first live run, after CG-071 delivered the two controls. The tier select has a Set button beside it, which is a click nobody wants; priority is a number box, and nobody remembers whether 0 or 4 goes first. Submit each form on change (`onchange="this.form.submit()"` on the select is enough; no script framework) and reload the page showing the new value with a log line. Replace the number box with a select whose options are words in order from first to last, with the number after the word so the CLI and the task files stay as they are: for example "first · 0", "next · 1", "normal · 2", "later · 3", "someday · 4". Pick the words, keep them plain, and put the scale in one place (`model.py`) so `garden priority`, the trellis and the phase tables can show the same words. A priority outside the scale shows as its number and stays selectable. The same on-change rule applies to any other select the task page grows.

## Acceptance criteria

- [ ] neither control has a button; changing either one posts and the page reloads with the new value.
- [ ] priority options are words with the number beside them, ordered first to last.
- [ ] a test that the page renders the priority words and that posting each value stores the number.

## Log

- 2026-09-04T23:04:28+00:00 dispatched work run 20260904T230419Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~8387 tokens)
- 2026-09-04T23:11:44+00:00 opened https://github.com/joshmarcus/context-garden/pull/77 (base main): Task page tier and priority selects now apply on change with no Set button, and priority is a words-first scale (first·0 .. someday·4) defined once in model.py and reused by the CLI, phase table and board tooltip. cost=$3.46
- 2026-09-04T23:13:01+00:00 automated review: approve — Both task-page controls are now on-change selects with no Set button, priority is a words-first scale defined once in model.py and reused by CLI/phase table, and a test covers rendering order and per-value storage including out-of-scale. All acceptance criteria met; tests and ruff pass. cost=$0.67
- 2026-09-05T00:02:23+00:00 PR conflicts with main (src/garden/web/templates/task.html); revise run will rebase and resolve
- 2026-09-05T00:41:23+00:00 dispatched revise run 20260905T004122Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~10408 tokens)
- 2026-09-05T00:45:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/77: Rebased CG-099 onto current main, resolving the task.html conflict by keeping main's newer 'Latest run' link while preserving the priority_label() call and on-change select markup from this branch; force-push is expected from the runner. cost=$0.89
- 2026-09-05T00:46:29+00:00 automated review: approve — Both task-page controls are on-change selects with no Set button, priority is a words-first scale centralized in model.py and reused across CLI/phase table/board, and a test covers rendering order, per-value storage, and the out-of-scale case. Tests and ruff pass. cost=$0.62
