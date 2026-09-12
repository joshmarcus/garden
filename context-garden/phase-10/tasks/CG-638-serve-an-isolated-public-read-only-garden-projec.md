---
id: CG-638
title: Serve an isolated public read-only garden projection
status: ready
product: context-garden
phase: phase-10
depends_on:
- id: CG-629
  after: merge
- id: CG-631
  after: merge
- id: CG-636
  after: merge
- id: CG-637
  after: merge
priority: 2
difficulty: hard
reading:
- context-garden/specs/multiplayer.md
- context-garden/phase-10/goals.md
- src/garden/web/app.py
- src/garden/web/common.py
runner: remote
discovered_from: 'owner: true multiplayer specification and task breakdown; each person runs locally;
  planning only'
created: '2026-09-11T20:19:16+00:00'
updated: '2026-09-12T16:55:55+00:00'
---

## Goal

Support viewer-only serving with a default-empty publication allowlist and no access to private control state or execution authority.

## Context and scope

Member-readable routes are not automatically public. Build a dedicated approved projection and positive read-route policy. A public process must be deployable using just that projection, without the private checkout, control store or operator secrets.

## Acceptance criteria

- [ ] Provide explicit project/field publication settings and a narrow initial projection for approved project/phase/task summaries and safe dependencies. Require explicit inclusion of free-form content; omit raw logs, transcripts, arbitrary files, private identities/links/paths, configuration and detailed costs by default.
- [ ] Serve the projection in viewer mode without constructing an enabled scheduler or starting watch, ingress, workers, upgrades or cleanup. Restrict the process to approved data and verify that all rendered content and file paths respect the projection boundary.
- [ ] Allowlist read pages, APIs, fragments, streams and exports. Reject mutation and elevation attempts through direct requests, alternate methods including HEAD/OPTIONS, aliases, query identity changes and traversal. Audit read handlers for incidental control writes.
- [ ] Apply revocation to subsequent responses, caches and existing subscriptions, and enforce private-viewer membership separately from anonymous publication. Demonstrate that a public reader cannot reach unpublished projects or private fields through counts, search, downloads or SSE.
- [ ] Validate an isolated disposable viewer process and direct authorization checks without deploying a public production site. Preserve useful empty, unavailable and revoked-publication states.

## Authorization and boundaries

Drafted from the owner's September 11 request for a true multiplayer specification and task breakdown. The owner selected each person running their UI and scheduler locally. Owner explicitly released Phase 10 implementation on September12; execute through normal dependencies, independent review and exact-head CI. Reuse the current accepted source and completed CG-414 ownership metadata. Existing single-user behavior stays supported until explicit multiplayer enrollment. Keep ordinary source review and exact-head CI gates. No production activation, public deployment, cloud resource creation, paid experiment or change to existing holds is authorized by this plan. Suggested source paths are starting points; choose implementation details and proportionate checks that satisfy the stated outcomes.

## Log

- 2026-09-12T16:55:55+00:00 approved (owner September12 request to launch true multiplayer with two remote workers)
