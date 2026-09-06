# Friction

_No friction reported yet._

## Reported

### 2026-09-06 · reported by CG-244 (Reserve retro task IDs and survive duplicate records) in run 20260906T000113Z-work

- The brief's task section has no explicit "Acceptance criteria" list, though the operating rules require one entry per criterion in that list; I mapped verified entries to the four clauses of the Goal sentence in order.

### 2026-09-06 · reported by CG-251 (Cost per accepted task and first-pass approval per model, tier and harness in metrics, the Costs page and the retro) in run 20260906T002504Z-work

- The full pytest suite runs longer than the terminal tool's synchronous output window in this shared environment.

### 2026-09-06 · reported by CG-292 (Every status write goes through _transition: Scheduler.mark_done and unapprove, and a source-grep test) in run 20260906T002733Z-work

- The full pytest invocation exceeded the tool's 30-second foreground window, so the complete suite was run successfully in bounded batches.

### 2026-09-06 · reported by CG-245 (Isolate planner execution from operator state) in run 20260906T003620Z-work

- The worktree's prior-attempt diff against current main looked like a large, alarming revert of CG-239's git-internals guard (gitops.py, fence.py, reap.py, ~250 lines) until I checked merge-base: the branch was simply forked before PR #193/#195 merged into main. A rebase resolved it with zero conflicts. Worth flagging because that diff shape (security code vanishing) is exactly what a careful reviewer should stop and investigate rather than assume is fine.

### 2026-09-06 · reported by CG-248 (TUI's dispatch action ('d' key) also bypasses the approve gate on a draft) in run 20260906T003801Z-work

- The brief cited src/garden/web/actions/control.py as the web dispatch guard to match, but that file has no per-task dispatch logic; the real guard from CG-238 is in web/actions/tasks.py's dispatch action (active-run check) and templates/task.html (hides the button on a draft task).

### 2026-09-06 · reported by CG-249 (`garden dispatch <id>` (CLI) allows dispatching a draft directly) in run 20260906T004012Z-work

- Acceptance criterion 4 names src/garden/web/actions/control.py as holding draft-gate logic to mirror, but that file only has tick/pause/resume/upgrade/config actions — the actual shared gate is Scheduler.approve in scheduler/human.py, called by web/actions/tasks.py's approve action and garden take. Fixed by calling the same Scheduler.approve, but the file reference in the brief was off.

### 2026-09-06 · reported by CG-236 (A trial winner's PR enters the review queue on its own, like any pushed revision) in run 20260906T004649Z-work

- Near the end of this session the shared sandbox's /tmp filled up (ENOSPC) from concurrent activity on other worktrees/sessions on the same host, blocking every shell command including trivial ones (confirmed via a fresh subagent hitting the same failure); I could not run a final full-suite pass after adding the last test or clean up a scratch file (cg236_wait.sh, untracked, left in the repo root) created while diagnosing it. All verification reported above (978 passed/3 skipped full suite, the 3 new tests individually, ruff clean) was captured before the outage.

### 2026-09-06 · reported by CG-291 (Each worker gets a private harness config dir holding only credentials, and the fence covers state.json and task files) in run 20260906T004845Z-revise

- Default pytest temporary retention exhausted /tmp during the first full-suite attempt; reran successfully with an isolated basetemp and retention disabled.

### 2026-09-05 · /tasks/CG-245 (CG-245)

I've been sent to this page (the task page) because the worker reported there was nothing to be done.  But now that I'm on the page, there's no decision to be made (no decision card shown) or way to move forward.

### 2026-09-05 · cli

Nobody looks at the real web pages. Workers build UI changes, reviewers approve them and personas review the phase without rendering a page: the Inbox card layout shipped collapsed to one word per line and buttons over text (CG-312), the task page a notification sends you to shows no decision (CG-311), and the phase-04 walkthrough was never captured. UI PRs must be reviewed against rendered pages, and the walkthrough must be part of every review that touches a template. Reported by the owner, 2026-09-06 02:10Z.
