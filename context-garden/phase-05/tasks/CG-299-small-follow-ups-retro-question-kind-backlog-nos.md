---
id: CG-299
title: 'Small follow-ups: retro_question kind, backlog noscript, CI flake, ambient config dir in tests,
  a second opinion for self products'
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 4
difficulty: easy
reading: []
branch: garden/cg-299-small-follow-ups-retro-question-kind-backlog-nos
pr: https://github.com/joshmarcus/context-garden/pull/282
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-07T08:42:32+00:00'
created: '2026-09-05T23:58:20+00:00'
updated: '2026-09-07T09:13:30+00:00'
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
- 2026-09-07T07:50:43+00:00 dispatched work run 20260907T074953Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~9392 tokens)
- 2026-09-07T08:05:31+00:00 preserved uncommitted worktree changes from run 20260907T074953Z-work outside the PR: `git stash apply 4990d1ccb1a8e02cb4aef4b4946f225fd06da4e4` in /home/joshua/work/worktrees/CG-299 (garden:CG-299:20260907T074953Z-work:reap)
- 2026-09-07T08:08:30+00:00 opened https://github.com/joshmarcus/context-garden/pull/282 (base main): Closed the six follow-ups: backlog no-JS fallback, wrap-safe diagnostics, test environment isolation, independent self-product approval, bounded environment retries, and confirmed retro_question handling. cost=$0.18
- 2026-09-07T08:14:24+00:00 automated review requested changes: The notification follow-up is covered, but doctor’s `soft_wrap=True` disables Rich wrapping, the no-JS test never submits the form, and three other criteria lack their required regression tests. The PR should not merge until the behavior and evidence match the brief. cost=$1.05
- 2026-09-07T08:14:55+00:00 dispatched revise run 20260907T081454Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~10528 tokens)
- 2026-09-07T08:35:44+00:00 preserved uncommitted worktree changes from run 20260907T081454Z-revise outside the PR: `git stash apply bfd4323e72eaf10d1c121f914ac1b8f545000151` in /home/joshua/work/worktrees/CG-299 (garden:CG-299:20260907T081454Z-revise:reap)
- 2026-09-07T08:37:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/282: Completed the review fixes for doctor wrapping, no-JS backlog submission, environment isolation, self-product approval independence, and bounded environment-error retries. The retro_question notification path was already wired and remains covered. cost=$0.20
- 2026-09-07T08:42:08+00:00 automated review requested changes: Four criteria are met with passing focused tests. The self-product approval rule is not met because the implementation still counts two automated rounds before accepting independent evidence. cost=$0.66
- 2026-09-07T08:42:32+00:00 dispatched revise run 20260907T084230Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~10343 tokens)
- 2026-09-07T08:54:27+00:00 preserved uncommitted worktree changes from run 20260907T084230Z-revise outside the PR: `git stash apply 1185fe44ccd85b6974abbf6d74e2cb92791f6f4d` in /home/joshua/work/worktrees/CG-299 (garden:CG-299:20260907T084230Z-revise:reap)
- 2026-09-07T08:56:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/282: Self-product reviews now require one automated approval plus current-head persona or human evidence; a second same-product automated approval is no longer scheduled by default. Focused tests, lint, and exact-commit CI passed. cost=$0.15
- 2026-09-07T08:59:28+00:00 description rewritten by the reviewer cost=$0.66
- 2026-09-07T09:04:58+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T09:07:27+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T09:13:30+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/282
