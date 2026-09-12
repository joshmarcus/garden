---
id: CG-384
title: Show deployed release identity and validate release artifacts
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading:
- pyproject.toml
- src/garden/config.py
branch: garden/cg-384-show-deployed-release-identity-and-validate-rele
pr: https://github.com/joshmarcus/context-garden/pull/407
attempts: 1
last_dispatched_at: '2026-09-09T23:48:52+00:00'
created: '2026-09-07T13:37:37+00:00'
updated: '2026-09-10T01:49:13+00:00'
---

## Goal

Support the operator's adopted versioned-release workflow in the product: make installed identity visible and mechanically prevent mismatched release metadata. See garden docs/release-protocol.md; baseline v0.1.0 preview is published at899b2c0.

## Acceptance criteria

- [ ] Show installed package version and available exact source identity in a small existing status/config surface and CLI. Distinguish installed from latest available release; unknown source remains unknown. No network request on each page or automatic upgrade.
- [ ] Add a manual release validation workflow or script checking package version/tag, exact source commit, required CI evidence, notes and artifact manifest before draft/prerelease publication. Do not auto-publish every merge or bypass review approval. Support GitHub Enterprise host/repository configuration.
- [ ] Document candidate-to-release and rollback steps; do not move published tags or rewind scheduler state. Preserve source installs and honestly label absent prebuilt artifacts.
- [ ] Focused version/manifest tests and one affected UI inspection; exact-head CI. Self-review and repair findings before completion.

## Log

- 2026-09-09T23:25:36+00:00 dispatched work run 20260909T232532Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~14947 tokens)
- 2026-09-09T23:33:52+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:35:08+00:00 opened https://github.com/joshmarcus/context-garden/pull/407 (base main): Added installed-version/source identity to CLI, status, and Configuration; added local-only release candidate validation and release/rollback documentation. Focused tests passed (27), along with Ruff and source compilation. cost=$0.84
- 2026-09-09T23:38:50+00:00 automated review requested changes: Release validation and identity tests pass, but two source-identity defects prevent merge. cost=$0.37
- 2026-09-09T23:39:06+00:00 dispatched revise run 20260909T233902Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~16159 tokens)
- 2026-09-09T23:43:41+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:44:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/407: Corrected the release identity wording and made release candidate manifests require a full canonical commit ID. Focused exact-head validation passed (5 tests), and Ruff is clean. cost=$0.51
- 2026-09-09T23:48:37+00:00 automated review requested changes: Implementation and focused checks are clean, but exact-head CI is still in progress, leaving one frozen criterion unmet. cost=$0.43
- 2026-09-09T23:48:52+00:00 dispatched revise run 20260909T234848Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15980 tokens)
- 2026-09-09T23:53:55+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T23:55:24+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/407: Added the missing architecture-map entries for the release validation modules. Focused architecture, release, and Configuration rendering tests passed; Ruff is clean. The prior exact-head CI failed only on the now-fixed architecture-map omission, and the corrected commit awaits runner publication before fresh CI can run. cost=$0.41
- 2026-09-10T00:03:18+00:00 automated review:  —  cost=$0.62
- 2026-09-10T01:49:13+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/407
