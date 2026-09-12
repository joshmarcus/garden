---
id: CG-531
title: Add an ontologist persona for precise and extensible data models
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-585
  after: merge
priority: 1
difficulty: medium
reading:
- src/garden/personas.py
- src/garden/scheduler/persona.py
- src/garden/scheduler/retro.py
- src/garden/model.py
- src/garden/runs.py
- src/garden/config.py
branch: garden/cg-531-add-an-ontologist-persona-for-precise-and-extens
pr: https://github.com/joshmarcus/context-garden/pull/447
attempts: 1
last_dispatched_at: '2026-09-10T16:10:49+00:00'
created: '2026-09-10T13:06:27+00:00'
updated: '2026-09-10T16:26:46+00:00'
---

## Goal

Add an ontologist persona that reviews Garden's domain concepts, data modeling and internal representations for precision, coherence and extensibility. It should identify conceptual ambiguity, duplicated or overloaded models, unclear identities and relationships, and representation choices that make future change brittle.

## Acceptance criteria

- [ ] Define a distinct ontologist role covering vocabulary, entity/value distinctions, identity and scope, relationships and cardinality, state/lifecycle semantics, invariants, authoritative versus derived data, persistence and protocol representation, and compatible extension/versioning. Findings must identify concrete model inconsistencies and practical corrections grounded in source.
- [ ] Make the persona available through the normal persona discovery, initialization and PR/phase review paths, following existing customization and non-overwrite behavior. Preserve explicitly selected roles and existing in-flight review plans; adding a persona must not retroactively require another review merely by count.
- [ ] Support substantial first-person narrative reasoning alongside structured findings, with diagrams or model examples when they clarify an issue. The persona can produce an ontology specification as a clearly identified authored section/artifact through the supported workflow.
- [ ] Document when to involve the ontologist, what it owns relative to staff engineering/product/security review, and how its findings and specification feed normal reviewed work.
- [ ] Verify discovery/loading/initialization idempotence, custom overrides, named invocation and structured output with focused tests or a bounded native invocation; use portable paths and preserve existing persona behavior.

owner_request_key: owner-ontologist-persona-20260910

## Log

- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T15:06:55+00:00 dispatched work run 20260910T150651Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~24699 tokens)
- 2026-09-10T15:10:43+00:00 discovered work filed: CG-587
- 2026-09-10T15:10:43+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:12:05+00:00 opened https://github.com/joshmarcus/context-garden/pull/447 (base main): Added the built-in ontologist persona with source-grounded modeling guidance and a durable Ontology specification section, plus documentation and focused PR/phase/customization coverage. Verified direct persona loading, non-overwrite initialization, section rendering, and lint; focused pytest collection is blocked by a pre-existing circular import. cost=$0.70
- 2026-09-10T15:14:40+00:00 automated review: approve — The ontologist persona is distinct, source-grounded, documented, customizable, and integrated through existing persona section/report workflows without altering stored in-flight plans. cost=$0.45

## Operator dependency disposition

Exact-head review151209 approves the ontologist change with one nonblocking CLI help nit. CI34493899606 fails before collection on the same main runs/hosts import cycle owned by CG-585; preserve this red CI and the limited direct checks, and do not merge yet. Wait for actual CG-585 merge, then rebase this existing PR and obtain fresh exact-head CI/review as applicable. The optional help-text nit may be handled with that reconciliation; no second review merely by count is required. Duplicate discovery CG-587 was cancelled in favor of CG-585, with provenance preserved.
- 2026-09-10T15:37:13+00:00 Recorded main import-repair dependency on CG-585; exact red CI retained until rebase and validation.
- 2026-09-10T15:48:20+00:00 triage: changes requested by hand: CG585 has actually merged at51241517dbccc79a3bd3a69effbcfb1485bd133d, satisfying the recorded shared-CI dependency. Reba
- 2026-09-10T16:02:22+00:00 dispatched revise run 20260910T160217Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~25836 tokens)
- 2026-09-10T16:06:17+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:07:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/447: Rebased the existing ontologist persona work onto main and added the missing ontologist entry to persona-review help with regression coverage. Focused persona/CLI tests completed without failures; lint and the new CLI test passed on commit 816440ed. cost=$0.54
- 2026-09-10T16:10:32+00:00 automated review requested changes: The ontologist implementation is coherent and lint-clean, but the PR's focused suite fails in a modified retro test. cost=$0.53
- 2026-09-10T16:10:49+00:00 dispatched revise run 20260910T161045Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~26099 tokens)
- 2026-09-10T16:14:33+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:15:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/447: Corrected the retro pending-report expectations for the eight built-in personas introduced by the ontologist. Verified commit 1300b9e4 with six focused persona/retro/CLI tests and Ruff. cost=$0.52
- 2026-09-10T16:17:20+00:00 automated review: approve — The ontologist is distinct, source-grounded, documented, customizable, and integrated through existing PR, phase, initialization, and reporting paths without changing stored review plans. cost=$0.38
- 2026-09-10T16:26:46+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/447
