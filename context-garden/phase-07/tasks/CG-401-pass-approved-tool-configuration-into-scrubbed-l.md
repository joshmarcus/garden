---
id: CG-401
title: Pass approved tool configuration into scrubbed local and remote workers
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: hard
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-401-pass-approved-tool-configuration-into-scrubbed-l
pr: https://github.com/joshmarcus/context-garden/pull/315
runner: local
attempts: 1
last_dispatched_at: '2026-09-08T13:52:46+00:00'
created: '2026-09-07T19:56:16+00:00'
updated: '2026-09-08T18:21:32+00:00'
---

## Goal

Implement explicit minimal config-file transport alongside existing directory and environment allowlists, governed by the approved policy.

## Acceptance criteria

- [ ] Allow only named source-to-destination mappings; reject traversal and unsafe symlink destinations, apply restrictive permissions, and do not copy the entire home or unrelated instructions.
- [ ] Local, SSH and portable worker paths apply equivalent policy; doctor verifies required tools and authentication in the actual scrubbed environment without exposing secrets.
- [ ] Test an allowed tool definition, missing config, denied tool and credential revocation; secret sentinels never enter claims, logs, briefs, notifications or committed output.

## Scope and provenance

Owner requested extraction into phase 07 on 2026-09-07. Generic capability mapping: G8. Read the phase spec; the private source survey is deliberately excluded from worker reading lists. Recheck the current implementation before adding code. This task does not authorize provisioning, internal access changes, production writes or publication of private facts.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T02:39:53+00:00 Owner requested removal of CG-400 and its dependency links; removed dependency. Existing task status and explicit holds preserved.
- 2026-09-08T13:52:46+00:00 dispatched work run 20260908T135246Z-work-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~9214 tokens)
- 2026-09-08T14:24:51+00:00 opened https://github.com/joshmarcus/context-garden/pull/315 (base main): Added named, fail-closed config-file mappings for local, SSH, and portable workers, with restrictive permissions, symlink/traversal protection, revocation behavior, scrubbed doctor authentication checks, and secret-free remote claims. Documented the configuration and committed the work in three focused commits. cost=$4.61
- 2026-09-08T14:44:31+00:00 check did not run (20260908T143952Z-check): idle 21 min (no output or file change); will retry
- 2026-09-08T14:45:44+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:46:57+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:48:08+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:49:24+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:50:44+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:51:55+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:53:12+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:54:27+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:55:48+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:57:01+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:58:14+00:00 check did not run (20260908T144431Z-check): idle 22 min (no output or file change); retry also failed; needs human
- 2026-09-08T14:59:03+00:00 triage: marked ready for review (Retired stale failed remote replay. Use local backend for controller-owned replay and review; origin)
- 2026-09-08T15:45:12+00:00 review validation scope expansion: portable worker doctor configuration — The CLI call omits the configuration argument added to doctor_worker, contradicting the actual-scrubbed-environment criterion.
- 2026-09-08T15:45:12+00:00 review validation scope expansion: config-file claim interaction and empty state — The supplied replay covers generic dispatch/reap flows but neither config-file claims nor an empty state.
- 2026-09-08T15:45:13+00:00 automated review requested changes: The file transport and focused regressions are sound, but the portable worker’s public doctor command never receives the approved mapping configuration, so it cannot verify the actual configured scrubbed environment. The required interaction replay also lacks an empty-state journey and does not exercise config-file claims. cost=$0.36
- 2026-09-08T18:21:32+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/315
