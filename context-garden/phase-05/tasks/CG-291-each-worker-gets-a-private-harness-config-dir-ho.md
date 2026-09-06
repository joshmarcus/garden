---
id: CG-291
title: Each worker gets a private harness config dir holding only credentials, and the fence covers state.json
  and task files
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
branch: garden/cg-291-each-worker-gets-a-private-harness-config-dir-ho
pr: https://github.com/joshmarcus/context-garden/pull/200
harness: codex
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-06T00:48:46+00:00'
created: '2026-09-05T23:58:18+00:00'
updated: '2026-09-06T01:57:52+00:00'
---

## Goal

Build CLAUDE_CONFIG_DIR and CODEX_HOME under the scratch home with only the credentials file, refreshed per dispatch; at minimum add settings.json, settings.local.json, CLAUDE.md and config.toml to _fence_guard_targets. On an attributed state.json change restore other tasks' keys from the dispatch snapshot, and apply attribution to live-garden task files instead of exempting them. Security mediums.

## Context

Carried into phase-05 from the phase-04 retro. Includes CG-246's scope: write separation also covers sibling run outputs under .garden/runs and the audit evidence the fence records; a worker's shell redirect into any of these is attributed at reap and restored, like state.json.

## Acceptance criteria

- [ ] Per-dispatch, CLAUDE_CONFIG_DIR and CODEX_HOME are built under the scratch home and contain only the credentials file, with no settings or other config carried over — verified by a dispatch test asserting the built dirs' contents.
- [ ] `_fence_guard_targets` includes at minimum settings.json, settings.local.json, CLAUDE.md, and config.toml — verified by reading the `_fence_guard_targets` list in the fence module.
- [ ] An attributed change to state.json triggers restoration of other tasks' keys from the dispatch snapshot — proven by a test that mutates a foreign task's key mid-run and asserts it is restored at reap.
- [ ] Attribution applies to live-garden task files instead of exempting them — proven by a test asserting a worker's edit to a file under `**/tasks/` is attributed rather than skipped.
- [ ] Write separation extends to sibling run outputs under `.garden/runs` and the audit evidence the fence records: a worker's shell redirect into either is attributed at reap and restored, matching state.json handling.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-280 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002110Z-edit) cost=$0.08
- 2026-09-06T00:24:02+00:00 approved (cli)
- 2026-09-06T00:25:38+00:00 dispatched work run 20260906T002521Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~6856 tokens)
- 2026-09-06T00:39:38+00:00 opened https://github.com/joshmarcus/context-garden/pull/200 (base main): Workers now receive refreshed credential-only Claude and Codex config directories under their scratch home, on both local and SSH runners. The fence now attributes task/state/run-audit writes and restores protected data. cost=$1.36
- 2026-09-06T00:48:09+00:00 automated review requested changes: Tests and lint pass and each criterion has a passing test, but the state-restore wholesale-replaces other tasks' entire entries (real data-loss risk on a live scheduler), the SSH runner silently drops custom harness config-dir variables, and the sibling-run guard re-copies the entire run history on every dispatch. cost=$0.63
- 2026-09-06T00:48:46+00:00 dispatched revise run 20260906T004845Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~7482 tokens)
- 2026-09-06T01:49:12+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/200: Resolved all three blocking review findings and added regression coverage. The revision is committed as 9c859cb. cost=$0.50
- 2026-09-06T01:57:52+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/200
