---
id: CG-343
title: Finished reviews are reconciled even after their task leaves review states
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 4
difficulty: medium
reading: []
branch: garden/cg-343-finished-reviews-are-reconciled-even-after-their
pr: https://github.com/joshmarcus/context-garden/pull/237
attempts: 1
last_dispatched_at: '2026-09-06T19:47:59+00:00'
created: '2026-09-06T14:19:10+00:00'
updated: '2026-09-06T20:29:02+00:00'
---

## Goal

A completed review cannot remain running indefinitely because its task changed status.

## Evidence

2026-09-06 operator investigation: CG-296 run 20260906T134945Z-review has exit_code 0 and a final review verdict, its PID 1065481 is gone, yet run.json remains running after 20+ minutes. The task is ready after a failed rebase; state.review_run still references the completed review. In the pinned build scheduler/__init__.py calls reap_review only when t.status.pr_open (awaiting_triage/in_review/changes_requested). reap.py _owned_run_ids protects every review_run pointer regardless of task status, and reap_dead_runs skips owned runs. Thus neither completion path handles this record. CG-254 was a separate ordinary collection delay and has since progressed to review.

## Acceptance criteria

- [ ] Completed review records are reconciled independently of task status. Apply valid current-head evidence once, or close obsolete reviews explicitly; never reuse a stale-head verdict or revive a terminal task.
- [ ] Regressions cover a finished review still referenced by a ready task following failed rebase, plus running and terminal task transitions. No double-counted usage or duplicate verdict application.
- [ ] Operational views distinguish executing processes from completed work awaiting collection; a stale pointer cannot consume capacity forever.

## Log

- 2026-09-06T14:19:13+00:00 approved (cli)
- 2026-09-06T19:22:30+00:00 dispatched work run 20260906T192158Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~8519 tokens)
- 2026-09-06T19:39:47+00:00 opened https://github.com/joshmarcus/context-garden/pull/237 (base main): Finished review runs are reconciled regardless of task status, with stale or terminal evidence collected for accounting but never applied. Operational run views now label exit-code-complete reviews as awaiting collection. cost=$1.63
- 2026-09-06T19:42:22+00:00 automated review requested changes: The review-reconciliation behavior and focused tests satisfy the task, but the PR also replaces a large generated runtime snapshot unrelated to CG-343. cost=$0.37
- 2026-09-06T19:47:59+00:00 dispatched revise run 20260906T194758Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9034 tokens)
- 2026-09-06T20:10:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/237: Restored the unrelated generated design snapshot from origin/main, leaving the review-reconciliation change scoped to five scheduler, view, and test files. Focused lifecycle tests and lint pass. cost=$0.52
- 2026-09-06T20:12:54+00:00 automated review: approve — The change correctly reconciles completed review runs across ready, running, and terminal task states while preventing stale-head verdict application and duplicate accounting. The five-file diff is scoped, focused tests pass (48 passed), and the PR description clearly captures the outcome and verification. cost=$0.28
- 2026-09-06T20:13:01+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-06T20:27:20+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-06T20:29:02+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/237
