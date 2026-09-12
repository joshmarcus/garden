---
id: CG-298
title: Persona runs are recorded per phase and the retro validates the run id it reads
status: done
product: context-garden
phase: phase-05
depends_on: []
priority: 4
difficulty: medium
reading: []
branch: garden/cg-298-persona-runs-are-recorded-per-phase-and-the-retr
pr: https://github.com/joshmarcus/context-garden/pull/281
discovered_from: retro:context-garden/phase-04
attempts: 1
last_dispatched_at: '2026-09-07T08:16:41+00:00'
created: '2026-09-05T23:58:20+00:00'
updated: '2026-09-07T08:27:26+00:00'
---

## Goal

dispatch_aux keys persona runs by phase rather than the shared _persona id; the retro validates the footer id against a safe character class and requires the resolved path under runs.dir. Also give discovered items structured file and error fields so dedup compares fields, not regexes.

## Context

Follow-up from the context-garden/phase-04 retro verdict.

## Acceptance criteria

- [ ] dispatch_aux persists persona run records keyed by phase, not the shared `_persona` id, so runs from different phases never collide or overwrite each other
- [ ] The retro rejects a footer run id containing any character outside a safe character class before it is used to build a path
- [ ] The retro rejects a run id whose resolved path falls outside `runs.dir`, even when the character class check passes
- [ ] Discovered items carry structured `file` and `error` fields, and dedup compares those fields directly instead of extracting them from text via regex
- [ ] A retro test asserts that both an invalid-character run id and one resolving outside `runs.dir` are rejected

## Suggestions

- [x] 2026-09-05 cli: Complete this brief so it passes the approve gate: add a '## Acceptance criteria' section with three to five '- [ ] ...' lines, each verifiable from the code or a page and one naming the test that proves it; add a reading list of four to eight paths that exist in the product checkout (check each with ls; write paths from the repository root such as src/garden/..., never invent one); keep the Goal and Context as written, tighten them if they narrate history; set difficulty if the current one is wrong. Do not change the title.

## Log

- 2026-09-05T23:59:00+00:00 refiled from the phase-04 retro branch, where it was CG-287 (renumbered by the operator: two reconcile runs drew ids from one counter)
- 2026-09-06T00:51:50+00:00 integrated 1 suggestion(s) (run 20260906T005028Z-edit) cost=$0.09
- 2026-09-06T00:52:24+00:00 approved (cli)
- 2026-09-07T07:40:35+00:00 dispatched work run 20260907T074015Z-work via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9200 tokens)
- 2026-09-07T07:51:49+00:00 preserved uncommitted worktree changes from run 20260907T074015Z-work outside the PR: `git stash apply 456bf8fd6bd2ec26d6b6e30d591964e2cc137284` in /home/joshua/work/worktrees/CG-298 (garden:CG-298:20260907T074015Z-work:reap)
- 2026-09-07T07:53:13+00:00 opened https://github.com/joshmarcus/context-garden/pull/281 (base main): Phase persona runs now use phase-specific run records, retro footer lookup is path-safe, and discovered-work dedup uses structured fields. cost=$1.03
- 2026-09-07T08:01:53+00:00 automated review requested changes: Phase-specific persona storage, path confinement, and structured discovery dedup are implemented correctly. The invalid-character regression case does not prove rejection because no corresponding unsafe run artifact exists, so that criterion remains unverified. cost=$0.36
- 2026-09-07T08:02:42+00:00 dispatched revise run 20260907T080240Z-revise via local [codex model=gpt-5.6-terra] (fresh session, base main, ~9781 tokens)
- 2026-09-07T08:10:04+00:00 preserved uncommitted worktree changes from run 20260907T080240Z-revise outside the PR: `git stash apply adebdc3a25a90983989bb62f1041d3724da03c3f` in /home/joshua/work/worktrees/CG-298 (garden:CG-298:20260907T080240Z-revise:reap)
- 2026-09-07T08:11:29+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/281: The retro regression now creates a valid artifact for an unsafe footer ID and independently asserts rejection of both unsafe and escaping IDs. Exact-commit CI passed. cost=$0.32
- 2026-09-07T08:16:29+00:00 PR conflicts with main; rebase onto main conflicts (src/garden/scheduler/retro.py); a rebase agent will resolve it
- 2026-09-07T08:16:41+00:00 dispatched rebase run 20260907T081639Z-rebase via local [codex model=gpt-5.6-luna] (fresh session, base main, conflict only; easy tier, ~12831 tokens)
- 2026-09-07T08:19:10+00:00 preserved uncommitted worktree changes from run 20260907T081639Z-rebase outside the PR: `git stash apply 59645b65e21bc97c952cdf087afae84b76c3e4a8` in /home/joshua/work/worktrees/CG-298 (garden:CG-298:20260907T081639Z-rebase:reap)
- 2026-09-07T08:20:42+00:00 pushed revision to https://github.com/joshmarcus/context-garden/pull/281: Rebased CG-298 onto origin/main and resolved the retro.py conflict preserving both phase-aware persona parsing and no_file gating. cost=$0.01
- 2026-09-07T08:24:40+00:00 automated review: approve — All five criteria are met. Phase-specific persona storage, confined retro lookup, and structured discovery dedup are correctly implemented and covered by 86 passing focused tests. cost=$0.33
- 2026-09-07T08:25:32+00:00 rebasing before merge; already on main's tip; not rebased or pushed
- 2026-09-07T08:27:26+00:00 PR merged by the garden: https://github.com/joshmarcus/context-garden/pull/281
