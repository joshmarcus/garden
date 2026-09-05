# Retrospective: context-garden/phase-02-friction

_2026-09-05T03:10:46+00:00_

## What changed

Phase 02 ran the loop on itself for a day: 89 tasks done, 94 PRs merged (25 by automerge), $547 spent, and every structural fix came from friction filed as tasks. The worker-environment friction that filled most PR bodies (no per-worktree venv, uv missing, GARDEN_ROOT leaking into tests, check commands resolving through the sentinel) is resolved by the per-product setup block, the guard/venv split, the conftest strip and the live garden's own setup config, and no worker after those merges reported it. Garden-repo deliverables run as a self product, stacked worktrees check out their parent, orphaned runs survive reaps, and a red base triggers a rebase instead of a revise round. Still unresolved from the friction record: briefs inline stale snippets and misreport existing files, the harvester drops hand-written sections and the reconciliation never reads Reported or comment friction, the principles digest contradicts the friction contract, the rebase tax and the fake_claude hotspot, timing-fragile subprocess tests, the dirty-on-read state rule, and the friction form's independent selects.

## Friction reconciled

| Friction item | Logged | Fixed by | Verdict | Evidence |
|---|---|---|---|---|
| Worktree has no .venv; tests silently import another worktree's editable install | CG-010 | CG-081 | fixed | Logged by 17 workers (CG-010, 013, 031, 035, 038, 041, 042, 043, 045, 053, 057, 069, 076, 100, 101, 106, 116); CG-081 made setup per-product, CG-092 gave the live garden.yaml a setup block that builds .venv per fresh worktree, CG-049 documented PYTHONPATH=src, and no worker after those merges (CG-121 to CG-140) reported it. |
| uv not on PATH so the documented install command fails | CG-013 | CG-092 | fixed | The live setup block uses python3 -m venv and pip, and the tool's CLAUDE.md now says a worktree has no .venv until setup.command runs. |
| pip install -e against the garden venv undocumented for worktrees | CG-032 | CG-049 | fixed | CG-049 documents PYTHONPATH=src and CG-081 makes the install a configured setup step rather than a manual one. |
| GARDEN_ROOT sentinel leaks into pytest and produces ~23 spurious failures | CG-037 | CG-098 | fixed | Also logged by CG-061; tests/conftest.py on main now strips GARDEN_ROOT and GARDEN_EXEC_ROOT, and CG-113 dropped the env -u stopgap. |
| Pre-PR check resolves its venv via the $GARDEN_ROOT sentinel and blocks runs falsely | CG-091 | CG-082 | fixed | Also logged by CG-037; CG-082 separated the guard from the check-path variable and the live setup.test command is .venv-relative. |
| Tasks whose deliverable is in the garden repo cannot run from a tool worktree | CG-029 | CG-123 | fixed | Also logged by CG-078; garden.yaml now declares the garden as a self product and this retro itself runs in a garden-repo worktree. |
| Brief inlines stale copies of reading-list files and reports existing files as not found | CG-045 | – | still true | Logged by CG-045, 078, 115, 117, 129 and 104; build_brief reads the task worktree if it exists, else the product clone, and nothing merged pins snippets to the branch tip at dispatch or validates paths. |
| A run that crashed before printing GARDEN_RESULT is recorded failed although its commits are correct | CG-057 | CG-083 | fixed | Also logged by CG-093 and CG-091; CG-036 tells the worker what is already on the branch, CG-083 made reaps atomic and CG-116 fixed the orphan sweep; distinguishing prior progress in the log remains as CG-125. |
| Stacked task dispatched on main instead of its parent branch, burning attempts | CG-082 | CG-126 | fixed | Also logged by CG-121; CG-126 makes worktree provisioning check out the parent branch. |
| max_turns drive-by in CG-034 contradicted CG-055 | CG-034 | CG-040 | outdated | CG-040 and CG-055 both merged; brief.py states the cap only when max_turns is greater than zero. |
| Rebase conflicts and overlaps between concurrently open PRs (CG-040/CG-055, CG-058/CG-060, CG-099) | CG-040 | – | outdated | All the named PRs merged; the notes were coordination snapshots, not defects. |
| tests/fake_claude.py is a hotspot that conflicts on every rebase | CG-111 | – | still true | fake_claude.py is still one 282-line fixture on main and no task splits it; CG-137 is only a draft. |
| Rebase tax from a fast-moving main: PRs spend rounds re-rebasing | CG-074 | – | still true | Reported by CG-074 and CG-079; the operator counted 32 rebase rounds and CG-139/CG-141 are ready and draft, not merged. |
| test_feedback_triggers_revise_round flakes under load | CG-100 | CG-064 | fixed | CG-064 made the test deterministic; CG-119 fixed the sibling happy-path flake. |
| Subprocess-driven scheduler tests are timing-fragile as a class | CG-126 | – | still true | Reported by CG-119 and CG-126 and the Reported section names test_event_log_digest_and_metrics; the staff-engineer review counts four flake-fix PRs and no in-process test runner exists. |
| test_set_budget_none_removes_cap fails on main | CG-079 | CG-127 | fixed | Also reported by CG-065, CG-062 and CG-079 in the Reported section; CG-127 closes the reset task's running run. |
| Local main drifts behind origin between dispatch and revise so an upstream-fixed bug looks new | CG-064 | CG-131 | fixed | CG-131 probes the check at the base commit and triggers a rebase instead of a revise round when the base is red. |
| Conflict plus red base falls back to a revise round instead of the conflict path | CG-131 | – | still true | Named as a follow-up in the CG-131 PR body and no task exists. |
| Stall detection AC 3 has no integration test | CG-038 | – | still true | Left as a discovered item in PR #21 and never filed. |
| Inbox friction form has independent product and phase selects | CG-044 | – | still true | The designer review finds a mismatched pair still returns a bare JSON 404, the one route CG-122 missed. |
| No JS test infrastructure for client-side behaviour | CG-087 | – | still true | CG-135 (an agent drives the loop through the web app) is ready, not merged. |
| garden take prints the whole brief; a session wants -q | CG-027 | CG-027 | fixed | cli.py take has a -q option that prints only the brief path. |
| Manual and harvested friction sections must coexist in friction.md | CG-027 | – | still true | write_friction_doc preserves only the Reported section, so the First live run section is dropped on the next harvest, as the project-manager review found. |
| Retro reconciliation cannot see the Reported section or comment friction | CG-133 | – | still true | _retro_materials calls only harvest on PR bodies; this brief omitted the sixteen Reported entries that friction.md holds. |
| A reviewer of a manual task cannot see garden state and a manual task gets no revise run | CG-027 | – | still true | Nothing merged gives manual tasks a revise path; CG-115's diff summary feeds attention cards only. |
| garden finish has no cost field | CG-027 | – | still true | No merged task names a cost field on finish; cost still travels in notes. |
| Harness logged out or environment broken burns both attempts | CG-027 | CG-032 | fixed | CG-032 makes doctor check gh, harness and git identity; CG-131 pauses on a base that fails checks; CG-033 was cancelled as superseded. |
| Whether harvest requires task.pr was ambiguous | CG-008 | – | outdated | The offline-first reading shipped and was accepted. |
| fixed.tokens versus fixed_tokens unclear from the brief-cost task | CG-012 | – | outdated | The report shipped and CG-066 shows estimates before any run; the open point is that nothing tracked the number over the phase. |
| Fake GitHub in conftest replaces feedback_since so the filter was untested | CG-047 | CG-047 | outdated | The same PR added a _gh stub and a test. |
| Editing garden.yaml in place for budgets needs a comment-preserving YAML dependency | CG-048 | CG-048 | outdated | The anticipated state.json fallback shipped; the leftover is UI copy that still says edit garden.yaml. |
| No per-product github override existed to follow | CG-068 | CG-068 | outdated | The PR added the _github_cfg helper matching the runner/harness override pattern. |
| Board priority controls left out of the priority task | CG-071 | – | outdated | CG-089 was filed for them and cancelled. |
| The Inbox has no log link to rename | CG-073 | CG-073 | outdated | Spec wording only; the run link was renamed and the acceptance criteria met. |
| Fence acceptance line reads like new code but existing find_root already guarantees it | CG-123 | CG-123 | outdated | Merged with an explicit self-scenario test; no reviewer disputed it. |
| Brief's suggested root cause for the budget test was a red herring | CG-127 | CG-127 | outdated | Task done; the lesson that an unreaped run holds a slot is recorded in the PR. |
| Nested dict __getitem__ marks state keys dirty | CG-053 | – | still true | The staff-engineer review reproduced that a read-only tick clobbers a concurrent garden set because reads dirty keys. |
| Aux runs (retro, personas) cannot reuse the worker-to-PR machinery | CG-133 | – | still true | The retro PR path is bespoke in _finish_retro; retro runs over two ticks and personas still write into the live garden's docs/reviews. |
| principles/00-index.md still tells workers to put friction in the PR body | CG-136 | – | still true | The principles digest inlined in this retro brief still says to note friction in the PR body under Friction. |
| Revise instructions about the runner force-pushing read like an instruction to push | CG-109 | – | still true | Reported after CG-136 merged and nothing since touches the revise template wording. |
| The brief invites a worker toward the garden root | CG-058 | CG-054 | fixed | CG-058 removed the invitation, CG-054 refuses root discovery from a worktree and CG-111 fences writes. |

## What the personas said

Security (5/10) is the sharpest: any PR commenter can author a worker prompt, workers inherit the operator's full credentials with unrestricted Bash and can push main, markdown renders raw HTML in a CSRF-free control panel, the fence exempts .garden and task files, checks run branch code unfenced, and automerge plus auto-upgrade can carry an injected change to a pip install. Staff engineer (6/10) reproduced two defects (reads dirty state keys so a read-only tick clobbers concurrent writes; a resumed reap double-emits run_finished) and wants the 3,200-line scheduler split, one Run.finish, one rebase helper, and an in-process test runner. Designer (6/10) and usability expert (6/10) find the same action named four ways, three things called a decision, cards and docs that still describe the pre-phase product, a flat 70-command help, an unreadable garden status at 80 columns, and the two headline features (stream-json live output, notify.command) documented nowhere. Project manager (7/10) and user (7/10) note the notification hook never fired live, triage pings before the review verdict, init defaults to ten workers with no budget, the brief-cost goal was never measured, and automerge reversed a stated non-goal without a record.

## Still open

- Briefs inline stale reading-list snippets and mark existing files not found (CG-045, 078, 115, 117, 129)
- garden friction drops the hand-written First live run section; the retro reconciliation reads neither the Reported section nor comment friction
- principles/00-index.md still says friction goes in the PR body (CG-136)
- Rebase tax and caps: 32 rebase rounds, fake_claude.py and scheduler.py hotspots (CG-139, CG-141, CG-137 not merged)
- Subprocess-driven scheduler tests remain timing-fragile; no in-process runner
- State dirty-on-read rule clobbers concurrent writes; run_finished double-emitted on resumed reap
- Feedback from any PR commenter becomes a worker prompt; workers inherit full credentials; raw HTML rendering and no origin check on POSTs
- notify.command unconfigured, undocumented and silent on failure; triage pings before the review verdict
- Brief fixed cost never measured over the phase
- Vocabulary and help: retry named four ways, decision means three things, flat help, no --version, garden status unreadable at 80 columns, cards that say edit garden.yaml or Mark done
- Inbox friction form independent selects return a bare 404 (CG-044)
- Stall-detection AC 3 untested (CG-038); conflict-plus-red-base corner (CG-131); revise template wording on pushing (CG-109)
- Manual tasks get no revise path and their reviewer cannot see garden state; garden finish has no cost field (CG-027)
- Aux runs cannot reuse the worker-to-PR path; retro spans two ticks and personas write into the live garden (CG-133, CG-145)
- Close-out: phase-01 not closed, roadmap Next names phase 02, review.difficulty still hard, automerge reversal unrecorded, manual exceptions (CG-027, CG-092, CG-113, CG-011, CG-039) unlisted

## Persona reports

- [designer](context-garden/phase-02-friction/docs/reviews/designer-2026-09-05.md)
- [project-manager](context-garden/phase-02-friction/docs/reviews/project-manager-2026-09-05.md)
- [security](context-garden/phase-02-friction/docs/reviews/security-2026-09-05.md)
- [staff-engineer](context-garden/phase-02-friction/docs/reviews/staff-engineer-2026-09-05.md)
- [usability-expert](context-garden/phase-02-friction/docs/reviews/usability-expert-2026-09-05.md)
- [user](context-garden/phase-02-friction/docs/reviews/user-2026-09-05.md)
