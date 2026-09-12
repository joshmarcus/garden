---
id: CG-637
title: Personalize Inbox and authorize issue actions for the current assignee
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-633
  after: merge
- id: CG-636
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/web/pages/inbox.py
- src/garden/web/actions/tasks.py
- src/garden/web/actions/decisions.py
- src/garden/web/app.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:15+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Give each person a Mine Inbox and reject stale or unauthorized actions even when sent directly to an endpoint.

## Context and scope

Reuse existing Inbox ownership filtering, but taskless/global cards require explicit recipients. Team visibility and project focus do not authorize operating someone else's work. Phase decisions use explicit phase-operation authority.

## Acceptance criteria

- [ ] Default Mine to effectively assigned issues and decisions/questions addressed to the caller, narrowed by the selected project. Keep owned issues outside the active execution phase visible without making them runnable. Provide a separate authorized team overview and an administration Inbox for global decisions.
- [ ] Use shared authorization and current assignment/task versions for every issue and decision action, including answer, approve, resume, retry, cancel and merge routes. Reject stale pages after reassignment and preserve idempotent retries, attribution and existing human-review gates.
- [ ] Keep counts, badges, notifications and SSE recipient/project scopes consistent with Inbox rows. Remove implicit inclusion of all taskless cards; public and private viewers receive only their allowed read projections.
- [ ] Validate two members with distinct addressed questions, stale direct actions after handoff, administrative reassignment and a member with no assignment. Inspect the affected Inbox behavior and preserve legacy single-user handling.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
