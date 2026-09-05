---
id: CG-233
title: Every codex run records its model and a cost computed from its usage and a per-model price table,
  so cost per accepted task compares across harnesses
status: done
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/harness.py
- src/garden/runner/local.py
- src/garden/runs.py
- src/garden/events.py
- src/garden/config.py
- context-garden/phase-05/specs/cost-aware-model-routing.md
branch: garden/cg-233-every-codex-run-records-its-model-and-a-cost-com
pr: https://github.com/joshmarcus/context-garden/pull/188
attempts: 1
last_dispatched_at: '2026-09-05T20:30:45+00:00'
created: '2026-09-05T20:29:25+00:00'
updated: '2026-09-05T21:13:56+00:00'
---

## Goal

A codex run is accounted like a claude run. The run record carries the model that actually ran (from the resolved tier map or the `-m` override, confirmed against the CLI's own output when it reports one) and a `cost_usd` computed from the run's usage (`input_tokens`, `cached_input_tokens`, `cache_write_input_tokens`, `output_tokens`, `reasoning_output_tokens` from codex's `turn.completed` events) and a per-model price table in garden.yaml, with the same fields as claude's usage so `garden costs`, `garden metrics`, trials and the retro compare harnesses on one basis. The price table has defaults for the models the garden names and is editable, since list prices change.

## Context

The user on 2026-09-05, after the CG-225 trials: "let's be sure to apply the above methodology to assigning cost for all codex tasks." The methodology: cost = uncached input × input price + cached input × cached price (10% of input for OpenAI) + cache writes × write price + output × output price, at list prices, even though both accounts bill by subscription, because list price is the common measure of quota consumed. Today codex runs record `cost_usd: null` and `model: ""`; the operator computed the two trial runs by hand (astra: about $3.77; terra: about $1.01, against claude sonnet 5 at $4.41 and $5.03). Prices at the time: gpt-6-astra $10 / $50 (cached $1, cache write $12.50; a long-context tier above 272K tokens per request at $20 / $75); gpt-5.6-sol $4 / $20 (promotional); gpt-5.6-terra $2 / $12; gpt-5.6-luna $0.20 / $1.20; cached input at 10% of the input price.

## Acceptance criteria

- [ ] `harnesses.codex.prices` (and a generic `prices` map any harness can use) holds per-model input, cached-input, cache-write and output prices per million tokens, with the defaults above; the docs say where the numbers came from and that they need updating.
- [ ] The codex harness parser reads the last `turn.completed` usage, stores it on the run in the same shape as claude's (`input_tokens`, `cache_read_input_tokens`, `cache_creation_input_tokens`, `output_tokens`), stores the model, and computes `cost_usd`; a run whose model has no price records the usage and `cost_usd: null` with a log line naming the missing price.
- [ ] `run_finished` events and the costs page carry the cost; `garden metrics` and the trial comparison show cost per contender; the retro's numbers include codex runs.
- [ ] A one-off `garden costs --backfill` recomputes `cost_usd` for existing codex runs from their stored transcripts, so today's runs enter the record.
- [ ] Tests with the fake codex for a run on each priced model and one on an unpriced model.

## Log

- 2026-09-05T20:29:25+00:00 approved (web)
- 2026-09-05T20:30:45+00:00 dispatched work run 20260905T203030Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~26792 tokens)
- 2026-09-05T21:01:30+00:00 opened https://github.com/joshmarcus/context-garden/pull/188 (base main): Codex runs now record a confirmed model and a cost_usd computed from turn.completed usage against a per-model price table (harnesses.codex.prices, plus a generic prices: map), with a --backfill command to recompute cost_usd for existing codex runs from their stored transcripts. cost=$6.04
- 2026-09-05T21:07:29+00:00 automated review: approve — Codex runs now record a confirmed model and cost_usd from a per-model price table with backfill support; all criteria are met, full test suite and lint pass, and the diff is well-scoped. cost=$0.72
- 2026-09-05T21:07:38+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T21:10:39+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-05T21:13:56+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/188
