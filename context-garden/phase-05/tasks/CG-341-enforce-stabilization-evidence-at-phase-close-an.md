---
id: CG-341
title: Enforce stabilization evidence at phase close and record unattended operation mechanically
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-05/specs/stabilization.md
branch: garden/cg-341-enforce-stabilization-evidence-at-phase-close-an
pr: https://github.com/joshmarcus/context-garden/pull/247
attempts: 1
last_dispatched_at: '2026-09-06T23:23:20+00:00'
created: '2026-09-06T13:46:36+00:00'
updated: '2026-09-07T01:04:02+00:00'
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
- 2026-09-06T23:36:10+00:00 opened https://github.com/joshmarcus/context-garden/pull/247 (base main): Added a token-free stabilization recorder, evidence report, phase-close gate, and next-phase release gate. Evidence must be current-build, cited, complete, interaction-aware, fixture-isolated where required, and include a four-hour/ten-task unattended window since the last counted repair. cost=$1.53
- 2026-09-06T23:48:45+00:00 triage: changes requested by hand: Operator will preserve and remove only the scheduler-added unrelated snapshot before the first review; no task run is ac
- 2026-09-06T23:59:15+00:00 Operator held first review and preserved scheduler-added snapshot1c18bfd under operator-test-tmp/snapshot-salvage-20260906T2343Z with hashed recovery metadata. Pushed cleanup426e0c82429a422c46a884a2389659ea31677768; complete Git tree equals intended9122d7f. Exact branch CI34067953339 and PR CI34067955193 SUCCESS at23:54. Update permanent PR description and review after current-main reconciliation; real soak remains UNPROVEN. No model revision/local full suite used for cleanup.
- 2026-09-07T01:04:02+00:00 2026-09-07 01:02 UTC: after CG354 merged, incorporated current main332ee916 and pushed1b0894c11de51982eb654eea18d4e23aad5bd457. Branch-specific diff byte-identical before/after integration. Previous6132f888 head CI passed; new head CI pending. PR description updated; first review after current-head CI and free reviewer slot.
