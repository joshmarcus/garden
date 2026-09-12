---
id: CG-380
title: Attribute controller, scheduler, and worker performance under load
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 1
difficulty: hard
reading:
- src/garden/scheduler/resources.py
- src/garden/store.py
- src/garden/web/common.py
- docs/validation/cg367/serve_profiled.py
- docs/validation/cg380/README.md
- tests/scheduler/test_resources.py
branch: garden/cg-380-attribute-controller-scheduler-and-worker-perfor
pr: https://github.com/joshmarcus/context-garden/pull/290
discovered_from: CG-367
attempts: 1
last_dispatched_at: '2026-09-08T17:04:20+00:00'
created: '2026-09-07T12:03:08+00:00'
updated: '2026-09-08T17:31:59+00:00'
---

## Goal

Explain how much local resource use and page latency comes from the garden controller versus workers, then identify the next measured optimization. Preserve owner-approved four-slot operation and the existing caps.

## Context

Owner requested continued performance investigation on 2026-09-07 because worker versus application cost remains unclear. CG-367 is DONE and its Inbox history-read reduction is deployed in 899b2c0; extend its evidence rather than repeating or reopening its implementation. CG-365 resource isolation is also deployed. This task measures attribution, not another concurrency/configuration feature.

Operator evidence is preserved in context-garden/docs/incidents/performance-attribution-2026-09-07.json in the garden repository. Read-only summary for product-only workers: a 12-second no-operator-probe interval consumed 2.80 server CPU-seconds of 4.08 total service CPU-seconds, with a scheduler state save. Three serial page probes then consumed 1.77 server CPU-seconds of 2.08 total over 1.78 wall seconds; Now1/Inbox/Config returned 200 in .760/.678/.345 seconds. Service memory was 1341MiB, memory high/max/OOM zero, no memory pressure or CPU throttling delta. No-operator-probes does not mean idle: other clients may exist. These short observational intervals cannot establish tick cost or a general proportional split.

## Acceptance criteria

- [ ] On the current product build, reuse CG-367 fixtures/profiling and create a bounded disposable comparison with representative retained history: no workers, model-session/CI-wait activity, setup, and one focused validation workload. Compare one and four admitted slots where applicable. Do not launch extra model agents; replay or use bounded subprocess fixtures and label their representativeness. No production stress, pause, configuration changes, or full local suite.
- [ ] Attribute web request handling and scheduler phases separately: CPU execution, request/lock waiting, filesystem/history reads and parsing, process/resource inspection, and rendering as applicable. Measure worker setup/validation separately from controller work, including short-lived descendants. Record process identity and cgroup membership so parent CPU is not mistaken for total workload CPU. Do not equate summed RSS with actual aggregate memory.
- [ ] Retain exact build, dataset sizes, commands, caps, timestamps, sample counts, CPU seconds, cgroup throttling and CPU/I/O/memory pressure deltas, memory anon/file/shmem and temp headroom. Report empirical page p50/p95/max for repeated samples, cold/warm behavior, and background tick timing. Quantify instrumentation overhead. Label unsupported or unmeasured components honestly.
- [ ] Produce an evidence-backed attribution report separating confirmed bottlenecks from hypotheses and recommending the highest-value next action. If a narrow correction is demonstrated, implement it with a matched before/after comparison; otherwise file a precise follow-up instead of speculative caching or broad telemetry. Preserve data freshness and control correctness. Four-second page tolerance is the owner's operational target, not permission to fabricate passing evidence.
- [ ] Use focused serial bounded local validation and exact-final-head GitHub CI for code changes. Self-review and fix findings before completion; report ordinary acceptance evidence. Avoid unrelated application-wide walkthrough demands and do not claim incident closure or four-hour stabilization from this experiment.

## Boundaries

This is a new independent investigation. Do not regroup, rewrite, or widen in-flight task briefs. Reuse deployed work and its artifacts. Operator owns live monitoring and any eventual production changes.

## Additional operator observation: cache-heavy admission stop

At 2026-09-07T12:29Z, shared limit was five but only CG253 had a recorded running run. Scheduler resource_pressure reported available memory550MiB below1536MiB. Host MemAvailable was5621MiB, service memory.current about2501MiB, earlier breakdown anon251MiB/file2198MiB/shmem58MiB; memory high/max/OOM all zero and memory PSI zero. Now1/Inbox .715/.602s. The current sensor takes the minimum of host and cgroup headroom, so this is not host exhaustion. Inspect the cgroup admission calculation and reclaimable file-cache treatment as a concrete attribution hypothesis. Preserve hard memory caps and pressure safeguards; do not bypass the admission stop or assume all file cache is reclaimable. Report whether conservative soft-limit headroom is intentionally preventing progress and propose a measured safe policy if warranted.

## Log

- 2026-09-07T12:32:43+00:00 dispatched work run 20260907T123241Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~10098 tokens)
- 2026-09-07T13:02:16+00:00 preserved uncommitted worktree changes from run 20260907T123241Z-work outside the PR: `git stash apply a269ad16d056130574a6d793ca55d1f5b6cc6b37` in /home/joshua/work/worktrees/CG-380 (garden:CG-380:20260907T123241Z-work:reap)
- 2026-09-07T13:38:22+00:00 opened https://github.com/joshmarcus/context-garden/pull/290 (base main): Added a reproducible bounded controller/scheduler/worker attribution study with retained-history page profiles, subprocess workload accounting, cgroup evidence, and an admission-cache analysis. The evidence identifies task/product scanning as the next controller optimization and supports a separate reclaimability experiment before changing memory admission policy. cost=$2.43
- 2026-09-07T15:29:26+00:00 automated review requested changes: The bounded controller/worker experiment is reproducible and well documented, but it does not attribute individual scheduler phases and does not include the required larger-history served comparison. These gaps leave the central attribution and scalability claims incomplete. cost=$0.73
- 2026-09-07T16:37:55+00:00 Temporary operator incident admission hold to reserve next drained slot for P0 CG385 recovery; preserve all work. Restore original runner from docs/incidents/cg385-recovery-admission-holds.json after CG385 starts.
- 2026-09-07T16:39:06+00:00 stuck: manual task has a revise round waiting; take it with `garden take`; take it (`garden take CG-380`) or send it back (`garden triage CG-380 --changes "..."`)
- 2026-09-07T17:01:39+00:00 Operator restored original runner after CG385 recovery repair acquired actual execution slot. Shared cap remains1.
- 2026-09-07T18:59:47+00:00 re-enabled by hand; revise run will follow
- 2026-09-07T18:59:47+00:00 Delegated operator Inbox audit: cleared stale manual-hold stop after verified normal runner restoration; existing implementation, PR and pending review feedback retained. No owner decision required.
- 2026-09-07T22:49:04+00:00 dispatched revise run 20260907T224859Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~12785 tokens)
- 2026-09-07T23:43:21+00:00 preserved uncommitted worktree changes from run 20260907T224859Z-revise outside the PR: `git stash apply a25b44ad6b03af9ae5bbf6c29c332212f7efeeb1` in /home/joshua/work/worktrees/CG-380 (garden:CG-380:20260907T224859Z-revise:reap)
- 2026-09-07T23:49:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/290: Extended the disposable attribution study with native scheduler-phase CPU/wall timing, separate lock and controller-overhead accounting, 100-versus-1,000-task served comparisons across three cache-expiry intervals, and structured running-app evidence. The measurements confirm retained task/product scanning as the next controller optimization while preserving the four-slot policy and all resource safeguards. cost=$3.81
- 2026-09-08T02:24:51+00:00 automated review requested changes: The bounded attribution study reproduces successfully and supports task/product scanning as the dominant measured controller cost. Request changes because the report pools cold and warm requests instead of reporting the explicitly required cold/warm behavior. cost=$0.89
- 2026-09-08T02:25:47+00:00 dispatched revise run 20260908T022545Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~13062 tokens)
- 2026-09-08T02:58:33+00:00 preserved uncommitted worktree changes from run 20260908T022545Z-revise outside the PR: `git stash apply 4f17c9fedf489aa607a5339ee366133d710bad70` in /home/joshua/work/worktrees/CG-380 (garden:CG-380:20260908T022545Z-revise:reap)
- 2026-09-08T03:07:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/290: Added verified cold-versus-warm latency attribution, replayed the bounded served-app study against the revised build, and strengthened structured scalability and resource-accounting evidence. Exact-final-head GitHub CI passed. cost=$2.17
- 2026-09-08T03:12:05+00:00 Owner shutdown: 20260908T030858Z-review interrupted; preserve worktree and saved artifacts. No resume without owner instruction.
- 2026-09-08T12:28:50+00:00 Owner-requested Inbox audit: completed verified source/test reading list; preserved implementation, PR and feedback.
- 2026-09-08T12:35:50+00:00 triage: changes requested by hand: Operator audit: finish the explicit cold/warm reporting from already collected ordered samples and check the verifier. P
- 2026-09-08T12:35:50+00:00 Delegated operator Inbox review: preserved PR/worktree and queued one concrete continuation within current 4 AWS + 1 local limits.
- 2026-09-08T16:47:54+00:00 dispatched revise run 20260908T164751Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~25637 tokens)
- 2026-09-08T16:51:34+00:00 preserved uncommitted worktree changes from run 20260908T164751Z-revise outside the PR: `git stash apply bc5e02108a3fd7cea72436a70812f9c2f8363b87` in /home/joshua/work/worktrees/CG-380 (garden:CG-380:20260908T164751Z-revise:reap)
- 2026-09-08T16:53:01+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/290: Clarified the preserved cold/warm measurements and strengthened the verifier to validate raw sample periods, order, and block sizes. No stress experiment or product behavior change was introduced. cost=$0.56
- 2026-09-08T17:02:25+00:00 automated review requested changes: The attribution study is reproducible, internally consistent, and meets all five criteria. Exact-head bounded interaction, focused verification, lint, and GitHub CI passed; no blocking correctness or scope issues were found. cost=$1.03
- 2026-09-08T17:04:20+00:00 dispatched revise run 20260908T170417Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~25929 tokens)
- 2026-09-08T17:12:05+00:00 preserved uncommitted worktree changes from run 20260908T170417Z-revise outside the PR: `git stash apply a98f6de18b77f0a7cc91ed566eed87136d1772a6` in /home/joshua/work/worktrees/CG-380 (garden:CG-380:20260908T170417Z-revise:reap)
- 2026-09-08T17:31:32+00:00 revision failed: worker finished with no commits
- 2026-09-08T17:31:59+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/290
