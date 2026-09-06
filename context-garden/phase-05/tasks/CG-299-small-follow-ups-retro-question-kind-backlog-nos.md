---
id: CG-299
title: 'Small follow-ups: retro_question kind, backlog noscript, CI flake, ambient config dir in tests,
  a second opinion for self products'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 4
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:20+00:00'
updated: '2026-09-06T00:52:25+00:00'
---

## Goal

Close six small follow-ups from the phase-04 retro: resolve the unused `retro_question` notification kind (drop it or wire it to a handler), add a no-JS submit path to the backlog phase form, make doctor's console lines wrap-safe for long paths, isolate tests from ambient `CLAUDE_CONFIG_DIR`/`CODEX_HOME`, require a persona review or a human approver for the second approval round on `self: true` products, and cap consecutive env-error returns per task while matching only the harness's own error field.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Acceptance criteria

- [ ] The `retro_question` notification kind is either rendered by a handler or removed from the notification schema/enum, so no dead kind is referenced without a consumer.
- [ ] The backlog phase form has a working `<noscript>` submit fallback and doctor's console output wraps instead of truncating for long paths, each verified by a test: one submitting the form with JS disabled, one asserting long-path output wraps within terminal width.
- [ ] A shared conftest fixture unsets `CLAUDE_CONFIG_DIR` and `CODEX_HOME` before tests run, verified by a test that fails if either variable leaks from the ambient environment.
- [ ] For `self: true` products, the second approving round requires a persona review or a human approver rather than another automated pass from the same product, verified by a test that exercises a `self: true` product and asserts the second round is not self-approved.
- [ ] Consecutive environment-error returns for a single task are capped, and only the harness's own error field is matched (not an error field nested in worker/tool output), verified by a test that simulates repeated env errors and asserts retries stop at the cap.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-288 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005029Z-edit) cost=$0.10
- 2026-09-06T00:52:25+00:00 approved (cli)
