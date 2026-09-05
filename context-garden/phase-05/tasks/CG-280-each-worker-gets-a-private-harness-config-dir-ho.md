---
id: CG-280
title: Each worker gets a private harness config dir holding only credentials, and the fence covers state.json
  and task files
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:05:56+00:00'
---

## Goal

Build CLAUDE_CONFIG_DIR and CODEX_HOME under the scratch home with only the credentials file, refreshed per dispatch; at minimum add settings.json, settings.local.json, CLAUDE.md and config.toml to _fence_guard_targets. On an attributed state.json change restore other tasks' keys from the dispatch snapshot, and apply attribution to live-garden task files instead of exempting them. Security mediums.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
