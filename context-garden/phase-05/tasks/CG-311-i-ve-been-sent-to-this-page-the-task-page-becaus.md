---
id: CG-311
title: 'The task page shows the decision a worker''s no-change or question report needs: the same card
  and actions as the Inbox, right where the notification sends you'
status: changes_requested
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
last_dispatched_at: '2026-09-06T04:50:49+00:00'
created: '2026-09-06T01:58:42+00:00'
updated: '2026-09-06T06:00:51+00:00'
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
- 2026-09-06T04:08:26+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 06839c21bbdf, not because of this branch; waiting for the base to go green, no revise round cost=$1.16
- 2026-09-06T04:28:43+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T04:50:49+00:00 dispatched revise run 20260906T045045Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~20590 tokens)
- 2026-09-06T05:01:12+00:00 worker says nothing to change: Current branch code addresses the outstanding review behavior without requiring another change. cost=$1.04
- 2026-09-06T05:22:52+00:00 no-change accepted by the person; resuming the round without a new work run
- 2026-09-06T05:25:55+00:00 operator: the accepted no-change landed in waiting_human with no question; back to in review for its round
- 2026-09-06T05:40:10+00:00 pre-PR check(s) test failed at the stale base 06839c21bbdf; the base branch `main` had moved, so rebased onto it and the checks pass now — no revise round
- 2026-09-06T05:40:14+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/208: The existing revision already renders the shared pending-decision card on task pages and preserves task-specific Inbox Discuss controls. Focused regression tests and lint pass; no further diff is warranted.
- 2026-09-06T06:00:51+00:00 automated review requested changes: The shared decision card and actions are correctly implemented and focused tests pass. The required four-way visual inspection for this UI change is not documented or evidenced. cost=$0.38
