---
id: CG-298
title: Persona runs are recorded per phase and the retro validates the run id it reads
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 4
difficulty: medium
reading: []
discovered_from: retro:context-garden/phase-04
created: '2026-09-05T23:58:20+00:00'
updated: '2026-09-06T00:52:24+00:00'
---

## Goal

dispatch_aux keys persona runs by phase rather than the shared _persona id; the retro validates the footer id against a safe character class and requires the resolved path under runs.dir. Also give discovered items structured file and error fields so dedup compares fields, not regexes.

## Context

Follow-up from the context-garden/phase-04 retro verdict.

## Acceptance criteria

- [ ] dispatch_aux persists persona run records keyed by phase, not the shared `_persona` id, so runs from different phases never collide or overwrite each other
- [ ] The retro rejects a footer run id containing any character outside a safe character class before it is used to build a path
- [ ] The retro rejects a run id whose resolved path falls outside `runs.dir`, even when the character class check passes
- [ ] Discovered items carry structured `file` and `error` fields, and dedup compares those fields directly instead of extracting them from text via regex
- [ ] A retro test asserts that both an invalid-character run id and one resolving outside `runs.dir` are rejected

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-287 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005028Z-edit) cost=$0.09
- 2026-09-06T00:52:24+00:00 approved (cli)
