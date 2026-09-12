---
id: CG-504
title: Write and update user operator and contributor documentation
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- README.md
- docs/architecture.md
- docs/worker-protocol.md
- docs/design.md
- pyproject.toml
branch: garden/cg-504-write-and-update-user-operator-and-contributor-d
pr: https://github.com/joshmarcus/context-garden/pull/423
attempts: 1
last_dispatched_at: '2026-09-10T11:25:57+00:00'
created: '2026-09-10T02:38:35+00:00'
updated: '2026-09-10T13:41:50+00:00'
---

## Goal

Write clear, accurate documentation that helps users get started, operators run and troubleshoot Garden, and contributors understand how to change it. Update the existing documentation rather than creating a competing set of guides.

## Context

Owner request: write documentation. Use the current product and supported workflows as the source of truth. Review existing README and documentation work, including CG378 and CG295, and build on it rather than repeating completed refreshes. Link feature-specific documentation owned by active tasks, such as CG423 worker lifecycle and CG499/CG501 worker status and diagnostics. Do not document unfinished features as available or private operational arrangements as standard product capabilities.

## Acceptance criteria

- [ ] Audit the existing documentation and identify the highest-impact gaps, outdated instructions and conflicting descriptions. Establish a concise navigation path for new users, operators and contributors, reusing canonical pages and removing or redirecting redundant guidance.
- [ ] Write or improve an end-to-end getting-started guide: prerequisites, installation, configuration, onboarding an existing repository, drafting and approving a useful task, observing progress, reviewing changes and reaching a completed result. Explain expected outcomes and how to recover from common setup mistakes.
- [ ] Document routine operation and troubleshooting: task states and dependencies, Inbox decisions, review and CI failures, revision/merge eligibility, local and remote worker availability, resource limits, pauses/resume, configuration precedence, recovery, upgrades and rollback where supported. Distinguish user decisions from automatic or delegated operator actions, and planned features from currently available behavior.
- [ ] Provide a concise contributor guide covering repository structure, a safe development setup, focused testing, relevant architecture and extension points, and documentation maintenance. Link detailed reference material instead of repeating implementation internals throughout user guides.
- [ ] Verify documented commands, links and examples against the named source revision using a disposable setup and proportionate smoke checks. Walk the getting-started sequence from a reader perspective, recording corrections and any unverified steps. Use synthetic examples and placeholders; publish no private environment identifiers, credentials or raw transcripts.
- [ ] Cover Linux, macOS and Windows through WSL with supported prerequisites and configurable paths. Explain genuine platform differences clearly and report platforms not tested. Keep instructions concise, task-oriented and consistent with actual CLI/UI terminology.

## Scope

Deliver usable documentation, not only an audit or a plan. Prioritize complete core journeys over exhaustive low-value reference prose. File focused follow-ups for large missing product capabilities instead of implementing unrelated features to make the documentation true.

## Log

- 2026-09-10T03:08:56+00:00 approved (delegated operator reviewed owner-requested draft during Inbox sweep)
- 2026-09-10T11:25:57+00:00 dispatched work run 20260910T112553Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20289 tokens)
- 2026-09-10T11:36:50+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:38:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/423 (base main): Added canonical user, operator, and contributor documentation, including an end-to-end first-project journey, task-state and recovery guidance, platform notes, and a role-based navigation map. Verified commit c9ff23791cf1a6a4e5904501a77c611fe55d4f8b with four focused disposable CLI/onboarding tests, Ruff, Markdown link/anchor checks, and final diff inspection. cost=$1.41
- 2026-09-10T11:40:36+00:00 automated review: approve — The documentation provides clear, accurate role-based guidance for first-time users, operators, and contributors without duplicating implementation references. cost=$0.56
- 2026-09-10T13:41:50+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/423
