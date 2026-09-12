---
id: CG-443
title: Keep out-of-scope review limitations from rejecting satisfied acceptance criteria
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-436
priority: 0
order: -102
difficulty: hard
reading:
- src/garden/review.py
- src/garden/scheduler/review.py
- src/garden/scheduler/checkruns.py
- src/garden/criteria.py
- tests/test_review.py
branch: garden/cg-443-keep-out-of-scope-review-limitations-from-reject
pr: https://github.com/joshmarcus/context-garden/pull/336
runner: remote
attempts: 1
last_dispatched_at: '2026-09-08T22:53:00+00:00'
created: '2026-09-08T17:14:13+00:00'
updated: '2026-09-08T23:41:51+00:00'
dependency_after:
  CG-436: merge
---

## Goal

Let reviewers report honest limitations without turning unrelated uncertainty into a source rejection. Tie each blocking unverified outcome to a frozen acceptance criterion or an explicitly justified affected-flow requirement. Preserve failures and contradictory provenance as blocking.

## Reproduced case

CG430 review 20260908T161605Z-review at c6e8c93a621b0b0e1a55d3c69a5007a39d52eade assessed all five criteria met, with 52 runner tests and actual supervised HTTP/process evidence. Its sole mechanical blocker came from interaction.unverified containing: The September 8 WSL launch failures and controller/web responsiveness issue were not reproduced, so their cause and resolution remain unverified. The task explicitly says to separate the confirmed adopted-zombie lifecycle defect from the broader incident; reproducing/solving the whole outage is not a required outcome.

Both installed rc5 and CG436's completed ccdcffd candidate still reject any nonempty unverified list in interaction_evidence_gaps. CG436 owns replay selection and evidence handoff; this narrowly follows that work and must reuse its interfaces.

## Acceptance criteria

- [ ] Separate required unverified outcomes from out-of-scope limitations/follow-up observations in the review contract and instructions. Preserve honest limitations in review output and task history.
- [ ] A blocking verification gap names the frozen criterion or justified affected-flow requirement and explains the failed/missing outcome. An unrelated limitation alone cannot force request_changes or another implementation revision.
- [ ] Preserve actual failed states, unmet criteria, missing affected-flow outcomes and contradictory source/artifact provenance as blocking, including when a reviewer wrongly labels one a limitation.
- [ ] Handle ambiguous legacy unverified strings through a bounded clarification/recovery path with the existing CG436 continuation, rather than silently approving an unknown gap or repeatedly spending author revisions. Keep prior reports intact and clarification idempotent across ticks/restart.
- [ ] Reproduce the exact CG430 report shape: all required outcomes pass plus an explicitly out-of-scope incident limitation. Verify approval eligibility and visible limitation; pair with a real unmet acceptance outcome that still rejects and a mislabeled required failure that still blocks.
- [ ] Verify parsing, briefing, mechanical verdict and recovery behavior with focused ordinary tests and a disposable scheduler/review-flow fixture. Do not deploy unreviewed code or introduce stress as default.

## Scope and provenance

Owner asked on September8 how to prevent this rejection in future and authorized preventive repair tickets. This is a separate follow-up because CG436 implementation is already complete/in review; avoid retroactively broadening its frozen criteria or duplicating its replay work. Operator records: /home/joshua/work/operator-test-tmp/operator-20260908T1712/before.json and actions.json. Broader WSL incident remains open and unresolved.

## Log

- 2026-09-08T17:15:15+00:00 approved (owner-preventive-review-scope-repair)
- 2026-09-08T17:50:15+00:00 dispatched work run 20260908T175015Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~12449 tokens)


## Owner deployment checkpoint 2026-09-08T18:43:07.522204+00:00

Owner-requested deployment interruption after shared test hangs; exact source and streamed outputs checkpointed at /home/joshua/work/operator-test-tmp/rc6-deploy-20260908T1818/checkpoint-CG-443
Source f156ae32f237868f091e165f0dbb1f69170e3e5d is preserved in source.bundle; this interruption is not a code-failure verdict. Resume this implementation with focused tests and bounded validation; do not repeat unchanged full-suite failures.
- 2026-09-08T18:43:07+00:00 Operator-owned deployment recovery; preserved implementation, no author failure verdict.
- 2026-09-08T18:44:00+00:00 stuck: no feedback recorded to revise against; resume with one more round (`garden retry CG-443`) or send it back (`garden triage CG-443 --changes "..."`)
- 2026-09-08T19:12:57+00:00 dispatched revise run 20260908T191256Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14256 tokens)
- 2026-09-08T19:21:08+00:00 opened https://github.com/joshmarcus/context-garden/pull/336 (base main): Review limitations are now preserved without blocking satisfied acceptance criteria, while required gaps and contradictory evidence remain blocking. Legacy unverified strings receive one restart-safe reviewer clarification instead of triggering author revisions. cost=$0.56
- 2026-09-08T20:16:49+00:00 automated review produced no verdict (idle 21 min (no output or file change))
- 2026-09-08T21:43:52+00:00 dispatched revise run 20260908T214352Z-revise via manual [human] (fresh session, base main, ~14168 tokens)
- 2026-09-08T21:51:43+00:00 external PR attached at garden/cg-443-keep-out-of-scope-review-limitations-from-reject; existing CI is PENDING
- 2026-09-08T22:03:38+00:00 review validation scope expansion: Current-head Inbox reviewer-clarification state — Commit c1b4d883 adds visible Inbox text and actions after the validation-plan head, creating a distinct affected-flow and visual risk not covered by the 7bf3b128 replay.
- 2026-09-08T22:03:40+00:00 automated review requested changes: The implementation and focused checks pass, but required running-application evidence is stale: the reviewed head is c1b4d883 while the replay targets 7bf3b128. The current-head Inbox clarification and recovery journey is therefore unverified. cost=$0.44
- 2026-09-08T22:04:01+00:00 dispatched revise run 20260908T220401Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~14836 tokens)
- 2026-09-08T22:20:51+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/336: Added durable served-app evidence for the reviewer-clarification Inbox state at source c1b4d883, including restart persistence, the operator recovery action, and exact-width light/dark captures. The focused suite and lint pass on final commit 38b2375. cost=$2.53
- 2026-09-08T22:37:07+00:00 automated review requested changes: All frozen criteria are satisfied: limitations remain visible without blocking, required failures remain blocking, and ambiguous legacy entries use a bounded restart-safe reviewer continuation. Focused tests and lint pass; the exact-head replay artifact was inaccessible in this reviewer environment, but equivalent served evidence covers the unchanged application tree and the final commit adds evidence files only. cost=$0.43
- 2026-09-08T22:37:28+00:00 dispatched revise run 20260908T223728Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15226 tokens)
- 2026-09-08T22:48:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/336: Completed the reviewer-clarification evidence with a reproducible disposable served-app replay containing a real HTTP 404 failure followed by successful recovery. Updated the permanent PR description to identify final head a891def and distinguish the unchanged application-source replay. cost=$1.44
- 2026-09-08T22:52:37+00:00 automated review requested changes: All six frozen criteria are satisfied. Focused tests and lint pass; required gaps still block while out-of-scope limitations remain visible and ambiguous legacy entries use a bounded reviewer-owned continuation. cost=$0.41
- 2026-09-08T22:53:00+00:00 dispatched revise run 20260908T225300Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~15481 tokens)
- 2026-09-08T22:59:10+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/336: Refreshed the durable served-app replay against reviewed source head a891defc and committed the evidence receipt at b948c1f. Required review gaps remain blocking, limitations remain visible, and reviewer clarification recovery is verified without queuing an author revision. cost=$0.59
- 2026-09-08T23:09:37+00:00 description rewritten by the reviewer cost=$0.41
- 2026-09-08T23:28:11+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-08T23:28:47+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-08T23:39:52+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-08T23:41:51+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/336
