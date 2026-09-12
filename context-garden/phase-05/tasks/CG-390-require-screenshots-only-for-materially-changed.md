---
id: CG-390
title: Require screenshots only for materially changed visual behavior
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 0
order: 7
difficulty: medium
reading: []
branch: garden/cg-390-require-screenshots-only-for-materially-changed
pr: https://github.com/joshmarcus/context-garden/pull/299
attempts: 1
last_dispatched_at: '2026-09-08T10:47:20+00:00'
created: '2026-09-07T18:08:12+00:00'
updated: '2026-09-08T11:02:10+00:00'
---

## Goal
Apply the owner policy: PRs do not universally require screenshots or design snapshots. Require visual evidence only for relevant visual changes, and keep functional evidence separate.

## Context
Owner explicitly clarified this after CG216 burned six revisions on captures. Installed review.validation_plan treats any web/app.py or web/common.py edit as shared visual chrome and fans out to every page; page-module paths imply visuals without inspecting the changed behavior. CG216 remote API/auth wiring required14pages/56PNGs despite nonvisual intent. CG377 is merged but its path-based classifier remains too broad. CG389 separately owns mixed-version capture CLI compatibility; do not duplicate it.

## Acceptance criteria
- Backend/API/auth, scheduler, test-only, documentation-only, and nonvisual shared-module edits can pass without screenshots; HTTP/CLI/functional evidence remains proportional to actual claims.
- For a materially visual change, name the changed visible behavior and require only affected pages/states. Shared styling uses representative affected consumers with expansion justified by distinct visual risk, not unconditional full inventory.
- Generated captures/design snapshot artifacts do not trigger new screenshot requirements. Current-head source equivalence can reuse unchanged visual evidence rather than create a self-referential evidence commit loop.
- Worker preflight, pre-PR checks, reviewer brief and mechanical gate consume the same scoped visual decision. Unknown paths require bounded inspection, not blanket screenshots or automatic exemption from functional tests.
- Focused regressions cover nonvisual web/app.py route/auth wiring, API-only, docs/capture artifacts, a single-page layout change, and shared visual styles. Record the chosen scope/reason and a bounded affected-page capture only for the visual example.

## Scope
Keep actual task-specific functional validation and ordinary review/CI. Do not weaken CG385 real reclaim proof. No live fault injection or active-branch edits.

## Log

- 2026-09-07T18:37:47+00:00 dispatched work run 20260907T183746Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~10282 tokens)
- 2026-09-07T19:07:17+00:00 preserved uncommitted worktree changes from run 20260907T183746Z-work outside the PR: `git stash apply b70c4cacaa09a4943626f9497e28a1a89c8fb9a0` in /home/joshua/work/worktrees/CG-390 (garden:CG-390:20260907T183746Z-work:reap)
- 2026-09-07T19:53:01+00:00 opened https://github.com/joshmarcus/context-garden/pull/299 (base main): Visual evidence is now scoped to declared rendered behavior rather than web-module paths, with representative shared-style captures and reusable source-equivalent capture evidence. cost=$1.91
- 2026-09-07T20:00:47+00:00 automated review requested changes: The policy direction is correct, and focused tests pass, but the implementation can falsely classify explicitly nonvisual work as visual and can treat stale functional checks as current when reusing screenshots. cost=$0.39
- 2026-09-08T10:12:34+00:00 dispatched revise run 20260908T101232Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11180 tokens)
- 2026-09-08T10:39:07+00:00 preserved uncommitted worktree changes from run 20260908T101232Z-revise outside the PR: `git stash apply 47642360c7a5ade8a35c16a7e66dae8677084511` in /home/joshua/work/worktrees/CG-390 (garden:CG-390:20260908T101232Z-revise:reap)
- 2026-09-08T10:40:24+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/299: Visual capture scope now requires explicit structured task metadata, and reusable capture checks contribute only successful UI evidence without validating current functional checks. The branch incorporates current origin/main and exact-head CI passed. cost=$1.89
- 2026-09-08T10:41:40+00:00 CI failure
- 2026-09-08T10:47:09+00:00 automated review: request_changes — The scoped visual-evidence policy is correctly implemented and focused validation passes, but exact-head CI includes a failed required test run. Resolve or successfully rerun the failing check before merge. cost=$0.59
- 2026-09-08T10:47:20+00:00 dispatched revise run 20260908T104718Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~11413 tokens)
- 2026-09-08T11:02:03+00:00 preserved uncommitted worktree changes from run 20260908T104718Z-revise outside the PR: `git stash apply 8d999620677f580ddb9d40bc90a7bb5cc6a55ce2` in /home/joshua/work/worktrees/CG-390 (garden:CG-390:20260908T104718Z-revise:reap)
- 2026-09-08T11:02:03+00:00 revision failed: worker finished with no commits
- 2026-09-08T11:02:10+00:00 PR merged: https://github.com/joshmarcus/context-garden/pull/299
