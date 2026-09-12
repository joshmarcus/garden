---
id: CG-407
title: Require content and deployment verification before describing a change as shipped
status: cancelled
product: context-garden
phase: phase-07
depends_on:
- CG-396
- CG-402
priority: 1
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
created: '2026-09-07T19:56:18+00:00'
updated: '2026-09-09T09:46:19+00:00'
owner_hold: Evidence gathering paused by owner on 2026-09-07; explicit owner release required.
---

## Goal

Start with a follow-up verification-task workflow rather than introducing a new broad execution mode. Keep merged/done distinct from deployed and verified.

## Acceptance criteria

- [ ] Link merge SHA and intended content to a verification task; a reported merge or empty merged branch alone is insufficient evidence of delivery.
- [ ] Require human deployment authorization and observed verification at the deployed boundary before a shipped label; record rollback/revert and unknown states honestly.
- [ ] Exercise missing content, stale deployment and successful verification with synthetic evidence; preserve existing task terminal semantics and prevent duplicate follow-ups.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: Post-merge policy gap. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-07T20:08:47+00:00 Owner hold: pause phase07 evidence export, pilot/acceptance and post-merge verification work; preserve scope/dependencies, do not reapprove automatically.
- 2026-09-09T09:46:19+00:00 cancelled (web)
