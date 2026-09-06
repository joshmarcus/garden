---
id: CG-305
title: 'Update docs: docs/worker-protocol.md'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 3
difficulty: easy
reading:
- docs/worker-protocol.md
- docs/architecture.md
- docs/design.md
discovered_from: kickoff:context-garden/phase-05
created: '2026-09-06T00:07:47+00:00'
updated: '2026-09-06T00:24:06+00:00'
---

## Goal

Update `docs/worker-protocol.md` so it matches current behavior: line 68 says 'Remote runners skip this; the host makes its own,' but `runner: remote` and the claim/heartbeat/finish flow do not exist yet. Reconcile this dangling forward reference against CG-216.

## Context

Raised at the context-garden/phase-05 kickoff; needed by CG-216.

## Acceptance criteria

- [ ] Line 68's claim ('Remote runners skip this; the host makes its own') is removed or rewritten so it no longer describes a claim/heartbeat/finish flow that doesn't exist in the code.
- [ ] The doc does not imply `runner: remote` is implemented today; it either omits the remote-runner flow or marks it explicitly as forthcoming.
- [ ] The doc points readers to CG-216 for the remote-runner flow instead of leaving a dangling, unexplained forward reference.
- [ ] Verified by: `grep -n "Remote runners" docs/worker-protocol.md` shows wording consistent with the current implementation.

## Out of scope

Implementing `runner: remote` or the claim/heartbeat/finish flow itself — that is CG-216's work.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002117Z-edit) cost=$0.08
- 2026-09-06T00:24:06+00:00 approved (cli)
