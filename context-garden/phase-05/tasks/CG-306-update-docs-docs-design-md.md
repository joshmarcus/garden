---
id: CG-306
title: 'Update docs: docs/design.md'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading:
- docs/design.md
- docs/roadmap.md
- docs/architecture.md
- docs/worker-protocol.md
discovered_from: kickoff:context-garden/phase-05
created: '2026-09-06T00:07:47+00:00'
updated: '2026-09-06T00:24:06+00:00'
---

## Goal

Update `docs/design.md`'s Non-goals section: it still lists 'automatic merging' as a non-goal, but the loop already automerges. (`docs/roadmap.md` has the same stale claim; that file is out of scope for this task.)

## Context

Raised at the context-garden/phase-05 kickoff; needed by CG-295, CG-265, CG-275.

## Acceptance criteria

- [ ] docs/design.md's Non-goals section no longer lists "automatic merging" as a non-goal; verified by `grep -n "automatic merging" docs/design.md` showing no match under Non-goals.
- [ ] docs/design.md's description of the review/merge loop states that merging is automatic, consistent with the loop behavior described in docs/architecture.md.
- [ ] docs/roadmap.md is left untouched by this task; its own stale non-goal reference, if present, stays out of scope here.
- [ ] The rest of docs/design.md's structure and unrelated non-goals are preserved; the diff is limited to the automatic-merging line(s).

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002118Z-edit) cost=$0.07
- 2026-09-06T00:24:06+00:00 approved (cli)
