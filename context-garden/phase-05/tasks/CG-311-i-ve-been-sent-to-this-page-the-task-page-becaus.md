---
id: CG-311
title: 'The task page shows the decision a worker''s no-change or question report needs: the same card
  and actions as the Inbox, right where the notification sends you'
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/web/pages/task.py
- src/garden/web/templates/task.html
- src/garden/web/templates/inbox.html
- src/garden/inbox.py
- src/garden/scheduler/human.py
- src/garden/notify.py
- tests/test_web.py
branch: garden/cg-311-the-task-page-shows-the-decision-a-worker-s-no-c
attempts: 1
last_dispatched_at: '2026-09-06T02:43:52+00:00'
created: '2026-09-06T01:58:42+00:00'
updated: '2026-09-06T02:43:52+00:00'
---

## Goal

When a notification sends a person to a task page because the worker reported nothing to change, asked a question, or stopped on an error, the page shows the decision to make (accept or reject the call, answer the question, continue or cancel) as the same card with the same actions the Inbox shows, above the fold. Nobody has to go back to the Inbox to find the button.

## Context

Reported by the owner from /tasks/CG-245 on 2026-09-06 01:58Z: "I've been sent to this page because the worker reported there was nothing to be done. But now that I'm on the page, there's no decision to be made (no decision card shown) or way to mark it." The Inbox renders decision cards from the task log (CG-195) and the task page has a decision panel (CG-178 for retro verdicts), but a worker's no-change report and a waiting_human question are not rendered there, so the notification's link lands on a page with nothing to do.

## Acceptance criteria

- [ ] For a task in `awaiting_triage` after a no-change or wont_do report, in `waiting_human` with a question, or `failed`, the task page shows the same decision card as the Inbox (reason, evidence, the worker's full message) with the same actions (accept, reject with a note, answer, continue the loop, discuss, cancel), rendered from one shared template fragment.
- [ ] The notification's link for such a transition points at the task page and the card is the first thing under the title.
- [ ] Tests in tests/test_web.py: a no-change report and a waiting_human question each render the card on the task page with its actions; a task with no pending decision renders none.
- [ ] The Inbox and the task page render the card from the same fragment, so CG-312's layout fix applies to both.

## Log
- 2026-09-06T02:09:41+00:00 approved (cli)
- 2026-09-06T02:43:52+00:00 dispatched work run 20260906T024331Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~13053 tokens)
