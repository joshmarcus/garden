---
id: CG-153
title: State dirty-on-read no longer clobbers concurrent writes; a resumed reap does not double-emit run_finished
status: ready
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 0
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-02-friction
created: '2026-09-05T03:14:37+00:00'
updated: '2026-09-05T03:20:00+00:00'
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
