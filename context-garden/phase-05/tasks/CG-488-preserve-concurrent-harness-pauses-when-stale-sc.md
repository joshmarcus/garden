---
id: CG-488
title: Preserve concurrent harness pauses when stale scheduler reads empty state
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/quota.py
- tests/scheduler/test_quota.py
- tests/test_interaction_replay.py
branch: codex/preserve-concurrent-harness-pause
pr: https://github.com/joshmarcus/context-garden/pull/386
runner: manual
attempts: 1
last_dispatched_at: '2026-09-09T15:36:45+00:00'
created: '2026-09-09T15:35:56+00:00'
updated: '2026-09-09T16:55:27+00:00'
---

## Goal
Fix the reproduced stale-reader race causing intermittent main CI harness-pause failure. paused_harnesses currently setdefaults an empty map during read; saving that stale scheduler overwrites another scheduler newly persisted pause.

## Acceptance criteria
- [ ] Read-only pause lookup must not dirty state or erase concurrent pause records.
- [ ] Explicit pause/resume and probe behavior persist normally, with no weakening of dispatch holds.
- [ ] Deterministically test old scheduler read, newer scheduler pause, old unrelated save and verify durable hold. Keep the actual served pause/recovery test.

Main CI34369078147 failed one served pause test; next main passed and twenty local repeats passed. Controlled two-scheduler interleaving reproduces actual lost pause at main7271172. Preserve failed CI evidence. Root isolated source and peer review before versioned deployment.

## Log

- 2026-09-09T15:36:15+00:00 approved
- 2026-09-09T15:36:45+00:00 dispatched work run 20260909T153644Z-work via manual [human] (fresh session, base main, ~21728 tokens)
- 2026-09-09T16:09:14+00:00 external PR attached at codex/preserve-concurrent-harness-pause; existing CI is SUCCESS
- 2026-09-09T16:11:54+00:00 automated review: approve — The focused fix correctly prevents absent pause lookups from dirtying state while preserving explicit pause/resume mutation and dispatch holds. cost=$0.34
- 2026-09-09T16:55:27+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/386
