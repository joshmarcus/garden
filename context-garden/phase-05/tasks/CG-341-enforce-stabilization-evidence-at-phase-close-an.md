---
id: CG-341
title: Enforce stabilization evidence at phase close and record unattended operation mechanically
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-05/specs/stabilization.md
created: '2026-09-06T13:46:36+00:00'
updated: '2026-09-06T13:46:36+00:00'
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
