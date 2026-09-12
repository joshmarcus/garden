---
id: CG-481
title: Persist worker decisions before publishing waiting status
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: medium
reading:
- src/garden/scheduler/reap.py
- tests/test_decisions.py
- tests/test_qa.py
branch: codex/fix-shared-qa-nochange-contract
pr: https://github.com/joshmarcus/context-garden/pull/379
runner: manual
attempts: 1
last_dispatched_at: '2026-09-09T14:15:02+00:00'
created: '2026-09-09T14:15:01+00:00'
updated: '2026-09-09T14:26:22+00:00'
---

## Goal

Fix the shared QA race where a separate reader sees waiting_human before the associated worker decision has reached state.json.

## Acceptance criteria

- [ ] Persist wont_do and outcome-changing no_change decisions before publishing waiting_human so independent readers can render the corresponding action immediately.
- [ ] Add deterministic regression coverage that fails on the old publication order and passes on the correction; verify existing decision, QA and canary journeys.
- [ ] Upstream the narrow RC11 release correction without overwriting newer main features, bypassing genuine failures or changing installed runtime/source.

## Context

Owner requested root-cause repair of repeated PR CI failures. Main 201ffb0 lacks the decision-before-status correction already present in RC11. Operator root owns this isolated engine fix; ordinary feature PRs remain owned by native Garden. Evidence and red/green results: /home/joshua/work/operator-test-tmp/ci-root-causes-20260909.

## Log

- 2026-09-09T14:15:01+00:00 approved (owner request to address CI root causes)
- 2026-09-09T14:15:02+00:00 dispatched work run 20260909T141502Z-work via manual [human] (fresh session, base main, ~18915 tokens)


## Shared question-path correction

The same race also exposes waiting_human before needs_input question/session_id/session_host/session_harness/question_run reach disk. Save that resume identity before publishing the status and cover it with a separate-reader regression. The deterministic regression fails before the correction. RC11 already includes the decision correction but does not include this question-path correction.
- 2026-09-09T14:21:36+00:00 Operator root published PR379 and expanded the same publication-order fix to worker questions; independent review and exact-head CI required.


## Follow-up split after concurrent merge

PR379 merged at eb1954611 before the question correction was published. CG-482 owns the remaining question/session publication fix in a separate PR. CG481 completion applies only to its original decision-persistence outcome.
- 2026-09-09T14:26:22+00:00 external PR merged and verified on main
