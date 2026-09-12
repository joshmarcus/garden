---
id: CG-639
title: Migrate single-user gardens to multiplayer with a recoverable cutover
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-634
  after: merge
- id: CG-635
  after: merge
- id: CG-637
  after: merge
- id: CG-638
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/cli/__init__.py
- src/garden/config.py
- src/garden/store.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:16+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Make explicit multiplayer enrollment safe and understandable for an existing garden while preserving the supported standalone mode.

## Context and scope

Document and implement the actual migration and reversal paths after shared authority, startup, handoff and views are available. Do not silently authenticate legacy owner labels or run a migration against this live garden.

## Acceptance criteria

- [ ] Provide a non-mutating preview that maps legacy owner labels to enrolled member IDs, preserves explicit unassignment and phase defaults, and identifies unknown owners, active attempts, pending effects, local edits and required setup. Commit only an explicitly chosen migration.
- [ ] Drain or hand off active work, preserve a consistent recoverable snapshot and enable shared authority with a version gate. Remove old supported controller write access; a configuration flag alone must not allow old local schedulers to keep progressing work.
- [ ] Make interrupted migration resumable and reversal explicit: quiesce claims/effects and export one consistent standalone authority. Preserve historical authors, raw results, failed checks and reviews; do not rewrite history as if legacy labels were authenticated identities.
- [ ] Document coordinator setup/recovery, member enrollment, assignment, local serve/watch, public projection setup and the supported trust/availability limits using actual implemented commands. Validate a representative disposable legacy garden, interrupted cutover and legacy-mode compatibility.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
