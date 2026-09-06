---
id: CG-339
title: Review affected behavior through the running application before accepting interaction claims
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-05/specs/stabilization.md
created: '2026-09-06T13:46:32+00:00'
updated: '2026-09-06T13:46:34+00:00'
---

## Goal

Review affected behavior through the running application before accepting interaction claims

## Context

Build on CG-315 capture evidence and CG-324 required evidence. Add actual interaction coverage for applicable PRs, with task objective, empty and failure states, browser observations and evidence tied to the tested head. Treat no_change and attention prompts as user outcomes, not just state transitions. Use disposable gardens, never the live operator queue.

## Acceptance criteria

- [ ] A reviewer can replay an affected flow in the real running app and distinguish screenshot-only evidence from performed actions. Applicable PRs with missing, failed or stale interaction evidence cannot be accepted as verified. Non-UI changes keep proportionate validation.
- [ ] The report cites commands, observed results and artifact paths, distinguishes automated checks from real interaction, and states all unverified requirements.

## Log

- 2026-09-06T13:46:34+00:00 approved (cli)
