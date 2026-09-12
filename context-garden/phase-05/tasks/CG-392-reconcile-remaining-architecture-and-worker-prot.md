---
id: CG-392
title: Reconcile remaining architecture and worker-protocol statements with implementation
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 9
difficulty: easy
reading:
- README.md
- docs/architecture.md
- docs/worker-protocol.md
- docs/roadmap.md
- src/garden/config.py
branch: garden/cg-392-reconcile-remaining-architecture-and-worker-prot
pr: https://github.com/joshmarcus/context-garden/pull/359
discovered_from: CG-378
attempts: 1
last_dispatched_at: '2026-09-09T03:50:42+00:00'
created: '2026-09-07T18:43:36+00:00'
updated: '2026-09-09T16:46:25+00:00'
file: docs/architecture.md
error: Architecture and worker-protocol sections still contradict current publication, recovery and review
  implementation.
---

Detailed guides retain contradictory claims about workers never pushing, automatic commitment of leftovers, combined concurrency and self-product review policy. Refresh those sections against worker_push, recovery stashes, separate admission limits and the current persona/human second-opinion gate; the README now describes the current behavior.

## Provenance

Discovered by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`.
## Log
- 2026-09-07T18:43:36+00:00 discovered by CG-378
- 2026-09-07T18:44:54+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:46:15+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:47:49+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:49:01+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:50:12+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:51:23+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:52:35+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:53:49+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:55:00+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:56:14+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:57:27+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T18:58:59+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:00:39+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:03:29+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:05:25+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:07:11+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:08:55+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:10:17+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:11:40+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:12:58+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:14:22+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:15:42+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:17:03+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:18:24+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:19:44+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:21:05+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:22:25+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:23:41+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:24:56+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:26:11+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:27:27+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:28:43+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:30:14+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:31:44+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:33:32+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:35:07+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:36:40+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:38:10+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:39:39+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:40:56+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:42:12+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:43:27+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:44:42+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`
- 2026-09-07T19:46:01+00:00 also found by CG-378 (Refresh README for the current garden and operator workflow) during run `20260907T175551Z-work`


## Acceptance criteria

- [ ] Reconcile architecture and worker protocol against the current reviewed source for pushes, recovery stashes, concurrency and human/persona review gates.
- [ ] Separate installed capabilities from unmerged or undeployed proposals; preserve generic wording and valid cross-links.
- [ ] Validate commands and config names against actual CLI/schema and record source evidence; no broad screenshots for prose-only edits.
- 2026-09-07T20:06:51+00:00 approved (operator-owner-delegated)
- 2026-09-09T02:56:37+00:00 dispatched work run 20260909T025632Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~20217 tokens)
- 2026-09-09T03:03:13+00:00 preserved uncommitted worktree changes from run 20260909T025632Z-work outside the PR: `git stash apply 7ee6a318532483c8a610328402b52a10952bb356` in /home/joshua/work/worktrees/CG-392 (garden:CG-392:20260909T025632Z-work:reap)
- 2026-09-09T03:03:13+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T03:04:32+00:00 opened https://github.com/joshmarcus/context-garden/pull/359 (base main): Reconciled architecture and worker-protocol documentation with current implementation and committed the docs-only change. cost=$0.10
- 2026-09-09T03:24:45+00:00 automated review requested changes: Most documentation updates accurately cover worker pushes, separate concurrency pools, and self-product review gates. However, the revised SSH protocol incorrectly claims uncommitted changes are preserved rather than committed. cost=$0.43
- 2026-09-09T03:44:02+00:00 dispatched revise run 20260909T034358Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~21200 tokens)
- 2026-09-09T03:46:20+00:00 preserved uncommitted worktree changes from run 20260909T034358Z-revise outside the PR: `git stash apply e7befe70263819d242e17164e7c518dd5cc775e0` in /home/joshua/work/worktrees/CG-392 (garden:CG-392:20260909T034358Z-revise:reap)
- 2026-09-09T03:46:20+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T03:47:39+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/359: Reconciled SSH leftover handling with SSHRunner, preserving the prior documentation updates for pushes, concurrency pools, and self-product review gates. Verified source behavior, 39 focused tests passed, Ruff passed, and the documentation diff is clean. cost=$0.06
- 2026-09-09T03:50:16+00:00 automated review requested changes: The SSH recovery correction is accurate, and the concurrency, worker-push, and review-gate updates match source. One installed-capability contradiction remains between the revised guides and README. cost=$0.43
- 2026-09-09T03:50:42+00:00 dispatched revise run 20260909T035037Z-revise via local [codex model=gpt-5.6-luna] (fresh session, base main, ~21503 tokens)
- 2026-09-09T03:54:32+00:00 preserved uncommitted worktree changes from run 20260909T035037Z-revise outside the PR: `git stash apply be4a225a2187d49a1d873214af65d165dff360cf` in /home/joshua/work/worktrees/CG-392 (garden:CG-392:20260909T035037Z-revise:reap)
- 2026-09-09T03:54:32+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T03:55:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/359: Reconciled the remaining installed-capability contradiction by documenting the implemented remote HTTPS worker and keeping AWS provisioning, model pools, and OpenRouter separate as unavailable. Verified focused runner tests, lint, source/config names, links, and a clean commit diff. cost=$0.08
- 2026-09-09T04:06:54+00:00 automated review: approve — Documentation now accurately distinguishes supported runners and transport-specific behavior from unavailable proposals. cost=$0.38
- 2026-09-09T04:23:14+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T04:24:16+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T04:31:55+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/359
- 2026-09-09T09:42:43+00:00 automated review could not start: CG-392 is done: #359 was merged at 04:31:55
- 2026-09-09T16:46:25+00:00 automatic review recovery retired because task is done
