---
id: CG-046
title: 'Task page: a full text box for the send-back note'
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/task.html
- src/garden/web/templates/base.html
branch: garden/cg-046-task-page-a-full-text-box-for-the-send-back-note
pr: https://github.com/joshmarcus/context-garden/pull/11
attempts: 1
last_dispatched_at: '2026-09-04T17:40:47+00:00'
created: '2026-09-04T17:22:57+00:00'
updated: '2026-09-04T18:47:54+00:00'
---

## Goal

On the task page, the "Send back" triage note is a proper multi-line text box, not a 280-pixel single-line input.

## Context

Asked by the person driving the first live run: a triage note is often several sentences (what is wrong, where, what to do instead), and the task page is where one has the room and the context to write it. The page already has the pattern for this: the "Answer and resume" form uses a `textarea` styled in `base.html` (full width, 72px minimum, vertical resize). Make the send-back form on `task.html` match it: a textarea for `note`, the "Send back" button underneath, "Ready for review" and "Open PR" staying as they are. The Inbox card's short input can stay; it is the quick path.

## Acceptance criteria

- [ ] the task page's send-back form uses a textarea for the note, full width, resizable.
- [ ] the form still posts `note` to `/tasks/<id>/triage-changes` and the web test for triage still passes.
- [ ] the Ready and Open PR actions keep their place and look.

## Out of scope

- Changing the Inbox card's input.

## Log

- 2026-09-04T17:22:57+00:00 approved
- 2026-09-04T17:22:57+00:00 dispatched work run 20260904T172257Z-work via manual [human] (fresh session, base main, ~10755 tokens)
- 2026-09-04T17:24:03+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/11 (base main): The task page's send-back note is now a full-width, resizable textarea with the button underneath, matching the answer form.
- 2026-09-04T17:26:12+00:00 automated review: approve — All three acceptance criteria met: textarea with full width and resize, form still posts to triage-changes endpoint with tests passing, Ready/Open actions preserved. Code is clean, properly scoped, and matches the requested pattern from the Answer form. cost=$0.09
- 2026-09-04T17:36:37+00:00 marked ready for review on GitHub; triage done
- 2026-09-04T17:39:52+00:00 2 new review item(s)
- 2026-09-04T17:40:47+00:00 dispatched revise run 20260904T174046Z-revise via local [claude model=sonnet] (fresh session, base main, ~11126 tokens)
- 2026-09-04T17:49:14+00:00 revision failed: worker exited 1: worker error: error_max_turns
- 2026-09-04T18:47:54+00:00 PR #11 merged while the task was failed; the poll skips failed tasks, so set by hand
