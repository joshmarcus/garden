---
id: CG-636
title: Focus all garden views with a shared project selector
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-632
  after: merge
- id: CG-630
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/web/common.py
- src/garden/web/app.py
- src/garden/web/pages/inbox.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:15+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Add the upper-right project selector and carry its validated scope consistently through every normal view and data route.

## Context and scope

The selector changes presentation only. Use the existing product identity. Keep member permissions, saved viewing preference and scheduler assignment independent; a team overview is not execution authority.

## Acceptance criteria

- [ ] Add an accessible shared-header selector with authorized projects and explicit All authorized projects. Prefer an authorized URL scope, then the per-user/browser preference, then the assigned project or neutral overview. Handle empty membership and revoked/invalid explicit projects without a broader fallback.
- [ ] Apply one scope resolver to Now, Board, Inbox, tasks, phases, graph, PRs, runs, costs, docs, search and exports, including JSON, HTMX fragments and SSE updates. Preserve selection in navigation and browser history; restricted global admin surfaces remain explicitly labelled.
- [ ] Keep row counts, badges, links and project costs consistent with the selected scope. Cross-project dependency links respect visibility and use opaque blockers when necessary. Avoid exposing unauthorized records through aggregates or streams.
- [ ] Verify navigation and selection across the affected UI with a suitable interaction check and focused route checks. Changing projects must leave execution assignment, claims and task state unchanged; include direct URLs and revoked visibility.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
