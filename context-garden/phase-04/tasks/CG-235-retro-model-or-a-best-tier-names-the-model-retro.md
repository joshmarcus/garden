---
id: CG-235
title: retro.model (or a best tier) names the model retros, persona reviews and trial comparisons run
  on, independent of the hard tier's price
status: ready
product: context-garden
phase: phase-04
depends_on: []
priority: 1
difficulty: easy
reading:
- src/garden/config.py
- src/garden/scheduler/persona.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/trials.py
- src/garden/scheduler/__init__.py
- garden.yaml
created: '2026-09-05T20:48:03+00:00'
updated: '2026-09-05T20:48:04+00:00'
---

## Goal

The model that judges (retro reconciliation, persona reviews, trial comparisons) is chosen separately from the tier map that prices work. `retro.model` (per harness, `harnesses.<h>.retro_model`, with `retro.difficulty` kept as the fallback) names it outright, so a garden can run work on cheap tiers and still hand its retro and its trial verdicts to the best model available, without editing the hard tier before each retro.

## Context

The user on 2026-09-05: "I want retros on best models but normal reviews don't need to be." CG-207 added `retro.difficulty` (default hard), but the tier map now prices hard work on opus 4.8 to cut spend, so a retro would run on opus; the best model (claude fable 5.1, $10 / $50) is not in the map at all. The operator's alternative is to flip `hard:` to fable for the duration of a retro and back, which is the config-editing CG-207 set out to remove. Trial comparisons matter the same way: the judge decides which contender's code merges (today's CG-225 verdicts were by sonnet 5); a wrong judge is more expensive than an expensive judge. PR reviews stay on the review tier.

## Acceptance criteria

- [ ] `harnesses.<h>.retro_model` (and a top-level `retro.model` for the default harness) is read by the retro reconciliation, persona reviews (phase and PR) and the trial comparison run; when unset, `retro.difficulty` resolves the tier as today.
- [ ] `garden retro --dry-run` and `garden trial` print the judge's model; the run records carry it.
- [ ] The example configs show work tiers on cheap models with `retro_model` on the top model; the docs say which runs use it.
- [ ] Tests: a config with `retro_model` set dispatches a persona review and a compare run on it while a work run uses the tier map.

## Log

- 2026-09-05T20:48:04+00:00 approved (web)
