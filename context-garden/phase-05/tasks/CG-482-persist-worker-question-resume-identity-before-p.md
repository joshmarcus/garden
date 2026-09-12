---
id: CG-482
title: Persist worker question resume identity before publishing waiting status
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
branch: codex/fix-worker-question-publication
pr: https://github.com/joshmarcus/context-garden/pull/380
runner: manual
attempts: 1
last_dispatched_at: '2026-09-09T14:26:24+00:00'
created: '2026-09-09T14:26:20+00:00'
updated: '2026-09-09T14:30:14+00:00'
---

## Goal

Prevent a separate reader from seeing waiting_human before the worker question and session identity are saved. An immediate answer must be able to resume the worker that asked.

## Acceptance criteria

- [ ] Persist question, session_id, session_host, session_harness and question_run before publishing WAITING_HUMAN.
- [ ] Add a deterministic separate-State-reader regression proving the old missing resume identity and the corrected publication order. Preserve ordinary decision/question/QA/canary behavior.

## Context

Owner requested CI root-cause repairs. CG481/PR379 fixed decision publication and was merged while this matching question correction was being prepared; this task is the remaining narrow follow-up. Source and red/green evidence are in /home/joshua/work/operator-test-tmp/ci-root-causes-20260909. Installed RC11 has the decision fix but does not yet include this question correction.

## Log

- 2026-09-09T14:26:20+00:00 approved (owner CI root-cause repair follow-up)
- 2026-09-09T14:26:24+00:00 dispatched work run 20260909T142624Z-work via manual [human] (fresh session, base main, ~18891 tokens)
- 2026-09-09T14:30:14+00:00 external PR merged and verified on main
