---
id: CG-643
title: Attach to a running task over SSH from the CLI
status: ready
product: context-garden
phase: phase-07
depends_on:
- id: CG-629
  after: merge
- id: CG-641
  after: merge
priority: 2
difficulty: medium
reading:
- src/garden/cli/diagnostics.py
- src/garden/runner/ssh.py
- src/garden/runs.py
- docs/worker-protocol.md
runner: remote
discovered_from: 'owner: cli command to ssh to a specific running task and join the tmux session in process'
created: '2026-09-12T17:42:02+00:00'
updated: '2026-09-12T17:42:02+00:00'
---

## Goal

Add a CLI command, preferably `garden attach TASK_ID`, that connects over SSH to the host running that task and joins its existing live tmux session. The operator should not have to find the host, reconstruct a session name or copy a command from `garden log`.

## Existing behavior and scope

Enterprise PR497 introduced durable SSH sessions. `garden log TASK_ID` currently prints the logical host and a manual `tmux attach-session -r -t ...` command, leaving SSH connection and attachment to the user. Reuse the recorded `ssh_tmux_session`, run identity and configured SSH transport rather than introducing another execution backend. CG641 verified this integration; CG629 supplies multiplayer identity and role foundations. Build against their accepted source.

Some managed remote runs execute directly under a supervisor and do not have a tmux session. Discover actual capabilities and explain this case clearly; never fabricate an attachable session or start another copy of the task to satisfy the command. This task does not convert all execution backends to tmux or implement Herdr.

## Acceptance criteria

- [ ] Resolve the requested task to its current active run, configured remote host and exact recorded tmux session. Allow an explicit run selector when needed and reject ambiguous, stale, finished or missing-session targets with useful diagnostics. Do not silently attach to another attempt, an arbitrary session, or the latest completed run.
- [ ] Open SSH with an allocated terminal and attach to that existing session using the supported host/user/port/key/proxy configuration and normal host-key verification. Construct arguments safely; task, host and session strings cannot inject shell commands. Respect existing access rules, including member/task authorization in multiplayer mode and denying viewer-only terminal access. Do not expose credentials in output.
- [ ] Default to the current read-only observation behavior so joining does not send keystrokes to the agent. Preserve normal tmux detach behavior, never detach other clients, and ensure exiting or losing the attaching SSH connection leaves the task and session running. Do not mutate task status, claims, publication, or worker lifecycle merely by attaching.
- [ ] Provide clear handling of a noninteractive local terminal, unreachable host, absent SSH/tmux, run completion during connection and execution backends without an existing tmux session. Keep `garden log` available for those cases and document the distinction between attachment and log streaming.
- [ ] Cover task/run/host/session selection, authorization, safe command construction and detach/non-cancellation behavior with focused tests. Exercise the attachment path against a disposable tmux session with a suitable terminal/transport check and state honestly which parts used a test double. Tear down only the owned disposable session in a finally path: a retained tmux server can otherwise hold the enclosing managed-worker supervisor open. Update CLI help and the worker-protocol guide, and pass normal independent review and current-head CI.

## Authorization and constraints

Owner explicitly requested this implementation task on September12. Use the existing two remote workers and retain their September13 8a.m.Eastern shutdown,120USD cap/8USD reserve and resource limits. No extra infrastructure, worker restart, production rollout or change to other holds. The separate CG642 Herdr evaluation remains a frozen draft; do not conflate it with this implementation.

## Log

- 2026-09-12T17:42:02+00:00 approved (owner requested SSH/tmux attach CLI task)
