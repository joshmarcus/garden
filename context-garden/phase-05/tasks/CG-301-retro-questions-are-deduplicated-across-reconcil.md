---
id: CG-301
title: Retro questions are deduplicated across reconcile runs, and a second judge can run with task filing
  off
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/operator_spend.py
- tests/test_retro.py
branch: garden/cg-301-retro-questions-are-deduplicated-across-reconcil
pr: https://github.com/joshmarcus/context-garden/pull/270
discovered_from: retro-editor:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-07T06:43:31+00:00'
created: '2026-09-06T00:00:00+00:00'
updated: '2026-09-07T08:14:43+00:00'
---

## Goal

Two reconcile runs of the same phase do not ask the owner the same question twice or file the same follow-ups twice: questions are matched by normalised text before decision cards are created, and garden retro takes --no-file (or a judge-only mode) so a comparison judge writes its document without filing drafts or blocking tasks.

## Context

The phase-04 retro ran twice (fable, then astra with --skip-personas). Each asked the same six questions in different words, so the owner answered each twice and phase-05/goals.md carries every decision twice; each also filed the same 31 persona findings and its own blocking set from one live id counter (CG-244 covers the ids). Raised by the retro-editor persona, 2026-09-05.

## Acceptance criteria

- [ ] A second reconcile run on the same phase files no question card whose normalised text matches an open or answered card from the first run; the answer is copied onto the retro record instead
- [ ] garden retro --no-file writes retro.md and the goals draft and opens the PR without filing features, follow-ups, blocking tasks or persona-finding drafts, and says so in the document header
- [ ] Tests: two runs with paraphrased questions yield one card each; --no-file leaves the task tree untouched

## Log

- 2026-09-06T00:24:05+00:00 approved (cli)
- 2026-09-06T13:13:16+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:33+00:00 reset to ready by hand
- 2026-09-07T06:27:27+00:00 dispatched work run 20260907T062708Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~11249 tokens)
- 2026-09-07T06:40:31+00:00 opened https://github.com/joshmarcus/context-garden/pull/270 (base main): Retro questions now deduplicate across runs, including answered questions, and `garden retro --no-file` creates judge-only retro PRs without task filing or phase mutation. cost=$0.17
- 2026-09-07T06:43:12+00:00 automated review requested changes: The intended same-phase flows are implemented and the focused retro suite passes, but retro-question deduplication currently crosses phase boundaries and can suppress legitimate questions in later phases. cost=$0.32
- 2026-09-07T06:43:31+00:00 dispatched revise run 20260907T064329Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~11779 tokens)
- 2026-09-07T06:51:38+00:00 preserved uncommitted worktree changes from run 20260907T064329Z-revise outside the PR: `git stash apply e05313c3113f1fe68b2fe9b3e9356513bf549412` in /home/joshua/work/worktrees/CG-301 (garden:CG-301:20260907T064329Z-revise:reap)
- 2026-09-07T06:53:00+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/270: Scoped retro question deduplication to the current phase and added a regression test covering answered questions across phases. cost=$0.06
- 2026-09-07T08:05:34+00:00 description rewritten by the reviewer cost=$0.43
- 2026-09-07T08:06:05+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T08:07:08+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T08:14:43+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/270
