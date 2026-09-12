---
id: CG-405
title: Apply host-local resource admission and capability routing to command-backed hosts
status: merged_into_parent
product: context-garden
phase: phase-07
depends_on:
- CG-404
- CG-346
priority: 1
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-405-apply-host-local-resource-admission-and-capabili
pr: https://github.com/joshmarcus/context-garden/pull/322
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T17:12:28+00:00'
created: '2026-09-07T19:56:17+00:00'
updated: '2026-09-09T04:11:20+00:00'
---

## Goal

Reuse portable admission and host execution contracts for memory, disk, heavy-check leases and required environment capabilities.

## Acceptance criteria

- [ ] Route only to an eligible host class/environment with fresh measured readiness; controller free memory cannot substitute for remote headroom.
- [ ] Work, setup, base probes, checks and reviews share host-scoped limits; two controllers or reconnects cannot double-admit a heavy check.
- [ ] Stale probes, unavailable hosts and lease loss fail closed with environment-owned recovery, not artificial implementation failures. Show actual host admission reasons using aliases.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G5 delta over phase-05 admission. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T15:44:09+00:00 dispatched work run 20260908T154409Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-404-add-command-backed-host-acquisition-readiness-an stacked on CG-404, ~9293 tokens)
- 2026-09-08T16:04:47+00:00 opened https://github.com/joshmarcus/context-garden/pull/322 (base garden/cg-404-add-command-backed-host-acquisition-readiness-an): Added portable host requirements and admission evidence, command-backed atomic admission/renewal/release actions, and fail-closed capability, resource, freshness, and lease validation. Host-local leases coordinate every execution activity across controllers without consulting controller headroom. cost=$1.55
- 2026-09-08T16:18:29+00:00 automated review produced no verdict (idle 21 min (no output or file change))
- 2026-09-08T16:49:08+00:00 PR conflicts with garden/cg-404-add-command-backed-host-acquisition-readiness-an; rebase onto garden/cg-404-add-command-backed-host-acquisition-readiness-an conflicts (src/garden/hosts/core.py, tests/test_command_hosts.py); a rebase agent will resolve it
- 2026-09-08T16:51:57+00:00 dispatched rebase run 20260908T165157Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base garden/cg-404-add-command-backed-host-acquisition-readiness-an, conflict only; easy tier, ~1215 tokens)
- 2026-09-08T16:58:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/322: Resolved conflicts in core.py and test_command_hosts.py, preserving host reservations and admission leases; rebase completed. cost=$0.03
- 2026-09-08T17:09:25+00:00 automated review requested changes: Request changes because admission renewal, cancellation, release, and environment-stop recording can lose concurrent controller updates. Current-head focused tests and lint pass, and the remaining admission behavior is well covered. cost=$0.35
- 2026-09-08T17:12:28+00:00 dispatched revise run 20260908T171228Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-404-add-command-backed-host-acquisition-readiness-an, ~10184 tokens)
- 2026-09-08T17:55:22+00:00 worker blocked: Serialized admission lifecycle read-modify-write operations, kept provider commands outside file locks, and added deterministic renewal/release concurrency regressions. Focused host tests and lint pass at 5a533973abbf7853c720c003fd656291a06e90a4, but the full ordinary suite is blocked by an unrelated onboarding failure and subsequent runner-test hang. cost=$2.56
- 2026-09-08T17:56:37+00:00 PR merged into CG-404's branch (`garden/cg-404-add-command-backed-host-acquisition-readiness-an`), not the base `main`; will be done once CG-404 reaches the base
- 2026-09-09T04:11:20+00:00 parent CG-404 merged to main, but this task's commits are not on main yet; still waiting
