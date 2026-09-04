---
id: CG-086
title: Web actions report failures as messages, never as a 500
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/task.html
branch: garden/cg-086-web-actions-report-failures-as-messages-never-as
pr: https://github.com/joshmarcus/context-garden/pull/74
attempts: 1
last_dispatched_at: '2026-09-04T22:55:32+00:00'
created: '2026-09-04T19:37:26+00:00'
updated: '2026-09-04T23:06:06+00:00'
---

## Goal

Every action a person can take in the web UI (trial, dispatch, triage, approve, answer, retry, cancel, persona review, friction report, suggestion) shows a plain message on the page when it cannot be done, with the reason, instead of an Internal Server Error.

## Context

Reported during the first live run: starting a model trial from the task page with one contender returned a 500. The scheduler raised `RuntimeError("a trial needs at least two contenders")`, which is the right refusal, and `task_action` in `web/app.py` let it escape. The same path handles a dozen actions and any `RuntimeError`, `GitHubError` or `GitError` from the scheduler becomes a blank error page. Catch those in the action handlers, put the message in a flash region at the top of the page the person came from (the redirect already exists), and log it. Also validate the trial form before calling the scheduler: the contenders field is a comma-separated list of `harness:model` entries and needs at least two; say so in the placeholder and in the message.

Also: the Answer form on a task that is no longer `waiting_human` does nothing and redirects (CG-092: the task had been moved to ready a minute before the person answered, and the answer vanished without a word). Any action whose precondition no longer holds must say so on the page and keep the typed text.

## Acceptance criteria

- [ ] a trial with one contender shows "a trial needs at least two contenders, e.g. claude:sonnet, claude:opus" on the task page; no 500.
- [ ] every other action's scheduler error shows the same way; a test posts an invalid action and asserts the message and a 303.
- [ ] unexpected exceptions still log a traceback and show a short "something failed; see the log" message.

## Log

- 2026-09-04T19:37:26+00:00 approved
- 2026-09-04T22:55:32+00:00 dispatched work run 20260904T225523Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~6027 tokens)
- 2026-09-04T23:03:17+00:00 discovered work filed: CG-122
- 2026-09-04T23:03:53+00:00 opened https://github.com/joshmarcus/context-garden/pull/74 (base main): task_action now catches RuntimeError/GitError/GitHubError and flashes the message on the page instead of 500ing, converts silent precondition no-ops (approve/unapprove/review/answer/accept/reject) into explicit errors that preserve typed text, pre-validates the trial form, and logs unexpected exceptions with a generic on-page message. cost=$4.75
- 2026-09-04T23:06:06+00:00 automated review: approve — All three acceptance criteria are met with tests; the task_action refactor cleanly converts scheduler errors and stale preconditions into 303 flash messages, preserves typed answers, and logs unexpected errors. Web tests pass and ruff is clean. cost=$0.58
