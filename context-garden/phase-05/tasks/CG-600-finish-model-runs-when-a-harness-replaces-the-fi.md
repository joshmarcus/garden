---
id: CG-600
title: Finish model runs when a harness replaces the final-output FIFO
status: done
product: context-garden
phase: phase-05
depends_on: []
kind: bug
priority: 0
difficulty: hard
reading:
- src/garden/run_supervisor.py
- src/garden/harness.py
- src/garden/remote_worker.py
- tests/test_runners.py
branch: garden/cg-600-finish-model-runs-when-a-harness-replaces-the-fi
pr: https://github.com/joshmarcus/context-garden/pull/478
runner: remote
discovered_from: CG-516
retro_blocking: true
attempts: 1
last_dispatched_at: '2026-09-10T23:44:13+00:00'
created: '2026-09-10T22:20:12+00:00'
updated: '2026-09-11T00:46:10+00:00'
---

## Goal

Finish supervised model runs safely when a harness writes its final message by replacing the requested output path. Preserve the original final text, usage/cost and actual process outcome, keep output redacted before durable publication, and bound every shutdown/drain path. Do not hotpatch installed runtimes.

## Reproduction

On exact RC19 70ae9179ae6e2af865aef5a8cecca90460328c4d, CG599 worker0 committed8df02641 and its model completed at21:56 with a valid GARDEN_RESULT in structured stdout,84focusedpasses and Ruff. At22:10 the only processes were managed daemon663248 and supervisor663773. The supervisor had no children, its main thread waited in futex_do_wait and final-reader thread663775 waited in wait_for_partner. .final.raw was a regular zero-byte file, final.md empty, and no exit_code existed. Original stdout remained171977bytes SHA24afe711caa77682bc840ee0c0b32058ca00ba3f89acc57f72a6a5cb71ac14c9; native Harness.parse recovered final/result and cost1.587848.

run_supervisor.py creates a FIFO, starts a blocking reader, then after the child and descendants exit opens the final path for writing if the reader remains alive and joins that thread without a deadline. An atomic replacement leaves the reader waiting on the original FIFO; the wake-up write opens/truncates the replacement file and cannot wake the old reader. Reproduce this deterministically with a fake child that atomically replaces the final path. This is separate from CG584 shared Run mutation and CG599 cleanup collection starvation.

Root preserved exact original output bytes and a source bundle, then killed ONLY the confirmed childless deadlocked supervisor at22:16:07. The existing daemon naturally submitted the original structured final, cost/usage and exact source at22:16:09, with the real interrupted exit retained. Do not fabricate an exit0, overwrite old raw/final bytes, duplicate the CG599 author, or classify the original supervision attempt as passed.

## Acceptance criteria

- [ ] A deterministic atomic-replacement final writer and an ordinary FIFO writer both finish without a stuck supervisor or lost/truncated final. Cover no final writer, empty output, a writer that fails, descendant-held output and bounded shutdown; do not rely on scheduling sleeps for the race.
- [ ] Use a transport compatible with the actual harness contract. For structured-output harnesses, their already-redacted stdout may provide the authoritative final. Do not pass a raw file target that silently bypasses the redaction boundary. Preserve parsing, usage/cost, errors, source identity and actual child return code for local and remote work/review/check paths.
- [ ] Remove unbounded final-reader/writer open and join behavior, preserve replacement bytes as evidence on failure, and retain pre-persistence authority redaction, protected output ownership, descendant containment, workload-identity cleanup and deadline enforcement. A missing final must remain an explicit result rather than hanging or inventing success.
- [ ] Run focused supervisor, harness, isolation and remote-result tests plus Ruff sequentially and obtain actual current-head CI and independent review. Use portable APIs/capability checks for Linux, macOS and Windows through WSL; report untested platforms accurately. Do not change cloud resources, credentials, deadlines, installed source or current work.

The root operator owns release and activation after this repair and CG599 are accepted. This new observed transport blocker belongs in CG537's existing closing account; do not create a duplicate verifier/persona run.

owner_request_key: rc19-final-fifo-replacement-deadlock-20260910

## Log

- 2026-09-10T22:20:12+00:00 approved (delegated operator: reproduced live final FIFO handoff deadlock)
- 2026-09-10T22:20:43+00:00 dispatched work run 20260910T222043Z-work via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~21922 tokens)


## Additional source evidence, 2026-09-10T22:23Z

A bounded disposable, non-model reproduction on exact RC19 finished in209ms/19.7MiB and proved inherited final-path routing is unsafe: an INNER run_supervisor with its own run_dir inherited GARDEN_RAW_FINAL_PATH/GARDEN_FINAL_PATH belonging to an OUTER dummy execution. The inner process exited0 after deleting the outer raw sentinel and creating an empty outer final. No live state, worker or real secret was touched. Receipt: operator-test-tmp/rc19-deploy-20260910/fifo-inheritance-repro/receipt.json (source assertion can be recreated without that operator-local file).

Source tests/test_runners.py _synthetic_child_env and _supervisor_test_env remove older execution fields but retain these new final-path fields. Several tests/test_remote_worker.py child launches also copy os.environ. run_supervisor consumes/unlinks the inherited paths without checking ownership against its current run_dir. This is a demonstrated additional route to replacing an enclosing supervisor's FIFO during nested tests. The exact writer responsible for the live replacement has not been established; do not present Codex atomic replacement as the proven live cause merely because that reproduction is useful.

Include an outer/inner execution regression: final routing must be scoped to the current owner/run, not inherited as mutation authority by descendants. Consider consuming/removing these supervisor-only control variables from child environments, validating ownership before opening/unlinking, and using the existing redacted structured final transport where appropriate. Preserve the generic replacement/writer/deadline cases already required. Do not weaken pre-persistence redaction or mutate original saved evidence.
- 2026-09-10T22:26:19+00:00 operator appended a disposable reproduction of inherited final routing; original replacement hypothesis retained with corrected scope
- 2026-09-10T22:50:28+00:00 discovered work filed: CG-601
- 2026-09-10T22:50:28+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T22:56:11+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T22:58:53+00:00 opened https://github.com/joshmarcus/context-garden/pull/478 (base main): Committed 6d529ebc: final output is drained without blocking, atomic replacements are safely collected and redacted, and structured Codex stdout is authoritative. Focused supervisor, harness, isolation, workload-identity, and remote-result coverage passed; Ruff passed. cost=$3.94
- 2026-09-10T23:01:34+00:00 triage: changes requested by hand: Independent source review of exact 6d529ebcc5301f6751d93476a0fd833d5ff86a45 finds one blocking residual: final routing s
- 2026-09-10T23:10:31+00:00 dispatched revise run 20260910T231031Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24142 tokens)
- 2026-09-10T23:19:45+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T23:23:58+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/478: Scoped final-output routing to the current supervisor, prevented inherited local/remote mutation authority, and bounded each FIFO drain call. On exact head 2bfef748, 167 focused supervisor/harness/isolation tests and 7 remote-result tests passed, and Ruff passed. cost=$1.11
- 2026-09-10T23:37:19+00:00 triage: changes requested by hand: Independent review of 2bfef748 confirms the inherited-owner correction and per-poll byte/time budgets are present; retai
- 2026-09-10T23:44:13+00:00 dispatched revise run 20260910T234412Z-revise via remote [codex model=gpt-5.6-sol] (fresh session, base main, ~24903 tokens)
- 2026-09-11T00:11:58+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-11T00:24:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/478: Committed 9945f1f2, making finalization drain to EOF within an overall byte/time budget while retaining replacement evidence on incomplete collection. All 287 focused supervisor, harness, isolation, workload-identity, and remote-worker tests passed, and Ruff passed; the single permitted full suite timed out at 90% under its required 900-second bound. cost=$2.27
- 2026-09-11T00:30:22+00:00 automated review: approve — The bounded nonblocking final-output transport resolves FIFO replacement deadlocks while preserving redaction, replacement evidence, structured Codex results, and actual process outcomes. cost=$0.47
- 2026-09-11T00:46:10+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/478
