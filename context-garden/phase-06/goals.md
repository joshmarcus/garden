---
plant: peony
latin: Paeonia mascula
plate: VI
---

## Current owner authorization, 2026-09-07

Phase06 is unfrozen and all ten tasks are approved for normal scheduling. This supersedes all historical freeze/defer statements below. Preserve existing branches and PRs; CG213 follows the CG302 adapter decision. Normal resource limits and current-head automated review remain required. Phase07 evidence holds on CG402/403/407/408 remain in force.


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

## Decisions

- **Should the recorded first-pass, hand-merge and agent-rebase target misses be accepted as explicit Phase05 exceptions with accountable follow-ups once substantive closing defects are resolved?** — answered: Given that we are re-opening, let's watch for real stabilization evidence now (by web at 2026-09-10T13:16:29+00:00)

## Phase05 retrospective proposal, September10

The [proposed next goals](docs/phase05-retro-proposed-goals-2026-09-10.md) are retained for planning review. Existing Phase06 authorization and active task ownership remain in force; the proposal does not refreeze the phase or replace explicit owner decisions.
