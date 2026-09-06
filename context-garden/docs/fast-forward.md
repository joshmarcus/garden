# Operator fast-forward protocol

Owner-authorized 2026-09-06. Purpose: finish open PRs through direct operator work when the automated review/revise loop is consuming time and cost without proportionate progress. Fast-forward is a maintenance mode, not a Git merge strategy; retain the repository's configured merge method.

## Enter and establish scope

1. Pause dispatch and inventory actual writers, reviewers, checks, base probes and detached processes, not only task status labels. Let bounded activity finish and preserve unfinished changes/transcripts before stopping anything. Save configuration and the PR head/base inventory.
2. Quiesce the scheduler completely: ordinary pause alone still permits checks/reviews/rebases. On this install, after all work drains, run the existing garden service with `serve --no-watch` via a reversible service drop-in. Keep the web UI and persistent resource caps. Never start a second server. Heartbeats must respect maintenance mode and must not call tick, dispatch, review or global resume automatically.
3. Inventory all open PRs. Resolve every eligible PR; explicitly account for frozen/deferred ones without changing their branches. Existing phase holds remain unless the owner explicitly includes them in a fast-forward exception. This protocol does not itself unfreeze phase 06.

## Resolve each PR directly

- Read its brief, current diff, CI, internal scheduler feedback and GitHub review threads. Recover dirty work/stashes before edits. Check for work already superseded or merged elsewhere.
- Address findings that improve correctness, intended behavior, maintainability or evidence. Review comments are inputs, not mandatory prescriptions. Decline obsolete, incorrect or disproportionate requests with a concrete rationale; defer unrelated useful ideas to a linked task. Do not ignore a known material defect to obtain a green label.
- Edit in the PR's isolated worktree. Refresh against current main; preserve useful work and avoid unrelated generated artifacts. Use force-with-lease only when rewriting that PR's history and after verifying its remote head.
- Self-review the final diff as the operator: intended behavior, edge cases, scope, regression risk, tests and remaining limitations. This owner authorization replaces the requirement for another automated model-review round during fast-forward. Do not fabricate an automated approval or mark unverified criteria passed.
- Run checks appropriate to the change and required repository CI. Reuse valid evidence for unchanged code; rerun affected validation after new changes or merges invalidate it. UI changes require an actual application walkthrough of relevant interactions; screenshots alone are insufficient. Keep test execution serial/resource-bounded and avoid repeating full suites purely to narrate verification.
- Update the permanent PR description and record the self-review, evidence and finding dispositions. Merge only after confirming the PR is still open, the expected head is current, required checks passed, and the branch is clean against current main. Use the established merge method. Resolve review threads only with an honest disposition. For duplicate/obsolete work, close with a recorded reason instead of manufacturing a merge.
- Merge serially, then refresh the next PR to avoid stale green checks. Reconcile garden state through supported commands after verifying GitHub's result; never mark a task done as a substitute for merging. Preserve cost and audit history.

## Resource and evidence rules

Operator-launched heavy work must be placed in a bounded service/scope; plain CLI launches can bypass garden service limits. Do not loosen the persistent CPU/memory caps merely for fast-forward. Keep an action ledger with PR/head, fixes, findings accepted/declined/deferred, self-review, checks, merge/closure and intervention time. This is supervised recovery, never evidence of unattended stabilization. Unknown spend or missing app evidence stays unknown/unproven.

## Exit

Report merged/closed PRs, explicitly deferred PRs and remaining blockers. Install a verified merged build only after work drains. Remove only the fast-forward service drop-in, reload systemd and restart the existing service with normal watch restored; verify health before global resume. Keep approved resource/concurrency settings and phase holds. Restore ordinary heartbeat duties only after the handoff records that maintenance mode ended. Do not resume a loop with known critical resource or main-branch failures merely because the PR queue is shorter.

## Activation record

2026-09-06 ~16:44 UTC: dispatch paused; no live worker/reviewer/check found in the garden cgroup or matching external worktrees. Existing garden-serve.service restarted with `~/.config/systemd/user/garden-serve.service.d/fast-forward.conf`, using `serve --no-watch`. UI remains available and resource caps remain. Fast-forward mode is active; open PR resolution and its ledger follow this protocol.
