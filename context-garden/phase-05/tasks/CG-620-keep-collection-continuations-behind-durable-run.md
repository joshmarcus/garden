---
id: CG-620
title: Keep collection continuations behind durable Run finalization
status: done
product: context-garden
phase: phase-05
depends_on:
- CG-584
- CG-619
priority: 0
difficulty: hard
reading:
- context-garden/phase-05/docs/check-collection-race-diagnosis.md
- src/garden/runs.py
- src/garden/scheduler/checkruns.py
branch: garden/cg-620-keep-collection-continuations-behind-durable-run
pr: https://github.com/joshmarcus/context-garden/pull/486
runner: remote
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-11T03:28:42+00:00'
created: '2026-09-11T03:28:04+00:00'
updated: '2026-09-11T04:38:02+00:00'
---

## Goal

Fix the reproduced collector continuation gap left after CG584's correct preservation of newer worker completion. When a Run save is superseded by newer completion or lease-generation state, the collector must not apply the old result, clear its ownership pointer, advance the task or report successful collection until it has durably finalized the applicable current Run.

## Concrete evidence

The mandatory diagnosis document includes a deterministic failing test against accepted69d903ac and identical installedRC19 methods. Current reap_check returnsTrue, calls the continuation with run.status running and clears check_run while the newer final is safely retained. Live616check023905 has the corresponding orphaned-active shape; its exact original interleaving is not proven. Preserve that distinction, original source/final/result/accounting and the existing584 worker-final protection.

## Acceptance criteria

- [ ] Reproduce the stale collector/new completion interleaving through real Run persistence and check collection. No continuation, next-task transition, false finished event or pointer release may occur before applicable current-generation terminal state is durable. A later valid collection must converge exactly once without duplicate checks or model work.
- [ ] Preserve newer completion, original result bytes, lease/generation ownership, shared cross-process locking, costs and truthful failed/cancelled/timeout states. A reclaim, revocation or replacement generation must not inherit the stale collector's result or approval. Do not weaken CG584 or overwrite the live evidence to make the regression pass.
- [ ] Inspect normal check and terminal-check collection and analogous worker/review paths for the same save-then-continue pattern. Correct affected callers with a bounded explicit outcome or revalidation contract; retain unaffected behavior and avoid broad unrelated lifecycle redesign. Ensure ordinary collected and terminal task checks still finish and never reopen terminal tasks.
- [ ] Add deterministic lifecycle/generation regressions including normal later collection and the terminal-task path, using controlled interleavings or two processes as appropriate. Run focused checks, Run-index/review/recovery tests and Ruff, then actual exact-source CI and independent review. Use portable APIs/capability checks and report Linux/macOS/Windows-through-WSL coverage truthfully.

## Scope and ownership

This is a distinct closing correctness follow-up to completed584/386/487, not another cleanup or final-output supervisor task. It is a Phase05 closing blocker. Root continues the explicitly requested RC20 gates and accounted rollout of already accepted repairs; do not hotpatch runtimes, alter the fleet/deadline/budget or claim this new correction is deployed. The existing616 orphan will be reconciled through supported terminal-check collection after actual task merge; do not directly modify its live Run. Avoid browser/model canaries and preserve all historical findings.
## Log
- 2026-09-11T03:28:05+00:00 approved (operator: deterministic collection regression during reopened Phase05 and owner-authorized repair work)
- 2026-09-11T03:28:42+00:00 dispatched work run 20260911T032842Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15729 tokens)
- 2026-09-11T04:05:44+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T04:15:48+00:00 opened https://github.com/joshmarcus/context-garden/pull/486 (base main): Added an explicit committed/superseded Run-save outcome and gated check, worker, review, terminal-check, and orphan continuations on durable finalization. Deterministic on-disk regressions prove normal and terminal check collections retain ownership and converge exactly once after a newer completion; focused lifecycle suites and Ruff passed, and independent review found no blockers. cost=$5.91
- 2026-09-11T04:20:42+00:00 automated review: approve — The durable save outcome correctly prevents stale check, worker, review, terminal-check, and orphan continuations from advancing or releasing ownership after a newer completion wins persistence. cost=$0.59
- 2026-09-11T04:35:16+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-11T04:38:02+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/486
