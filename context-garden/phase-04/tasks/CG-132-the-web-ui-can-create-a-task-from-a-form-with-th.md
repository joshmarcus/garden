---
id: CG-132
title: The web UI can create a task from a form, with the same fields as garden new-task
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/phase.html
- src/garden/scaffold.py
- src/garden/cli.py
branch: garden/cg-132-the-web-ui-can-create-a-task-from-a-form-with-th
pr: https://github.com/joshmarcus/context-garden/pull/133
attempts: 2
last_dispatched_at: '2026-09-05T12:07:09+00:00'
created: '2026-09-05T00:27:31+00:00'
updated: '2026-09-05T12:15:03+00:00'
---

## Goal

A person can add a task from the web UI: a "New task" form on the phase page (and a link from the rail) with title, goal, context, acceptance criteria, difficulty, priority (the words from CG-099), reading list, dependencies and an "approve now" box, producing the same task file `garden new-task` would.

## Context

Asked on the first live run. The web has three ways to make tasks appear and none is a plain "add a task": the friction-report form files a draft framed as friction and takes only free text; the phase page's plan action runs the planner agent to propose tasks; the task page's suggestion box (CG-079) changes an existing task. Every task the person wanted tonight went through the CLI or a chat session. The form should reuse the scaffold's template so the file is identical to the CLI's, validate like `garden validate`, land the task as draft unless "approve now" is ticked, and return to the new task's page with a flash message (CG-086). Keep the copy plain and the form short; the acceptance criteria field can start with three empty checkboxes.

## Acceptance criteria

- [ ] the phase page has a New task form with the fields above; submitting creates the file and redirects to the task page.
- [ ] the created file matches `garden new-task` output for the same inputs; a test compares them.
- [ ] validation errors show as a message on the form with the typed text kept.

## Log

- 2026-09-05T03:15:00+00:00 moved to phase-04 at the phase-02 close (deferred by the freeze)

- 2026-09-05T00:34:28+00:00 deferred by the feature freeze (2026-09-05): carry into phase 03
- 2026-09-05T03:01:07+00:00 approved (web)
- 2026-09-05T03:02:32+00:00 dispatched work run 20260905T030223Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~5932 tokens)
- 2026-09-05T03:05:29+00:00 back to draft: approved by mistake during the phase 02 freeze; phase 03 work (CG-137 runs alone, first)
- 2026-09-05T10:31:12+00:00 approved (web)
- 2026-09-05T11:51:27+00:00 dispatched work run 20260905T115127Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-197-split-cli-py-into-a-cli-package-and-fold-the-fou stacked on CG-197, ~13606 tokens)
- 2026-09-05T11:55:55+00:00 parent CG-197 merged; will rebase onto main when the current run finishes
- 2026-09-05T12:03:10+00:00 parent CG-197 merged; rebased onto main and retargeted the PR
- 2026-09-05T12:04:20+00:00 opened https://github.com/joshmarcus/context-garden/pull/133 (base main): Added a New task form to the phase page (title, goal, context, acceptance criteria, difficulty, priority, reading list, dependencies, approve-now) with a rail link, validation matching `garden validate`, and a test proving the created file matches `garden new-task`'s output. cost=$2.65
- 2026-09-05T12:05:49+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/pages/phase.py); a rebase agent will resolve it
- 2026-09-05T12:06:55+00:00 automated review: approve — Adds a New task form to the phase page with a rail link, validation like garden validate, and byte-identical output to garden new-task; all three acceptance criteria are met and tested, checks pass. cost=$0.85
- 2026-09-05T12:07:09+00:00 dispatched rebase run 20260905T120709Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~4544 tokens)
- 2026-09-05T12:12:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/133: Rebased onto main; resolved the single conflict in src/garden/web/pages/phase.py by keeping both sides' additions — main's has_retro/_retro_doc/_retro_operator/_persona_scores (from CG-146) and this branch's new_task/_new_task_prefill (from CG-132) — in both the phase_page template context and the module-level helper functions. Full test suite (607 passed, 3 skipped) and ruff both pass. cost=$0.25
- 2026-09-05T12:13:47+00:00 automated review: approve — Adds a New task form to the phase page with a rail link, validation matching garden validate, and byte-identical output to garden new-task; all three acceptance criteria are met and tested, and checks pass. cost=$0.88
- 2026-09-05T12:13:58+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T12:15:03+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-132` for one more round, or review on GitHub
