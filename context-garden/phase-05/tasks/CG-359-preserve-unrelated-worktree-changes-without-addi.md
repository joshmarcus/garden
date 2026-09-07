---
id: CG-359
title: Preserve unrelated worktree changes without adding them to recovered PRs
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading: []
branch: garden/cg-359-preserve-unrelated-worktree-changes-without-addi
pr: https://github.com/joshmarcus/context-garden/pull/248
attempts: 1
last_dispatched_at: '2026-09-06T23:37:35+00:00'
created: '2026-09-06T19:13:47+00:00'
updated: '2026-09-07T00:23:47+00:00'
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
- 2026-09-06T23:50:11+00:00 opened https://github.com/joshmarcus/context-garden/pull/248 (base main): Recovery now preserves uncommitted worktree artifacts as run-scoped named stashes instead of committing them into task branches. Committed worker work continues through normal salvage and PR creation. cost=$1.03
- 2026-09-06T23:52:37+00:00 triage: changes requested by hand: Operator removing only the installed old scheduler's unrelated snapshot salvage before first review; preserve original d
- 2026-09-06T23:59:15+00:00 Operator held first review and preserved the installed old scheduler's own snapshot salvage54e4f3c in operator-test-tmp/snapshot-salvage-20260906T2343Z with hashed metadata. Pushed cleanup2c889374a81d956b61971b496a149995c657a41f; complete tree equals intended4a3565b. New branch/PR CI34068102211/34068103543 pending at23:55; prioritize review and verified deployment once passed. No data discarded, no model revision/local full suite used for cleanup.
- 2026-09-07T00:07:20+00:00 triage: marked ready for review
- 2026-09-07T00:10:16+00:00 description rewritten by the reviewer cost=$0.53
- 2026-09-07T00:10:22+00:00 stuck: pending feedback recorded but the task is in_review, not changes_requested; resume with one more round (`garden retry CG-359`) or send it back (`garden triage CG-359 --changes "..."`)
- 2026-09-07T00:19:38+00:00 triage: changes requested by hand: Review approved the implementation. Integrating the subsequently merged onboarding main before final CI/re-review and de
- 2026-09-07T00:23:47+00:00 Review20260907T000722Z-review approved all four implementation criteria with no code findings, requesting only permanent phase-goal framing. After the earlier onboarding merge, operator integrated current mainf41b414 into reviewed2c88937, verified the branch-specific diff is byte-for-byte unchanged, and pushed35d15ef08ef8bb314bf1def4245e3ff769dda24c. PR body has phase-goal framing and accurately says new integration CI is pending. Held changes_requested to prevent stale approval/CI merging; after current-head CI passes, request a fresh review with the single reviewer slot, then merge/deploy at accounted drain. No extra implementation worker is needed.
