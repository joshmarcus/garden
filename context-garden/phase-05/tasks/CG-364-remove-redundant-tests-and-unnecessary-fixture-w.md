---
id: CG-364
title: Remove redundant tests and unnecessary fixture work
status: ready
product: context-garden
phase: phase-05
depends_on:
- CG-354
- CG-361
priority: 2
difficulty: medium
reading: []
created: '2026-09-06T23:32:08+00:00'
updated: '2026-09-06T23:32:09+00:00'
---

## Goal

Remove demonstrated redundant or ineffective test assertions and avoid unnecessary fixture work while retaining regression confidence. Optimize the failures the suite can detect and its execution cost, not its raw test count.

## Context and initial audit

Josh asked on 2026-09-06 whether tests could be removed for redundancy or low value. Operator read-only audit of CG354 head dd7ff92 (based on deployed main58e13b99) found1190 test functions across83 files, no identical AST bodies or repeated test names. Semantic overlap and unnecessary setup remain:762 functions directly request garden or sched, and the common garden fixture always initializes/commits/pushes a Git repo, creates a bare remote and clones a second checkout. This is a static inventory, not a measured deletion speedup.

CG354 owns focused suite organization and bounded Git fixture cleanup; CG361 is changing resource/runner/web tests. Follow their landed versions and avoid competing edits. This task explicitly permits justified test deletions/consolidation; CG354's original preserve-collected-count wording must not turn historical test count into the objective here.

Concrete candidates to investigate:

- tests/test_now1_design.py:test_difficulty_by_model_tables (line148) and tests/test_now1.py:test_difficulty_by_model_credits_the_model_that_got_the_task_accepted (line119) replay the same four-task model-escalation/cost/approval scenario against garden.events.difficulty_by_model. Consolidate their overlapping cases into one authoritative metrics suite, preserving the stronger field/denominator checks and distinct boundary cases. Related ranking/format cases overlap partly but include unique thin/midpoint/rounds cases; do not delete those blindly.
- tests/test_web.py:test_inbox_and_task_page_include_the_same_decision_card_fragment (line612) checks literal Jinja include syntax; nearby actual rendered decision-card tests are stronger. Remove it if the behavioral cases cover its intended contract. test_inbox_page_head_subtitle_is_not_capped_narrow (line1450) checks that '62ch' is absent from response HTML, without loading/layout-checking CSS; it cannot establish the claimed layout outcome. Replace with proportionate actual-layout coverage or retire that assertion with a concrete rationale. The global regex banning Set/Apply/Save button text at1731 also deserves narrowing to the actual autosave behavior, rather than forbidding legitimate unrelated controls.
- tests/test_web.py:test_initial_pages_stay_bounded_with_large_run_history contains assert p95 <= max(timings) even though p95 is selected directly from the same sorted values: this is tautological. Remove the redundant assertion, retain the actual latency and bounded-read checks. The 1546/6000-record cases and real incident-regression coverage are not automatically redundant.
- Ordinary cache-expiry tests sleep for MAX_INDEX_AGE_SECONDS (tests/test_run_index.py:39; tests/test_web.py:57). Use an injected/controlled monotonic clock for deterministic expiry semantics where possible. Retain separately identified real-clock/served-app performance evidence for the responsiveness incident; mocked time is not a performance benchmark.
- Split lightweight document/config/store fixture data from real Git topology and the second remote-host checkout where tests do not need those behaviors. Start with demonstrably pure/read-only test groups and an opt-in remote clone. Preserve real Git integration cases; don't introduce globally shared mutable fixtures just to make them faster.
- The old Now design mock tests are candidates for a separate design-tools check only after checking their current consumers. Some tests in test_now1_design.py exercise production metrics and must remain in normal product coverage. Both live Now pages remain supported; this task does not retire either page.

## Acceptance criteria

- [ ] For every removed or consolidated case, record the invariant it protected and the surviving test(s), or why the invariant was ineffective/obsolete. Preserve unique error/edge cases and security, state concurrency, recovery, merge, resource-admission and responsiveness regressions. No arbitrary target reduction in test count.
- [ ] Remove the demonstrated semantic/tautological duplication and replace implementation-text checks only when equivalent behavioral coverage exists or is added. Retain meaningful CLI/web boundary smoke checks without replaying every lower-layer case at every layer.
- [ ] Demonstrate fewer unnecessary Git/process/fixture operations for a representative small suite with independent mutable state and unchanged relevant behavior. Report serial before/after test counts, elapsed time, peak memory and temp use under the same limits; distinguish selection-only gains from total-suite savings. Do not claim the expected speedup as measured.
- [ ] Focused local checks remain serial and bounded; final exact-commit GitHub CI passes for the complete retained suite. No local full-suite stress runs, weakened merge gate, production service changes or extra model agents. Report normal acceptance evidence and unresolved limitations.

## Provenance

Owner question: Are there tests we could remove for being redundant or not useful? Operator review only so far; no tests have been deleted by this audit.

## Log

- 2026-09-06T23:32:09+00:00 approved (cli)
