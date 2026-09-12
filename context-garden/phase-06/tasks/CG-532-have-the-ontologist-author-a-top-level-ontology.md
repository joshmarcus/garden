---
id: CG-532
title: Have the ontologist author a top-level ontology specification
status: done
product: context-garden
phase: phase-06
depends_on:
- id: CG-531
  after: merge
priority: 1
difficulty: hard
reading:
- src/garden/model.py
- src/garden/runs.py
- src/garden/events.py
- src/garden/config.py
- src/garden/personas.py
- src/garden/remote_worker.py
- docs/architecture.md
branch: garden/cg-532-have-the-ontologist-author-a-top-level-ontology
pr: https://github.com/joshmarcus/context-garden/pull/462
attempts: 1
last_dispatched_at: '2026-09-10T18:49:00+00:00'
created: '2026-09-10T13:06:27+00:00'
updated: '2026-09-10T19:08:35+00:00'
---

## Goal

Have the new ontologist persona author a comprehensive top-level ONTOLOGY.md in the product repository. Clearly specify Garden's internal data models, what they mean, how they relate and how they can evolve, with diagrams and a complete written specification. Link it from the README and product-level architecture specifications so it is a canonical design reference rather than a phase-specific report.

## Context

This depends on the ontologist-persona task. The owner explicitly requested that the ontology be written by that persona. Run the named ontologist against the relevant source and design materials through the supported persona workflow, preserve its actual authored output/provenance, and integrate that output into the document through normal review. Do not merely attribute operator-written prose to an ontologist that did not run.

## Acceptance criteria

- [ ] Invoke the actual ontologist persona after its dependency is available, supplying the accepted source identity and relevant existing architecture/schema materials. Preserve the run/source identity and authored output used for ONTOLOGY.md, while keeping credentials and private operational details out of the shared document.
- [ ] Define the domain vocabulary and all material core concepts found in source, including product, phase, task, dependency/stack, run/attempt, review/finding/decision, check/validation, artifact, worker/host/lease, harness/model/profile, event/cost/usage and provisioning operation where applicable. Explain distinctions and boundaries, not just class names.
- [ ] Specify each model's identity and scope, attributes and types, required/optional/default/null semantics, relationships and cardinalities, lifecycle and allowed transitions, invariants, ownership/authority, and deletion/retention behavior. Cover authoritative state versus derived projections and persisted versus protocol representations.
- [ ] Include readable relationship/cardinality diagrams and lifecycle/state diagrams, plus representative examples and serialization/schema references. Show how task, run, review, validation, worker lease, artifact and event relationships fit together and where extensibility points belong.
- [ ] Specify compatibility and extension rules, schema/version evolution and ambiguous or conflicting representations. Ground claims in actual source and established architecture; record discrepancies as explicit findings rather than inventing fields or silently presenting conflicting implementations as one coherent contract. Keep this a full system specification, without turning it into a rollout plan or progress inventory.
- [ ] Validate references and diagrams, inspect rendered Markdown at readable widths, and have relevant maintainers/reviewers check the specification against the model and persistence/protocol code. Keep terminology consistent with the existing product-level architecture specs and identify one canonical ontology location.

owner_request_key: owner-top-level-ontology-20260910

## Log

- 2026-09-10T13:21:20+00:00 approved (delegated operator all-Inbox review)
- 2026-09-10T17:42:00+00:00 dispatched work run 20260910T174150Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~24561 tokens)
- 2026-09-10T18:04:10+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:07:04+00:00 base branch `main` is itself broken — pre-PR check(s) lint fail at its own commit bcc8419c2dde, not because of this branch; waiting for the base to go green, no revise round cost=$4.51
- 2026-09-10T18:34:09+00:00 base branch `main` recovered (moved to dc84676ee573); rebased onto it and the pre-PR checks pass now — continuing without a worker run
- 2026-09-10T18:34:12+00:00 opened https://github.com/joshmarcus/context-garden/pull/462 (base main): Added and linked the canonical ontologist-authored ONTOLOGY.md, preserving source/run provenance and incorporating source-focused maintainer corrections. Focused ontologist tests passed, references and Markdown rendering were checked, and all work was committed; repository lint reached one unchanged origin/main import-order failure.
- 2026-09-10T18:34:12+00:00 rebased; patch id unchanged but approval lineage was not proven; exact-head review queued
- 2026-09-10T18:37:52+00:00 automated review: approve — The canonical ontology is comprehensive, source-grounded, linked from product-level references, and preserves actual ontologist authorship and maintainer review provenance. cost=$0.51
- 2026-09-10T18:40:38+00:00 automated review requested changes: The ontology is comprehensive and well-provenanced, but its task lifecycle omits several implemented transitions, so it does not yet specify the allowed lifecycle required of a canonical model reference. cost=$0.75
- 2026-09-10T18:41:02+00:00 dispatched revise run 20260910T184057Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~25717 tokens)
- 2026-09-10T18:45:13+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:46:38+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/462: Completed the canonical task lifecycle specification by documenting the exhaustive caller-guarded transition relation and separating it from the readable principal-loop diagram. Verified commit ce8ba1b1e3f3001b061ee9b865988ff69eb624eb with 52 focused tests and clean repository lint. cost=$1.10
- 2026-09-10T18:48:20+00:00 automated review requested changes: The ontology is comprehensive and well-provenanced, but its exhaustive lifecycle table misstates the guard for explicit completion. cost=$0.59
- 2026-09-10T18:49:00+00:00 dispatched revise run 20260910T184856Z-revise-2 via local [codex model=gpt-5.6-sol] (fresh session, base main, ~25936 tokens)
- 2026-09-10T18:54:28+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T18:56:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/462: Corrected the canonical lifecycle table to state that ancestry verification applies only when a PR is recorded; tasks without a recorded PR may be explicitly completed without that check. Verified against Scheduler.mark_done, passed the focused lifecycle test and repository lint, and committed as fc06addf. cost=$0.62
- 2026-09-10T18:59:27+00:00 automated review: approve — The canonical ontology is comprehensive, source-grounded, correctly linked, and preserves verifiable ontologist authorship provenance. The corrected explicit-completion guard matches Scheduler.mark_done. cost=$0.78
- 2026-09-10T19:05:30+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T19:08:35+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/462
