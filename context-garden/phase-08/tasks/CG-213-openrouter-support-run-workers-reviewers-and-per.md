---
id: CG-213
title: 'OpenRouter support: run workers, reviewers and personas through any model on OpenRouter, as a
  harness with per-tier model ids and cost from the response usage'
status: done
product: context-garden
phase: phase-08
depends_on:
- CG-302
priority: 3
difficulty: hard
reading:
- context-garden/phase-05/specs/cost-aware-model-routing.md
- src/garden/harness.py
- src/garden/runner/local.py
- src/garden/runner/base.py
- src/garden/brief.py
- tests/fake_codex.py
- docs/architecture.md
branch: garden/cg-213-openrouter-support-run-workers-reviewers-and-per
pr: https://github.com/joshmarcus/context-garden/pull/433
runner: remote
freeze_exception: true
freeze_exception_reason: Owner explicitly unfroze OpenRouter work on 2026-09-10; only CG-302 and CG-213
  are exempt. Other Phase08 tasks remain frozen.
attempts: 1
last_dispatched_at: '2026-09-10T14:03:15+00:00'
created: '2026-09-05T16:00:57+00:00'
updated: '2026-09-10T14:49:27+00:00'
---

## Goal

A garden can point any tier at a model served by OpenRouter (`openrouter/<vendor>/<model>`), for workers, reviewers, personas and the retro, and the loop treats it like the claude and codex harnesses: a detached process per run, a transcript in `stdout.json`, a final message with `GARDEN_RESULT`, usage and cost per run from the API's response, the same worker environment scrub, and the same tests with a fake.

## Spec

The user's spec `context-garden/phase-05/specs/cost-aware-model-routing.md` (2026-09-05) defines the routing policy, the escalation model, the codex compatibility suite, the evaluation corpus and the phase-1 acceptance criteria; this task is its first deliverable (the harness) and should read it before designing.

## Context

Backlog item from the user on 2026-09-05 ("support for open router"), the day the Claude account hit its monthly spend limit and the Codex account its usage limit, and the day the tier map moved to cheaper models. OpenRouter is one API key for many providers with per-token pricing and no per-account quota of the kind that stopped both harnesses today; it also makes cheap open-weight models available for easy tasks and reviews. The harness layer today wraps agent CLIs (`claude -p`, `codex exec`, or a custom CLI described in `harnesses:`); OpenRouter is an OpenAI-compatible chat API, so the shape is either (a) a small built-in agent loop (chat completions with tool calls for shell, read and write, running inside the worktree with the scrubbed environment) or (b) an adapter around an existing OpenAI-compatible agent CLI (for example opencode or aider) configured with `OPENROUTER_API_KEY`, parsed like codex's JSON. Option (a) gives the loop one more thing to maintain; option (b) depends on a third-party CLI's output format. Choose in the design and say why.

## Acceptance criteria

- [ ] `harnesses.openrouter` in garden.yaml with `api_key_env` (default `OPENROUTER_API_KEY`), `models` per tier, `max_turns`, and an optional `base_url`; `garden doctor` checks the key and lists the tiers' models.
- [ ] A work run, a review run and a persona run complete through OpenRouter on a throwaway garden, with `stdout.json`, `final.md`, `run.json` usage and cost (from the response's usage and OpenRouter's pricing), and the transcript renders on the task page.
- [ ] The worker environment scrub and the fence apply; the key reaches only the harness process.
- [ ] `tests/fake_openrouter.py` (an OpenAI-compatible stub) drives the suite's harness tests; no test needs the network.
- [ ] `docs/architecture.md` and `examples/` show the configuration, including a mixed map (cheap OpenRouter model for easy and reviews, claude for hard).

## Log

- 2026-09-05T16:11:16+00:00 moved from context-garden/phase-04 to context-garden/phase-05
- 2026-09-06T00:55:00+00:00 deferred by the operator: dispatches after the OpenRouter shape spike (CG-302) and the cost-per-accepted-task measurement (CG-251) merge (joined phase-05 goals, goal 2)
- 2026-09-06T03:38:31+00:00 approved (web)
- 2026-09-06T13:13:27+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:22+00:00 reset to ready by hand
- 2026-09-06T13:44:56+00:00 Owner-directed feature deferral until phase-05 stabilization is demonstrated. Preserve existing branch and PR; no further implementation or merge before the gate passes.
- 2026-09-06T13:44:57+00:00 moved from context-garden/phase-05 to context-garden/phase-06
- 2026-09-07T20:10:03+00:00 Owner explicitly unfroze phase06 and authorized task approval on 2026-09-07; this supersedes historical feature-freeze notes. Preserve existing implementation/PR and normal review/resource gates.
- 2026-09-07T20:10:03+00:00 approved (owner-unfreeze-phase06)
- 2026-09-09T12:53:02+00:00 back to draft (web)
- 2026-09-09T12:53:11+00:00 moved from context-garden/phase-06 to context-garden/phase-08
- 2026-09-10T11:24:08+00:00 Owner unfreezes OpenRouter implementation; retain normal dependency, source, review and CI gates. Use existing remote capacity; no live provider spend or fleet extension follows.
- 2026-09-10T11:24:08+00:00 approved (owner OpenRouter unfreeze)
- 2026-09-10T11:32:07+00:00 dispatched work run 20260910T113207Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-302-spike-openrouter-harness-shape-and-adapter-cli stacked on CG-302, ~21698 tokens)
- 2026-09-10T11:59:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T12:01:35+00:00 opened https://github.com/joshmarcus/context-garden/pull/433 (base garden/cg-302-spike-openrouter-harness-shape-and-adapter-cli): Added a named Codex-backed OpenRouter harness with tier routing, provider usage/cost capture, scoped credential admission, doctor diagnostics, offline fake coverage, and mixed-routing documentation. Verified committed head bef2539e30e9e5b33fc6b613d9b3ee167f73675a with the full ordinary suite (2422 passed, 4 skipped, 4 stress tests deselected) and repository-wide Ruff. cost=$5.02
- 2026-09-10T13:03:07+00:00 automated review requested changes: OpenRouter routing and lifecycle plumbing are coherent, but provider-reported cost—the core accounting outcome—is only simulated after the provider boundary. cost=$0.65
- 2026-09-10T13:03:21+00:00 dispatched revise run 20260910T130321Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-302-spike-openrouter-harness-shape-and-adapter-cli, ~22735 tokens)
- 2026-09-10T13:15:10+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:16:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/433: Added a tested OpenRouter Responses accounting proxy so provider-reported usage and cost flow into Codex JSONL and persisted run records, while the real provider key remains confined to the proxy. Verified focused harness, runner, work/review/persona lifecycle, doctor, and credential tests plus repository-wide Ruff. cost=$1.23
- 2026-09-10T13:20:59+00:00 automated review requested changes: OpenRouter routing and provider-reported accounting work, but the provider credential is not actually confined from the Codex worker. cost=$0.71
- 2026-09-10T13:21:15+00:00 dispatched revise run 20260910T132115Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base garden/cg-302-spike-openrouter-harness-shape-and-adapter-cli, ~22946 tokens)
- 2026-09-10T13:35:19+00:00 parent CG-302 merged; will rebase onto main when the current run finishes
- 2026-09-10T13:38:12+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:38:21+00:00 parent CG-302 merged; rebased onto main and retargeted the PR
- 2026-09-10T13:39:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/433: Confined OpenRouter credentials from Codex and its ancestor process environments across local and SSH launches. Verified current head b94d8c6c with 122 focused harness/OpenRouter/runner tests and repository-wide Ruff. cost=$2.39
- 2026-09-10T13:45:41+00:00 automated review requested changes: OpenRouter routing, accounting, credential confinement, and lifecycle coverage are coherent, but configured OpenRouter turn limits are never enforced. cost=$0.59
- 2026-09-10T14:02:17+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:03:15+00:00 dispatched revise run 20260910T140315Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24467 tokens)
- 2026-09-10T14:10:23+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:14:11+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/433: OpenRouter now enforces the selected tier's max_turns at the Responses boundary for initial and resumed runs. Verified exact head c8b5711563ddbbea39df2ade78e2b888fcae4bfa with 124 focused harness/runner/lifecycle tests, the focused doctor test, and repository-wide Ruff. cost=$0.97
- 2026-09-10T14:16:59+00:00 automated review: approve — OpenRouter support meets the frozen criteria, including provider-reported accounting, credential confinement, and per-tier turn-limit enforcement. cost=$0.40
- 2026-09-10T14:49:27+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/433
