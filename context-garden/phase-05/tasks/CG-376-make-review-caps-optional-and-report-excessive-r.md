---
id: CG-376
title: Make review caps optional and report excessive review loops as friction
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/config.py
- src/garden/scheduler/review.py
- src/garden/scheduler/human.py
- src/garden/web/pages/config.py
branch: garden/cg-376-make-review-caps-optional-and-report-excessive-r
pr: https://github.com/joshmarcus/context-garden/pull/286
attempts: 1
last_dispatched_at: '2026-09-07T11:59:51+00:00'
created: '2026-09-07T09:29:27+00:00'
updated: '2026-09-07T14:39:28+00:00'
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

## Log

- 2026-09-07T09:30:45+00:00 approved (web)
- 2026-09-07T09:39:58+00:00 priority 1 -> 0 (web)
- 2026-09-07T10:21:10+00:00 dispatched work run 20260907T102043Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10512 tokens)
- 2026-09-07T10:50:39+00:00 preserved uncommitted worktree changes from run 20260907T102043Z-work outside the PR: `git stash apply fc7d5cb9523f3b67adf24f8fba5bac8417d86d61` in /home/joshua/work/worktrees/CG-376 (garden:CG-376:20260907T102043Z-work:reap)
- 2026-09-07T11:40:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/286 (base main): Added explicit null/unlimited review-cap semantics, a separate soft loop-friction threshold, UI/CLI/Now support, regression tests, and a retrospective of the representative review loops. Final CI passed on ab256d7d6e393998d9ea91beee6eadf61eb05d8e. cost=$1.83
- 2026-09-07T11:44:09+00:00 automated review requested changes: Unlimited-cap behavior is implemented coherently and the UI captures are clean, but the required end-to-end regression coverage for continued review and stale-cap recovery is missing. cost=$0.75
- 2026-09-07T11:59:51+00:00 dispatched revise run 20260907T115949Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~17461 tokens)
- 2026-09-07T12:11:49+00:00 preserved uncommitted worktree changes from run 20260907T115949Z-revise outside the PR: `git stash apply 523d7ca079351834f2a06ffb605ec04fa38791b1` in /home/joshua/work/worktrees/CG-376 (garden:CG-376:20260907T115949Z-revise:reap)
- 2026-09-07T12:21:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/286: Added end-to-end review lifecycle regression coverage beyond the former cap and across capped-review recovery. CI passed for 2855f3d. cost=$0.88
- 2026-09-07T14:39:28+00:00 Fast-forward: verified GitHub merge 879cd608bf13672510d15d240db353f5acda7469 after exact-head CI and operator self-review. Not yet deployed; apply unlimited cap after rollout.
