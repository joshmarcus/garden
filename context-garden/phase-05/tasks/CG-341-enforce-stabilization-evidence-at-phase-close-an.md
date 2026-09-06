---
id: CG-341
title: Enforce stabilization evidence at phase close and record unattended operation mechanically
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-05/specs/stabilization.md
branch: garden/cg-341-enforce-stabilization-evidence-at-phase-close-an
attempts: 1
last_dispatched_at: '2026-09-06T23:23:20+00:00'
created: '2026-09-06T13:46:36+00:00'
updated: '2026-09-06T23:23:20+00:00'
---

## Goal

Enforce stabilization evidence at phase close and record unattended operation mechanically

## Context

Implement the evidence report and closure gate described in specs/stabilization.md. Reuse existing run/event/metrics APIs and close/retro mechanisms. A lightweight recorder must observe an four-hour productive soak without keeping an LLM awake. Build and test the recorder/gate in this task; the operator then runs the actual soak on the deployed stabilized build. Do not fabricate an four-hour result during a short worker run.

## Acceptance criteria

- [ ] A phase cannot close as stabilized or release deferred features without current-build evidence for required journeys, recovery exercises and the productive unattended window. Missing evidence is UNPROVEN. Operator repairs reset the unattended window and are counted; fixture fault injection is isolated from production. Tests cover bypass paths, stale evidence and absent real-user evidence.
- [ ] The report cites commands, observed results and artifact paths, distinguishes automated checks from real interaction, and states all unverified requirements.

## Log

- 2026-09-06T13:46:36+00:00 approved (cli)


## Owner-authorized concurrency trial, 2026-09-06

The owner raised the worker/shared local-run limit to four after GitHub CI offload. This task is selected for the stabilization critical path alongside CG354 focused-test/Git-fixture cleanup, CG361 resource isolation and CG340 adoption validation. Keep scope independent: implement the mechanical evidence recorder and phase-close gate; CG340 owns the independent-project fixture/journey evidence. Reuse existing APIs and use dedicated modules/tests where practical. Do not rewrite CG361 runner/resource enforcement, CG354 shared Git fixtures or their development guide. Preserve existing work. Full suites use the configured GitHub CI helper on the exact committed head; local checks stay focused, serial and bounded. Do not change production services/configuration, start additional model agents, fault-inject the live garden or claim the actual four-hour soak has completed.
- 2026-09-06T23:23:20+00:00 dispatched work run 20260906T232301Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10291 tokens)
