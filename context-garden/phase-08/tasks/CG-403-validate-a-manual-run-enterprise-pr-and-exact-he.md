---
id: CG-403
title: Validate a manual-run enterprise PR and exact-head CI journey
status: ready
product: context-garden
phase: phase-08
depends_on:
- CG-395
- CG-396
- CG-397
- CG-398
- CG-399
- CG-402
- CG-409
- CG-410
- CG-411
priority: 1
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
created: '2026-09-07T19:56:17+00:00'
updated: '2026-09-09T13:56:28+00:00'
owner_hold: Evidence gathering paused by owner on 2026-09-07; explicit owner release required.
---

## Goal

Before checkout automation changes, run a representative manual-runner journey. Use a synthetic repository for repeatability; real environment evidence requires separately verified access and stays private.

## Acceptance criteria

- [ ] Exercise task packet, authored change, exact-head CI, independent review, revision and human merge handoff using a non-default base and explicit server host.
- [ ] Demonstrate an old green head cannot pass and that bot notices, notification failure and denied access do not cause unsafe progress.
- [ ] Record checkout constraints, wrapper argv/stdin behavior and canonical-path requirements from actual observations to inform the in-place design. Label simulated versus live evidence.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: Manual adoption milestone. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.


## Additional manual milestone prerequisites

F1/F2/F3 expose and complete off-machine manual work and preserve adopted PR branch identity. Demonstrate these flows in the manual pilot; a local-only manual fixture is insufficient.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-07T20:08:47+00:00 Owner hold: pause phase07 evidence export, pilot/acceptance and post-merge verification work; preserve scope/dependencies, do not reapprove automatically.
- 2026-09-08T10:45:40+00:00 approved (web)
- 2026-09-09T13:56:28+00:00 owner moved deferred work from context-garden/phase-07 to context-garden/phase-08; destination remains frozen, status/history/dependencies preserved
