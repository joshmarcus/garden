---
id: CG-625
title: Simplify overengineered code and remove redundant or obsolete code
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-503
priority: 2
difficulty: hard
reading:
- docs/architecture.md
- pyproject.toml
- src/garden/scheduler/poll.py
- src/garden/store.py
- docs/test-suites.md
branch: garden/cg-625-simplify-overengineered-code-and-remove-redundan
pr: https://github.com/joshmarcus/context-garden/pull/491
runner: local
discovered_from: 'owner: identify and simplify overengineered, redundant and obsolete code; follow through
  on CG-503'
attempts: 1
last_dispatched_at: '2026-09-11T11:39:41+00:00'
created: '2026-09-11T11:14:51+00:00'
updated: '2026-09-11T12:01:19+00:00'
---

## Goal

Identify and simplify overengineered code, consolidate redundant implementations and remove demonstrably obsolete code in context-garden. Deliver concrete implementation changes that make the current system easier to understand and maintain while preserving supported behavior.

## Owner request and existing work

Owner request: "Task: identify and simply over engineered code and redundancy and obsolete code". Interpret "simply" as "simplify". CG-503 already completed a source-grounded simplification audit in PR420 and filed CG-521/522/523/524. Start from that accepted report and the current accepted source, reconcile its findings with landed implementations, and look for remaining or newly introduced opportunities. This task owns implementation follow-through and a current source assessment; do not repeat the completed audit or reopen completed fixes without new evidence.

CG-624 separately owns the explicit 40% reduction in test count and test runtime. Coordinate any overlapping test/fixture edits with its current source, keep production simplification here, and do not import that numeric target as a code-deletion quota. This Phase07 task does not add a Phase05 closing blocker.

## Acceptance criteria

- [ ] Inspect current production code and supporting scripts/tooling for unnecessary abstraction or indirection, speculative extensibility, duplicate logic, redundant state or caches, unused entry points, unreachable branches and obsolete compatibility code. Check real callers, CLI/API routes, plugin registration, configuration, documentation and supported versions/platforms before classifying code as unused. Static-reference absence alone is insufficient evidence for removal.
- [ ] Record a concise prioritized inventory of material candidates with exact source references, present purpose and consumers, the reason for simplification/removal, a smaller alternative, expected benefit and relevant compatibility constraints. Reconcile CG-503 and its follow-ups first. Distinguish supported complexity needed for correctness from unnecessary complexity; do not infer obsolescence merely from low observed use.
- [ ] Implement the confirmed simplifications and removals in coherent, reviewable changes. Prefer direct code and one clear owner for duplicated behavior over new general-purpose frameworks. Remove obsolete wiring, imports, configuration and documentation with the code they describe. Do not stop at another audit or cosmetic renaming. Explain any material candidate retained or deferred and its concrete reason or existing canonical owner.
- [ ] Preserve supported public behavior, persisted formats, plugin/provider contracts and cross-platform capability fallbacks. Retain necessary authentication, concurrency, recovery, idempotency, resource/deadline and exact-source merge safeguards. A current compatibility requirement must be resolved explicitly rather than silently declared obsolete. No production runtime hotpatch, operational-history deletion, cloud-resource change or new spending follows from this task.
- [ ] Validate changed behavior with the smallest relevant existing suites and meaningful boundary/regression checks where needed. Use comparable workloads and resource limits for any claimed speedup; distinguish maintenance/readability gains from measured performance. Final exact-head CI, applicable lint and independent review must pass. Publish a concise before/after account of what was simplified, consolidated or removed, why it was safe and any remaining limitations. Use portable APIs/configurable paths and report actual Linux, macOS and Windows-through-WSL validation, including untested platforms.

## Execution

Use the normal local runner and existing admission/validation limits in an isolated task checkout. Preserve active branches, results, owner holds and the separately owned Phase05 closing work. Existing CG-503 audit-only limits describe that completed task; the present owner request authorizes implementation of justified source simplification and removal under normal review gates.

## Log

- 2026-09-11T11:14:51+00:00 approved (owner request; delegated operator task approval)
- 2026-09-11T11:15:23+00:00 dispatch failed: local runtime scratch blocked: Windows backing volume measurement unavailable: Windows backing-volume probe timed out
- 2026-09-11T11:39:22+00:00 reset to ready by hand
- 2026-09-11T11:39:41+00:00 dispatched work run 20260911T113938Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~2676 tokens)
- 2026-09-11T11:47:33+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T11:49:03+00:00 opened https://github.com/joshmarcus/context-garden/pull/491 (base main): Removed the obsolete deep-copy discovery path, consolidated duplicate brief-input reading, cleaned redundant architecture documentation, and recorded a current prioritized simplification inventory. Commit 205a7238 passed 95 focused tests and `.venv/bin/ruff check src tests scripts`; validation ran on WSL/Linux, while macOS and native Windows remain untested. cost=$1.69
- 2026-09-11T11:51:53+00:00 automated review: approve — The simplifications are coherent, behavior-preserving, and satisfy the task’s source-owned outcomes. Exact-head CI is still pending. cost=$0.39
- 2026-09-11T11:59:48+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T12:01:19+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/491
