---
id: CG-432
title: Make onboarding GitHub metadata detection transport-independent
status: done
product: context-garden
phase: phase-07
depends_on:
- id: CG-395
  after: merge
priority: 1
difficulty: easy
reading:
- src/garden/onboard.py
- src/garden/gitops.py
- src/garden/github.py
- src/garden/config.py
- tests/test_onboard.py
branch: garden/cg-432-make-onboarding-github-metadata-detection-transp
pr: https://github.com/joshmarcus/context-garden/pull/337
runner: remote
discovered_from: CG-406
attempts: 1
last_dispatched_at: '2026-09-09T01:00:11+00:00'
created: '2026-09-08T15:29:39+00:00'
updated: '2026-09-09T16:46:27+00:00'
file: src/garden/onboard.py
error: tests/test_onboard.py::test_onboard_this_repository_uses_documented_setup_and_ci_tests fails because
  the onboarding report omits `GitHub repository metadata`.
---

## Goal

Make onboarding's GitHub metadata discovery behave consistently across supported clone transports, with honest unavailable-metadata behavior.

## Context

CG406 observed the self-onboarding regression fail on a worker checkout using ssh://git@ssh.github.com:443/... . The operator saw the same transport dependency during the rc5 AWS suite qualification. Recheck the merged CG395 shared URL/host implementation first; reuse it and retain only the missing onboarding behavior/regression rather than building another parser.

## Acceptance criteria

- [ ] Equivalent supported HTTPS, scp-style and official SSH-alias URLs resolve the same canonical public GitHub repository identity; explicit enterprise host routing remains isolated.
- [ ] Onboarding uses the shared resolver for metadata. Unavailable/auth-limited metadata is reported truthfully and does not fabricate a fetched response.
- [ ] Add deterministic transport-equivalence and unavailable-metadata tests with synthetic API responses; self-onboarding expectations do not depend on the operator's checkout transport or credentials.
- [ ] Preserve strict rejection of malformed/credential-bearing URLs and do not send a token to another host.

## Provenance

Discovered by CG406 during run20260908T143602Z-revise. If CG395 already satisfies the behavior, demonstrate that on its merged source and close/reduce this follow-up with evidence.

## Log

- 2026-09-08T15:56:32+00:00 approved (owner-delegated-input-triage)


## Consolidated discovery CG-440

The AWS ordinary suite fails `tests/test_onboard.py::test_onboard_this_repository_uses_documented_setup_and_ci_tests` because the generated report lacks `GitHub repository metadata`, then hangs in `tests/test_runners.py::test_local_runner_launch_flips_to_running_only_after_pid` with a supervisor running `sleep 0.5; cat`. Diagnose these baseline validation failures so the ordinary suite completes deterministically.

## Provenance

Discovered by CG-428 (Keep remote worker runs alive across controller redeploys) during run `20260908T154233Z-work`.
## Log
- 2026-09-08T16:21:10+00:00 discovered by CG-428


Operator disposition: reuse this existing repair; preserve all reporter evidence. CG432 owns onboarding metadata transport identity. CG433 owns completed stdin-consumer liveness and bounded regression cleanup. Do not duplicate implementation.
- 2026-09-08T19:15:14+00:00 dispatched work run 20260908T191514Z-work via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~16250 tokens)
- 2026-09-08T19:23:06+00:00 opened https://github.com/joshmarcus/context-garden/pull/337 (base main): Onboarding now uses the shared GitHub resolver and recognizes HTTPS, scp-style, and official ssh.github.com:443 transports consistently. Added deterministic synthetic metadata and unavailable-metadata regressions while preserving enterprise isolation and URL validation. cost=$0.05


## Consolidated reporter CG-442

Clarify or correct `test_onboard_this_repository_uses_documented_setup_and_ci_tests`: it mocks `_gh_json` to return `None` but asserts that the onboarding report includes `GitHub repository metadata`. Decide whether absent metadata should still render that heading or adjust the assertion to the intended fallback behavior.

## Provenance

Discovered by CG-410 (Show eligible manual work in Inbox with a safe take action) during run `20260908T163839Z-revise`.
## Log
- 2026-09-08T17:03:55+00:00 discovered by CG-410

Operator disposition: preserve this observation under the current deterministic onboarding repair. The transient-cache causal attribution is a reporter hypothesis unless reproduced; absent synthetic metadata must be handled truthfully. No second author.


## Consolidated reporter CG-445

The repository onboarding regression changes its report when `.pytest_cache` exists in the source checkout, causing `test_onboard_this_repository_uses_documented_setup_and_ci_tests` to miss its expected GitHub metadata note. Exclude transient test caches from project discovery so full-suite execution does not alter onboarding results.

## Provenance

Discovered by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) during run `20260908T170122Z-work`.
## Log
- 2026-09-08T17:49:27+00:00 discovered by CG-438

Operator disposition: preserve this observation under the current deterministic onboarding repair. The transient-cache causal attribution is a reporter hypothesis unless reproduced; absent synthetic metadata must be handled truthfully. No second author.
- 2026-09-08T21:34:31+00:00 Delegated Input sweep retired the proven never-started remote request and queued one local review in its original logical round.


## Delegated Input CI audit

Delegated Input CI audit at 2026-09-08T21:39:00.619967+00:00 for current head 7e0756019aba452935a487023a5514b340563780:
test	UNKNOWN STEP	2026-09-08T19:35:00.4601974Z E       AssertionError: assert False
test	UNKNOWN STEP	2026-09-08T19:35:00.4621439Z FAILED tests/scheduler/test_reap.py::test_real_check_waits_for_lease_then_runs_once_and_silent_process_times_out - AssertionError: assert False
test	UNKNOWN STEP	2026-09-08T19:35:00.4625815Z FAILED tests/test_interaction_replay.py::test_task_specific_harness_pause_is_observed_through_the_served_app - assert 'Harness paused' in '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,....getItem(SEEN)) localStorage.setItem(SEEN, nowIso());\n  setInterval(poll, 30000);\n})();\n</script>\n</body>\n</html>'
test	UNKNOWN STEP	2026-09-08T19:35:00.4628843Z 2 failed, 1716 passed, 3 skipped, 4 deselected, 2 warnings in 498.76s (0:08:18)
Original full diagnostics: /home/joshua/work/operator-test-tmp/input-sweep-20260908T2125/pr-337-ci-34268640750.log.
CG446 is merged and owns the named silent-check timeout test removal/timeout policy. Integrate its approved changes when this writer/reviewer drains, then verify affected tests once. The separate served harness-pause expectation remains a real failure to diagnose; do not suppress it.
- 2026-09-08T21:43:25+00:00 automated review requested changes: The transport-independent onboarding change is correct and its focused 71-test suite plus lint pass. The reviewed head still lacks a passing full-suite result: exact-head CI reported two failures, so current main/CG-446 must be integrated and the ordinary suite rerun. cost=$0.39
- 2026-09-09T00:03:36+00:00 RC8 controller routing repairs verified; restored original remote runner for future work/checks/reviews without restarting existing work.
- 2026-09-09T00:04:43+00:00 dispatched revise run 20260909T000443Z-revise via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~17900 tokens)
- 2026-09-09T00:34:19+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/337: Merged current main, preserved the approved timeout-policy repair, and completed the transport-independent onboarding change. Focused onboarding/GitHub/replay tests and lint pass; the full suite retains two unrelated remote-worker lifecycle timeout failures with a durable receipt. cost=$0.11
- 2026-09-09T01:00:04+00:00 1 new review item(s)
- 2026-09-09T01:00:11+00:00 dispatched revise run 20260909T010011Z-revise via remote [codex model=gpt-5.6-luna] (fresh session, base main, ~18859 tokens)
- 2026-09-09T01:00:26+00:00 PR 337 merged at exact reviewed head d12e5bbeb3410212df88490bf9b77d92ab6d71c6 as merge commit a4b27c72a7ef155e71f951a818fb5aa830c257f2 after both exact-head CI runs passed. Operator review attestation records the strict public alias and transport-independent onboarding assessment. Mark complete by merged ancestry.

## Consolidated CG460 discovery 2026-09-09T01:05:16.732720+00:00

CG460 discovery is consolidated into CG432 by operator assessment and confirmation from its assigned reviewer. It reports the exact existing self-onboarding metadata fixture on worker checkouts, not a distinct platform feature. Preserve the original evidence below; current PR337 transport/metadata work owns the outcome. Do not dispatch a duplicate implementation or new generic verification cycle solely from this retained discovery.

The ordinary suite consistently fails `test_onboard_this_repository_uses_documented_setup_and_ci_tests` because the generated report omits the expected GitHub repository metadata section when `_gh_json` is mocked unavailable. Diagnose and make the fixture expectation independent of checkout metadata.

## Provenance

Discovered by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) during run `20260908T235138Z-revise-2`.
## Log
- 2026-09-09T00:30:28+00:00 discovered by CG-438
- 2026-09-09T16:46:27+00:00 automatic review recovery retired because task is done
