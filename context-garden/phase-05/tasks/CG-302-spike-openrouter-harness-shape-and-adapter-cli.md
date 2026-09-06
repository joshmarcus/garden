---
id: CG-302
title: 'Spike: OpenRouter harness shape and adapter CLI'
status: draft
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: hard
reading: []
discovered_from: kickoff:context-garden/phase-05
created: '2026-09-06T00:07:46+00:00'
updated: '2026-09-06T00:07:46+00:00'
spike: true
---

## Goal

Goal 2 mandates an adapter around an existing OpenAI-compatible CLI (not a garden-owned loop), but CG-213's body still leaves built-in-loop vs adapter open and names no concrete CLI, while the spec frames it as the codex harness pointed at OpenRouter; whether it is a new `harnesses.openrouter` or codex+base_url is unsettled and shapes the fake stub and the member syntax CG-230 reuses.

## Suggested spike

Pick the concrete adapter (a named CLI, or codex exec with an OpenRouter base_url) and whether it is a distinct openrouter harness or codex configured with base_url; define fake_openrouter.py's request/response contract and GARDEN_RESULT parsing.

## Context

Raised at the context-garden/phase-05 kickoff. Relevant to CG-213, CG-230.
