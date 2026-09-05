---
id: CG-237
title: 'The not-logged-in check reads a worker''s prose as an auth failure: match the CLI''s own error,
  not the report text'
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/harness.py
- tests/test_harness.py
created: '2026-09-05T22:48:41+00:00'
updated: '2026-09-05T22:48:41+00:00'
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

