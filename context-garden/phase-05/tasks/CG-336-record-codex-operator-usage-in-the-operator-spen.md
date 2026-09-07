---
id: CG-336
title: Record Codex operator usage in the operator spend ledger
status: in_review
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
branch: garden/cg-336-record-codex-operator-usage-in-the-operator-spen
pr: https://github.com/joshmarcus/context-garden/pull/274
attempts: 1
last_dispatched_at: '2026-09-07T07:13:38+00:00'
created: '2026-09-06T13:15:21+00:00'
updated: '2026-09-07T11:55:09+00:00'
---

## Goal

Record Codex operator usage in the operator spend ledger

## Context

Josh handed operation to the Codex desktop task on 2026-09-06. Both tools/operator_spend.py and garden operator-spend record currently parse Claude transcripts. Support actual Codex operator usage so the operator share remains measurable; do not fall back to guessed prices or record Claude usage as Codex. Coordinate or document the garden-local helper migration.

## Acceptance criteria

- [ ] A representative Codex transcript produces correctly attributed usage with no double counting across check-ins. Unknown pricing or unavailable usage is explicitly unavailable, never zero or a Claude fallback. Existing Claude recording continues to work.

## Log

- 2026-09-06T13:15:22+00:00 approved (cli)
- 2026-09-07T06:59:29+00:00 dispatched work run 20260907T065834Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~8900 tokens)
- 2026-09-07T07:12:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/274 (base main): Codex operator transcripts now record cumulative token usage without double counting and preserve unavailable usage or pricing as unavailable. Claude recording remains supported through explicit source selection. cost=$0.91
- 2026-09-07T07:13:24+00:00 automated review requested changes: The Codex parser double-counts reasoning tokens and does not obtain the model from real Codex transcripts, so representative usage is not correctly attributed. The 23 focused tests pass, but their synthetic session metadata does not match the actual transcript schema. cost=$0.31
- 2026-09-07T07:13:38+00:00 dispatched revise run 20260907T071337Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9550 tokens)
- 2026-09-07T07:26:15+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/274: Codex operator records now take model attribution from real turn_context events and avoid double-counting reasoning output. The representative fixture covers the actual schema and cumulative token invariant. cost=$0.72
