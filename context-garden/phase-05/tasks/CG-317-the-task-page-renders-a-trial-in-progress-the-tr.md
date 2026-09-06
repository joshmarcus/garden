---
id: CG-317
title: 'The task page renders a trial in progress: the trial panel treats winner, scores and PRs as optional,
  and a test renders a task mid-trial with a failed contender'
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/web/templates/task.html
- src/garden/web/pages/task.py
- src/garden/scheduler/trials.py
- src/garden/web/templates/trials.html
- tests/test_web.py
branch: garden/cg-317-the-task-page-renders-a-trial-in-progress-the-tr
attempts: 1
last_dispatched_at: '2026-09-06T03:03:16+00:00'
created: '2026-09-06T02:14:10+00:00'
updated: '2026-09-06T03:03:16+00:00'
---

## Goal

A task page never fails while a trial is running. The trial panel reads `winner`, per-contender `score`, `pr` and `cost` as optional values and shows what is known so far (contender, model, status, run, elapsed) with a plain "no verdict yet"; the page for a task whose trial was reset by `--again` or whose contender failed renders the same way.

## Context

2026-09-06 02:13Z: /tasks/CG-307 returned 500 with `jinja2.exceptions.UndefinedError: 'dict object' has no attribute 'winner'` while its design trial was in progress (one contender running, one failed, the state reset once by `garden trial --again`). CG-185 promised that no page 500s on an undefined template variable, and this path escaped it because the trial state only gains `winner` when the comparison finishes. The owner hit it while checking on the design work.

## Acceptance criteria

- [ ] `task.html`'s trial panel renders for a trial state with no `winner`, contenders with no `score`/`pr`/`cost`, and a contender in `failed` or `env_error`, showing status and elapsed time per contender and "no verdict yet"; the page returns 200.
- [ ] A test in tests/test_web.py renders a task mid-trial (one running contender, one failed, no winner) and after `--again` (reset state) and asserts 200 and the panel text.
- [ ] The StrictUndefined guard from CG-185 covers the trial panel: every optional trial field goes through `.get` or a default filter, checked by the existing template-variable test.

## Log
- 2026-09-06T02:14:11+00:00 approved (cli)
- 2026-09-06T03:03:16+00:00 dispatched work run 20260906T030249Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~14905 tokens)
