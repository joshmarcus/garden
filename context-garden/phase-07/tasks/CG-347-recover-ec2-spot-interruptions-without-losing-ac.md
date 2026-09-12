---
id: CG-347
title: Recover EC2 Spot interruptions without losing accepted work or exceeding pool limits
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-216
- CG-346
priority: 2
order: 6
difficulty: hard
reading:
- context-garden/phase-06/specs/ec2-workers.md
branch: garden/cg-347-recover-ec2-spot-interruptions-without-losing-ac
pr: https://github.com/joshmarcus/context-garden/pull/417
attempts: 1
last_dispatched_at: '2026-09-10T13:29:55+00:00'
created: '2026-09-06T16:27:50+00:00'
updated: '2026-09-10T13:51:26+00:00'
---

## Owner validation policy, 2026-09-10

Live canaries are optional and cannot be required for task acceptance, review, merge, release or phase closure. Proportionate deterministic tests, provider fakes, protocol integration and disposable offline bootstrap/lifecycle exercises establish the required behavior. Report live-cloud coverage as untested when absent; that absence alone is not a blocker. Preserve genuine correctness, security, recovery, deadline and resource requirements. Any optional live exercise still requires its own applicable resource/spending authorization. This supersedes older live-canary or paid clean-image rollout requirements, including historical operator dispositions below.

## Goal and evidence

### Current operator disposition, 2026-09-10

Run 20260910T012444Z-work produced clean committed implementation e526c1884c7e97b53f9756fb0f534e0779f95d37 with 92 focused tests and Ruff reported passing. The owner has removed the live-canary requirement. Preserve and finish this existing implementation through proportionate offline verification and ordinary PR/check/review flow; do not implement it again or request cloud credentials. No live provisioning is needed. Missing live coverage is explicitly untested, not a completion blocker.

Add Spot purchase policy and replacement on top of managed EC2 execution. Handle interruption notices and abrupt loss without notice, preserve recoverable work/transcripts, fence stale attempts and respect the configured capacity and spend envelope. On-demand fallback is opt-in and priced explicitly.

Exercise interruption during work, checks and result upload; stale-worker return after reassignment; no available Spot capacity; and repeated controller reconciliation. Prove no duplicate result acceptance or merge, no canonical branch overwrite by stale workers, bounded retries, and separate retry/model-cost accounting. Use deterministic simulations and disposable offline integration tests; live canaries are optional. Do not claim an exactly-once execution guarantee.

## Provenance and scheduling

Requested by Josh on 2026-09-06: automate EC2 instances for remote workers. See the shared spec for outcomes and design guidance. Owner explicitly brought this work into phase 05 on 2026-09-07. Implementation is authorized now under ordinary admission; live provisioning follows the spec’s bounded resource/cost plan.

## Pluggability requirement (owner clarification)

Expose generic interruption/drain/replacement events from the EC2 provider, with task checkpoint/retry behavior implemented by the garden consumer. Capability-check Spot requests. Remote-dev profiles default to on-demand and persistent storage; never apply disposable-worker destruction or replacement policies to a person's development workspace. A dev profile may opt into Spot only with an explicit recoverable-workspace policy.

## Suggestions

- [x] 2026-09-09 web (applies to goal): Drop live canary requirement — applied under explicit owner policy on 2026-09-10.

## Log

- 2026-09-07T12:47:31+00:00 moved from context-garden/phase-06 to context-garden/phase-05
- 2026-09-10T03:18:04+00:00 reset to ready by hand
- 2026-09-10T03:18:15+00:00 reset to ready by hand
- 2026-09-10T05:39:59+00:00 dispatched work run 20260910T053957Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~15682 tokens)
- 2026-09-10T05:52:27+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T05:53:39+00:00 opened https://github.com/joshmarcus/context-garden/pull/417 (base main): Added bounded EC2 Spot purchasing, interruption/abrupt-loss replacement, opt-in priced on-demand fallback, persistent-workspace safeguards, and generation-aware stale-host retirement. At head 198bf04b9d3e2366f2baddc71d6578a06302107f, 156 focused lifecycle/remote-worker/scheduler tests and Ruff passed. cost=$1.77
- 2026-09-10T05:53:46+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/hosts/core.py); a rebase agent will resolve it
- 2026-09-10T05:56:19+00:00 dispatched rebase run 20260910T055617Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1553 tokens)
- 2026-09-10T05:58:34+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/417: Rebased CG-347 onto origin/main, combining shared operation identities with replacement-generation fencing while preserving both sides' changes. cost=$0.01
- 2026-09-10T06:00:59+00:00 automated review requested changes: Abrupt-loss replacement and generation fencing are covered, but the implemented notice path cannot receive actual EC2 Spot interruption or rebalance signals. cost=$0.44
- 2026-09-10T06:01:10+00:00 dispatched revise run 20260910T060107Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~16727 tokens)
- 2026-09-10T06:06:47+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T06:08:05+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/417: Added a durable EventBridge-compatible EC2 event source that translates actual Spot interruption warnings and rebalance recommendations into the provider-neutral recovery path. Verified replacement fencing and remote-worker behavior with 137 focused tests, reran the final 27 host tests, and passed Ruff across src, tests, and scripts. cost=$0.89
- 2026-09-10T06:10:37+00:00 automated review requested changes: Spot purchasing and abrupt-loss generation rotation are covered, but the production notice path remains disconnected and destroys warned hosts before recoverable work can drain. cost=$0.45
- 2026-09-10T06:15:21+00:00 dispatched revise run 20260910T061518Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17254 tokens)
- 2026-09-10T06:24:21+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T06:25:33+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T06:26:43+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T06:28:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/417: Connected production EC2 Spot notices through a durable SQS/EventBridge journal and added a bounded worker-drain handshake before replacement. At head 0196f671e0dc3b835e304e8b9460836fd4ad1655, 33 focused host/CLI/protocol tests and Ruff across src, tests, and scripts passed; live-cloud coverage was not run. cost=$1.92
- 2026-09-10T06:30:19+00:00 automated review requested changes: Spot recovery behavior passes focused tests, but the production CLI still permits Spot provisioning with interruption handling disconnected. cost=$0.56
- 2026-09-10T10:53:57+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T11:01:17+00:00 dispatched revise run 20260910T110113Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17685 tokens)
- 2026-09-10T11:04:44+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:06:07+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/417: Closed the production CLI bypass so every Spot scale operation requires durable interruption-event configuration before AWS access, and documented the drain module in the architecture map. At exact head 26cb9fe61f783bbc94220233e3d78909480bfbfe, 136 focused host/CLI/protocol/architecture tests and repository Ruff passed; live-cloud coverage was not run. cost=$0.48
- 2026-09-10T11:08:40+00:00 automated review requested changes: Spot interruption recovery, draining, and stale-generation fencing are covered, but an explicit Spot maximum price can bypass the pool's admission estimate and spend limit. cost=$0.48
- 2026-09-10T11:42:58+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T11:44:34+00:00 dispatched revise run 20260910T114431Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18054 tokens)
- 2026-09-10T11:49:25+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:50:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/417: Bound explicit Spot maximum prices into capacity admission so launch ceilings cannot bypass pool spend limits, and reject invalid ceilings before AWS access. Committed as 267a508f; 43 focused host/CLI/safety tests and repository Ruff passed. cost=$0.76
- 2026-09-10T11:53:44+00:00 automated review requested changes: Spot interruption recovery and fencing are well covered, but Spot launches without an explicit maximum price can still exceed the pool's admitted cost estimate. cost=$0.33
- 2026-09-10T13:25:02+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T13:29:34+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T13:29:55+00:00 dispatched revise run 20260910T132952Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~18485 tokens)
- 2026-09-10T13:34:59+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:36:25+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/417: Closed the omitted-MaxPrice budget path by admitting the on-demand hourly price as Spot's implicit ceiling and rejecting unpriced or over-budget launches before AWS access. Commit ded2aa5c passed 37 focused host/CLI tests and repository Ruff. cost=$0.60
- 2026-09-10T13:39:53+00:00 automated review: approve — Spot interruption recovery, stale-generation fencing, durable draining, bounded replacement, and explicit/implicit price admission satisfy the task goal. cost=$0.42
- 2026-09-10T13:49:49+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T13:51:26+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/417
