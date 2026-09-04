---
id: CG-087
title: Trial form picks contenders from the known harnesses and models
status: ready
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
created: '2026-09-04T19:40:52+00:00'
updated: '2026-09-04T19:40:52+00:00'
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
