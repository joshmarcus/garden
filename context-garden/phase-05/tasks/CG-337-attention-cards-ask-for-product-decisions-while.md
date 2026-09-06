---
id: CG-337
title: Attention cards ask for product decisions, while no-change reports reconcile automatically
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading: []
created: '2026-09-06T13:20:33+00:00'
updated: '2026-09-06T13:20:34+00:00'
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
