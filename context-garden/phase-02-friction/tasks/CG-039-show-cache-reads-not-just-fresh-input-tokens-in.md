---
id: CG-039
title: Show cache reads, not just fresh input tokens, in runs and usage
status: failed
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/cli.py
- src/garden/runs.py
- src/garden/web/templates/phase.html
branch: garden/cg-039-show-cache-reads-not-just-fresh-input-tokens-in
discovered_from: CG-027
attempts: 2
last_dispatched_at: '2026-09-04T17:30:41+00:00'
created: '2026-09-04T17:03:10+00:00'
updated: '2026-09-04T17:37:41+00:00'
---

## Goal

The token columns tell the truth about how much context a run read.

## Context

On CG-027 `garden runs CG-012` showed 481 input tokens for a run whose cache reads were 3.4M and whose cost was $0.58; the phase page's tokens column is the same pair. The `in` number is the uncached remainder, which is the least informative of the three. Show total context read (input + cache read + cache creation) with cache reads beside it, in `garden runs`, `garden usage`, the Runs page and the phase table.

## Acceptance criteria

- [ ] every table that shows input tokens shows the total context read, with cache reads visible.
- [ ] the column titles say which is which.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:10+00:00 discovered by CG-027
- 2026-09-04T17:23:53+00:00 approved (web)
- 2026-09-04T17:26:18+00:00 dispatched work run 20260904T172617Z-work via local [claude model=haiku] (fresh session, base main, ~5595 tokens)
- 2026-09-04T17:30:33+00:00 no active run found; back to ready
- 2026-09-04T17:30:41+00:00 dispatched work run 20260904T173041Z-work via local [claude model=haiku] (fresh session, base main, ~5647 tokens)
- 2026-09-04T17:37:41+00:00 attempt 2 failed: worker exited 1: worker error: error_max_turns; giving up
