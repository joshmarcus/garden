---
id: CG-340
title: Demonstrate onboarding and a useful accepted change on an independent project
status: running
product: context-garden
phase: phase-05
depends_on:
- CG-215
priority: 1
difficulty: hard
reading:
- context-garden/phase-05/specs/stabilization.md
branch: garden/cg-340-demonstrate-onboarding-and-a-useful-accepted-cha
attempts: 1
last_dispatched_at: '2026-09-06T23:25:37+00:00'
created: '2026-09-06T13:46:35+00:00'
updated: '2026-09-06T23:25:37+00:00'
---

## Goal

Demonstrate onboarding and a useful accepted change on an independent project

## Context

Onboarding CG-215 is the entry point. Execute the independent-project journey in specs/stabilization.md. Use a non-Python disposable fixture for repeatability; explicitly distinguish that from a real existing repository and maintainer acceptance. If the real target is unavailable, return the specific missing decision and preserve fixture evidence rather than claiming adoption.

## Acceptance criteria

- [ ] Evidence shows project setup, a grounded plan, useful implementation, review and final behavior. No fabricated provenance or hand-edited generated configuration. State PASS/FAIL/UNPROVEN separately for repeatable compatibility and real-user adoption.
- [ ] The report cites commands, observed results and artifact paths, distinguishes automated checks from real interaction, and states all unverified requirements.

## Log

- 2026-09-06T13:46:35+00:00 approved (cli)


## Owner-authorized concurrency trial, 2026-09-06

The owner raised the worker/shared local-run limit to four after GitHub CI offload. This task is selected alongside CG354 focused-test cleanup, CG361 resource isolation and CG341 mechanical stabilization recording. Own the isolated non-Python onboarding/journey fixture and honest adoption evidence, keeping implementation independent of those tasks. Use disposable assets inside the assigned worktree; do not onboard or push changes to an unrelated real repository without an identified authorized target. No real external maintainer/project has been supplied in this brief: complete all useful repeatable fixture validation and identify the exact missing real-adoption evidence as UNPROVEN rather than inventing it or claiming full adoption. Keep any needed shared-core changes narrow. Do not rewrite resource/runner enforcement, shared Git fixtures or phase-close/soak mechanisms owned by the other tasks. Full suites use the configured GitHub CI helper on the exact committed head; local checks and fixture services remain bounded and serial. Do not change production services/configuration or start extra model agents.
- 2026-09-06T23:25:37+00:00 dispatched work run 20260906T232518Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10298 tokens)
