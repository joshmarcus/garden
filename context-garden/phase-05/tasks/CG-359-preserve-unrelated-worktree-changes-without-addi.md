---
id: CG-359
title: Preserve unrelated worktree changes without adding them to recovered PRs
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading: []
branch: garden/cg-359-preserve-unrelated-worktree-changes-without-addi
attempts: 1
last_dispatched_at: '2026-09-06T23:37:35+00:00'
created: '2026-09-06T19:13:47+00:00'
updated: '2026-09-06T23:37:35+00:00'
---

## Goal

Recover worker results without silently adding unrelated dirty artifacts to the task's PR; preserve those artifacts and provenance separately.

## Context

In CG-357 the worker explicitly left docs/design/snapshot.json uncommitted. Scheduler leftover salvage committed it in7b818c4 and again1b8d31c after an operator cleanup, adding tens of thousands of unrelated runtime-state lines to PR234. Review rejected the diff and operator had to preserve/remove it twice. CG-333 salvages already committed work when a result is missing; coordinate with that task rather than weakening recovery or discarding dirty data. See context-garden/docs/incidents/2026-09-06-web-responsiveness-retro.md.

## Acceptance criteria

- [ ] Track pre-existing dirty changes and provenance at dispatch; recovery does not blindly commit every modified/untracked file or treat a worker's excluded artifact as part of its completed result.
- [ ] Preserve ambiguous/unrelated changes in a documented recovery artifact or equivalent safe location, with task/run references and clear restoration instructions. Never delete them merely to obtain a clean PR.
- [ ] A completed worker with intended commits plus an unrelated dirty snapshot opens/updates a PR containing only intended changes. A second revise/reap cycle cannot reintroduce the preserved snapshot.
- [ ] Missing-result salvage still preserves intended committed work per CG-333. Cover pre-existing edits, intentional new files, interrupted runs and repeated recovery with regression tests; do not use a blanket filename denylist that blocks a legitimate snapshot task.

## Counterfactual

Provenance-aware salvage would have prevented repeated enormous unrelated diffs, review failures and manual cleanup during incident restoration.

19:43 recurrence evidence: CG-329 and CG-330 were also held on unrelated snapshot diffs committed by leftover salvage; operator preserved /home/joshua/work/operator-test-tmp/CG-329-snapshot-1943.json and CG-330-snapshot-1943.json and removed only those diffs in8874a88/31b2db9. Review correctness findings were otherwise satisfied; this is repeated recovery overhead, not speculative scope.


## Repeated CI-offload failure, 2026-09-06 23:36 UTC

This root cause has now blocked CG354/PR245 (scheduler leftover commit dd7ff92224af1217853a48ab17e07117ca92628e adds roughly69000 snapshot lines and invalidates worker CI at c4e6ca3) and CG361/PR244. CG341 worker completed at9122d7f3ff1da7ae833f28ac7154674e88740b6b with successful CI34066986116, explicitly restored unrelated snapshot after temporary CI stash, and is entering the same salvage path. Prioritize prevention over repeated operator cleanup. Worker-committed exact-head CI should remain valid when only unrelated artifacts need preservation. For already-salvaged branches, preserve evidence before removing unrelated final diff; do not rewrite active task branches from this worker. Scope changes to salvage/provenance modules and dedicated regressions; coordinate around CG361 resource/runner enforcement, CG354 shared fixture work and CG341 stabilization gate. No extra model agents, local full suites or production scheduler actions; use focused bounded tests plus exact-commit GitHub CI.

## Log

- 2026-09-06T23:36:57+00:00 priority 1 -> 0
- 2026-09-06T23:37:35+00:00 dispatched work run 20260906T233716Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9480 tokens)
