---
id: CG-277
title: Live config reload holds while any in-flight worker's fence manifest disagrees with garden.yaml
  on disk
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:05:56+00:00'
---

## Goal

In reload_config_if_changed, compare the file with each in-flight run's fence_guard.json and hold the reload while any disagrees, logging that the change waits for those runs to reap; the reap releases or reverts it. Also run notify.command through scrubbed_env with GARDEN_* added explicitly. Security high 3 of the phase-04 review.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
