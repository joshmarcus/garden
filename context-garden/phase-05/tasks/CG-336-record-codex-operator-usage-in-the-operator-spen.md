---
id: CG-336
title: Record Codex operator usage in the operator spend ledger
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-06T13:15:21+00:00'
updated: '2026-09-06T13:15:22+00:00'
---

## Goal

Record Codex operator usage in the operator spend ledger

## Context

Josh handed operation to the Codex desktop task on 2026-09-06. Both tools/operator_spend.py and garden operator-spend record currently parse Claude transcripts. Support actual Codex operator usage so the operator share remains measurable; do not fall back to guessed prices or record Claude usage as Codex. Coordinate or document the garden-local helper migration.

## Acceptance criteria

- [ ] A representative Codex transcript produces correctly attributed usage with no double counting across check-ins. Unknown pricing or unavailable usage is explicitly unavailable, never zero or a Claude fallback. Existing Claude recording continues to work.

## Log

- 2026-09-06T13:15:22+00:00 approved (cli)
