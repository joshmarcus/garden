---
id: CG-235
title: retro.model (or a best tier) names the model retros, persona reviews and trial comparisons run
  on, independent of the hard tier's price
status: done
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
branch: garden/cg-235-retro-model-or-a-best-tier-names-the-model-retro
pr: https://github.com/joshmarcus/context-garden/pull/190
attempts: 1
last_dispatched_at: '2026-09-05T21:56:10+00:00'
created: '2026-09-05T20:48:03+00:00'
updated: '2026-09-05T22:30:33+00:00'
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
- 2026-09-05T20:49:24+00:00 dispatched work run 20260905T204908Z-work via local [claude model=claude-sonnet-5] (fresh session, base main, ~19122 tokens)
- 2026-09-05T21:10:40+00:00 pre-PR checks failed (test); no PR opened yet; revise run will fix cost=$3.81
- 2026-09-05T21:11:03+00:00 dispatched revise run 20260905T211103Z-revise via local [claude model=claude-sonnet-5] (fresh session, base main, ~19720 tokens)
- 2026-09-05T21:16:54+00:00 worker says nothing to change: Re-ran the full suite twice in isolation (PYTHONPATH=src .venv/bin/python -m pytest -q -x): 914 passed, 3 skipped, ~101-102s both times, and .venv/bin/ruff check src tests passes clean. The prior pre-PR failure (exit 143, 'Terminated' after ~94% of tests) is consistent with this shared machine running several concurrent worker/pytest/claude processes at that moment (confirmed via ps aux — another pytest run, a live `garden serve`, and multiple claude worker subprocesses were active), not a defect introduced by the diff. All acceptance criteria were already satisfied by the existing commits (b03c0ab/ed4e716/52edd53): retro_model_for() in scheduler/__init__.py is used by retro.py (retro_plan and start_retro), aux.py's dispatch_aux for persona/compare runs, and trials.py now sources its tier from retro.difficulty; garden retro --dry-run (cli/planning.py:287) and garden trial (cli/loop.py:486-489) both print the judge's model; README/architecture.md/examples/garden.work.yaml document it; and tests/test_extras.py + tests/test_retro.py cover persona (phase+PR), trial-compare and retro-reconciliation resolution including the harness-scoped fallback. cost=$0.62
- 2026-09-05T21:43:54+00:00 no-change accepted by the person (operator: the pre-PR test check was killed under load (exit 143 at 94%), not a defect; accepted, open the PR); resuming the round without a new work run
- 2026-09-05T21:46:40+00:00 opened https://github.com/joshmarcus/context-garden/pull/190 (base main): No code change was needed: the failing pre-PR test check was an environment/resource-contention flake on this shared machine, not a defect in the CG-235 diff, which already satisfies every acceptance criterion.
- 2026-09-05T21:46:44+00:00 PR conflicts with main; rebase onto main conflicts (README.md); a rebase agent will resolve it
- 2026-09-05T21:47:06+00:00 dispatched rebase run 20260905T214706Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~11170 tokens)
- 2026-09-05T21:55:50+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/190: Rebased onto origin/main; the sole conflict was in README.md, where main's independent CG-234 rewrite (PR #189) had already replaced the whole file with a terser front-door README that dropped the Personas/Configuration sections this branch's ed4e716 had edited. Resolved by taking main's current README.md verbatim (byte-identical to origin/main after resolution) since the retro.model/retro_model documentation this branch adds is preserved without conflict in docs/architecture.md and examples/garden.work.yaml, which is where the technical reference now lives. Rebase completed cleanly (git rebase --continue) and the full test suite passes (933 passed, 3 skipped). cost=$0.78
- 2026-09-05T21:55:53+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/trials.py); a rebase agent will resolve it
- 2026-09-05T21:56:10+00:00 dispatched rebase run 20260905T215610Z-rebase via local [claude model=claude-sonnet-5] (fresh session, base main, conflict only; easy tier, ~7356 tokens)
- 2026-09-05T22:03:21+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/190: Rebased onto origin/main; the sole conflict was in src/garden/scheduler/trials.py, where main's CG-212 refactor had introduced a local `harness_name` variable (reused for the pause-check before compare dispatch) on the same line this branch's 0c38b10 changed the difficulty source from review.difficulty to retro.difficulty. Resolved by keeping main's `harness_name` variable reuse and applying this branch's `retro.difficulty` change, preserving both changes' intent. Rebase completed cleanly; full suite passes (958 passed, 3 skipped) and ruff is clean. cost=$0.30
- 2026-09-05T22:10:39+00:00 description rewritten by the reviewer cost=$0.87
- 2026-09-05T22:30:33+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/190
