---
id: CG-384
title: Show deployed release identity and validate release artifacts
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading:
- pyproject.toml
- src/garden/config.py
created: '2026-09-07T13:37:37+00:00'
updated: '2026-09-07T13:37:37+00:00'
---

## Goal

Support the operator's adopted versioned-release workflow in the product: make installed identity visible and mechanically prevent mismatched release metadata. See garden docs/release-protocol.md; baseline v0.1.0 preview is published at899b2c0.

## Acceptance criteria

- [ ] Show installed package version and available exact source identity in a small existing status/config surface and CLI. Distinguish installed from latest available release; unknown source remains unknown. No network request on each page or automatic upgrade.
- [ ] Add a manual release validation workflow or script checking package version/tag, exact source commit, required CI evidence, notes and artifact manifest before draft/prerelease publication. Do not auto-publish every merge or bypass review approval. Support GitHub Enterprise host/repository configuration.
- [ ] Document candidate-to-release and rollback steps; do not move published tags or rewind scheduler state. Preserve source installs and honestly label absent prebuilt artifacts.
- [ ] Focused version/manifest tests and one affected UI inspection; exact-head CI. Self-review and repair findings before completion.
