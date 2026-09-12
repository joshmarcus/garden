---
id: CG-629
title: Introduce authenticated garden members and explicit multiplayer roles
status: running
product: context-garden
phase: phase-10
depends_on: []
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/config.py
- src/garden/web/app.py
branch: garden/cg-629-introduce-authenticated-garden-members-and-expli
pr: https://github.com/joshmarcus/context-garden/pull/504
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
attempts: 1
last_dispatched_at: '2026-09-12T17:48:53+00:00'
created: '2026-09-11T20:19:12+00:00'
updated: '2026-09-12T17:48:53+00:00'
---

## Goal

Give every multiplayer request and local scheduler a stable, authenticated member identity with administrator, member and viewer capabilities.

## Context and scope

Implement identity and membership foundations behind explicit multiplayer mode. Existing task owner strings are metadata and cannot authenticate a caller. Use a single shared identity vocabulary across coordinator, local clients and web actions; avoid independently trusted owner parameters.

## Acceptance criteria

- [ ] Represent stable garden/member/installation identities, active or disabled membership, roles and project visibility. Support explicit administrator enrollment, installation credential rotation and revocation without storing secrets or private identity bindings in committed context.
- [ ] Authenticate caller and coordinator identities across the local-client protocol; reject spoofed user IDs, wrong-garden credentials, disabled members and revoked installations. Use an authenticated encrypted transport outside explicit local development.
- [ ] Provide common authorization decisions for administrator operations, member-owned work and read-only viewers. Administrator status alone does not grant the scheduler authority over other assignees. Preserve existing substantive human/review gates.
- [ ] Exercise role and membership boundaries with focused checks, including direct requests that bypass visible controls. Preserve legacy single-user behavior when multiplayer mode is not enabled.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers); no kickoff report for context-garden/phase-10
- 2026-09-12T17:06:50+00:00 dispatched work run 20260912T170650Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2624 tokens)
- 2026-09-12T17:15:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-12T17:17:00+00:00 opened https://github.com/joshmarcus/context-garden/pull/504 (base main): Added private authenticated garden membership with stable garden/member/installation identities, administrator/member/viewer roles, visibility policy, credential rotation/revocation, and shared authorization at the web boundary. Verified 187 focused tests pass and `.venv/bin/ruff check src tests scripts` is clean. cost=$1.98
- 2026-09-12T17:19:39+00:00 automated review requested changes: The identity registry and legacy compatibility work, but required project visibility, member-owned API authorization, and authenticated scheduler identity are not implemented end to end. cost=$0.42
- 2026-09-12T17:19:47+00:00 dispatched revise run 20260912T171947Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2862 tokens)
- 2026-09-12T17:24:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-12T17:26:26+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/504: Added concrete project visibility, project-filtered task reads, owned task API authorization, and member-bound scheduler credentials with assignee enforcement. Verified 19 focused tests pass, Ruff and git diff checks are clean, and all changes are committed. cost=$0.91
- 2026-09-12T17:29:09+00:00 automated review requested changes: The multiplayer foundations are incomplete: legacy enrolled workers crash, unassigned work is mutable by any member, and the HTTPS setting does not actually enable encryption. cost=$0.32
- 2026-09-12T17:29:23+00:00 dispatched revise run 20260912T172923Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2878 tokens)
- 2026-09-12T17:33:07+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-12T17:34:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/504: Closed all three multiplayer review gaps and committed the fixes as c1f8d89f. Verified 16 focused membership/host-registry tests pass, Ruff passes across src/tests/scripts, git diff checks are clean, and the worktree is clean. cost=$0.66
- 2026-09-12T17:37:08+00:00 automated review requested changes: Two multiplayer compatibility and usability defects remain despite focused tests and clean lint. cost=$0.31
- 2026-09-12T17:48:28+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-12T17:48:53+00:00 dispatched revise run 20260912T174852Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2894 tokens)
