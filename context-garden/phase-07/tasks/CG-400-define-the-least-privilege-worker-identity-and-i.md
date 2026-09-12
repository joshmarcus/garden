---
id: CG-400
title: Define the least-privilege worker identity and internal tooling policy
status: cancelled
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
created: '2026-09-07T19:56:16+00:00'
updated: '2026-09-08T02:39:53+00:00'
---

## Goal

Record an explicit policy decision before widening worker configuration or tool access. Seek Quality and Security/Privacy review; no automatic access expansion.

## Acceptance criteria

- [ ] Define allowed tools, operations, environments, identity provenance, credential scope and lifetime, revocation and local audit boundaries. Identify unresolved human decisions concretely.
- [ ] Require synthetic or approved sanitized evaluation data, preserve authorization failures and environment/host-class restrictions, and prohibit autonomous production writes or deployment.
- [ ] Distinguish delegated personal access from an automation identity; no impersonation assumption. Publish only generic policy structure and keep deployment-specific decisions private.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G8 policy prerequisite. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T02:39:53+00:00 Cancelled at owner request; removed CG-400 as a dependency from all tasks.
