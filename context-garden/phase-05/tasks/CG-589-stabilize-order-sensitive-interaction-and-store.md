---
id: CG-589
title: Stabilize order-sensitive interaction and Store tests
status: done
product: context-garden
phase: phase-05
depends_on:
- id: CG-585
  after: merge
priority: 2
difficulty: medium
reading:
- tests/test_interaction_replay.py
- tests/test_web.py
- src/garden/store.py
branch: garden/cg-589-stabilize-order-sensitive-interaction-and-store
pr: https://github.com/joshmarcus/context-garden/pull/453
runner: remote
discovered_from: CG-585
attempts: 1
last_dispatched_at: '2026-09-10T15:49:30+00:00'
created: '2026-09-10T15:31:38+00:00'
updated: '2026-09-10T16:10:38+00:00'
file: tests/test_interaction_replay.py
error: 'Full-suite-only failures: DM-002 did not reach failed; discovery signature count advanced unexpectedly.'
---

## Goal

Find and remove the shared-state or timing dependence in interaction replay and discovery-generation validation, preserving their real behavior checks.

## Acceptance criteria

- [ ] Preserve CG585's full-suite failures and focused passes at6ea7dd8c for tests/test_interaction_replay.py::test_replay_records_performed_requests_and_existing_artifacts and tests/test_web.py::test_read_generation_skips_discovery_fingerprints_until_a_watch_event. Record source, environment and preceding-test/order evidence; a focused pass alone is not a diagnosis.
- [ ] Isolate whether the cause is leaked module/fixture state, a real Store generation or replay lifecycle defect, or an unsuitable timing assumption. Use a bounded reproducer or selected predecessor sequence and distinguish confirmed causes from hypotheses.
- [ ] Fix the responsible boundary or test isolation while preserving recorded performed requests/artifacts, failure/recovery transitions and watcher-driven discovery freshness. Do not blanket-retry tests, skip coverage, inflate timeouts without evidence or weaken assertions just to turn the run green.
- [ ] Verify the reproducing order and relevant combined suite; retain original failures and explain any remaining uncertainty. Coordinate the already-completed CG522 discovery-snapshot implementation rather than undoing its contract. Use portable tests and report native platforms actually exercised.

## Original discovery

The full suite repeatedly failed the interaction replay timeout and Store discovery-generation assertion, while both exact nodes passed in a subsequent focused selection. Identify and remove the shared-state or timing dependence without coupling it to the RunStore import repair.

## Provenance

Discovered by CG-585 (Repair the RunStore import cycle on merged main) during run `20260910T145928Z-work`.
## Log
- 2026-09-10T15:31:38+00:00 discovered by CG-585
- 2026-09-10T15:48:26+00:00 approved (delegated operator; complete bounded follow-up with original nonblocking discovery preserved)
- 2026-09-10T15:49:30+00:00 dispatched work run 20260910T154930Z-work via remote [codex model=gpt-5.6-terra] (fresh session, base main, ~15861 tokens)
- 2026-09-10T15:57:54+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T15:59:21+00:00 opened https://github.com/joshmarcus/context-garden/pull/453 (base main): Released inotify descriptors held by discarded discovery watchers, preventing long test processes from exhausting the Linux watcher budget and falling back to per-request Store fingerprints. Verified commit 3a0233c1 with the complete interaction-replay module plus discovery-generation regressions and full lint. cost=$0.77
- 2026-09-10T16:02:00+00:00 automated review: approve — The finalizer closes descriptors leaked by short-lived web apps without changing Store discovery, replay assertions, retries, or timing thresholds. cost=$0.27
- 2026-09-10T16:10:38+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/453
