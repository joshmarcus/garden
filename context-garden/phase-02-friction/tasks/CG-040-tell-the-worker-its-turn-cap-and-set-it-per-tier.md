---
id: CG-040
title: Tell the worker its turn cap, and set it per tier
status: changes_requested
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/harness.py
- src/garden/brief.py
- src/garden/config.py
branch: garden/cg-040-tell-the-worker-its-turn-cap-and-set-it-per-tier
pr: https://github.com/joshmarcus/context-garden/pull/20
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T17:32:35+00:00'
created: '2026-09-04T17:03:10+00:00'
updated: '2026-09-04T18:35:27+00:00'
---

## Goal

Workers know how many turns they have, and the cap fits the model.

## Context

CG-012's first attempt on haiku used all 60 turns exploring and exited with `error_max_turns` and no final message, after making three good commits; the second attempt finished the same work in 29 turns. `max_turns` is one number for every tier in `harnesses.claude`. Put the cap in the brief's rules ("you have N turns; commit early and report before you run out") and allow `max_turns` per tier next to `models`.

## Acceptance criteria

- [ ] the brief states the turn cap.
- [ ] `harnesses.<name>.max_turns` accepts a map by tier as well as a number.
- [ ] a test for the brief text and the config shape.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:10+00:00 discovered by CG-027
- 2026-09-04T17:23:54+00:00 approved (web)
- 2026-09-04T17:32:35+00:00 dispatched work run 20260904T173235Z-work via local [claude model=haiku] (fresh session, base main, ~8291 tokens)
- 2026-09-04T17:38:04+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/20 (base main): Workers now know their turn cap. The brief includes a rule stating turns available, and max_turns can be configured per tier. All tests pass. cost=$0.61
- 2026-09-04T17:40:27+00:00 automated review requested changes: All acceptance criteria met, 122 tests pass, lint clean. PR description is missing the motivation — the CG-012 haiku exhaustion incident that makes this change necessary — which a reader without the task file needs. cost=$0.34
- 2026-09-04T18:35:27+00:00 triage: changes requested by hand: Codex review on PR #20, dropped at the time. (P2) src/garden/brief.py:131: the brief reads the product harness but dispa
