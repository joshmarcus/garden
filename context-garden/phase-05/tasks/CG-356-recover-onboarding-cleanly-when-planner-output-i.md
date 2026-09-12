---
id: CG-356
title: Recover onboarding cleanly when planner output is rejected
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: medium
reading: []
branch: garden/cg-356-recover-onboarding-cleanly-when-planner-output-i
pr: https://github.com/joshmarcus/context-garden/pull/276
attempts: 1
last_dispatched_at: '2026-09-08T09:36:41+00:00'
created: '2026-09-06T17:34:36+00:00'
updated: '2026-09-08T09:45:26+00:00'
---

## Goal

A failed onboarding planner step leaves an understandable, recoverable draft instead of requiring the user to untangle a half-created product before retrying.

## Evidence

Operator inspection of #216 on 2026-09-06: onboard_project writes config, product, conventions and phase before calling the planner. Invalid or ambiguous provenance correctly rejects the plan, but a repeated onboard command then encounters the existing-product protection. The first successful onboarding path is validated; planner-failure recovery needs a separate explicit path.

## Acceptance criteria

- [ ] Reproduce planner failure and unsupported-provenance rejection with a disposable existing garden; preserve its pre-existing configuration and files.
- [ ] Offer a deterministic retry/resume or transactional rollback for generated onboarding drafts. Never remove or overwrite owner edits or an unrelated existing product.
- [ ] Explain which draft files were created, whether anything was imported, and the exact recovery action. Do not misreport a partial run as successful onboarding.
- [ ] Exercise failure then successful retry, changed draft files, and existing-product collision. Do not launch task workers or approve drafts implicitly.

## Scheduling

Phase-05 stabilization follow-up to CG-215. Preserve fast-forward hold until the current PR queue is handled.

## Log

- 2026-09-06T17:35:33+00:00 approved (cli)
- 2026-09-07T07:06:57+00:00 dispatched work run 20260907T070629Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9059 tokens)
- 2026-09-07T07:22:51+00:00 preserved uncommitted worktree changes from run 20260907T070629Z-work outside the PR: `git stash apply 49c0252f00c20c7a30787f2d43206da3c4b34795` in /home/joshua/work/worktrees/CG-356 (garden:CG-356:20260907T070629Z-work:reap)
- 2026-09-07T07:24:53+00:00 opened https://github.com/joshmarcus/context-garden/pull/276 (base main): Onboarding now rolls back its generated scaffold when planner execution or output validation fails, preserving prior garden files and owner edits. The failure explains what was rolled back, confirms no tasks were imported or approved, and gives the recovery action. cost=$1.05
- 2026-09-07T07:28:22+00:00 automated review requested changes: The normal planner-failure rollback and clean retry work, but recovery breaks when an owner edits a generated draft: the retained file causes the advertised retry to fail. Failure reporting also omits generated/restored configuration files. cost=$0.28
- 2026-09-07T07:28:47+00:00 dispatched revise run 20260907T072845Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10054 tokens)
- 2026-09-07T07:44:53+00:00 preserved uncommitted worktree changes from run 20260907T072845Z-revise outside the PR: `git stash apply 752c750575591b42cc5c7b64715f1924bbb3a851` in /home/joshua/work/worktrees/CG-356 (garden:CG-356:20260907T072845Z-revise:reap)
- 2026-09-07T07:46:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/276: Planner rejection now relocates retained owner draft content out of the product collision path, reports each scaffold file's recovery disposition, and gives a usable retry command. The final commit d6567c3bc9121d213f4a05d721846b416af865dd passed exact-commit CI. cost=$0.84
- 2026-09-07T07:49:15+00:00 automated review requested changes: Rollback behavior and focused coverage are sound, but the advertised retry command is not reliably executable when repository or garden paths contain spaces. The focused onboarding suite passes 22 tests and lint passes. cost=$0.33
- 2026-09-07T07:49:53+00:00 dispatched revise run 20260907T074952Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10006 tokens)
- 2026-09-07T07:58:02+00:00 preserved uncommitted worktree changes from run 20260907T074952Z-revise outside the PR: `git stash apply 758fba0ad2a0be1761cd2275c4ba8cb37c9a29ee` in /home/joshua/work/worktrees/CG-356 (garden:CG-356:20260907T074952Z-revise:reap)
- 2026-09-07T07:59:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/276: Planner-rejection recovery now prints a shell-safe onboarding retry command. Coverage proves paths with spaces parse correctly and retry produces draft tasks. cost=$0.41
- 2026-09-07T15:45:45+00:00 review validation scope expansion: Fresh served interaction evidence — The required scheduler replay manifest path was absent, so the reviewed head was exercised through a disposable HTTP harness around the real onboarding implementation.
- 2026-09-07T15:45:46+00:00 automated review requested changes: Onboarding rollback safely preserves existing garden content and owner edits, reports recovery precisely, and supports a clean retry producing draft-only tasks. Code is approved; the supplied description rewrite updates stale verification evidence to the reviewed head. cost=$0.50
- 2026-09-07T16:37:55+00:00 Temporary operator incident admission hold to reserve next drained slot for P0 CG385 recovery; preserve all work. Restore original runner from docs/incidents/cg385-recovery-admission-holds.json after CG385 starts.
- 2026-09-07T16:39:06+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-356`) or send it back (`garden triage CG-356 --changes "..."`)
- 2026-09-07T17:01:39+00:00 Operator restored original runner after CG385 recovery repair acquired actual execution slot. Shared cap remains1.
- 2026-09-07T18:59:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T18:59:47+00:00 Delegated operator Inbox audit: cleared stale manual-hold stop after verified normal runner restoration; existing implementation, PR and pending review feedback retained. No owner decision required.
- 2026-09-07T21:11:45+00:00 dispatched revise run 20260907T211142Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11827 tokens)
- 2026-09-07T21:28:45+00:00 preserved uncommitted worktree changes from run 20260907T211142Z-revise outside the PR: `git stash apply a86e94146a0935559d1a8d49240a65589ee1d4fb` in /home/joshua/work/worktrees/CG-356 (garden:CG-356:20260907T211142Z-revise:reap)
- 2026-09-07T21:33:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/276: Replayed the reviewed onboarding recovery through a disposable served HTTP harness and refreshed the PR description evidence. Exact-commit CI passed for 697930e297d9466dfb5bde75a92e220751a9a14d. cost=$0.97
- 2026-09-07T21:41:30+00:00 review validation scope expansion: Partial import failure during import_plan — Code inspection found that planner-output validation continues after the rollback-protected block and can mutate the garden before raising.
- 2026-09-07T21:41:31+00:00 stalled: review finding repeated after a revise round: running-app evidence incomplete: scheduler-produced interaction replay manifest ; run `garden triage CG-356 --changes "<feedback>" to unblock`
- 2026-09-08T02:30:03+00:00 triage: changes requested by hand: Delegated operator authorizes one focused revision. Repair the concrete findings below before self-review; preserve actu
- 2026-09-08T08:56:24+00:00 dispatched revise run 20260908T085621Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12440 tokens)
- 2026-09-08T09:08:13+00:00 preserved uncommitted worktree changes from run 20260908T085621Z-revise outside the PR: `git stash apply 882b10a99378b4ceedacabd1aa21408c7a3f3e44` in /home/joshua/work/worktrees/CG-356 (garden:CG-356:20260908T085621Z-revise:reap)
- 2026-09-08T09:09:33+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/276: Onboarding now rolls back task files and Store lock side effects when import-time validation fails, leaving the prior garden byte-for-byte intact and retryable. The focused suite, served HTTP replay, lint, and exact-head GitHub CI passed. cost=$1.05
- 2026-09-08T09:17:29+00:00 review validation scope expansion: Fresh served interaction evidence — The scheduler replay manifest specified by the validation plan was absent, so the exact head was independently exercised through a disposable HTTP wrapper around the real onboarding implementation.
- 2026-09-08T09:17:31+00:00 automated review requested changes: Onboarding failures now roll back generated and partially imported files, preserve owner content, and permit a clean draft-only retry. Focused tests, lint, fresh served interaction, and exact-head CI passed. cost=$0.84
- 2026-09-08T09:17:46+00:00 dispatched revise run 20260908T091744Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12447 tokens)
- 2026-09-08T09:31:14+00:00 preserved uncommitted worktree changes from run 20260908T091744Z-revise outside the PR: `git stash apply f32e3eb9127d5ab8d77fcc8289775ddf351de8b4` in /home/joshua/work/worktrees/CG-356 (garden:CG-356:20260908T091744Z-revise:reap)
- 2026-09-08T09:32:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/276: Added durable, reproducible served HTTP interaction evidence for onboarding recovery. The exact-head CI workflow passed, and the unrelated design snapshot edit was restored unchanged. cost=$1.44
- 2026-09-08T09:36:25+00:00 review validation scope expansion: Fresh served interaction evidence — The scheduler-provided manifest exercised generic task-management flows rather than onboarding, so the committed CG-356 HTTP replay was independently run against the reviewed head.
- 2026-09-08T09:36:26+00:00 automated review requested changes: Onboarding failures transactionally restore prior garden content, preserve owner edits, report recovery precisely, and allow a clean draft-only retry. Focused tests, lint, conflict scanning, and an exact-head disposable served replay passed. cost=$0.41
- 2026-09-08T09:36:41+00:00 dispatched revise run 20260908T093639Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~12939 tokens)
- 2026-09-08T09:45:26+00:00 marked done without merging (web)
