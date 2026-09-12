---
id: CG-505
title: Audit and update all Garden specifications
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- docs/architecture.md
- docs/design.md
- docs/worker-protocol.md
- context-garden/phase-05/goals.md
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-505-audit-and-update-all-garden-specifications
pr: https://github.com/joshmarcus/context-garden/pull/424
attempts: 1
last_dispatched_at: '2026-09-10T12:52:05+00:00'
created: '2026-09-10T02:39:38+00:00'
updated: '2026-09-10T13:09:27+00:00'
---

## Goal

Audit and update all Garden specifications so they form a coherent, current account of intended behavior, implemented capabilities, remaining work and explicit owner decisions.

## Context

Owner request: update all specs in garden. Inventory specifications across the product repository and Garden workspace, including phase specs and normative requirements outside spec-named directories. Coordinate with CG504 user/operator/contributor documentation; this task owns specification consistency and coverage rather than duplicating user guides. Read current owner decisions and actual implementation before resolving stale requirements. Specs describe intended behavior as well as implementation: an implementation mismatch may be a bug, not permission to weaken the requirement.

## Acceptance criteria

- [ ] Create a complete inventory of specification documents in the configured Garden workspace and product repository, including relevant phase goals and normative design/protocol material. Classify each as active, planned, superseded or historical and identify its canonical location, related implementation and owning tasks. Record the scope and source revisions used so all-specs coverage is auditable.
- [ ] Review every inventoried spec against current owner decisions, supported behavior and existing tasks. Correct stale interfaces, terminology, configuration, state transitions, architecture assumptions and broken references. Clearly distinguish implemented, partially implemented, planned and deferred behavior; do not imply merged source is deployed.
- [ ] Reconcile duplicates and contradictions with a canonical requirement and clear cross-references. Preserve historical decisions and closed-phase evidence through explicit supersession notes or links rather than silently rewriting history. Keep unresolved product decisions visible with concrete alternatives and implications; do not invent owner approval.
- [ ] Ensure active requirements are understandable and verifiable, with scope, non-goals, dependencies, relevant behavior/failure cases and acceptance outcomes. Preserve security, compatibility, recovery and resource constraints. Remove obsolete requirements only when their superseding decision or rationale is documented; do not make failing implementation appear compliant by weakening its spec.
- [ ] Link genuine implementation gaps to existing tasks or file focused deduplicated follow-ups. Provide a concise change summary and disposition for every inventoried spec, including reviewed-but-unchanged documents and unresolved questions. Deliver actual updated specifications, not only an inventory or recommendations.
- [ ] Validate internal links, referenced paths, documented interfaces and representative examples against the named source revisions. Keep Linux, macOS and Windows through WSL requirements consistent, explain supported platform differences, and report unverified behavior honestly. Exclude private credentials, environment-specific connection details and raw private operational records.

## Scope boundaries

This task does not authorize unfreezing phases, closing milestones, changing budgets/deadlines, modifying live runtimes or implementing unrelated features. The accepted Phase05 stabilization evidence and remaining closing-review requirement are owner decisions to preserve.

## Log

- 2026-09-10T03:08:56+00:00 approved (delegated operator reviewed owner-requested draft during Inbox sweep)
- 2026-09-10T11:29:38+00:00 dispatched work run 20260910T112934Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19758 tokens)
- 2026-09-10T11:39:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:40:39+00:00 opened https://github.com/joshmarcus/context-garden/pull/424 (base main): Added an auditable inventory and disposition for every Garden product specification, phase goal, phase specification, and normative product-repository document against product base a17ce238 and Garden workspace commit a703480 plus visible workspace source. Reconciled stale specification links and blanket review-evidence requirements with current owner policy; focused architecture tests, Ruff, relative-link validation, inventory completeness, and diff checks pass. cost=$1.31
- 2026-09-10T11:43:06+00:00 automated review requested changes: The audit is coherent and complete at the document level, but it assigns the automatic model-escalation gap to tasks that do not own that behavior. cost=$0.45
- 2026-09-10T11:54:10+00:00 dispatched revise run 20260910T115405Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20727 tokens)
- 2026-09-10T11:58:22+00:00 discovered work filed: CG-526
- 2026-09-10T11:58:22+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:59:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/424: Corrected the specification audit to distinguish CG-437's implemented revision-threshold escalation from the broader unimplemented failure-trigger policy, and removed the incorrect assignment to CG-213/302. Committed as 6be2b5e5; 5 focused tests and Ruff passed. cost=$0.65
- 2026-09-10T12:02:54+00:00 automated review requested changes: The escalation ownership correction is accurate, but the claimed complete audit still omits a specification visible in the audited workspace. cost=$0.46
- 2026-09-10T12:52:05+00:00 dispatched revise run 20260910T125201Z-revise-2 via local [codex model=gpt-5.6-sol] (fresh session, base main, ~21215 tokens)
- 2026-09-10T12:56:30+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T12:57:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/424: Added and reviewed the omitted phase-06 enterprise specification, identifying it as a byte-identical superseded alias and recording its canonical source and task ownership. Verified all 28 workspace specification files are inventoried; 5 focused tests and Ruff passed on commit 93ee7d96. cost=$0.55
- 2026-09-10T12:59:25+00:00 automated review: approve — The specification audit is complete and coherent, including the previously omitted phase-06 alias and accurate escalation ownership. cost=$0.30
- 2026-09-10T13:07:36+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T13:09:27+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/424
