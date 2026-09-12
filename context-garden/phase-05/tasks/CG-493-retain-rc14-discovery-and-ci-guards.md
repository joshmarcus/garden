---
id: CG-493
title: Retain RC14 discovery and CI guards
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading: []
branch: garden/cg-493-retain-rc14-discovery-and-ci-guards
pr: https://github.com/joshmarcus/context-garden/pull/396
last_dispatched_at: '2026-09-09T20:52:05+00:00'
created: '2026-09-09T18:26:32+00:00'
updated: '2026-09-10T01:59:16+00:00'
---

## Goal

Retain the two narrow source safeguards introduced while validating RC14 on current main.

## Context

PR 395 was prepared from fresh main after the RC14 candidate froze. The source is already
implemented and focused-tested; this task exists so Garden owns the normal exact-head review
and merge lifecycle instead of leaving the PR untracked.

## Acceptance criteria

- [ ] Persistent concurrent task-file edits cannot trap discovery in an unbounded parse loop;
      the next operation retries after the bounded fallback.
- [ ] GitHub CI ignores only the ephemeral runner's unrelated Google Chrome apt source before
      Playwright installs Chromium dependencies from the unchanged Ubuntu repositories.
- [ ] The exact PR head passes applicable CI and substantive review before Garden merges it.

## Out of scope

- RC14 release metadata, deployment helpers, PR 393 source, and unrelated performance work.

## Log

- 2026-09-09T18:27:06+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/395 (pr_number none -> 395)
- 2026-09-09T18:27:07+00:00 Linked exact prepared retention PR for normal Garden review
- 2026-09-09T19:24:40+00:00 automated review: approve — The bounded discovery fallback and narrowly scoped Chrome apt-source removal satisfy the task without unrelated changes. cost=$0.42
- 2026-09-09T19:27:23+00:00 automated review requested changes: The exact reviewed head 7b989f46a83151a22f410f5f99ecb73d72edffb0 omits both RC14 safeguards. They exist only on the separate origin/codex/retain-rc14-performance-guards history, whose commits are not ancestors of this head. cost=$0.35
- 2026-09-09T19:33:59+00:00 dispatched revise run 20260909T193357Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~15426 tokens)
- 2026-09-09T19:37:20+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T19:38:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/396 (base main): Restored both RC14 safeguards on the actual task branch and strengthened the persistent-churn regression to prove the following operation retries. Exact local head b22755853 passed the two focused discovery tests and repository lint; GitHub CI and substantive review remain for Garden's normal post-publication gate. cost=$0.67
- 2026-09-09T19:41:05+00:00 automated review requested changes: The two RC14 safeguards are correctly restored at the exact PR head, but its required GitHub CI has not completed. cost=$0.36
- 2026-09-09T19:42:49+00:00 dispatched revise run 20260909T194245Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~15384 tokens)
- 2026-09-09T19:48:36+00:00 worker found no change to make: The requested source is already correct and committed. Review requested waiting for exact-head CI rather than a code change, and an exact-head workflow has now passed.; reconciling with checks and a fresh review
- 2026-09-09T19:49:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/396: Exact PR head b2275585313b574d877ea9719aad27ba95f0afb7 retains both safeguards and completed a successful full GitHub CI run. Focused discovery tests, the previously failing canary node, and repository lint also pass locally; the duplicate CI run's lone canary failure did not reproduce. cost=$0.62
- 2026-09-09T19:51:04+00:00 CI failure
- 2026-09-09T19:53:28+00:00 automated review: approve — Both RC14 safeguards are correctly retained with focused regression coverage and no unrelated source changes. cost=$0.33
- 2026-09-09T20:09:00+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T20:21:23+00:00 dispatched revise run 20260909T202119Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16168 tokens)
- 2026-09-09T20:25:51+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T20:27:06+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/396: Serialized worker-answer dispatch with scheduler ticks and added regression coverage for the stale waiting_human race. Commit b7671295e passes 47 focused tests, including the canary, plus repository lint; Garden must still obtain CI and review for this newly published exact head before merging. cost=$0.96
- 2026-09-09T20:29:30+00:00 automated review requested changes: The RC14 discovery and CI safeguards are correctly retained, but the PR now includes an unrelated answer/tick synchronization change and exact-head CI is still pending. cost=$0.35
- 2026-09-09T20:46:45+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T20:52:05+00:00 dispatched revise run 20260909T205202Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16269 tokens)
- 2026-09-09T20:54:15+00:00 discovered work filed: CG-497
- 2026-09-09T20:54:15+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T20:55:31+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/396: Reverted the unrelated answer/tick synchronization change, leaving only the bounded discovery retry safeguard, its regression coverage, and the narrow CI apt-source cleanup. Exact head cfa2e33e19f592c02373da8c089552035af029d4 passes focused tests, lint, and diff checks; Garden must still obtain exact-head CI and substantive review after publishing it. cost=$0.43
- 2026-09-09T20:57:54+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: the exact pr head passes applicable ci; run `garden triage CG-493 --changes "<feedback>" to unblock`
- 2026-09-09T21:23:03+00:00 nothing to fix; resumed to in review by hand
- 2026-09-10T01:59:16+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/396
