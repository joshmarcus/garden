---
id: CG-503
title: Find removable and overengineered code to simplify and optimize
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- docs/architecture.md
- pyproject.toml
- src/garden/scheduler/poll.py
- src/garden/store.py
branch: garden/cg-503-find-removable-and-overengineered-code-to-simpli
pr: https://github.com/joshmarcus/context-garden/pull/420
attempts: 1
last_dispatched_at: '2026-09-10T11:13:46+00:00'
created: '2026-09-10T02:37:43+00:00'
updated: '2026-09-10T13:36:55+00:00'
---

## Goal

Find code that can be removed, simplified or made more efficient because it is unused, redundant or more complex than the behavior requires. Prioritize concrete reductions in maintenance burden and measured runtime cost while preserving supported behavior.

## Context

Owner request: simplify and optimize code; find code that can be removed or is over engineered. Review current code and actual callers before proposing changes. Favor a smaller understandable design over speculative extensibility or a broad rewrite. Coordinate with CG502, which audits expensive low-value tests; this task owns production code and supporting tooling, not a duplicate test audit.

## Acceptance criteria

- [ ] Inspect representative high-complexity and frequently used code paths. Identify dead or unreachable code, duplicate implementations, obsolete compatibility paths, redundant state/caches, excessive indirection, unnecessary configuration and abstractions with little current benefit. Check runtime entry points, plugins, CLI/API exposure, scripts and documented consumers; absence of direct static references alone is not proof a symbol is unused.
- [ ] For each serious candidate, describe its purpose, concrete callers and supported behavior, why complexity or cost is unnecessary, and a smaller alternative or justified removal. Preserve security, concurrency, recovery, idempotency, resource and compatibility safeguards unless evidence establishes they are redundant. Include candidates that should be retained and why.
- [ ] Produce a ranked report with exact source references, expected maintenance or performance benefit, risk, dependencies and a bounded proposed change. Distinguish measured hot-path costs from readability improvements and speculation. Use profiles or equivalent representative measurements for performance claims rather than assuming fewer lines means faster execution.
- [ ] Validate the highest-value proposals with proportionate disposable experiments or small isolated prototypes where useful. Demonstrate preservation of meaningful public behavior, error handling and affected failure/recovery cases. For performance changes, compare the same workload and resource limits and report tradeoffs, not just the best sample.
- [ ] File focused, deduplicated implementation follow-ups with the behavior/compatibility contract and evidence needed for review. Avoid a sweeping rewrite, arbitrary line-count target or deleting code just to meet a cleanup quota. This discovery task does not itself authorize broad removal, public API breakage or live-runtime modification.
- [ ] Use portable APIs and configurable paths for Linux, macOS and Windows through WSL. Retain optional-platform capability handling and explain any proposed compatibility retirement explicitly. Report source revision, environments actually checked and untested platforms.

## Log

- 2026-09-10T03:08:55+00:00 approved (delegated operator reviewed owner-requested draft during Inbox sweep)
- 2026-09-10T11:13:46+00:00 dispatched work run 20260910T111342Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~13682 tokens)
- 2026-09-10T11:25:40+00:00 discovered work filed: CG-521, CG-522, CG-523, CG-524
- 2026-09-10T11:25:40+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:27:01+00:00 opened https://github.com/joshmarcus/context-garden/pull/420 (base main): Committed a ranked simplification audit covering scheduler polling, store/web discovery, dispatch, enrollment, plugins, CLI entry points, scripts, and documented consumers. Verified with measured provider-call and disposable web/store benchmarks, 192 focused tests, and clean Ruff lint. cost=$1.53
- 2026-09-10T11:29:24+00:00 automated review: approve — The ranked audit is source-grounded, appropriately bounded, and distinguishes measured runtime costs from maintenance-only opportunities while preserving important safeguards. cost=$0.33
- 2026-09-10T13:36:55+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/420
