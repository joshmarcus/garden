---
id: CG-447
title: Unify scp-form repository classification across config and worker claims
status: done
product: context-garden
phase: phase-07
depends_on:
- CG-395
priority: 0
difficulty: medium
reading:
- src/garden/config.py
- src/garden/gitops.py
- src/garden/web/pages/api.py
branch: garden/cg-447-unify-scp-form-repository-classification-across
pr: https://github.com/joshmarcus/context-garden/pull/345
runner: remote
discovered_from: Owner report 2026-09-08; CG395/PR307 and rc6 source8f050073 config.py:333
attempts: 1
last_dispatched_at: '2026-09-08T22:56:12+00:00'
created: '2026-09-08T18:15:46+00:00'
updated: '2026-09-09T00:27:37+00:00'
---

## Goal

Recognize Git scp-form repository references consistently at configuration and claim boundaries using the shared resolver, so they remain clone sources rather than being resolved as local paths.

## Owner report and existing work

Owner reported on September8 that published rc6 src/garden/config.py:333 still uses startswith("git@"). Example: acct-1234@forge-one.test:team/repo.git. Git scp syntax is [user@]host:path, with an arbitrary optional SSH transport username.

CG395/PR307 is already P0 and its exact669f519a head repairs arbitrary-username config classification and adds a regression; it also updates claim routing. Preserve that work, do not duplicate its implementation or launch another author on its branch. This follow-up owns the residual shared-classifier audit (especially username-omitted host:path) and proves the configuration-to-claim path after CG395 merges. CG432 separately owns onboarding metadata discovery.

## Acceptance criteria

- [ ] Reuse one audited remote-reference classifier at product/task configuration and worker-claim boundaries; acct-1234@forge-one.test:team/repo.git and forge-one.test:team/repo.git remain the exact remote string and are never prefixed with the garden directory. Preserve standard git@, ssh:// and https:// forms.
- [ ] Preserve real relative/absolute filesystem paths, including Windows drive and UNC spellings where supported. Reject malformed or password-bearing references according to the existing credential/host policy; arbitrary SSH usernames are transport identities, not bearer secrets.
- [ ] Add deterministic config-to-claim and parser regressions for both optional-username forms, local paths and refusals. Demonstrate the failure against the affected source and passing behavior on the proposed source, using synthetic hosts and no private credentials.
- [ ] Verify corrected behavior on the proposed commit with the bounded config-to-claim evidence above. Record rc6 as affected. Merge and first immutable release identification are subsequent operator release obligations, not prerequisites for author completion or review approval. Carry remaining source gaps as concrete follow-ups without replaying completed CG395 implementation.

## Verification scope

Actual served disposable claim API is appropriate for this boundary; synthetic hosts and authorization are sufficient. No live enterprise access or unrelated full application journey is required. Preserve source/command/result evidence and strict host separation.

## Log

- 2026-09-08T18:15:46+00:00 approved (owner-requested-P0-scp-classifier)
- 2026-09-08T19:15:13+00:00 dispatched work run 20260908T191513Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15002 tokens)
- 2026-09-08T19:25:23+00:00 worker asks: Which immutable release tag should be cut or designated after this branch merges, so the first release containing CG-395/CG-447 can be explicitly recorded? cost=$0.76
- 2026-09-08T20:39:56+00:00 Operator answered release question and removed circular pre-merge criterion; source/resume remains preserved while AWS capacity is restored.
- 2026-09-08T21:34:41+00:00 Delegated owner answer is complete; original source513001a restored for bounded completion after capacity restoration.
- 2026-09-08T21:55:13+00:00 dispatched revise run 20260908T215513Z-revise via manual [human] (fresh session, base main, ~15618 tokens)
- 2026-09-08T21:55:19+00:00 external PR attached at garden/cg-447-unify-scp-form-repository-classification-across; existing CI is PENDING
- 2026-09-08T22:32:16+00:00 automated review requested changes: The classifier change is correct under focused testing, including a reproduced rc6/main failure and passing proposed-head behavior. The required served claim interaction cannot be verified because its supplied manifest is absent. cost=$0.87
- 2026-09-08T22:32:41+00:00 dispatched revise run 20260908T223241Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~16202 tokens)
- 2026-09-08T22:44:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/345: Added a real TCP HTTP regression and committed disposable interaction transcripts for both supported SCP forms. The claim flow now has durable affected, empty, failure, and recovery evidence; rc6’s username-less classification gap remains recorded as the affected source. cost=$0.94
- 2026-09-08T22:55:44+00:00 automated review requested changes: The shared classifier correctly preserves both SCP forms through configuration and worker claims while retaining path and credential-safety behavior. Exact-head served interaction, 16 focused test cases, Ruff, and diff checks passed. cost=$0.36
- 2026-09-08T22:56:12+00:00 dispatched revise run 20260908T225611Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~16243 tokens)
- 2026-09-08T23:28:15+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/345: Refreshes durable disposable HTTP claim evidence for both supported SCP forms, including exact source identity and affected, empty, failure, and recovery state summaries. The shared classifier and claim behavior remain covered by focused current-head regressions. cost=$0.53
- 2026-09-08T23:44:28+00:00 stalled: review finding repeated after a revise round: running-app evidence incomplete: interaction requirements remain unverified; run `garden triage CG-447 --changes "<feedback>" to unblock`

## Operator evidence disposition 2026-09-08T23:50:16.661542+00:00

Operator assessment: all four criteria and actual exact1502a13 API outcomes pass. Preserve the full raw review, including its unreadable generic manifest limitation. The independently recorded eight TCP events supply affected/empty/failure/recovery evidence. Hold one uncounted review with explicit author context until the deployed evidence-routing repair; do not replay completed classifier implementation.
- 2026-09-08T23:50:17+00:00 triage: marked ready for review (Operator assessment: all four criteria and actual exact1502a13 API outcomes pass. Preserve the full )
- 2026-09-09T00:10:25+00:00 automated review: approve — The shared classifier correctly preserves both SCP forms through configuration and worker claims while retaining filesystem-path and credential-safety behavior. Exact-head served interaction, 15 focused tests, Ruff, and diff checks passed. cost=$0.38
- 2026-09-09T00:15:24+00:00 rebasing before merge; rebased onto main mechanically and force-pushed
- 2026-09-09T00:16:33+00:00 rebased; patch id unchanged; verdict kept
- 2026-09-09T00:25:34+00:00 automated review: approve — The shared classifier preserves both SCP forms through configuration and worker claims while retaining filesystem-path and credential-safety behavior. Exact-head served interaction, focused tests, Ruff, conflict checks, and an rc6 failure reproduction passed. cost=$0.46
- 2026-09-09T00:25:58+00:00 rebasing before merge; reviewed remote head already contains main; not rebased or pushed
- 2026-09-09T00:27:37+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/345
