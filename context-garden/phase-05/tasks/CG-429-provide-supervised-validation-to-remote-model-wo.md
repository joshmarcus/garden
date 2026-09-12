---
id: CG-429
title: Provide supervised validation to remote model workers
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/remote_worker.py
- src/garden/runner/local.py
- src/garden/run_supervisor.py
- src/garden/validation.py
- src/garden/managed_worker.py
- tests/test_remote_worker.py
- tests/test_runners.py
branch: codex/cg429-remote-validation
pr: https://github.com/joshmarcus/context-garden/pull/314
runner: manual
created: '2026-09-08T12:51:03+00:00'
updated: '2026-09-08T13:47:12+00:00'
---

## Goal

Remote workers must receive the functioning supervised validation command required by their briefs.

## Evidence

Owner reported multiple AWS workers saying GARDEN_VALIDATION_RUNNER is empty on2026-09-08. Deployed remote_worker.execute_claim launches the model harness directly with _env, while the local runner uses garden.run_supervisor, which establishes the validation executable, run directory and owner identity. Setting only the executable variable would still fail garden.validation's owner/run preflight.

## Acceptance criteria

- [ ] Launch remote model work/review/persona processes through the supported host-local supervision path, providing a valid validation executable and per-run ownership/metadata directory without controller paths or credentials.
- [ ] A real remote harness invokes garden.validation successfully; nested validation uses host limits and per-owner serialization, propagates nonzero results, and leaves auditable per-run status. No unsupervised fallback.
- [ ] Preserve stdin, streamed transcript/final results, signal handling, host lock, lease checks and separate check-mode execution. Remote runtime identities must be created locally rather than inherited from unrelated execution state.
- [ ] Focused remote lifecycle/validation regressions, lint, and actual bounded AWS verification pass before versioned worker rollout. Stress/load tests remain opt-in.

## Log

- 2026-09-08T12:51:03+00:00 Direct operator repair reserved after owner report; deployment drain already active. Do not duplicate implementation.
- 2026-09-08T13:26:22+00:00 Operator self-reviewed sourcec8c1a96e;37remote tests and exactsourceCI34230204597pass. Candidate41d0da0cfullCI34230307312passes;actualAWSnewremote validation regressions pass. Versioned runtime rollout is pending.
- 2026-09-08T13:47:12+00:00 PR314 verified MERGED at 0e517fa9c479dd881d84726cff79fa8afddb31ca after operator self-review, 37 focused tests/lint and both exact source CI runs passed. Squash merge verified through GitHub because ancestry-only mark-done cannot recognize the squashed head. Approved code is deployed in rc5 on controller and six hosts.
