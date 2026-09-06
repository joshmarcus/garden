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
pr: https://github.com/joshmarcus/context-garden/pull/208
attempts: 1
last_dispatched_at: '2026-09-06T03:50:20+00:00'
created: '2026-09-06T01:58:42+00:00'
updated: '2026-09-06T03:50:20+00:00'
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
- 2026-09-06T03:00:01+00:00 opened https://github.com/joshmarcus/context-garden/pull/208 (base main): Task pages now show the same shared pending-decision card as the Inbox directly below the task title. The card supports worker reports, questions, and stopped/failed runs, with regression coverage and commit 9523d65. cost=$0.82
- 2026-09-06T03:01:58+00:00 automated review requested changes: The shared card is correctly placed and focused web tests pass, but the new shared Inbox card breaks Discuss when more than one attention item is present. The PR description also needs phase context and verification results. cost=$0.23
- 2026-09-06T03:02:48+00:00 dispatched revise run 20260906T030243Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~19351 tokens)
- 2026-09-06T03:15:44+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/208: Task pages retain the shared pending-decision card, and shared Inbox attention cards now use task-specific Discuss panel and copy targets so multiple stopped tasks remain independently actionable. cost=$0.39
- 2026-09-06T03:21:35+00:00 automated review: approve — The shared decision-card fragment is rendered directly below the task title and reused by the Inbox; focused web tests pass. cost=$0.28
- 2026-09-06T03:22:12+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-06T03:30:06+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-06T03:33:19+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/templates/task.html); a rebase agent will resolve it
- 2026-09-06T03:35:32+00:00 dispatched rebase run 20260906T033526Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~7574 tokens)
- 2026-09-06T03:47:19+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated cost=$0.01
- 2026-09-06T03:50:20+00:00 dispatched revise run 20260906T035020Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~21094 tokens)
