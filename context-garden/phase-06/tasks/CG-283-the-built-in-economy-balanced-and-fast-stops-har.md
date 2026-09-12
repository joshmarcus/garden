---
id: CG-283
title: The built-in economy, balanced and fast stops hardcode Claude model ids and mode
status: cancelled
product: context-garden
phase: phase-06
depends_on: []
priority: 2
order: 0
difficulty: medium
reading:
- src/garden/profiles.py
- src/garden/config.py
- src/garden/web/templates/base.html
harness: codex
discovered_from: persona:user:context-garden/phase-04
created: '2026-09-05T23:58:16+00:00'
updated: '2026-09-07T21:37:02+00:00'
---

## Goal

Key a stop's models per harness (or by the harness's own tier map) and only apply a stop's models to a harness it names; say so in the rail meaning line.

## Context

Raised by the user persona review (operating profiles). persona:user:context-garden/phase-04.

## Scope note (operator, 2026-09-06)

This task owns the stops-name-a-tier-per-harness mechanism (the CG-255 line folded into CG-296 keeps only the copy half: no task ids in user-facing text).

## Acceptance criteria

- [ ] The built-in economy, balanced, and fast stops no longer hardcode a single Claude model id or mode; each stop's models are keyed per harness or delegate to that harness's own tier map.
- [ ] A stop applies its named models only to the harness(es) it names; a harness not named by the stop falls back to its own tier map or default, not the stop's Claude-specific values.
- [ ] The rail's meaning line states that stop models are keyed per harness.
- [ ] Configuring a stop with models for one harness and none for another produces correct per-harness behavior at runtime, not a crash or silent Claude-only fallback.
- [ ] A test in the stops test suite asserts that a stop's models apply only to harnesses it names and that an unnamed harness uses its own tier map instead of the stop's hardcoded values.

## Out of scope

Renaming or restructuring tasks beyond this mechanism; task-id references in user-facing copy (handled under CG-296).

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-272 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005021Z-edit) cost=$0.09
- 2026-09-06T00:52:23+00:00 approved (cli)
- 2026-09-06T13:13:11+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:27+00:00 reset to ready by hand
- 2026-09-06T13:45:07+00:00 Owner-directed feature deferral until phase-05 stabilization is demonstrated. Preserve existing branch and PR; no further implementation or merge before the gate passes.
- 2026-09-06T13:45:08+00:00 moved from context-garden/phase-05 to context-garden/phase-06
- 2026-09-07T20:10:03+00:00 Owner explicitly unfroze phase06 and authorized task approval on 2026-09-07; this supersedes historical feature-freeze notes. Preserve existing implementation/PR and normal review/resource gates.
- 2026-09-07T20:10:03+00:00 approved (owner-unfreeze-phase06)
- 2026-09-07T21:37:02+00:00 cancelled (web)
