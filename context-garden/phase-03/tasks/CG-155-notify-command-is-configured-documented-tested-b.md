---
id: CG-155
title: notify.command is configured, documented, tested by doctor and loud on failure; triage pings fire
  after the review verdict
status: running
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 2
difficulty: easy
reading: []
branch: garden/cg-155-notify-command-is-configured-documented-tested-b
pr: https://github.com/joshmarcus/context-garden/pull/123
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T05:22:18+00:00'
created: '2026-09-05T03:14:37+00:00'
updated: '2026-09-05T05:22:18+00:00'
---

## Goal

notify.command is configured, documented, tested by doctor and loud on failure; triage pings fire after the review verdict.

## Context

From the phase-02 retro's open list (item 8), reconciled against what merged on 2026-09-05: "notify.command unconfigured, undocumented and silent on failure; triage pings before the review verdict". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 8)
- 2026-09-05T03:20:00+00:00 approved (web)
- 2026-09-05T04:57:25+00:00 dispatched work run 20260905T045717Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~3718 tokens)
- 2026-09-05T05:17:47+00:00 opened https://github.com/joshmarcus/context-garden/pull/123 (base main): notify.command failures are now logged instead of swallowed, garden doctor actually runs the command to test it, the config is documented in README/architecture.md/examples, and the awaiting_triage ping now waits for the automated review's verdict instead of firing on PR-open. cost=$3.75
- 2026-09-05T05:21:03+00:00 automated review: approve — Meets all acceptance criteria with correct, well-tested logic: notify.command is documented in three places, doctor runs it for real, failures are logged via garden.notify, and the triage ping is deferred until the review verdict via a one-shot pending_triage_notify flag. Lint and the notify/cli tests pass. cost=$0.73
- 2026-09-05T05:21:10+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_cli.py); a rebase agent will resolve it
- 2026-09-05T05:22:18+00:00 dispatched rebase run 20260905T052218Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~5986 tokens)
