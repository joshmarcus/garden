---
id: CG-507
title: Honor a granted revision before repeating a threshold stop
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/human.py
- src/garden/scheduler/dispatch.py
- tests/scheduler/test_human.py
branch: garden/cg-507-honor-a-granted-revision-before-repeating-a-thre
pr: https://github.com/joshmarcus/context-garden/pull/413
discovered_from: CG-437
attempts: 1
last_dispatched_at: '2026-09-10T03:58:59+00:00'
created: '2026-09-10T03:14:14+00:00'
updated: '2026-09-10T11:07:32+00:00'
---

## Goal

Honor an explicitly granted bounded revision without immediately stopping the same task at an unrecorded historical revision threshold. Keep lifetime limits and the next genuine decision boundary intact.

## Context

Observed repeatedly on RC16 after the supported continue_troubled/change_troubled_approach action. CG411 at head8d560ae1ceab0a41f4a52ffe4987147457c6af4d had8 substantive revisions, recorded thresholds[4,6], and no active run. The operator granted allowance1 for a new substantive recovery-state finding. The next tick recorded threshold8 and set needs_human again BEFORE consuming allowance1. A second supported retry was needed solely to clear the stale threshold stop. CG434 exhibited the same sequence at threshold10 earlier. Preserve the original evidence in input-sweep-0305-review-actions.json and input-sweep-0305-411-threshold.json. Follow up completed CG437 troubled-task policy; coordinate CG500 automatic CI recovery without broadening its scope.

## Acceptance criteria

- [ ] An explicit bounded continuation at the current revision count acknowledges the applicable current decision boundary atomically; the next tick may dispatch the authorized revision without asking for the same threshold decision again.
- [ ] Preserve all lifetime counters, pending findings, source/PR lineage and the exact granted allowance. Do not erase future threshold stops, permit duplicate grants on repeated requests, or let unauthorized revisions proceed after the allowance is consumed.
- [ ] Use the same supported action semantics for CLI/UI/operator paths, with current-head/run/decision checks and safe behavior across restart and a concurrent scheduler tick. Existing active work and explicit deferrals/manual holds remain protected.
- [ ] Regressions cover allowance granted at an unrecorded threshold, previously recorded threshold, ordinary nonthreshold count, repeated approval, restart before dispatch and exhausted allowance afterward. Verify one permitted dispatch and the next genuine stop, rather than merely inspecting state fields.

## Log

- 2026-09-10T03:14:14+00:00 approved (delegated operator recovery of repeated stalled granted revisions)
- 2026-09-10T03:58:59+00:00 dispatched work run 20260910T035855Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18868 tokens)
- 2026-09-10T04:06:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T04:08:14+00:00 opened https://github.com/joshmarcus/context-garden/pull/413 (base main): Troubled-task continuation now records the applicable current decision boundary under the controller lock, preserving lifetime revision counts, feedback, PR/source lineage, and the exact allowance. Verified one authorized dispatch after restart followed by the next genuine exhausted-allowance stop; 127 human scheduler tests and 34 dispatch tests passed, and lint is clean. cost=$1.70
- 2026-09-10T04:10:49+00:00 automated review: approve — The granted continuation now survives restart and permits exactly the authorized revision before the next genuine stop. No blocking defects found. cost=$0.60
- 2026-09-10T11:07:32+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/413
