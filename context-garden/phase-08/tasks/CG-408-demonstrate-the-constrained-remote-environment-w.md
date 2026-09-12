---
id: CG-408
title: Demonstrate the constrained remote environment with recovery and human gates
status: ready
product: context-garden
phase: phase-08
depends_on:
- CG-406
- CG-407
- CG-398
- CG-412
- CG-413
- CG-414
- CG-415
- CG-416
priority: 2
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
created: '2026-09-07T19:56:18+00:00'
updated: '2026-09-09T13:56:28+00:00'
owner_hold: Evidence gathering paused by owner on 2026-09-07; explicit owner release required.
---

## Goal

Produce a repeatable non-production acceptance exercise for the complete generic profile and record outstanding environment-specific evidence privately.

## Acceptance criteria

- [ ] Complete work, checks, independent review, revision and human merge/deploy handoffs on a ready command-backed host using a canonical checkout.
- [ ] Exercise slow provisioning, readiness timeout, dirty reuse, external stack movement, old-head CI, tool denial, host loss and result recovery without lost edits or duplicate acceptance.
- [ ] Audit all committed context and exported artifacts for secret/physical-identity sentinels; record resource limits, cleanup and actual evidence provenance.
- [ ] Keep fixture success distinct from real environment qualification; do not claim unverified source-survey facts or production authorization.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: Phase acceptance. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.


## Multi-product acceptance

- [ ] Exercise multiple products with different checks/timeouts/resource weights, effective ownership, private adapter registration and brief-size reporting alongside the off-machine manual milestone.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-07T20:08:47+00:00 Owner hold: pause phase07 evidence export, pilot/acceptance and post-merge verification work; preserve scope/dependencies, do not reapprove automatically.
- 2026-09-08T10:46:16+00:00 approved (web)
- 2026-09-09T13:56:28+00:00 owner moved deferred work from context-garden/phase-07 to context-garden/phase-08; destination remains frozen, status/history/dependencies preserved
