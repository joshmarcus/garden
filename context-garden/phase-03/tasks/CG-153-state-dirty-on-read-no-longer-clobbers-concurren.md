---
id: CG-153
title: State dirty-on-read no longer clobbers concurrent writes; a resumed reap does not double-emit run_finished
status: done
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 0
difficulty: medium
reading: []
branch: garden/cg-153-state-dirty-on-read-no-longer-clobbers-concurren
pr: https://github.com/joshmarcus/context-garden/pull/97
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T03:37:31+00:00'
created: '2026-09-05T03:14:37+00:00'
updated: '2026-09-05T03:50:55+00:00'
---

## Goal

State dirty-on-read no longer clobbers concurrent writes; a resumed reap does not double-emit run_finished.

## Context

From the phase-02 retro's open list (item 6), reconciled against what merged on 2026-09-05: "State dirty-on-read rule clobbers concurrent writes; run_finished double-emitted on resumed reap". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 6)
- 2026-09-05T03:20:00+00:00 approved (web)
- 2026-09-05T03:37:31+00:00 dispatched work run 20260905T033721Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-137-split-the-scheduler-by-tick-phase-and-the-web-ac stacked on CG-137, ~3674 tokens)
- 2026-09-05T03:42:07+00:00 parent CG-137 merged; will rebase onto main when the current run finishes
- 2026-09-05T03:47:21+00:00 opened https://github.com/joshmarcus/context-garden/pull/97 (base garden/cg-137-split-the-scheduler-by-tick-phase-and-the-web-ac): State now writes back only keys it actually changed (snapshot-on-read replaces the mark-on-read rule that clobbered concurrent writers of a merely-read key), and a resumed reap skips the already-sent run_finished so a run's cost is counted once. cost=$2.52
- 2026-09-05T03:47:25+00:00 parent CG-137 merged; rebased onto main and retargeted the PR
- 2026-09-05T03:49:45+00:00 automated review: approve — Both defects are correctly fixed and well-tested: snapshot-on-read replaces the clobbering mark-on-read rule, and a resumed finalize skips the run_finished emit. Scope is tight and the description is clean. cost=$0.48
- 2026-09-05T03:50:55+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/97
