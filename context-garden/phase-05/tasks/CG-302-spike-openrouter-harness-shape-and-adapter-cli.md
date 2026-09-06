---
id: CG-302
title: 'Spike: OpenRouter harness shape and adapter CLI'
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: hard
reading:
- docs/architecture.md
- docs/worker-protocol.md
- docs/design.md
discovered_from: kickoff:context-garden/phase-05
created: '2026-09-06T00:07:46+00:00'
updated: '2026-09-06T00:24:07+00:00'
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
