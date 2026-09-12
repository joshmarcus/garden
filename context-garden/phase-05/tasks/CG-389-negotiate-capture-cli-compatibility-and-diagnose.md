---
id: CG-389
title: Negotiate capture CLI compatibility and diagnose renderer exit before requesting revisions
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/checks.py
- src/garden/walkthrough.py
- src/garden/scheduler/checkruns.py
- tests/test_browser.py
- tests/test_walkthrough.py
branch: garden/cg-389-negotiate-capture-cli-compatibility-and-diagnose
pr: https://github.com/joshmarcus/context-garden/pull/362
attempts: 1
last_dispatched_at: '2026-09-09T09:50:16+00:00'
created: '2026-09-07T17:59:29+00:00'
updated: '2026-09-09T10:02:09+00:00'
---

## Goal
A pinned controller can capture an older supported worktree without wasting implementation revisions on an incompatible invocation.

## Evidence
CG216 six revision rounds ended with UI renderer did not return a result and no PNG captures. Installed v0.2.0rc1 passes a fourth pages argument; branch c82d123 only accepts three argv entries, exiting2 with empty output. Operator compatibility patch accepted both forms; identical controller invocation then captured14pages/56PNGs in69s,691MiB,no swap. Evidence /home/joshua/work/operator-test-tmp/cg216-capture-compat.

## Acceptance criteria
- [ ] Negotiate or fall back across supported legacy and page-selecting capture entry points without hiding genuine render failures; exercise new controller against old worktree source.
- [ ] Report child exit code, sanitized invocation and empty-output/protocol diagnosis, including quiet exit2; retain stderr and evidence paths.
- [ ] Treat a protocol/infrastructure mismatch as operator/check recovery rather than repeated implementation revisions; preserve PR, feedback and counters.
- [ ] Recheck the same commit successfully after environment/protocol recovery and enqueue normal automated review once; focused mixed-version regression and disposable actual capture evidence.

## Log

- 2026-09-08T12:28:50+00:00 Owner-requested Inbox audit: completed verified source/test reading list; preserved implementation, PR and feedback. Repaired parsed acceptance checklist.
- 2026-09-09T03:56:09+00:00 dispatched work run 20260909T035606Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~25524 tokens)
- 2026-09-09T04:02:40+00:00 preserved uncommitted worktree changes from run 20260909T035606Z-work outside the PR: `git stash apply d06a1fd3fe377e2ca34643a158e083a19b5c98d9` in /home/joshua/work/worktrees/CG-389 (garden:CG-389:20260909T035606Z-work:reap)
- 2026-09-09T04:02:40+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T04:04:02+00:00 opened https://github.com/joshmarcus/context-garden/pull/362 (base main): Committed legacy/page-selecting walkthrough renderer negotiation and trusted protocol-mismatch recovery in 83a88ca29. Verified 89 focused tests, Ruff, and a disposable actual /now capture producing four 1280/390 light/dark PNGs. cost=$0.66
- 2026-09-09T04:09:32+00:00 automated review requested changes: Compatibility fallback and diagnostics are well covered, but the scheduler’s recovery classification trusts a child-controlled summary and can hide a genuine renderer failure. cost=$0.36
- 2026-09-09T04:10:02+00:00 dispatched revise run 20260909T040959Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~26717 tokens)
- 2026-09-09T04:11:05+00:00 preserved uncommitted worktree changes from run 20260909T040959Z-revise outside the PR: `git stash apply 602962cb7cb5a96e1a7b14a436d7aca51428d97b` in /home/joshua/work/worktrees/CG-389 (garden:CG-389:20260909T040959Z-revise:reap)
- 2026-09-09T04:11:05+00:00 environment stop (quota): quota limit hit on codex; not counted as an attempt; dispatch paused for codex until a probe succeeds; feedback restored, will retry the revise round
- 2026-09-09T09:42:49+00:00 dispatched revise run 20260909T094246Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~26871 tokens)
- 2026-09-09T09:45:16+00:00 preserved uncommitted worktree changes from run 20260909T094246Z-revise outside the PR: `git stash apply 5a66c6ddef559915565a8f085079f9950e75bb6e` in /home/joshua/work/worktrees/CG-389 (garden:CG-389:20260909T094246Z-revise:reap)
- 2026-09-09T09:45:16+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T09:46:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/362: Restricted capture protocol recovery to the generated UI wrapper's exact source and capture_protocol_mismatch metadata, preventing renderer-controlled summaries from hiding failures. Verified with 99 focused tests and Ruff on commit b7335aa32. cost=$0.32
- 2026-09-09T09:47:21+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/walkthrough.py, tests/scheduler/test_reap.py); a rebase agent will resolve it
- 2026-09-09T09:49:58+00:00 automated review: approve — Capture compatibility negotiation, diagnostics, and trusted scheduler recovery meet the requested outcomes without masking child-reported renderer failures. cost=$0.39
- 2026-09-09T09:50:16+00:00 dispatched rebase run 20260909T095012Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1854 tokens)
- 2026-09-09T09:52:26+00:00 preserved uncommitted worktree changes from run 20260909T095012Z-rebase outside the PR: `git stash apply 4e9d5fbee45a47b8ae7b48cf3adba05156a271d2` in /home/joshua/work/worktrees/CG-389 (garden:CG-389:20260909T095012Z-rebase:reap)
- 2026-09-09T09:53:37+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/362: Rebased CG-389 onto origin/main and resolved walkthrough.py and test_reap.py conflicts. cost=$0.02
- 2026-09-09T09:56:06+00:00 automated review: approve — Capture CLI negotiation and trusted scheduler recovery meet the requested outcomes without masking reported renderer failures. cost=$0.34
- 2026-09-09T10:00:53+00:00 rebasing before merge; reviewed remote head already contains main; not rebased or pushed
- 2026-09-09T10:02:09+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/362
