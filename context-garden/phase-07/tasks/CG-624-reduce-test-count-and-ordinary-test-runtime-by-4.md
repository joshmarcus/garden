---
id: CG-624
title: Reduce test count and ordinary test runtime by 40%
status: cancelled
product: context-garden
phase: phase-07
depends_on:
- CG-364
- CG-453
- CG-502
priority: 2
difficulty: hard
reading:
- pyproject.toml
- tests/conftest.py
- scripts/check_ci.py
- .github/workflows/ci.yml
- docs/test-suites.md
branch: garden/cg-624-reduce-test-count-and-ordinary-test-runtime-by-4
runner: remote
discovered_from: 'owner: Task: cut tests and test runtime by 40%'
attempts: 1
last_dispatched_at: '2026-09-11T13:46:00+00:00'
created: '2026-09-11T11:12:48+00:00'
updated: '2026-09-11T14:02:02+00:00'
---

## Goal

Implement the owner's request: "Task: cut tests and test runtime by 40%". Reduce the retained test suite's genuine collected case count by at least 40%, and reduce ordinary full-suite execution wall time by at least 40% against a recorded current accepted-source baseline. This is implementation and measured reduction, building on completed cleanup and audit work.

## Existing work

Reuse CG-364 (redundant tests and fixture work), CG-453 (ordinary-suite runtime), CG-502 (validation-cost audit, PR419), and its merged follow-ups CG-509/510/511/512. Inspect their accepted changes and report before choosing new candidates; do not count their historical savings again. Preserve CG-616's explicit browser opt-in and the existing stress/load opt-in policy. This is Phase07 follow-through and is not an added Phase05 closing blocker.

## Acceptance criteria

- [ ] Before changing tests, freeze an exact accepted-source baseline and capture test inventories with parameterized cases expanded, the ordinary CI command, collected/executed/skipped/deselected counts, duration data and relevant fixture/setup costs. Record interpreter, dependencies, hardware/resource caps and cache conditions. Start from existing actual CI logs and the CG-502 audit; supplement with bounded measurements where comparability is missing. Report ordinary and opt-in inventories separately so moving tests between suites cannot masquerade as removal.
- [ ] Final genuine test case count is no more than 60% of baseline, accounting for any newly added cases. Remove obsolete, implementation-mirroring, tautological or redundant checks and consolidate repeated scenarios. Do not achieve the numerical target through blanket skips/xfails, broad deselection, moving unchanged cases to optional suites, hiding parameterized cases inside loops or simply reducing test discovery. Keep a concise removal/consolidation map identifying each protected behavior, its surviving coverage or the concrete reason it is obsolete/ineffective.
- [ ] Final ordinary full-suite wall time is no more than 60% of the comparable baseline. Measure serial cold and warm before/after runs under the same prepared dependencies, interpreter and resource caps; cold means empty pytest caches and test-created temporary state, warm means an immediate second run with unchanged dependencies. Report each condition, raw timings and percentage reduction, separating queue/admission wait and dependency installation from pytest execution. No extra CPUs, parallel suites or altered hardware may stand in for runtime savings. Use existing equivalent evidence where available and only repeat measurements to resolve a specific failure or uncertainty.
- [ ] Retain meaningful coverage of distinct supported behavior, especially authentication/authorization, data integrity, cross-process state races, deadline/resource enforcement, worker completion/recovery and exact-source CI/review/merge gates. Preserve distinct error and boundary cases with appropriately cheaper checks; line coverage or a smaller test count alone is not proof of equivalent regression value. Where a shared fixture or process boundary changes, use focused regression evidence that demonstrates the important failure is still detected. Do not add implementation-mirroring tests merely to replace deleted ones.
- [ ] Final retained ordinary suite passes through the actual repository CI command on the exact proposed head, with independent review and applicable lint. Publish a short reproducible before/after report with source identities, counts, timings, removal rationale and limitations, and update test-suite guidance. Both 40% targets are acceptance criteria: if either remains unmet, report the actual result and remaining gap rather than declaring completion. Use portable APIs/configurable paths and accurately report Linux, macOS and Windows-through-WSL validation, including untested environments.

## Execution scope

Use the normal remote runner on an existing restored worker and retain existing admission/validation limits. Profile and edit in the task's isolated checkout; retain original CI failures and active work. This request authorizes justified test removal and consolidation, superseding the older CG-364 no-arbitrary-count-target wording for this new task, while retaining substantive correctness and review requirements. It does not authorize additional cloud resources, deadline extensions, increased concurrency, production runtime edits or deletion of historical operational evidence. Keep unrelated owner holds intact.

## Log

- 2026-09-11T11:12:48+00:00 approved (owner request; delegated operator task approval)
- 2026-09-11T11:13:46+00:00 dispatched work run 20260911T111342Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~2670 tokens)
- 2026-09-11T11:22:09+00:00 worker asks: Should CG-624 resume on a host capable of completing the required current-head cold/warm baseline, or should the contract be amended to permit a historical/incomplete baseline? cost=$0.71
- 2026-09-11T11:41:43+00:00 dispatched resume run 20260911T114138Z-resume via local [codex model=gpt-5.6-sol] (fresh session, base main, ~2724 tokens)
- 2026-09-11T11:43:29+00:00 worker blocked: Recorded exact-source GitHub Actions run 34592989538: 2,876 passed, 4 skipped, 8 deselected in 602.68 seconds on Python 3.12.14. The required paired cold/warm denominator cannot be obtained without triggering a scoped hosted workflow, while this worker is forbidden to push; no test reduction was attempted without that denominator. cost=$0.44


## Operator continuation after restored capacity, 2026-09-11

The operator restored six equivalent RC21 Ubuntu/Python3.12 workers under the owner's new120USD cap and existing17:36:42UTC deadline. Continue on the normal remote runner using one of those already authorized workers and its unchanged3CPU/12GiB/swap0 cap. This replaces the previous local-only execution choice and the unavailable hosted-workflow plan; no additional host, concurrency or deadline is authorized.

The operator published your existing documentation-only progress fd185824 (including bc21a331) to the assigned task branch, without a force push. Preserve both original blocked results and the exact41ff4de3 inventory and hosted run34592989538. Obtain the missing COMPLETE current-baseline cold/warm pair on this restored worker, using the same prepared Python3.12 dependency lock, interpreter and resource caps for baseline and candidate. A separate disposable checkout at the exact41ff4de3 source is permitted; keep the active candidate checkout intact. Existing hosted602.68s and historicCG453 are context, not paired denominators. Keep both40percent targets and meaningful protected regression coverage; don't hide/deselect cases to meet the count. Record actual ambient PYTEST_ADDOPTS and execute the ordinary repository selection under the supported validation supervisor. If baseline again fails, diagnose the specific original result and preserve it; do not loop an unchanged stalled command or weaken correctness. No hosted workflow change or direct worker push is required: normal controller publication and exact-head CI/review follow the worker's final result. Complete before/after measurement and source changes in this assigned task; if a concrete external action is still needed, ask the controller explicitly with the prepared exact action.
- 2026-09-11T12:15:12+00:00 reset to ready by hand
- 2026-09-11T12:15:22+00:00 dispatched work run 20260911T121522Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2670 tokens)
- 2026-09-11T12:34:28+00:00 worker asks: Can the operator provide an authorized existing Linux/Python 3.12 validation environment where the exact `41ff4de3` ordinary suite can complete twice within the unchanged 900-second limit, then resume this task there for the paired baseline and candidate measurements? cost=$1.70
- 2026-09-11T13:16:38+00:00 dispatched resume run 20260911T131638Z-resume via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2670 tokens)
- 2026-09-11T13:19:46+00:00 worker asks: May the frozen criteria be amended to replace both 40% thresholds with implementing the four vetted CG-502 consolidations and reporting their actual count/runtime savings using bounded measurements available in this environment? cost=$0.44
- 2026-09-11T13:28:28+00:00 dispatched resume run 20260911T132828Z-resume via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2670 tokens)
- 2026-09-11T13:31:37+00:00 worker says won't do: The frozen 40% count target requires reducing 2,880 ordinary cases to 1,728. CG-502's four vetted consolidations are already incorporated in the frozen baseline, and an AST inspection found zero exact duplicate test bodies; deleting 1,152 distinct cases without product-level decisions about unsupported behavior would conflict with the criterion requiring meaningful coverage. cost=$0.46
- 2026-09-11T13:44:54+00:00 decision rejected by the person; revise run will follow: Delegated operator decision under the owner's September 11 instruction to review all human actions:
- 2026-09-11T13:46:00+00:00 dispatched revise run 20260911T134600Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~2742 tokens)
- 2026-09-11T13:50:58+00:00 worker blocked: Consolidated five behaviorally redundant Cartesian test matrices, reducing ordinary collection from 2,880 to 2,855 cases (0.87%) while retaining every distinct axis value. Focused tests passed 21/21, collection confirmed 2,855 ordinary and 2,863 expanded cases with 8 opt-in cases unchanged, and ruff plus diff checks passed; the 40% count and runtime targets remain unmet. cost=$0.76
- 2026-09-11T14:02:02+00:00 cancelled (web)
