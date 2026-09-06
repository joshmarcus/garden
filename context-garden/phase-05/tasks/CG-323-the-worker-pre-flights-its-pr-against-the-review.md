---
id: CG-323
title: The worker pre-flights its PR against the review rubric, mechanical review items become pre-PR
  checks, and criteria are frozen at dispatch
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/brief.py
- src/garden/review.py
- src/garden/checks.py
- src/garden/checkrun.py
- src/garden/scheduler/review.py
- src/garden/scheduler/dispatch.py
- docs/worker-protocol.md
- tests/test_brief.py
- tests/test_review.py
branch: garden/cg-323-the-worker-pre-flights-its-pr-against-the-review
attempts: 1
last_dispatched_at: '2026-09-06T10:36:05+00:00'
created: '2026-09-06T03:59:37+00:00'
updated: '2026-09-06T11:26:56+00:00'
---

## Goal

A PR arrives at its first review already checked against what the reviewer will look for. The work and revise briefs end with the review rubric as a pre-flight the worker walks before writing its result: a test per criterion (or a stated reason there is none), lint clean, no conflict markers, captures at both widths for any UI change, a description in goal-and-outcome form with no history, the criteria addressed by name; the result block carries the pre-flight as a checklist with a line per item. Items a machine can judge (conflict markers, syntax, a UI diff with no captures, a missing description) become pre-PR checks that fail before any reviewer spends a round. The criteria a worker sees are frozen at dispatch: a change to the task file after dispatch reaches the worker as a revise note on the next round, and the reviewer judges the brief the worker had.

## Context

Owner, 2026-09-06 04:05Z: 'How can we reduce the number of review rounds?' Of 85 send-backs so far, 54 were on PRs whose criteria were all met, for the same recurring findings (no test for a criterion, conflict markers, narrative descriptions, unsandboxed HTML, no captures); several more came from criteria added or corrected after dispatch (the Now tasks, CG-212). Sol, reviewing one rung above the writer since 03:20Z, has sent back 11 of 11 PRs on such findings. The reviewer's rubric is in src/garden/review.py; the worker never sees it.

## Acceptance criteria

- [ ] The work and revise briefs include the review rubric as a pre-flight section and the GARDEN_RESULT block carries a pre_flight list with one entry per item and a status; a result missing the list is a mechanical changes_requested naming the missing items
- [ ] Pre-PR checks fail on conflict markers, a syntax error, a UI diff (templates, static, web pages) with no captures under the run, and an empty PR description, each with a one-line reason the revise brief carries
- [ ] The brief records the criteria text it was built from; a task-file change after dispatch is delivered as a revise note and the review brief shows the criteria the worker had, with the delta marked
- [ ] Tests: the pre-flight section renders; each mechanical check fails on its shape and passes on a clean diff; a criteria change after dispatch shows up as a note in the next revise brief
- [ ] Measured after a week in the retro: send-backs on findings-only PRs per merged task, before and after (the number this task exists to move)

- [ ] The work and revise briefs state that the run ends when the worker stops: long commands run in the foreground, nothing is backgrounded to await a notification, and the result is written only after the checks have returned (five Fable runs on 2026-09-06 ended 'waiting for the monitor' with their work committed and no result).

## Log
- 2026-09-06T03:59:39+00:00 approved (cli)
- 2026-09-06T05:25:22+00:00 dispatched work run 20260906T052256Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~28859 tokens)
- 2026-09-06T06:42:21+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 508a28c4fe30, not because of this branch; waiting for the base to go green, no revise round cost=$1.36
- 2026-09-06T07:18:11+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T08:57:54+00:00 dispatched revise run 20260906T085752Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~29428 tokens)
- 2026-09-06T09:49:41+00:00 pre-PR checks failed (test) (still failing after a rebase onto `main`); no PR opened yet; revise run will fix cost=$2.39
- 2026-09-06T10:36:05+00:00 dispatched revise run 20260906T103604Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9055 tokens)
- 2026-09-06T11:00:31+00:00 base branch `main` is itself broken — pre-PR check(s) test fail at its own commit 56af81dfcba5, not because of this branch; waiting for the base to go green, no revise round cost=$0.81
- 2026-09-06T11:26:56+00:00 re-enabled by hand; revise run will follow
