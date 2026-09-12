---
id: CG-336
title: Record Codex operator usage in the operator spend ledger
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
branch: garden/cg-336-record-codex-operator-usage-in-the-operator-spen
pr: https://github.com/joshmarcus/context-garden/pull/274
attempts: 1
last_dispatched_at: '2026-09-07T22:23:26+00:00'
created: '2026-09-06T13:15:21+00:00'
updated: '2026-09-07T22:44:47+00:00'
---

## Goal

Record Codex operator usage in the operator spend ledger

## Context

Josh handed operation to the Codex desktop task on 2026-09-06. Both tools/operator_spend.py and garden operator-spend record currently parse Claude transcripts. Support actual Codex operator usage so the operator share remains measurable; do not fall back to guessed prices or record Claude usage as Codex. Coordinate or document the garden-local helper migration.

## Acceptance criteria

- [ ] A representative Codex transcript produces correctly attributed usage with no double counting across check-ins. Unknown pricing or unavailable usage is explicitly unavailable, never zero or a Claude fallback. Existing Claude recording continues to work.

## Log

- 2026-09-06T13:15:22+00:00 approved (cli)
- 2026-09-07T06:59:29+00:00 dispatched work run 20260907T065834Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~8900 tokens)
- 2026-09-07T07:12:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/274 (base main): Codex operator transcripts now record cumulative token usage without double counting and preserve unavailable usage or pricing as unavailable. Claude recording remains supported through explicit source selection. cost=$0.91
- 2026-09-07T07:13:24+00:00 automated review requested changes: The Codex parser double-counts reasoning tokens and does not obtain the model from real Codex transcripts, so representative usage is not correctly attributed. The 23 focused tests pass, but their synthetic session metadata does not match the actual transcript schema. cost=$0.31
- 2026-09-07T07:13:38+00:00 dispatched revise run 20260907T071337Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9550 tokens)
- 2026-09-07T07:26:15+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/274: Codex operator records now take model attribution from real turn_context events and avoid double-counting reasoning output. The representative fixture covers the actual schema and cumulative token invariant. cost=$0.72
- 2026-09-07T15:41:47+00:00 automated review requested changes: Codex cumulative token totals are handled correctly, but real transcripts emit several token snapshots per turn; counting snapshots as turns makes the operator ledger's turn, model, and average-context attribution incorrect. cost=$0.36
- 2026-09-07T16:37:55+00:00 Temporary operator incident admission hold to reserve next drained slot for P0 CG385 recovery; preserve all work. Restore original runner from docs/incidents/cg385-recovery-admission-holds.json after CG385 starts.
- 2026-09-07T16:39:06+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-336`) or send it back (`garden triage CG-336 --changes "..."`)
- 2026-09-07T17:01:39+00:00 Operator restored original runner after CG385 recovery repair acquired actual execution slot. Shared cap remains1.
- 2026-09-07T18:59:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T18:59:47+00:00 Delegated operator Inbox audit: cleared stale manual-hold stop after verified normal runner restoration; existing implementation, PR and pending review feedback retained. No owner decision required.
- 2026-09-07T21:00:55+00:00 dispatched revise run 20260907T210053Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11162 tokens)
- 2026-09-07T21:17:40+00:00 preserved uncommitted worktree changes from run 20260907T210053Z-revise outside the PR: `git stash apply 28aab9ab20f3b2590dad3c58458303cac248e6f4` in /home/joshua/work/worktrees/CG-336 (garden:CG-336:20260907T210053Z-revise:reap)
- 2026-09-07T21:32:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/274: Codex operator transcripts now count turns and model attribution from turn_context boundaries while retaining only the latest cumulative token snapshot. Final exact-head CI passed for db3302159576a00c56a91bfd09a52375ce99dabe. cost=$1.07
- 2026-09-07T21:34:59+00:00 automated review: approve — Codex cumulative usage, turn/model attribution, unavailable pricing, and Claude compatibility are correctly implemented and tested. Exact-head CI and local focused checks pass. cost=$0.30
- 2026-09-07T21:35:17+00:00 rebasing before merge; rebase onto main conflicts (src/garden/operator_spend.py, tests/test_operator_spend.py, tests/test_operator_spend_cli.py); a rebase agent will resolve it
- 2026-09-07T21:35:21+00:00 dispatched rebase run 20260907T213518Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~8382 tokens)
- 2026-09-07T21:37:43+00:00 preserved uncommitted worktree changes from run 20260907T213518Z-rebase outside the PR: `git stash apply ece923f888b72093a4a3e8956c512773f04df4a3` in /home/joshua/work/worktrees/CG-336 (garden:CG-336:20260907T213518Z-rebase:reap)
- 2026-09-07T21:39:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/274: Rebased CG-336 onto origin/main and resolved the three marked conflicts. cost=$0.02
- 2026-09-07T21:44:06+00:00 automated review: approve — Codex cumulative usage, turn/model attribution, unavailable pricing, and Claude compatibility are correctly implemented and tested. The exact reviewed head passes the focused operator-spend suite and lint. cost=$0.37
- 2026-09-07T21:52:12+00:00 CI failure
- 2026-09-07T21:53:16+00:00 dispatched revise run 20260907T215314Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12121 tokens)
- 2026-09-07T22:14:33+00:00 preserved uncommitted worktree changes from run 20260907T215314Z-revise outside the PR: `git stash apply 44b83a1677bcb016d55990c53879c236c2496cc2` in /home/joshua/work/worktrees/CG-336 (garden:CG-336:20260907T215314Z-revise:reap)
- 2026-09-07T22:16:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/274: Made run metadata replacement atomic so a crash cannot erase a recovery launch's idempotency key and admit a duplicate launch. Exact-head CI passed. cost=$1.57
- 2026-09-07T22:16:35+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-07T22:17:46+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-07T22:23:11+00:00 review validation scope expansion: Run metadata atomic replacement lifecycle validation — The unrelated src/garden/runs.py change expanded this PR into scheduler lifecycle behavior and triggered the required disposable-app replay.
- 2026-09-07T22:23:12+00:00 automated review requested changes: Codex transcript parsing is correctly cumulative and attributed, but the CLI still presents all-unavailable pricing as a $0.00 total. The branch also includes an unrelated run-metadata durability change that should be split out. cost=$0.39
- 2026-09-07T22:23:26+00:00 dispatched revise run 20260907T222324Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12236 tokens)
- 2026-09-07T22:35:44+00:00 preserved uncommitted worktree changes from run 20260907T222324Z-revise outside the PR: `git stash apply 3af8302358d88c3d43c308fc8475b8229e267513` in /home/joshua/work/worktrees/CG-336 (garden:CG-336:20260907T222324Z-revise:reap)
- 2026-09-07T22:37:35+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/274: Codex operator usage remains cumulatively attributed without double counting, while unavailable pricing is explicit in the CLI. The unrelated run-metadata durability change has been removed from this branch. cost=$0.57
- 2026-09-07T22:41:35+00:00 automated review: approve — Codex cumulative usage, turn/model attribution, unavailable pricing, and Claude compatibility are correctly implemented and tested. Focused tests and repository-wide lint pass at the reviewed head. cost=$0.42
- 2026-09-07T22:42:32+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-07T22:44:47+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/274
