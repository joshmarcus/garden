---
id: CG-216
title: 'Workers on independent remote hosts: a worker agent that claims runs from the garden over HTTP,
  works in its own clone, pushes the branch and posts the result and transcript back'
status: running
product: context-garden
phase: phase-05
depends_on: []
priority: 1
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
attempts: 1
last_dispatched_at: '2026-09-06T06:08:31+00:00'
created: '2026-09-05T16:12:08+00:00'
updated: '2026-09-06T06:08:31+00:00'
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
