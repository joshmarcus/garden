---
id: CG-373
title: Bound rebase prompts and recover oversized generated-file conflicts
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-07T09:14:33+00:00'
updated: '2026-09-07T09:14:34+00:00'
---

## Goal

Bound rebase prompts and recover oversized generated-file conflicts.

## Context

CG294 twice sent ~1.595 million characters against a1048576 limit because docs/design/snapshot.json dominated a conflict-only brief. Owner requested prevention tickets after resolving the human queue.

## Acceptance criteria

- [ ] Budget serialized prompt size before harness invocation; oversized inputs never reach turn/start.
- [ ] Represent large generated-file conflicts with bounded summaries and artifact paths; preserve original blobs and salvage stashes.
- [ ] Recover this deterministic input failure without duplicate retries or asking an owner to resolve generated data; cover a >1MiB conflict fixture.

## Log

- 2026-09-07T09:14:34+00:00 approved (web)
