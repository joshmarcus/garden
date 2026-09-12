---
id: CG-484
title: Initialize fresh base probes and distinguish unavailable checks from broken source
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/scheduler/reap.py
- src/garden/scheduler/checkruns.py
- tests/scheduler/test_reap.py
branch: codex/fix-base-probe-setup-lifecycle
pr: https://github.com/joshmarcus/context-garden/pull/384
runner: manual
attempts: 1
last_dispatched_at: '2026-09-09T14:56:18+00:00'
created: '2026-09-09T14:56:16+00:00'
updated: '2026-09-09T16:41:35+00:00'
---

## Goal

Make fresh base-probe worktrees run their required setup and distinguish an unavailable validation tool from evidence that base source is broken.

## Evidence

CG349 base probe20260909T144524Z-check at main2f8c5c418 failed lint with exit127 and /bin/sh: 2: .venv/bin/ruff: not found. A setup marker beside the probe survived its deletion/recreation, so command-only setup caching skipped creating the environment in the fresh checkout. Garden falsely parked CG349 as base_broken. Its separate rebased-branch lint errors remain real and must be preserved.

## Acceptance criteria

- [ ] Bind setup caching to the actual probe lifecycle or force setup through the existing mutex when the checkout is recreated; a stale marker cannot skip required environment setup.
- [ ] Preserve lock identity and concurrent setup safety; do not unlink lock files while they may be held, or delete source/results to recover.
- [ ] Classify setup/tool-unavailable probe outcomes as infrastructure/check-unavailable, not proof that main is broken. Preserve fail-closed validation and original error details.
- [ ] Add focused regressions for recreated probe plus stale setup marker, unavailable tool, and genuine base-source failure. A real base lint failure must still park the task, and branch failures must not be erased.

Implement in isolated existing source, then independently review and validate a versioned release. Do not hotpatch installed RC11/RC12 or clear current stops without a corrected actual recheck.

## Log

- 2026-09-09T14:56:17+00:00 approved (owner-reported false main-is-broken failure during root-cause repair)
- 2026-09-09T14:56:18+00:00 dispatched work run 20260909T145617Z-work via manual [human] (fresh session, base main, ~14661 tokens)
- 2026-09-09T15:15:33+00:00 PR attached: https://github.com/joshmarcus/context-garden/pull/384 (pr_number none -> 384)
- 2026-09-09T15:16:53+00:00 automated review could not start: git worktree add /home/joshua/work/worktrees/CG-484 codex/fix-base-probe-setup-lifecycle (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/fix-base-probe-setup-lifecycle')
fatal: 'codex/fix-base-probe-setup-lifecycle' is already used by worktree at '/home/joshua/work/operator-test-tmp/base-probe-setup-fix-20260909/source'
- 2026-09-09T15:16:53+00:00 automatic review recovery 1/2 queued for the current head: startup failed: git worktree add /home/joshua/work/worktrees/CG-484 codex/fix-base-probe-setup-lifecycle (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/fix-base-probe-setup-lifecycle')
fatal: 'codex/fix-base-probe-setup-lifecycle' is already used by worktree at '/home/joshua/work/operator-test-tmp/base-probe-setup-fix-20260909/source'
- 2026-09-09T15:19:52+00:00 automated review could not start: git worktree add /home/joshua/work/worktrees/CG-484 codex/fix-base-probe-setup-lifecycle (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/fix-base-probe-setup-lifecycle')
fatal: 'codex/fix-base-probe-setup-lifecycle' is already used by worktree at '/home/joshua/work/operator-test-tmp/base-probe-setup-fix-20260909/source'
- 2026-09-09T15:19:52+00:00 automatic review recovery 2/2 queued for the current head: startup failed: git worktree add /home/joshua/work/worktrees/CG-484 codex/fix-base-probe-setup-lifecycle (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/fix-base-probe-setup-lifecycle')
fatal: 'codex/fix-base-probe-setup-lifecycle' is already used by worktree at '/home/joshua/work/operator-test-tmp/base-probe-setup-fix-20260909/source'
- 2026-09-09T15:23:45+00:00 automated review could not start: git worktree add /home/joshua/work/worktrees/CG-484 codex/fix-base-probe-setup-lifecycle (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/fix-base-probe-setup-lifecycle')
fatal: 'codex/fix-base-probe-setup-lifecycle' is already used by worktree at '/home/joshua/work/operator-test-tmp/base-probe-setup-fix-20260909/source'
- 2026-09-09T15:23:45+00:00 automatic review recovery exhausted after 2 attempt(s): startup failed: git worktree add /home/joshua/work/worktrees/CG-484 codex/fix-base-probe-setup-lifecycle (in /home/joshua/work/repos/context-garden): Preparing worktree (checking out 'codex/fix-base-probe-setup-lifecycle')
fatal: 'codex/fix-base-probe-setup-lifecycle' is already used by worktree at '/home/joshua/work/operator-test-tmp/base-probe-setup-fix-20260909/source'
- 2026-09-09T15:30:31+00:00 nothing to fix; needs-human stop cleared by hand
- 2026-09-09T15:34:12+00:00 automated review requested changes: Probe lifecycle caching and check-command recovery work, but unavailable setup commands can still be misclassified as broken base source. cost=$0.32
- 2026-09-09T16:05:37+00:00 external PR attached at codex/fix-base-probe-setup-lifecycle; existing CI is SUCCESS
- 2026-09-09T16:05:44+00:00 stuck: pending feedback recorded but the task is in_review, not changes_requested; resume with one more round (`garden retry CG-484`) or send it back (`garden triage CG-484 --changes "..."`)
- 2026-09-09T16:33:56+00:00 re-enabled by hand; revise run will follow
- 2026-09-09T16:38:30+00:00 current review resolved the pending review findings
- 2026-09-09T16:38:30+00:00 automated review: approve — Fresh base probes now rerun setup despite stale sibling markers, while unavailable checks use bounded infrastructure recovery and genuine base failures still park tasks. cost=$0.41
- 2026-09-09T16:39:53+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-09T16:41:35+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/384
