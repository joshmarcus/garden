---
id: CG-362
title: Complete externally implemented tasks from verified PR metadata
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: medium
reading: []
created: '2026-09-06T22:23:48+00:00'
updated: '2026-09-06T23:59:15+00:00'
---

## Goal

An operator who implements a task in an existing session can record its real branch and PR, complete verified merged work, and retain honest audit/cost evidence without guessing scheduler worktree paths or launching redundant checks/review agents.

## Context

On 2026-09-06 the owner authorized direct operator implementation alongside the sole scheduled worker. CG-360 was implemented on codex/cg-360-restore-index, passed focused ext4/tmpfs tests and full final-head CI, and merged as PR242 at44b9a312. A later garden take --no-worktree generated a different branch name and snapshotted the expected CG-360 worktree. The finish --pr path selects its behavior by whether that expected directory exists, even for externally implemented/merged work. The operator mistakenly moved its worktree after take to use the external completion path; this correctly triggered the Git guard. The path was restored, every guard hash compared equal to the original snapshot, and only the resolved operator-created block marker was archived with provenance. The task branch also had to be corrected before ancestry-based completion would succeed. The failed manual bookkeeping run remains recorded; it must not be rewritten as successful worker execution.

Source evidence: docs/incidents/CG-360-validation.md, CG-360 task log and manual run20260906T220127Z-work. No source fix or test failure resulted from the bookkeeping problem. This change should make the safe ordinary workflow direct and explicit; it must preserve Git protection.

## Acceptance criteria

- [ ] Support claiming externally implemented work with an explicit existing worktree/branch or PR identity; persist those actual choices and distinguish external work from scheduler-managed worktree creation. Generated defaults cannot silently override an existing PR's branch.
- [ ] Finishing with an already merged PR verifies the expected head is included in the configured final base and completes the task through the normal transition/audit path without running another test/review cycle. For an open PR, retain the applicable validation/review gates and accurately identify existing head-specific evidence rather than manufacturing an approval.
- [ ] Completion mode is explicit and is not inferred merely from whether a coincidentally named directory exists. No worktree move, clone recreation or guard weakening is needed for a normal external completion. Keep malicious/unattributed Git metadata mutations blocked.
- [ ] Record failed completion attempts separately from successful implementation/merge evidence. Preserve run/task/PR links, expose unknown manual operator cost as unknown, and never count supervised operator work as unattended stabilization.
- [ ] Add focused tests for external and managed paths, mismatched generated/actual branches, already merged versus unmerged or stacked PRs, repeated completion and a genuine Git-guard violation. Document a short copyable operator workflow.

## Log

- 2026-09-06: Priority1 follow-up filed with owner authority after direct operator implementation exposed manual completion overhead. Ordinary dispatch remains paused.
- 2026-09-06T22:59:27+00:00 2026-09-06T22:59:27+00:00: CG363 external worktree remained outside scheduler path from the outset. Normal finish_manual API succeeded with review.enabled false scoped to that single call under owner direct-work authority, followed by normal merged-PR reconciliation; no extra model launched and spend stayed unknown. A supported CLI option should avoid needing this scoped API configuration.
- 2026-09-06T23:59:15+00:00 Operator review workflow friction23:53-23:57: triage-ready retained CG340 old pending_feedback; reconcile set needs_human="stuck: pending feedback recorded but the task is in_review, not changes_requested". Explicit review_again clears needs_human at dispatch but an approve verdict with description_rewrite returned early and left old feedback/stop intact. Actual reviewed head and CI were valid; operator applied permanent rewrite and merged. A supported manual-repair -> queued re-review path should respect review_parallel, preserve findings for review, then clear only obsolete feedback/stops on approval. Include this boundary in external/manual completion design or file a separate fix if scope warrants; never hand-edit state as the workaround.
