---
id: CG-065
title: 'Plates and plants: positional assignment, invalid --plant, --out, atomic publish, one-line source
  rows'
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 3
difficulty: easy
reading:
- src/garden/store.py
- src/garden/scaffold.py
- src/garden/platefetch.py
- src/garden/cli.py
created: '2026-09-04T18:35:08+00:00'
updated: '2026-09-04T18:41:38+00:00'
---

## Goal

Five small defects in the plates and plants code, all raised by Codex reviews on PRs #2, #3 and #5 and never acted on because bot comments were filtered at the time.

## Context

1. `store.py` (PR #2): when any phase has an explicit `plant`, a phase without one gets the first globally unused plant instead of its positional plant, so one override changes other phases' emblems. Use `PLANTS[i % len(PLANTS)]` for metadata-free phases; keep next-unused for scaffolding new phases.
2. `scaffold.py` (PR #2): a mistyped `--plant fernn` silently falls back to an automatic plant and a rerun does not repair it. Reject an unknown explicit plant before creating the scaffold.
3. `cli.py` (PR #3): `garden plants --fetch --out DIR` reports scans in DIR, but `garden serve` only reads the package's `static/plates`, so custom-output plates are never shown. Either pass the directory to `serve` (option or config) or document `--out` as export only.
4. `platefetch.py` (PR #3): a failure mid-loop leaves earlier plates visible without `SOURCES.md` provenance, or a rerun pairs new scans with a stale manifest. Stage into a temporary directory and publish atomically, or update the manifest per plate.
5. `sources_markdown()` (PR #5): an `Artist` field containing a newline breaks the markdown table (the snapdragon row). Collapse whitespace and test multiline metadata.

## Acceptance criteria

- [ ] each of the five has a test that fails before and passes after.
- [ ] the checked-in `SOURCES.md` renders as one table.

## Log

- 2026-09-04T18:41:38+00:00 approved
