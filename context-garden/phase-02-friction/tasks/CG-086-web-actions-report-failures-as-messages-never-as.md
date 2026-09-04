---
id: CG-086
title: Web actions report failures as messages, never as a 500
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/app.py
- src/garden/web/templates/task.html
created: '2026-09-04T19:37:26+00:00'
updated: '2026-09-04T19:37:26+00:00'
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
