---
id: CG-118
title: A bot comment that is a notice, not a finding, is not feedback
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/github.py
- src/garden/scheduler.py
- tests/test_github.py
created: '2026-09-04T21:59:16+00:00'
updated: '2026-09-04T21:59:16+00:00'
---

## Goal

A comment from a review bot that carries no finding (a usage-limit notice, "no issues found", a status line) does not count as feedback, does not move the task to `changes_requested`, and does not start a revise round.

## Context

Found on the first live run. Codex hit its usage limit for code reviews at 21:57; from then on every new PR received a comment from `chatgpt-codex-connector[bot]` saying "You have reached your Codex usage limits for code reviews". The poll counted each one as "1 new review item", moved CG-111 to `changes_requested` and would have dispatched a revise round to address the notice; the person put it back by hand. CG-059 made bot comments count, which is right for findings. Tell the two apart: a bot comment is feedback only when it points at code (a review comment on a diff line, or a body that carries a finding marker such as Codex's `[P1]`/`[P2]` badges) or when a human wrote it; a bot comment that matches a small list of notice patterns (`usage limit`, `no issues`, `looks good`, `reviewed and found nothing`) is logged on the task ("bot notice ignored: ...") and otherwise ignored. Keep the patterns in `github.bot_notice_patterns` with those defaults so a work setting can add its own bot's phrasing. Do not use `bot_logins` for this: that silences a bot's findings as well.

## Acceptance criteria

- [ ] a bot comment matching a notice pattern does not count as feedback; the task log records it.
- [ ] a bot comment with a `[P1]`/`[P2]` badge or on a diff line still counts.
- [ ] tests for both, and the README lists the config key.
