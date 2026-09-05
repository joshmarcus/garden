---
id: CG-178
title: 'The retro ends in a verdict: close the phase, close with follow-ups for the next phase, or reopen
  with named tasks that must land first'
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-182
- CG-197
priority: 1
difficulty: medium
reading:
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/discovered.py
- src/garden/cli.py
- src/garden/inbox.py
- src/garden/web/pages/phase.py
branch: garden/cg-178-the-retro-ends-in-a-verdict-close-the-phase-clos
pr: https://github.com/joshmarcus/context-garden/pull/139
attempts: 2
last_dispatched_at: '2026-09-05T15:36:44+00:00'
created: '2026-09-05T09:40:41+00:00'
updated: '2026-09-05T15:36:44+00:00'
---

## Goal

A retro is not finished until it has decided what happens to the phase. The reconciliation run returns one of three verdicts, the garden files the tasks the verdict names, a person (or the operator acting for them) accepts or changes the verdict on a decision card, and `garden close-phase` follows it.

1. **Close.** Nothing blocks closing; the phase joins the herbarium.
2. **Close with follow-ups.** Nothing blocks closing, and the named items become draft tasks in the next phase, linked to the retro.
3. **Reopen.** The named items must land before the phase can close: they become tasks in this phase, carry a freeze exception so a frozen phase still dispatches them, and `close-phase` refuses until each is done or cancelled.

## Context

Requested by the user on 2026-09-05 during the phase-03 wrap-up. Today `garden retro` writes `docs/retro.md` and a next-goals draft and opens a PR; `garden close-phase` is a separate command with no verdict behind it, so the "should this phase close" decision lives only in the operator's head. Phase 02's retro produced 41 items and the operator sorted them into phase 03 and phase 04 by hand; phase 03's retro is being handled the same way. The freeze exception exists since CG-148; decision cards since CG-100 and CG-112; the retro page (CG-146) is where the verdict and its tasks should be visible.

## Design

- The reconciliation brief asks for a `GARDEN_RETRO` block: `verdict` (`close` | `close_with_followups` | `reopen`), `followups` (title, body, difficulty, priority) and `blocking` (same fields, plus the reason it blocks). The retro document gets a `## Verdict` section that states the choice and lists the tasks by id once filed.
- On reap, the garden files `followups` as drafts in the next phase and `blocking` as drafts in the current phase with `retro_blocking: true` and `freeze_exception: true`, all with `discovered_from: retro:<phase>` provenance, and acts on the verdict: `close` and `close_with_followups` close the phase at once and record the verdict on a notice card (the owner decided on 2026-09-05 that closing does not wait for approval); `reopen` raises a decision card that approves the blocking tasks when accepted, or can be changed to close. Any verdict can be reversed from the phase page (`garden reopen-phase`).
- `garden close-phase` refuses while any `retro_blocking` task is open, names them, and says `--force` overrides; it warns (does not refuse) when the phase has no retro verdict at all.
- The phase page and the retro page show the verdict, who accepted it and when, and the generated tasks with their current status.
- CLI parity: `garden retro` prints the verdict; `garden retro-decide <phase> close|followups|reopen [--note]` accepts or changes it.

## Acceptance criteria

- [ ] The reconciliation result carries a verdict and the task lists; the retro document has a `## Verdict` section.
- [ ] Follow-ups are filed as drafts in the next phase and blocking tasks in the current phase with `retro_blocking` and a freeze exception, all with retro provenance; `close` verdicts close the phase at once with a notice, `reopen` raises a decision card that does what the verdict says when accepted.
- [ ] `garden close-phase` refuses with the names of open blocking tasks unless forced, and warns when no verdict exists.
- [ ] The phase page and the retro page show the verdict and the generated tasks with status.
- [ ] Tests for each verdict path with the fake harness, including the refusal and the override.

## Log

- 2026-09-05T10:31:14+00:00 approved (web)
- 2026-09-05T11:50:51+00:00 dispatched work run 20260905T115043Z-work via local [claude model=claude-opus-4-8] (fresh session, base garden/cg-197-split-cli-py-into-a-cli-package-and-fold-the-fou stacked on CG-197, ~24177 tokens)
- 2026-09-05T11:55:55+00:00 parent CG-197 merged; will rebase onto main when the current run finishes
- 2026-09-05T12:15:08+00:00 parent CG-197 merged; rebase onto main conflicts; the next run must resolve it
- 2026-09-05T12:15:08+00:00 parent CG-197 merged; rebase conflicts; a rebase agent will resolve it cost=$11.64
- 2026-09-05T12:15:29+00:00 dispatched rebase run 20260905T121529Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~4943 tokens)
- 2026-09-05T12:19:46+00:00 opened https://github.com/joshmarcus/context-garden/pull/139 (base main): Rebased onto origin/main; resolved one conflict in src/garden/web/pages/phase.py by keeping both sides — has_retro/_retro_doc/_retro_operator/_persona_scores from main and retro_verdict/_verdict_view from this branch, passing both has_retro and retro_verdict to the phase.html template. Full test suite (615 passed, 3 skipped) and ruff pass. cost=$0.21
- 2026-09-05T12:19:52+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/retro.py, src/garden/scheduler/retro.py); a rebase agent will resolve it
- 2026-09-05T12:20:04+00:00 dispatched rebase run 20260905T122004Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~16425 tokens)
- 2026-09-05T12:28:11+00:00 pre-PR checks failed (lint); revise run will fix before the PR is updated cost=$1.15
- 2026-09-05T12:28:29+00:00 dispatched revise run 20260905T122829Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~23345 tokens)
- 2026-09-05T12:32:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/139: Removed the duplicated "worker_env" dictionary key in the _live_garden config helper in tests/test_retro.py that failed the pre-PR lint check (ruff F601). Lint and the full test suite (619 passed, 3 skipped) now pass. cost=$0.67
- 2026-09-05T12:35:20+00:00 description rewritten by the reviewer cost=$1.30
- 2026-09-05T12:39:28+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T12:41:44+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-178` for one more round, or review on GitHub
- 2026-09-05T12:54:09+00:00 automated review: approve — CG-178 delivers the three-verdict retro end-to-end with retro_blocking tasks, a close-phase guard, verdict surfaces, and thorough tests; full suite (635) and ruff pass. cost=$1.72
- 2026-09-05T13:11:29+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/cli/planning.py, src/garden/scheduler/retro.py, src/garden/web/pages/phase.py); a rebase agent will resolve it
- 2026-09-05T13:13:10+00:00 dispatched rebase run 20260905T131310Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~19895 tokens)
- 2026-09-05T13:14:18+00:00 attempt 1 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); will retry
- 2026-09-05T13:14:42+00:00 dispatched work run 20260905T131442Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~23709 tokens)
- 2026-09-05T13:16:00+00:00 attempt 2 failed: worker exited 1: worker error: success You've hit your monthly spend limit · raise it at claude.ai/settings/usage?from=cc_cli_limit_message · your session limit resets 10:30am (America/New_York); giving up
- 2026-09-05T14:33:46+00:00 re-enabled by hand; revise run will follow
- 2026-09-05T14:34:10+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-178`) or send it back (`garden triage CG-178 --changes "..."`)
- 2026-09-05T15:10:00+00:00 nothing to fix; resumed to in review by hand
- 2026-09-05T15:10:14+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/cli/planning.py, src/garden/cli/scaffold.py, src/garden/retro.py, src/garden/scheduler/retro.py, src/garden/web/pages/phase.py); a rebase agent will resolve it
- 2026-09-05T15:10:35+00:00 dispatched rebase run 20260905T151035Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~29577 tokens)
- 2026-09-05T15:20:53+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/139: Rebased onto origin/main, resolving conflicts in src/garden/cli/planning.py, src/garden/cli/scaffold.py, src/garden/retro.py, src/garden/scheduler/retro.py, src/garden/web/pages/phase.py, and docs/architecture.md (across all 8 commits in the branch, including two CG-189 commits that were already part of this branch's history). Each conflict was resolved by keeping both sides' additions: retro-decide/retro-answer CLI commands alongside main's PANEL_INSIGHT usage panel; close-phase now defers entirely to scheduler.close_phase (which main already had the retro_blocking + open_tasks checks for) plus the no-verdict warning; render_retro_doc's signature merged to carry followups/blocking/next_phase/questions and difficulty/model together; _file_retro_features merged to take both existing_titles (threaded across all filing helpers) and persona_feats; the phase page passes both new_task and retro_verdict context; architecture.md's retro row combined the corrected `retro.difficulty` model tier with the fuller verdict+questions description. Full test suite (721 passed, 3 skipped) and ruff both pass; working tree is clean. cost=$2.09
- 2026-09-05T15:20:53+00:00 2 automated review round(s) used; this PR is yours — run `garden review CG-178` for one more round, or review on GitHub
- 2026-09-05T15:36:24+00:00 automated review requested changes: Core verdict/filing/close-phase logic is solid and well tested, but the retro page never shows the verdict and the reopen decision (and close notice) are never surfaced in the Inbox or digest, leaving a blocking decision invisible outside the phase page. cost=$1.07
- 2026-09-05T15:36:44+00:00 dispatched revise run 20260905T153644Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~20915 tokens)
