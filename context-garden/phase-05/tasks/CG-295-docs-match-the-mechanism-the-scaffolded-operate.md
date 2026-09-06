---
id: CG-295
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
created: '2026-09-05T23:58:19+00:00'
updated: '2026-09-06T00:50:23+00:00'
---

## Goal

scaffold.py's skill template says garden.yaml reloads each tick and only RESTART_KEYS need a restart; design.md and roadmap.md drop automatic merging from non-goals; the architecture map adds kickoff.py, scheduler/kickoff.py, profiles.py, inbox.py and web/pages/costs with a test that every module appears, plus the restart-recovery timing note CG-198 asked for. Also remove the stale 'once CG-207 lands' comment from the live garden.yaml.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Suggestions

- [ ] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-284 (renumbered by the operator: two reconcile runs drew ids from one counter)
