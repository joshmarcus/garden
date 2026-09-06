---
id: CG-237
title: 'The not-logged-in check reads a worker''s prose as an auth failure: match the CLI''s own error,
  not the report text'
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/harness.py
- tests/test_harness.py
branch: garden/cg-237-the-not-logged-in-check-reads-a-worker-s-prose-a
pr: https://github.com/joshmarcus/context-garden/pull/207
attempts: 1
last_dispatched_at: '2026-09-06T03:15:11+00:00'
created: '2026-09-05T22:48:41+00:00'
updated: '2026-09-06T03:15:11+00:00'
---

## Goal

A worker whose report talks about a login outage is a finished run, not a login failure. The harness's auth check reads only what the CLI itself emits (stderr, the error text, or a short output with no result block), so a long report that contains the words "not logged in" is reaped as done and its cost, findings and verdict are kept.

## Context

2026-09-05 22:40Z: four of the seven phase-04 persona reviews on fable ($22 in all) were classified `env_error: auth` because their prose discussed the day's "Not logged in" worker outage (CG-217). The harness was paused ("auth limit hit on claude"), the reports were discarded, and the retro stalled at the persona stage; the reconcile run's own document would have tripped the same check. The operator restored the reports from the run output by hand and shipped the check narrowing in a hand-merged PR. This task keeps that narrowing honest: a test per shape (stderr message, is_error result, long report, GARDEN_RESULT in a short text) and the same rule for codex's `{"type": "error"}` line.

## Acceptance criteria

- [ ] `Harness.parse` flags `env_kind: auth` only when an AUTH_FAILURE_MARKER appears in stderr, in the error text, or in an output under 2000 characters that carries no GARDEN_* block; a long report or any parsed result block is never an auth failure.
- [ ] The same rule holds for codex output: an `error` event with the marker is auth; an agent message that mentions it is not.
- [ ] `garden doctor` and the login probe still report a real logged-out harness.
- [ ] Tests for each shape; the four discarded phase-04 persona runs' stdout, replayed through parse, come back `done` with their cost.

## Log

- 2026-09-06T00:50:16+00:00 approved (cli)
- 2026-09-06T02:29:02+00:00 dispatched work run 20260906T022845Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~11411 tokens)
- 2026-09-06T02:38:15+00:00 opened https://github.com/joshmarcus/context-garden/pull/207 (base main): Narrowed auth detection to CLI error/stderr output and protected worker prose, garden blocks, and Codex agent messages from false auth failures. cost=$0.05
- 2026-09-06T02:40:21+00:00 automated review requested changes: The auth guard still misclassifies an error result containing a parsed GARDEN_RESULT block, and the required replay of the four discarded persona outputs is absent. The branch also includes substantial unrelated work. cost=$0.15
- 2026-09-06T02:43:31+00:00 dispatched revise run 20260906T024331Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12143 tokens)
- 2026-09-06T02:57:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/207: Auth detection now ignores markers in parsed worker results and Codex agent messages while preserving real CLI login failures. Added four persona replay cases that retain done status and cost. cost=$0.05
- 2026-09-06T02:59:59+00:00 automated review requested changes: Codex agent-message detection can suppress a later genuine Codex auth error, and the required persona-output replays are synthetic rather than the four discarded stdout artifacts. cost=$0.07
- 2026-09-06T03:00:53+00:00 dispatched revise run 20260906T030052Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12473 tokens)
- 2026-09-06T03:10:08+00:00 worker asks: Please provide the four discarded persona stdout artifacts so I can add exact replay fixtures. cost=$0.05
- 2026-09-06T03:15:10+00:00 kept 1 local-only commit(s) on `backup/20260906T031510Z-resume` before syncing to origin/garden/cg-237-the-not-logged-in-check-reads-a-worker-s-prose-a's head: da020b9 Fix Codex auth error precedence
- 2026-09-06T03:15:11+00:00 dispatched resume run 20260906T031510Z-resume via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12588 tokens)
