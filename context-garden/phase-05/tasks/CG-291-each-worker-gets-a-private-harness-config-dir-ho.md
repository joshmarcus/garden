---
id: CG-291
title: Each worker gets a private harness config dir holding only credentials, and the fence covers state.json
  and task files
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-05T23:58:18+00:00'
discovered_from: retro:context-garden/phase-04
---

## Goal

Build CLAUDE_CONFIG_DIR and CODEX_HOME under the scratch home with only the credentials file, refreshed per dispatch; at minimum add settings.json, settings.local.json, CLAUDE.md and config.toml to _fence_guard_targets. On an attributed state.json change restore other tasks' keys from the dispatch snapshot, and apply attribution to live-garden task files instead of exempting them. Security mediums.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

Folded in from CG-246 (astra's blocker, cancelled as the duplicate): write separation also covers sibling run outputs under .garden/runs and the audit evidence the fence records; a worker's shell redirect into any of these is attributed at reap and restored, like state.json.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-280 (renumbered by the operator: two reconcile runs drew ids from one counter)
