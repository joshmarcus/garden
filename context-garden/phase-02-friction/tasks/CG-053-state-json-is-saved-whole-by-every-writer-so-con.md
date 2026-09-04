---
id: CG-053
title: state.json is saved whole by every writer, so concurrent writers lose updates
status: in_review
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/scheduler.py
- docs/architecture.md
branch: garden/cg-053-state-json-is-saved-whole-by-every-writer-so-con
pr: https://github.com/joshmarcus/context-garden/pull/37
attempts: 1
last_dispatched_at: '2026-09-04T19:12:18+00:00'
created: '2026-09-04T17:41:02+00:00'
updated: '2026-09-04T19:31:43+00:00'
---

## Goal

Two processes writing `.garden/state.json` at the same time (the `garden serve` loop and a `garden tick`, `garden triage`, a web action, or a person editing a key) do not silently undo each other's changes.

## Context

Seen during the first live run. `State.save` writes the whole file from the process's in-memory copy. `garden serve` reloads at the start of every tick and saves at the end, several seconds later while it polls GitHub. Anything written in that window by another process (a CLI command, a second tick, a hand edit to clear `pr_updated_at` so a PR would be re-read) is overwritten by the loop's save. It took three attempts to get one cleared key to survive long enough for a poll to see it, and in the end the server had to be stopped to make the edit stick. The architecture page's "two ticks overlap" note covers run reaping, not state.

Options, smallest first: save per task (`state/<task>.json`) so writers only touch their own task; or reload-merge-save under a file lock (`fcntl.flock`) with the process's changed keys applied on top of what is on disk; or an append-only patch log the way `events.jsonl` already works. Whatever is chosen, `garden tick` while `serve` runs and a web action during a tick must both be safe.

## Acceptance criteria

- [ ] a test: two State objects change different keys of the same task and both changes are on disk afterwards.
- [ ] a CLI command that changes state during a running tick does not lose its change.
- [ ] `docs/architecture.md` says what the guarantee is.

## Out of scope

- Task files; only the scheduler writes their status and it already reloads them each tick.

## Log

- 2026-09-04T18:41:38+00:00 approved
- 2026-09-04T19:12:18+00:00 dispatched work run 20260904T191218Z-work via local [claude model=sonnet] (fresh session, base main, ~7520 tokens)
- 2026-09-04T19:31:43+00:00 opened https://github.com/joshmarcus/context-garden/pull/37 (base main): Replaced State.save() with a lock-based merge-on-save: _TaskState tracks dirty keys at the top level (including reads of nested dicts/lists), and save() acquires an exclusive flock, re-reads disk, merges only changed keys, then writes back. All 195 tests pass. cost=$2.91
