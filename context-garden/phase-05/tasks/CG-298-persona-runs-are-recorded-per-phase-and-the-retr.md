---
id: CG-298
title: Persona runs are recorded per phase and the retro validates the run id it reads
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 4
difficulty: easy
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:20+00:00'
updated: '2026-09-06T00:50:27+00:00'
---

## Goal

dispatch_aux keys persona runs by phase rather than the shared _persona id; the retro validates the footer id against a safe character class and requires the resolved path under runs.dir. Also give discovered items structured file and error fields so dedup compares fields, not regexes.

## Context

A follow-up carried into phase-05 by the context-garden/phase-04 retro verdict.

## Suggestions

- [ ] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-287 (renumbered by the operator: two reconcile runs drew ids from one counter)
