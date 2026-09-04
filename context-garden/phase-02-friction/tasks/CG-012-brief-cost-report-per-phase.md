---
id: CG-012
title: Brief cost report per phase
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
estimate: M
difficulty: easy
reading:
- principles/agent-loop.md
- context-garden/phase-01-bootstrap/specs/brief.md
branch: garden/cg-012-brief-cost-report-per-phase
pr: https://github.com/joshmarcus/context-garden/pull/7
attempts: 2
last_dispatched_at: '2026-09-04T16:55:55+00:00'
created: '2026-09-04T00:00:00+00:00'
updated: '2026-09-04T17:02:20+00:00'
---

## Goal

Show, per phase, the fixed brief cost (digest + product + goals) and each task's reading-list cost, so the human can see when context is bloating.

## Context

`garden usage`, the task page and the phase table already show actual tokens and cost per task and per run; `build_brief` returns per-section sizes. Put the estimate next to the actual instead of adding a page: `garden usage` gains a brief-tokens column (fixed part plus reading list), the phase view gets a header line with the fixed-cost estimate, and the phase page's task table gets the same column.

## Acceptance criteria

- [ ] `garden usage product/phase`: task, brief tokens (estimated: fixed + reading), actual input tokens (last run), cost.
- [ ] A phase header line with the fixed-cost estimate, in the CLI and on the phase page.
- [ ] The phase page's task table carries the brief-tokens column.

## Out of scope

- Optimising the briefs automatically.

## Log

- 2026-09-04T16:06:35+00:00 approved
- 2026-09-04T16:38:32+00:00 dispatched work run 20260904T163832Z-work via local [claude model=haiku] (fresh session, base main, ~2636 tokens)
- 2026-09-04T16:43:33+00:00 attempt 1 failed: worker exited 1: worker error: error_max_turns; will retry
- 2026-09-04T16:43:33+00:00 dispatched work run 20260904T164333Z-work via local [claude model=haiku] (fresh session, base main, ~2698 tokens)
- 2026-09-04T16:45:54+00:00 pre-PR checks failed (lint); no PR opened yet; revise run will fix cost=$0.28
- 2026-09-04T16:45:54+00:00 dispatched revise run 20260904T164554Z-revise via local [claude model=haiku] (fresh session, base main, ~3106 tokens)
- 2026-09-04T16:48:17+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/7 (base main): Addressed lint error by fixing import sorting. All acceptance criteria met: brief tokens now show in CLI usage command, phase page displays fixed cost header and brief-tokens column in task table. cost=$0.17
- 2026-09-04T16:50:22+00:00 automated review: approve — All acceptance criteria met. Cost breakdown correctly partitions brief sections, CLI and web UI display estimated tokens per task and phase, and tests validate the new properties. No bugs or scope creep. cost=$0.07
- 2026-09-04T16:50:39+00:00 triage: changes requested by hand: The phase page header still shows the whole first task brief, not the fixed part. In web/app.py the template gets fixed_
- 2026-09-04T16:51:26+00:00 dispatched revise run 20260904T165125Z-revise via local [claude model=haiku] (fresh session, base main, ~3197 tokens)
- 2026-09-04T16:53:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/7: Fixed the phase header to use fixed_tokens instead of total tokens, ensuring consistency between the header display and task table rows. Updated PR body with review responses and a friction note about task clarity. cost=$0.18
- 2026-09-04T16:53:50+00:00 marked ready for review on GitHub; triage done
- 2026-09-04T16:55:54+00:00 automated review requested changes: All acceptance criteria met, code is correct. PR description has scar tissue: remove the "Review responses" section, which references the revision process. cost=$0.07
- 2026-09-04T16:55:55+00:00 dispatched revise run 20260904T165554Z-revise via local [claude model=haiku] (fresh session, base main, ~3432 tokens)
- 2026-09-04T16:58:16+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/7: Removed scar tissue from PR description by eliminating the 'Review responses' section. The PR now reads as if the feature was implemented correctly from the start, while preserving the 'Friction' section. All acceptance criteria remain met, tests pass, lint passes. cost=$0.10
- 2026-09-04T16:58:16+00:00 stalled: revise run 20260904T165554Z-revise produced no change to the diff; needs a human (garden retry to resume)
- 2026-09-04T17:02:20+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/7
