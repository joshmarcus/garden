---
id: CG-616
title: Make Playwright tasks and browser validation opt-in
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/brief.py
- src/garden/scheduler/checkruns.py
- src/garden/config.py
- src/garden/walkthrough.py
branch: garden/cg-616-make-playwright-tasks-and-browser-validation-opt
pr: https://github.com/joshmarcus/context-garden/pull/481
runner: remote
attempts: 2
last_dispatched_at: '2026-09-11T04:16:17+00:00'
created: '2026-09-11T00:34:12+00:00'
updated: '2026-09-11T04:57:14+00:00'
---

## Goal

Do not run Playwright tasks or browser-dependent validation by default. The owner explicitly requests this because Playwright is unsupported in some enterprise environments. Make browser execution a deliberate scoped choice while ordinary non-browser development, checks and review continue.

## Owner request

"priority task: don't run playwright tasks by default (not supported in some enterprise environments)"

## Acceptance criteria

- [ ] New projects, existing projects without explicit browser authorization, generated tasks, automatic UI/capture checks, review/acceptance plans and default CI/test entry points do not automatically dispatch or launch Playwright, Chromium or browser-install work. Inspect the actual default entry points rather than changing only one caller.
- [ ] Provide a documented project/task opt-in. An explicitly authorized Playwright task or deliberately configured browser check can run when supported; generated/template defaults must not silently count as owner opt-in. Preserve explicit existing user choices through compatibility handling.
- [ ] When Playwright is disabled or unavailable by policy, show truthful not-run/unsupported or not-required evidence and continue applicable non-browser unit, protocol, rendering and CI checks. Never report browser coverage as passed, silently weaken unrelated gates, or require browser evidence merely because the default template used to add it.
- [ ] If explicitly opted-in browser work cannot run in the environment, surface an actionable typed environment/policy reason before repeated work or installation attempts. Missing browser support must not trigger endless retries, paid author revisions or implementation/model escalation.
- [ ] Add deterministic coverage for defaults, existing config with no opt-in, explicit scoped enablement, unsupported capability, no automatic browser installation/launch, and unaffected non-browser checks. Use fakes for browser availability and subprocesses; real Playwright execution is not required for this task. Document enterprise configuration and report Linux/macOS/Windows-through-WSL coverage accurately.

## Boundaries

Keep this a focused configuration, dispatch, validation and evidence-policy correction. Do not remove unrelated browser tooling, uninstall existing tools, change cloud resources or weaken source/CI/review/security requirements. Do not run real browser tasks merely to prove that defaults are disabled. Existing explicit holds and the withdrawn Herdr direction remain intact.

## Log

- 2026-09-11T00:34:12+00:00 Owner priority request filed as616 to preserve withdrawn Herdr identity; initial new-only603draft moved to lossless operator evidence before any approval or execution
- 2026-09-11T00:34:13+00:00 approved (owner priority request: Playwright opt-in)
- 2026-09-11T00:34:44+00:00 dispatched work run 20260911T003444Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~13208 tokens)
- 2026-09-11T01:06:47+00:00 attempt 1 failed: worker idle 21 min (no output or file change); will retry
- 2026-09-11T01:07:07+00:00 dispatched work run 20260911T010706Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~13272 tokens)
- 2026-09-11T01:33:52+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T01:54:24+00:00 check did not run (20260911T013359Z-check): idle 20 min (no output or file change); will retry
- 2026-09-11T02:04:52+00:00 opened https://github.com/joshmarcus/context-garden/pull/481 (base main): Made Playwright and Chromium execution explicitly opt-in across dependencies, managed-worker bootstrap, walkthroughs, diagnostics, task dispatch, validation planning and review prompts. Verified deterministic default, opt-in, unsupported-runtime and non-browser behavior at commit 07ac5a5fcf5ee458f59627117e5d868f0a42b780; focused suites passed and Ruff passed. cost=$4.18
- 2026-09-11T02:08:49+00:00 CI failure
- 2026-09-11T02:09:17+00:00 dispatched revise run 20260911T020917Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14496 tokens)
- 2026-09-11T02:38:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T02:39:28+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/481: Ordinary CI no longer installs Playwright or Chromium, and project-level browser authorization no longer gates unrelated non-browser tasks. Verified at commit 56c88765 with 268 focused tests passing, 1 skipped, and Ruff clean. cost=$0.68
- 2026-09-11T02:56:06+00:00 automated review requested changes: Browser execution is mostly opt-in, but task prose containing “capture” is treated as authorization even when it explicitly says captures must not run. Exact-head passing CI evidence was also not provided; the supplied failure belongs to the previous head. cost=$0.56
- 2026-09-11T02:56:42+00:00 dispatched revise run 20260911T025642Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14755 tokens)
- 2026-09-11T03:16:13+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T03:18:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/481: Browser capture authorization now requires structured task/project/check opt-in or a narrowly explicit legacy capture requirement; negative and incidental capture prose neither probes browsers nor creates capture evidence. Verified commit 1a7fefeca8b11e4d24897043fdaefb8f1e48eb0f with 314 focused tests passing, 1 skipped, and Ruff clean. cost=$1.05
- 2026-09-11T03:28:10+00:00 automated review requested changes: The browser opt-in implementation satisfies the task in focused validation, but exact-head CI evidence is unavailable for the reviewed commit. cost=$0.33
- 2026-09-11T03:36:41+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-11T03:36:41+00:00 triage: changes requested by hand: Actual current1a7fefec CI34557803877 failed2 tests with2756passes,5skips and4deselected. tests/test_reviewer_judgment.py
- 2026-09-11T03:36:56+00:00 dispatched revise run 20260911T033656Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14922 tokens)
- 2026-09-11T04:05:50+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T04:15:53+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/481: Ordinary pytest and CI now deselect the two real-browser tests unless --run-browser-tests is explicitly supplied, while browser-independent web tests continue normally. The stale review-plan fixture now correctly expects no inferred pages without browser authorization; exact committed-source focused tests passed 60 tests with 2 browser tests deselected, and Ruff passed. cost=$0.77
- 2026-09-11T04:16:14+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_criteria.py); a rebase agent will resolve it
- 2026-09-11T04:16:17+00:00 dispatched rebase run 20260911T041617Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~5403 tokens)
- 2026-09-11T04:35:21+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/481: Rebased onto origin/main and resolved the tests/test_criteria.py conflict by retaining both sides' tests. cost=$0.01
- 2026-09-11T04:43:00+00:00 automated review: approve — Browser execution is consistently opt-in across configuration, dispatch, validation, walkthroughs, dependencies, worker bootstrap, pytest, and CI. Explicit browser work retains typed unsupported-runtime handling without automatic installation, while non-browser checks continue. cost=$0.67
- 2026-09-11T04:57:14+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/481
