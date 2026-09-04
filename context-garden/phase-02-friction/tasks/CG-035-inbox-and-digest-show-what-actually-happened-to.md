---
id: CG-035
title: Inbox and digest show what actually happened to a task
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: medium
reading:
- src/garden/inbox.py
- src/garden/cli.py
branch: garden/cg-035-inbox-and-digest-show-what-actually-happened-to
pr: https://github.com/joshmarcus/context-garden/pull/18
discovered_from: CG-027
attempts: 1
last_dispatched_at: '2026-09-04T17:24:46+00:00'
created: '2026-09-04T17:03:09+00:00'
updated: '2026-09-04T17:42:29+00:00'
---

## Goal

A draft that has a history shows it, and a failed attempt is visible somewhere a person looks, before the second one fails.

## Context

On CG-027: CG-008 had been forced back to draft after a failed attempt on another machine, and the Inbox showed it as "draft seed · 39m · planned, not yet approved", a stock phrase from `inbox.py` for any draft without `discovered_from`. The age is time since `updated`, which `set-status` touches. CG-012's first attempt failed (max turns) and was redispatched in the same tick; the Inbox listed it nowhere and `garden digest` said "nothing notable" beside "$0.58 spent". Show the last log line and the attempt count on draft and ready cards; add a "recent failures" group or line to the Inbox and count `run_finished` with status error as notable in the digest.

## Acceptance criteria

- [ ] a draft card shows its last log line and `attempts` when either exists.
- [ ] a failed attempt that was retried appears on the Inbox and in the digest.
- [ ] tests for both.

## Provenance

Discovered by CG-027 (First live run of the loop on itself) during run `20260904T160635Z-work`.

## Log

- 2026-09-04T17:03:09+00:00 discovered by CG-027
- 2026-09-04T17:23:52+00:00 approved (web)
- 2026-09-04T17:24:46+00:00 dispatched work run 20260904T172446Z-work via local [claude model=sonnet] (fresh session, base main, ~3766 tokens)
- 2026-09-04T17:35:40+00:00 discovered work filed: CG-051
- 2026-09-04T17:36:03+00:00 opened draft https://github.com/joshmarcus/context-garden/pull/18 (base main): Draft cards now show attempt count and last log line; a new 'retrying' inbox group surfaces auto-retried tasks (ready or running with prior failures); garden digest lists failed work/revise runs as notable. 120 tests pass, lint clean. cost=$1.99
- 2026-09-04T17:38:41+00:00 automated review: approve — All three acceptance criteria met with clean, focused changes and four passing tests. Two minor annotation/signature nits but nothing blocking. cost=$0.31
- 2026-09-04T17:42:29+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/18
