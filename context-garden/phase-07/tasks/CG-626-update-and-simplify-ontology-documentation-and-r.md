---
id: CG-626
title: Update and simplify ontology documentation and related Markdown
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-531
- CG-532
- CG-504
- CG-505
priority: 2
difficulty: hard
reading:
- README.md
- docs/architecture.md
- src/garden/model.py
- src/garden/runs.py
- src/garden/personas.py
branch: garden/cg-626-update-and-simplify-ontology-documentation-and-r
pr: https://github.com/joshmarcus/context-garden/pull/490
runner: local
discovered_from: 'owner: documentation/markdown on our ontology, and update/simplify where useful'
attempts: 1
last_dispatched_at: '2026-09-11T11:18:20+00:00'
created: '2026-09-11T11:17:07+00:00'
updated: '2026-09-11T11:38:18+00:00'
---

## Goal

Review the documentation and Markdown describing Garden's ontology, update it against current accepted source and product contracts, and simplify it wherever that makes the model easier to understand. Deliver actual documentation improvements, including ONTOLOGY.md and the related explanations that readers rely on.

## Owner request and foundations

Owner request: "Task: documentation/markdown on our ontology, and update/simplify where useful". CG-531 supplied the ontologist persona and CG-532 supplied the canonical product-repository ONTOLOGY.md in PR462. CG-504/505 updated general documentation and specifications. These tasks are complete; use their accepted output rather than creating a second ontology or repeating an initial discovery project. The current ontology retains its original source/run identity, authored output and maintainer corrections; preserve that provenance while making the current reference truthful.

CG-624 owns test-count/runtime reduction and CG-625 owns production-code simplification. Coordinate overlapping terms and documentation with their actual accepted changes; do not describe pending implementations as present behavior. This is Phase07 documentation follow-through, not another Phase05 closing blocker.

## Acceptance criteria

- [ ] Inventory ONTOLOGY.md and the related README, architecture/design, model/protocol, configuration, persona and product-specification Markdown. Check definitions and links against an exact current accepted source identity and established product contracts. Identify stale statements, ambiguous or overloaded terms, duplicated explanations, obsolete examples and unnecessary detail. Prioritize reader confusion and actual inconsistency rather than cosmetic churn.
- [ ] Update the canonical ontology and relevant Markdown so identities, scope, relationships/cardinality, lifecycles, ownership/authority, persisted versus derived state, null/default semantics and compatibility rules are consistent and precise. Retain important distinctions such as task versus run, model versus harness, worker versus host and measured evidence versus operator acceptance. Represent any source/spec conflict explicitly; do not invent a new contract or silently turn a discrepancy into a supported behavior.
- [ ] Simplify wording, structure, examples and diagrams where useful. Define each core concept once in its canonical location and link from supporting documents instead of maintaining competing copies. Remove genuinely obsolete documentation, repair its inbound links and preserve information needed by supported users. Keep a useful overview with deeper detail available where necessary; shorter text alone is not the objective. Keep product-level architecture specs in their established canonical locations and as full-system design references, without turning them into rollout plans or an implemented/future inventory.
- [ ] Use the established ontologist workflow for substantive ontology/model revisions and preserve actual source/run/output attribution. Do not attribute new prose to a persona that did not author or review it, overwrite the original raw persona output or rewrite historical task/retro/failure evidence. Routine editorial corrections need proportionate documentation review, with no extra review merely by count. Keep any larger runtime/schema redesign in its existing canonical implementation task or a justified follow-up, rather than slipping it into documentation edits.
- [ ] Deliver reviewed Markdown changes with a concise account of corrected concepts, consolidated references and useful removals. Validate local links, anchors, examples and Mermaid syntax; inspect rendered Markdown/diagrams using supported tooling without making browser execution mandatory. Check substantive claims against relevant model/persistence/protocol source, run only applicable documentation or affected-behavior checks, and preserve exact-head CI and normal independent review. Keep examples generic and portable across Linux, macOS and Windows through WSL; report what was actually validated and any limitations.

## Execution scope

Use the normal local runner and existing resource/validation limits in an isolated checkout. The primary artifact is the existing product-repository ontology and related documentation; coordinate any canonical context-spec changes through their normal repository workflow. Preserve original reports, active work and explicit owner holds. No production hotpatch, model/schema change, additional cloud resource or deadline extension is authorized by this documentation task.

## Log

- 2026-09-11T11:17:44+00:00 approved (owner request; delegated operator task approval)
- 2026-09-11T11:18:20+00:00 dispatched work run 20260911T111816Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~2672 tokens)
- 2026-09-11T11:23:29+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T11:24:52+00:00 opened https://github.com/joshmarcus/context-garden/pull/490 (base main): Refreshed the canonical ontology against accepted source commit 41ff4de3, preserved the original ontologist run attribution, corrected task/run/PR and worker/host terminology, clarified state and archive persistence, and removed resolved or speculative findings. Verified focused documentation tests (5 passed), Ruff, local links, balanced fences, Markdown rendering, and a clean committed worktree. cost=$0.99
- 2026-09-11T11:26:17+00:00 automated review: approve — The documentation update accurately consolidates Garden’s ontology, corrects stale terminology and persistence claims, and preserves the original ontologist attribution. Exact-head CI remains pending as an independently enforced merge gate. cost=$0.32
- 2026-09-11T11:36:44+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T11:38:18+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/490
