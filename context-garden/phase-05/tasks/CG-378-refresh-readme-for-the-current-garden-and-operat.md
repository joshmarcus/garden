---
id: CG-378
title: Refresh README for the current garden and operator workflow
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: hard
reading:
- README.md
- docs/architecture.md
- docs/worker-protocol.md
- docs/roadmap.md
- src/garden/config.py
harness: codex
model: gpt-6-astra
created: '2026-09-07T09:36:56+00:00'
updated: '2026-09-07T11:55:09+00:00'
---

## Goal

Rewrite README as a clear, accurate introduction and practical entry point for a new context-garden user. Owner explicitly requested Astra for this task.

## Context

CG234 updated an earlier README; this is a new accuracy/usability pass against current main. Existing prose includes unconditional workers-never-push and local-check descriptions that need verification against CI offload and worker_push. Explain the product and normal user journey before implementation mechanics. Distinguish the token-free scheduler from a model-powered delegated operator and its cost. Product documentation must describe supported behavior rather than this garden's temporary trial limits or unshipped tickets.

## Acceptance criteria

- [ ] Explain purpose, intended user, context/planning/work/review/merge/retro flow and operator role clearly, matching current code and defaults. Explain human decisions versus delegated operator recovery and that agent usage includes operator cost.
- [ ] Verify installation/onboarding and a minimal end-to-end quickstart against actual CLI help/config/schema; validate safe commands in a disposable fixture. No live garden mutations or unnecessary full local suite for documentation.
- [ ] Correct stale push/check/CI, review/merge, configuration reload, concurrency and deployment claims using current implementation. Clearly distinguish supported remote options from frozen/unimplemented expansion; no claim that pending optional caps or UI changes already shipped.
- [ ] Give concise operating/recovery and operator-handoff guidance with links to maintained detailed docs; avoid copying a sprawling operational ledger or machine-specific settings into README.
- [ ] Check links/paths/commands, self-review for factual accuracy and reader usability, repair findings, and report acceptance evidence. Screenshots are required only if replaced or used to make new visual claims; broad application capture is unnecessary for prose alone.

## Log

- 2026-09-07T09:36:57+00:00 approved (web)
