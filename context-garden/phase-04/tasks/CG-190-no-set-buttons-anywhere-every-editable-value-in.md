---
id: CG-190
title: 'No Set buttons anywhere: every editable value in the web UI applies when the user changes it,
  with a saved mark and an undo'
status: in_review
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/config.html
- src/garden/web/templates/task.html
- src/garden/web/templates/phase.html
- src/garden/web/actions/control.py
- src/garden/web/actions/tasks.py
branch: garden/cg-190-no-set-buttons-anywhere-every-editable-value-in
pr: https://github.com/joshmarcus/context-garden/pull/146
attempts: 1
last_dispatched_at: '2026-09-05T12:45:04+00:00'
created: '2026-09-05T10:26:48+00:00'
updated: '2026-09-05T12:59:11+00:00'
---

## Goal

Changing a value is saving it. Every editable control in the web UI (pulldowns, number fields, text fields, toggles) applies on change: a pulldown or toggle posts immediately, a text or number field posts on Enter or when it loses focus, and the control shows a brief "saved" mark and offers undo for a few seconds. No Set, Apply or Save button remains; forms that create something (a new task, a friction report, a note with an action) keep their one submit button because they are not edits.

## Context

The user on 2026-09-05: "task for next time: no 'Set' buttons, automatically update if user updates the value." CG-099 did this for the tier and priority pulldowns on the task page; the Config page's live overrides (`max_parallel`, budgets) and other fields still use a button. The rule from CG-099 becomes the rule everywhere, with the same HTMX pattern: the control is inside its own form, `hx-trigger="change"` (or `blur, keyup[key=='Enter']` for text), the response swaps the control back with the saved mark.

## Acceptance criteria

- [ ] No Set, Apply or Save button in any template for editing an existing value; a grep in the test suite enforces it.
- [ ] Each edited value posts on change (text and number on Enter or blur), shows a saved mark, and offers undo that restores the previous value with one press.
- [ ] Without JavaScript every control still works: the form posts on Enter and the page reloads with the new value.
- [ ] The walkthrough's Config and task pages show the pattern; a test edits `max_parallel` on the Config page and sees it applied without a button.

## Log

- 2026-09-05T10:31:16+00:00 approved (web)
- 2026-09-05T12:25:49+00:00 dispatched work run 20260905T122540Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~15741 tokens)
- 2026-09-05T12:44:45+00:00 opened https://github.com/joshmarcus/context-garden/pull/146 (base main): Every editable value in the web UI (task tier/priority, the Config page's live max_parallel override, and a phase's budget) now applies on change with a saved mark and a one-press undo, and no Set/Apply/Save button remains anywhere; a grep test enforces the latter. cost=$3.04
- 2026-09-05T12:44:53+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/templates/task.html); a rebase agent will resolve it
- 2026-09-05T12:45:04+00:00 dispatched rebase run 20260905T124504Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~6756 tokens)
- 2026-09-05T12:49:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/146: Rebased onto origin/main; resolved the sole conflict in src/garden/web/templates/task.html by keeping main's new 'move to another phase' form (from CG-162, merged after this branch forked) and applying the incoming commit's data-autosave/requestSubmit/saved-mark markup to the difficulty and priority selects. No other files touched. Full test suite (626 passed, 3 skipped) and a grep for stray Set/Apply/Save buttons both pass. cost=$0.24
- 2026-09-05T12:51:15+00:00 automated review: approve — Every editable value (task tier/priority, config max_parallel, phase budget) applies on change with a saved mark and undo; no Set/Apply/Save buttons remain, enforced by a grep test. Tests and ruff pass. cost=$1.03
- 2026-09-05T12:59:11+00:00 automated review: approve — Every editable scalar (tier, priority, max_parallel, budget) applies on change with a saved mark and one-press undo; no Set/Apply/Save button remains, enforced by a grep test. Full suite (626 passed, 3 skipped) and ruff pass; change is localized and well-described. cost=$1.13
