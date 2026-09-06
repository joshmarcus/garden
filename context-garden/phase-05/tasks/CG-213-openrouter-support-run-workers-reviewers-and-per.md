---
id: CG-213
title: 'OpenRouter support: run workers, reviewers and personas through any model on OpenRouter, as a
  harness with per-tier model ids and cost from the response usage'
status: draft
product: context-garden
phase: phase-05
depends_on: []
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
created: '2026-09-05T16:00:57+00:00'
updated: '2026-09-05T16:11:16+00:00'
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
