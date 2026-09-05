---
id: CG-194
title: Workers get no HOME, retry_command comes only from config, and the fence hash-checks garden.yaml
  and state.json
status: draft
product: context-garden
phase: phase-04
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-03
created: '2026-09-05T10:26:55+00:00'
updated: '2026-09-05T10:26:55+00:00'
---

## Goal

**User value:** a worker or a branch's test suite cannot read the operator's gh token, cannot forge an approve verdict into .garden/state.json, and cannot run a shell command through a check's JSON output; the docs say exactly what is and is not isolated.

**Why now:** the security persona verified all three on the phase-03 build and with automerge on they chain into a self-approved merge.

**Size:** medium. **Depends on:** CG-164 and CG-165 (merged) for the shared allowlist. Also hold automerge when a diff touches garden*.yaml, **/tasks/, .github/ or principles/, and require a loopback Host on POSTs.

## Context

Proposed at the context-garden/phase-03 retro. Phase 03 claimed trust at the edges; the verified gaps are small, local fixes that make the claim true.
