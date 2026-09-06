---
id: CG-349
title: Centralize editable configuration metadata and enforce project overrides and locks
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 2
difficulty: hard
reading:
- context-garden/phase-06/specs/web-configuration.md
created: '2026-09-06T16:39:23+00:00'
updated: '2026-09-06T16:39:23+00:00'
---

## Goal and evidence

Implement the metadata, scope and mutation-policy foundation in the shared web-configuration spec. Inventory all options currently displayed by Configuration. Preserve existing precedence and fence behavior; support explicit project value overrides, edit locks and enforced values with provenance. Enforce direct and indirect edits across API/CLI/profile/global/reset/reload paths, project isolation, atomic validation, stale-write rejection and redacted auditing. A normal edit must not remove its own lock. Describe global-only and derived settings honestly. Evidence must prove these policies at the shared backend boundary, not only through disabled UI controls.

## Provenance

Owner request 2026-09-06: editable web configuration with explanations and project policies that prohibit editing selected options. Draft under the existing phase-06 freeze.
