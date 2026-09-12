---
id: CG-302
title: 'Spike: OpenRouter harness shape and adapter CLI'
status: done
product: context-garden
phase: phase-08
depends_on: []
priority: 2
order: 1
difficulty: hard
reading:
- docs/architecture.md
- docs/worker-protocol.md
- docs/design.md
branch: garden/cg-302-spike-openrouter-harness-shape-and-adapter-cli
pr: https://github.com/joshmarcus/context-garden/pull/421
runner: remote
discovered_from: kickoff:context-garden/phase-05
freeze_exception: true
freeze_exception_reason: Owner explicitly unfroze OpenRouter work on 2026-09-10; only CG-302 and CG-213
  are exempt. Other Phase08 tasks remain frozen.
attempts: 1
last_dispatched_at: '2026-09-10T11:24:37+00:00'
created: '2026-09-06T00:07:46+00:00'
updated: '2026-09-10T13:35:19+00:00'
spike: true
---

## Goal

Decide the concrete OpenRouter adapter shape: a distinct `harnesses.openrouter` entry, or `codex` configured with a `base_url`. Goal 2 requires an adapter around an existing OpenAI-compatible CLI, not a garden-owned loop, but CG-213 leaves built-in-loop vs. adapter open and names no concrete CLI. The choice shapes `fake_openrouter.py`'s contract and the member syntax CG-230 reuses.

## Suggested spike

Pick the concrete adapter (a named CLI, or codex exec with an OpenRouter base_url) and whether it is a distinct openrouter harness or codex configured with base_url; define fake_openrouter.py's request/response contract and GARDEN_RESULT parsing.

## Context

Raised at the context-garden/phase-05 kickoff. Relevant to CG-213, CG-230.

## Acceptance criteria

- [ ] The adapter shape decision (distinct `harnesses.openrouter` vs. `codex` + `base_url`) is written down with rationale in the spike's output, referencing CG-213 and CG-230 — verified by reading the decision writeup.
- [ ] `fake_openrouter.py` exists and documents/implements the request shape, response payload, and how `GARDEN_RESULT` is parsed from it — verified by reading `fake_openrouter.py`.
- [ ] A smoke run of the chosen adapter against `fake_openrouter.py` produces a parseable `GARDEN_RESULT` — proven by `test_fake_openrouter_smoke`.
- [ ] Open questions or follow-ups for CG-213 (harness config) and CG-230 (member syntax) are called out explicitly in the writeup.

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; never invent a path); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-06T00:22:40+00:00 integrated 1 suggestion(s) (run 20260906T002119Z-edit) cost=$0.12
- 2026-09-06T00:24:07+00:00 approved (cli)
- 2026-09-06T13:13:18+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:34+00:00 reset to ready by hand
- 2026-09-06T13:44:58+00:00 Owner-directed feature deferral until phase-05 stabilization is demonstrated. Preserve existing branch and PR; no further implementation or merge before the gate passes.
- 2026-09-06T13:44:59+00:00 moved from context-garden/phase-05 to context-garden/phase-06
- 2026-09-07T20:10:03+00:00 Owner explicitly unfroze phase06 and authorized task approval on 2026-09-07; this supersedes historical feature-freeze notes. Preserve existing implementation/PR and normal review/resource gates.
- 2026-09-07T20:10:03+00:00 approved (owner-unfreeze-phase06)
- 2026-09-07T21:37:54+00:00 back to draft (web)
- 2026-09-08T02:29:28+00:00 approved (delegated-owner-inbox-approval)
- 2026-09-09T12:52:05+00:00 back to draft (web)
- 2026-09-09T12:54:37+00:00 moved from context-garden/phase-06 to context-garden/phase-08
- 2026-09-10T11:24:08+00:00 Owner unfreezes OpenRouter implementation; retain normal dependency, source, review and CI gates. Use existing remote capacity; no live provider spend or fleet extension follows.
- 2026-09-10T11:24:08+00:00 approved (owner OpenRouter unfreeze)
- 2026-09-10T11:24:37+00:00 dispatched work run 20260910T112437Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14126 tokens)
- 2026-09-10T11:30:40+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:31:57+00:00 opened https://github.com/joshmarcus/context-garden/pull/421 (base main): Selected the existing Codex harness configured with an OpenRouter base URL, documented the rationale and follow-ups, and added a token-free fake adapter smoke test. Verified commit 5b4c74ae with 43 passing focused tests and clean Ruff lint. cost=$1.09
- 2026-09-10T11:38:08+00:00 automated review: approve — The spike makes a coherent Codex-plus-base_url decision, defines the fake adapter boundary, and explicitly scopes CG-213/CG-230 follow-ups. cost=$0.42
- 2026-09-10T13:35:19+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/421
