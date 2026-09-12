---
id: CG-536
title: Make accepted-task costs and phase comparisons trustworthy
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/costs.py
- src/garden/now1.py
- src/garden/web/pages/costs.py
- src/garden/cli/costs.py
- src/garden/retro.py
- src/garden/operator_spend.py
branch: garden/cg-536-make-accepted-task-costs-and-phase-comparisons-t
pr: https://github.com/joshmarcus/context-garden/pull/446
runner: remote
discovered_from: retro:context-garden/phase-05
freeze_exception: true
freeze_exception_reason: Misleading filters and unknown costs shown as definitive values invalidate the
  phase's central cost-per-accepted-task and comparison outcomes.
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T16:37:58+00:00'
created: '2026-09-10T13:10:36+00:00'
updated: '2026-09-10T17:09:02+00:00'
---

## Goal

Use one explicit acceptance and cost-cohort contract across Costs, Now, CLI and retro. Honor selected product, phase, time, model, tier and harness semantics; distinguish accepted work from forced status completion. Preserve unknown prices and consistently scope operator and worker spending. Reuse CG-251/300/336/351 calculations where sound, and coordinate CG-530 presentation without duplicating it.

## Context

Filed by the context-garden/phase-05 retro `reopen` verdict: it must land before the phase can close. Reason: Misleading filters and unknown costs shown as definitive values invalidate the phase's central cost-per-accepted-task and comparison outcomes.

## Acceptance criteria

- [ ] The same selected cohort produces consistent accepted counts and cost results across Costs, Now, CLI and retro, with documented completion-window and run-cost inclusion semantics.
- [ ] Unknown prices remain partial or unavailable, with priced/unpriced counts; an unpriced accepted task never becomes a definitive zero-dollar task or complete average.
- [ ] Forced completion without acceptance provenance does not inflate accepted-task outcomes, while genuine owner acceptance is represented according to an explicit shared rule.
- [ ] Adding unrelated-phase worker or operator spending cannot change the Phase05 result; unattributed spending is shown separately rather than silently assigned.
- [ ] Focused regressions cover mixed routing, window boundaries, missing prices and forced completion; the corrected Phase05 account reports its actual denominators and uncertainties without fabricating historical data.

## Log

- 2026-09-10T13:10:36+00:00 filed by the context-garden/phase-05 retro reopen verdict (blocking)
- 2026-09-10T13:16:43+00:00 approved by the retro reopen verdict
- 2026-09-10T14:21:18+00:00 dispatched work run 20260910T142117Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22154 tokens)
- 2026-09-10T14:38:51+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:40:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/446 (base main): Implemented a shared accepted-task cohort across Costs, Now, CLI metrics and retros, with completion-window semantics, full pre-acceptance run costs, explicit price completeness, forced-completion exclusion and scoped operator spending. Committed as 2532823b; 94 focused tests and repository-wide Ruff lint passed. cost=$3.28
- 2026-09-10T14:45:13+00:00 automated review requested changes: The shared cohort and unknown-price handling are sound on Costs/CLI/retro, but Now still allows unrelated-phase activity to change the selected phase’s results. cost=$0.52
- 2026-09-10T14:45:40+00:00 dispatched revise run 20260910T144539Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23323 tokens)
- 2026-09-10T14:54:01+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:55:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/446: Scoped Now period accounting to the selected primary-phase cohort and separated unattributed operator spend from phase totals. Verified the current head with 69 focused tests and repository-wide Ruff lint. cost=$1.28
- 2026-09-10T14:57:47+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: adding unrelated-phase worker or opera; run `garden triage CG-536 --changes "<feedback>" to unblock`
- 2026-09-10T15:00:15+00:00 triage: changes requested by hand: Keep the shared acceptance cohort and unknown-price accounting already validated. Fix cumulative operator ledger attribu
- 2026-09-10T15:00:37+00:00 dispatched revise run 20260910T150037Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24136 tokens)
- 2026-09-10T15:08:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:09:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/446: Retro operator accounting now preserves cumulative session baselines before cohort filtering, so Phase05 receives only its actual increments and unattributed spend remains separate. Verified the four-file focused suite exited successfully, the targeted operator-spend suite passed 18 tests, and repository-wide Ruff lint passed. cost=$1.27
- 2026-09-10T15:12:02+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: adding unrelated-phase worker or opera; run `garden triage CG-536 --changes "<feedback>" to unblock`
- 2026-09-10T15:16:22+00:00 triage: changes requested by hand: Preserve the now-correct cumulative-ledger delta conversion and shared acceptance cohort. Normalize supported operator p
- 2026-09-10T15:18:15+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T15:18:36+00:00 dispatched revise run 20260910T151836Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24272 tokens)
- 2026-09-10T15:27:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:28:52+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/446: Canonicalized operator phase attribution across Costs, CLI metrics, Now and retro, preserving product identity for short phase names. Committed as cd97a38e; 123 focused tests passed, the final targeted suite passed 28 tests, and repository-wide Ruff passed. cost=$1.67
- 2026-09-10T15:31:37+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: the same selected cohort produces cons; run `garden triage CG-536 --changes "<feedback>" to unblock`
- 2026-09-10T15:37:15+00:00 triage: changes requested by hand: Retain the fixed delta-before-filter logic and product-aware phase attribution. Preserve unpriced operator deltas throug
- 2026-09-10T15:48:23+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T15:49:26+00:00 dispatched revise run 20260910T154926Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24922 tokens)
- 2026-09-10T16:04:52+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:06:16+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/446: Preserved priced-zero and unpriced operator deltas across Costs, Now, CLI metrics and retro reporting, with explicit completeness counts and partial totals. Canonicalized the Costs page phase selector so accepted summaries and outcome tables share the same product/phase cohort; exact head 4b4291d1 passed 125 focused tests and repository-wide Ruff lint. cost=$2.52
- 2026-09-10T16:10:31+00:00 automated review requested changes: The main cohort logic is sound, but two operator-spend edge cases remain incorrect. cost=$0.58
- 2026-09-10T16:31:21+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T16:37:26+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T16:37:58+00:00 dispatched revise run 20260910T163758Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24940 tokens)
- 2026-09-10T16:55:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:56:55+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/446: Corrected operator cost handling so unknown prices no longer crash total aggregation, and product-only or phase-only operator records remain explicitly unattributed across Costs, Now, metrics and retro. Restored legacy closed-phase task-status counts without weakening the provenance-backed accepted-task cohort; committed as 52d581bd94ac81a64435ae5a14ec749aa4a7e398. cost=$2.42
- 2026-09-10T16:59:53+00:00 automated review: approve — The shared acceptance cohort and operator-spend accounting now satisfy the requested cross-surface contract. Unknown prices and incomplete attribution remain explicit without contaminating selected phase totals. cost=$0.82
- 2026-09-10T17:07:40+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T17:09:02+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/446
