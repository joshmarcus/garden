---
id: CG-641
title: Verify the enterprise integration merges on current main
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 2
difficulty: hard
reading:
- context-garden/specs/system-architecture.md
- src/garden/config.py
- src/garden/criteria.py
- src/garden/review.py
- src/garden/runner/ssh.py
- src/garden/scheduler/poll.py
branch: garden/cg-641-verify-the-enterprise-integration-merges-on-curr
pr: https://github.com/joshmarcus/context-garden/pull/505
runner: remote
discovered_from: 'owner: verify new enterprise merges while launching multiplayer'
attempts: 1
last_dispatched_at: '2026-09-12T17:06:50+00:00'
created: '2026-09-12T16:55:55+00:00'
updated: '2026-09-12T17:30:41+00:00'
---

## Goal

Verify that the enterprise-contributed merges now in public main work correctly together, and preserve a concise, reproducible account of the actual checks. Diagnose and repair a demonstrated regression within these changed behaviors; do not invent unrelated cleanup or manufacture a code change if the behavior already works.

## Scope and accepted source

Start from accepted main 0c6b2c838c007af9c1f5101939e80a9f4e900fff, containing PR495 exact-head command validation, PR496 authoritative frozen validation plans, PR497 durable recoverable SSH/tmux execution, PR502 retirement of terminal-task infrastructure holds, and PR501 recovery when automatic reviews omit a verdict. The exact combined-head hosted workflow34700272684 already completed SUCCESS; reuse that result, while checking the important behavior interactions directly. The controller's shared code checkout is stale; inspect current accepted source in the worker checkout. Production controller and worker daemon runtime remains the independently published stable0.3.0; source verification here does not claim a production upgrade or activate these newer changes.

## Acceptance criteria

- [ ] Inspect the five merged changes and their regression coverage at the combined accepted head. Run relevant focused checks for exact-head command CI, frozen validation-plan integrity, review verdict recovery, terminal hold retirement and durable SSH session recovery, preserving original failure output and source/environment identity. Reuse the existing successful hosted CI instead of repeating an unchanged full baseline.
- [ ] Verify boundary behavior: stale command results cannot satisfy a new head; workers cannot silently replace a frozen validation plan; missing review verdicts enter the intended recovery route without self-approval; terminal tasks stop surfacing stale infrastructure holds without clearing active-task or owner holds; disconnected SSH collection retains one durable execution and truthful result/cancellation state. Use existing real implementation tests and add focused regression coverage only for a concrete uncovered defect.
- [ ] Exercise the SSH transport/session contract with actual tmux in a disposable isolated environment if available, using a harmless fake harness rather than a paid model or live task. If needed ask the operator for the bounded transport/environment setup; do not disturb another worker, alter live Garden state, leak credentials or claim a mocked test proves a real remote journey. Label any remaining environment limitation precisely.
- [ ] Write a concise verification note under docs/enterprise-merge-validation.md describing the checked commits, behaviors, commands and actual results, or update an existing matching note. Fix only demonstrated in-scope regressions, run the affected tests and Ruff, and pass ordinary independent review and current-head CI. Do not weaken assertions, hide failures, force changes to tests merely to turn them green, or require a particular receipt/screenshot format.

## Execution and boundaries

Owner requested this verification on September12 alongside launching true multiplayer and two remote workers. Use one of the new bounded remote workers, retaining3CPU/12GiB/swap0 and existing focused-validation limits. No new cloud capacity, publication, release, live rollout, Herdr work or reopening unrelated holds. Use a concrete native question if you need operator-owned evidence or credentials. The original exact combined-head CI is https://github.com/joshmarcus/context-garden/actions/runs/34700272684.

## Log

- 2026-09-12T16:56:45+00:00 approved (owner September12 enterprise merge verification request)

## Operator-supplied existing evidence

The exact combined-head push CI34700272684 succeeded with quality, all three shards and the test aggregate; exact-head-push was correctly skipped for a push. Logs show888 passed plus1121 passed/1 skipped plus991 passed/3 skipped:3000 passed,4 skipped,8 deselected total. Root preserved original metadata/logs in enterprise-validation-20260912 under operator-test-tmp. Both new workers have actual tmux3.4 available as garden-worker, verified September12 17:04UTC. Use disposable session names/paths and a harmless fake harness for the runtime probe; ask the operator for any required SSH transport setup rather than touching live runs.
- 2026-09-12T17:06:50+00:00 dispatched work run 20260912T170650Z-work-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2645 tokens)
- 2026-09-12T17:20:57+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-12T17:22:20+00:00 opened https://github.com/joshmarcus/context-garden/pull/505 (base main): Verified the five enterprise integrations together at accepted main 0c6b2c838c007af9c1f5101939e80a9f4e900fff and committed a reproducible validation note. All 416 focused tests, the disposable real-tmux probe, and Ruff passed; no in-scope regression was demonstrated. cost=$0.83
- 2026-09-12T17:24:59+00:00 automated review: approve — The documentation accurately records validation of the five enterprise integrations on accepted main. Source is accepted; exact-head CI remains a controller-enforced pending merge gate. cost=$0.24
- 2026-09-12T17:29:08+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-12T17:30:41+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/505
