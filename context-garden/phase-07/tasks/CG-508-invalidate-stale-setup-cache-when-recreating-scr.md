---
id: CG-508
title: Invalidate stale setup cache when recreating scratch-merge checkouts
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/runner/base.py
- src/garden/scheduler/checkruns.py
- src/garden/gitops.py
- tests/test_runners.py
- tests/test_automerge.py
branch: garden/cg-508-invalidate-stale-setup-cache-when-recreating-scr
pr: https://github.com/joshmarcus/context-garden/pull/416
discovered_from: CG-484
attempts: 1
last_dispatched_at: '2026-09-10T05:37:41+00:00'
created: '2026-09-10T04:57:35+00:00'
updated: '2026-09-10T11:08:49+00:00'
---

## Goal

Invalidate setup-cache evidence when a scratch-merge checkout is removed and recreated, so required tools are provisioned before checks run.

## Confirmed reproduction

CG-349 scratch-merge checks 20260910T041055Z-check and 20260910T041206Z-check each failed with exit 127 because the recreated checkout had no `.venv/bin/ruff`, while the external `.garden-setup-CG-349.scratch-merge` command-stamp marker from September 9 survived. `run_setup` treated the stale marker as a valid hit and skipped setup. A manually restored scratch venv passed Ruff 0.16.6, but the next scratch recreation removed it and reproduced the failure. This extends the stale recreated-checkout defect addressed for base probes by completed CG-484; cancelled CG-097 recorded the older vague symptom and must remain historical.

## Acceptance criteria

- [ ] Pair setup-cache validity with the actual checkout/environment lifetime. Removing or recreating a scratch worktree invalidates its external setup marker, or a cache hit verifies the required environment still exists before skipping setup.
- [ ] A fresh scratch-merge checkout with a stale matching command stamp runs setup, then the configured check. Repeated checks against an unchanged intact environment may still reuse safe setup work.
- [ ] Preserve CG-484 base-probe recovery, genuine source/check failures, exact-head scratch-merge gating, and concurrent task isolation. Do not convert missing tools into a pass or require a manual venv repair.
- [ ] Add deterministic regressions for stale external marker plus recreated scratch, intact-cache reuse, failed/partial setup, and concurrent task names. Use portable configurable paths on Linux, macOS, and Windows through WSL; report platforms not exercised.

## Log

- 2026-09-10T04:57:35+00:00 approved (delegated operator follow-up for confirmed recurring scratch setup-cache defect)
- 2026-09-10T05:37:41+00:00 dispatched work run 20260910T053738Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20430 tokens)
- 2026-09-10T05:44:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T05:45:34+00:00 opened https://github.com/joshmarcus/context-garden/pull/416 (base main): Scratch-merge materializations now carry unique setup-cache generation keys, preventing stale markers from skipping setup after checkout recreation while preserving reuse for retries. Focused tests passed (83), Ruff passed, and the change is committed as commit 36095ff4. cost=$1.28
- 2026-09-10T05:47:52+00:00 automated review: approve — Scratch-merge setup caching is correctly bound to each checkout materialization while preserving retry reuse and existing failure gating. cost=$0.42
- 2026-09-10T11:08:49+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/416
