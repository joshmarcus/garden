---
id: CG-436
title: Prevent unrelated interaction replays from driving repeated task revisions
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/interaction_replay.py
- src/garden/walkthrough.py
- src/garden/review.py
- src/garden/scheduler/review.py
- src/garden/scheduler/checkruns.py
- tests/test_review.py
branch: garden/cg-436-prevent-unrelated-interaction-replays-from-drivi
pr: https://github.com/joshmarcus/context-garden/pull/326
runner: remote
discovered_from: CG-332
attempts: 1
last_dispatched_at: '2026-09-08T16:40:38+00:00'
created: '2026-09-08T16:05:24+00:00'
updated: '2026-09-08T17:29:27+00:00'
---

## Goal

Make interaction verification exercise the affected behavior and preserve valid task-specific evidence so unrelated generic replays cannot create an endless implementation/review cycle.

## Context

CG332 has six revisions/four review rounds: the author reports the harness-pause served journey verified, but the scheduler supplies a generic replay and the reviewer correctly rejects its relevance. CG375 has eight review rounds and the same mismatch for actor provenance/stabilization. CG393 and CG397 show similar unrelated-flow rejection. Distinguish a real absent outcome from an artifact path or source-identity problem. Reuse CG339's affected-behavior review policy and CG431's controller-owned backend routing; this follow-up owns replay selection and evidence handoff, not another runner implementation.

## Acceptance criteria

- [ ] Reproduce the CG332 mismatch with a disposable task-specific harness-pause journey and a generic unrelated replay; demonstrate where valid author evidence is lost, superseded or unreadable.
- [ ] Route required interaction verification to a declared affected-flow replay or validate and expose equivalent existing task-specific evidence with defensible source/component provenance. Generic smoke coverage must not claim affected-flow coverage.
- [ ] Preserve refusal for actual missing/failed outcomes or contradictory provenance. Missing metadata alone stays advisory; do not regenerate passing implementation or tests only to fill fields.
- [ ] Classify replay setup/selection/path failures as an actionable verification issue with durable deduplicated continuation, instead of automatically spending repeated implementation revisions on unchanged source.
- [ ] Focused regressions cover repeated ticks/restart, stale and valid source evidence, generic versus affected-flow mismatch, and remote authoring with local verification. Verify a real bounded served journey without production mutation or stress load.

## Evidence

Operator audit 2026-09-08T16:00Z. See CG332 review20260908T155722Z and CG375 review20260908T111417Z; current operator receipt status-20260908T1601. No release deployment is authorized by this task.

## Log

- 2026-09-08T16:05:24+00:00 approved (owner-delegated-repeat-loop-audit)
- 2026-09-08T16:40:38+00:00 dispatched work run 20260908T164038Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14216 tokens)
- 2026-09-08T16:58:25+00:00 opened https://github.com/joshmarcus/context-garden/pull/326 (base main): Interaction review now reuses valid current-head task-specific author evidence or selects a declared affected-flow replay, while explicitly preventing generic smoke replays from claiming affected-flow coverage. Replay failures retain a durable, deduplicated recovery continuation instead of triggering source revisions. cost=$2.07


## Related owner-requested scope classification follow-up

CG-443 owns the CG430 false rejection from an explicitly out-of-scope limitation in interaction.unverified. It follows this completed replay/evidence repair; retain this task's current criteria and do not silently duplicate its implementation here.
- 2026-09-08T17:20:38+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/326
- 2026-09-08T17:29:27+00:00 automated review could not start: CG-436 is done: #326 was merged at 17:20:38
