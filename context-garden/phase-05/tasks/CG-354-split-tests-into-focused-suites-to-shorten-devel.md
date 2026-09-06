---
id: CG-354
title: Split tests into focused suites to shorten development feedback
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
branch: garden/cg-354-split-tests-into-focused-suites-to-shorten-devel
attempts: 1
last_dispatched_at: '2026-09-06T23:11:15+00:00'
created: '2026-09-06T17:04:04+00:00'
updated: '2026-09-06T23:11:15+00:00'
---

## Goal

Shorten task development feedback by organizing tests into focused, independently runnable suites. Workers and reviewers should be able to run the relevant tests during iteration without repeatedly paying for the entire suite.

## Context

Josh requested this in a side conversation on 2026-09-06: "split up the tests so we can run more focused tests (to speed up task development)". Repeated full suites have contributed to slow iteration and memory/temp pressure during phase-05 stabilization. Some tests already have subsystem organization (for example tests/scheduler); build on it rather than reorganizing everything mechanically. CG-338 owns resource admission and CG-344 owns fence-state memory, so this task focuses on test organization, selection and development guidance.

## Acceptance criteria

- [ ] Inventory existing test organization and measured slow setup/tests. Split large mixed-responsibility files and heavyweight shared fixtures where this makes useful subsystem suites independently runnable. Preserve collected test cases, assertions and fixture isolation; demonstrate that the full suite still collects and passes the intended coverage.
- [ ] Provide documented, copyable commands for fast feedback by subsystem and for cross-cutting integration/full validation. Separate slow integration or external-process setup where justified by measurements; ordinary focused tests must not initialize unrelated expensive fixtures.
- [ ] Give workers and reviewers a clear selection guide mapping changed responsibilities to relevant suites, including shared configuration/state/fixture changes that need broader checks. Update relevant development instructions or brief guidance so focused validation is actually used during edits, with an explicit conservative fallback when impact is unclear. A complex automatic dependency-selection engine is not required.
- [ ] Keep full-suite CI as the final regression gate. Targeted passes must be reported as targeted, never as evidence that the whole suite passed; this task does not weaken merge checks or actual-application review requirements.
- [ ] Compare representative small changes before/after under the same environment and resource caps. Record commands, test counts, elapsed time, peak memory and temp use; demonstrate materially faster iteration and explain any unchanged full-suite bottlenecks. Run suites serially for the comparison so extra parallelism cannot masquerade as the improvement.

## Scope and scheduling

Approved phase-05 stabilization work, priority1. Owner authorized a monitored two-run concurrency trial on2026-09-06. Keep full suites on GitHub using the configured helper; local checks and comparisons must remain focused, serial and bounded. Preserve coverage and do not weaken CI or actual-application requirements.

CG361 is concurrently finishing resource enforcement. Keep this task independent: focus on bounded Git fixture subprocess/descendant cleanup, tests/conftest.py, dedicated regression tests and a useful subsystem selection guide. Avoid editing CG361's active tests/test_runners.py, tests/test_web.py, tests/inprocess.py, tests/scheduler/test_resources.py, resource/runner modules, src/garden/brief.py, src/garden/cli/loop.py, docs/codex.md and docs/architecture.md until that work merges. Do not mechanically reorganize files merely to show a split; use measured setup costs to choose useful changes. A selection guide can live in a new document linked from AGENTS.md. Record concurrent-host limitations honestly in timing evidence. No extra model agents, production service changes or parallel local suites.

## Log

- 2026-09-06: Filed at the owner's request from a side conversation; implementation has not started.
- 2026-09-06T21:39:50+00:00 priority 2 -> 1
- 2026-09-06T21:39:50+00:00 approved (cli)


## Measured fixture stall, 2026-09-06 22:08 UTC

During CG-361 validation, a full suite spent 694.80s before reporting 425 passed and a fixture error. A stack sample found pytest PID1962007 in tests/conftest.py git() -> subprocess.run(). Its direct git push child1995747 had already exited128, but orphan sh1995748 and git-receive-pack1995749 retained its stderr pipe in the throwaway test_persona_without_sections_0 remote. CPU time stopped advancing while communicate() waited for pipe EOF. The operator verified process identities, start times, cwd and shared pipe, then terminated only those orphan fixture helpers; pytest immediately finished. Preserve raw evidence /home/joshua/work/operator-test-tmp/CG361-orphan-git-helpers.json. No product worktree Git process was stopped.

Extend the fixture inventory and acceptance evidence to bounded Git subprocess waits and complete helper cleanup, including a child that exits while a descendant holds captured output open. Surface command/stderr/timeouts promptly, preserve useful failed fixtures and avoid declaring unrelated branch code broken. This task should measure useful test execution separately from stuck setup and repeated full-suite retries. The originating git push failure still needs diagnosis; terminating the helpers explains recovery, not the original exit128.
- 2026-09-06T22:59:27+00:00 2026-09-06T22:59:27+00:00: CG-363 merged and installed: full worker suites now offloaded to GitHub, pre-PR avoids local repetition. Retain this task for focused-test selection and the measured unbounded Git fixture pipe/descendant stall; do not duplicate the CI work.
- 2026-09-06T23:10:32+00:00 Owner requested concurrency increase after CI offload. Selected as independent second stabilization task for monitored2-run trial; scoped around in-flight CG361 changes, focused local tests and full GitHub CI.
- 2026-09-06T23:11:15+00:00 dispatched work run 20260906T231053Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10080 tokens)
