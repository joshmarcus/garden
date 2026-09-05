---
id: CG-284
title: 'Docs match the mechanism: the scaffolded operate skill, design.md and roadmap.md non-goals, and
  the architecture module map'
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:05:56+00:00'
updated: '2026-09-05T23:05:56+00:00'
---

## Goal

scaffold.py's skill template says garden.yaml reloads each tick and only RESTART_KEYS need a restart; design.md and roadmap.md drop automatic merging from non-goals; the architecture map adds kickoff.py, scheduler/kickoff.py, profiles.py, inbox.py and web/pages/costs with a test that every module appears, plus the restart-recovery timing note CG-198 asked for. Also remove the stale 'once CG-207 lands' comment from the live garden.yaml.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.
