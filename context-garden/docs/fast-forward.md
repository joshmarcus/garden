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

Owner scope clarification: leave frozen PRs #221 and #222 open. Fast-forward completes when #232, #229, #228, #223 and #216 are merged or closed with justified dispositions; reconcile their task states and exit maintenance at that point. The five-minute operator reminder drives this work until completion, then returns to ordinary 25-minute duties.

## PR resolution ledger

2026-09-06 16:58 UTC — #232 / CG-344: directly repaired and pushed f7b2646 (base merged from current main). Removed unrelated design snapshot, eliminated untrusted manifest fallback, preserved trusted references through manual runs and interrupted finalization, and made integrity failure an honest inspection stop. Added corruption/deletion/reference and concurrent-writer regression coverage. Operator self-review and finding dispositions are in the PR body. 182 targeted tests plus full lint passed; bounded test peak 376 MiB, zero swap. New-head GitHub CI pending; PR not yet merged. This was supervised repair, not unattended stabilization.

2026-09-06 17:02 UTC — #232 merged as bda4911f5a9854212298294ef957813f5b1c016d after full new-head CI passed and GitHub reported CLEAN. CG-344 reconciled to done through the CLI. Four eligible PRs remain (#229, #228, #223, #216); #221/#222 remain held. #229 has a local cleanup/merge commit 35bce9d removing unrelated snapshot and preserving main Now behavior; not yet validated or pushed. Fast-forward remains active.

2026-09-06 17:13 UTC — #229 merged at d5825a3feb93f2ea1869ae09753eb3cb944ba4a6 after new-head full CI and CLEAN verification. Removed unrelated scope, merged current main, corrected stale exit-file liveness and deferred pin installation while workers/checks remain. 64 lifecycle/CLI tests and lint passed, test peak 318 MiB, zero swap. CG-254 reconciled done. #228/#223/#216 remain; maintenance active.

2026-09-06 17:16 UTC — owner reported Now links unavailable; verified 404 on both because installed b72dbcc predated their merges. With no active workers/checks, installed verified merged d5825a3 under a bounded service (136 MiB peak), restarted existing UI-only service preserving pause/no-watch/caps. Both /now1 and /now2 now return 200; Now 1 verified in browser with both sidebar links. Fast-forward remains active.

2026-09-06 17:33 UTC — #228 merged at 14676f5 after 169 targeted tests, full CI and actual browser journeys (including a found/fixed stale Approve button after brief save). CG-296 done. #223 conflicts resolved, 125 tests and browser evidence passed, new-head CI pending at 8135d50. #216 latest code addresses convention/provenance findings; retained existing trusted authors, 18 tests/lint pass, CI pending at a5c12d6. Both remain open.

2026-09-06 17:40 UTC — Owner explicitly ended fast-forward early and requested normal operation. Owner merged #216 at 545c745f6cc38087f4623a7a5726768e17856a02; CG-215 reconciled done. #223 remains open, with passed head CI but requiring current-main reconciliation after #216. #221/#222 remain frozen/open. Installed verified 14676f5, stopped disposable fixture servers, removed only fast-forward.conf, restarted existing service with normal watch, verified / and both Now routes 200, resumed globally (200). Persistent CPU/memory caps and one-worker/review limits verified unchanged. Maintenance is INACTIVE by owner exception; remaining PR follows ordinary operation. This was supervised intervention, not unattended stabilization.

2026-09-06 17:41 UTC — Verified #223 also merged at cf76e6ed1f671b5a9d5a6055ae8f3d1f127a07ae and scheduler reconciled CG-324 done. All five eligible PRs now merged. Owner requested max_parallel=3; applied supported persistent live override and verified 0/3 worker slots, review limit 1, CPU 200%, MemoryHigh 3 GiB / Max 4 GiB / SwapMax 512 MiB unchanged. Resource observation temporarily every five minutes for one hour, then ordinary 25 minutes.
