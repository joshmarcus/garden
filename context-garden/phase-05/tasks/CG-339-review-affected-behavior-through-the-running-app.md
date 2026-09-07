---
id: CG-339
title: Review affected behavior through the running application before accepting interaction claims
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-05/specs/stabilization.md
branch: garden/cg-339-review-affected-behavior-through-the-running-app
pr: https://github.com/joshmarcus/context-garden/pull/254
attempts: 1
last_dispatched_at: '2026-09-07T06:03:41+00:00'
created: '2026-09-06T13:46:32+00:00'
updated: '2026-09-07T09:13:14+00:00'
---

## Goal

Review affected behavior through the running application before accepting interaction claims

## Context

Build on CG-315 capture evidence and CG-324 required evidence. Add actual interaction coverage for applicable PRs, with task objective, empty and failure states, browser observations and evidence tied to the tested head. Treat no_change and attention prompts as user outcomes, not just state transitions. Use disposable gardens, never the live operator queue.

## Acceptance criteria

- [ ] A reviewer can replay an affected flow in the real running app and distinguish screenshot-only evidence from performed actions. Applicable PRs with missing, failed or stale interaction evidence cannot be accepted as verified. Non-UI changes keep proportionate validation.
- [ ] The report cites commands, observed results and artifact paths, distinguishes automated checks from real interaction, and states all unverified requirements.

## Log

- 2026-09-06T13:46:34+00:00 approved (cli)

## Web-incident retro extension, 2026-09-06

CG-357 initially claimed performance evidence using inert worker records and ten in-process HTTP samples; an extrapolated p95 exceeded the maximum. Require applicable scalability claims to include a served disposable app, representative and larger history sizes, repeated cache-expiry intervals, actual executing bounded workload processes, empirical latency distribution and read/scan counts. Explicitly distinguish controlled load from real model harnesses. Tie evidence to reviewed head; a reviewer must refresh the comparison base before claiming unrelated history. Counterfactual: this evidence gate before the Now rollout would have exposed repeated full-history reads before normal operation failed. Existing operator recovery benchmark in product docs/design/cg357-validation is a starting point, not proof this policy is enforced.
- 2026-09-07T02:01:09+00:00 dispatched work run 20260907T020052Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10233 tokens)
- 2026-09-07T02:13:34+00:00 preserved uncommitted worktree changes from run 20260907T020052Z-work outside the PR: `git stash apply fc1f601846eba0ad31f16ee41f134f7b8d53d665` in /home/joshua/work/worktrees/CG-339 (garden:CG-339:20260907T020052Z-work:reap)
- 2026-09-07T02:16:07+00:00 opened https://github.com/joshmarcus/context-garden/pull/254 (base main): Automated reviews now require head-bound, replayable running-application evidence for UI and lifecycle changes, and mechanically reject missing, failed, stale, live-garden, or incomplete interaction claims. Scalability claims additionally require served load, multiple history sizes and cache intervals, executing workloads, empirical latency, read/scan counts, and honest load provenance. cost=$2.39
- 2026-09-07T02:18:37+00:00 automated review requested changes: The running-app journey succeeds, but the mechanical gate can exempt lifecycle changes outside its narrow path allowlist and accepts structurally incomplete scalability evidence. Applicable PRs can therefore still be approved without the required proof. cost=$0.51
- 2026-09-07T03:05:26+00:00 dispatched revise run 20260907T030525Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~11242 tokens)
- 2026-09-07T03:16:08+00:00 preserved uncommitted worktree changes from run 20260907T030525Z-revise outside the PR: `git stash apply c6a66c461a692b8603a75266e7a3c681f00e475a` in /home/joshua/work/worktrees/CG-339 (garden:CG-339:20260907T030525Z-revise:reap)
- 2026-09-07T03:30:20+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/254: Expanded interaction-evidence applicability across lifecycle-owning modules and added strict semantic validation for scalability evidence. Added classifier, boundary, and scheduler-level enforcement tests; exact-commit CI passed. cost=$1.21
- 2026-09-07T03:32:37+00:00 automated review requested changes: The disposable nine-flow application journey passes, but the mechanical gate still misses applicable lifecycle/scalability changes and accepts screenshot-only placeholders as performed interaction evidence. cost=$0.36
- 2026-09-07T03:40:30+00:00 dispatched revise run 20260907T034029Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~11582 tokens)
- 2026-09-07T03:50:34+00:00 preserved uncommitted worktree changes from run 20260907T034029Z-revise outside the PR: `git stash apply d81b8fef92b0e86b8e6b2bf491fd7c0fa1bea3c0` in /home/joshua/work/worktrees/CG-339 (garden:CG-339:20260907T034029Z-revise:reap)
- 2026-09-07T03:58:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/254: Interaction-evidence enforcement now covers review and stabilization lifecycle modules, evaluates scalability claims from task and PR context, and rejects malformed, screenshot-only, generic, or stale evidence. The final head passed focused checks, a nine-flow disposable running-app replay, lint, and exact-commit CI. cost=$1.33
- 2026-09-07T05:39:12+00:00 PR conflicts with main; rebase onto main conflicts (docs/worker-protocol.md); a rebase agent will resolve it
- 2026-09-07T05:54:06+00:00 dispatched rebase run 20260907T055403Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~10067 tokens)
- 2026-09-07T05:56:32+00:00 preserved uncommitted worktree changes from run 20260907T055403Z-rebase outside the PR: `git stash apply c9e1047913e91d317f09e08a5b16fad73cde55a0` in /home/joshua/work/worktrees/CG-339 (garden:CG-339:20260907T055403Z-rebase:reap)
- 2026-09-07T05:57:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/254: Rebased CG-339 onto origin/main and merged both sides of the worker-protocol documentation conflict. cost=$0.01
- 2026-09-07T05:59:24+00:00 automated review requested changes: The focused tests pass, but the gate still accepts screenshot-only placeholder records, and the PR's verification is stale after the rebase. Applicable interaction claims can therefore be approved without performed, head-bound evidence. cost=$0.33
- 2026-09-07T06:03:41+00:00 dispatched revise run 20260907T060340Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~12111 tokens)
- 2026-09-07T06:15:49+00:00 preserved uncommitted worktree changes from run 20260907T060340Z-revise outside the PR: `git stash apply ffdb32a7352590b0fa83adfed4cf1b49b2a46398` in /home/joshua/work/worktrees/CG-339 (garden:CG-339:20260907T060340Z-revise:reap)
- 2026-09-07T06:17:08+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/254: Interaction review enforcement now requires independently structured served-HTTP or browser-action events with observed results for affected, empty, and failure/recovery states, rejecting screenshot-only placeholders. The final head passed the nine-flow disposable running-app replay, focused tests, lint, and exact-commit CI. cost=$1.30
- 2026-09-07T06:18:28+00:00 automated review requested changes: The enforcement is head-bound and rejects screenshot placeholders, but it does not prove the required empty or failure/recovery behavior and overclassifies pure non-UI changes. cost=$0.28
- 2026-09-07T06:19:03+00:00 stuck: 3 revision rounds already used; resume with one more round (`garden retry CG-339`) or send it back (`garden triage CG-339 --changes "..."`)
- 2026-09-07T09:13:13+00:00 triage: changes requested by hand: Owner delegates this routine recovery. Address the concrete preserved review findings below; self-review and repair befo
- 2026-09-07T09:13:14+00:00 re-enabled by hand; revise run will follow
