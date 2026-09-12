# Friction

_No friction reported yet._

## Reported

### 2026-09-08 · reported by CG-395 (Support explicit GitHub Enterprise hosts across all repository operations) in run 20260908T120323Z-work

- GARDEN_VALIDATION_RUNNER was unset, so focused checks ran directly.

### 2026-09-08 · reported by CG-397 (Respect external branch-stack ownership and configurable protected paths) in run 20260908T120326Z-work

- GARDEN_VALIDATION_RUNNER was unset, so its required invocation failed with Permission denied; focused validation ran directly.

### 2026-09-08 · reported by CG-399 (Keep physical host identities out of committed context and public evidence) in run 20260908T120326Z-work-2

- The CI helper's unauthenticated GitHub Actions API quota exhausted during polling; the exact run's public Actions page confirmed terminal success.

### 2026-09-08 · reported by CG-406 (Support fenced in-place canonical checkouts with safe per-run reconciliation) in run 20260908T120328Z-work

- The supplied enterprise-environment specification did not resolve from the reading list.
- GARDEN_VALIDATION_RUNNER was unset, so focused validations ran directly.
- Public CI metadata exposed the failed step but not logs; the initial missing architecture-map entry was diagnosed with a local suite run.

### 2026-09-08 · reported by CG-409 (Finish manual work pushed from another machine without a local authoring checkout) in run 20260908T124014Z-work

- The referenced phase-07 enterprise remote environments specification did not resolve in the supplied reading list.
- GARDEN_VALIDATION_RUNNER was unset, so the prescribed wrapper invocation failed before launching tests; focused validation was run directly.

### 2026-09-08 · reported by CG-401 (Pass approved tool configuration into scrubbed local and remote workers) in run 20260908T135246Z-work-2

- The phase specification listed in the reading manifest was unavailable, so the implementation used the frozen acceptance criteria and existing worker isolation conventions as the contract.
- The supervised combined runner suite deadlocked on nested supervisor admission; final runner verification set `GARDEN_EXECUTION_LEASED=1` for the already-supervised nested integration selection.

### 2026-09-08 · reported by CG-404 (Add command-backed host acquisition readiness and warm reuse to the shared lifecycle) in run 20260908T135247Z-work

- The required phase-07 enterprise remote-environments specification was absent from the checkout.
- The supervised full suite could not complete cleanly: one run deadlocked in an existing nested local-runner supervisor test, while fail-fast reached 911 passed before an unrelated onboarding assertion failed because GitHub repository metadata was unavailable.

### 2026-09-08 · reported by CG-412 (Resolve check commands analyzers and timeouts per product) in run 20260908T135248Z-work

- The supervised full suite hung in existing `tests/test_runners.py::test_local_runner_launch_flips_process_finished`; its tiny runner child did not write exit_code after more than ten minutes, so the validation was stopped.

### 2026-09-08 · reported by CG-398 (Validate a human-gated enterprise profile with bot feedback and private notifications) in run 20260908T135246Z-work

- The ordinary full suite reported one failure at 57% and then stalled without emitting the failing node; focused coverage and lint passed.

### 2026-09-08 · reported by CG-395 (Support explicit GitHub Enterprise hosts across all repository operations) in run 20260908T142935Z-revise

- The supervised full pytest run stalled at test_trial_wait_polls_until_the_trial_concludes without emitting a failure; it was terminated after several minutes. Focused affected tests and lint passed.
- Declined review improvement: Create a served-app interaction replay manifest. — The frozen validation plan explicitly marks interaction false and this change has no rendered or served lifecycle behavior; direct CLI and REST tests exercise the affected boundary.

### 2026-09-08 · reported by CG-406 (Support fenced in-place canonical checkouts with safe per-run reconciliation) in run 20260908T143602Z-revise

- The supplied phase specification path did not resolve.
- The full-suite policy referenced known stress nodes without naming them on this pre-CG-426 branch.

### 2026-09-08 · reported by CG-397 (Respect external branch-stack ownership and configurable protected paths) in run 20260908T142935Z-revise-2

- The full pytest child completed, but a test-created disposable run-supervisor descendant prevented the validation wrapper from publishing a trustworthy pytest receipt; the exact orphan was terminated after inspection. Focused regressions and lint passed.

### 2026-09-08 · reported by CG-404 (Add command-backed host acquisition readiness and warm reuse to the shared lifecycle) in run 20260908T145826Z-revise

- The supplied phase specification reading-list path did not resolve.
- The supervised full suite hung in an unrelated local-runner test on its first run; a fail-fast rerun exposed an unrelated GitHub-metadata onboarding failure.
- No typecheck command or mypy/pyright configuration exists in the repository.

### 2026-09-08 · reported by CG-411 (Adopt an existing PR with its verified branch and revision identity) in run 20260908T153212Z-work

- Full ordinary pytest run hung in tests/test_runners.py::test_local_runner_launch_flips_process_finished after its child exited; the supervised run was stopped and returned exit code 3.
- No configured typecheck tool exists in pyproject.toml.

### 2026-09-08 · reported by CG-405 (Apply host-local resource admission and capability routing to command-backed hosts) in run 20260908T154409Z-work

- The phase specification reading-list entry was unavailable as declared in the brief; implementation used the frozen criteria and existing host lifecycle documentation.

### 2026-09-08 · reported by CG-413 (Use product-specific execution timeouts and weighted resource admission) in run 20260908T154653Z-work

- The referenced enterprise remote environments specification was unavailable in the supplied reading list.

### 2026-09-08 · reported by CG-404 (Add command-backed host acquisition readiness and warm reuse to the shared lifecycle) in run 20260908T162136Z-revise

- The full ordinary suite hung in an unrelated local-runner supervisor test after reaching 79%; the focused lifecycle suites and full lint completed successfully.

### 2026-09-08 · reported by CG-406 (Support fenced in-place canonical checkouts with safe per-run reconciliation) in run 20260908T162909Z-revise

- The preserved operator pyproject overlay makes the interaction replay clean-head test fail even though task source is committed.
- The supervised full suite deadlocked in an existing nested local-runner supervision test after the clean-head failure.

### 2026-09-08 · reported by CG-415 (Register private runner adapters through trusted configuration) in run 20260908T170706Z-work

- The broad `tests/test_runners.py -q` validation wrapped by the supervised runner stalled in an existing local-runner lifecycle test; it was stopped and replaced with the focused adapter selection, which passed.

### 2026-09-08 · reported by CG-404 (Add command-backed host acquisition readiness and warm reuse to the shared lifecycle) in run 20260908T171818Z-revise

- GitHub CLI was unauthenticated and the public PR endpoint was unavailable, preventing direct inspection of current PR comments and checks.
- The full ordinary suite hung in an unrelated local-runner fixture after 78%; its separate onboarding failure was caused by unavailable GitHub metadata.
- The phase specification reading-list entry was absent, as noted in the brief.

### 2026-09-08 · reported by CG-415 (Register private runner adapters through trusted configuration) in run 20260908T175642Z-revise

- No project typechecker is configured in pyproject.toml or documented test commands.
- Declined review improvement: Make the interaction replay artifact readable by the review worker and record its launch command. — The frozen validation plan explicitly sets interaction=false and identifies no rendered or lifecycle behavior change; this diagnostic-only change is covered by CLI interaction tests rather than a served-app replay.

### 2026-09-08 · reported by CG-414 (Assign owners to tasks and phases and filter work by owner) in run 20260908T190921Z-revise

- The supervised runner returned partial progress for broader focused selections; exact owner and remote UI nodes were rerun and reported passing results.

### 2026-09-08 · reported by CG-443 (Keep out-of-scope review limitations from rejecting satisfied acceptance criteria) in run 20260908T191256Z-revise

- No project typecheck command or configured type checker was found in pyproject.toml, docs/test-suites.md, or scripts; focused tests and required lint were run.

### 2026-09-08 · reported by CG-432 (Make onboarding GitHub metadata detection transport-independent) in run 20260908T191514Z-work

- No repository-configured typecheck command or mypy/pyright executable was available.

### 2026-09-08 · reported by CG-451 (Reject credential-bearing and ambiguous manually adopted PR URLs) in run 20260908T192612Z-work

- No configured typecheck command was found in pyproject, Makefile, scripts, or docs/test-suites.md.

### 2026-09-08 · reported by CG-396 (Use pluggable exact-head CI status for review and merge eligibility) in run 20260908T193927Z-revise

- The referenced phase specification was unavailable in the dispatched reading list; the supplied frozen criteria and product documentation were sufficient.

### 2026-09-08 · reported by CG-452 (Keep GitHub Actions analyzers scoped to the configured repository host) in run 20260908T194939Z-work

- No project type-check command or type-check executable is configured.

### 2026-09-08 · reported by CG-452 (Keep GitHub Actions analyzers scoped to the configured repository host) in run 20260908T215347Z-revise

- Failed GitHub Actions job logs require repository-admin access; public metadata exposed the failing step but not its test output.

### 2026-09-08 · reported by CG-447 (Unify scp-form repository classification across config and worker claims) in run 20260908T223241Z-revise

- The broad remote-worker focused suite entered existing managed-worker lifecycle subprocess waits; it was stopped after exceeding the 120-second ordinary-test bound. Targeted current-head regressions completed successfully.

### 2026-09-08 · reported by CG-454 (Skip destructive pre-merge rebase when the reviewed remote head is already current) in run 20260908T224702Z-revise

- The unrelated served remote-lifecycle fixture exceeded its 120-second per-test budget while waiting on a detached check process; it was terminated and not counted as passing evidence.

### 2026-09-08 · reported by CG-414 (Assign owners to tasks and phases and filter work by owner) in run 20260908T222403Z-revise-2

- Combined remote-worker test selection exceeded the 120-second ordinary-test bound and was interrupted; split focused owner regressions passed.

### 2026-09-08 · reported by CG-443 (Keep out-of-scope review limitations from rejecting satisfied acceptance criteria) in run 20260908T225300Z-revise

- A supplemental web-test node was initially referenced by an outdated name; the actual named test was then run successfully.

### 2026-09-08 · review loop for CG-443 (Keep out-of-scope review limitations from rejecting satisfied acceptance criteria)

- Review loop: 4 rounds, $6.40 cumulative work/revise/review cost; head lineage 7bf3b12897f7d8d72783680c6b0ce122a2bbc209, 38b2375e0081fa1f2bf6e9434527e270c47b1328, a891defc081191e9f6b14c170d992496755189ec; cause: unknown; actionable evidence: All six frozen criteria are satisfied. Focused tests and lint pass; required gaps still block while out-of-scope limitations remain visible and ambiguous legacy entries use a bounded reviewer-owned continuation.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-08 · reported by CG-447 (Unify scp-form repository classification across config and worker claims) in run 20260908T225611Z-revise

- A completed broad remote-worker test process left its validation supervisor holding the shared slot; focused validation was rerun after cleanup.

### 2026-09-08 · reported by CG-457 (Prevent remote queue-age timeouts from duplicating live work and losing run fences) in run 20260908T230247Z-work

- The full-suite served-HTTP tests left remote check supervisors holding shared validation capacity after their internal 30-second subprocess timeouts; these processes required scoped termination before focused validation could continue.
- The full suite also failed an unrelated onboarding assertion because repository metadata was unavailable in that test environment.

### 2026-09-08 · reported by CG-406 (Support fenced in-place canonical checkouts with safe per-run reconciliation) in run 20260908T232847Z-revise

- The phase specification named in the reading list was unavailable, as recorded in the brief.

### 2026-09-09 · reported by CG-456 (Admit remote reviews independently of occupied local review capacity) in run 20260909T001054Z-revise

- Automated review demanded served HTTP evidence despite the frozen validation plan marking interaction false and the acceptance criterion rejecting unrelated UI replay.
- Declined review improvement: Replay the affected flow through served HTTP or browser actions. — The scheduler admission decision has no served HTTP action; `/now` only renders state. The frozen plan marks interaction false, controller commands are prohibited in this worker, and the criterion explicitly rejects a generic unrelated UI replay.

### 2026-09-09 · discovered by CG-432 (Make onboarding GitHub metadata detection transport-independent) in run 20260909T000443Z-revise

The remote-worker lifecycle timeout remains independently reproducible on the exact reviewed head; receipt: artifacts/cg-432-validation/remote-worker-focused.log.

### 2026-09-09 · reported by CG-432 (Make onboarding GitHub metadata detection transport-independent) in run 20260909T000443Z-revise

- The exact-head ordinary suite still times out in unrelated remote-worker lifecycle tests; focused reproduction is saved under artifacts/cg-432-validation/remote-worker-focused.log.
- No configured mypy or pyright type-check command exists in the repository.
- Declined review improvement: If served interaction remains required mechanically, add a task-specific CLI/onboarding replay type or classify onboarding as non-served behavior. — Declined adding unrelated replay infrastructure because onboarding is non-served behavior and the frozen validation plan explicitly sets interaction to false; existing served replay regression passes.

### 2026-09-09 · reported by CG-406 (Support fenced in-place canonical checkouts with safe per-run reconciliation) in run 20260909T002924Z-revise

- The phase specification reading-list entry was unavailable as noted in the brief.
- The repository has no configured static typechecker or typecheck dependency; pytest and Ruff are the available final checks.

### 2026-09-09 · review loop for CG-406 (Support fenced in-place canonical checkouts with safe per-run reconciliation)

- Review loop: 4 rounds, $17.57 cumulative work/revise/review cost; head lineage 87d4317de48e0be23c71981087bfa064a8ab0708, c6a11f43166b8e3a4c3e23c69e6919d731f70c66, 9b6f840ef09af17560a8d3c985eca5ebb221b630, ec3d515495047eef63d8bde8ff516193bbc833f7, dc165c67136c5ac2ccca5e0ab9db17c004778e29; cause: unknown; actionable evidence: Canonical exclusivity is incomplete: ordinary local dispatches do not record their canonical worktree before claiming, allowing another dispatch to reclaim the live lease, while remote collection hard-resets the local canonical checkout without claiming or preflighting it.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-406 (Support fenced in-place canonical checkouts with safe per-run reconciliation) in run 20260909T014155Z-revise

- The phase specification reading-list entry was unavailable, as noted in the supplied brief.
- The repository defines no separate typecheck command; focused typed-Python tests and Ruff were used.

### 2026-09-09 · reported by CG-451 (Reject credential-bearing and ambiguous manually adopted PR URLs) in run 20260909T014538Z-revise

- No configured mypy or pyright executable is present; repository lint and focused tests were run.

### 2026-09-09 · reported by CG-404 (Add command-backed host acquisition readiness and warm reuse to the shared lifecycle) in run 20260909T015450Z-revise

- The phase specification reading-list entry was unavailable as noted in the brief; existing repository architecture, design, worker protocol, and implementation supplied sufficient context.

### 2026-09-09 · review loop for CG-404 (Add command-backed host acquisition readiness and warm reuse to the shared lifecycle)

- Review loop: 4 rounds, $11.66 cumulative work/revise/review cost; head lineage 1c1164cd0d30f88dd0d0189d7a0c44585eef067b, 633e78f4901636f5817c364819dcc16b3df33a9e, e7548b50461f947e0a9d590977da40d8e430db8c, 6420cb9d8bb16f314820715c3058cc7b50601f87; cause: unknown; actionable evidence: The overlapping-controller acquisition race is fixed and the focused 29-test suite passes. However, a wrong-shaped inspect response bypasses environment-stop handling, leaving a provisioning failure path unrecoverable under the lifecycle contract.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-412 (Resolve check commands analyzers and timeouts per product) in run 20260909T020220Z-revise

- No configured type-checker exists in pyproject or repository tooling.

### 2026-09-09 · reported by CG-413 (Use product-specific execution timeouts and weighted resource admission) in run 20260909T034518Z-revise

- The preceding rebase left syntactically interleaved conflict-resolution fragments in dispatch.py and review.py.

### 2026-09-09 · reported by CG-414 (Assign owners to tasks and phases and filter work by owner) in run 20260909T094250Z-revise-2

- GitHub Actions failure logs could not be accessed because gh is not authenticated in this worker.

### 2026-09-09 · review loop for CG-414 (Assign owners to tasks and phases and filter work by owner)

- Review loop: 4 rounds, $9.71 cumulative work/revise/review cost; head lineage 2005322b25927b61ceb10b5554cf90c629bb577b, 20e32b484fc66dc17eb8711a5e8d6fb39396e187, 8a74b2ee22fe50fafb7416c29a96830a281af0e2; cause: unknown; actionable evidence: unknown. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-466 (Exclude remote queue time and controller checkouts from idle timeouts) in run 20260909T095234Z-revise

- Declined review improvement: Add optional UI scope mapping for src/garden/web/pages/api.py. — The changed endpoint only updates remote-run lifecycle metadata and has no rendered UI behavior; focused API tests are the proportionate coverage.

### 2026-09-09 · reported by CG-411 (Adopt an existing PR with its verified branch and revision identity) in run 20260909T094734Z-revise

- The supervised full pytest attempt exited 1 after its nested validation-admission scenario waited behind the outer one-slot validation lease; no passing full-suite receipt was produced.

### 2026-09-09 · reported by CG-414 (Assign owners to tasks and phases and filter work by owner) in run 20260909T100332Z-revise

- Declined review improvement: Add an optional UI scope mapping. — The reviewer provided no concrete correctness gap, and the ownership UI already has focused rendered tests; no code change is warranted.

### 2026-09-09 · owner-requested Inbox category audit; operator loop

- Inbox recovery categories still surface routine operator work as human decisions (2026-09-09 RC10 sweep): CG406 and CG437 had remote checks time out without a result while their exact current PR heads each had two successful GitHub test runs; the operator resumed the check path without reimplementing source. By contrast CG434 had a current CI failure and a substantive validation-bypass finding and needed an existing-source correction. A generic check-could-not-run prompt does not distinguish these cases. Route interrupted checks, normal CI/review waiting, base-health investigation and bounded revision-cap diagnosis to the operator loop, preserving real failures and explicit holds. Ask the owner only for a concrete unresolved product/scope/budget/access decision. Continue auditing policy-only or stale review feedback before author redispatch. Existing prevention work CG428/CG438/CG466 (transport, review recovery, idle accounting), CG437 (troubled-task investigation), and RC9/RC10 review policy should be reconciled before creating another implementation task. This is a fresh incident/category report, not proof those native fixes are all deployed or that any still-open PR is merged. Evidence: /home/joshua/work/operator-test-tmp/input-sweep.json and the September9 operator sweep dispositions.

### 2026-09-09 · terminal check recovery repeats after plain resume

- CG406 (`20260909T025423Z-check`), CG437 (`20260909T033806Z-check`) and CG434
  (`20260909T044820Z-check`) each retained a collected terminal `check_run` pointer after
  `garden resume` cleared the human stop. The next terminal audit recreated the same
  `check_did_not_run` card. The supported two-command recovery (`garden recover-check`,
  then resume or retry) worked, but the card's primary resume action did not make the
  recovery durable. CG406 and CG437 had fresh exact-head GitHub CI success and required no
  implementation retry; CG434 retained a real current CI failure and substantive review
  feedback and correctly continued its existing branch. CG471 owns one guarded atomic
  recovery action that preserves run/source evidence, retains live or newer pointers, and
  cannot recreate the same stop on the next tick.

### 2026-09-09 · asynchronous CI replaced the full review supplied to a worker

- CG438 review `20260909T095747Z-review` recorded the precise blocking
  environment-error recovery finding and six failing focused tests. Revise run
  `20260909T095937Z-revise` received only a generic CI failure and GitHub authentication
  error in its `Review feedback to address`; the environment-error finding was absent.
  The worker fixed the six tests, and review `20260909T101945Z-review` rediscovered the
  omitted finding and triggered a repeated-finding stall. Installed RC10
  `_after_ci_check` can finish after review and replace `pending_feedback` through
  `_apply_feedback`. CG474 owns provenance-aware merging of concurrent CI and review
  feedback so the next worker receives the complete applicable record without reviving
  stale, superseded or resolved findings.

### 2026-09-09 · reported by CG-413 (Use product-specific execution timeouts and weighted resource admission) in run 20260909T110520Z-revise-2

- Declined review improvement: Add optional UI scope mapping for src/garden/web/pages/api.py. — The change affects JSON worker protocol behavior only and introduces no rendered UI behavior; the frozen validation plan likewise identifies no visual pages.

### 2026-09-09 · review loop for CG-413 (Use product-specific execution timeouts and weighted resource admission)

- Review loop: 4 rounds, $8.16 cumulative work/revise/review cost; head lineage 2989a95e0fbd598b397ad1101b5cb2f3c151560c, f2eb2e94751d2fe80eb39e1975c72e8f968edd1a, f4c5092d4b048dc011be12220433d7074db7826a, 8f51303d059d5cdc32b88e8afe2879645f9ad67d; cause: unknown; actionable evidence: Weighted admission and product-specific budgets otherwise pass focused verification, but legacy remote check runs incorrectly receive a product execution timeout.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-468 (Avoid nested validation admission deadlock during supervised full suites) in run 20260909T113040Z-work

- No type-check command is configured in pyproject tooling.

### 2026-09-09 · reported by CG-473 (Reserve a task in Manual mode from automatic actions) in run 20260909T113958Z-revise

- Declined review improvement: Add optional UI scope mappings for the previously changed web files. — The reviewer identified metadata omission rather than a rendered defect; this revision changes scheduler lifecycle behavior only and the existing UI remains unchanged.

### 2026-09-09 · reported by CG-473 (Reserve a task in Manual mode from automatic actions) in run 20260909T115540Z-revise

- Declined review improvement: Add optional UI scope mapping for the previously changed web files. — This revision makes no rendered UI change, and editing scheduler-owned task metadata is prohibited.

### 2026-09-09 · reported by CG-473 (Reserve a task in Manual mode from automatic actions) in run 20260909T120624Z-revise

- Declined review improvement: Add optional UI scope mapping for the previously changed web files. — This revision changes only scheduler trial behavior and regression tests; it introduces no rendered behavior requiring additional UI scope metadata.

### 2026-09-09 · reported by CG-473 (Reserve a task in Manual mode from automatic actions) in run 20260909T121815Z-revise

- Declined review improvement: Add optional UI scope mapping for previously changed web files. — This revision changes only the scheduler trial-entry guard and its regression coverage; it introduces no rendered behavior or new UI scope.

### 2026-09-09 · review loop for CG-473 (Reserve a task in Manual mode from automatic actions)

- Review loop: 4 rounds, $10.77 cumulative work/revise/review cost; head lineage 1adf43c2bb9170a897d7e627048c69babc35c299, 322db8b52c361cfc9e7aa70d1aaec8b842b3e864, c6db17d530fcaa10022f8e36631ad4cd29068cf5, 8e5e362f4634a7302b60c4f3a487578dfb42ad0a; cause: unknown; actionable evidence: Manual-mode lifecycle parking works in the tested paths, but starting a replacement model trial can still mutate a reserved task.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-475 (Refresh open PR conflicts, checks, and review comments) in run 20260909T122218Z-revise

- Declined review improvement: Add optional UI scope mapping for src/garden/web/templates/_prs.html. — The feedback identifies omitted review metadata but no concrete UI defect; Board PR rendering is already covered by focused tests and no additional source change is warranted.

### 2026-09-09 · reported by CG-396 (Use pluggable exact-head CI status for review and merge eligibility) in run 20260909T094731Z-revise

- GitHub CLI was installed but unauthenticated, preventing live PR comment and CI inspection.
- The supervised full suite conflicts with tests that start nested workers requiring the same host validation lease.
- Declined review improvement: Create another served interaction artifact replay. — The current owner policy makes prescribed replay artifacts advisory; the applicable served tests were attempted and their enclosing-lease timeout was reported without rerunning unchanged implementation.

### 2026-09-09 · reported by CG-473 (Reserve a task in Manual mode from automatic actions) in run 20260909T122740Z-revise

- Declined review improvement: Add optional UI scope mapping for touched web files. — The revision changes only hidden concurrency-guard data and no rendered appearance or interaction layout; the validation plan explicitly identifies no rendered behavior change.

### 2026-09-09 · reported by CG-475 (Refresh open PR conflicts, checks, and review comments) in run 20260909T123251Z-revise

- Declined review improvement: Add optional UI scope mapping for src/garden/web/templates/_prs.html. — No rendered behavior changed: the existing PR table already displays arbitrary check-state strings and mergeability values, so changing the template would add unnecessary scope.

### 2026-09-09 · operator / open PR CI status

Backlog-wide CI failures block delivery, while operator status understated the extent. The owner repeatedly reported that all CI seemed to be failing. The operator initially discussed only CG438, CG349 and CG475 and cited isolated green runs; a complete current-head sweep then found 19 open PRs: 11 with at least one failed check, 3 still running and only 5 passing. A passing check alongside a failed check is still blocked. Routing feedback or registering features is not the same as repairing CI or delivering a merge.

Expected: report the entire open-PR denominator and current-head passing/running/failing counts up front; distinguish shared regressions from branch-specific failures and superseded runs; preserve precise failure logs and all open PR/reviewer feedback in the actual author brief; track each blocker through a correction, passing current-head CI and normal reviewed serial merge. Expose stalled CI repairs and their concrete next action instead of repeatedly reassuring from a few successful examples. Do not bypass real CI failures or claim fixes merely from queued work.

Existing related work: CG474 feedback preservation is deployed in RC11; CG475 owns PR-wide observation and its canary adapter failure; CG438 owns review recovery and the remaining quota-transition failures; CG349 owns its branch corrections; CG477 adds user-triggered investigations and reports. Reuse these tasks rather than duplicate their code fixes. Evidence: /home/joshua/work/operator-test-tmp/current-pr-ci-status.json, current-ci-routing-20260909T1215.json and cg438-quota-ci-routing-20260909T1232.json. Snapshot counts are from the September 9 approximately12:37UTC inspection, not a claim that later heads remain unchanged.

### 2026-09-09 · reported by CG-477 (Run user-triggered local deep dives with published reports and follow-up fixes) in run 20260909T122501Z-work

- CG-437 was not present on the dispatched base branch, so its completed lifecycle commits had to be integrated before extending them.

### 2026-09-09 · reported by CG-473 (Reserve a task in Manual mode from automatic actions) in run 20260909T124341Z-revise

- An initial broader focused-test command named a nonexistent tests/scheduler/test_trials.py and exited before collection; the corrected 297-test selection completed successfully.
- Declined review improvement: Add optional UI scope mapping for the listed web files. — This revision changes no rendered behavior; the existing Manual controls are unchanged and their functional web coverage passed.

### 2026-09-09 · reported by CG-413 (Use product-specific execution timeouts and weighted resource admission) in run 20260909T124457Z-revise

- GitHub CLI had no credentials, so open comments and status checks could not be queried; git ls-remote confirmed PR #324 still points to 371accd65 pending controller publication.
- Declined review improvement: Add optional UI scope mapping for src/garden/web/pages/api.py. — The endpoint payload behavior changed without rendered UI behavior; the frozen validation plan likewise identifies no visual paths or interaction requirement.

### 2026-09-09 · Inbox / CG-230

CG230 Inbox presents an unclear infrastructure-recovery prompt as a user decision. It says "check did not run ... idle21min; retry also failed; needs human" and offers "Nothing to fix, resume", "Continue the loop", Discuss and Cancel. The underlying problem is an interrupted automatic pre-PR lint check, while the actual PR222 is also draft, conflicting and failing two CI tests. The card simultaneously cites an older review source06a910 while the actual PR head is073057. The user explicitly reported that the prompt is not clear.

Expected: explain what operation failed in plain language, why it stopped, whether the evidence applies to the current head, what work/results are preserved, who owns recovery, and exactly what the recommended action will do. Distinguish check-infrastructure recovery from actual source/CI/conflict findings and genuine product decisions. Do not ask the user to assert "Nothing to fix" while unrelated failures remain, or imply a generic continuation fixes the prerequisite. Route ordinary known recovery to the operator/agent with visible progress; only ask the user for a real unresolved decision. Reuse CG471 atomic check recovery and CG477 investigation flows; preserve all failure/source records. Evidence: /home/joshua/work/operator-test-tmp/cg230-inbox-20260909 (rendered card, state, fresh PR snapshot).

### 2026-09-09 · reported by CG-475 (Refresh open PR conflicts, checks, and review comments) in run 20260909T124341Z-revise-2

- Declined review improvement: Add optional UI scope mapping for src/garden/web/templates/_prs.html. — This revision changes scheduler migration and GitHub REST pagination only; rendered behavior and template scope did not change, so additional UI mapping would not verify either defect.

### 2026-09-09 · review loop for CG-475 (Refresh open PR conflicts, checks, and review comments)

- Review loop: 4 rounds, $7.44 cumulative work/revise/review cost; head lineage c51f8ef978030938577c27ee5b9470a5c2e1e097, 67ccdf0970fa103783d34c245c9b2d4a33bb4356, 99045a5692236a9fa3cbd1f4f5d85ccf04548417, e1a09dcf822c3ac5f13e2b9527a61d77277029a5; cause: unknown; actionable evidence: The shared scheduler observation flow is coherent, but initial feedback migration and REST check pagination can cause incorrect actions or status.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-473 (Reserve a task in Manual mode from automatic actions) in run 20260909T125941Z-revise

- Declined review improvement: Add optional UI scope mapping for the listed web files. — This revision changes only the hidden lifecycle guard value and adds no rendered appearance or layout behavior; additional visual-scope metadata would not improve the functional fix.

### 2026-09-09 · reported by CG-475 (Refresh open PR conflicts, checks, and review comments) in run 20260909T132910Z-revise-2

- Declined review improvement: Optional UI scope mapping for `src/garden/web/templates/_prs.html` — The fix only changes scheduler fetch coordination and has no rendered behavior or template change to map.

### 2026-09-09 · reported by CG-477 (Run user-triggered local deep dives with published reports and follow-up fixes) in run 20260909T132041Z-revise

- Declined review improvement: Optional UI scope mapping for touched web files — No concrete usability or rendering defect was identified; focused web tests cover both affected entry points and report routes.

### 2026-09-09 · reported by CG-478 (Allow non-draft tasks to move into frozen phases) in run 20260909T133818Z-revise

- Declined review improvement: Add an optional UI scope mapping for the existing task-page/template changes. — This revision changes scheduler behavior and tests only; the existing UI behavior is already covered by the focused move test.

### 2026-09-09 · operator / merge hold

An operator automerge hold can outlive its repair and silently block an otherwise approved, green PR. CG464 retained task.extra.automerge=false after the recorded exact-source lineage correction, CI and independent-review restoration gates were met. The relevant field is Task.extra, not scheduler state. Surface hold ownership, reason, release conditions and current condition evidence; re-evaluate due holds during operator sweeps, preserving all fresh head/CI/review guards. Root restored the original absent setting on afd16e1b at13:50:49 without manually merging. Reuse CG480 recovery-ownership clarity and the existing merge policy rather than inventing a new merger. Receipt: clean-head-merge-policy-20260909/cg464-automerge-hold-restored.json.

### 2026-09-09 · reported by CG-396 (Use pluggable exact-head CI status for review and merge eligibility) in run 20260909T132742Z-revise

- No project typecheck command or mypy/pyright configuration is present, so no separate type checker could be run.
- Declined review improvement: Add optional UI scope mapping for src/garden/web/pages/api.py and src/garden/web/templates/task.html. — This revision changes receipt-policy lookup and status semantics without changing rendered layout or appearance; existing web behavior tests passed.

### 2026-09-09 · review loop for CG-396 (Use pluggable exact-head CI status for review and merge eligibility)

- Review loop: 4 rounds, $31.48 cumulative work/revise/review cost; head lineage 1a446e1da7ee75d24c2633e5caa3063bb620a3d0, e8097dd1caf940422271eb6bbddc3d2e18145de3, 990d5a14d9a4f6363aedd8b977e32e76379f6996, 6bde29916b413bad90242a4f40b3bfd96f95dd2f; cause: unknown; actionable evidence: The exact-head foundation works in focused tests, but GitHub status-context compatibility and per-product validation-policy integration remain incomplete.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-475 (Refresh open PR conflicts, checks, and review comments) in run 20260909T134619Z-revise

- Declined review improvement: Add optional UI scope mapping for `src/garden/web/templates/_prs.html`. — This revision changes only REST error propagation and adds no rendered behavior; the existing PR view already displays repository refresh errors and stale timestamps.

### 2026-09-09 · reported by CG-477 (Run user-triggered local deep dives with published reports and follow-up fixes) in run 20260909T140120Z-revise

- Declined review improvement: Optional UI scope mapping for previously changed web files — This revision changes scheduler handoff state and worker brief composition only; it introduces no rendered UI behavior, so screenshots or additional UI mapping would not verify the corrected defect.

### 2026-09-09 · reported by CG-475 (Refresh open PR conflicts, checks, and review comments) in run 20260909T140533Z-revise

- GitHub exposed failing job and step metadata publicly but required authentication for job logs; the supervised local full suite provided the exact failing node.

### 2026-09-09 · review loop for CG-471 (Make stale check recovery one guarded atomic action)

- Review loop: 4 rounds, $4.55 cumulative work/revise/review cost; head lineage 340c83664ae9605ed9ce09117cf74a139d1dede8, 8e7d1edf9c594149bf82c64266f6993bf69cff0b, 39a5ad772f5d01c830a0cc66e68eadfd8842fe70, b9331e7c68af3dbb74b9beeb7c8dd66c14286344; cause: unknown; actionable evidence: The guarded recovery correctly reconciles matching terminal check state, preserves newer or live continuations, and selects pipeline resume versus existing-branch revision from durable actionable evidence.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-466 (Exclude remote queue time and controller checkouts from idle timeouts) in run 20260909T143132Z-revise

- The supervised full-suite output stream detached from the tool session after partial progress; the durable supervisor record reported finished with exit_code 0.
- Declined review improvement: Add optional UI scope mapping for src/garden/web/pages/api.py. — The changed API path controls remote claim/deadline accounting and does not alter rendered UI behavior; the frozen validation plan likewise identifies no rendered scope.

### 2026-09-09 · reported by CG-473 (Reserve a task in Manual mode from automatic actions) in run 20260909T145454Z-revise

- Declined review improvement: Add optional UI scope mappings for the listed web files. — The note concerns reviewer-output metadata and identifies no rendered defect; the frozen validation plan explicitly records that no rendered behavior changed.

### 2026-09-09 · reported by CG-470 (Add an origin-aware back control to task detail) in run 20260909T144414Z-revise

- Declined review improvement: Add an additional UI scope mapping artifact for the task detail files. — The existing focused page module, template, and shared styling already form the minimal direct mapping; no concrete product defect or missing behavior was identified.

### 2026-09-09 · reported by CG-475 (Refresh open PR conflicts, checks, and review comments) in run 20260909T150244Z-revise

- Declined review improvement: Add optional UI scope mapping for src/garden/web/templates/_prs.html. — This revision changes only REST data acquisition and no rendered behavior or template; the frozen validation plan likewise identifies no visual paths.

### 2026-09-09 · reported by CG-478 (Allow non-draft tasks to move into frozen phases) in run 20260909T150415Z-revise

- Declined review improvement: Optional UI scope mapping for existing task-page files. — This revision changes only scheduler behavior and a backend regression test; it introduces no UI diff.

### 2026-09-09 · review loop for CG-477 (Run user-triggered local deep dives with published reports and follow-up fixes)

- Review loop: 4 rounds, $14.24 cumulative work/revise/review cost; head lineage 17ebd23c087b7cf99d789bde76cf5d0283f56937, cade24927471a5e1db2a30a888394b9e7fafabbe, 90fce86c35d0292c0d27f091a27589b19e4a1966, 9dca73b456d18c7a4052239e704f64b30916f290; cause: unknown; actionable evidence: Deep dives now satisfy the requested local investigation, durable reporting/publication, complete PR-feedback capture, and corrective-work handoff, including the previously missing dispatch-time refresh.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-478 (Allow non-draft tasks to move into frozen phases) in run 20260909T152111Z-revise

- Declined review improvement: Add a separate UI scope mapping artifact. — The small conditional template change is directly covered by the task-page regression; no separate mapping is used by this project.

### 2026-09-09 · reported by CG-475 (Refresh open PR conflicts, checks, and review comments) in run 20260909T153017Z-revise

- Declined review improvement: Optional UI scope mapping for src/garden/web/templates/_prs.html — This revision changes REST data acquisition only; rendered behavior and template scope did not change, matching the head-bound validation plan's no-rendered-evidence assessment.

### 2026-09-09 · reported by CG-478 (Allow non-draft tasks to move into frozen phases) in run 20260909T154503Z-revise

- Declined review improvement: Optional UI scope mapping — The small conditional task-page control change is directly covered by the held-page regression; no separate mapping artifact is needed.

### 2026-09-09 · review loop for CG-478 (Allow non-draft tasks to move into frozen phases)

- Review loop: 4 rounds, $4.40 cumulative work/revise/review cost; head lineage 0f2f6086868360698cedfb16fa267b91dd872040, a1d639e35c99964f097ecab59fa5a93ab24ff916, ac83b360580d0d4573ee8794a104f173f028d682, 0059eab3a53bdb65fae8f8bd9417269e4e5f3304; cause: unknown; actionable evidence: Moving and the covered freeze gates work, but frozen tasks can still enter the model-trial reset path, which mutates durable lifecycle state before dispatch is refused.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-478 (Allow non-draft tasks to move into frozen phases) in run 20260909T161627Z-revise

- Declined review improvement: Expand UI mapping for task page/template. — Existing frozen-hold UI already shows preserved status and reason and hides review controls; this lifecycle-only fix needs no UI change.

### 2026-09-09 · reported by CG-478 (Allow non-draft tasks to move into frozen phases) in run 20260909T162740Z-revise

- Declined review improvement: Add a separate UI scope mapping artifact. — The review described it as optional; the minimal correct scope is already evident in the task page, template, and focused regression.

### 2026-09-09 · review loop for CG-411 (Adopt an existing PR with its verified branch and revision identity)

- Review loop: 4 rounds, $8.49 cumulative work/revise/review cost; head lineage 1ac5d0ef9bcf696fa0e883c4416db5d1e6702162, 9a3f4ae12a440b32212de8e70ba3cea6aee4b926, becfa58771126007e49e319ec7552b90374ec578, 4551f1f5735759b7059866241335b1b7320e90e9; cause: unknown; actionable evidence: PR identity handling is mostly sound, but current-head focused validation exposes two blocking lifecycle defects. Rejected incomplete metadata can persist a replacement identity, and external head movement fails the newly added regression.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-396 (Use pluggable exact-head CI status for review and merge eligibility) in run 20260909T175522Z-revise

- GitHub CLI was unauthenticated, so current PR comments and CI could not be queried live from this worker.
- Declined review improvement: Add optional UI scope mapping for src/garden/web/pages/api.py and src/garden/web/templates/task.html. — This revision changes only backend receipt selection and tests; no rendered behavior changed, and existing scoped task-page captures already cover the branch's visual change.

### 2026-09-09 · reported by CG-411 (Adopt an existing PR with its verified branch and revision identity) in run 20260909T185516Z-revise

- The listed enterprise remote environments specification did not resolve, as noted in the brief.

### 2026-09-10 · reported by CG-498 (Clean up worker branches when they are no longer needed) in run 20260910T030114Z-work

- The prescribed test command initially named a nonexistent tests/test_config.py; reran the applicable test_gitops.py and cleanup selections instead.

### 2026-09-10 · reported by CG-498 (Clean up worker branches when they are no longer needed) in run 20260910T032904Z-revise

- The repository has no configured typecheck command, so no separate typecheck was run.

### 2026-09-10 · reported by CG-499 (Show worker status and current jobs in a Now tab and API) in run 20260910T042934Z-revise

- `git diff --check main...HEAD` reports trailing whitespace in unrelated historical replay artifacts inherited through the branch base; the revision-only diff is clean.

### 2026-09-10 · review loop for CG-499 (Show worker status and current jobs in a Now tab and API)

- Review loop: 4 rounds, $7.17 cumulative work/revise/review cost; head lineage 4ef84db757292723570eb174577207b30d1fbf3c, 90f78cc69c2a73644f3f7f82f43e55f42bf37c1f, 780aff39a26d6d767729c000cf324d2c363ce5e4, bd15d5de6c6d179c00c345be02323c02aca60964; cause: unknown; actionable evidence: The API and Now tab omit enrolled workers until their first successful contact, so an idle or unavailable enrolled fleet can disappear.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-506 (Return complete worker transcripts for server-side storage and analysis) in run 20260910T044022Z-work

- The first focused validation named a nonexistent tests/test_runs_page.py; it was corrected to tests/test_web.py and the valid selection passed.

### 2026-09-10 · reported by CG-501 (Diagnose worker disconnects and resets and make recovery resilient) in run 20260910T045851Z-revise

- The base branch diff contains historical generated HTML whitespace warnings unrelated to CG-501; current revision commits pass diff checking and Ruff.

### 2026-09-10 · reported by CG-347 (Recover EC2 Spot interruptions without losing accepted work or exceeding pool limits) in run 20260910T060107Z-revise

- An initially attempted focused-test command named a nonexistent `tests/test_host_acquisition.py`; it ran no tests and was replaced with the repository's actual host enrollment and registry test files.

### 2026-09-10 · reported by CG-501 (Diagnose worker disconnects and resets and make recovery resilient) in run 20260910T062652Z-revise

- Exact-head GitHub CI cannot run for an unpushed worker commit; local WSL policy assigns full CI to the controller merge gate.

### 2026-09-10 · review loop for CG-501 (Diagnose worker disconnects and resets and make recovery resilient)

- Review loop: 4 rounds, $11.88 cumulative work/revise/review cost; head lineage ea6076e115c02ead701af6fe8bd58d99c47754c3, 1e4b18f7b65b2dcadd6e04d26cc30ecdd145308f, d8c63cf3e39928bb3b77a8e8f1f577b525579a2a, 0de0db295a4d70c8653e1e9236409037c977e7e9; cause: unknown; actionable evidence: Managed model executions survive daemon replacement, but remote check executions do not persist an active-claim handoff and therefore cannot be recovered after a worker daemon restart.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · review loop for CG-347 (Recover EC2 Spot interruptions without losing accepted work or exceeding pool limits)

- Review loop: 4 rounds, $8.70 cumulative work/revise/review cost; head lineage 198bf04b9d3e2366f2baddc71d6578a06302107f, a62fef1167fdbb894f5dce8a47ea5af9686bec79, 4947aa0490efb09bb32f601dc361b35223c67dbe, 0196f671e0dc3b835e304e8b9460836fd4ad1655; cause: unknown; actionable evidence: Spot recovery behavior passes focused tests, but the production CLI still permits Spot provisioning with interruption handling disconnected.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-348 (Make EC2 pool cost health draining and teardown understandable and verifiable) in run 20260910T110733Z-revise

- No type-checker is configured in pyproject.toml; `.venv/bin/python -m mypy --version` reports that mypy is not installed.

### 2026-09-10 · review loop for CG-506 (Return complete worker transcripts for server-side storage and analysis)

- Review loop: 4 rounds, $9.83 cumulative work/revise/review cost; head lineage 723dd2bfe297bf67492928a436b7a78e3d3001b6, a7f0adf790e6bb52ce8187a75913f06c27a96609, 2dca1088065c6d7f66491364cd6ac18f4ce6230b, 665f27ddc0a6032717ed521e845bc3d1f50069fc; cause: unknown; actionable evidence: Transcript upload works in ordinary execution, but restart recovery and superseded-attempt retrieval remain incomplete.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-503 (Find removable and overengineered code to simplify and optimize) in run 20260910T111342Z-work

- The documented web benchmark accepts zero runs but always requests a hard-coded run route, producing a 404; the audit records a focused repair.

### 2026-09-10 · reported by CG-505 (Audit and update all Garden specifications) in run 20260910T112934Z-work

- The configured Garden workspace commit predates several visible specification files, so the audit records both the commit and the newer dispatch-visible workspace source instead of attributing all files to that revision.
- Ruby was unavailable for link validation; the equivalent read-only scan ran successfully with Perl.

### 2026-09-10 · reported by CG-505 (Audit and update all Garden specifications) in run 20260910T115405Z-revise

- The brief's referenced phase-07 specification was unavailable in the product checkout and had to be inspected through the configured read-only Garden workspace.

### 2026-09-10 · reported by CG-510 (Consolidate duplicated canary composition tests) in run 20260910T115229Z-work

- No type-checker is configured in the project virtual environment.

### 2026-09-10 · reported by CG-523 (Make web benchmark size controls internally consistent) in run 20260910T125527Z-work

- No repository-configured or installed type-checker was available for the requested typecheck step.

### 2026-09-10 · reported by CG-513 (Show only relevant unique design files for each pull request) in run 20260910T133113Z-revise

- A broader tests/test_web.py run exited 1 at unrelated test_read_generation_skips_discovery_fingerprints_until_a_watch_event; the focused changed behavior passed.

### 2026-09-10 · reported by CG-514 (Never require a second review solely by count) in run 20260910T133843Z-revise-2

- The initially named tests/test_config.py path did not exist; corrected to tests/test_configuration.py before running the intended suite.

### 2026-09-10 · reported by CG-527 (Clean up abandoned worker branches, worktrees and temporary files) in run 20260910T134031Z-work

- The branch base differs substantially from the current local `main`, so repository-wide `main...HEAD` whitespace checks include unrelated historical artifacts; the two task commits themselves pass `git diff --check`.

### 2026-09-10 · review loop for CG-513 (Show only relevant unique design files for each pull request)

- Review loop: 4 rounds, $3.41 cumulative work/revise/review cost; head lineage ed5cd00c4be89d3d059b62a6e942304e5826ba85, 6d1bc557c2d6efcdb31ff1766e139e95cb3cb6fb, 2f335efd25b845f07a96f72f28129e710e654edf, b63671ca1e1482ddd5088e573d842084cbcf8f0c; cause: unknown; actionable evidence: PR-scoped design output correctly handles refreshed refs, stacked bases, deduplication, deletions, shared references, and pure renames.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging) in run 20260910T135010Z-work

- The prescribed adjacent check-run test path did not exist; the applicable scheduler, setup, runner, review, rebase, retro, and web suites were used instead.
- PowerShell interop was unavailable in this WSL worker, so real Windows backing-volume validation could not run.

### 2026-09-10 · reported by CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging) in run 20260910T142745Z-revise

- The two context-garden reading-list paths were not present in this product checkout; equivalent product and phase context was supplied inline in the brief.

### 2026-09-10 · reported by CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging) in run 20260910T143624Z-revise

- The brief listed context-garden/product.md and context-garden/phase-07/goals.md, but those paths are absent from this product checkout.

### 2026-09-10 · reported by CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging) in run 20260910T151721Z-revise

- The listed context-garden/product.md and context-garden/phase-07/goals.md paths were absent from this product checkout; their content was embedded in the supplied brief.

### 2026-09-10 · review loop for CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging)

- Review loop: 4 rounds, $11.62 cumulative work/revise/review cost; head lineage 06271bb2401a02fb8462db62ed77254249c7554d, fc7d91e8a1bddc0ab9f9002560e7b36ffb0d4b8a, d0ccaa4f1ee480f4bae2149d2b4d48c16595a0ee, 3032d885ab7a0a8f9474ae01763bebf339f7503e; cause: unknown; actionable evidence: Checkout staging and reservation accounting are improved, but runtime/probe scratch and setup still perform or permit writes after the last reserve check.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-526 (Complete objective failure-trigger model escalation) in run 20260910T153156Z-work

- Focused pytest collection is blocked at import time by an existing garden.runs/garden.hosts.drain circular dependency.

### 2026-09-10 · reported by CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging) in run 20260910T161734Z-revise

- The brief-required context-garden/product.md and context-garden/phase-07/goals.md paths were absent from this product checkout.

### 2026-09-10 · reported by CG-529 (Automatically start the phase closing review when prerequisites are met) in run 20260910T162811Z-revise

- The local main ref was stale and divergent; the branch was correctly rebased onto accepted origin/main instead.

### 2026-09-10 · reported by CG-501 (Diagnose worker disconnects and resets and make recovery resilient) in run 20260910T170409Z-revise

- `git diff --check main...HEAD` reports historical trailing whitespace in pre-existing committed validation replay HTML; the current revision itself passes `git diff --check HEAD^..HEAD`.

### 2026-09-10 · reported by CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging) in run 20260910T170526Z-revise

- The listed context-garden/product.md and context-garden/phase-07/goals.md paths do not exist in this product checkout; their relevant contents were supplied inline in the task brief.
- The initially suggested persona test filename did not exist; validation was rerun using the actual persona consumer suites.

### 2026-09-10 · review loop for CG-526 (Complete objective failure-trigger model escalation)

- Review loop: 4 rounds, $10.72 cumulative work/revise/review cost; head lineage b9bf6988642af7b748aea124d295d46b4865e8d0, 1b9a3cb336526ad450c02a8a9c9efd61239b8f2a, 5049f2791f55158d1fca6093fec035bbf5b0f77c, 517b1a076f43b4ce648cf4a98540733263ceb405; cause: unknown; actionable evidence: Automated-review escalation treats every blocking finding as an implementation failure, including infrastructure or unavailable-evidence blockers that the task explicitly excludes.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-597 (Keep pending CI from starting author revisions) in run 20260910T190141Z-revise

- Hosted `actions` diagnostics could not query GitHub because the worker intentionally has no GH_TOKEN or authenticated gh session.

### 2026-09-10 · reported by CG-529 (Automatically start the phase closing review when prerequisites are met) in run 20260910T184716Z-revise-2

- The supervised full ordinary suite exceeded its 900-second deadline at 98%; its streamed output showed one failure but pytest did not emit the failing node or summary before termination.

### 2026-09-10 · reported by CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging) in run 20260910T194219Z-revise

- The listed context-garden/product.md and context-garden/phase-07/goals.md paths were absent from this product worktree; the equivalent product and phase material was supplied inline in the brief.

### 2026-09-10 · reported by CG-528 (Enforce a 20 GiB physical-disk reserve before local work and staging) in run 20260910T195936Z-revise-2

- The brief-listed context-garden/product.md and context-garden/phase-07/goals.md are not present in this product checkout.

### 2026-09-10 · review loop for CG-529 (Automatically start the phase closing review when prerequisites are met)

- Review loop: 4 rounds, $15.83 cumulative work/revise/review cost; head lineage 05187d8cdee814f9e014e7ccdc663ed32386539b, f16c09850ec5e515289df2ef944456effa4aae6c, f9d7f32e0d638e88fd4ea27dd3cf9a15793524b5, 4f09530e9717a7a0bb0aae0715a2b3e3a584da4b; cause: unknown; actionable evidence: The durable initial preparation handoff works, but expensive closing-review work still occurs under the controller lock on later ticks.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-526 (Complete objective failure-trigger model escalation) in run 20260910T204728Z-revise-2

- One broader focused-test command initially named nonexistent test files; it collected no tests and was immediately replaced with the repository's actual review/scheduler test paths.

### 2026-09-10 · review loop for CG-586 (Configure sequential phase execution, one phase at a time)

- Review loop: 4 rounds, $10.76 cumulative work/revise/review cost; head lineage afd806449a25cbb067e200202158e9aa26dca227, 3507a5b8005db960792a7201b626c1dfede773ea, 7e3afc7f5998329968d97db3278927a8655c823e, 328b8a4c89a3f72e2b6be0ef4b8476e2b53673de, de150a7f65d7f4e92263c32e3b9e17e2cb0aa250; cause: unknown; actionable evidence: Sequential phase gating is broadly implemented, but fresh investigation-agent runs can still start for a later, non-selected phase.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · review loop for CG-583 (Archive and deduplicate run history without losing recovery or accounting)

- Review loop: 4 rounds, $15.86 cumulative work/revise/review cost; head lineage 282715ff44123d225badf1856b96ae3111bf204e, 6be835f465d9b5548d06343ca051c8964a41c319, c608de33b03c58a59b7b1de5f57df58457fdd194, e6e585d22e970d98ca4816ac5ae72115660813e5, 6ec72e8ff0994cff61a197b8a89a38ee7b976717; cause: unknown; actionable evidence: Run archival can clear its recovery marker before the rebuilt history index is durably committed, allowing a crash to silently omit moved runs from history and accounting.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-11 · reported by CG-529 (Automatically start the phase closing review when prerequisites are met) in run 20260911T004511Z-revise

- The validation worker exports PYTEST_ADDOPTS, which leaks into a nested pytest subprocess and causes one shared full-suite failure.

### 2026-09-11 · reported by CG-616 (Make Playwright tasks and browser validation opt-in) in run 20260911T020917Z-revise

- GitHub Actions failure diagnostics were unavailable because the authenticated lookup failed; local deterministic tests covered the reported CI defects.

### 2026-09-11 · reported by CG-529 (Automatically start the phase closing review when prerequisites are met) in run 20260911T022733Z-revise

- The full ordinary suite has a pre-existing validation-policy failure: tests/test_validation.py::test_old_branch_can_explicitly_opt_in_to_known_stress expects an old-checkout stress opt-in subprocess to fail, but it exits successfully after deselecting stress tests.

### 2026-09-11 · review loop for CG-616 (Make Playwright tasks and browser validation opt-in)

- Review loop: 4 rounds, $9.05 cumulative work/revise/review cost; head lineage 07ac5a5fcf5ee458f59627117e5d868f0a42b780, 56c887657d7de724f70cb4758b36c3ce49203596, 1a7fefeca8b11e4d24897043fdaefb8f1e48eb0f, 543049dbc46599be2d4aa4db033e76fb0339ff20; cause: unknown; actionable evidence: The browser opt-in implementation satisfies the task in focused validation, but exact-head CI evidence is unavailable for the reviewed commit.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-11 · review loop for CG-412 (Resolve check commands analyzers and timeouts per product)

- Review loop: 4 rounds, $4.33 cumulative work/revise/review cost; head lineage 4bbc7572e6b6254763278309180aa959d62d5524, 87e4312ac1845880ee352f0b201b9d61b59f8776, 5f4040ab9f511c2dec65d915894678d65170d9ab, 99aa7bc3848a6c5f531c313cdba091e2c4fcd5d2; cause: unknown; actionable evidence: Product-specific pre-PR checks, CI analyzers, environments, and timeouts are resolved independently and persisted across continuations and configuration changes.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-11 · reported by CG-412 (Resolve check commands analyzers and timeouts per product) in run 20260911T103446Z-revise

- The referenced enterprise-remote-environments.md reading-list entry was unavailable, as noted in the brief.

### 2026-09-11 · reported by CG-626 (Update and simplify ontology documentation and related Markdown) in run 20260911T111816Z-work

- The system Python lacked the project Markdown dependency, so rendering validation used the prepared `.venv`; the project defines no typecheck command.

### 2026-09-11 · reported by CG-625 (Simplify overengineered code and remove redundant or obsolete code) in run 20260911T113938Z-work

- The first focused pytest command named a nonexistent `tests/test_personas.py`; it was corrected to the repository's actual kickoff/retro suites. No standalone typecheck command is configured in `pyproject.toml`, `docs/test-suites.md`, or `scripts/check_ci.py`.

### 2026-09-11 · reported by CG-492 (Automate safe live rollout of published versions to the worker fleet) in run 20260911T140430Z-work

- The repository has no configured static typecheck command; Python compilation and Ruff were run alongside the requested tests.

### 2026-09-11 · reported by CG-492 (Automate safe live rollout of published versions to the worker fleet) in run 20260911T142746Z-revise

- Exact-head GitHub CI remained external to this worker run; local focused validation and lint passed.

### 2026-09-11 · review loop for CG-492 (Automate safe live rollout of published versions to the worker fleet)

- Review loop: 4 rounds, $4.19 cumulative work/revise/review cost; head lineage 9c240016af230278a1ff1b8fa84931b5625c06bd, b4c4ce5f64f3001462276fc70b11841130619d9a, ea3ccb921f3d73d0c57daee918acf2a1b2ec9f35, 2c647c3ea2cff4c897fc8b95a53d917913d4fb36; cause: unknown; actionable evidence: Recovery replay is fixed, but activation verification can accept a runtime that was never staged or verified.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-11 · reported by CG-628 (Parallelize the ordinary test suite across separate CI jobs) in run 20260911T152747Z-resume

- The validation wrapper rejected the shard inventory helper because it indirectly invokes pytest; per policy, the repository helper was run directly and passed.
