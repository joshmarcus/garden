---
id: CG-304
title: 'Update docs: docs/architecture.md'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading:
- docs/architecture.md
- src/garden/kickoff.py
- src/garden/scheduler/kickoff.py
- src/garden/profiles.py
- src/garden/runner/ssh.py
- src/garden/runner/manual.py
- src/garden/web/pages/api.py
discovered_from: kickoff:context-garden/phase-05
created: '2026-09-06T00:07:47+00:00'
updated: '2026-09-06T00:25:04+00:00'
---

## Goal

Update `docs/architecture.md`'s module map to add kickoff.py, scheduler/kickoff.py, profiles.py, runner/ssh.py, runner/manual.py and web/pages/api.py, and to reflect the remote runner and runs API added by CG-216.

## Context

Raised at the context-garden/phase-05 kickoff; needed by CG-216, CG-295, CG-275.

## Acceptance criteria

- [ ] Module map in docs/architecture.md lists kickoff.py, scheduler/kickoff.py, profiles.py, runner/ssh.py and runner/manual.py, each with a one-line description
- [ ] Module map lists web/pages/api.py and the remote runner and runs API surface added by CG-216
- [ ] Every path named in the module map exists in the product checkout, confirmed by diffing the map against the actual file tree (e.g. `git ls-files`)
- [ ] No module map entries reference files that have since been removed or renamed
- [ ] docs/architecture.md still renders correctly (headings and links intact) after the edit

## Out of scope

- Any documentation file other than docs/architecture.md
- Describing CG-216's remote runner/runs API design beyond naming it in the module map

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002116Z-edit) cost=$0.06
- 2026-09-06T00:25:04+00:00 approved (cli)
