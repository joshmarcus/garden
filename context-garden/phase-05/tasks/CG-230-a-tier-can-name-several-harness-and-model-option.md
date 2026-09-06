---
id: CG-230
title: A tier can name several harness and model options, and dispatch spreads runs across them to share
  quotas, skipping a paused or exhausted one
status: ready
product: context-garden
phase: phase-05
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
created: '2026-09-05T19:22:53+00:00'
updated: '2026-09-06T03:38:44+00:00'
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
