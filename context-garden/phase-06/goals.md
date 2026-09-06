---
plant: peony
latin: Paeonia mascula
plate: VI
frozen: '2026-09-06'
---

# phase-06 goals

_Stub written by the operator on 2026-09-05; a holding pen for speculative designs the user wants kept but not scheduled. Rewritten when phase 05 closes._

**In one sentence: ideas that need a design before they need a task.**

## Why this phase

Some proposals are worth keeping and not worth building yet. They live here with a design sketch and open questions, so the planner and the retros can see them without a phase committing to them.

## Goals

1. A collective, searchable context written by runs and read by briefs (CG-222), after a design document argues it is worth a prototype.
2. Whatever the phase-04 and phase-05 retros defer here.

## Non-goals

- Anything a user needs in phase 05.

## Deferred feature expansion, owner decision 2026-09-06

This phase is frozen until all required phase-05 stabilization evidence passes. Preserve existing PRs and branches but do not dispatch, revise or merge them during the hold. Deferred work includes OpenRouter and its adapter spike, remote workers, model pools, operating presets, and consolidation of the two Now pages. Reprioritize based on the adoption demonstration after the gate; do not auto-unfreeze at a calendar time or merely because phase-05 tasks merged.

## EC2 worker automation proposal

Owner-requested specification: [EC2 worker pools](specs/ec2-workers.md). CG-345, CG-346, CG-347, CG-348 cover on-demand provisioning, portable execution, Spot recovery and cost/teardown evidence. These remain drafts under the existing freeze.

Owner clarification: EC2 automation must be a pluggable remote-host lifecycle reusable for workplace development hosts. Garden workers and standalone persistent dev hosts are separate consumers/profiles of the same provider contracts.
