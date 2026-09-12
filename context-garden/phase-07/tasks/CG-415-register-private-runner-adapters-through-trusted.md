---
id: CG-415
title: Register private runner adapters through trusted configuration
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 1
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-415-register-private-runner-adapters-through-trusted
pr: https://github.com/joshmarcus/context-garden/pull/329
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T23:12:59+00:00'
created: '2026-09-07T20:05:53+00:00'
updated: '2026-09-09T01:29:52+00:00'
---

## Goal

Register private runner adapters through trusted configuration. Recheck current implementation before choosing the smallest compatible change.

## Acceptance criteria

- [ ] Allow explicitly configured dotted-path runner registration while retaining built-in names and aliases. Validate the required interface/version and capability declarations.
- [ ] Resolve registrations only from trusted operator configuration, not worker results, task content or arbitrary repository files. Reject silent replacement of built-ins and report missing imports clearly.
- [ ] Apply ordinary environment, admission, ownership and result validation to adapters; registration cannot exempt a runner from fences or human review gates.
- [ ] Demonstrate a separately packaged synthetic runner without editing the public package. Keep imports side-effect-free during read-only diagnostics, or explicitly isolate validation if import-time code would execute.

## Provenance and scope

Owner-provided additional gap F8, 2026-09-07. Generic requirements only. This task remains a phase-07 draft and does not authorize new access, deployment or external notifications. Refer to the shared spec, not the private environment survey.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T17:07:06+00:00 dispatched work run 20260908T170706Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9251 tokens)
- 2026-09-08T17:35:02+00:00 opened https://github.com/joshmarcus/context-garden/pull/329 (base main): Private runner adapters can now be registered by trusted operator configuration with explicit interface and capability declarations, while built-ins remain protected. Adapter registrations are fenced as executable configuration and use the normal scheduler lifecycle. cost=$1.11
- 2026-09-08T17:55:25+00:00 automated review requested changes: The adapter contract and scheduler integration are well tested, but `garden doctor` imports arbitrary private adapter modules in-process, violating the explicit side-effect-free diagnostic requirement. cost=$0.31
- 2026-09-08T17:56:43+00:00 dispatched revise run 20260908T175642Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~10345 tokens)
- 2026-09-08T18:16:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/329: Doctor now keeps private runner adapters outside the controller import boundary, reporting declarative syntax validity and deferring runtime contract validation until dispatch. A side-effecting separately packaged synthetic adapter regression proves the diagnostic leaves import-time state untouched. cost=$0.65
- 2026-09-08T18:29:32+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/cli/diagnostics.py, src/garden/config.py); a rebase agent will resolve it
- 2026-09-08T18:52:15+00:00 check did not run (20260908T183113Z-check): idle 21 min (no output or file change); will retry
- 2026-09-08T18:59:13+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:00:46+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:02:17+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:03:47+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:05:18+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:06:50+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:08:23+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:10:26+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:12:05+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:14:11+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:16:22+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:18:43+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:20:45+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:23:02+00:00 check did not run (20260908T185215Z-check): exit 126; retry also failed; needs human
- 2026-09-08T19:23:55+00:00 Operator verified deployment-era interrupted check/review, preserved failed record, queued exactly one current-head replay/review through current controller runtime; no implementation retry.
- 2026-09-08T19:26:04+00:00 feedback from an untrusted author ignored: Copilot: > @copilot resolve the merge conflicts in this pull request

Merged main and resolved conflicts in `src/garden/config.py` (combined `EXECUTABLE_KEYS`, keeping both `worker_env.config_files` and `runne
- 2026-09-08T19:26:04+00:00 1 new review item(s)
- 2026-09-08T21:21:50+00:00 automated review: request_changes — Private adapter registration and diagnostic isolation are well covered, but a custom local adapter bypasses the scheduler's local-capacity admission gate. The PR should not merge until admission uses adapter capabilities rather than built-in names. cost=$0.47
- 2026-09-08T22:40:34+00:00 dispatched rebase run 20260908T224031Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1965 tokens)
- 2026-09-08T22:43:04+00:00 preserved uncommitted worktree changes from run 20260908T224031Z-rebase outside the PR: `git stash apply ece821a72569fa7b5688936b69e4850df2f3dd1f` in /home/joshua/work/worktrees/CG-415 (garden:CG-415:20260908T224031Z-rebase:reap)
- 2026-09-08T22:44:45+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/329: Resolved both rebase conflicts and completed the rebase onto origin/main. cost=$0.01
- 2026-09-08T22:45:27+00:00 stuck: pending feedback recorded but the task is in_review, not changes_requested; resume with one more round (`garden retry CG-415`) or send it back (`garden triage CG-415 --changes "..."`)
- 2026-09-08T23:12:26+00:00 triage: changes requested by hand: Operator verified current rebased7cbf22f still has the real prior defect: dispatch.py:108 gates only runner.name==local,
- 2026-09-08T23:12:59+00:00 dispatched revise run 20260908T231259Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~14246 tokens)
- 2026-09-08T23:41:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/329: Private local runner adapters now use their validated execution capability for scheduler admission and active-run accounting, preventing aliases from bypassing local capacity. Added a bounded synthetic-adapter regression and committed the fix as a23f2c5fd709d89c75e5918026fdc3b7552e98b2. cost=$0.84
- 2026-09-09T00:47:55+00:00 PR 329 merged at exact reviewed head a23f2c5fd709d89c75e5918026fdc3b7552e98b2 as merge commit 4b63471a1b888a1ce9d791d19af8dfd7266bd83c. Operator review attestation records the trusted-registration and corrected private-local-admission assessment; both exact-head CI runs passed. Mark complete by merged ancestry.
- 2026-09-09T01:29:52+00:00 automated review could not start: CG-415 is done: #329 was merged at 00:47:55
