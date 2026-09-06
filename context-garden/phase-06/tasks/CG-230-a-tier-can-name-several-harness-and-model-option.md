---
id: CG-230
title: A tier can name several harness and model options, and dispatch spreads runs across them to share
  quotas, skipping a paused or exhausted one
status: draft
product: context-garden
phase: phase-06
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/config.py
- src/garden/harness.py
- src/garden/scheduler/dispatch.py
- src/garden/scheduler/budget.py
- src/garden/scheduler/trials.py
- context-garden/phase-05/specs/cost-aware-model-routing.md
branch: garden/cg-230-a-tier-can-name-several-harness-and-model-option
pr: https://github.com/joshmarcus/context-garden/pull/222
attempts: 1
last_dispatched_at: '2026-09-06T08:47:03+00:00'
created: '2026-09-05T19:22:53+00:00'
updated: '2026-09-06T13:45:05+00:00'
---

## Goal

A difficulty tier can list more than one option, each a harness and model (`claude:claude-sonnet-5`, `codex:`, later `openrouter:z-ai/glm-5.3-flash`), and dispatch spreads a phase's runs across them by a policy: round robin by default, weights when given, and quota-aware when the garden knows a member is paused or near its limit. The point is sharing and managing quotas across accounts: today the Claude subscription's spend limit and the ChatGPT usage limit each stopped the loop for a stretch; with two members in the medium tier the loop keeps working on the other while one recovers.

## Context

Requested by the user on 2026-09-05 after the first medium-tier trial (CG-225) went to codex and both quotas had been hit that day. The tier map is one model per tier per harness (`harnesses.<h>.models`); a task's `harness:` picks the harness; CG-212 pauses a harness on a quota error and probes it back; CG-221 makes the tier map a slider stop; the routing spec in `specs/cost-aware-model-routing.md` adds difficulty routing and failure-driven escalation. This task is the pool beneath those: several members per tier and a choice per dispatch.

## Design

- `models.<tier>` accepts a list: `[{harness: claude, model: claude-sonnet-5, weight: 2}, {harness: codex, model: "", weight: 1}]`; a plain string keeps today's meaning. `dispatch.spread: round_robin | weighted | quota_aware` (default `quota_aware`, which is weighted round robin that skips paused members and, when usage-limit events were seen for a member in the last N hours, halves its weight until a probe succeeds).
- Each dispatch records the member on the run (`harness`, `model`, `pool_member`) so reviews, trials, the costs page (CG-214) and `garden metrics` can compare members; the retro reports cost per accepted task per member.
- A task's `harness:` or `model:` override pins it to one member; a trial (`garden trial`) can name a whole tier's pool as its contenders (`-c tier:medium`).
- Reviews and persona runs use pools the same way, and a review pool may name the top model of each harness regardless of the task's tier: the user's example (2026-09-05) is reviews split across `codex:gpt-6-astra` and `claude:claude-fable-5-1`, alternating to share the two quotas. Until this lands, `harnesses.<h>.review_model` pins each harness's review model and `review.harness` picks one harness for all reviews.
- The slider (CG-221) stops carry pools, so "economy" can be a cheap pair and "fast" a strong single member.

## Acceptance criteria

- [ ] A tier configured with two members dispatches alternately by default, honours weights, and skips a member the harness pause (CG-212) has marked; a test runs ten dispatches and checks the split and the skip.
- [ ] Runs, PRs and reviews record the member; `garden costs` and `garden metrics` slice by it; the retro's numbers list cost per accepted task per member.
- [ ] Task-level `harness:` and `model:` overrides still pin a run; `garden trial -c tier:medium` expands to the pool.
- [ ] `review.pool` (a list of harness:model members with weights) spreads reviews across harnesses; a test with two members sees alternating review harnesses and the skip of a paused one.
- [ ] Docs: `docs/architecture.md` describes pools and the spread policies; the example configs show a claude-and-codex medium tier.
- 2026-09-06T00:55:00+00:00 deferred by the operator: after the measurement (CG-251) merges, so each pool member can be compared

## Log

- 2026-09-06T03:38:44+00:00 approved (web)
- 2026-09-06T04:31:53+00:00 dispatched work run 20260906T042947Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~8094 tokens)
- 2026-09-06T05:20:38+00:00 pre-PR check(s) test failed at the stale base db1fe0678dce; the base branch `main` had moved, so rebased onto it and the checks pass now — no revise round
- 2026-09-06T05:20:41+00:00 opened https://github.com/joshmarcus/context-garden/pull/222 (base main): Tier and review pools now distribute work across harness/model members, skip paused harnesses, and preserve member attribution through runs, costs, and metrics. Trial contenders can expand a configured tier pool. cost=$1.69
- 2026-09-06T05:25:20+00:00 automated review requested changes: Core pool rotation works, but required near-limit quota weighting, retro/PR attribution, and reliable review-member selection are incomplete. The branch also contains unrelated CG-317 UI changes. cost=$0.46
- 2026-09-06T05:29:23+00:00 dispatched revise run 20260906T052921Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~26202 tokens)
- 2026-09-06T06:40:48+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/222: Completes quota-aware pool weighting, fixes review-pool model attribution, adds pool-member retro outcomes, and removes unrelated CG-317 trial UI work. Committed as 6a46e63 and d238276. cost=$2.22
- 2026-09-06T06:45:46+00:00 automated review requested changes: Tier dispatch, quota handling, trials, costs, metrics, retro reporting, and documentation are substantially implemented. Review-pool routing and PR attribution remain incomplete, so the PR should not merge yet. cost=$0.40
- 2026-09-06T07:05:15+00:00 dispatched revise run 20260906T070511Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~20295 tokens)
- 2026-09-06T07:40:14+00:00 pre-PR checks failed (test); revise run will fix before the PR is updated cost=$1.43
- 2026-09-06T07:41:10+00:00 dispatched revise run 20260906T074108Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, rebase round 2 (not counted), ~20854 tokens)
- 2026-09-06T08:15:49+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/222: Completed quota-aware tier and review pools, including member attribution and review routing. Restored an unrelated active-trial task-page regression accidentally removed by the prior revision. cost=$1.29
- 2026-09-06T08:16:51+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/events.py); a rebase agent will resolve it
- 2026-09-06T08:18:23+00:00 dispatched rebase run 20260906T081747Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~9469 tokens)
- 2026-09-06T08:45:49+00:00 pre-PR checks failed (checks); revise run will fix before the PR is updated cost=$0.03
- 2026-09-06T08:47:03+00:00 dispatched revise run 20260906T084648Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~20468 tokens)
- 2026-09-06T09:10:31+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/222: Committed 18a9dd2 to preserve structured results when a detached check job crashes, replacing the opaque no-results error with the exception detail. cost=$0.65
- 2026-09-06T09:15:29+00:00 automated review requested changes: Pool rotation and attribution are substantially implemented, but valid empty-model members and top-level string mappings route to the wrong model. The PR also includes an unrelated check-runner fix. cost=$0.55
- 2026-09-06T09:16:35+00:00 stuck: 3 revision rounds already used; resume with one more round (`garden retry CG-230`) or send it back (`garden triage CG-230 --changes "..."`)
- 2026-09-06T13:18:42+00:00 triage: changes requested by hand: Owner-authorized additional revision: preserve intentional empty model members such as codex:, honor backward-compatible
- 2026-09-06T13:18:49+00:00 re-enabled by hand; revise run will follow
- 2026-09-06T13:45:04+00:00 Owner-directed feature deferral until phase-05 stabilization is demonstrated. Preserve existing branch and PR; no further implementation or merge before the gate passes.
- 2026-09-06T13:45:05+00:00 moved from context-garden/phase-05 to context-garden/phase-06
