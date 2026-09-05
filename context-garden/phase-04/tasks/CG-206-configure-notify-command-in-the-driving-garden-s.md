---
id: CG-206
title: Configure notify.command in the driving garden so a needs-human transition reaches the operator
status: draft
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: easy
reading: []
created: '2026-09-05T10:30:01+00:00'
updated: '2026-09-05T10:30:01+00:00'
---

## Goal

`notify.command` is implemented and doctor-tested (CG-155) but the driving garden's garden.yaml does not configure it, so no stall overnight reached anyone; the operator found stalls by polling. This is a configuration task for the operator, not a code change: choose a channel that reaches the owner's phone (the Tailscale route was parked), wire `notify.command`, and test it with `garden doctor`.

## Provenance

From the phase-03 persona reviews of 2026-09-05 (project-manager:medium); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] A needs-human transition in the live garden sends a message the owner receives.
- [ ] `garden doctor` reports the notify command as configured and tested.
- [ ] The choice and the command are recorded in the garden's CLAUDE.md.

