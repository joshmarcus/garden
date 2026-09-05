---
id: CG-227
title: garden retro's own persona-phase and reconcile dispatch aren't gated on a paused harness
status: done
product: context-garden
phase: phase-04
depends_on:
- CG-212
priority: 1
difficulty: easy
reading:
- src/garden/harness.py
- src/garden/scheduler/reap.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/budget.py
- src/garden/inbox.py
- context-garden/phase-02-friction/tasks/CG-033-an-environment-error-in-a-worker-pauses-dispatch.md
branch: garden/cg-227-garden-retro-s-own-persona-phase-and-reconcile-d
pr: https://github.com/joshmarcus/context-garden/pull/183
discovered_from: CG-212
attempts: 1
last_dispatched_at: '2026-09-05T21:24:36+00:00'
created: '2026-09-05T17:49:54+00:00'
updated: '2026-09-05T22:01:54+00:00'
---

## Goal

`start_retro`'s loop over missing personas (`dispatch_persona_phase`, which now goes through the gated `dispatch_aux`) and `_dispatch_retro_run` (used by `_dispatch_reconcile`, which dispatches its own run directly via `runner_for`/`runner.start`, not through `dispatch_aux`) can still start a run against a harness that is currently paused, or fail to recognise a quota `env_error` if one hits mid-retro. `dispatch_persona_phase` will now raise if paused (an improvement from this round), but the reconcile dispatch has neither the gate nor env_error handling.

## Context

Out of scope for CG-212's reviewer feedback (which named trial contenders, automated review, and persona/compare aux runs specifically); retro is a rarer, human-triggered flow so the risk is lower, but the same account-limit trouble could still strand a retro mid-flight without pausing the harness for other dispatch.

## Acceptance criteria

- [ ] `_dispatch_retro_run` refuses (or the retro flow otherwise handles) a paused harness before dispatching.
- [ ] `reap_retro`'s reconcile-collection path recognises `env_error` and pauses the harness instead of treating it as a failed retro.

## Provenance

Discovered by CG-212 (A usage or spend-limit error from a harness pauses dispatch for that harness and leaves the task ready, instead of burning attempts and failing tasks) during run `20260905T172529Z-revise`.

## Log

- 2026-09-05T17:49:54+00:00 discovered by CG-212
- 2026-09-05T19:16:28+00:00 approved (web)
- 2026-09-05T19:30:39+00:00 dispatched work run 20260905T193023Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus stacked on CG-212, ~18448 tokens)
- 2026-09-05T19:43:34+00:00 opened https://github.com/joshmarcus/context-garden/pull/183 (base garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus): Gated the retro's reconcile dispatch on a paused harness: _dispatch_retro_run now refuses when paused, reap_retro defers the reconcile pre-dispatch instead of raising, and env_error mid-reconcile pauses the harness and retries rather than being read as a failed retro. cost=$1.87
- 2026-09-05T19:47:55+00:00 automated review: approve — Both acceptance criteria are met: _dispatch_retro_run now refuses a paused harness before dispatching, and reap_retro's reconcile path recognizes env_error and pauses the harness instead of failing the retro; tests and lint pass and the diff is tightly scoped. cost=$0.70
- 2026-09-05T20:37:59+00:00 PR conflicts with garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus; rebased onto garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus mechanically and force-pushed
- 2026-09-05T20:45:42+00:00 automated review: approve — Both criteria are met: the reconcile dispatch goes through the shared paused-harness gate, reap_retro defers rather than raising, and a quota env_error mid-reconcile pauses the harness and retries instead of dropping the retro. Full suite and lint pass. cost=$1.79
- 2026-09-05T20:53:43+00:00 PR conflicts with garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus; rebase onto garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus conflicts (src/garden/scheduler/review.py, src/garden/scheduler/trials.py, tests/scheduler/test_quota.py); a rebase agent will resolve it
- 2026-09-05T20:54:02+00:00 dispatched rebase run 20260905T205402Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus, conflict only; easy tier, ~19595 tokens)
- 2026-09-05T21:02:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/183: Rebased CG-227 onto CG-212's updated tip. The conflict was entirely within commit 16e2bab, an older version of a CG-212 commit whose content was fully superseded by later CG-212 fixups already in the new base — resolved review.py, trials.py, and test_quota.py to match the base tip exactly (verified byte-identical), making that commit a no-op which git auto-skipped. CG-227's own commit (retro.py, test_retro.py) then applied cleanly with no changes needed. Full test suite (938 passed) and ruff lint pass. cost=$0.95
- 2026-09-05T21:07:28+00:00 automated review: approve — Both acceptance criteria are correctly implemented and tested: the reconcile dispatch is gated on the paused-harness check via the standard `_raise_if_harness_paused`/`resolved_harness_name` helpers, and a mid-reconcile quota env_error now pauses the harness and defers the entry instead of dropping the retro. Full suite (938 passed) and lint pass; diff is tightly scoped to retro.py and its tests. cost=$0.57
- 2026-09-05T21:24:17+00:00 PR conflicts with garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus; rebase onto garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus conflicts (src/garden/harness.py, tests/fake_claude.py); a rebase agent will resolve it
- 2026-09-05T21:24:36+00:00 dispatched rebase run 20260905T212435Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-212-a-usage-or-spend-limit-error-from-a-harness-paus, conflict only; easy tier, ~16478 tokens)
- 2026-09-05T21:36:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/183: Rebased CG-227 onto CG-212's updated tip. The first conflict (harness.py, fake_claude.py) was an older CG-212 commit whose content was fully superseded by later CG-212 fixups already in the new base; resolved to match the base tip exactly. The next conflicts (quota.py, reap.py, runner/base.py, inprocess.py, test_quota.py, review.py, trials.py) followed the same pattern across two more old CG-212 commits, also resolved to the base tip, both becoming no-ops that git auto-skipped. The auto-merge for runner/local.py silently duplicated the probe()/_probe_launch() methods across two commits (no conflict marker was raised there since it was an insertion, not a textual clash) - caught this by diffing the rebased tree against origin's tip, then fixed it properly via git rebase --onto so each of those two commits' local.py hunks resolve as flagged conflicts favoring the base (which already had the final, single-copy implementation), collapsing both to true no-ops. CG-227's own commit (retro.py, test_retro.py) then applied cleanily. Full test suite (950 passed, 3 skipped) and ruff lint pass; the only net diff against the new base is CG-227's own commit. cost=$1.58
- 2026-09-05T21:40:45+00:00 automated review: approve — The reconcile dispatch is now gated on a paused harness at both the direct-dispatch and reap_retro pre-dispatch points, and a mid-reconcile quota env_error now pauses the harness and retries instead of dropping the retro; diff is tightly scoped, tests and lint pass. cost=$0.54
- 2026-09-05T21:51:16+00:00 stack parent CG-212 merging; retargeted this PR to main before the parent branch is deleted
- 2026-09-05T21:52:53+00:00 parent CG-212 merged; rebased onto main and retargeted the PR
- 2026-09-05T21:57:22+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-05T22:00:20+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-05T22:01:54+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/183
