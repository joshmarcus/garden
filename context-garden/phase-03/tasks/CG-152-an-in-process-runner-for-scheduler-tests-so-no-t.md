---
id: CG-152
title: An in-process runner for scheduler tests so no test drives a subprocess worker
status: running
product: context-garden
phase: phase-03
depends_on:
- CG-137
priority: 1
difficulty: hard
reading: []
branch: garden/cg-152-an-in-process-runner-for-scheduler-tests-so-no-t
discovered_from: retro:context-garden/phase-02-friction
attempts: 1
last_dispatched_at: '2026-09-05T03:37:51+00:00'
created: '2026-09-05T03:14:36+00:00'
updated: '2026-09-05T03:42:07+00:00'
---

## Goal

An in-process runner for scheduler tests so no test drives a subprocess worker.

## Context

From the phase-02 retro's open list (item 5), reconciled against what merged on 2026-09-05: "Subprocess-driven scheduler tests remain timing-fragile; no in-process runner". See `../phase-02-friction/docs/retro.md` for the evidence and the persona reports under `../phase-02-friction/docs/reviews/`. Write the acceptance criteria when the task is planned.

## Acceptance criteria

- [ ] to be written at planning; the retro item above is the requirement.

## Log
- 2026-09-05T03:15:00+00:00 filed from the phase-02 retro (open item 5)
- 2026-09-05T03:19:59+00:00 approved (web)
- 2026-09-05T03:37:51+00:00 dispatched work run 20260905T033741Z-work via local [claude model=claude-fable-5-1] (fresh session, base garden/cg-137-split-the-scheduler-by-tick-phase-and-the-web-ac stacked on CG-137, ~3655 tokens)
- 2026-09-05T03:42:07+00:00 parent CG-137 merged; will rebase onto main when the current run finishes
