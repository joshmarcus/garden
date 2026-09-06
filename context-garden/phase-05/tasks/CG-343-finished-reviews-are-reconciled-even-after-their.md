---
id: CG-343
title: Finished reviews are reconciled even after their task leaves review states
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading: []
created: '2026-09-06T14:19:10+00:00'
updated: '2026-09-06T14:19:13+00:00'
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
