---
id: CG-126
title: Verify worktree provisioning for stacked tasks actually checks out the parent branch
status: done
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/web/app.py
- src/garden/web/templates/base.html
- src/garden/web/templates/phase.html
- src/garden/store.py
- src/garden/model.py
- src/garden/cli.py
- context-garden/phase-01-bootstrap/specs/botanical-theme.md
branch: garden/cg-126-verify-worktree-provisioning-for-stacked-tasks-a
pr: https://github.com/joshmarcus/context-garden/pull/90
discovered_from: CG-121
attempts: 1
last_dispatched_at: '2026-09-05T00:55:38+00:00'
created: '2026-09-04T23:45:33+00:00'
updated: '2026-09-05T01:13:16+00:00'
---

Twice now (this run and the prior CG-121 attempt) a task whose brief says "based on <parent-task-branch>" was actually checked out at main instead, because the parent PR wasn't merged yet. This time the branch had no commits of its own so a fast-forward fixed it safely, but that won't always be true. Worth checking the runner/worktree setup for stacked tasks so this doesn't recur and doesn't require a worker to reach for git surgery.

## Provenance

Discovered by CG-121 (Planner and friction reports can still create tasks in a closed phase) during run `20260904T233628Z-work`.

## Log

- 2026-09-04T23:45:33+00:00 discovered by CG-121
- 2026-09-05T00:04:53+00:00 approved (web)
- 2026-09-05T00:04:53+00:00 priority 3 -> 1 (web)
- 2026-09-05T00:46:50+00:00 dispatched work run 20260905T004640Z-work via local [claude model=claude-opus-4-8] (fresh session, base main, ~15412 tokens)
- 2026-09-05T00:53:20+00:00 opened https://github.com/joshmarcus/context-garden/pull/90 (base main): prepare_worktree only applied `base` when creating a fresh branch; reused/existing local/remote branches were left on a stale base, so a stacked task could stay on main instead of its parent branch. Added _ensure_base to fast-forward a commit-less branch onto its base and leave branches with real work for the rebase path. cost=$2.22
- 2026-09-05T00:55:27+00:00 automated review: approve — Adds gitops._ensure_base and wires it into every worktree-establishing path so a stacked task's commit-less branch is fast-forwarded onto its parent instead of left on a stale base; branches with their own work are left for the rebase path. Correct, minimal, well-tested (6/6 pass, ruff clean). cost=$0.67
- 2026-09-05T00:55:37+00:00 CI failure
- 2026-09-05T00:55:38+00:00 dispatched revise run 20260905T005538Z-revise via local [claude model=claude-opus-4-8] (fresh session, base main, ~11113 tokens)
- 2026-09-05T01:07:31+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/90: Fixed the failing CI check: a pre-existing timing race in test_event_log_digest_and_metrics where the stacked DM-002 run could be reaped before the digest was read, breaking exact-match assertions. Reworked those assertions to check DM-001's deterministic lifecycle; the gitops _ensure_base change from the prior commit is unchanged and already review-approved. cost=$2.46
- 2026-09-05T01:11:50+00:00 automated review: approve — gitops._ensure_base correctly fast-forwards a commit-less stacked branch onto its parent across all worktree-establishing paths and leaves branches with their own work for the rebase path; well-tested, full suite green, lint clean. The bundled test_coordination de-flake is orthogonal to the gitops change (DM-002 uses the fresh-branch path) and preserves DM-001's deterministic assertions. cost=$0.82
- 2026-09-05T01:13:16+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/90
