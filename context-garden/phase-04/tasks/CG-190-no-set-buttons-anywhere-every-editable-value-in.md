---
id: CG-190
title: 'No Set buttons anywhere: every editable value in the web UI applies when the user changes it,
  with a saved mark and an undo'
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/config.html
- src/garden/web/templates/task.html
- src/garden/web/templates/phase.html
- src/garden/web/actions/control.py
- src/garden/web/actions/tasks.py
created: '2026-09-05T10:26:48+00:00'
updated: '2026-09-05T10:26:48+00:00'
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

