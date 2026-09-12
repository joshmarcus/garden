---
id: CG-635
title: Make local multiplayer startup and unassigned idle state explicit
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-632
  after: merge
- id: CG-633
  after: merge
priority: 2
difficulty: medium
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/cli/__init__.py
- src/garden/web/app.py
- src/garden/config.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:14+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Provide a clear local setup, serve and watch experience for assigned members, unassigned members and viewers.

## Context and scope

Use the established CLI and service entry points. A user should be able to start the application without acquiring work. This is product setup behavior; do not activate multiplayer in the live operator garden while implementing it.

## Acceptance criteria

- [ ] Provide supported enrollment/connect and identity/work-scope inspection commands, plus actionable diagnostics for missing credentials, no assignment, expired credentials, disconnected coordinator and incompatible protocol.
- [ ] Starting UI and watch for a member without assignment succeeds with a visible No work assignment state and zero work/resource effects. There is no inferred identity or first-project/phase fallback. Starting a viewer never launches scheduler, worker ingress or maintenance helpers.
- [ ] Show current identity and execution project/phase separately from the viewing project; provide explicit permitted assignment/request controls without automatically claiming unowned issues.
- [ ] Validate fresh local setup, repeated restarts, unassigned ticks, viewer startup and reconnect using disposable configuration, and document the actual CLI commands rather than proposed examples that do not run.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
