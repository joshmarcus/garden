---
id: CG-410
title: Show eligible manual work in Inbox with a safe take action
status: done
product: context-garden
phase: phase-07
depends_on: []
priority: 0
difficulty: medium
reading:
- context-garden/phase-07/specs/enterprise-remote-environments.md
branch: garden/cg-410-show-eligible-manual-work-in-inbox-with-a-safe-t
pr: https://github.com/joshmarcus/context-garden/pull/346
runner: remote
attempts: 1
last_dispatched_at: '2026-09-09T01:40:24+00:00'
created: '2026-09-07T20:05:52+00:00'
updated: '2026-09-09T16:46:26+00:00'
---

## Goal

Show eligible manual work in Inbox with a safe take action. Recheck current implementation before choosing the smallest compatible change.

## Acceptance criteria

- [ ] Show ready manual-runner tasks as actionable work awaiting a person, with task packet, assignment and clear take/resume action.
- [ ] Distinguish dependency-blocked, frozen, paused, already claimed and active tasks; never offer an unsafe take or label waiting work as running.
- [ ] Use authoritative task state for counts and claim transitions; concurrent take requests cannot start duplicate runs. Integrate CG-381 ownership semantics.
- [ ] Exercise Inbox to take to finish through the actual UI, including full capacity and stale-card recovery.

## Provenance and scope

Owner-provided additional gap F2, 2026-09-07. Generic requirements only. This task remains a phase-07 draft and does not authorize new access, deployment or external notifications. Refer to the shared spec, not the private environment survey.

## Log

- 2026-09-07T20:06:51+00:00 approved (owner-approve-phase07)
- 2026-09-08T12:39:03+00:00 Operator continuation: route this next eligible Phase07 P0 task to the existing four-host AWS pool as capacity frees; keep current 4 AWS + 1 local total and 20:00UTC deadline.
- 2026-09-08T12:40:15+00:00 dispatched work run 20260908T124015Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~8479 tokens)
- 2026-09-08T12:54:11+00:00 worker blocked: Inbox now shows claimable manual work, safe waiting states, and a guarded take action with immutable assigned packets. Focused UI/scheduler tests and lint pass on fa7c57c, which is pushed to the assigned branch; exact-head CI could not be retrieved because GitHub metadata polling repeatedly returned HTTP 403. cost=$1.46
- 2026-09-08T14:08:35+00:00 reset to ready by hand


## Operator continuation, 2026-09-08

Preserve existing implementation fa7c57c915eaa55bff7167677d1a9c32bc17cad0. Its exact full GitHub CI passed (run34228252750), verified centrally after the public rate-limit stop. Complete the remaining take -> finish interaction and verify unsafe/full-capacity/stale-card recovery using the actual served application, with equivalent evidence accepted. The retained implementation is already useful; continue it rather than rebuild. The remote supervisor and host test/browser tools are repaired in rc5. Follow the current AWS ordinary-suite instruction instead of polling scripts/check_ci.py.
- 2026-09-08T14:57:10+00:00 dispatched work run 20260908T145710Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9492 tokens)
- 2026-09-08T15:29:44+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$1.95
- 2026-09-08T15:32:12+00:00 dispatched revise run 20260908T153212Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9720 tokens)
- 2026-09-08T15:57:29+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$1.68
- 2026-09-08T15:57:49+00:00 dispatched revise run 20260908T155749Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9798 tokens)
- 2026-09-08T16:33:30+00:00 pre-PR checks failed (review pre-flight); no PR opened yet; revise run will fix cost=$2.32
- 2026-09-08T16:38:39+00:00 dispatched revise run 20260908T163839Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9894 tokens)
- 2026-09-08T17:10:44+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$0.92
- 2026-09-08T17:20:47+00:00 dispatched revise run 20260908T172047Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~9947 tokens)
- 2026-09-08T17:47:16+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$0.88
- 2026-09-08T17:50:15+00:00 dispatched revise run 20260908T175015Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~10027 tokens)
- 2026-09-08T18:09:59+00:00 pre-PR checks failed (ui, UI captures); no PR opened yet; revise run will fix cost=$0.52
- 2026-09-08T19:09:20+00:00 dispatched revise run 20260908T190917Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~11376 tokens)
- 2026-09-08T19:16:22+00:00 pre-PR checks failed (UI captures, PR description) and 6 revision rounds already used; needs a human cost=$0.59
- 2026-09-08T21:43:51+00:00 dispatched revise run 20260908T214351Z-revise via manual [human] (fresh session, base main, ~11450 tokens)
- 2026-09-08T21:58:56+00:00 external PR attached at garden/cg-410-show-eligible-manual-work-in-inbox-with-a-safe-t; existing CI is SUCCESS
- 2026-09-08T22:08:03+00:00 automated review requested changes: The core Inbox journey works, but two unsafe claim paths remain: blocked task pages still offer Take, and stale READY state with an active manual run can create a duplicate claim. cost=$0.54
- 2026-09-08T22:08:24+00:00 stuck: 6 revision rounds already used; resume with one more round (`garden retry CG-410`) or send it back (`garden triage CG-410 --changes "..."`)
- 2026-09-08T22:22:47+00:00 triage: changes requested by hand: Operator investigated the cap stop and authorizes ONE precise revision. Preserve the existing real captures and complete
- 2026-09-08T22:24:03+00:00 dispatched revise run 20260908T222403Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15036 tokens)
- 2026-09-08T22:44:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/346: Manual task pages now suppress unsafe Take/Resume controls, and stale READY state cannot create a second manual claim. A served disposable Inbox journey records blocked/frozen pages, full capacity, stale conflict, completion failure, recovery, and empty state. cost=$0.97
- 2026-09-08T22:49:38+00:00 automated review requested changes: Manual work is presented accurately and claimed through an authoritative, serialized action that rejects stale or unsafe requests. Focused tests, lint, exact-head served interaction, and responsive captures pass inspection. cost=$0.46
- 2026-09-08T22:50:07+00:00 stuck: 6 revision rounds already used; resume with one more round (`garden retry CG-410`) or send it back (`garden triage CG-410 --changes "..."`)


## Operator evidence interpretation, 2026-09-08

Operator disposition of review224636 at ab067c85: all4 substantive criteria passed, including both actual claim-safety fixes. The served stale Take returned actual HTTP409 and proves the required failure path. Malformed completion returned actual303 to display an application error while preserving the session; keep that true303 evidence, but do not mislabel the redirect as an unsuccessful HTTP response. Use409 for HTTP-failure coverage and retain malformed completion as a separate application-rejection observation. The recovery303 and final empty200 were observed. Do not change working implementation or fabricate a status code; reuse the already-inspected exact-head journey/captures. Full original review/raw events remain preserved.
- 2026-09-08T23:12:26+00:00 triage: marked ready for review (Source criteria pass; preserve303 application rejection and409 HTTP refusal. One fresh evidence revi)
- 2026-09-08T23:35:39+00:00 automated review requested changes: Manual work is presented accurately and claimed through an authoritative serialized action that rejects stale or unsafe requests. Focused tests, lint, served interaction evidence, and responsive captures support all four criteria. cost=$0.35
- 2026-09-08T23:35:57+00:00 stuck: 6 revision rounds already used; resume with one more round (`garden retry CG-410`) or send it back (`garden triage CG-410 --changes "..."`)

## Operator evidence disposition 2026-09-08T23:50:16.661542+00:00

Operator assessment: all current-head acceptance criteria pass. Preserve the complete current review and separately attributed affected-flow evidence on completed author 20260908T222403Z-revise. No new implementation revision is requested. Hold one uncounted review with explicit author context until the deployed evidence-routing repair is ready; generic unreadable replay metadata is not an unverified product outcome. CG410 original 303 malformed-form application rejection remains preserved; stale Take409 supplies the HTTP failure, and the prior independently observed URLs truthfully retain an explicit ephemeral-port placeholder.
- 2026-09-08T23:50:17+00:00 triage: marked ready for review (Operator assessment: all current-head acceptance criteria pass. Preserve the complete current review)
- 2026-09-09T00:10:23+00:00 automated review requested changes: Core manual claim, finish, stale-card recovery, and responsive UI behavior are verified. Inbox still offers Resume for revision-capped work, violating the safe-action criterion. cost=$0.56
- 2026-09-09T00:10:54+00:00 stuck: 6 revision rounds already used; resume with one more round (`garden retry CG-410`) or send it back (`garden triage CG-410 --changes "..."`)
- 2026-09-09T00:16:00+00:00 triage: changes requested by hand: Operator assessment after deployed RC8: review000620 reused the preserved actual author interaction and no longer blocke
- 2026-09-09T00:17:00+00:00 dispatched revise run 20260909T001700Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~16938 tokens)
- 2026-09-09T00:22:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/346: Capped manual revision tasks now render as paused Inbox work with no unsafe Resume action. A focused regression and disposable served interaction verify the cap guard while preserving stale-claim recovery coverage. cost=$0.52
- 2026-09-09T00:30:34+00:00 automated review: approve — Manual Inbox work is presented accurately and claimed through an authoritative serialized action that rejects stale, capped, or otherwise unsafe requests. Focused tests, lint, served interaction evidence, and responsive captures support all four criteria. cost=$0.33
- 2026-09-09T00:32:11+00:00 CI failure, but 6 revision rounds already used; needs a human
- 2026-09-09T01:03:11+00:00 dispatched revise run 20260909T010311Z-revise via manual [human] (fresh session, base main, ~14140 tokens)
- 2026-09-09T01:39:06+00:00 external PR attached at garden/cg-410-show-eligible-manual-work-in-inbox-with-a-safe-t; existing CI is PENDING
- 2026-09-09T01:40:19+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/human.py); a rebase agent will resolve it
- 2026-09-09T01:40:24+00:00 dispatched rebase run 20260909T014023Z-rebase via remote [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~3111 tokens)
- 2026-09-09T01:44:40+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/346: Rebased CG-410 onto origin/main and preserved both manual-claim safety and mainline actor/review behavior. cost=$0.01
- 2026-09-09T01:50:22+00:00 automated review: approve — Manual Inbox work is accurately presented and claimed through a serialized, authoritative action that rejects unsafe or stale requests. Focused checks, preserved served interaction evidence, and responsive Inbox/task captures support all four criteria. cost=$0.44
- 2026-09-09T01:50:52+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T01:52:06+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T02:00:27+00:00 automated review requested changes: Manual Inbox work is accurately presented and claimed through a serialized authoritative action that rejects stale, capped, blocked, frozen, and otherwise unsafe requests. Focused checks, preserved served interaction evidence, and responsive Inbox/task captures support all four criteria. cost=$0.47
- 2026-09-09T02:00:42+00:00 stuck: 6 revision rounds already used; resume with one more round (`garden retry CG-410`) or send it back (`garden triage CG-410 --changes "..."`)
- 2026-09-09T02:05:10+00:00 Operator held exact current source after native reviewer APPROVE was mechanically rewritten by RC8 for a malformed-form 303 redirect. Full state/raw review/stored result/cap feedback preserved; no new implementation. One actual review will re-evaluate after verified RC9.
- 2026-09-09T02:14:24+00:00 Operator released only the historical RC8 HTTP-status policy stop after exact RC9 source verification; one real same-head Garden review queued, raw/stored prior verdicts and counts preserved.
- 2026-09-09T02:32:10+00:00 automated review: approve — Manual Inbox work is accurately presented and guarded against blocked, frozen, capped, active, and stale claims. The implementation satisfies the requested take-to-finish workflow. cost=$0.39
- 2026-09-09T02:46:35+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T02:56:11+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T02:57:53+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/346
- 2026-09-09T03:02:08+00:00 automated review could not start: CG-410 is done: #346 was merged at 02:57:53
- 2026-09-09T16:46:26+00:00 automatic review recovery retired because task is done
