---
id: CG-517
title: Separate authenticated worker ingress from operator control access
status: done
product: context-garden
phase: phase-06
depends_on:
- CG-216
- CG-398
priority: 0
difficulty: hard
reading:
- src/garden/web/app.py
- src/garden/web/trust.py
- src/garden/web/pages/api.py
- src/garden/remote_worker.py
- docs/worker-protocol.md
- context-garden/phase-06/specs/context-garden-stripe-environment.md
branch: garden/cg-517-separate-authenticated-worker-ingress-from-opera
pr: https://github.com/joshmarcus/context-garden/pull/430
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T13:48:42+00:00'
created: '2026-09-10T11:18:51+00:00'
updated: '2026-09-10T14:01:49+00:00'
---

## Goal

Expose the authenticated worker protocol without exposing operator controls to worker-accessible networks. Require a separate operator authentication and authorization boundary for every non-worker control route, with explicit deployment diagnostics and no trust inferred from a missing Origin header.

## Context

CG-216 authenticates claim, heartbeat and finish requests, and CG-398 validates a human-gated profile. Current shared application routing still needs an enforceable boundary between worker credentials and operator authority.

## Acceptance criteria

- [ ] Classify worker protocol, read-only public, operator read and operator mutation routes in one auditable policy; startup fails when a configured exposure has unclassified routes.
- [ ] Worker bearer credentials authorize only their host-bound protocol operations. They never authorize operator pages, APIs, task decisions, configuration, merges, maintenance or deployment actions.
- [ ] Require configured operator authentication for operator routes on non-loopback or worker-reachable listeners. Missing Origin, forwarded headers or direct API access cannot bypass it; trusted-proxy handling is explicit and bounded.
- [ ] Keep browser CSRF/origin protection and add clear 401/403 diagnostics without disclosing identities or policy data. Existing local-only development remains explicit and safe.
- [ ] Disposable network fixtures cover unauthenticated direct requests, worker tokens on operator routes, valid operator access, proxy-header spoofing, route additions and local-only mode. No live access policy is changed by the tests.

enterprise_capability_key: enterprise-operator-worker-network-boundary

## Log

- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:37:02+00:00 dispatched work run 20260910T113702Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~22967 tokens)
- 2026-09-10T11:53:33+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:55:17+00:00 opened https://github.com/joshmarcus/context-garden/pull/430 (base main): Separated worker ingress from operator access with a centralized, startup-audited route policy. Exposed listeners now require distinct operator bearer authentication while worker credentials remain limited to host-bound protocol operations; final-head web and remote-worker suites passed 236 tests with 4 deselected, and repository lint passed. cost=$1.88
- 2026-09-10T11:59:45+00:00 automated review: approve — The centralized route policy and middleware enforce the requested worker/operator boundary without weakening local-only behavior or origin checks. cost=$0.33
- 2026-09-10T13:36:59+00:00 triage: changes requested by hand: Current exact-head CI34473852879 and34473706012 fail because the architecture map omits the new web/access.py module; on
- 2026-09-10T13:38:43+00:00 dispatched revise run 20260910T133843Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~23897 tokens)
- 2026-09-10T13:46:57+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:48:23+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/430: Documented the new web access-policy module and repaired the disposable auto-upgrade fixture so its synthetic route satisfies the fail-closed startup audit. The final focused selection passed 9 tests in 44.71 seconds, repository lint passed, and the correction is committed at 14bc43dc. cost=$0.74
- 2026-09-10T13:48:32+00:00 PR conflicts with main; rebase onto main conflicts (docs/architecture.md); a rebase agent will resolve it
- 2026-09-10T13:48:42+00:00 dispatched rebase run 20260910T134842Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1523 tokens)
- 2026-09-10T13:51:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/430: Rebased CG-517 onto origin/main and merged the architecture module-map conflict. cost=$0.01
- 2026-09-10T13:53:53+00:00 automated review: approve — The centralized route policy and middleware correctly separate worker ingress from operator access while preserving explicit loopback development behavior and origin protection. cost=$0.32
- 2026-09-10T14:00:22+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T14:01:49+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/430
