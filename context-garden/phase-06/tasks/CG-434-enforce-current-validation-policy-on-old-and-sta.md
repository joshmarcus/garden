---
id: CG-434
title: Enforce current validation policy on old and stacked worker branches
status: done
product: context-garden
phase: phase-06
depends_on: []
priority: 0
order: 2
difficulty: hard
reading:
- src/garden/managed_worker.py
- src/garden/remote_worker.py
- src/garden/validation.py
- src/garden/runner/base.py
- tests/conftest.py
- tests/test_runners.py
- tests/test_remote_worker.py
branch: garden/cg-434-enforce-current-validation-policy-on-old-and-sta
pr: https://github.com/joshmarcus/context-garden/pull/327
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T05:09:58+00:00'
created: '2026-09-08T15:39:34+00:00'
updated: '2026-09-10T05:25:00+00:00'
---

## Goal

Ensure a worker cannot silently restore prohibited default validation workloads merely by starting from an older feature or stacked branch.

## Repeated production evidence

On September8, rc5 workers CG396, CG397 and CG406 used branches predating CG426's approved stress opt-in policy. Their tests/conftest.py had no --run-stress gate and their stress cases were unmarked. CG397 was running plain pytest -q. An upgraded worker daemon and a correct prose brief did not change the old branch's test-selection behavior.

The operator preserved source HEADs, binary diffs and untracked/changed files, then applied only approved CG426 test-selection/marker/instruction hunks from887dbf76430e7ea8688a73eaa5392a210d4a36e6 to those existing checkouts. The old unopted CG397 pytest process was interrupted with SIGINT so its next run could use the corrected policy; its model/daemon and edits survived. Current-main branches and the local CG328 branch already had the policy. No installed package or release was changed.

## Acceptance criteria

- [ ] Resolve mandatory validation policy from an approved current source independently of a worker branch's age; apply or validate it before tests can execute prohibited default workloads.
- [ ] Preserve actual implementation edits and commit provenance. If a safe policy application cannot be established, report a precise setup/policy block rather than run an old full suite or reset useful work.
- [ ] Record effective policy/selection with validation results and integrate the exact-source receipt contract from CG396 without inventing passing results or disabling meaningful ordinary tests.
- [ ] Cover an older branch with unmarked known stress cases, a current branch, a stacked branch and a dirty checkout. Ordinary validation must keep functional tests and exclude stress; explicit authorized opt-in remains available.
- [ ] Use small deterministic fixtures for these regressions. Real CPU/memory/load experiments remain outside the ordinary suite. Do not reintroduce GitHub polling or copy controller credentials into workers.

## Scope and evidence

This closes policy propagation at worker preparation/validation. CG426 already implements the policy on updated source; do not duplicate that implementation. CG431 owns check-backend/path ownership, and CG393 owns waiting/startup timeout classification. Evidence is under /home/joshua/work/operator-test-tmp/heartbeat-20260908T1511 and host-local operator-preservation receipts. Owner explicitly requires stress/load tests excluded by default.

## Log

- 2026-09-08T15:39:34+00:00 approved (operator-owner-default-test-policy)
- 2026-09-08T15:41:03+00:00 dispatched work run 20260908T154103Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22983 tokens)
- 2026-09-08T16:46:44+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$9.69
- 2026-09-08T16:47:54+00:00 dispatched revise run 20260908T164754Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23323 tokens)
- 2026-09-08T16:56:52+00:00 pre-PR checks failed (PR description); no PR opened yet; revise run will fix cost=$1.08
- 2026-09-08T16:57:21+00:00 dispatched revise run 20260908T165721Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23369 tokens)
- 2026-09-08T17:03:55+00:00 opened https://github.com/joshmarcus/context-garden/pull/327 (base main): Mandatory current-source validation policy now protects old, current, stacked, and dirty worker branches while preserving implementation state and recording exact-source validation receipts. The focused regression suite and lint pass at HEAD. cost=$0.44
- 2026-09-08T17:19:39+00:00 automated review produced no verdict (idle 24 min (no output or file change))
- 2026-09-08T17:33:37+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/review.py, tests/test_web.py); a rebase agent will resolve it
- 2026-09-08T17:36:01+00:00 dispatched rebase run 20260908T173601Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1602 tokens)
- 2026-09-08T17:55:13+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Rebased onto origin/main and resolved the review.py and test_web.py conflicts while preserving both sides' changes. cost=$0.01
- 2026-09-08T18:31:22+00:00 check did not run (20260908T183058Z-check): idle 38 min (no output or file change); will retry
- 2026-09-08T18:34:04+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:36:11+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:38:13+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:40:08+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:42:09+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:43:46+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:43:50+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:45:01+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:46:10+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:47:20+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:48:30+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:49:40+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:50:50+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:52:14+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:53:43+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:55:04+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:56:24+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:57:47+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T18:59:13+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:00:46+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:02:17+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:03:47+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:05:17+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:06:50+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:08:23+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:10:26+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:12:05+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:14:04+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:16:19+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:18:33+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:20:38+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:23:00+00:00 check did not run (20260908T183122Z-check): idle 41 min (no output or file change); retry also failed; needs human
- 2026-09-08T19:23:55+00:00 Operator verified deployment-era interrupted check/review, preserved failed record, queued exactly one current-head replay/review through current controller runtime; no implementation retry.
- 2026-09-08T19:34:04+00:00 review validation scope expansion: Indirect pytest launcher admission — Inspection found that only shell-wrapped pytest is rejected; other launchers fall through as non-pytest and can remove the environment guard.
- 2026-09-08T19:34:06+00:00 automated review requested changes: The focused regressions and lint pass at the reviewed head, but validation admission still permits prohibited workloads through common indirect launchers such as `env`, `uv`, `tox`, or `make`. The required served replay is also generic evidence for unrelated reap/retry behavior and does not exercise validation policy or receipt ingestion. cost=$0.43
- 2026-09-09T01:52:58+00:00 Operator restored queued author to remote after current-source check routing inspection: no generated capture pages or controller-owned spec paths. Full substantive feedback preserved; current owner proportional-validation policy appended. No active run or cap changed.
- 2026-09-09T01:54:48+00:00 dispatched revise run 20260909T015448Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~28170 tokens)
- 2026-09-09T02:08:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Validation admission now rejects indirect launchers whose workloads cannot be proven non-pytest, preventing environment or build wrappers from bypassing current stress policy. Policy rejections also write exact-source auditable failure receipts without executing the requested workload. cost=$0.68
- 2026-09-09T02:09:22+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/events.py, src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-09T02:12:38+00:00 dispatched rebase run 20260909T021232Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3353 tokens)
- 2026-09-09T02:21:39+00:00 automated review: request_changes — The named launcher regressions pass, but validation remains bypassable through any unrecognized project script, so old branches can still execute prohibited default stress workloads. cost=$0.50
- 2026-09-09T02:57:40+00:00 rebase conflict run 20260909T021232Z-rebase did not finish: worker idle 22 min (no output or file change); will retry
- 2026-09-09T02:57:41+00:00 rebase conflict run 20260909T021232Z-rebase did not finish: worker idle 22 min (no output or file change); will retry
- 2026-09-09T02:57:58+00:00 dispatched rebase run 20260909T025758Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3535 tokens)
- 2026-09-09T04:28:02+00:00 rebase conflict run 20260909T025758Z-rebase did not finish: worker exited 1: {'message': "You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 15th, 2026 2:14 AM."}; retry also failed; needs human to resolve src/garden/events.py, src/garden/scheduler/review.py
- 2026-09-09T04:48:20+00:00 check did not run (20260909T042808Z-check): idle 20 min (no output or file change); will retry
- 2026-09-09T05:08:28+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:09:45+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:10:59+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:12:15+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:13:34+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:14:46+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:15:58+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:17:09+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:18:21+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:19:34+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:20:47+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:22:00+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:23:12+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:24:31+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:25:43+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:26:55+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T05:28:08+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:42:13+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:42:21+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:43:57+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:45:19+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:45:33+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T09:46:50+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:48:39+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:49:59+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:51:18+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:52:28+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:53:37+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:54:46+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:56:06+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:57:23+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T09:59:11+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:00:39+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:02:00+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:03:15+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:04:34+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:05:57+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:07:09+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:08:19+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:09:50+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:11:20+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:12:37+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:14:01+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:14:05+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:15:15+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:16:25+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:17:36+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:18:04+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:18:09+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:19:30+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:20:47+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:22:01+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:23:29+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:24:42+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:25:55+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:27:09+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:28:23+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:29:43+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:30:54+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:32:06+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:33:18+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:34:34+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:35:46+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:37:12+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:38:37+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:39:50+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:40:58+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:42:16+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:43:43+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:45:01+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:46:14+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:47:27+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:48:35+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:49:51+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:51:08+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:52:21+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:53:33+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:54:42+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:55:51+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:57:04+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:58:21+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T10:59:32+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T11:01:16+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T11:02:36+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T11:03:51+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T11:04:09+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T11:05:06+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T11:06:23+00:00 check did not run (20260909T044820Z-check): idle 20 min (no output or file change); retry also failed; needs human
- 2026-09-09T11:06:38+00:00 cleared stale check metadata and recovered task state
- 2026-09-09T11:06:39+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T11:07:50+00:00 dispatched revise run 20260909T110750Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21281 tokens)
- 2026-09-09T12:44:43+00:00 revision failed: worker timed out
- 2026-09-09T12:45:04+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T12:46:14+00:00 dispatched revise run 20260909T124614Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21765 tokens)
- 2026-09-09T13:46:01+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T13:47:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Validation admission now fails closed for opaque scripts and build-tool launchers, so only direct pytest commands can use the current-source policy wrapper; rejected commands produce exact-source failure receipts without execution. Merged current main without rewriting branch history and verified exact HEAD e47ff030c497368c76c05903012a2364ef922069 with focused policy, receipt, scheduler, remote-worker, review, brief, and nested-supervisor tests plus lint. cost=$2.30
- 2026-09-09T14:03:52+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/brief.py, src/garden/events.py, src/garden/scheduler/poll.py, src/garden/scheduler/review.py, tests/scheduler/test_poll.py); a rebase agent will resolve it
- 2026-09-09T14:04:08+00:00 dispatched rebase run 20260909T140408Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~11422 tokens)
- 2026-09-09T14:45:16+00:00 check did not run (20260909T142512Z-check): idle 20 min (no output or file change); will retry
- 2026-09-09T14:54:34+00:00 pre-PR checks failed (lint, syntax); revise run will fix before the PR is updated cost=$0.08
- 2026-09-09T14:57:39+00:00 dispatched revise run 20260909T145739Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22330 tokens)
- 2026-09-09T15:08:07+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:12:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Repaired the rebase-introduced syntax and import failures, preserved CI failure-triggered revision behavior, restored exact-head CI status rendering, and aligned the nested validation fixture with fail-closed direct-pytest admission. Committed as 620794838e7f68b79f535ceeff0f7b4edd5e3fd2; focused suites passed with 14, 147, and 4 tests respectively, and Ruff passed. cost=$1.02
- 2026-09-09T15:16:50+00:00 automated review requested changes: Current-source validation behavior is well covered, but remotely supplied incomplete receipts can still satisfy the authoritative worker-check CI gate. cost=$0.47
- 2026-09-09T15:17:19+00:00 dispatched revise run 20260909T151719Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22406 tokens)
- 2026-09-09T15:50:19+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T15:52:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Authoritative worker-check CI now accepts only complete, internally consistent exact-head supervisor receipts and rejects truncated or fabricated remote payloads. Verified commit b369e906 with 163 focused tests and clean Ruff lint. cost=$0.88
- 2026-09-09T15:52:18+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py, tests/scheduler/test_poll.py); a rebase agent will resolve it
- 2026-09-09T15:52:32+00:00 dispatched rebase run 20260909T155232Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~7910 tokens)
- 2026-09-09T16:13:10+00:00 automated review:  —
- 2026-09-09T16:39:48+00:00 check did not run (20260909T161907Z-check): idle 21 min (no output or file change); will retry
- 2026-09-09T17:00:24+00:00 check did not run (20260909T163948Z-check): idle 21 min (no output or file change); retry also failed; needs human
- 2026-09-09T17:17:10+00:00 check did not run (20260909T170038Z-check): check execution did not complete

worker materialization failed during checkout preflight: warm checkout has unresolved index; preserved at /var/lib/garden-worker/work/preserved-materializations/CG-434/20260909T170038Z-check-b6cbb85ce060; will retry
- 2026-09-09T17:18:52+00:00 check did not run (20260909T171710Z-check): check execution did not complete

worker materialization failed during checkout preflight: warm checkout has unresolved index; preserved at /var/lib/garden-worker/work/preserved-materializations/CG-434/20260909T171710Z-check-7c7fca8468d5; retry also failed; needs human
- 2026-09-09T17:20:20+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-09T17:33:03+00:00 recovered terminal check stop; retained actionable feedback for revision
- 2026-09-09T17:35:05+00:00 dispatched rebase run 20260909T173459Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8128 tokens)
- 2026-09-09T17:42:57+00:00 check did not run (20260909T174107Z-check): check execution did not complete

worker materialization failed during checkout preflight: warm checkout has unresolved index; preserved at /var/lib/garden-worker/work/preserved-materializations/CG-434/20260909T174107Z-check-fbf9308b800c; will retry
- 2026-09-09T17:45:03+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$0.02
- 2026-09-09T17:51:35+00:00 dispatched revise run 20260909T175130Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23039 tokens)
- 2026-09-09T17:54:25+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T17:56:34+00:00 check did not run (20260909T175431Z-check): check execution did not complete

worker materialization failed during checkout preflight: warm checkout has unresolved index; preserved at /var/lib/garden-worker/work/preserved-materializations/CG-434/20260909T175431Z-check-a72df8fdd2d7; will retry
- 2026-09-09T17:58:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Sorted the scheduler poll imports to resolve the reported pre-PR lint failure. At commit 96767b1fb6c22a879635010b4d8c572d4546f65f, the focused poll suite passed 28 tests and repository-wide Ruff lint passed. cost=$0.37
- 2026-09-09T18:00:27+00:00 CI failure
- 2026-09-09T18:32:05+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T18:51:22+00:00 dispatched revise run 20260909T185122Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23427 tokens)
- 2026-09-09T18:59:53+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T19:24:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Authoritative validation receipt selection now follows controller-observed completion-write order rather than PID/index filenames, ensuring a newer failed rerun supersedes an older success. Verified commit eda2f90dce77590026e20ba5ede35742979d4469 with 347 affected tests passing (4 stress tests deselected), a final 65-test focused pass, clean Ruff lint, and clean diff/conflict inspection. cost=$0.94
- 2026-09-09T19:24:53+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/events.py, src/garden/scheduler/reap.py); a rebase agent will resolve it
- 2026-09-09T19:25:00+00:00 dispatched rebase run 20260909T192500Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8806 tokens)
- 2026-09-09T19:28:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Rebased onto origin/main and resolved conflicts while preserving both branches' metrics, pool-member state, exact-head tracking, and validation policy changes. cost=$0.02
- 2026-09-09T19:28:48+00:00 1 new review item(s)
- 2026-09-09T20:07:50+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T20:08:14+00:00 dispatched revise run 20260909T200813Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24027 tokens)
- 2026-09-09T23:52:26+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:54:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Fail-closed receipt selection now treats the newest matching malformed or inconsistent exact-head receipt as authoritative instead of falling back to an older success. Remote validation also preserves execution.json, exit_code, and stderr.log in the controller-owned receipt directory; focused tests and repository-wide Ruff lint pass at ba703601ec64099b2600343324c5f90f0bfd18c7. cost=$1.36
- 2026-09-09T23:58:12+00:00 automated review requested changes: Branch-policy enforcement is well covered, but the authoritative receipt gate still accepts incomplete supervisor evidence as successful. cost=$0.67
- 2026-09-10T00:11:45+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T00:59:23+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T00:59:59+00:00 dispatched revise run 20260910T005959Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24187 tokens)
- 2026-09-10T01:04:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T01:06:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Authoritative worker CI now accepts only validation receipts with a genuine finished supervisor state and consistent exit codes. Commit 3d3281b4 passed 37 focused CI-status/scheduler tests and repository-wide Ruff lint. cost=$0.83
- 2026-09-10T01:10:07+00:00 automated review requested changes: Current-source validation behavior is well covered, but incomplete supervisor evidence can still satisfy the authoritative worker-check gate. cost=$0.58
- 2026-09-10T01:43:22+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T01:44:31+00:00 dispatched revise run 20260910T014431Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24637 tokens)
- 2026-09-10T01:52:49+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T01:54:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Authoritative worker CI now rejects truncated supervisor receipts and validates bounded timing, ownership, and direct or inherited admission evidence. Exact HEAD c67deb52d8e9e8bd7fafebcee0fff758ed7d4fec passed 96 focused tests and repository-wide Ruff lint. cost=$1.17
- 2026-09-10T01:54:14+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_remote_worker.py); a rebase agent will resolve it
- 2026-09-10T01:54:21+00:00 dispatched rebase run 20260910T015421Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8675 tokens)
- 2026-09-10T01:57:55+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Rebased onto origin/main and resolved the tests/test_remote_worker.py import conflict while preserving both sides’ changes. cost=$0.01
- 2026-09-10T02:01:39+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-10T02:01:43+00:00 dispatched rebase run 20260910T020143Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8676 tokens)
- 2026-09-10T02:02:45+00:00 automated review: request_changes — Validation policy behavior is well covered, but the authoritative receipt selector can still report success after a newer receipt was truncated. cost=$0.86
- 2026-09-10T02:05:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Rebased onto origin/main and resolved the review.py conflicts, preserving current-main provenance arguments and exact-head CI evidence. cost=$0.02
- 2026-09-10T02:07:43+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: record effective policy/selection and ; run `garden triage CG-434 --changes "<feedback>" to unblock`
- 2026-09-10T02:26:42+00:00 moved from context-garden/phase-05 to context-garden/phase-06
- 2026-09-10T02:27:16+00:00 triage: changes requested by hand: The prior supervisor-schema correction made real progress; the remaining reproduced defect is specifically INVALID/TRUNC
- 2026-09-10T02:29:09+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T02:30:34+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T02:31:39+00:00 dispatched revise run 20260910T023139Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22266 tokens)
- 2026-09-10T02:36:11+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T02:37:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Authoritative worker-check selection now fails closed when the newest truncated receipt identifies the queried source, while unrelated-source truncations do not block valid evidence. Commit 4b9a004b passed 41 focused CI-status/scheduler tests and repository-wide Ruff lint. cost=$0.56
- 2026-09-10T02:41:04+00:00 automated review requested changes: Validation policy behavior is well covered, but the authoritative receipt gate can still reuse an older success after a newer receipt is truncated before its source SHA is recoverable. cost=$0.55
- 2026-09-10T03:11:36+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T03:12:41+00:00 dispatched revise run 20260910T031241Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22696 tokens)
- 2026-09-10T03:16:05+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T03:17:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Fixed authoritative receipt selection so a newest receipt truncated before source identity is recoverable cannot expose an older success. Commit 760db902 passed 42 focused CI-status and scheduler tests plus repository-wide Ruff lint. cost=$0.58
- 2026-09-10T03:20:13+00:00 automated review requested changes: Current-source validation is well covered, but remote receipt transport still permits fallback to an older success after a newer receipt is truncated. cost=$0.57
- 2026-09-10T04:07:32+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T04:10:42+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T04:11:05+00:00 dispatched revise run 20260910T041105Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22935 tokens)
- 2026-09-10T04:17:00+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T04:18:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Remote validation transport now preserves malformed or truncated receipt candidates as bounded SHA-only sentinels, preventing a newer incomplete attempt from exposing an older success. Commit 5f3f9fbba3e8f470e43ed6632dbbd5bffd12ae70 passed 89 focused remote-receipt/CI-status tests and repository-wide Ruff lint. cost=$0.98
- 2026-09-10T04:18:32+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/poll.py); a rebase agent will resolve it
- 2026-09-10T04:18:35+00:00 dispatched rebase run 20260910T041834Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8676 tokens)
- 2026-09-10T04:21:56+00:00 automated review: request_changes — Validation policy behavior is well covered, but authoritative receipt selection can still reuse an older success after a newer malformed receipt exceeds the sentinel's eight-SHA limit. cost=$0.56
- 2026-09-10T04:25:43+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Rebased CG-434 onto origin/main and resolved all conflicts. cost=$0.04
- 2026-09-10T04:30:39+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: record effective policy/selection with; run `garden triage CG-434 --changes "<feedback>" to unblock`
- 2026-09-10T04:57:31+00:00 triage: changes requested by hand: Preserve the new bounded SHA-only malformed-receipt sentinel and the end-to-end remote transport regressions. Close the
- 2026-09-10T05:00:19+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T05:01:24+00:00 dispatched revise run 20260910T050124Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23590 tokens)
- 2026-09-10T05:08:10+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T05:09:34+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Malformed remote validation receipts now carry an explicit identity-overflow flag, preventing a ninth-or-later queried SHA from falling back to an older success. Also corrected the branch-specific GitHub CI identity regression; 124 affected tests and repository-wide Ruff lint pass at final HEAD c35d531b. cost=$1.66
- 2026-09-10T05:09:45+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-10T05:09:58+00:00 dispatched rebase run 20260910T050958Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8676 tokens)
- 2026-09-10T05:14:26+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/327: Rebased onto origin/main and merged both review.py changes without unrelated edits. cost=$0.02
- 2026-09-10T05:20:12+00:00 automated review: approve — Current-source validation policy and fail-closed exact-head receipt handling satisfy the task outcomes. cost=$0.78
- 2026-09-10T05:22:39+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T05:25:00+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/327
