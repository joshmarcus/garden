---
id: CG-362
title: Complete externally implemented tasks from verified PR metadata
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-362-complete-externally-implemented-tasks-from-verif
pr: https://github.com/joshmarcus/context-garden/pull/261
attempts: 1
last_dispatched_at: '2026-09-08T09:08:27+00:00'
created: '2026-09-06T22:23:48+00:00'
updated: '2026-09-08T10:59:44+00:00'
---

## Goal

An operator who implements a task in an existing session can record its real branch and PR, complete verified merged work, and retain honest audit/cost evidence without guessing scheduler worktree paths or launching redundant checks/review agents.

## Context

On 2026-09-06 the owner authorized direct operator implementation alongside the sole scheduled worker. CG-360 was implemented on codex/cg-360-restore-index, passed focused ext4/tmpfs tests and full final-head CI, and merged as PR242 at44b9a312. A later garden take --no-worktree generated a different branch name and snapshotted the expected CG-360 worktree. The finish --pr path selects its behavior by whether that expected directory exists, even for externally implemented/merged work. The operator mistakenly moved its worktree after take to use the external completion path; this correctly triggered the Git guard. The path was restored, every guard hash compared equal to the original snapshot, and only the resolved operator-created block marker was archived with provenance. The task branch also had to be corrected before ancestry-based completion would succeed. The failed manual bookkeeping run remains recorded; it must not be rewritten as successful worker execution.

Source evidence: docs/incidents/CG-360-validation.md, CG-360 task log and manual run20260906T220127Z-work. No source fix or test failure resulted from the bookkeeping problem. This change should make the safe ordinary workflow direct and explicit; it must preserve Git protection.

## Acceptance criteria

- [ ] Support claiming externally implemented work with an explicit existing worktree/branch or PR identity; persist those actual choices and distinguish external work from scheduler-managed worktree creation. Generated defaults cannot silently override an existing PR's branch.
- [ ] Finishing with an already merged PR verifies the expected head is included in the configured final base and completes the task through the normal transition/audit path without running another test/review cycle. For an open PR, retain the applicable validation/review gates and accurately identify existing head-specific evidence rather than manufacturing an approval.
- [ ] Completion mode is explicit and is not inferred merely from whether a coincidentally named directory exists. No worktree move, clone recreation or guard weakening is needed for a normal external completion. Keep malicious/unattributed Git metadata mutations blocked.
- [ ] Record failed completion attempts separately from successful implementation/merge evidence. Preserve run/task/PR links, expose unknown manual operator cost as unknown, and never count supervised operator work as unattended stabilization.
- [ ] Add focused tests for external and managed paths, mismatched generated/actual branches, already merged versus unmerged or stacked PRs, repeated completion and a genuine Git-guard violation. Document a short copyable operator workflow.

## Log

- 2026-09-06: Priority1 follow-up filed with owner authority after direct operator implementation exposed manual completion overhead. Ordinary dispatch remains paused.
- 2026-09-06T22:59:27+00:00 2026-09-06T22:59:27+00:00: CG363 external worktree remained outside scheduler path from the outset. Normal finish_manual API succeeded with review.enabled false scoped to that single call under owner direct-work authority, followed by normal merged-PR reconciliation; no extra model launched and spend stayed unknown. A supported CLI option should avoid needing this scoped API configuration.
- 2026-09-06T23:59:15+00:00 Operator review workflow friction23:53-23:57: triage-ready retained CG340 old pending_feedback; reconcile set needs_human="stuck: pending feedback recorded but the task is in_review, not changes_requested". Explicit review_again clears needs_human at dispatch but an approve verdict with description_rewrite returned early and left old feedback/stop intact. Actual reviewed head and CI were valid; operator applied permanent rewrite and merged. A supported manual-repair -> queued re-review path should respect review_parallel, preserve findings for review, then clear only obsolete feedback/stops on approval. Include this boundary in external/manual completion design or file a separate fix if scope warrants; never hand-edit state as the workaround.
- 2026-09-07T00:50:07+00:00 Operator 2026-09-07 00:50 UTC: idle recovery gap after CG359 main CI passed. Paused admission was retained while no workers/reviewers were active; operator failed to immediately consume satisfied deployment/review gates. Add actionable paused-and-idle recovery detection/next-action ownership, not another uninformative needs-human card. Main repair now installed and controlled work restarting.
- 2026-09-07T01:13:09+00:00 2026-09-07 01:13 UTC: CG361/PR244 merged01:06:18 before reviewer010546 finished01:09:01 with blocking findings. DONE is correct for GitHub state but late review findings need preserved, actionable follow-up without reopening a merged task or treating it as deployment-approved. CG365 reused for actual fixes; earlier reviewers also accepted workload evidence later rejected. Preserve review evidence lineage and flag changes in criterion conclusions.
- 2026-09-07T01:43:27+00:00 2026-09-07 01:43 UTC: CG365 triage-changes wrote a complete pending_feedback but simultaneously produced needs_human="stuck: no feedback recorded to revise against"; task sat changes_requested while ordinary slots advanced other work. Verified persisted state contains the complete correction, no active CG365 run and PR OPEN; supported /retry cleared needs_human while retaining feedback, no immediate dispatch/bypass. Add regression for state visibility/order during triage transition and stuck reconciliation.
- 2026-09-07T02:13:54+00:00 CG293 owner inquiry02:12 UTC exposed another lost-feedback case: last_review.request_changes with three findings survived, pending_feedback was empty, needs_human claimed no feedback. Restored from actual stored verdict through triage/retry. Regression should preserve/reconstruct actionable review feedback across failed checks/base-broken and rebase transitions without making owner interpret this internal inconsistency.
- 2026-09-07T02:24:00+00:00 Human-queue audit: CG322/293 lost revision feedback, CG326 stale base probe, CG332 zero actual PNGs causing repeated broad screenshot findings, and frozen drafts appearing as current human decisions. Recovery must distinguish actionable decisions from deferred/operator-owned prerequisite holds and route missing capture infrastructure to its repair rather than paid unrelated revisions. See docs/human-queue-2026-09-07.md.
- 2026-09-07T03:49:33+00:00 Browser capture infrastructure root cause confirmed: host lacks libnspr4/libnss3; empty base-probe recovery was repeatedly retried despite checks=[]. User-local Ubuntu libraries now activated for service, worker continuation explicitly receives library path. Prevent repeated empty probes and classify missing browser runtime as infrastructure readiness rather than unrelated revisions.
- 2026-09-07T04:14:39+00:00 dispatched work run 20260907T041419Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10485 tokens)
- 2026-09-07T04:42:45+00:00 preserved uncommitted worktree changes from run 20260907T041419Z-work outside the PR: `git stash apply 41c4c8aa52b74ed7795dce1b849844ea3a2ffde3` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T041419Z-work:reap)
- 2026-09-07T04:43:57+00:00 opened https://github.com/joshmarcus/context-garden/pull/261 (base main): External task claims now persist an explicit completion mode, real branch/PR identity, and refused-completion audit records. Merged PRs complete only after final-base ancestry verification; open PRs retain review gates without manufacturing evidence. cost=$1.73
- 2026-09-07T04:45:48+00:00 automated review requested changes: The external completion path works for PR identity and ancestry, but bypasses the fence/Git-guard checks and loses the attempted PR link on refused finishes. Focused tests pass (165), but they do not exercise these required boundaries. cost=$0.47
- 2026-09-07T04:46:12+00:00 dispatched revise run 20260907T044610Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11330 tokens)
- 2026-09-07T04:57:37+00:00 preserved uncommitted worktree changes from run 20260907T044610Z-revise outside the PR: `git stash apply c2f40d52c65144b8d061ed6118ddca60449f911d` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T044610Z-revise:reap)
- 2026-09-07T04:59:52+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/261: External completion now validates dispatch-time Git and fence guards before accepting PR evidence, and refused attempts retain the attempted PR identity. Commit c8a2a8c passed focused tests, lint, and GitHub CI. cost=$1.17
- 2026-09-07T05:01:51+00:00 automated review requested changes: External completion identity, ancestry verification, explicit mode, audit records, guards, tests, and workflow documentation are implemented. However, externally completed supervised work is still counted as unattended stabilization, violating a core acceptance criterion. cost=$0.35
- 2026-09-07T05:08:36+00:00 dispatched revise run 20260907T050835Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11526 tokens)
- 2026-09-07T05:19:40+00:00 preserved uncommitted worktree changes from run 20260907T050835Z-revise outside the PR: `git stash apply b7c703c6330b86ad32385c4820ecc541d98bb339` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T050835Z-revise:reap)
- 2026-09-07T05:20:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/261: Excluded supervised external merged-PR completions from productive-unattended stabilization counts, with a regression through the real external completion path. Incorporated current main, pushed the final head, and exact-commit GitHub CI passed. cost=$1.04
- 2026-09-07T05:22:38+00:00 automated review requested changes: External claiming, guard enforcement, audit records, and stabilization accounting are covered, but verified merged completion omits normal post-merge handling for stacked dependents and tool upgrades. cost=$0.47
- 2026-09-07T05:23:14+00:00 dispatched revise run 20260907T052311Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11784 tokens)
- 2026-09-07T05:31:44+00:00 preserved uncommitted worktree changes from run 20260907T052311Z-revise outside the PR: `git stash apply cb1ea8202e70d4ce5a1b6635418f8a561fadec09` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T052311Z-revise:reap)
- 2026-09-07T05:33:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/261: External merged-PR completion now invokes the ordinary post-merge lifecycle without cleaning an operator-owned checkout. The revision is committed as 57ffcd2 and exact-commit GitHub CI passed. cost=$0.61
- 2026-09-07T10:11:55+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/dispatch.py); a rebase agent will resolve it
- 2026-09-07T10:13:30+00:00 dispatched rebase run 20260907T101328Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~10624 tokens)
- 2026-09-07T10:15:55+00:00 preserved uncommitted worktree changes from run 20260907T101328Z-rebase outside the PR: `git stash apply cac6b5cb6c4f53c94598ca0d307b927dc1b040a5` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T101328Z-rebase:reap)
- 2026-09-07T10:17:22+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/261: Rebased onto origin/main and resolved the dispatch.py conflict preserving both sides. cost=$0.02
- 2026-09-07T10:20:24+00:00 automated review requested changes: External PR reconciliation largely follows the intended lifecycle, but claimed identity is not fully persisted at claim time and some failed completion attempts bypass the audit record. Final-head CI is also still pending. cost=$0.44
- 2026-09-07T10:21:10+00:00 stuck: 3 revision rounds already used; resume with one more round (`garden retry CG-362`) or send it back (`garden triage CG-362 --changes "..."`)
- 2026-09-07T12:13:04+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-07T12:32:36+00:00 dispatched revise run 20260907T123235Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12786 tokens)
- 2026-09-07T12:54:26+00:00 preserved uncommitted worktree changes from run 20260907T123235Z-revise outside the PR: `git stash apply dac43743f56c010a5165c411db65086644f131a6` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T123235Z-revise:reap)
- 2026-09-07T13:35:29+00:00 check did not run (20260907T133410Z-check): idle 41 min (no output or file change); will retry
- 2026-09-07T13:36:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/261: External claims now persist their real branch and PR identity at take time, PR lookup failures are audited as refused completions, and branch-first blocked work preserves normal guarded manual behavior. Rebased onto current main, pushed normally, and exact-head CI passed. cost=$2.18
- 2026-09-07T13:37:12+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/dispatch.py); a rebase agent will resolve it
- 2026-09-07T13:37:20+00:00 dispatched rebase run 20260907T133717Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~11249 tokens)
- 2026-09-07T13:40:58+00:00 preserved uncommitted worktree changes from run 20260907T133717Z-rebase outside the PR: `git stash apply e190249e1488118677decda7fdd092e6c35d623e` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T133717Z-rebase:reap)
- 2026-09-07T13:43:47+00:00 pre-PR checks failed (lint) and 3 revision rounds already used; needs a human cost=$0.04
- 2026-09-07T15:29:52+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-07T15:37:17+00:00 automated review: request_changes — The lifecycle behavior is covered by 95 passing focused tests, but final-head lint fails on a duplicated test definition. The required scheduler replay manifest is also absent at the supplied path. cost=$0.54
- 2026-09-07T16:37:55+00:00 Temporary operator incident admission hold to reserve next drained slot for P0 CG385 recovery; preserve all work. Restore original runner from docs/incidents/cg385-recovery-admission-holds.json after CG385 starts.
- 2026-09-07T16:39:06+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-362`) or send it back (`garden triage CG-362 --changes "..."`)
- 2026-09-07T17:01:39+00:00 Operator restored original runner after CG385 recovery repair acquired actual execution slot. Shared cap remains1.
- 2026-09-07T18:59:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T18:59:47+00:00 Delegated operator Inbox audit: cleared stale manual-hold stop after verified normal runner restoration; existing implementation, PR and pending review feedback retained. No owner decision required.
- 2026-09-07T22:18:04+00:00 dispatched revise run 20260907T221801Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~14614 tokens)
- 2026-09-07T22:26:52+00:00 preserved uncommitted worktree changes from run 20260907T221801Z-revise outside the PR: `git stash apply 9b56d794dfbcdc63c58183b0e4cd98910186c671` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T221801Z-revise:reap)
- 2026-09-07T22:29:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/261: Removed the duplicate stacked-child external completion regression test that caused final-head lint to fail. Focused scheduler tests, lint, and exact-head GitHub CI now pass. cost=$0.47
- 2026-09-07T22:29:19+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/dispatch.py); a rebase agent will resolve it
- 2026-09-07T22:29:28+00:00 dispatched rebase run 20260907T222925Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~4518 tokens)
- 2026-09-07T22:37:36+00:00 preserved uncommitted worktree changes from run 20260907T222925Z-rebase outside the PR: `git stash apply bc7f059dda65cfb78308de9a362a4e2ee9a58ae7` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T222925Z-rebase:reap)
- 2026-09-07T22:37:36+00:00 rebase conflict run 20260907T222925Z-rebase did not finish: worker exited 1: {'message': 'unexpected status 401 Unauthorized: Missing bearer or basic authentication in header, url: https://api.openai.com/v1/responses, cf-ray: a3792fa32d5c9bb4-EWR, request id: req_c7322bb24df84; will retry
- 2026-09-07T22:37:36+00:00 rebase conflict run 20260907T222925Z-rebase did not finish: worker exited 1: {'message': 'unexpected status 401 Unauthorized: Missing bearer or basic authentication in header, url: https://api.openai.com/v1/responses, cf-ray: a3792fa32d5c9bb4-EWR, request id: req_c7322bb24df84; will retry
- 2026-09-07T22:41:37+00:00 automated review: request_changes — External completion largely satisfies the lifecycle requirements, but `take --pr` accepts a URL for any repository while resolving and persisting identity from the configured repository's same-numbered PR. The required disposable served-interaction manifest is also absent, leaving the mandated journey unverified. cost=$0.34
- 2026-09-07T22:42:38+00:00 dispatched rebase run 20260907T224236Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~4884 tokens)
- 2026-09-07T22:43:44+00:00 preserved uncommitted worktree changes from run 20260907T224236Z-rebase outside the PR: `git stash apply 0665911fc6fe61516dbe2c956a14a3b6ee0c5d55` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260907T224236Z-rebase:reap)
- 2026-09-07T22:46:09+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/261: Rebased onto origin/main and resolved the dispatch.py conflict preserving validation-plan capture and external worktree handling. cost=$0.02
- 2026-09-07T22:58:43+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: support claiming ext; run `garden triage CG-362 --changes "<feedback>" to unblock`
- 2026-09-08T02:27:56+00:00 triage: changes requested by hand: Delegated operator authorizes continuing. Fix repository identity validation for take --pr: reject URLs for a different
- 2026-09-08T09:08:27+00:00 dispatched revise run 20260908T090825Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~15254 tokens)
- 2026-09-08T09:21:49+00:00 preserved uncommitted worktree changes from run 20260908T090825Z-revise outside the PR: `git stash apply f695da36b81130f465d3330c1d1e6ed4cf2951d8` in /home/joshua/work/worktrees/CG-362 (garden:CG-362:20260908T090825Z-revise:reap)
- 2026-09-08T09:31:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/261: Validated external PR URLs against the configured GitHub repository before resolving their PR number, preventing same-number identity confusion. Added focused host/repository mismatch coverage and verified the final commit with disposable interaction replay, lint, and exact-head GitHub CI. cost=$1.44
- 2026-09-08T09:36:27+00:00 review validation scope expansion: Task-specific served interaction — The required replay covers generic approve/revise/close flows rather than the changed external claim and completion lifecycle.
- 2026-09-08T09:36:28+00:00 stalled: review finding repeated after a revise round: acceptance criterion lacks a passing, evidenced assessment: support claiming ext; run `garden triage CG-362 --changes "<feedback>" to unblock`
- 2026-09-08T10:59:44+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/261
