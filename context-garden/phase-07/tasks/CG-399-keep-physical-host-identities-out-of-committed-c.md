---
id: CG-399
title: Keep physical host identities out of committed context and public evidence
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-399-keep-physical-host-identities-out-of-committed-c
pr: https://github.com/joshmarcus/context-garden/pull/310
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T12:03:27+00:00'
created: '2026-09-07T19:56:16+00:00'
updated: '2026-09-08T12:50:40+00:00'
---

## Goal

Enforce logical run host aliases and local-only connection resolution; audit configuration and evidence surfaces before any real remote dispatch.

## Acceptance criteria

- [ ] Doctor flags tracked configuration containing concrete connection targets using host-field-aware checks; permit approved logical aliases and ignored local overlays.
- [ ] Dispatch logs, task files, briefs, notifications and exported reports contain aliases, not physical connection identifiers or credential material.
- [ ] Document the retention/access boundary for local command scripts, run records and event logs; test sentinels across surfaces without publishing real identifiers.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G10. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T12:02:32+00:00 Owner four-host rollout verified; route this eligible Phase07 P0 task to the authenticated AWS pool while retaining two local resource slots.
- 2026-09-08T12:03:27+00:00 dispatched work run 20260908T120326Z-work-2 via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~8335 tokens)
- 2026-09-08T12:34:53+00:00 opened https://github.com/joshmarcus/context-garden/pull/310 (base main): Added tracked-config host-target auditing, alias and credential scrubbing for shared context, and documented the local retention boundary. Final commit bcf25cf7b762455a4d83b6a13cb155312d63674c passed exact-head GitHub Actions at https://github.com/joshmarcus/context-garden/actions/runs/34225793508. cost=$2.76
- 2026-09-08T12:42:43+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/310
- 2026-09-08T12:50:40+00:00 automated review could not start: CG-399 is done: #310 was merged at 12:42:43
