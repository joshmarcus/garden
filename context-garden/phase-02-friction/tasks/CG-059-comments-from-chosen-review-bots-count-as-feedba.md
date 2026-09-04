---
id: CG-059
title: Bot comments count as feedback unless excluded
status: awaiting_triage
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/github.py
- src/garden/config.py
branch: garden/cg-059-bot-comments-count-as-feedback-unless-excluded
pr: https://github.com/joshmarcus/context-garden/pull/30
attempts: 1
last_dispatched_at: '2026-09-04T17:57:36+00:00'
created: '2026-09-04T17:53:43+00:00'
updated: '2026-09-04T17:59:52+00:00'
---

## Goal

Review comments from bots (a Codex or Copilot review app, a linter bot) become feedback for a revise round; only logins listed in config are ignored.

## Context

Asked during the first live run: PR #20 received three line comments from `chatgpt-codex-connector[bot]` and a review summary, and the person expected the garden to act on them. `GitHub.feedback_since` dropped every author whose login ends in `[bot]`. That rule predates the marker that now tells the garden's own comments apart, so it no longer protects the loop from itself; it only hides reviewers the person installed on purpose. Remove the rule. `github.bot_logins` (already read into `GitHub.bot_logins`) stays as the way to ignore specific accounts such as a dependency bot. Say in the revise brief that an item came from a bot.

## Acceptance criteria

- [ ] a comment from a `[bot]` login is returned by `feedback_since` unless the login is in `bot_logins`.
- [ ] the README documents `github.bot_logins` as the exclusion list, with an example.
- [ ] the unit tests cover both cases.

## Log

- 2026-09-04T17:57:36+00:00 dispatched work run 20260904T175736Z-work via manual [human] (fresh session, base main, ~7387 tokens)
- 2026-09-04T17:59:52+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/30 (base main): Bot comments now count as feedback; github.bot_logins is the exclusion list and is wired from config; bot items are labelled in the revise brief.
