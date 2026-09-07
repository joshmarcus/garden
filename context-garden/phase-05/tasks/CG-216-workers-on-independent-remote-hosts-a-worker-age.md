---
id: CG-216
title: 'Workers on independent remote hosts: a worker agent that claims runs from the garden over HTTP,
  works in its own clone, pushes the branch and posts the result and transcript back'
status: changes_requested
product: context-garden
phase: phase-05
depends_on: []
priority: 1
order: 0
difficulty: hard
reading:
- src/garden/runner/base.py
- src/garden/runner/ssh.py
- src/garden/runner/local.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/reap.py
- src/garden/web/pages/api.py
- src/garden/web/trust.py
- docs/worker-protocol.md
- docs/architecture.md
branch: garden/cg-216-workers-on-independent-remote-hosts-a-worker-age
pr: https://github.com/joshmarcus/context-garden/pull/221
last_dispatched_at: '2026-09-07T16:36:44+00:00'
created: '2026-09-05T16:12:08+00:00'
updated: '2026-09-07T18:04:43+00:00'
---

## Goal

A worker can run on a machine the scheduler cannot reach and that shares nothing with it: no filesystem, no ssh from the garden, only HTTPS to the garden's web app and git access to the product repository. A `garden worker` agent on that host claims runs, does the work in its own clone with its own environment, pushes the branch, and posts the result, usage and transcript back; the scheduler reaps remote runs exactly like local ones, and reviews, checks, rebases and persona runs can be claimed the same way.

## Context

Asked by the user on 2026-09-05 for phase 05: "supporting workers that run on independent remote hosts." Today `runner: ssh` needs the scheduler to reach the host over ssh and to hold a clone per product there, and `runner: local` needs the worktree on the scheduler's disk; both assume the scheduler drives the process. A team's build farm, a cloud sandbox or a colleague's laptop are none of those. The web app is already the hub the loop talks through; `web/trust.py` has the origin check and trusted-author model; the worker environment scrub (CG-154, CG-194) defines what a worker may see; `docs/worker-protocol.md` is the step-by-step contract this task extends.

## Design

- **A runs API on the garden.** `POST /api/runs/claim` (host name, harness names and tiers it offers, capacity) returns one run the host may take: the brief, the mode, the branch and base, the product repo URL, the setup block, the turn cap and the env allowlist; the run is marked `claimed` by that host with a lease. `POST /api/runs/<id>/heartbeat` renews the lease and streams transcript chunks; `POST /api/runs/<id>/finish` posts the exit code, the final message, usage and cost, and confirms the pushed branch head. A lease that lapses returns the run to the queue (the same dead-run logic as CG-144 and CG-198).
- **Auth.** A per-host token in `garden.yaml` (`workers.hosts[].token_env`) sent as a bearer header; the origin check is bypassed for token-authenticated API routes only; tokens are never in the brief. Git access is the host's own (deploy key or the person's credentials).
- **`garden worker --garden <url> --host <name> [--once]`.** A long-running agent shipped with the tool: polls claim, prepares or reuses a clone under its own work dir, runs the product's `setup.command` there, runs the harness with the scrubbed environment, commits and pushes, posts finish; it never touches `.garden/` and needs nothing from the scheduler's disk. One `--once` mode for CI-style hosts.
- **Scheduler side.** `runner: remote` is a third runner: dispatch enqueues instead of launching, `active_runs` counts claimed runs against the host's capacity, reap reads what the host posted; the fence checks the pushed head against the claimed base; a run's page shows the host. Local and remote runners can coexist: a task or product can prefer a host by tag.
- **What stays the same.** Briefs, results, reviews, the merge queue, cost accounting and the task pages; a remote run is a run record with `host` set.

## Acceptance criteria

- [ ] The three API routes exist with bearer-token auth, leases and a returned-to-queue path; the origin check still applies to browser POSTs.
- [ ] `garden worker` on a second machine (a throwaway VM or container in the test, a fake harness in CI) claims a work run, pushes a branch and posts the result; the scheduler opens the PR and reviews it as usual, and the run page shows the host.
- [ ] A remote review run and a remote check run complete the same way; a lapsed lease returns the run to the queue and the task is not failed.
- [ ] `docs/worker-protocol.md` and `docs/architecture.md` describe the remote flow; `garden doctor` on the worker host checks git access, the harness and the token.
- [ ] No scheduler credential reaches the worker host; a test asserts the claim payload carries only the allowlisted names.
- 2026-09-06T00:55:00+00:00 deferred by the operator: last in dispatch order (joined phase-05 goals, goal 4); approve once the onboarding and routing work is in

## Log

- 2026-09-06T03:38:35+00:00 approved (web)
- 2026-09-06T04:10:53+00:00 dispatched work run 20260906T040922Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~25151 tokens)
- 2026-09-06T04:54:48+00:00 opened https://github.com/joshmarcus/context-garden/pull/221 (base main): Added bearer-authenticated, lease-based remote run claiming plus the `garden worker` agent, independent clone execution, branch pushing, transcript/result reporting, and scheduler integration for work, review, and check runs. Added end-to-end coverage and updated the worker protocol and architecture documentation. cost=$4.22
- 2026-09-06T04:59:44+00:00 automated review requested changes: The pull-based work path is present, but remote checks lose required context, leases do not fence stale workers, and the worker does not upload its transcript. The tests also do not exercise a completed remote review or check run. cost=$0.76
- 2026-09-06T05:07:42+00:00 dispatched revise run 20260906T050735Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~27819 tokens)
- 2026-09-06T05:39:32+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/221: Remote leases now fence stale workers, checks retain portable scheduler context, transcripts return to the garden, and integration coverage completes remote work, check, and review runs. All changes are committed and the full test and lint suites pass. cost=$2.36
- 2026-09-06T05:59:00+00:00 automated review requested changes: Remote execution is substantially implemented, but expired workers can still push after lease loss, and claim payloads can expose credentials embedded in repository URLs or harness arguments. cost=$0.48
- 2026-09-06T06:08:31+00:00 dispatched revise run 20260906T060704Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~28189 tokens)
- 2026-09-06T07:40:13+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated cost=$4.73
- 2026-09-06T07:41:08+00:00 dispatched revise run 20260906T074100Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~29318 tokens)
- 2026-09-06T08:07:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/221: Stabilized the scripted canary by aligning HTTP request timeouts with the configured flow deadline. The previously failing canary and the complete test and lint suites pass. cost=$1.27
- 2026-09-06T08:12:10+00:00 automated review requested changes: Remote work, review, check, lease reclaim, and staged-push fencing are well covered, but persona runs remain local-only and setup commands can leak scheduler credentials in claim payloads. cost=$0.74
- 2026-09-06T08:14:42+00:00 stuck: 3 revision rounds already used; resume with one more round (`garden retry CG-216`) or send it back (`garden triage CG-216 --changes "..."`)
- 2026-09-06T13:15:34+00:00 nothing to fix; resumed to in review by hand
- 2026-09-06T13:18:22+00:00 triage: changes requested by hand: Owner-authorized revision: address the last automated review in full. Enable the promised remote persona flow or explici
- 2026-09-06T13:18:26+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T13:45:02+00:00 Owner-directed feature deferral until phase-05 stabilization is demonstrated. Preserve existing branch and PR; no further implementation or merge before the gate passes.
- 2026-09-06T13:45:03+00:00 moved from context-garden/phase-05 to context-garden/phase-06
- 2026-09-07T12:47:30+00:00 moved from context-garden/phase-06 to context-garden/phase-05

## Owner scope update, 2026-09-07

Remote AWS workers are now phase-05 work, without waiting for local stabilization failure. Preserve existing PRs, branches, evidence and dependency order. The reusable host lifecycle must still support non-garden remote development hosts. This supersedes earlier feature-deferral notes; it does not approve an old PR verdict or waive validation.
- 2026-09-07T12:47:30+00:00 approved (owner-phase05-promotion)
- 2026-09-07T12:47:30+00:00 reset to ready by hand
- 2026-09-07T12:47:52+00:00 triage: changes requested by hand: - **triage** (human): Owner-authorized revision: address the last automated review in full. Enable the promised remote p
- 2026-09-07T12:47:53+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T13:03:43+00:00 dispatched revise run 20260907T130341Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~22894 tokens)
- 2026-09-07T13:25:23+00:00 preserved uncommitted worktree changes from run 20260907T130341Z-revise outside the PR: `git stash apply 1343bf9e336991b5728f142b28b7078bc581681a` in /home/joshua/work/worktrees/CG-216 (garden:CG-216:20260907T130341Z-revise:reap)
- 2026-09-07T13:35:26+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/221: Completed pull-based remote execution for work, review, check, and persona runs. Setup commands are now host-owned so embedded scheduler credentials never cross the claim API, and worker-push documentation consistently describes lease-specific staging refs. cost=$4.33
- 2026-09-07T13:40:58+00:00 automated review requested changes: Remote execution is substantially implemented, but leases are not renewed during several potentially long stages and credential stripping misses SCP-style repository URLs. These defects violate the lease and credential-isolation criteria. cost=$1.26
- 2026-09-07T13:41:15+00:00 stuck: 3 revision rounds already used; resume with one more round (`garden retry CG-216`) or send it back (`garden triage CG-216 --changes "..."`)
- 2026-09-07T15:29:52+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-07T15:37:54+00:00 dispatched revise run 20260907T153748Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~24363 tokens)
- 2026-09-07T16:01:05+00:00 preserved uncommitted worktree changes from run 20260907T153748Z-revise outside the PR: `git stash apply a798d5ca3dc357382b54a3816df205b4448cd917` in /home/joshua/work/worktrees/CG-216 (garden:CG-216:20260907T153748Z-revise:reap)
- 2026-09-07T16:06:13+00:00 pre-PR checks failed (ui, UI captures); revise run will fix before the PR is updated cost=$2.75
- 2026-09-07T16:20:00+00:00 dispatched revise run 20260907T161958Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~24067 tokens)
- 2026-09-07T16:26:57+00:00 pre-PR checks failed (ui, UI captures); revise run will fix before the PR is updated cost=$0.82
- 2026-09-07T16:27:13+00:00 dispatched revise run 20260907T162711Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~24136 tokens)
- 2026-09-07T16:36:32+00:00 pre-PR checks failed (ui, UI captures); revise run will fix before the PR is updated cost=$1.34
- 2026-09-07T16:36:44+00:00 dispatched revise run 20260907T163643Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~24205 tokens)
- 2026-09-07T16:37:24+00:00 Operator incident containment: temporary manual admission hold after the current active revision drains, so P0 CG385 repair gets the sole recovery slot. Preserve current worker, PR, edits and feedback. Restore normal runner after CG385 is actually admitted; no owner action required.
- 2026-09-07T17:01:21+00:00 pre-PR checks failed (ui, UI captures) and 6 revision rounds already used; needs a human cost=$2.83
- 2026-09-07T17:01:39+00:00 Operator restored original runner after CG385 recovery repair acquired actual execution slot. Shared cap remains1.


## Operator recovery evidence, 2026-09-07
Controller/branch capture CLI incompatibility repaired in4a1371f8e77bf01c1ea1175871aca97649ccf438. Installed controller passed argv4 (JSON pages), branch accepted only argv3 and silently exited2. Both forms now accepted; legacy engine safely renders all pages. Focused regression passes. Actual installed-interpreter invocation with the new fourth argument produced56PNGs across14pages at1280/390 light/dark, all narrow clientWidth/scrollWidth390. Runtime69.2seconds,691MiB,noSwap. Source changes after this capture only add a blank line between test imports; production source identical to committed head. Evidence and JSON result: /home/joshua/work/operator-test-tmp/cg216-capture-compat/stdout.json; PNGs at sibling captures directory. Prior failed check run is honest history, superseded by this actual recovery capture, not grounds for another blind implementation revision. Exact-head CI34149879293 must pass before merge. CG389 records cross-version protocol diagnostics/prevention. Operator requests current-head automated review of remaining lease/credential and acceptance criteria; preserve all prior commits.
- 2026-09-07T18:04:27+00:00 re-enabled by hand with one more round past the revision cap; revise run will follow
- 2026-09-07T18:04:28+00:00 triage: marked ready for review
- 2026-09-07T18:04:41+00:00 converted back to draft on GitHub
- 2026-09-07T18:04:43+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/cli/diagnostics.py, src/garden/scheduler/checkruns.py, src/garden/scheduler/review.py, src/garden/web/pages/api.py); a rebase agent will resolve it
