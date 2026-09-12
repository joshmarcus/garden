---
id: CG-518
title: Enforce filesystem and network sandboxes for planning and approved tools
status: done
product: context-garden
phase: phase-06
depends_on:
- CG-245
- CG-401
- CG-406
priority: 0
difficulty: hard
reading:
- src/garden/kickoff.py
- src/garden/scheduler/kickoff.py
- src/garden/runner/base.py
- src/garden/harness.py
- src/garden/checks.py
- docs/architecture.md
- context-garden/phase-06/specs/context-garden-stripe-environment.md
branch: garden/cg-518-enforce-filesystem-and-network-sandboxes-for-pla
pr: https://github.com/joshmarcus/context-garden/pull/428
runner: remote
attempts: 1
last_dispatched_at: '2026-09-10T16:51:39+00:00'
created: '2026-09-10T11:18:52+00:00'
updated: '2026-09-10T17:10:22+00:00'
---

## Goal

Make filesystem and network policy an enforced execution capability for planners, synchronous kickoff, workers, checks and approved tools. Refuse permission modes or platform combinations that discard required deny paths or run without the configured sandbox.

## Context

CG-245 moved planning into a scrubbed scratch directory, CG-401 scopes tool configuration, and CG-406 fences canonical checkouts. Prompt and environment rules alone do not enforce the controller boundary when a harness bypass mode or missing OS sandbox retains broader authority.

## Acceptance criteria

- [ ] Define a capability-checked sandbox contract with authorized writable roots, readable context, named network destinations, subprocess inheritance and platform-specific enforcement reporting.
- [ ] Apply it to planning and synchronous kickoff as well as work, review and check execution. Scheduler state, credentials, sibling attempts and unrelated products remain outside the writable boundary.
- [ ] Reject bypass permission modes, missing enforcement capabilities and incompatible checkout strategies when policy requires isolation. Never silently drop deny paths or broaden network access.
- [ ] Preserve supported Linux, macOS and Windows-through-WSL execution through explicit mechanisms or actionable unsupported diagnostics; record which mechanism protected each run without leaking host details.
- [ ] Malicious planning documents and tool-output fixtures attempt controller reads/writes, symlink/path escapes, child-process escape and unapproved network access; all are denied while normal approved setup and publication still work.

enterprise_capability_key: enterprise-enforced-planner-tool-sandbox

## Log

- 2026-09-10T11:36:45+00:00 approved (owner all-drafts review; routed to renewed workers)
- 2026-09-10T11:37:02+00:00 dispatched work run 20260910T113702Z-work-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~26078 tokens)
- 2026-09-10T11:50:43+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T11:52:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/428 (base main): Added an opt-in, fail-closed execution sandbox contract that requires an installed OS wrapper, composes native Claude/Codex protections, rejects bypass and unsupported runners, constrains named network destinations, and records a host-detail-free mechanism for protected runs. Verified at commit 976fbba9 with 223 focused tests and clean Ruff lint. cost=$3.06
- 2026-09-10T11:55:20+00:00 automated review requested changes: The proposed wrapper contract can report enforcement without establishing it, and its writable-root contract conflicts with setup's required writes outside the worktree. cost=$0.40
- 2026-09-10T11:55:40+00:00 dispatched revise run 20260910T115540Z-revise-2 via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~27974 tokens)
- 2026-09-10T12:05:31+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T12:06:55+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/428: Added a versioned sandbox-wrapper capability handshake and explicit per-launch policies for readable, writable, protected, network, symlink, and descendant boundaries. Moved setup cache-marker writes into trusted controller bookkeeping; 200 focused tests and repository-wide Ruff lint passed at cecda732. cost=$1.64
- 2026-09-10T12:54:54+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: define a capability-checked sandbox co; run `garden triage CG-518 --changes "<feedback>" to unblock`
- 2026-09-10T13:25:06+00:00 triage: changes requested by hand: Change the sandbox validation approach to establish actual enforcement. A wrapper capability JSON or command-substring f
- 2026-09-10T13:25:40+00:00 dispatched revise run 20260910T132540Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~28534 tokens)
- 2026-09-10T13:33:34+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T13:34:57+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/428: Replaced self-attested sandbox validation with a bounded hostile-operation challenge and moved copied harness credentials outside writable worker homes. Verified commit 5f2bc7f5 with 171 focused tests and clean repository-wide Ruff lint; Linux was tested, while macOS and Windows-through-WSL were inspected but not executed. cost=$1.39
- 2026-09-10T13:35:13+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/harness.py); a rebase agent will resolve it
- 2026-09-10T13:35:20+00:00 dispatched rebase run 20260910T133520Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~1833 tokens)
- 2026-09-10T13:39:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/428: Rebased CG-518 onto origin/main and resolved the harness.py conflict. cost=$0.01
- 2026-09-10T13:42:59+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: apply it to planning and synchronous k; run `garden triage CG-518 --changes "<feedback>" to unblock`
- 2026-09-10T14:02:21+00:00 triage: changes requested by hand: Preserve the improved enforced sandbox and current green CI, but fix the remaining reviewed execution and denial-challen
- 2026-09-10T14:05:38+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:09:14+00:00 dispatched revise run 20260910T140913Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~28828 tokens)
- 2026-09-10T14:19:27+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:20:53+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/428: Sandboxed model results now use a narrowly authorized per-run output root and trusted supervisor publication, while the enforcement challenge verifies direct and descendant denial outside the full allowlist. Verified commit 75ef07a2 with 145 focused tests plus a final 12-test sandbox run and clean repository-wide Ruff lint. cost=$2.26
- 2026-09-10T14:23:36+00:00 stalled: review finding repeated after a revise round: acceptance criterion is explicitly unmet: define a capability-checked sandbox co; run `garden triage CG-518 --changes "<feedback>" to unblock`
- 2026-09-10T14:31:08+00:00 triage: changes requested by hand: Retain the enforced sandbox challenges and protected result publication that now pass. Close the two remaining execution
- 2026-09-10T14:33:40+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T14:34:00+00:00 dispatched revise run 20260910T143400Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~28942 tokens)
- 2026-09-10T14:38:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T14:40:17+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/428: Closed both reviewed execution-policy gaps and committed the fix as f0e9b5a8. Verified 125 focused tests pass and repository-wide Ruff lint is clean. cost=$1.01
- 2026-09-10T14:45:15+00:00 automated review: approve — The sandbox contract is fail-closed and is consistently applied across the requested local execution paths, with unsupported runners rejected explicitly. cost=$0.69
- 2026-09-10T14:49:15+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T14:49:24+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/harness.py, src/garden/runner/local.py); a rebase agent will resolve it
- 2026-09-10T14:49:28+00:00 dispatched rebase run 20260910T144928Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~6251 tokens)
- 2026-09-10T14:52:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/428: Rebased CG-518 onto origin/main and resolved all rebase conflicts while preserving both sandbox and main-branch behavior. cost=$0.03
- 2026-09-10T14:54:08+00:00 CI failure
- 2026-09-10T15:48:18+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T16:02:23+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T16:03:50+00:00 dispatched revise run 20260910T160349Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~29445 tokens)
- 2026-09-10T16:09:10+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:09:10+00:00 revision failed: remote worker finished without pushing commits
- 2026-09-10T16:18:26+00:00 triage: marked ready for review (Recovered the exact completed worker staging revisionf5bf5d84aedbfd7abfe6d8e6e94c1ed55f2db825 after )
- 2026-09-10T16:22:23+00:00 automated review: approve — The sandbox contract is fail-closed and consistently covers planning, kickoff, local workers, setup, command checks, retries, and protected result publication; unsupported execution modes return actionable errors. cost=$0.67
- 2026-09-10T16:26:34+00:00 automated review: approve — The sandbox contract is fail-closed and consistently covers planning, synchronous kickoff, local workers, setup, command checks, retries, and protected result publication. Unsupported runner/platform combinations produce explicit diagnostics. cost=$0.49
- 2026-09-10T16:30:29+00:00 automated review: approve — The sandbox contract is fail-closed and consistently covers planning, synchronous kickoff, local workers, setup, command checks, retries, and protected result publication. Unsupported runners and bypass modes are rejected with actionable diagnostics. cost=$0.60
- 2026-09-10T16:31:49+00:00 CI failure
- 2026-09-10T16:37:25+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T16:51:39+00:00 dispatched revise run 20260910T165139Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~29480 tokens)
- 2026-09-10T16:56:56+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T16:58:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/428: Rebased the sandbox implementation onto current origin/main, including accepted QA and abandoned-preparer recovery, while preserving the sandbox delta and custom-harness/difficulty fixes. At exact local head 9c308aae51522d919d8ede1bcf56fad5ec7f1c72, 164 focused tests and repository-wide Ruff lint passed; hosted exact-head CI awaits controller publication because this worker must not push and has no GitHub authentication. cost=$1.22
- 2026-09-10T17:02:32+00:00 automated review: approve — The sandbox contract is fail-closed and consistently covers planning, synchronous kickoff, local workers/reviews, setup, command checks, retries, and protected result publication. Unsupported runners, custom harnesses, bypass modes, and missing enforcement capabilities are rejected explicitly. cost=$0.51
- 2026-09-10T17:08:58+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T17:10:22+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/428
