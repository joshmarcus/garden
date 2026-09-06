---
id: CG-299
title: 'Small follow-ups: retro_question kind, backlog noscript, CI flake, ambient config dir in tests,
  a second opinion for self products'
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 4
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:20+00:00'
updated: '2026-09-06T00:50:28+00:00'
---

## Goal

Drop or wire the retro_question notification kind; add a noscript submit to the backlog phase form; make doctor's console lines wrap-safe for long paths; a conftest fixture clears CLAUDE_CONFIG_DIR and CODEX_HOME; for self: true products the second approving round is a persona review or a person; cap consecutive env-error returns per task and match only the harness's own error field.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Suggestions

- [ ] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-288 (renumbered by the operator: two reconcile runs drew ids from one counter)
