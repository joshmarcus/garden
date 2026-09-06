---
id: CG-337
title: Attention cards ask for product decisions, while no-change reports reconcile automatically
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 0
difficulty: hard
reading: []
branch: garden/cg-337-attention-cards-ask-for-product-decisions-while
pr: https://github.com/joshmarcus/context-garden/pull/235
attempts: 1
last_dispatched_at: '2026-09-06T20:11:48+00:00'
created: '2026-09-06T13:20:33+00:00'
updated: '2026-09-06T20:11:48+00:00'
---

## Goal

People can understand what decision they are making and its consequences. A worker reporting no_change ordinarily goes through evidence reconciliation, checks and review without asking the person to accept or reject internal scheduler terminology.

## Context

Josh, 2026-09-06 operator session: "those decisions are confusing; it's unclear how I should be responding. e.g. for no_change ... it seems like we should handle that differently". CG-324 displayed "no question recorded" while a check was already running. CG-328 covers the existing accept-path bug; build on that fix rather than duplicating it. Absence of GitHub comments alone does not establish that internal automated findings are resolved.

## Acceptance criteria

- [ ] A no_change report is reconciled against current-head evidence, outstanding internal and external findings, and required checks. Satisfied work continues through review; unresolved actionable findings return to the worker without a routine human decision. Preserve bounded retries and surface genuine unresolved ambiguity.
- [ ] Proposed cancellation or changed outcomes are presented as explicit product decisions: what changes, why, recommendation and consequences of each response. Labels describe those outcomes rather than accept/reject of a machine status.
- [ ] A missing question or inconsistent running-check state is diagnosed and recovered as an operational issue; it never asks the person to answer an absent question.
- [ ] Tests cover satisfied no-change, ignored internal findings, real scope disagreement and the CG-324 empty-card case. Provide representative rendered cards or captures showing that the decision can be understood without knowing scheduler internals.

## Log

- 2026-09-06T13:20:34+00:00 approved (cli)

Additional takeover evidence: setting CG-324 in_review while its pre-PR check was live exposed a misleading Review and merge card with `garden set-status CG-324 done`. Reconciliation to running removed that false decision. CG-308 displayed a running rebase from 12:56Z despite the rebased branch having green CI and no live run; a fresh review required operator recovery. Derive attention from live run/continuation state, and never recommend marking done as a substitute for verifying checks/review/merge. Coordinate with CG-316 and CG-333 on stale run recovery.
- 2026-09-06T13:46:58+00:00 priority 1 -> 0
- 2026-09-06T17:41:58+00:00 reordered in context-garden/phase-05 (order 3 -> 0) (web)
- 2026-09-06T17:42:43+00:00 dispatched work run 20260906T174219Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~8786 tokens)
- 2026-09-06T18:18:59+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$3.85
- 2026-09-06T19:14:18+00:00 dispatched revise run 20260906T191417Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~9678 tokens)
- 2026-09-06T19:21:53+00:00 opened https://github.com/joshmarcus/context-garden/pull/235 (base main): Updated the discovered-decision test to require outcome-oriented labels, restoring the full pre-PR suite. No-change reconciliation, explicit product decisions, and empty-card recovery remain covered by the completed implementation. cost=$0.41
- 2026-09-06T19:25:42+00:00 automated review requested changes: The no-change and empty-card recovery paths can discard scheduler evidence or cancel live work instead of reconciling it. Required rendered-card evidence is also absent, and an unrelated generated snapshot rewrite remains in the branch. cost=$0.48
- 2026-09-06T19:34:26+00:00 dispatched revise run 20260906T193424Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10009 tokens)
- 2026-09-06T19:47:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/235: No-change reconciliation now preserves internal finding identities and reaches the bounded stall path when findings persist. Empty-question cards use dedicated recovery that retains live checks, reaps finished checks, and clears only stale metadata; representative decision cards were captured and inspected across widths and themes. cost=$1.84
- 2026-09-06T19:55:10+00:00 stalled: review finding repeated after a revise round: ui captures not read for: board, board-list, config, events, herbarium, inbox, n; run `garden triage CG-337 --changes "<feedback>" to unblock`
- 2026-09-06T20:11:34+00:00 nothing to fix; resumed to in review by hand
- 2026-09-06T20:11:45+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/checkruns.py); a rebase agent will resolve it
- 2026-09-06T20:11:48+00:00 dispatched rebase run 20260906T201146Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8517 tokens)
