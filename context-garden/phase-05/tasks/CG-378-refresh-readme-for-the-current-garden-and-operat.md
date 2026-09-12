---
id: CG-378
title: Refresh README for the current garden and operator workflow
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 4
difficulty: hard
reading:
- README.md
- docs/architecture.md
- docs/worker-protocol.md
- docs/roadmap.md
- src/garden/config.py
branch: garden/cg-378-refresh-readme-for-the-current-garden-and-operat
pr: https://github.com/joshmarcus/context-garden/pull/297
harness: codex
model: gpt-6-astra
attempts: 1
last_dispatched_at: '2026-09-07T17:55:53+00:00'
created: '2026-09-07T09:36:56+00:00'
updated: '2026-09-07T20:27:55+00:00'
---

## Goal

Rewrite README as a clear, accurate introduction and practical entry point for a new context-garden user. Owner explicitly requested Astra for this task.

## Context

CG234 updated an earlier README; this is a new accuracy/usability pass against current main. Existing prose includes unconditional workers-never-push and local-check descriptions that need verification against CI offload and worker_push. Explain the product and normal user journey before implementation mechanics. Distinguish the token-free scheduler from a model-powered delegated operator and its cost. Product documentation must describe supported behavior rather than this garden's temporary trial limits or unshipped tickets.

## Acceptance criteria

- [ ] Explain purpose, intended user, context/planning/work/review/merge/retro flow and operator role clearly, matching current code and defaults. Explain human decisions versus delegated operator recovery and that agent usage includes operator cost.
- [ ] Verify installation/onboarding and a minimal end-to-end quickstart against actual CLI help/config/schema; validate safe commands in a disposable fixture. No live garden mutations or unnecessary full local suite for documentation.
- [ ] Correct stale push/check/CI, review/merge, configuration reload, concurrency and deployment claims using current implementation. Clearly distinguish supported remote options from frozen/unimplemented expansion; no claim that pending optional caps or UI changes already shipped.
- [ ] Give concise operating/recovery and operator-handoff guidance with links to maintained detailed docs; avoid copying a sprawling operational ledger or machine-specific settings into README.
- [ ] Check links/paths/commands, self-review for factual accuracy and reader usability, repair findings, and report acceptance evidence. Screenshots are required only if replaced or used to make new visual claims; broad application capture is unnecessary for prose alone.

## Log

- 2026-09-07T09:36:57+00:00 approved (web)
- 2026-09-07T15:47:32+00:00 priority 2 -> 0 (web)
- 2026-09-07T17:55:53+00:00 dispatched work run 20260907T175551Z-work via local [codex model=gpt-6-astra] (fresh session, base main, ~20820 tokens)
- 2026-09-07T18:43:36+00:00 preserved uncommitted worktree changes from run 20260907T175551Z-work outside the PR: `git stash apply cfa873d6dd9ec9f18f6dbc6597b345c725bacf02` in /home/joshua/work/worktrees/CG-378 (garden:CG-378:20260907T175551Z-work:reap)
- 2026-09-07T19:47:17+00:00 check did not run (20260907T194602Z-check): idle 64 min (no output or file change); will retry
- 2026-09-07T19:48:42+00:00 opened https://github.com/joshmarcus/context-garden/pull/297 (base main): Rewrote README around onboarding, the first-PR journey, current scheduler behavior and delegated operator responsibilities and cost. Corrected publication, CI, merge, concurrency, reload and maintenance guidance; final exact-commit CI passed. cost=$21.22
- 2026-09-07T19:51:32+00:00 description rewritten by the reviewer cost=$0.46
- 2026-09-07T20:06:51+00:00 Operator queued required further automated review; owner merge prompt is premature until all approval gates pass. Ownership correction tracked by CG-381.
- 2026-09-07T20:11:04+00:00 automated review produced no verdict (idle 21 min (no output or file change))
- 2026-09-07T20:17:03+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-07T20:17:39+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T20:18:42+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T20:27:55+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/297
