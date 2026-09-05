---
id: CG-221
title: 'A slider from efficient to fast: named operating profiles that set workers, the tier map, the
  review tier and the observation feed together, switched live from the rail'
status: running
product: context-garden
phase: phase-04
depends_on:
- CG-219
- CG-192
priority: 2
difficulty: medium
reading:
- src/garden/config.py
- src/garden/scheduler/budget.py
- src/garden/web/actions/control.py
- src/garden/web/templates/base.html
- src/garden/web/pages/config.py
- garden.yaml
branch: garden/cg-221-a-slider-from-efficient-to-fast-named-operating
pr: https://github.com/joshmarcus/context-garden/pull/175
attempts: 1
last_dispatched_at: '2026-09-05T18:05:54+00:00'
created: '2026-09-05T16:51:03+00:00'
updated: '2026-09-05T18:05:54+00:00'
---

## Goal

One control answers "how hard should the garden run right now": a slider in the rail with named stops from efficient to fast. Each stop is an operating profile that sets, together, the number of workers and review slots, the tier map (which model each difficulty uses), the review tier, `retro.difficulty`, and the observation profile from CG-219. Moving the slider applies on change (CG-190), writes the profile as a live override the way `max_parallel` does, and every part of the loop reads it within a tick (CG-192), so a person turns the garden down before leaving and up when they are watching a phase land.

## Context

The user on 2026-09-05, after a day that spent $1,100 and then cut the tier map by hand: "basically a slider from efficient to faster." Today those knobs are five separate places: `max_parallel` (live), `harnesses.<h>.models` and `review.difficulty` (in garden.yaml, reloaded since CG-192), `retro.difficulty` (CG-207), and the observation cadence (CG-219). Changing the operating point at 14:50 took four edits and a restart; the retro of phase 03 needed two more. The trade is real: on 2026-09-05 the fast setting cost about $130 per stretch that the efficient one did for $50, and the efficient one finished the same tasks with a lower first-pass approval on hard PRs.

## Design

- `profiles:` in garden.yaml, ordered from efficient to fast, each with `workers`, `reviews`, `models` (per tier), `review_difficulty`, `retro_difficulty`, `observe`. Built-in defaults: **economy** (3 workers, 2 reviews, all tiers on the cheapest capable model, reviews easy, observe quiet), **balanced** (5, 3, easy and medium on the mid model, hard on the top, reviews easy, observe quiet), **fast** (7, 3, medium on the top model, reviews medium, observe watch). A garden can add or edit stops; the tier map inside a stop may point at any harness model, including OpenRouter (CG-213) later.
- The rail shows the slider with the stop names and, under it, one line of what the stop means (workers, model names, review tier) and the spend rate of the last hour so the choice is visible in money. The Config page shows the full table and the cost per stop over the last day when the costs page (CG-214) has the data.
- The chosen stop is the `operating_profile` override in state; `Store.config` resolves each knob from the profile unless a more specific live override exists (so `max_parallel` alone still works). `garden profile <name>` is the CLI form; `garden status` names the current stop.
- An annotation event (`profile_changed`, with from and to) lands on the costs chart (CG-214) so the effect of a move is readable afterwards.

## Acceptance criteria

- [ ] Three built-in stops exist and a garden can define its own in `profiles:`; each field has a default so a partial stop is valid.
- [ ] The rail slider and `garden profile` switch the stop live; within a tick dispatch uses the new worker count and tier map, reviews use the new tier, and the observe feed uses the new cadence; a test switches from economy to fast and checks all four.
- [ ] A more specific live override (for example `max_parallel`) still wins over the stop, and the Config page says which values come from the stop and which are overridden.
- [ ] Each change emits `profile_changed` and the costs page shows it as an annotation; the rail shows the stop's meaning and the last hour's spend rate.
- [ ] No Set button anywhere in it; works with JavaScript off through a plain select and form post.

## Log

- 2026-09-05T16:51:03+00:00 approved (web)
- 2026-09-05T17:20:10+00:00 dispatched work run 20260905T171954Z-work via local [claude model=claude-sonnet-5] (fresh session, base garden/cg-219-garden-observe-a-configurable-operator-feed-inte stacked on CG-219, ~15274 tokens)
- 2026-09-05T17:28:13+00:00 parent CG-219 merged; will rebase onto main when the current run finishes
- 2026-09-05T17:46:37+00:00 parent CG-219 merged; rebase onto main conflicts; the next run must resolve it
- 2026-09-05T17:46:37+00:00 parent CG-219 merged; rebase conflicts; a rebase agent will resolve it cost=$5.98
- 2026-09-05T17:47:02+00:00 dispatched rebase run 20260905T174702Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~4629 tokens)
- 2026-09-05T17:52:00+00:00 opened https://github.com/joshmarcus/context-garden/pull/175 (base main): Rebased onto origin/main; resolved the single conflict in src/garden/web/common.py by keeping both import additions (Status, dispatch_sort_key from ..model, and describe as describe_stop from ..profiles) since the file body uses all three. Rebase completed, ruff and full test suite (826 passed, 3 skipped) pass. cost=$0.20
- 2026-09-05T17:56:27+00:00 automated review requested changes: Core mechanism, tests and CLI/web wiring are solid, but the costs-page annotation criterion was skipped on a factually wrong premise (the /costs page already exists on main via CG-214) and the PR description is pure rebase narration. cost=$0.57
- 2026-09-05T17:56:49+00:00 dispatched revise run 20260905T175649Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~17567 tokens)
- 2026-09-05T18:05:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/175: Added profile_changed annotations to the /costs chart (the review's blocking finding) and rewrote the PR description to describe the feature instead of rebase narration; all prior CG-221 functionality (profiles, rail slider, garden profile, precedence, live-tick effects) was already in place and unchanged. cost=$0.95
- 2026-09-05T18:05:35+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/charts.py, src/garden/web/pages/costs.py, tests/test_costs.py); a rebase agent will resolve it
- 2026-09-05T18:05:54+00:00 dispatched rebase run 20260905T180554Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~9646 tokens)
