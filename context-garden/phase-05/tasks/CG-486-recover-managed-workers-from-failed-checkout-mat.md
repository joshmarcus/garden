---
id: CG-486
title: Recover managed workers from failed checkout materialization
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
difficulty: hard
reading:
- src/garden/remote_worker.py
- src/garden/managed_worker.py
- tests/test_remote_worker.py
branch: codex/recover-worker-materialization
pr: https://github.com/joshmarcus/context-garden/pull/387
attempts: 2
last_dispatched_at: '2026-09-10T01:16:57+00:00'
created: '2026-09-09T15:18:32+00:00'
updated: '2026-09-10T01:37:22+00:00'
---

## Goal

Keep a managed worker alive when claim checkout or setup materialization fails, report the
claim-bound infrastructure outcome exactly once, and recover on a clean later generation
without losing unpublished source or allowing stale publication.

## Context

The September 9 remote no-process audit found four assigned claims stranded after
`execute_claim` raised from `git checkout`: two warm repositories retained unresolved or dirty
source, and two other checkout failures exited the managed daemon before `/finish`. Preserve
the dirty checkout, index, source and result artifacts for operator recovery. CG-428 owns HTTP
transport retry and is out of scope. Operational repair of live hosts is separately owned; do
not hotpatch or mutate them from this task.

## Acceptance criteria

- [ ] Checkout, fetch and setup/materialization exceptions cannot escape the managed claim
  loop. The worker posts one structured infrastructure failure for the exact lease generation,
  with useful stage/error evidence and no author harness launch.
- [ ] A dirty or unmerged warm per-task repository is preserved byte-for-byte for recovery.
  The failed generation uses a fresh isolated materialization path rather than reset, clean,
  stash, checkout-overwrite or deletion of unpublished work.
- [ ] Recovery is bounded and fenced: a later clean generation can execute successfully, while
  an expired/stale generation cannot push or finish authoritatively. Existing heartbeat and
  finish idempotency remain intact.
- [ ] Focused tests exercise actual dirty and unresolved-index checkout failures, prove no
  author launch, exactly one finish attempt for the failed generation, and eventual successful
  clean retry. Existing remote worker lifecycle and transport tests remain green.

## Out of scope

- HTTP/heartbeat/transcript/finish transport retry policy owned by CG-428.
- Live worker-host cleanup, daemon restart, or hotpatching.
- Discarding, resetting or publishing preserved unpublished worker source.

## Log

- 2026-09-09T15:18:39+00:00 dispatched work run 20260909T151838Z-work via local [codex model=gpt-5.6-sol] (fresh session, base main, ~17488 tokens)
- 2026-09-09T15:19:06+00:00 operator conversion to requested manual isolated implementation before author launch
- 2026-09-09T15:19:07+00:00 reserved for manual operator implementation in isolated fresh-main checkout
- 2026-09-09T15:19:17+00:00 holding for requested manual reservation while isolated checkout is created
- 2026-09-09T15:20:19+00:00 approved (cli)
- 2026-09-09T15:20:20+00:00 dispatched work run 20260909T152020Z-work via manual [human] (fresh session, base main, ~18150 tokens)
- 2026-09-09T15:49:56+00:00 external PR attached at codex/recover-worker-materialization; existing CI is PENDING
- 2026-09-09T16:00:20+00:00 automated review requested changes: Core recovery behavior is well tested, but some materialization failures can still terminate the managed daemon without a structured finish. cost=$0.77
- 2026-09-09T16:14:58+00:00 dispatched revise run 20260909T161458Z-revise via manual [human] (fresh session, base main, ~18936 tokens)
- 2026-09-09T16:26:08+00:00 external PR attached at codex/recover-worker-materialization; existing CI is SUCCESS
- 2026-09-09T16:31:42+00:00 automated review requested changes: Core checkout recovery and fencing work, but a supported pre-author materialization failure can still escape and terminate the managed daemon. cost=$0.57
- 2026-09-09T17:02:06+00:00 dispatched revise run 20260909T170204Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19142 tokens)
- 2026-09-09T17:07:24+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T17:08:46+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/387: Pre-author configuration and source-identity failures now become claim-scoped structured materialization outcomes without weakening lease fencing. Verified the complete remote-worker test module (64 passed) and Ruff lint; committed as c596ca745. cost=$0.80
- 2026-09-09T17:12:44+00:00 automated review requested changes: Recovery and lease fencing are well covered, but dirty repositories are not always preserved byte-for-byte. cost=$0.73
- 2026-09-09T17:36:48+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T17:59:16+00:00 dispatched revise run 20260909T175903Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19405 tokens)
- 2026-09-09T18:26:28+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T18:29:30+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/387: Prevented the warm-checkout preflight from modifying tracked dirty indexes by using Git's no-optional-locks mode, with regression coverage for tracked, untracked, and unresolved-index repositories. Verified commit 944d7879fd8c73e01a3d96436a0fb10045fdc8bf with all 65 remote-worker tests passing and Ruff clean. cost=$0.73
- 2026-09-09T18:50:55+00:00 automated review requested changes: Core checkout recovery passes, but repository-lock materialization errors still escape the managed claim loop without a structured finish. cost=$0.43
- 2026-09-09T20:07:52+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-09T20:13:03+00:00 dispatched revise run 20260909T201300Z-revise via local [codex model=gpt-5.6-sol] (fresh session, base main, ~19711 tokens)
- 2026-09-09T20:17:30+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-09T20:18:46+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/387: Repository-lock path creation, opening, contention, and acquisition failures are now converted into structured claim-scoped materialization outcomes without author launch. Verified commit 8c82373d1383c8c62c7847f566205f138d8390ae with all 68 remote-worker tests passing and Ruff clean. cost=$0.64
- 2026-09-09T20:21:11+00:00 automated review requested changes: Core recovery, preservation, retry, and lease-fencing tests pass, but preservation/quarantine filesystem failures can still escape the managed claim loop. cost=$0.34
- 2026-09-09T20:46:44+00:00 troubled task continued with 1 bounded revision(s) at hard
- 2026-09-10T00:59:23+00:00 re-enabled by hand; revise run will follow
- 2026-09-10T01:00:03+00:00 dispatched revise run 20260910T005959Z-revise-3 via local [codex model=gpt-5.6-sol] (fresh session, base main, ~20131 tokens)
- 2026-09-10T01:04:43+00:00 review pre-flight advisory: omitted optional items: A test or stated reason for every acceptance criterion, Lint is clean, No conflict markers remain, UI changes have 1280px and 390px captures, The PR description states the goal and outcome without process history, Every acceptance criterion is addressed by name
- 2026-09-10T01:06:12+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/387: Quarantine filesystem failures now remain inside the managed claim loop and produce one structured materialization outcome while preserving source at its original or partially quarantined location. Committed as 352a1c5e; all 70 remote-worker tests passed and project Ruff lint was clean. cost=$1.00
- 2026-09-10T01:08:48+00:00 automated review: approve — Managed claim materialization failures are contained, preserved, reported once, and retried without weakening lease fencing. cost=$0.59
- 2026-09-10T01:14:07+00:00 PR conflicts with main; rebase onto main conflicts (tests/test_remote_worker.py); a rebase agent will resolve it
- 2026-09-10T01:16:57+00:00 dispatched rebase run 20260910T011655Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~2554 tokens)
- 2026-09-10T01:19:18+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/387: Rebased CG-486 onto origin/main and resolved the test import conflict while preserving both sides. cost=$0.01
- 2026-09-10T01:21:56+00:00 automated review: approve — Managed checkout materialization failures are contained, preserved, reported as infrastructure errors, and safely retried with lease fencing intact. cost=$0.37
- 2026-09-10T01:34:50+00:00 hard-tier scratch-merge check passed; ready to merge once the queue reaches it
- 2026-09-10T01:37:22+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/387
