---
id: CG-198
title: A restart reaps finished-but-unreaped runs of every mode before its first tick, and a dispatch
  onto a dirty worktree stashes and continues
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 2
difficulty: medium
reading: []
branch: garden/cg-198-a-restart-reaps-finished-but-unreaped-runs-of-ev
pr: https://github.com/joshmarcus/context-garden/pull/154
attempts: 2
last_dispatched_at: '2026-09-05T16:33:02+00:00'
created: '2026-09-05T10:30:00+00:00'
updated: '2026-09-05T17:35:11+00:00'
---

## Goal

Two restarts on 2026-09-05 lost a review verdict the old process had reaped in its last tick (CG-150 at 05:00, CG-176 at 10:01) and each needed a fresh review. After the WSL outage, CG-176's next dispatch failed with `git merge --ff-only … Your local changes` because the killed worker left uncommitted edits. Also: `finalize` emits `run_finished` before the first terminal `run.save()`, so a kill during the fence check re-emits it (staff engineer).

## Provenance

From the phase-03 persona reviews of 2026-09-05 (product-manager:medium, user:low, staff-engineer:medium); filed by the operator so that every finding is kept (see CG-187). Reports: `context-garden/phase-03/docs/reviews/`.

## Acceptance criteria

- [ ] On start the scheduler walks run records of every mode, reaps those whose process is gone and whose output is complete, applies verdicts and results as a normal reap would, and only then ticks; a test kills a scheduler after a review finishes and starts another.
- [ ] A dispatch that finds a dirty worktree stashes the edits under a named stash, logs it on the task, and proceeds; the stash is listed on the task page.
- [ ] `run_finished` is emitted once per run, after the terminal save.

## Log

- 2026-09-05T10:31:18+00:00 approved (web)
- 2026-09-05T12:48:16+00:00 dispatched work run 20260905T124807Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4500 tokens)
- 2026-09-05T13:09:42+00:00 opened https://github.com/joshmarcus/context-garden/pull/154 (base main): A restarted scheduler now reaps finished-but-unreaped runs of every mode before its first tick (recovering a review verdict the old process reaped but never persisted), a dispatch onto a worktree a killed worker left dirty stashes the edits under a named stash and continues, and run_finished is emitted once per run after the finalize outcome is persisted. cost=$8.15
- 2026-09-05T13:12:48+00:00 automated review produced no verdict (worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_messa) cost=$0.84
- 2026-09-05T13:34:49+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/__init__.py); a rebase agent will resolve it
- 2026-09-05T13:35:05+00:00 dispatched rebase run 20260905T133505Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~6729 tokens)
- 2026-09-05T13:36:10+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:36:27+00:00 dispatched work run 20260905T133627Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~4927 tokens)
- 2026-09-05T13:37:32+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:48+00:00 re-enabled by hand; revise run will follow
- 2026-09-05T14:34:10+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-198`) or send it back (`garden triage CG-198 --changes "..."`)
- 2026-09-05T15:10:01+00:00 nothing to fix; resumed to in review by hand
- 2026-09-05T15:10:18+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/__init__.py); a rebase agent will resolve it
- 2026-09-05T15:13:20+00:00 dispatched rebase run 20260905T151320Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~7057 tokens)
- 2026-09-05T15:20:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/154: Rebased onto origin/main; resolved the single conflict in src/garden/scheduler/__init__.py by keeping both main's `_guard` helper (CG-203) and this branch's `_reap_all`/`reap_on_start` methods (CG-198), which the rest of the file already called. Full test suite (709 passed) and ruff both pass post-rebase; verified none of the PR's three claims (start-up reap of every mode, dirty-worktree stash, single run_finished emit) were already present in main, so no pr_body change is needed. cost=$0.49
- 2026-09-05T15:32:04+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/dispatch.py, src/garden/web/templates/task.html); a rebase agent will resolve it
- 2026-09-05T15:32:23+00:00 dispatched rebase run 20260905T153223Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~12021 tokens)
- 2026-09-05T15:37:46+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/154: Rebased onto origin/main. Resolved conflicts in src/garden/scheduler/dispatch.py (kept main's `_sweep_terminal_state` (CG-195) alongside this branch's `_stash_dirty_worktree`, both called elsewhere in the file) and src/garden/web/templates/task.html (kept the new stashed-changes panel, combined with main's newer `and not task.status.terminal` guard on the pending-feedback panel). Full suite (734 passed, 3 skipped) and ruff both pass post-rebase. Verified main doesn't already contain the reap-on-start, dirty-worktree-stash, or single run_finished changes, so no pr_body update is needed. cost=$0.41
- 2026-09-05T15:37:46+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-198` for one more round, or review on GitHub
- 2026-09-05T15:37:48+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/templates/task.html); a rebase agent will resolve it
- 2026-09-05T15:38:53+00:00 automated review: request_changes — The dirty-worktree stash and single run_finished emit are correct and well-tested, but the restart's review-recovery path can duplicate the posted GitHub review comment in exactly the crash scenario the task describes. cost=$1.30
- 2026-09-05T15:42:52+00:00 nothing to fix; resumed to in review by hand
- 2026-09-05T15:42:57+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/web/templates/task.html); a rebase agent will resolve it
- 2026-09-05T15:43:17+00:00 dispatched rebase run 20260905T154317Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~8693 tokens)
- 2026-09-05T15:49:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/154: Rebased onto origin/main; resolved the single conflict in src/garden/web/templates/task.html by combining both timeline event-kind chains — kept main's newer 'rebase', 'merge_head', 'feedback_ignored', and 'rebased_stale_base' event cases alongside this branch's 'stashed' event case (inserted right after 'moved', matching its original position). Full test suite (751 passed, 3 skipped) and ruff both pass post-rebase. Verified main still doesn't contain the reap-on-start, dirty-worktree-stash, or single run_finished changes, so no pr_body update is needed. cost=$0.32
- 2026-09-05T15:49:01+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-198` for one more round, or review on GitHub
- 2026-09-05T15:59:25+00:00 automated review produced no verdict (worker error: success Not logged in · Please run /login) cost=$0.00
- 2026-09-05T16:32:43+00:00 automated review requested changes: Dirty-worktree stash and single run_finished emit are correct and tested, but the restart's review-verdict recovery path still duplicates the posted GitHub comment (and other side effects) in exactly the crash scenario the task describes — a bug an earlier review round on this PR already flagged and which was dismissed by hand without a fix. cost=$0.96
- 2026-09-05T16:33:02+00:00 dispatched revise run 20260905T163302Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~6625 tokens)
- 2026-09-05T16:49:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/154: Fixed the reviewer-flagged bug where a restart's crash-recovery review path could duplicate a posted GitHub comment (and task log/transition/notify) by saving state.json immediately after applying a review verdict, plus a GitHub-side idempotency backstop for the narrower remaining window; added two tests reproducing both windows. cost=$2.04
- 2026-09-05T16:49:33+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-198` for one more round, or review on GitHub
- 2026-09-05T17:16:41+00:00 description rewritten by the reviewer cost=$1.00
- 2026-09-05T17:29:46+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T17:32:05+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-05T17:35:11+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/154
