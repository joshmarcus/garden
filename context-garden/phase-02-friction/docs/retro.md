# Retrospective: context-garden/phase-02-friction

_2026-09-05T02:56:23+00:00_

## What changed

Phase 02 ran the tool on itself for the first time and shipped 88 merged PRs, all through garden tick apart from five manual exceptions (CG-027, CG-092, CG-113, CG-011, CG-039). The four goals landed structurally: automated review with revise rounds, bot-notice filtering and the garden's own comment marker close the review loop; stream-json live output, run pages with transcripts and a notification hook make waiting visible; friction is harvested from PR bodies, reported from anywhere and now reconciled by garden retro; brief estimates appear in garden usage. Most of the friction workers reported was the worker-environment cluster (missing venvs, shared editable installs, the GARDEN_ROOT sentinel), which CG-081, CG-082, CG-098 and CG-113 resolved so thoroughly that six duplicate reports were cancelled. The phase also hardened the loop in ways the goals did not name: atomic state and task writes, a worktree write fence, checkouts outside the garden, automerge with gates, base-red probing, stacked worktrees, self-upgrade, and structured decision cards. What did not land: the notification hook was never configured live, no number backs the flat-brief-cost goal, the automerge non-goal was reversed in config without a record, and briefs still inline stale snippets.

## Friction reconciled

| Friction item | Logged | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| Worktree has no .venv; CLAUDE.md's .venv/bin/pytest path assumes the repo root | CG-010 | CG-081 | fixed | CG-081 made environment setup a per-product setup block (live garden.yaml runs python3 -m venv .venv && pip install -e per fresh worktree) and CG-049 documented PYTHONPATH=src; duplicates CG-051/052/056/077/097/114 were cancelled against it. |
| Shared editable install points at another worktree so tests silently run stale code | CG-033 | CG-081 | fixed | Per-worktree venvs from the setup block plus CG-092 removing the shared venv install lines from the driving garden's config mean no worktree imports a sibling's src; no worker reported it after PR #48 merged. |
| uv not on PATH so the documented install command fails | CG-013 | CG-081 | fixed | The setup command now uses python3 -m venv and the config comments 'no uv here'; the documented command no longer assumes uv. |
| GARDEN_ROOT sentinel leaks into pytest and produces ~23 spurious CLI failures | CG-061 | CG-098 | fixed | CG-098 made the test suite not read the developer's GARDEN_ROOT and CG-113 dropped the env -u stopgap; CG-105 was cancelled as a duplicate. |
| Pre-PR check command resolves its venv via $GARDEN_ROOT, which is the worker sentinel, so checks fail before running | CG-091 | CG-082 | fixed | CG-082 separated the guard variable from the check-command venv path variable and CG-101 aligned the tests check; CG-095/CG-103/CG-108 were cancelled against it. |
| Stacked task's worktree checked out at main instead of the parent branch | CG-121 | CG-126 | fixed | CG-126 verified and fixed worktree provisioning for stacked tasks to check out the parent branch. |
| Task dispatched before its dependency merged, burning three attempts | CG-082 | CG-126 | fixed | Stacking on the parent's branch is the intended model and CG-126 makes that checkout correct; the wasted attempts came from the wrong base, not from dispatching early. |
| A run that committed work but crashed before GARDEN_RESULT was recorded failed and redispatched | CG-057 | CG-116 | fixed | CG-043, CG-083 and CG-116 made finish/reap atomic and stopped the orphan sweep closing live runs; the log distinction between 'made progress' and 'clean restart' remains as draft CG-125. |
| Garden-record tasks (CG-029, CG-078 criteria) cannot run from a product-repo worktree | CG-029 | CG-123 | fixed | CG-123 runs tasks that edit the garden's own files in a worktree of the garden repo; this retro is running in one. |
| test_set_budget_none_removes_cap fails at the branch base (latent CG-048 bug) | CG-079 | CG-127 | fixed | CG-127 fixed the missing reap tick on main; CG-128/CG-130 were cancelled as duplicates. |
| Rebase conflicts and overlaps between concurrently open PRs (max_turns, harness.py, read-these wording) | CG-034 | – | outdated | CG-034/CG-040/CG-055/CG-058/CG-060 all merged with the conflicts resolved at rebase time; nothing remains to act on. |
| One-off brief ambiguities resolved by a recorded judgement call (task.pr, fixed_tokens, github override shape, log link, leaderboard filter, fence acceptance line, red-herring root cause) | CG-068 | – | outdated | CG-008, CG-012, CG-047, CG-048, CG-068, CG-073, CG-087, CG-123 and CG-127 each merged with the decision documented in the PR body and no follow-up requested. |
| Brief's inlined reading-list snippets are stale or point at paths that moved or supposedly do not exist | CG-045 | – | still true | CG-078, CG-104, CG-115, CG-117 and CG-129 all hit it and no merged task regenerates snippets from the target checkout at dispatch time. |
| fake_claude.py is a hotspot; repeated mechanical rebases exhausted the revision cap | CG-111 | – | still true | CG-057 added a rebase round but rebase rounds still count toward the cap; CG-139 and CG-141 are drafts and CG-138 was cancelled. |
| State dirty-marking on nested dict mutation is subtle and regressed tests | CG-053 | – | still true | The staff-engineer persona reproduced that _TaskState marks keys dirty on read, so a read-only tick clobbers a concurrent garden set; no merged task fixes it. |
| Subprocess-driven scheduler tests flake under load | CG-100 | – | still true | CG-064, CG-119 and CG-127 fixed individual flakes, but CG-126 hit another and the staff engineer counts four flake-fix PRs with no in-process test runner shipped. |
| Local main drifts behind origin/main between dispatch and revise, so fixed upstream bugs look like new failures | CG-064 | – | still true | CG-131 rebases when the base is red, but nothing refreshes local main before revise checks; the project-manager persona lists it as an unowned follow-up. |
| Conflict-plus-red-base corner falls back to a plain revise round | CG-131 | – | still true | Flagged as a follow-up in PR #92 and by the project-manager persona; no task exists. |
| AC 3 of stall detection has no integration test | CG-038 | – | still true | Left as a discovered item in PR #21 and never filed. |
| Manual and harvested friction sections must coexist in friction.md | CG-027 | – | still true | friction.md currently holds hand-written First live run and Reported sections and the project-manager persona reports write_friction_doc keeps only Reported; the user persona adds that empty 'None.' entries are written. |
| Manual-task ergonomics: garden take prints the whole brief, finish has no cost field, a manual task's reviewer request waits for a person | CG-027 | – | still true | No merged task touched the manual take/finish path; CG-039 added cache reads to usage but not a cost field on finish. |
| Inbox friction form's product and phase selects are one combined select with no cascade | CG-044 | – | still true | The designer persona reports a mismatched pair still returns a bare JSON 404, the one route CG-122 missed. |
| Aux/orchestration runs cannot reuse the worker-to-PR machinery; retro needed a bespoke push+PR path | CG-133 | – | still true | PR #94 shipped _finish_retro as a one-off; CG-145 and CG-146 are drafts that will need the same path. |

## What the personas said

Six personas scored the phase between five and seven out of ten. Security (5) is the sharpest: the loop trusts everything that arrives from GitHub or a worker, so any PR commenter can author a revise prompt, workers inherit the operator's credentials with unrestricted Bash, PR text renders as raw HTML on a CSRF-free control panel, the fence exempts .garden and task files, and automerge plus auto-upgrade can carry an injected change to a pip install. Staff engineer (6) reproduced two defects (dirty-on-read state clobbering concurrent sets, and a resumed reap double-counting cost) and wants the 3,200-line scheduler split, one Run.finish, one rebase helper and an in-process test runner. Designer (6) and usability expert (6) agree the product reads as several features rather than one tool: the retry action has four names, 'decision' and 'resume' each mean three things, the help is a flat list of ~70 commands, garden status is unreadable at 80 columns, and the two headline features (stream-json, notify.command) are undocumented. User (7) would run it unattended if triage pings waited for the review verdict, the hook were documented and its failures logged, and init did not default to ten parallel workers with no budget. Project manager (7) says the phase is not closed: the harvester drops the hand-written friction record, the retro cannot see the Reported section, goal 2 was never exercised live, goal 4 has no measurement, and the automerge reversal is unrecorded.

## Still open

- Briefs inline stale reading-list snippets and wrong paths; regenerate from the target checkout at dispatch and verify each path exists
- Rebase rounds count toward the revision cap and hotspot files burn it (CG-111); CG-139 and CG-141 are drafts
- _TaskState marks keys dirty on read, so a read-only tick clobbers a concurrent garden set (reproduced by the staff engineer)
- A resumed reap re-emits run_finished and double-counts cost
- Scheduler tests drive subprocess fake workers; four flake-fix PRs this phase with no in-process runner
- Local main is not refreshed before revise checks (CG-064 follow-up); conflict-plus-red-base corner (CG-131 follow-up)
- garden friction rewrites friction.md keeping only Reported, would drop the First live run section, and writes 'None.' entries; the retro does not see the Reported section or comment friction
- notify.command is unset in the live garden, undocumented in the tool repo, and notify() swallows errors; triage pings fire before the review verdict
- The fixed brief cost was never measured over the phase; goal 4 has no number
- Automerge reversed a stated non-goal; design.md and roadmap.md still list it as a non-goal and the closing document must record the decision
- Security: no author trust on PR feedback, full credentials in the worker env, raw HTML in the web UI with no CSRF/Origin check, fence exempts .garden and task files, checks run branch code unfenced, automerge needs no human approval
- One vocabulary: retry/resume/decision naming, help panels, README and TUI key lists regenerated, budget and review cards updated, in_review task page panel
- Manual-task ergonomics from the first live run (take prints the brief, finish has no cost field, manual tasks get no revise round)
- Aux runs (retro, personas) cannot reuse the worker-to-PR path; CG-145 and CG-146 are drafts
- Stall-detection AC 3 has no integration test (CG-038); friction form product/phase mismatch returns a bare 404 (CG-044)
- Close-out loose ends: phase-01 not closed, roadmap Next names phase 02, principles/00-index.md says to put friction in the PR body, review.difficulty is hard with a note to revert, garden init defaults to max_parallel 10 with no budget

## Persona reports

- [designer](context-garden/phase-02-friction/docs/reviews/designer-2026-09-05.md)
- [project-manager](context-garden/phase-02-friction/docs/reviews/project-manager-2026-09-05.md)
- [security](context-garden/phase-02-friction/docs/reviews/security-2026-09-05.md)
- [staff-engineer](context-garden/phase-02-friction/docs/reviews/staff-engineer-2026-09-05.md)
- [usability-expert](context-garden/phase-02-friction/docs/reviews/usability-expert-2026-09-05.md)
- [user](context-garden/phase-02-friction/docs/reviews/user-2026-09-05.md)
