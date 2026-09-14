---
id: CG-704
title: 'Every Git refresh walks and decodes the entire state history even when its head '
status: draft
product: context-garden
phase: phase-11
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: persona:staff-engineer:context-garden/phase-10
created: '2026-09-14T00:06:03+00:00'
updated: '2026-09-14T00:06:03+00:00'
---

## Goal

In GitStateStore._fetch/_validate_history, cache validated immutable commit identities and validate only descendants of the last verified head while retaining rewrite detection. Batch Git object reads and define a retention/checkpoint strategy that preserves replay resolution. Add deterministic command-count tests for unchanged heads and one-commit advancement; measure larger histories separately under the stress policy.

## Context

Raised by the staff-engineer persona review (Coordination history growth). persona:staff-engineer:context-garden/phase-10.
