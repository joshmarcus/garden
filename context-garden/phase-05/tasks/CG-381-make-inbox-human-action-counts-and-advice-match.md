---
id: CG-381
title: Make Inbox human-action counts and advice match actual ownership
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 5
difficulty: medium
reading:
- src/garden/inbox.py
- src/garden/web/pages/inbox.py
- src/garden/web/templates/inbox.html
- tests/test_inbox_digest.py
- tests/test_attention.py
- tests/test_triage.py
branch: garden/cg-381-make-inbox-human-action-counts-and-advice-match
pr: https://github.com/joshmarcus/context-garden/pull/291
runner: remote
discovered_from: CG-337
attempts: 1
last_dispatched_at: '2026-09-09T00:34:46+00:00'
created: '2026-09-07T12:54:17+00:00'
updated: '2026-09-09T00:46:31+00:00'
---

## Goal

Make Inbox ownership and recommended actions match actual scheduler state. Queued automated reviews and deliberately deferred work must not be presented as unresolved human decisions.

## Evidence

Owner-requested Inbox audit on 2026-09-07 found 24 "need you" items: 13 PRs already had pending_reviews, 10 were intentionally frozen phase06 drafts, and CG294 was an operator-owned deployment prerequisite. The CLI labeled queued reviews "no review yet" despite prior request_changes verdicts and recommended garden set-status TASK done. This is not approval or a safe merge procedure. CG337 has shipped; CG374 and CG362 are in flight. This follow-up owns these specific presentation/action defects and must not expand their frozen briefs.

## Acceptance criteria

- [ ] Derive owner-action count from actual unresolved decisions. Queued/running automatic review shows its queue or resource wait and prior verdict separately, without demanding owner action or recommending set-status done.
- [ ] Explicitly frozen/deferred drafts appear as deferred with the policy reason; owner-action count excludes them. Preserve a deliberate way to change the decision without approving or cancelling to clear a badge.
- [ ] An operator-owned deployment/recovery prerequisite has a concrete reason and next action and is not described as an unanswered owner question. Do not hide genuinely required authority or product choices.
- [ ] CLI and web agree on representative queued-review, prior-request-changes, deferred-draft, and deployment-wait fixtures. Focused tests verify displayed count, wording and actions; actual small Inbox journey verifies rendering. No broad unrelated page checklist, fabricated approval, state rewrite, or auto-merge bypass.
- [ ] Self-review and fix findings; focused bounded validation and exact-head CI for implementation.

## Owner clarification: PR actions require automated approval

Do not ask the human to act on a PR until an automated reviewer has approved its current head. Pending/queued reviews, missing verdicts, and request_changes are automated workflow states, not owner PR-action cards. Prior-head approval is stale after substantive code changes. Approved PRs still require normal exact-head CI/mergeability checks; approval does not itself authorize unsafe completion. Preserve technical recovery visibility as operator-owned and distinguish independent product questions from PR action requests. Cover pending, request_changes, approved-current-head and stale-approved-head cases in CLI/web count and action tests.

## Log

- 2026-09-07T13:41:15+00:00 dispatched work run 20260907T134113Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9733 tokens)
- 2026-09-07T14:05:29+00:00 preserved uncommitted worktree changes from run 20260907T134113Z-work outside the PR: `git stash apply c325a1596c8c8f51f5325e3d3ce4a9f563c90469` in /home/joshua/work/worktrees/CG-381 (garden:CG-381:20260907T134113Z-work:reap)
- 2026-09-07T14:10:47+00:00 opened https://github.com/joshmarcus/context-garden/pull/291 (base main): Inbox ownership now reflects actual scheduler responsibility: only current-head automated approval creates a human PR action, while review waits and frozen drafts are notices. Added focused coverage, live Inbox captures, and exact-head CI passed. cost=$2.82
- 2026-09-07T14:15:58+00:00 automated review requested changes: Current-head approval is incorrectly counted as human-owned when another automated review is queued, and queued notices do not expose the scheduler's actual wait reason. Focused tests pass, but the representative Inbox journey does not exercise the affected queued, deferred, or deployment states. cost=$0.93
- 2026-09-07T15:48:47+00:00 priority 1 -> 0 (web)
- 2026-09-07T16:37:55+00:00 Temporary operator incident admission hold to reserve next drained slot for P0 CG385 recovery; preserve all work. Restore original runner from docs/incidents/cg385-recovery-admission-holds.json after CG385 starts.
- 2026-09-07T16:39:06+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-381`) or send it back (`garden triage CG-381 --changes "..."`)
- 2026-09-07T17:01:39+00:00 Operator restored original runner after CG385 recovery repair acquired actual execution slot. Shared cap remains1.
- 2026-09-07T18:59:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T18:59:47+00:00 Delegated operator Inbox audit: cleared stale manual-hold stop after verified normal runner restoration; existing implementation, PR and pending review feedback retained. No owner decision required.
- 2026-09-07T22:59:21+00:00 dispatched revise run 20260907T225919Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12140 tokens)
- 2026-09-07T23:49:58+00:00 preserved uncommitted worktree changes from run 20260907T225919Z-revise outside the PR: `git stash apply fdc4813035e02332d82cdde9e43f4850d5a3efbd` in /home/joshua/work/worktrees/CG-381 (garden:CG-381:20260907T225919Z-revise:reap)
- 2026-09-07T23:50:00+00:00 pre-PR checks failed (review pre-flight); revise run will fix before the PR is updated cost=$3.48
- 2026-09-08T02:16:26+00:00 dispatched revise run 20260908T021622Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11713 tokens)
- 2026-09-08T02:50:48+00:00 preserved uncommitted worktree changes from run 20260908T021622Z-revise outside the PR: `git stash apply 030b42469e42d769050d2e85899a6265b9c0d9fa` in /home/joshua/work/worktrees/CG-381 (garden:CG-381:20260908T021622Z-revise:reap)
- 2026-09-08T02:56:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/291: Inbox ownership notices and actions remain correct after integrating current main; the required pre-flight evidence is now supplied. Exact-head CI passed for 2f75bbf99ae5791bd41c5963d463da796917d6e4. cost=$3.19
- 2026-09-08T03:12:05+00:00 Owner shutdown: 20260908T030855Z-review interrupted; preserve worktree and saved artifacts. No resume without owner instruction.
- 2026-09-08T10:54:46+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py, src/garden/web/templates/inbox.html); a rebase agent will resolve it
- 2026-09-08T11:02:13+00:00 dispatched rebase run 20260908T110211Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~5966 tokens)
- 2026-09-08T11:05:38+00:00 preserved uncommitted worktree changes from run 20260908T110211Z-rebase outside the PR: `git stash apply 6edfeb955f6211bb3ddbe9054ea79eafaf7c5433` in /home/joshua/work/worktrees/CG-381 (garden:CG-381:20260908T110211Z-rebase:reap)
- 2026-09-08T11:05:41+00:00 push failed: lease rejected on garden/cg-381-make-inbox-human-action-counts-and-advice-match: expected origin at 2f75bbf99ae5, now at 38129a2f7ab6 cost=$0.03
- 2026-09-08T12:28:50+00:00 Owner-requested Inbox audit: completed verified source/test reading list; preserved implementation, PR and feedback.
- 2026-09-08T12:35:50+00:00 triage: changes requested by hand: Operator audit: preserved local1810976 and remote38129a2 under refs/operator/inbox-audit-20260908/CG-381 and merged both
- 2026-09-08T12:35:50+00:00 Delegated operator Inbox review: preserved PR/worktree and queued one concrete continuation within current 4 AWS + 1 local limits.


## Additional live Inbox fixtures, 2026-09-08T16:15:35.229474+00:00

Review cards incorrectly demand owner action and offer Mark done for CG405 (review actually queued/running plus stacked dependency), CG411 (check/review queued), CG398/430 (review timed out before claim; automatic review intent lost, CG-438 owns recovery), and CG395 (no current verdict, checks held). Existing automated ownership criteria cover these; use these as concrete fixtures and do not duplicate CG-438. Explicit phase holds CG402/407 are acknowledged choices, not fresh approval requests; operator-owned verification investigations CG328/332/397 should expose their actual owner once CG437 provides the state.
- 2026-09-08T17:48:08+00:00 kept 6 local-only commit(s) on `backup/20260908T174807Z-revise` before syncing to origin/garden/cg-381-make-inbox-human-action-counts-and-advice-match's head: b901768f Merge remote-tracking branch 'origin/garden/cg-381-make-inbox-human-action-counts-and-advice-match' into garden/cg-381-make-inbox-human-action-counts-and-advice-match; 1810976d Normalize wrapped Inbox CLI output; cc8a0ad3 Make Inbox CLI assertions wrapping-safe; 10fcf71e Fix queued Inbox review ownership; 283276f1 Capture Inbox ownership states; dbe73b05 Fix Inbox ownership and review advice
- 2026-09-08T17:48:14+00:00 dispatched revise run 20260908T174807Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~25210 tokens)
- 2026-09-08T18:30:52+00:00 preserved uncommitted worktree changes from run 20260908T174807Z-revise outside the PR: `git stash apply 4df510b99d8bb7ceedf7ba20ddd805777140c1a6` in /home/joshua/work/worktrees/CG-381 (garden:CG-381:20260908T174807Z-revise:reap)
- 2026-09-08T18:34:04+00:00 pre-PR checks failed (ui, UI captures); revise run will fix before the PR is updated cost=$2.61
- 2026-09-08T19:08:59+00:00 dispatched revise run 20260908T190856Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~26607 tokens)
- 2026-09-08T19:18:23+00:00 preserved uncommitted worktree changes from run 20260908T190856Z-revise outside the PR: `git stash apply ebacbbe4dfe885794ba6b16e839695d815f547ce` in /home/joshua/work/worktrees/CG-381 (garden:CG-381:20260908T190856Z-revise:reap)
- 2026-09-08T19:20:34+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/291: Scoped Inbox UI checks now retain and verify the representative decision-card page, with committed 1280/390 light/dark capture evidence. Focused Inbox, web, CLI, attention, triage, and walkthrough tests plus lint passed on commit cdcb4b9e. cost=$1.07
- 2026-09-08T19:23:40+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py, src/garden/web/templates/inbox.html, tests/test_cli.py); a rebase agent will resolve it
- 2026-09-08T19:29:01+00:00 review validation scope expansion: src/garden/walkthrough.py forces task-decision into every bounded page selection — This changes the declared scoped-capture contract and adds an unrelated page despite the criterion prohibiting broad unrelated page checklists.
- 2026-09-08T19:29:01+00:00 review validation scope expansion: served affected-state Inbox interaction — The supplied generic replay never requests the affected Inbox page or exercises its ownership cards.
- 2026-09-08T19:29:02+00:00 automated review: request_changes — Core ownership behavior is well covered by focused tests, but this head lacks the required affected Inbox interaction and exact-head CI. It also globally expands scoped Inbox captures to an unrelated task page. cost=$0.70
- 2026-09-08T22:02:35+00:00 dispatched rebase run 20260908T220231Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~7261 tokens)
- 2026-09-08T22:06:23+00:00 preserved uncommitted worktree changes from run 20260908T220231Z-rebase outside the PR: `git stash apply 085e3a6d22d527acb70d132599dfc85c29e03bf7` in /home/joshua/work/worktrees/CG-381 (garden:CG-381:20260908T220231Z-rebase:reap)
- 2026-09-08T22:22:47+00:00 dispatched revise run 20260908T222247Z-revise via manual [human] (fresh session, base main, ~27039 tokens)
- 2026-09-08T23:44:48+00:00 cleared stale check metadata and recovered task state
- 2026-09-08T23:46:56+00:00 external PR attached at garden/cg-381-make-inbox-human-action-counts-and-advice-match; existing CI is SUCCESS
- 2026-09-08T23:49:04+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/291: Fixed scoped capture expansion and exact duplicate test left by rebase.6focusedtests and lint pass; actual final-head servedInbox8HTTPevents/4PNGs verify affected, empty and failure/recovery with correct count0. Current-head CI and automated review remain required.
- 2026-09-08T23:49:31+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/inbox.py); a rebase agent will resolve it
- 2026-09-08T23:49:51+00:00 dispatched rebase run 20260908T234951Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3525 tokens)
- 2026-09-08T23:52:41+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/291: Rebased CG-381 onto origin/main and resolved the inbox.py conflict preserving both sides' behavior. cost=$0.01
- 2026-09-08T23:58:11+00:00 review validation scope expansion: Committed task-decision and Now walkthrough/capture artifacts — The final diff still includes unrelated task-decision and Now evidence despite the Inbox-only validation scope and explicit prohibition on broad unrelated page checklists.
- 2026-09-08T23:58:11+00:00 automated review clarification requested for ambiguous unverified observations
- 2026-09-09T00:34:28+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/review.py); a rebase agent will resolve it
- 2026-09-09T00:34:46+00:00 dispatched rebase run 20260909T003446Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3763 tokens)
- 2026-09-09T00:37:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/291: Rebased CG-381 onto origin/main and preserved both exact-head ownership tracking and review diff metadata. cost=$0.01
- 2026-09-09T00:43:30+00:00 review validation scope expansion: Committed task-decision and Now walkthrough/capture artifacts — The diff includes unrelated pages despite the frozen criterion prohibiting broad unrelated page checklists; the Inbox template maps only to the Inbox page.
- 2026-09-09T00:43:32+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: cli and web agree on; run `garden triage CG-381 --changes "<feedback>" to unblock`
- 2026-09-09T00:46:31+00:00 Owner-authorized current-head operator review approved proportionate verification; GitHub merge confirmed 8cc8a9c3211ab859aadc0c4db9001af0858604bf
