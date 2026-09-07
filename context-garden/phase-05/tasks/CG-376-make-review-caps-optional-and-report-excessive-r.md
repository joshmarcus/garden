---
id: CG-376
title: Make review caps optional and report excessive review loops as friction
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/config.py
- src/garden/scheduler/review.py
- src/garden/scheduler/human.py
- src/garden/now1.py
- src/garden/web/pages/config.py
created: '2026-09-07T09:29:27+00:00'
updated: '2026-09-07T09:30:03+00:00'
---

## Goal

Let an operator disable the hard automated-review round cap while retaining a separate observable threshold for excessive loops. Owner requested optional review caps on2026-09-07; configure this garden for no hard review cap once supported and deployed. Concurrency remains reviewer3/shared5.

## Context

CG300/323 stopped at four reviews despite concrete actionable findings. CG297 repeatedly mishandled child CSS combinators; CG339 repaired evidence placeholders but retained label-only recovery validation. CG358 had all functional criteria accepted but was blocked by a blanket missing-capture finding. CG365 reached approval after four reviews with only stale description evidence to rewrite. These are different causes and should not be collapsed into an unexplained owner card. CG374 owns broader routine recovery classification; CG372 review admission fairness; CG323 worker preflight; CG339 proportional real-application review evidence.

## Acceptance criteria

- [ ] Support an explicit unlimited/null review.max_rounds setting and positive finite limits. Preserve existing finite configurations and document default/migration semantics; no int(None), sentinel huge integer, or zero ambiguity across scheduler/human recovery/config/CLI/Now.
- [ ] Config UI offers a clear optional hard cap with help text distinguishing total rounds, concurrency, and friction threshold. Unlimited cap never disables reviews, exact-head evidence, security checks, merge gates, resource admission or explicit owner holds.
- [ ] A separate configurable soft threshold emits one deduplicated friction record per task/loop episode, with round count, cumulative work/revise/review cost, head lineage and actionable evidence. It does not require owner action solely because the threshold was crossed.
- [ ] Classify evidenced loop causes: repeated unaddressed finding, newly discovered defect, mechanical rebase/head change, stale/missing infrastructure evidence, description-only correction, and lost feedback/state transition. Preserve unknowns; link existing prevention work instead of creating a ticket every tick.
- [ ] Regression coverage proves unlimited review continues beyond former cap, finite caps still work, soft signals deduplicate, stale-cap recovery preserves feedback, and resource/reviewer limits remain enforced. Bound unchanged no-progress loops through existing stall handling and actionable operator diagnosis; do not silently run infinite identical paid attempts.
- [ ] Report a retrospective of representative CG300/323/297/339/358/365 loop histories, separating actual implementation defects from avoidable process churn, with measurable prevention follow-ups and no weakened acceptance claims.
