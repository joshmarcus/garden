---
id: CG-087
title: Trial form picks contenders from the known harnesses and models
status: done
product: context-garden
phase: phase-02-friction
depends_on:
- CG-086
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/task.html
- src/garden/web/app.py
- src/garden/config.py
- src/garden/harness.py
branch: garden/cg-087-trial-form-picks-contenders-from-the-known-harne
pr: https://github.com/joshmarcus/context-garden/pull/78
attempts: 1
last_dispatched_at: '2026-09-04T23:04:19+00:00'
created: '2026-09-04T19:40:52+00:00'
updated: '2026-09-05T00:05:57+00:00'
---

## Goal

Starting a model trial from the task page means choosing contenders from menus of the harnesses and models the garden knows about, not typing `harness:model` pairs into a text box.

## Context

Asked during the first live run after a trial attempt failed on the free-text field. The garden already knows the candidates: every harness under `harnesses:` in config, each harness's tier map (`models`) and `review_model`, plus the full model names used today (`claude-sonnet-5`, `claude-opus-4-8`, `fable`); the harness's own aliases (`sonnet`, `opus`, `haiku`, `fable`) are also valid. Replace the field with a contender list: two rows to start, an "add contender" control for more, each row a harness select and a model select populated from config (with an "other…" entry that reveals a text input for a model name not in the map), and a "current tier" option that uses whatever the task would normally get. Post the chosen pairs as a list; the handler validates at least two distinct pairs and shows a message otherwise (CG-086). The Trials page's leaderboard gets the same selects for its filter, and the CLI `garden trial -c` keeps accepting the pair syntax.

## Acceptance criteria

- [ ] the task page's trial form has harness and model selects seeded from config, two rows by default, add and remove controls, and an "other" escape.
- [ ] fewer than two distinct contenders, or a duplicate, is refused with a message on the page.
- [ ] a test renders the form for a config with two harnesses and posts a valid and an invalid selection.

## Log

- 2026-09-04T19:40:52+00:00 approved
- 2026-09-04T23:04:19+00:00 dispatched work run 20260904T230410Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-086-web-actions-report-failures-as-messages-never-as stacked on CG-086, ~11399 tokens)
- 2026-09-04T23:15:09+00:00 opened https://github.com/joshmarcus/context-garden/pull/78 (base garden/cg-086-web-actions-report-failures-as-messages-never-as): Replaced the free-text trial contender field with harness/model select rows (seeded from garden.yaml, with an 'other…' escape and 'current tier' default) on the task page, added a matching filter to the trials leaderboard, and made the web handler reject duplicate contenders with a message. CLI `garden trial -c` is unchanged. cost=$5.85
- 2026-09-04T23:17:02+00:00 automated review: approve — Replaces the free-text trial field with config-seeded harness/model contender rows (add/remove, other-escape, current-tier default), adds a matching leaderboard filter, and rejects duplicate contenders with a page message. All acceptance criteria met with a test; web tests and ruff pass. cost=$0.66
- 2026-09-05T00:05:57+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/78
