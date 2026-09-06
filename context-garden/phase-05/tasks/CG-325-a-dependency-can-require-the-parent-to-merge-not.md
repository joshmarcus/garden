---
id: CG-325
title: 'A dependency can require the parent to merge, not only to have a PR: depends_on entries take after:
  merge, the default for a design-to-build pair'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/graph.py
- src/garden/model.py
- src/garden/scheduler/dispatch.py
- docs/design.md
- tests/test_graph.py
created: '2026-09-06T04:03:15+00:00'
updated: '2026-09-06T13:14:36+00:00'
---

## Goal

A task can say that it needs its dependency merged, not merely under review. `depends_on` accepts either an id (today's meaning: the child may start stacked on the parent's open PR) or `{id: CG-307, after: merge}`, which keeps the child blocked until the parent's commits are on the base branch. A task whose parent is a design, spec or document task defaults to `after: merge`, since the child builds from the document's content and a document under revision is not a stable base. The task page and the graph show which rule applies.

## Context

Owner, 2026-09-06 04:05Z: "Why is Now 1 design and build running at the same time? Isn't build dependent on design?" The build (CG-308) depends on the design (CG-307); the scheduler dispatched the build at 02:58Z stacked on the design's open PR, which is the stacking rule made for code-on-code chains. The design then took a revise round for six persona findings while the build was already running from the earlier version. Stacking is right when the child needs the parent's code; it is wrong when the child needs the parent's final words.

## Acceptance criteria

- [ ] `depends_on` parses both forms; `after: merge` keeps the child blocked until the parent is done (commits on base), while the bare form keeps today's stacking; `garden validate` reports a malformed entry.
- [ ] A parent whose title or body marks it as a design, spec or document task (a `kind: design` frontmatter field, set by the planner and by hand) makes `after: merge` the default for its children unless overridden.
- [ ] The task page and `garden graph` show "after merge" against such a dependency; tests cover both forms, the default, and dispatch honouring them.

## Log
- 2026-09-06T04:03:15+00:00 approved (cli)
- 2026-09-06T13:13:21+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:36+00:00 reset to ready by hand
