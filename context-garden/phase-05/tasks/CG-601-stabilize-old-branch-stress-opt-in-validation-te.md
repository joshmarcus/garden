---
id: CG-601
title: Isolate old-branch validation policy fixtures from inherited pytest options
status: done
product: context-garden
phase: phase-05
depends_on:
- id: CG-600
  after: merge
priority: 0
difficulty: medium
reading:
- src/garden/validation.py
- context-garden/phase-05/docs/cg601-validation-fixture-diagnosis.md
branch: garden/cg-601-isolate-old-branch-validation-policy-fixtures-fr
pr: https://github.com/joshmarcus/context-garden/pull/484
runner: remote
discovered_from: CG-600
attempts: 3
last_dispatched_at: '2026-09-11T05:50:53+00:00'
created: '2026-09-10T22:50:28+00:00'
updated: '2026-09-11T06:13:39+00:00'
file: tests/test_validation.py
error: Expected nested pytest return code 1, observed 0.
---

The exact-head full suite and focused rerun both failed `tests/test_validation.py::test_old_branch_can_explicitly_opt_in_to_known_stress`: the synthetic old checkout returned 0 with one pass and three deselections where the test expects return code 1. The author reported it as unrelated; that attribution has not yet been independently established.

## Provenance

Discovered by CG-600 (Finish model runs when a harness replaces the final-output FIFO) during run `20260910T222043Z-work`.
## Log
- 2026-09-10T22:50:28+00:00 discovered by CG-600
- 2026-09-10T22:56:11+00:00 also found by CG-600 (Finish model runs when a harness replaces the final-output FIFO) during run `20260910T222043Z-work`


## Operator disposition, 2026-09-10T23:05Z

Retain this draft while CG600's already-requested correction diagnoses the same exact validation failure. Do not launch a duplicate author or grant stress opt-in. If it persists independently after accepted CG600, scope and approve this distinct validation repair; if CG600 resolves it, preserve the original observation and cancel this duplicate. Current non-approval is a bounded dependency/duplicate disposition, not a test waiver.
- 2026-09-10T23:09:55+00:00 operator retained draft pending CG600 diagnosis of the same failure; original observation preserved


## Resolved scope after independent diagnosis, 2026-09-11

The exact unchanged test and validation module match accepted main059a28e4277248b6782a759e0d2647e92b594553. A bounded independent pair ran ONLY the named synthetic fixture: a clean PYTEST_ADDOPTS environment passed; inherited worker default --deselect options reproduced the expected1/observed0 failure. The fixture calls resolve_validation directly and then subprocess.run, bypassing the environment normalization that validation.main performs. The real stress workloads were never run. Evidence is rc20-20260910/validation-fixture-diagnosis/receipt.json and the two original logs, captured00:13:02UTC.

This establishes a distinct fixture/policy-boundary issue; CG600's final-output source does not modify either file. Keep the original observations above. Wait for CG600's actual merge, then repair this bounded fixture issue. This task does not explain the other unidentified full-suite failure or waive the original timeout.

## Goal

Make the synthetic old-branch policy tests accurately exercise explicit opt-in in an environment that already carries the worker's default test exclusions, while preserving default enforcement for real validation.

## Acceptance criteria

- [ ] The dummy-checkout opt-in fixture passes both with empty options and with inherited worker POLICY_ADDOPTS; the deliberate dummy failures are exercised as intended. Do not run the repository's actual stress workloads.
- [ ] Isolate or normalize only the fixture subprocess using the intended public validation behavior. Preserve unrelated pytest options and the parent environment, and do not weaken production default exclusion, approval, ownership or timeout policy.
- [ ] Add proportionate deterministic coverage of both environments, run the relevant validation test file and Ruff, and obtain real exact-head CI and independent review. Use portable process/environment APIs and report untested platforms accurately.
- 2026-09-11T00:24:03+00:00 independent bounded diagnosis establishes distinct fixture issue; scoped for implementation only after CG600 actual merge
- 2026-09-11T00:30:10+00:00 provided exact source excerpts and independent two-environment reproduction as accessible reading; original missing cached-checkout path failure preserved
- 2026-09-11T00:30:10+00:00 approved (delegated operator after independent fixture diagnosis)
- 2026-09-11T00:46:37+00:00 dispatched work run 20260911T004633Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~16066 tokens)
- 2026-09-11T01:06:46+00:00 attempt 1 failed: no GARDEN_RESULT in worker output (WARNING: proceeding, even though we could not create PATH aliases: Permission denied (os error 13)
Error: failed to initialize in-process app-server client: Permission denied (os error 13)); will retry
- 2026-09-11T01:07:06+00:00 dispatched work run 20260911T010702Z-work via local [codex model=gpt-5.6-luna] (fresh session, base main, ~16174 tokens)
- 2026-09-11T01:09:36+00:00 Local attempt004633 failed before model output with read-only Codex home; original evidence and absent exit/final preserved. Existing fixture task now uses remote capacity;617 owns distinct local startup repair.
- 2026-09-11T01:34:00+00:00 attempt 2 failed: no GARDEN_RESULT in worker output (WARNING: proceeding, even though we could not create PATH aliases: Permission denied (os error 13)
Error: failed to initialize in-process app-server client: Permission denied (os error 13)); giving up
- 2026-09-11T01:34:00+00:00 reset to ready by hand
- 2026-09-11T01:34:01+00:00 One supported retry after routing to existing remote capacity; preserve two local pre-model failures and their original missing exit/final/cost evidence. Native retry resets its automatic-attempt counter; complete Run history remains unchanged.
- 2026-09-11T01:34:23+00:00 dispatched work run 20260911T013423Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~16331 tokens)
- 2026-09-11T02:21:16+00:00 attempt 1 failed: worker idle 21 min (no output or file change); will retry
- 2026-09-11T02:21:47+00:00 dispatched work run 20260911T022147Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~16394 tokens)
- 2026-09-11T02:39:05+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T02:56:04+00:00 opened https://github.com/joshmarcus/context-garden/pull/484 (base main): Isolated the old-branch opt-in fixture from inherited policy deselections and added clean/inherited-policy coverage. Focused validation passed (15 tests) and Ruff passed; exact-head CI and independent review remain scheduler gates. cost=$0.03
- 2026-09-11T03:02:44+00:00 automated review requested changes: The focused suite and Ruff pass in the current environment, but the new fixture is not deterministic and does not actually guarantee an empty-options case. cost=$0.18
- 2026-09-11T03:03:10+00:00 dispatched revise run 20260911T030310Z-revise via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~17421 tokens)
- 2026-09-11T03:16:09+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T03:18:02+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/484: Made old-branch opt-in fixture environments deterministic and verified all 15 validation tests pass even with ambient -x, plus Ruff and compile checks. cost=$0.03
- 2026-09-11T03:28:07+00:00 automated review requested changes: The fixture change passes focused review, but the revised head lacks the required exact-head CI result. cost=$0.18
- 2026-09-11T03:28:42+00:00 dispatched revise run 20260911T032841Z-revise via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~17429 tokens)
- 2026-09-11T03:36:41+00:00 temporary runner hold by delegated_operator: Current25c5520a exactCI34557802474/34557799640 passed; prior reviewer accepted the source but had parent-only CI. Preserve the already-running032841 revision and its output; prevent another unchanged author round. Root will return current source to evidence review after this run concludes.
- 2026-09-11T03:48:38+00:00 temporary runner hold released by delegated_operator: Current25c5520a exactCI34557802474/34557799640 passed; prior reviewer accepted the source but had parent-only CI. Preserve the already-running032841 revision and its output; prevent another unchanged author round. Root will return current source to evidence review after this run concludes.
- 2026-09-11T03:48:38+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T03:53:59+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/484: Hardened old-branch opt-in fixture environment handling and committed the fix. Focused validation, Ruff, compile, and diff checks pass; exact-head CI remains scheduler-owned. cost=$0.03
- 2026-09-11T04:05:44+00:00 automated review requested changes: The fixture remains dependent on unrelated inherited pytest behavior: ambient `-x` prevents all three deliberate failures from running and breaks the focused suite. Exact-head CI is also still pending. cost=$0.20
- 2026-09-11T04:06:12+00:00 difficulty easy -> medium after 2 substantive revisions; model gpt-5.6-luna -> gpt-5.6-terra
- 2026-09-11T04:06:12+00:00 dispatched revise run 20260911T040612Z-revise via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~18314 tokens)
- 2026-09-11T04:35:28+00:00 revision failed: worker idle 26 min (no output or file change)
- 2026-09-11T05:50:53+00:00 dispatched work run 20260911T055053Z-work via manual [human] (fresh session, base main, ~2591 tokens)
- 2026-09-11T05:50:54+00:00 external PR attached at garden/cg-601-isolate-old-branch-validation-policy-fixtures-fr; existing CI is SUCCESS
- 2026-09-11T06:02:11+00:00 automated review: approve — The fixture deterministically covers clean, inherited-policy, and unrelated-option environments without changing production policy code. cost=$0.10
- 2026-09-11T06:13:39+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/484
