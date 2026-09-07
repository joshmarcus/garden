---
id: CG-300
title: The retro's Numbers section reads the operator ledger where the owner keeps it, and reports spend
  and share
status: in_review
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
branch: garden/cg-300-the-retro-s-numbers-section-reads-the-operator-l
pr: https://github.com/joshmarcus/context-garden/pull/269
discovered_from: retro-editor:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-07T09:03:31+00:00'
created: '2026-09-06T00:00:00+00:00'
updated: '2026-09-07T11:50:52+00:00'
completion_track: walkthrough-costs
---

## Goal

The retro document's Numbers section finds the operator ledger at the product's docs directory (context-garden/docs/operator-spend.jsonl, or a config key naming the path) and prints the operator's spend, turns and share of total, so the definition-of-done line on operator share can be read from the retro.

## Context

Both phase-04 reconcile runs printed operator: $0.00, 0% of total, because the section reads <garden root>/docs/operator-spend.jsonl while the ledger the owner chose lives under context-garden/docs/. The operator retro had the real figures ($195 of $669, 29%). Raised by the retro-editor persona, 2026-09-05.

## Acceptance criteria

- [ ] The ledger path defaults to <product>/docs/operator-spend.jsonl and can be set by a config key; tools/operator_spend.py and the retro agree on it
- [ ] The Numbers section shows operator spend, turns and share when the ledger exists, and says the ledger was not found otherwise
- [ ] A retro test with a ledger at the configured path renders the figures

## Log

- 2026-09-06T00:24:05+00:00 approved (cli)
- 2026-09-06T13:13:15+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:32+00:00 reset to ready by hand
- 2026-09-07T06:19:03+00:00 dispatched work run 20260907T061843Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~11191 tokens)
- 2026-09-07T06:31:19+00:00 opened https://github.com/joshmarcus/context-garden/pull/269 (base main): Retro Numbers now uses the shared configurable operator ledger path and reports spend, turns, share, or a missing-ledger message. cost=$0.13
- 2026-09-07T06:34:22+00:00 automated review requested changes: The configured-path behavior works and focused tests pass, but the default remains rooted at the garden rather than the product, reproducing the task's original failure. Reported turns are also all-time while spend and share are phase-scoped. cost=$0.84
- 2026-09-07T06:34:54+00:00 dispatched revise run 20260907T063454Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12213 tokens)
- 2026-09-07T06:52:56+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/269: Retro Numbers now reads the product-relative or configured operator ledger, reports phase-windowed spend and turns, and Now 2 invalidates on configured ledger changes. Focused tests and CI pass. cost=$0.10
- 2026-09-07T06:57:50+00:00 automated review produced no verdict ({'message': 'Selected model is at capacity. Please try a different model.'})
- 2026-09-07T08:29:16+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_retro.py); a rebase agent will resolve it
- 2026-09-07T08:29:28+00:00 dispatched rebase run 20260907T082927Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~13050 tokens)
- 2026-09-07T08:32:24+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/269: Rebased CG-300 onto origin/main and resolved the tests/test_retro.py conflict while preserving both sides. cost=$0.01
- 2026-09-07T08:47:42+00:00 automated review requested changes: The ledger resolution and retro reporting behavior are correct and well tested. Re-run CI for current HEAD after the rebase and update the PR description with that exact commit and run. cost=$0.88
- 2026-09-07T08:48:09+00:00 dispatched revise run 20260907T084808Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12585 tokens)
- 2026-09-07T08:57:54+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/269: Retro Numbers now resolves the operator ledger from the product docs directory by default or a configured path, and reports spend, phase-windowed turns, share, or a missing-ledger message. Exact-commit CI passed. cost=$0.03
- 2026-09-07T09:03:00+00:00 automated review requested changes: Retro rendering and configured-ledger tests pass, but the shared default resolver still returns <garden>/docs when callers provide only root and config, so several Costs/Now surfaces continue reading a different ledger. cost=$0.73
- 2026-09-07T09:03:31+00:00 dispatched revise run 20260907T090331Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~12777 tokens)
- 2026-09-07T09:14:56+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/269: Operator spend now consistently resolves to the tool-owning product's docs ledger by default, with configured paths still supported. Retro, Costs, Now, and the operator CLI share this behavior. cost=$0.08
- 2026-09-07T09:14:57+00:00 4 automated review round(s) used; this PR is yours — run `garden review CG-300` for one more round, or review on GitHub
- 2026-09-07T09:35:02+00:00 triage: marked ready for review

## Completion track

Reliable walkthrough and cost reporting (`walkthrough-costs`), grouped by owner request. Members: CG-253, CG-297, CG-300, CG-336.

Integrate renderer correctness and Codex usage capture before final walkthrough/retro reporting integration. Validate a representative walkthrough plus one matched time-window cost calculation across ledger, retro and displayed metrics; retain unavailable-price labels.

This is shared integration guidance, not additional implementation scope or a replacement for this task’s acceptance criteria. Preserve existing work and current-run criteria; the operator owns combined validation. Garden plan: context-garden/phase-05/completion-tracks.md.
