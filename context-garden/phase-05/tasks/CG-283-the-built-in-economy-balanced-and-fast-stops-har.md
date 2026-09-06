---
id: CG-283
title: The built-in economy, balanced and fast stops hardcode Claude model ids and mode
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
harness: codex
discovered_from: persona:user:context-garden/phase-04
created: '2026-09-05T23:58:16+00:00'
updated: '2026-09-06T00:50:21+00:00'
---

## Goal

Key a stop's models per harness (or by the harness's own tier map) and only apply a stop's models to a harness it names; say so in the rail meaning line.

## Context

Raised by the user persona review (operating profiles). persona:user:context-garden/phase-04.

## Scope note (operator, 2026-09-06)

This task owns the stops-name-a-tier-per-harness mechanism (the CG-255 line folded into CG-296 keeps only the copy half: no task ids in user-facing text).

## Suggestions

- [ ] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-272 (renumbered by the operator: two reconcile runs drew ids from one counter)
