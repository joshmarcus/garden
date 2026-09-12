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

### 2026-09-06 · reported by CG-307 (Design the Now page: information architecture, visual system, motion, and a static mock of every state) in run 20260906T022844Z-revise

- garden persona-review cannot run inside a worker (garden commands are refused), so a criterion phrased as 'the command returns no high finding' cannot be met by the worker
- The automated review's diff included commits already merged to main (CG-248, CG-250); the review base was stale
- Headless desktop Chrome on Windows will not open a 390px window and lays out wider than it captures; a 390-wide iframe was needed to check the phone view

### 2026-09-06 · reported by CG-311 (The task page shows the decision a worker's no-change or question report needs: the same card and actions as the Inbox, right where the notification sends you) in run 20260906T024331Z-work

- The execution wrapper stopped complete pytest runs at roughly 30 seconds; focused web tests and lint completed successfully.

### 2026-09-06 · reported by CG-312 (Inbox decision cards lay out at full width: the text column no longer collapses to one word per line and the action buttons no longer overlap the evidence list) in run 20260906T024545Z-work

- Playwright is not installed, so browser screenshot validation was unavailable; HTML walkthrough capture remains covered.

### 2026-09-06 · reported by CG-314 (Design Now 2: astra's take on the Now page, information architecture, visual system, motion, and a static mock of every state) in run 20260906T031506Z-resume

- Subsequent Windows Edge launches failed with WSL UtilAcceptVsock accept4 timeout; the narrow capture was clipped and its CSS viewport could not be measured.
- External reading-list files are absent locally; GitHub authentication was unavailable to re-fetch the sources recorded by the prior attempt.
- The supplied aggregate snapshot lacks shared-metrics computation provenance; required persona reviews depend on runner publication.

### 2026-09-06 · discovered by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) in run 20260906T025753Z-work

The Now page shows hand merges as '— until metrics carries them'; the metrics work that records hand merges and tick duration should also feed the Now page's last period when it lands.

### 2026-09-06 · reported by CG-318 (The web app serves design documents, mocks and run captures: /design/<file> for the product's docs/design and a run page link to each capture) in run 20260906T031054Z-work

- The full required test suite takes approximately 7 minutes in this environment.

### 2026-09-06 · reported by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) in run 20260906T025753Z-work

- No Playwright in the worktree: screenshots came from Windows Chrome over WSL, and desktop Chrome will not lay out a 390px window, so the phone view needs an iframe
- The mock's stage_word_for disagreed with the design prose on the growth-stage bands (0.1 read as seed); the prose was followed
- Task state written with dict.update on a _TaskState is silently not saved (only __setitem__ is tracked); cost a debugging round in a test
- The garden fixture's review round cap is 2, not the design's 4, which the first test assumed

### 2026-09-06 · reported by CG-237 (The not-logged-in check reads a worker's prose as an auth failure: match the CLI's own error, not the report text) in run 20260906T033748Z-revise

- The original phase-04 stdout.json files were unavailable because they were truncated; surviving final result texts were used per the human-provided instruction.

### 2026-09-06 · reported by CG-314 (Design Now 2: astra's take on the Now page, information architecture, visual system, motion, and a static mock of every state) in run 20260906T034122Z-revise

- External garden reading files are absent locally; GitHub CLI authentication was unavailable to reread them.
- Direct WSL launches intermittently failed with UtilAcceptVsock; launching Edge through Windows PowerShell enabled full-page captures.
- Persona execution is required by acceptance but prohibited by worker operating rules.
- The supplied aggregate snapshot cannot establish shared metrics computation provenance.

### 2026-09-06 · reported by CG-237 (The not-logged-in check reads a worker's prose as an auth failure: match the CLI's own error, not the report text) in run 20260906T035343Z-revise

- The original four stdout.json artifacts were truncated; only their complete final result texts and preserved metadata were available.

### 2026-09-06 · reported by CG-237 (The not-logged-in check reads a worker's prose as an auth failure: match the CLI's own error, not the report text) in run 20260906T041429Z-revise

- The four original stdout.json artifacts were truncated and unavailable; only complete final-result texts and recorded metadata survived.

### 2026-09-06 · reported by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) in run 20260906T034805Z-revise

- Edge headless enforces a window floor of about 496 px, so --window-size=390 from the product overview's recipe lays the page out at 496 and looks like an overflow bug; a 390 px iframe wrapper gives a true viewport
- The venv has no image library, so the framed 390 captures keep a white margin and could not be cropped
- Port 8766 from the recipe was already taken by another server on this machine
- pkill -f and pgrep -f match the calling shell's own command line and killed it (exit 144) three times before a bracketed grep pattern worked
- _TaskState change tracking misses dict.update, a footgun for any script seeding state.json by hand

### 2026-09-06 · reported by CG-317 (The task page renders a trial in progress: the trial panel treats winner, scores and PRs as optional, and a test renders a task mid-trial with a failed contender) in run 20260906T040655Z-revise

- Initial pre-PR canary reported a dispatch timeout, but the isolated canary rerun passed.

### 2026-09-06 · reported by CG-316 (A dispatch that fails before its process starts closes the run record at once, and the orphan sweep closes any running record with no live process) in run 20260906T040653Z-revise

- Concurrent repository test workers made pytest temporary-directory cleanup hang after all tests reached 100%.

### 2026-09-06 · reported by CG-318 (The web app serves design documents, mocks and run captures: /design/<file> for the product's docs/design and a run page link to each capture) in run 20260906T040919Z-revise

- Windows Edge headless capture sessions conflicted with an existing process on port 8765 and hung on subsequent captures, preventing valid light/dark desktop/mobile screenshots.

### 2026-09-06 · reported by CG-314 (Design Now 2: astra's take on the Now page, information architecture, visual system, motion, and a static mock of every state) in run 20260906T042651Z-resume

- External garden reading files were absent locally; unauthenticated GitHub access could not retrieve them. Existing design source references and the supplied brief were retained.
- Edge produced all four full-page captures, but additional strip capture encountered timeout and WSL interoperability failures; the redundant pass was stopped.

### 2026-09-06 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260906T042947Z-work

- The brief's context-garden product, phase goals, and routing-spec paths were absent from this checkout.
- Full suite was slow under shared test-environment contention.

### 2026-09-06 · reported by CG-316 (A dispatch that fails before its process starts closes the run record at once, and the orphan sweep closes any running record with no live process) in run 20260906T045305Z-revise

- The CI-only temporary-file test is present on the updated base branch but not in this checkout; the cleanup regression was traced from its failure output and guarded accordingly.

### 2026-09-06 · discovered by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) in run 20260906T044547Z-revise

base.html's shell grid gives the folded rail half of any free viewport height on a page shorter than the viewport (min-height:100vh with auto rows); harmless on phones today, visible in a tall capture frame.

### 2026-09-06 · reported by CG-308 (Build Now 1 at /now1 from the Fable design: live view of what is running, what is next, where the phase is, and the last period) in run 20260906T044547Z-revise

- Edge's headless window will not go to 390 wide and it exits 1 without writing a file every few launches; the phone capture needs an iframe frame and a retry loop, which CG-315 should own so no worker rediscovers it
- A capture frame taller than the page shows a blank band above the folded rail because the shell's grid stretches the rail's row into the free height; on a real phone the viewport is shorter than the page so it never shows, but it costs a capture round to diagnose
- The stream test's 10,000-second progress interval only suppressed progress on a machine up under 2.8 hours; the stream measures from a monotonic zero

### 2026-09-06 · reported by CG-311 (The task page shows the decision a worker's no-change or question report needs: the same card and actions as the Inbox, right where the notification sends you) in run 20260906T045045Z-revise

- GitHub CLI is unauthenticated, so open review comments and CI metadata could not be queried directly.
- Windows Edge resolved the alternate temporary WSL server port to an existing localhost service, preventing valid rendered-page captures.
- The full pytest invocation detached after partial progress in this terminal environment; focused web regressions passed.

### 2026-09-06 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260906T052921Z-revise

- Full pytest run was terminated by the shared environment at 27% (exit 143) despite no failures; targeted tests and lint passed.

### 2026-09-06 · reported by CG-215 (Onboarding skill and command: analyse an existing project and its environment to create a garden product, principles, setup config and a first phase) in run 20260906T052917Z-revise

- The shared host was running many concurrent pytest processes in uninterruptible I/O states, making the full-suite rerun stall and obscuring a later unrelated failure.

### 2026-09-06 · reported by CG-324 (The loop produces the evidence a criterion requires: persona reviews, captures and checks named by a task's criteria run when its PR opens, before the first review) in run 20260906T061704Z-work

- The full pytest command continued beyond the command-output window in the shared environment; focused tests and lint completed successfully.

### 2026-09-06 · reported by CG-216 (Workers on independent remote hosts: a worker agent that claims runs from the garden over HTTP, works in its own clone, pushes the branch and posts the result and transcript back) in run 20260906T074100Z-revise

- The scripted QA flow advertised a 30-second deadline but silently imposed a 10-second per-request timeout, making the canary load-sensitive.

### 2026-09-06 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260906T074108Z-revise

- Long pytest processes detach from the command wrapper; captured the final suite output in a temporary log.

### 2026-09-06 · reported by CG-320 (Reviews by the model one step above the writer: a review ladder across harnesses picks the reviewer from the PR's last work or revise model) in run 20260906T080853Z-revise

- Concurrent full pytest suites in other worktrees saturated the shared filesystem and prevented a reliable full-suite/lint completion.

### 2026-09-06 · reported by CG-230 (A tier can name several harness and model options, and dispatch spreads runs across them to share quotas, skipping a paused or exhausted one) in run 20260906T084648Z-revise

- Full pytest runs are blocked in uninterruptible filesystem waits by concurrent pre-existing pytest processes in the shared environment; the new focused test reached its passing assertion, and `.venv/bin/ruff check src tests` passed.

### 2026-09-06 · reported by CG-318 (The web app serves design documents, mocks and run captures: /design/<file> for the product's docs/design and a run page link to each capture) in run 20260906T093400Z-revise

- The reported pre-PR QA failure was order/timing-sensitive and could not be reproduced.

### 2026-09-06 · reported by CG-215 (Onboarding skill and command: analyse an existing project and its environment to create a garden product, principles, setup config and a first phase) in run 20260906T101732Z-revise

- Pytest cleanup of shared temporary directories stalled after tests completed; isolating `PYTEST_DEBUG_TEMPROOT` allowed both targeted and full suites to finish normally.

### 2026-09-06 · reported by CG-324 (The loop produces the evidence a criterion requires: persona reviews, captures and checks named by a task's criteria run when its PR opens, before the first review) in run 20260906T122022Z-revise

- Full pytest runs remain slow while concurrent scheduler checks perform worktree-heavy tests.

### 2026-09-06 · reported by CG-296 (One vocabulary and one place for each fact across rail, Config, CLI and Inbox) in run 20260906T131807Z-work

- The required final lint command encountered an unrelated untracked tests/test_ambient_env_probe.py formatting error after this change was committed; lint was clean before that file appeared.
- Concurrent full pytest processes in the shared worktree obscured normal completion output.

### 2026-09-06 · reported by CG-254 (redispatch kills the superseded worker, and pin runs the canary, installs and restarts after a tick) in run 20260906T135407Z-revise

- The full pytest process exceeds the execution tool's reporting window and is terminated before it can return a result; focused affected tests completed successfully.

### 2026-09-06 · reported by CG-342 (Reconcile Now CLI tests with the page-2 command) in run 20260906T153916Z-work

- The checkout contained a pre-existing docs/design/snapshot.json modification, which was preserved outside this change.

### 2026-09-06 · reported by CG-329 (The worker count the dispatcher enforces and the count the rail shows are the same number: checks, reviews and edit runs either take a slot visibly or not at all) in run 20260906T174248Z-work

- The full pytest run reached 80% without failures but was externally terminated with exit 143 before completion.

### 2026-09-06 · reported by CG-357 (Keep web requests responsive while workers run and run history grows) in run 20260906T183056Z-revise

- The acceptance criterion requests three real capped workers, but worker/controller commands and live-garden access are prohibited in this worktree; validation therefore used three active records and states that limit explicitly.

### 2026-09-06 · reported by CG-329 (The worker count the dispatcher enforces and the count the rail shows are the same number: checks, reviews and edit runs either take a slot visibly or not at all) in run 20260906T190051Z-revise

- The review capture request listed pages beyond those touched by this scheduler-only revision.
- Declined review improvement: Capture every listed UI page in light and dark at desktop and narrow widths. — This revision changes scheduler logic and tests only; no UI markup or page behavior was changed.

### 2026-09-06 · reported by CG-338 (Keep the operator machine responsive under concurrent workers and test suites) in run 20260906T193843Z-revise

- The initial pre-PR suite was externally terminated by SIGTERM despite progressing normally; a foreground rerun completed in 3:10.

### 2026-09-06 · reported by CG-343 (Finished reviews are reconciled even after their task leaves review states) in run 20260906T194758Z-revise

- `.venv/bin/python -m pytest -q -x` was externally terminated with exit 143 twice during a long-running integration segment; focused changed-module tests passed.
- Tool-session retries spawned duplicate pytest processes; they were cleaned up before the final focused verification.

### 2026-09-06 · reported by CG-358 (Keep incident control actions responsive and retry-safe during web overload) in run 20260906T193955Z-work

- The incident document referenced as docs/incidents/2026-09-06-web-responsiveness-retro.md was absent from this checkout.

### 2026-09-06 · reported by CG-293 (A brief never ships with an empty or unresolved reading list, and a revise brief restates the criteria and the concrete blocker) in run 20260906T203139Z-revise

- Test tool windows left earlier pytest processes running; stopped only processes started in this worktree.

### 2026-09-06 · reported by CG-337 (Attention cards ask for product decisions, while no-change reports reconcile automatically) in run 20260906T203723Z-revise

- The seeded UI check captures every walkthrough page even when a change affects only Inbox, so reviewers must acknowledge many unrelated pages.

### 2026-09-06 · reported by CG-358 (Keep incident control actions responsive and retry-safe during web overload) in run 20260906T204704Z-revise

- Concurrent full-suite runs from several worktrees caused heavy filesystem contention; this branch's suite still completed successfully in 553.06 seconds.

### 2026-09-06 · reported by CG-361 (Bound test workloads within each run and reserve web capacity) in run 20260906T230331Z-work

- The exact-commit CI helper requires a clean tree, so the scheduler-preserved unrelated snapshot had to be temporarily stashed and restored.

### 2026-09-06 · reported by CG-354 (Split tests into focused suites to shorten development feedback) in run 20260906T231053Z-work

- A concurrent docs/design/snapshot.json edit had to be temporarily stashed and restored so the exact-commit CI helper could run.

### 2026-09-06 · reported by CG-340 (Demonstrate onboarding and a useful accepted change on an independent project) in run 20260906T232518Z-work

- The CI helper requires a clean checkout, so the unrelated pre-existing snapshot modification had to be temporarily stashed and restored.

### 2026-09-06 · reported by CG-341 (Enforce stabilization evidence at phase close and record unattended operation mechanically) in run 20260906T232301Z-work

- An unrelated pre-existing docs/design/snapshot.json modification had to be temporarily stashed for the clean-worktree CI helper and was restored unchanged.

### 2026-09-06 · reported by CG-361 (Bound test workloads within each run and reserve web capacity) in run 20260906T232501Z-revise

- Edge capture required 56 serial browser launches because the shared rail affects every operator page.
- Declined review improvement: Define one host-owned lease policy source instead of allowing different gardens to advertise different slot counts over the same lock namespace. — A host-owned policy and migration mechanism would materially expand configuration ownership beyond this task. The current boundary remains per-user and documentation requires gardens sharing that account to use the same configured limit; central host policy should be designed as a follow-up.

### 2026-09-06 · reported by CG-359 (Preserve unrelated worktree changes without adding them to recovered PRs) in run 20260906T233716Z-work

- CI helper requires a clean checkout; the unrelated snapshot was temporarily stashed and restored around exact-commit CI.

### 2026-09-07 · reported by CG-361 (Bound test workloads within each run and reserve web capacity) in run 20260906T235529Z-revise

- Declined review improvement: Exercise cgroup membership with a disposable delegated cgroup when the host supports it, skipping explicitly otherwise. — The only writable cgroup available to this worker is the live garden-serve service cgroup. Creating or migrating processes there would modify the production service boundary, which the task explicitly forbids; finite-limit and migration behavior remains covered with isolated filesystem tests.

### 2026-09-07 · reported by CG-361 (Bound test workloads within each run and reserve web capacity) in run 20260907T005035Z-revise

- Declined review improvement: Avoid commit subjects such as “leftover changes from worker run” in the permanent branch story where workflow permits. — That subject is already in published shared history; rewriting it would violate the no-history-rewrite rule. The new commit uses the product-focused subject “share validation capacity without serializing agents”.

### 2026-09-07 · reported by CG-365 (Complete resource isolation enforcement and evidence after CG-361) in run 20260907T011212Z-work

- The CI helper required a clean tree; restoring the preserved unrelated snapshot required resolving its stash conflict back to the original uncommitted file.

### 2026-09-07 · reported by CG-326 (Fix the Edge capture recipe for 390-wide captures: frame the page in a 390 px iframe) in run 20260907T012252Z-work

- The local main checkout lacked the current-origin scripts/check_ci.py; incorporated the origin/main CI helper and workflow before running CI.

### 2026-09-07 · reported by CG-327 (The live-garden fence attributes only the worker's own writes: the operator's and the scheduler's commits during a run's window are never counted against the run) in run 20260907T012757Z-work

- Integrating origin/main required stashing a pre-existing untracked docs/design/snapshot.json because main now tracks that path; the prior file remains preserved in git stash.

### 2026-09-07 · reported by CG-332 (A task parked by a harness environment stop is dispatched again as soon as the harness resumes, without a hand) in run 20260907T012758Z-work

- The first CI run had a nondeterministic unrelated canary timeout; local reproduction passed and the fresh final-commit CI run passed.

### 2026-09-07 · reported by CG-333 (A run that ends without a result but with new commits in its worktree is reaped as a pushed revision, not a failed attempt) in run 20260907T014003Z-work

- The CI helper required temporarily stashing the pre-existing unrelated snapshot edit; it was restored afterward.

### 2026-09-07 · reported by CG-332 (A task parked by a harness environment stop is dispatched again as soon as the harness resumes, without a hand) in run 20260907T015006Z-revise

- One unrelated retained-history capacity test observed a host cgroup memory.events.high increase; the affected focused tests and exact-commit CI passed.

### 2026-09-07 · reported by CG-339 (Review affected behavior through the running application before accepting interaction claims) in run 20260907T020052Z-work

- Git stashes are shared across worktrees, so a concurrent snapshot-only stash briefly displaced the labeled CG-339 stash; diff-count verification identified it and both snapshots were preserved.

### 2026-09-07 · reported by CG-366 (Prevent fence attribution from rewinding concurrent worker logs) in run 20260907T020637Z-work

- The exact-head CI helper requires a completely clean worktree, so the pre-existing design snapshot modification had to be temporarily preserved in a named stash and restored afterward.

### 2026-09-07 · reported by CG-323 (The worker pre-flights its PR against the review rubric, mechanical review items become pre-PR checks, and criteria are frozen at dispatch) in run 20260907T021858Z-resume

- Preserved an unrelated runtime docs/design/snapshot.json rewrite in a named local stash so it does not enter this branch.

### 2026-09-07 · reported by CG-366 (Prevent fence attribution from rewinding concurrent worker logs) in run 20260907T023123Z-revise

- The exact-head CI helper requires a clean worktree, so the unrelated docs/design/snapshot.json change was temporarily preserved in a named stash and restored after each CI run.

### 2026-09-07 · reported by CG-322 (A _TaskState written with dict.update or |= is not saved) in run 20260907T030025Z-revise

- The branch initially lacked the current CI helper and required refreshing from origin/main; an unrelated generated snapshot edit was preserved outside the task commits.

### 2026-09-07 · reported by CG-323 (The worker pre-flights its PR against the review rubric, mechanical review items become pre-PR checks, and criteria are frozen at dispatch) in run 20260907T030027Z-revise

- Temporarily stashed and restored a pre-existing unrelated docs/design/snapshot.json change so the CI helper could run on a clean exact head.

### 2026-09-07 · reported by CG-339 (Review affected behavior through the running application before accepting interaction claims) in run 20260907T030525Z-revise

- The CI helper required temporarily stashing an unrelated pre-existing docs/design/snapshot.json modification; it was restored unchanged after CI.

### 2026-09-07 · reported by CG-322 (A _TaskState written with dict.update or |= is not saved) in run 20260907T034518Z-revise

- Direct git push lacked interactive credentials; scripts/check_ci.py authenticated and pushed successfully.

### 2026-09-07 · reported by CG-327 (The live-garden fence attributes only the worker's own writes: the operator's and the scheduler's commits during a run's window are never counted against the run) in run 20260907T034027Z-revise

- CI required temporarily stashing an unrelated generated snapshot; it was restored unchanged.

### 2026-09-07 · reported by CG-339 (Review affected behavior through the running application before accepting interaction claims) in run 20260907T034029Z-revise

- The CI helper required temporarily stashing an unrelated pre-existing docs/design/snapshot.json modification to obtain a clean exact-commit run.

### 2026-09-07 · reported by CG-358 (Keep incident control actions responsive and retry-safe during web overload) in run 20260907T034031Z-revise

- The exact-head CI helper requires a completely clean worktree, so the unrelated runtime snapshot had to be temporarily stashed and restored.

### 2026-09-07 · reported by CG-365 (Complete resource isolation enforcement and evidence after CG-361) in run 20260907T034033Z-revise

- Declined review improvement: Add broad UI screenshots for every page sharing the rail. — CG-326 owns the capture infrastructure and broad-page capture evidence; fabricated or incomplete PNG evidence would not validate this resource-isolation change.

### 2026-09-07 · reported by CG-331 (The tick-responsiveness test measures against the machine, not the clock: it fails a PR only when a web action waits on the tick, never because the box is busy) in run 20260907T040246Z-work

- CI helper required temporarily stashing an unrelated pre-existing snapshot change to satisfy its clean-worktree precondition.

### 2026-09-07 · reported by CG-355 (Restore automatic installation and safe restart after tool updates) in run 20260907T040742Z-work

- A direct git push lacked credentials; scripts/check_ci.py supplied the authorized command-local authentication and pushed successfully.
- The focused web suite's cgroup high-pressure counter changed during a concurrent workload; the affected resource-isolation test passed when rerun alone.

### 2026-09-07 · reported by CG-331 (The tick-responsiveness test measures against the machine, not the clock: it fails a PR only when a web action waits on the tick, never because the box is busy) in run 20260907T042139Z-revise

- The pre-existing docs/design/snapshot.json edit had to be temporarily stashed because check_ci.py requires a clean worktree; it was restored unchanged.
- One full web-suite run hit an unrelated host cgroup memory.events.high change; the isolated test passed on rerun and CI passed.

### 2026-09-07 · reported by CG-364 (Remove redundant tests and unnecessary fixture work) in run 20260907T041221Z-work

- Shared global git stash namespace requires explicit stash references when preserving unrelated edits for CI.

### 2026-09-07 · reported by CG-362 (Complete externally implemented tasks from verified PR metadata) in run 20260907T041419Z-work

- The referenced docs/incidents/CG-360-validation.md was absent from this checkout.
- A pre-existing docs/design/snapshot.json change had to be temporarily stashed for CI and was restored unchanged.

### 2026-09-07 · reported by CG-362 (Complete externally implemented tasks from verified PR metadata) in run 20260907T044610Z-revise

- The CI helper required temporarily stashing the unrelated generated design snapshot; it was restored unchanged.

### 2026-09-07 · reported by CG-355 (Restore automatic installation and safe restart after tool updates) in run 20260907T044253Z-revise

- The local full web suite's resource-isolation test observed host cgroup `memory.events high` changing under concurrent system pressure; all other 96 web tests passed, and clean exact-commit GitHub CI passed the full 1288-test suite.

### 2026-09-07 · reported by CG-368 (Check browser runtime readiness before admitting capture-dependent work) in run 20260907T045827Z-work

- The exact-head CI helper required temporarily stashing an unrelated pre-existing snapshot edit; it was restored unchanged after CI.

### 2026-09-07 · reported by CG-326 (Fix the Edge capture recipe for 390-wide captures: frame the page in a 390 px iframe) in run 20260907T050248Z-revise

- An unrelated pre-existing docs/design/snapshot.json modification required temporary stashing so the exact-commit CI helper could run.

### 2026-09-07 · reported by CG-362 (Complete externally implemented tasks from verified PR metadata) in run 20260907T050835Z-revise

- The shared generated design snapshot had to be temporarily stashed for CI because the CI helper requires a clean worktree; it was restored unchanged afterward.

### 2026-09-07 · reported by CG-355 (Restore automatic installation and safe restart after tool updates) in run 20260907T051310Z-revise

- The repository-wide shared git stash index changed concurrently while preserving an unrelated generated snapshot edit; the displaced stash object was restored and the original edit preserved.

### 2026-09-07 · reported by CG-368 (Check browser runtime readiness before admitting capture-dependent work) in run 20260907T051633Z-revise

- The exact-head CI helper requires a clean tree, so the pre-existing snapshot edit had to be temporarily stashed and restored; shared cross-worktree stash indexing required hash-based recovery.

### 2026-09-07 · reported by CG-369 (Align phase-close gate with fixture-sufficient onboarding requirement) in run 20260907T051635Z-work

- A pre-existing unrelated docs/design/snapshot.json edit required temporary preservation in a stash so the CI helper could run; it was restored unchanged.

### 2026-09-07 · reported by CG-362 (Complete externally implemented tasks from verified PR metadata) in run 20260907T052311Z-revise

- Pre-existing docs/design/snapshot.json edit required a temporary stash because the CI helper requires a clean worktree.

### 2026-09-07 · reported by CG-355 (Restore automatic installation and safe restart after tool updates) in run 20260907T052750Z-revise

- The repository-wide shared stash changed concurrently during CI preservation; the displaced stash entry was immediately reconstructed by its commit hash, and the pre-existing snapshot modification remains restored.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T053542Z-work

- The CI helper initially required temporarily stashing a pre-existing unrelated docs/design/snapshot.json edit.

### 2026-09-07 · reported by CG-370 (Fix measured narrow-viewport overflow on Phase and Runs pages) in run 20260907T053326Z-work

- The shared generated snapshot edit required a temporary stash to satisfy clean-tree CI; it was restored unmodified.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T055530Z-revise

- System Python lacked pytest; checks required the prepared .venv interpreter.
- A pre-existing unrelated snapshot edit made the CI helper require a temporary stash and explicit restoration.
- One resource-capacity test observed host cgroup counter drift during its workload; exact-commit CI passed.
- Declined review improvement: Add a scheduler retro test asserting capture completes before the first persona dispatch and that the resulting brief contains a newly generated walkthrough marker. — Existing scheduler ordering places capture before persona dispatch, while walkthrough capture tests verify the generated page evidence; adding another orchestration test was not necessary for this fix.

### 2026-09-07 · reported by CG-339 (Review affected behavior through the running application before accepting interaction claims) in run 20260907T060340Z-revise

- The CI helper requires a clean worktree, so the unrelated pre-existing snapshot edit had to be temporarily preserved and restored.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T061723Z-revise

- The first exact-commit CI run exposed legacy fixtures using unannotated completion events; compatibility was added and the final run passed.

### 2026-09-07 · reported by CG-301 (Retro questions are deduplicated across reconcile runs, and a second judge can run with task filing off) in run 20260907T062708Z-work

- GitHub CI took several minutes to complete after registering the exact commit.

### 2026-09-07 · reported by CG-301 (Retro questions are deduplicated across reconcile runs, and a second judge can run with task filing off) in run 20260907T064329Z-revise

- An unrelated pre-existing snapshot edit required temporary stashing to run the CI helper.

### 2026-09-07 · reported by CG-326 (Fix the Edge capture recipe for 390-wide captures: frame the page in a 390 px iframe) in run 20260907T064208Z-revise

- The required CI helper initially refused the preserved unrelated snapshot modification; it was temporarily stashed and restored unchanged.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T063927Z-revise

- The inherited docs/design/snapshot.json change made check_ci require temporary stash handling; it was restored unchanged and remains outside the commit.

### 2026-09-07 · reported by CG-313 (parse_result accepts the GARDEN_RESULT marker wrapped in markdown emphasis or code and a JSON payload that spans lines) in run 20260907T065318Z-work

- System Python did not include pytest; used the prepared .venv as instructed.

### 2026-09-07 · reported by CG-325 (A dependency can require the parent to merge, not only to have a PR: depends_on entries take after: merge, the default for a design-to-build pair) in run 20260907T065335Z-work

- A pre-existing unrelated modification to docs/design/snapshot.json required temporary stashing because check_ci requires a clean worktree; it was restored unchanged.

### 2026-09-07 · reported by CG-294 (Planning sequences dependent tasks and inlines retro evidence into the brief) in run 20260907T071059Z-work

- Current main changed the unrelated design snapshot; its local modification was preserved outside the commit while integrating the current CI workflow.

### 2026-09-07 · reported by CG-325 (A dependency can require the parent to merge, not only to have a PR: depends_on entries take after: merge, the default for a design-to-build pair) in run 20260907T071221Z-revise

- The CI helper required temporarily stashing a pre-existing unrelated snapshot change before running.

### 2026-09-07 · reported by CG-356 (Recover onboarding cleanly when planner output is rejected) in run 20260907T070629Z-work

- An unrelated dirty design snapshot required a temporary stash while CI ran.

### 2026-09-07 · reported by CG-336 (Record Codex operator usage in the operator spend ledger) in run 20260907T071337Z-revise

- Remote task branch required a normal merge after rebase so the final push remained non-force.

### 2026-09-07 · reported by CG-297 (The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal exit) in run 20260907T072308Z-work

- The CI helper required temporarily stashing a pre-existing unrelated snapshot edit.

### 2026-09-07 · reported by CG-304 (Update docs: docs/architecture.md) in run 20260907T072631Z-work

- A pre-existing edit to docs/design/snapshot.json required temporary stashing so the CI helper could verify a clean tree; it was restored unchanged.

### 2026-09-07 · reported by CG-356 (Recover onboarding cleanly when planner output is rejected) in run 20260907T072845Z-revise

- Pre-existing unrelated docs/design/snapshot.json edit required a temporary stash so the exact-commit CI helper could run.
- First exact-commit CI run hit a transient unrelated empty JSON read in tests/test_runners.py; isolated test passed locally and the diagnosed exact-commit rerun passed.

### 2026-09-07 · reported by CG-306 (Update docs: docs/design.md) in run 20260907T073719Z-work

- CI helper initially required temporarily stashing a pre-existing unrelated snapshot change.

### 2026-09-07 · reported by CG-297 (The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal exit) in run 20260907T073857Z-revise

- The CI helper required a clean worktree; an unrelated pre-existing snapshot edit was temporarily stashed and restored unchanged.

### 2026-09-07 · reported by CG-298 (Persona runs are recorded per phase and the retro validates the run id it reads) in run 20260907T074015Z-work

- CI helper required temporarily stashing an inherited unrelated snapshot edit before it could check the committed branch.

### 2026-09-07 · reported by CG-356 (Recover onboarding cleanly when planner output is rejected) in run 20260907T074952Z-revise

- An inherited unrelated docs/design/snapshot.json modification required temporary preservation while CI ran.

### 2026-09-07 · reported by CG-297 (The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal exit) in run 20260907T075458Z-revise

- The CI helper required temporarily stashing a pre-existing unrelated snapshot edit before running.

### 2026-09-07 · reported by CG-299 (Small follow-ups: retro_question kind, backlog noscript, CI flake, ambient config dir in tests, a second opinion for self products) in run 20260907T074953Z-work

- The pre-existing design snapshot made the CI helper reject the worktree, so it was temporarily stashed and restored unchanged.

### 2026-09-07 · reported by CG-298 (Persona runs are recorded per phase and the retro validates the run id it reads) in run 20260907T080240Z-revise

- The CI helper required temporarily stashing an unrelated existing snapshot edit before checking the clean commit.

### 2026-09-07 · reported by CG-297 (The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal exit) in run 20260907T081021Z-revise

- The CI helper required temporarily stashing and restoring an unrelated pre-existing snapshot edit.

### 2026-09-07 · reported by CG-304 (Update docs: docs/architecture.md) in run 20260907T082128Z-revise

- CI helper initially required temporarily stashing an unrelated pre-existing snapshot change.

### 2026-09-07 · reported by CG-299 (Small follow-ups: retro_question kind, backlog noscript, CI flake, ambient config dir in tests, a second opinion for self products) in run 20260907T081454Z-revise

- The CI helper required temporarily stashing and restoring an unrelated pre-existing docs/design/snapshot.json modification.

### 2026-09-07 · reported by CG-305 (Update docs: docs/worker-protocol.md) in run 20260907T083324Z-revise

- The CI helper required temporarily stashing a pre-existing unrelated modification in docs/design/snapshot.json; it was restored unchanged.

### 2026-09-07 · reported by CG-305 (Update docs: docs/worker-protocol.md) in run 20260907T084349Z-revise

- The CI helper required temporarily stashing a pre-existing unrelated working-tree modification; it was restored unchanged afterward.

### 2026-09-07 · reported by CG-299 (Small follow-ups: retro_question kind, backlog noscript, CI flake, ambient config dir in tests, a second opinion for self products) in run 20260907T084230Z-revise

- CI required temporarily stashing a pre-existing unrelated docs/design/snapshot.json edit because the helper requires a clean worktree.

### 2026-09-07 · reported by CG-300 (The retro's Numbers section reads the operator ledger where the owner keeps it, and reports spend and share) in run 20260907T084808Z-revise

- The first exact-commit CI attempt hit a timing-sensitive JSON read race in an unrelated runner test; the diagnosed rerun passed.

### 2026-09-07 · reported by CG-365 (Complete resource isolation enforcement and evidence after CG-361) in run 20260907T084638Z-revise

- A pre-existing generated snapshot change had to be temporarily stashed so the CI helper could validate the committed head.

### 2026-09-07 · reported by CG-300 (The retro's Numbers section reads the operator ledger where the owner keeps it, and reports spend and share) in run 20260907T090331Z-revise

- The final base-diff includes extensive pre-existing branch history and an unrelated blank-line diff from main; the worktree itself is clean.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T091343Z-revise

- The CI helper required temporarily stashing a pre-existing unrelated snapshot change before running exact-head CI.

### 2026-09-07 · reported by CG-297 (The walkthrough renderer skips hidden elements and attributes, and check runs retry once on a signal exit) in run 20260907T091345Z-revise

- The CI helper initially rejected a pre-existing unrelated docs/design/snapshot.json modification; it was temporarily stashed and restored unchanged.

### 2026-09-07 · reported by CG-329 (The worker count the dispatcher enforces and the count the rail shows are the same number: checks, reviews and edit runs either take a slot visibly or not at all) in run 20260907T091349Z-revise

- The default UI port was already occupied, so disposable captures used port 8876.

### 2026-09-07 · reported by CG-339 (Review affected behavior through the running application before accepting interaction claims) in run 20260907T092821Z-revise

- The exact-head CI helper required temporarily stashing an unrelated pre-existing snapshot modification; it was restored unchanged afterward.

### 2026-09-07 · reported by CG-373 (Bound rebase prompts and recover oversized generated-file conflicts) in run 20260907T093244Z-work

- The first CI attempt hit an unrelated transient execution.json read race in tests/test_runners.py; isolated local coverage passed and the exact-commit CI rerun passed.

### 2026-09-07 · reported by CG-294 (Planning sequences dependent tasks and inlines retro evidence into the brief) in run 20260907T095935Z-revise

- Concurrent workers can reorder shared git stashes during CI, requiring content-based restoration of a named stash.

### 2026-09-07 · reported by CG-365 (Complete resource isolation enforcement and evidence after CG-361) in run 20260907T100531Z-revise

- An unrelated restored docs/design/snapshot.json artifact required temporary named preservation before CI.

### 2026-09-07 · reported by CG-339 (Review affected behavior through the running application before accepting interaction claims) in run 20260907T100838Z-revise

- The shared Git stash namespace changed concurrently during CI preparation; the displaced stash was restored and the pre-existing snapshot edit was preserved.

### 2026-09-07 · reported by CG-373 (Bound rebase prompts and recover oversized generated-file conflicts) in run 20260907T101616Z-revise

- The CI helper required temporarily stashing the pre-existing snapshot edit; it was restored unchanged afterward.

### 2026-09-07 · reported by CG-377 (Scope review validation to affected behavior and acceptance claims) in run 20260907T102236Z-work

- CG-376: scoped plans avoid unrelated whole-inventory capture review; unmapped UI consumers remain a bounded inspection point.
- The CI helper requires a clean tree; the unrelated design snapshot was temporarily stashed and restored unchanged.

### 2026-09-07 · reported by CG-339 (Review affected behavior through the running application before accepting interaction claims) in run 20260907T103105Z-revise

- The CI helper requires a completely clean tree, so the pre-existing snapshot edit had to be temporarily stashed and restored.

### 2026-09-07 · reported by CG-375 (Measure unattended stabilization by required human-owner action) in run 20260907T104101Z-work

- Pre-existing unstaged docs/design/snapshot.json required a temporary stash for the CI helper; it was restored unchanged.

### 2026-09-07 · reported by CG-376 (Make review caps optional and report excessive review loops as friction) in run 20260907T102043Z-work

- The live garden's garden.yaml is not present in this checkout, so its deployment-time review.max_rounds:null setting cannot be committed here.

### 2026-09-07 · reported by CG-295 (Docs match the mechanism: the scaffolded operate skill, design.md and roadmap.md non-goals, and the architecture module map) in run 20260907T120226Z-work

- An unrelated pre-existing docs/design/snapshot.json change made the CI helper require a temporary stash.

### 2026-09-07 · reported by CG-379 (Add a maintenance pause that safely freezes scheduling and collection) in run 20260907T115951Z-work

- The supervised focused validation queue was initially occupied; targeted maintenance tests were then run directly for diagnostic output.

### 2026-09-07 · reported by CG-376 (Make review caps optional and report excessive review loops as friction) in run 20260907T115949Z-revise

- The CI helper requires a clean worktree; a pre-existing unrelated snapshot edit was temporarily stashed and restored unchanged for CI.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T121652Z-revise

- GitHub CI required roughly six minutes per exact-commit run.

### 2026-09-07 · reported by CG-216 (Workers on independent remote hosts: a worker agent that claims runs from the garden over HTTP, works in its own clone, pushes the branch and posts the result and transcript back) in run 20260907T130341Z-revise

- An unrelated untracked docs/design/snapshot.json collided with the current-main merge and had to be preserved under a non-conflicting untracked name.
- Direct git push lacked credentials in the isolated worker home; the mandated CI helper successfully performed the authenticated push.

### 2026-09-07 · reported by CG-362 (Complete externally implemented tasks from verified PR metadata) in run 20260907T123235Z-revise

- Shared validation slot was temporarily occupied by other supervised CI runs.
- Preserved unrelated docs/design/snapshot.json changes while rebasing and running CI.

### 2026-09-07 · reported by CG-374 (Route routine recovery stops to operator actions instead of owner decisions) in run 20260907T123238Z-work

- Rebasing onto current origin/main rewrote existing branch commits, requiring a non-force merge of the assigned remote branch before CI push.

### 2026-09-07 · reported by CG-375 (Measure unattended stabilization by required human-owner action) in run 20260907T115946Z-revise

- A pre-existing docs/design/snapshot.json edit had to be temporarily stashed for CI and was restored unchanged.

### 2026-09-07 · reported by CG-380 (Attribute controller, scheduler, and worker performance under load) in run 20260907T123241Z-work

- The required CI helper refused the pre-existing unrelated snapshot modification, requiring a temporary single-file stash and restoration.
- The validation coordinator queued one short lint invocation for several minutes.

### 2026-09-07 · reported by CG-295 (Docs match the mechanism: the scaffolded operate skill, design.md and roadmap.md non-goals, and the architecture module map) in run 20260907T133954Z-revise

- A pre-existing unrelated docs/design/snapshot.json modification required a path-scoped temporary stash so check_ci.py could validate the exact commit.

### 2026-09-07 · reported by CG-381 (Make Inbox human-action counts and advice match actual ownership) in run 20260907T134113Z-work

- The broad web suite had one unrelated served-overload fixture failure after 102 passes; exact-head CI passed.

### 2026-09-07 · reported by CG-382 (Profile and reduce repeated Store scans per web request) in run 20260907T134402Z-work

- Concurrent workers share the repository stash namespace; an unrelated pre-existing snapshot change had to be preserved while CI required a clean worktree.

### 2026-09-07 · owner-authorized fast-forward integration

- CG377/CG376: actual scheduler-to-runner fixture requests zero capture pages for backend control and parser changes, task only for a task-page change, and broad consumers for shared UI. Against the historical14-page/four-variant request this is56 versus0/4 image requests in fixtures. Production rounds avoided and money saved remain unknown; use CG376 signals after deployment. Scoped preflight, current-head checks and inspection-error recovery fixed directly during fast-forward.
- CG339/CG372: self-review found synchronous180second replay under scheduler with os.environ copy; moved it to supervised detached checks and guarded priority-drain recursion. Actual integrated9-flow HTTP replay passed104requests at104.8MiB/noSwap. No production throughput or unattended-stability claim.

### 2026-09-07 · review loop for CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail)

- Review loop: 4 rounds, $4.39 cumulative work/revise/review cost; head lineage unknown; cause: unknown; actionable evidence: Most walkthrough, metrics, retro-ordering, and rail work is correct, and all 89 focused tests pass. The production walkthrough still omits the required decision-card page whenever the phase has no currently actionable decision; only the QA fixture guarantees one.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-07 · review loop for CG-294 (Planning sequences dependent tasks and inlines retro evidence into the brief)

- Review loop: 4 rounds, $3.89 cumulative work/revise/review cost; head lineage unknown; cause: unknown; actionable evidence: All four acceptance criteria are implemented and the 22-test focused planner suite passes. The description references an earlier commit, so the supplied rewrite makes the verification current without requiring another revision.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-07 · review loop for CG-295 (Docs match the mechanism: the scaffolded operate skill, design.md and roadmap.md non-goals, and the architecture module map)

- Review loop: 4 rounds, $1.93 cumulative work/revise/review cost; head lineage 784bc61624f81078c7899f17b856f2f72e8f484a, 3eb1ca38184a56499f59f39bf182506e6feafca1; cause: unknown; actionable evidence: The focused architecture test fails because `interaction_replay.py` and `preflight.py` are absent from the module map. Ruff passes and the remaining acceptance criteria are supported.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-07 · reported by CG-385 (Recover cache-limited admission through bounded reclaim and a fresh headroom check) in run 20260907T151701Z-work

- The required CI helper initially rejected an unrelated pre-existing snapshot edit; it was temporarily stashed and restored unchanged.
- The reading list marked resource and CG-383 files unresolved even though they were present in the checkout.

### 2026-09-07 · reported by CG-385 (Recover cache-limited admission through bounded reclaim and a fresh headroom check) in run 20260907T170131Z-revise

- jq was unavailable, so validation artifacts were inspected directly.

### 2026-09-07 · review loop for CG-216 (Workers on independent remote hosts: a worker agent that claims runs from the garden over HTTP, works in its own clone, pushes the branch and posts the result and transcript back)

- Review loop: 5 rounds, $28.49 cumulative work/revise/review cost; head lineage 4a1371f8e77bf01c1ea1175871aca97649ccf438; cause: stale/missing infrastructure evidence; actionable evidence: - **pre-PR check** `ui` error: UI renderer did not return a result
- **pre-PR check** `UI captures` fail: UI files changed but this run produced no PNG captures. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-07 · reported by CG-385 (Recover cache-limited admission through bounded reclaim and a fresh headroom check) in run 20260907T175548Z-revise

- The exact-head CI helper required temporarily stashing and restoring an unrelated generated snapshot edit.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T190406Z-revise

- CI validation initially required stashing a pre-existing unrelated generated snapshot modification.

### 2026-09-07 · reported by CG-378 (Refresh README for the current garden and operator workflow) in run 20260907T175551Z-work

- Shared validation leases delayed local validation while another worker awaited remote CI.
- Initial CI exposed README navigation-format coverage and two QA/canary failures; the navigation issue was repaired, both QA/canary cases passed focused reproduction, and final full CI passed.

### 2026-09-07 · reported by CG-387 (Distinguish full execution slots from resource pressure in the status banner) in run 20260907T183858Z-work

- The broad local web suite hit an unrelated served-incident setup timing failure; the exact-head GitHub CI workflow completed successfully.

### 2026-09-07 · reported by CG-216 (Workers on independent remote hosts: a worker agent that claims runs from the garden over HTTP, works in its own clone, pushes the branch and posts the result and transcript back) in run 20260907T200230Z-revise

- The CI helper requires a completely clean worktree, so the unrelated docs/design/snapshot.json edit had to be temporarily stashed and restored.

### 2026-09-07 · reported by CG-327 (The live-garden fence attributes only the worker's own writes: the operator's and the scheduler's commits during a run's window are never counted against the run) in run 20260907T200107Z-revise

- The supervised validation wrapper returned only exit-code artifacts, so focused test diagnostics were run directly after its opaque failure result.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T200102Z-revise

- A pre-existing generated docs/design/snapshot.json modification blocked the CI helper; it was temporarily stashed for CI and restored unchanged.

### 2026-09-07 · reported by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) in run 20260907T201920Z-revise

- The requested served-app replay manifest/tooling was unavailable in this checkout.

### 2026-09-07 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260907T203609Z-revise

- CI helper initially rejected the pre-existing generated docs/design/snapshot.json modification; it was temporarily stashed for CI and restored unchanged.

### 2026-09-07 · reported by CG-327 (The live-garden fence attributes only the worker's own writes: the operator's and the scheduler's commits during a run's window are never counted against the run) in run 20260907T205204Z-revise

- The shared worktree retained an unrelated docs/design/snapshot.json edit; it was temporarily stashed for CI and remains uncommitted.

### 2026-09-07 · reported by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) in run 20260907T205443Z-revise

- The required served-interaction manifest was not available for this lifecycle-only change; functional application coverage is present in the decision tests.

### 2026-09-07 · reported by CG-336 (Record Codex operator usage in the operator spend ledger) in run 20260907T210053Z-revise

- Exact-head CI required temporarily preserving an unrelated generated design snapshot.

### 2026-09-07 · reported by CG-356 (Recover onboarding cleanly when planner output is rejected) in run 20260907T211142Z-revise

- Focused validation waited for the shared heavy-test slot while another task's CI ran.

### 2026-09-07 · reported by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) in run 20260907T213639Z-revise

- CI required temporarily stashing and restoring an unrelated pre-existing docs/design/snapshot.json modification.

### 2026-09-07 · review loop for CG-327 (The live-garden fence attributes only the worker's own writes: the operator's and the scheduler's commits during a run's window are never counted against the run)

- Review loop: 4 rounds, $12.04 cumulative work/revise/review cost; head lineage 4cd2e11f3b4787ef751be57c9b3f5fd19d34ab88, 052bddd0e97addff0bf2d7213e9c0cc61fea4aa0, 95511c7ca63f8107f9f7422241a8b57a96fe7ca3, 8f1f8ddd44c7756bc6b1be5c45d132d6a5e8eb78; cause: unknown; actionable evidence: Fence behavior satisfies all three criteria, with 59 focused tests and lint passing. The interaction replay is not valid evidence because it fabricates a browser action and lists artifacts it never creates.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-07 · reported by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) in run 20260907T220325Z-revise

- Base diff check reports a pre-existing blank line at EOF in tests/test_now2_metrics.py; unrelated and not modified.

### 2026-09-07 · review loop for CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question)

- Review loop: 4 rounds, $1.90 cumulative work/revise/review cost; head lineage ee6e48504a3c97a9bf9991c8e83b2fe3e1ceb289, 00be31cafc719dc9fb0dc7766e810e5232b3ca4d, ed78d12e9cd7138bdfc79cd717df70dd9f478f21, 83af889c0aaa6ed62d91f5e85a9a244b15b9d028; cause: unknown; actionable evidence: The lifecycle fix passes focused coverage, but exact-head PR CI fails in the new no-PR regression and the required served-interaction evidence is absent.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-07 · reported by CG-336 (Record Codex operator usage in the operator spend ledger) in run 20260907T215314Z-revise

- The pre-existing docs/design/snapshot.json edit had to be temporarily stashed because the CI helper requires a clean worktree; it was restored unchanged.

### 2026-09-07 · review loop for CG-336 (Record Codex operator usage in the operator spend ledger)

- Review loop: 4 rounds, $5.62 cumulative work/revise/review cost; head lineage 7614d25420dc9febd13774b44d838dc7312938aa, db3302159576a00c56a91bfd09a52375ce99dabe, c435261f6744c16b8207b81751a1cddff574df1b; cause: unknown; actionable evidence: Codex cumulative usage, turn/model attribution, unavailable pricing, and Claude compatibility are correctly implemented and tested. The exact reviewed head passes the focused operator-spend suite and lint.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-07 · review loop for CG-362 (Complete externally implemented tasks from verified PR metadata)

- Review loop: 6 rounds, $10.07 cumulative work/revise/review cost; head lineage c872dd16401e45e185b3cf4a122ecdf2249f5586; cause: unknown; actionable evidence: The lifecycle behavior is covered by 95 passing focused tests, but final-head lint fails on a duplicated test definition. The required scheduler replay manifest is also absent at the supplied path.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-07 · reported by CG-336 (Record Codex operator usage in the operator spend ledger) in run 20260907T222324Z-revise

- CI helper requires a clean worktree; an unrelated generated design snapshot was temporarily stashed and restored unchanged.

### 2026-09-07 · reported by CG-374 (Route routine recovery stops to operator actions instead of owner decisions) in run 20260907T223627Z-revise

- The validation runner queued behind concurrent validations before starting focused checks.

### 2026-09-07 · reported by CG-375 (Measure unattended stabilization by required human-owner action) in run 20260907T224238Z-revise

- Shared one-slot validation budget delayed focused validation behind other workers.

### 2026-09-07 · reported by CG-380 (Attribute controller, scheduler, and worker performance under load) in run 20260907T224859Z-revise

- Exact-head CI required temporarily stashing and restoring an unrelated pre-existing docs/design/snapshot.json modification because the helper requires a clean worktree.

### 2026-09-08 · reported by CG-381 (Make Inbox human-action counts and advice match actual ownership) in run 20260908T021622Z-revise

- CI helper requires a clean worktree; the unrelated generated snapshot was temporarily stashed and restored.

### 2026-09-08 · reported by CG-380 (Attribute controller, scheduler, and worker performance under load) in run 20260908T022545Z-revise

- Exact-head CI required temporarily stashing and then restoring a pre-existing uncommitted generated snapshot.

### 2026-09-08 · review loop for CG-356 (Recover onboarding cleanly when planner output is rejected)

- Review loop: 4 rounds, $5.95 cumulative work/revise/review cost; head lineage 697930e297d9466dfb5bde75a92e220751a9a14d; cause: unknown; actionable evidence: The tested rejection and recovery paths work, but malformed planner data can fail during import after tasks have already been written, bypassing rollback and leaving onboarding unrecoverable.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-08 · reported by CG-356 (Recover onboarding cleanly when planner output is rejected) in run 20260908T091744Z-revise

- The CI helper requires a clean tree; the pre-existing design snapshot was temporarily stashed and restored unchanged.

### 2026-09-08 · reported by CG-387 (Distinguish full execution slots from resource pressure in the status banner) in run 20260908T095056Z-revise

- GitHub Actions polling briefly hit an API rate limit while CI was running; a backed-off query confirmed success.

### 2026-09-08 · review loop for CG-375 (Measure unattended stabilization by required human-owner action)

- Review loop: 4 rounds, $10.44 cumulative work/revise/review cost; head lineage e58f8d25d641443344d78d065a209671d5b46578, 2c94007bd0afb3bf48d38129ceafd703c33ce5fe, 220bde71b9880c7d281d71e73a27ec4b4cb4bab6; cause: unknown; actionable evidence: All four acceptance criteria are met. Actor provenance is preserved through stabilization recording and real retry paths, owner actions reset the window conservatively, and the existing stabilization gates remain intact.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-08 · reported by CG-375 (Measure unattended stabilization by required human-owner action) in run 20260908T101806Z-revise

- An unrelated generated docs/design/snapshot.json change required a temporary stash for the clean-checkout CI helper and was restored unchanged.

### 2026-09-08 · reported by CG-390 (Require screenshots only for materially changed visual behavior) in run 20260908T101232Z-revise

- Supervised validation queued behind another run's exclusive validation lease.

### 2026-09-08 · reported by CG-375 (Measure unattended stabilization by required human-owner action) in run 20260908T104605Z-revise

- The mandated nested validation wrapper propagates its lease environment into runner-spawning tests, which can contend with the parent lease during local iteration.

### 2026-09-08 · reported by CG-421 (Verify public GitHub CI from scoped AWS workers without operator credentials) in run 20260908T105002Z-work

- GARDEN_VALIDATION_RUNNER was unset in this worker environment, so its prescribed wrapper could not be invoked.

### 2026-09-08 · reported by CG-393 (Distinguish validation-slot waiting from stale-worktree idle timeouts) in run 20260908T110840Z-work

- The validation wrapper's inherited heavy-execution lease self-blocks tests/test_runners.py because that suite intentionally launches real nested supervisors; its direct focused run passed 49/49.

### 2026-09-08 · reported by CG-319 (Keep Now 1 as Now, retire Now 2, and place Now after Inbox) in run 20260908T111955Z-work

- The exact-head CI helper required a clean tree, so the pre-existing snapshot edit had to be temporarily stashed and restored.

### 2026-09-08 · reported by CG-386 (Prevent stale collected checks from reopening terminal tasks) in run 20260907T175554Z-work

- The shared validation runner queued focused tests and exact-head CI for several minutes without initial progress output.

### 2026-09-08 · reported by CG-393 (Distinguish validation-slot waiting from stale-worktree idle timeouts) in run 20260908T120731Z-revise

- jq is unavailable in the worker image; replay manifest was inspected with sed instead.

### 2026-09-08 · reported by CG-253 (The retro captures its own walkthrough, and hand merges and tick duration are in garden metrics and the rail) in run 20260908T135244Z-revise

- The initial focused command referenced nonexistent tests/test_events.py; the actual affected test paths were used successfully.

### 2026-09-08 · reported by CG-430 (Reap exited adopted children while supervised workers are still running) in run 20260908T144218Z-work

- Running the complete runner suite inside the validation wrapper self-serialized early tests that copy inherited execution-owner variables; the run was stopped, the runner suite was executed directly, and the actual validation entrypoint was exercised separately with a nesting-safe disposable fixture.
- No project typecheck command is configured; compileall was used as a lightweight syntax check in addition to tests and lint.

### 2026-09-08 · reported by CG-431 (Keep controller-owned replay checks local for remote-authored tasks) in run 20260908T152144Z-work

- Full ordinary pytest suite hung in existing test_local_runner_launch_flips_process_finished waiting on a run supervisor; validation was stopped after about 16 minutes, so no full-suite pass is claimed.

### 2026-09-08 · reported by CG-328 (Accepting a worker's no-change call on a revise round returns the task to review and queues the round; it never lands in waiting_human with no question) in run 20260908T145444Z-revise

- Full ordinary pytest wedged in an unrelated runner completion test under Python 3.14.4 and required interruption after more than 20 minutes.

### 2026-09-08 · reported by CG-332 (A task parked by a harness environment stop is dispatched again as soon as the harness resumes, without a hand) in run 20260908T153509Z-revise

- The generic replay harness does not model harness quota/auth pauses, so scoped disposable HTTP evidence was recorded alongside the dedicated scheduler regression tests.

### 2026-09-08 · reported by CG-427 (Render Codex event streams on run transcript pages) in run 20260908T155611Z-revise

- The controller pre-PR UI check attempted to read an inaccessible controller checkout and consequently did not discover the already committed captures; CG-431 owns that routing/receipt correction.
- No type-check tool is configured in this checkout; `.venv/bin/python -m mypy src` reports `No module named mypy`.

### 2026-09-08 · reported by CG-433 (Prevent LocalRunner process_finished from hanging on a completed stdin consumer) in run 20260908T160521Z-work

- The supervised validation wrapper inherits an owner-scoped lease that intentionally blocks nested LocalRunner fixtures; the direct focused runner suite was used after the wrapper attempt stalled.

### 2026-09-08 · reported by CG-433 (Prevent LocalRunner process_finished from hanging on a completed stdin consumer) in run 20260908T165157Z-revise

- Wrapper-based whole-file runner validation encountered an unrelated nested heavy-validation lease deadlock; focused lifecycle validation completed directly with explicit 30-second outer bound.
- Declined review improvement: Persist or expose the scheduler interaction manifest at a path readable from the review worker. — This runner-test cleanup change has no scheduler replay artifact to expose; changing scheduler artifact persistence would expand scope. The direct LocalRunner/supervisor tests provide inspectable lifecycle evidence.

### 2026-09-08 · reported by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) in run 20260908T170122Z-work

- The full ordinary suite reached 79%, reported an unrelated onboarding assertion affected by repository `.pytest_cache` discovery, and then stalled for over twelve minutes in `test_local_runner_launch_flips...`; focused review validation and lint completed cleanly.

### 2026-09-08 · reported by CG-423 (Scale production AWS workers through one resumable operation) in run 20260908T190859Z-revise

- The revision feedback identified only a shared validation-lock hang and no concrete product defect; the preserved external rollout artifacts were outside the allowed worktree.

### 2026-09-08 · reported by CG-428 (Keep remote worker runs alive across controller redeploys) in run 20260908T190911Z-revise

- Remote pre-PR UI checks execute on workers whose installed package may predate the candidate branch, making candidate-only callback fixes ineffective.

### 2026-09-08 · reported by CG-425 (Give the Now page beautiful, unmistakable section hierarchy) in run 20260908T191928Z-work

- No project typecheck command is configured.

### 2026-09-08 · reported by CG-448 (Align Now held-card ownership with Inbox review queues) in run 20260908T192609Z-work

- No repository typecheck command is configured.

### 2026-09-08 · review loop for CG-430 (Reap exited adopted children while supervised workers are still running)

- Review loop: 4 rounds, $3.10 cumulative work/revise/review cost; head lineage c6e8c93a621b0b0e1a55d3c69a5007a39d52eade, d804ecb4f5ec8985e19838a40e83148dce88b5b2; cause: unknown; actionable evidence: The supervisor promptly reaps adopted exits while preserving leader status, termination escalation, descendant draining, and validation-slot ownership. Exact-head focused tests, lint, and the disposable served replay pass; the broader WSL incident remains a separate investigation.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-08 · reported by CG-437 (Escalate revision difficulty and surface explicit troubled-task decisions) in run 20260908T215800Z-revise-2

- The frozen validation plan stated no rendered behavior changed even though the task and implementation materially change the Inbox decision journey.

### 2026-09-08 · reported by CG-430 (Reap exited adopted children while supervised workers are still running) in run 20260908T221525Z-revise

- Wrapping runner lifecycle tests in an inherited validation lease deadlocks fixtures that intentionally launch their own supervisors; the exact-head focused suite passed with validation ownership variables removed so those fixtures could exercise their own lease behavior.

### 2026-09-08 · reported by CG-428 (Keep remote worker runs alive across controller redeploys) in run 20260908T215800Z-revise

- The bounded full suite exposed one checkout-remote-dependent onboarding assertion unrelated to this task after 1,719 passing tests.

### 2026-09-08 · reported by CG-385 (Recover cache-limited admission through bounded reclaim and a fresh headroom check) in run 20260908T225432Z-revise

- The brief-required `context-garden/product.md` and `context-garden/phase-05/goals.md` paths do not exist in this product worktree; their content was supplied inline.
- A pre-existing unrelated modification to `docs/design/snapshot.json` remained in the worktree and was deliberately excluded from the commit.

### 2026-09-08 · review loop for CG-385 (Recover cache-limited admission through bounded reclaim and a fresh headroom check)

- Review loop: 4 rounds, $12.36 cumulative work/revise/review cost; head lineage 11064356128f6aec9b3614f43ec88c70f09302fb, 813c3c721afaa46e913c93f36a881caa819c4111, 2f001bcc08c4590e7a8e88186defa8563dfe3a0c, 4704288bd94be661892d08f1cf39a24ec5da6ae6; cause: unknown; actionable evidence: The reclaim implementation passes lint and 25 focused tests, but required reviewed-head evidence is missing: the replay never exercises reclaim and exact-head CI is not reported. The branch must also be reconciled with current main.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-08 · reported by CG-430 (Reap exited adopted children while supervised workers are still running) in run 20260908T224525Z-revise

- The full ordinary suite showed failures but timed out at 900 seconds before pytest emitted named tracebacks.
- GitHub Actions status could not be queried because the worker has no GH_TOKEN or authenticated gh session.

### 2026-09-08 · reported by CG-386 (Prevent stale collected checks from reopening terminal tasks) in run 20260908T231841Z-revise

- The brief-listed `context-garden/product.md` and `context-garden/phase-05/goals.md` paths do not exist in this product worktree; the equivalent product and phase context was already inlined in the brief.
- No configured typecheck command or mypy/pyright executable exists in the prepared environment, so there was no project typecheck to run.

### 2026-09-09 · reported by CG-428 (Keep remote worker runs alive across controller redeploys) in run 20260909T001659Z-revise

- The purported main base probe actually ran the CG-428 branch head, so it could not establish main’s lint state.

### 2026-09-09 · reported by CG-453 (Reduce the ordinary test suite runtime below eight minutes) in run 20260908T230115Z-revise

- The prepared AWS environment excluded dependency/browser installation and exposed no trustworthy setup-duration receipt, while worker rules prohibited rerunning package installation.

### 2026-09-09 · reported by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) in run 20260908T235138Z-revise-2

- The full-suite onboarding metadata assertion and two remote-worker subprocess timeouts reproduce on exact focused rerun despite all affected paths being unchanged from origin/main.
- A second supervised Ruff invocation returned no diagnostic output after the full-suite run; the earlier exact-source Ruff run completed with `All checks passed!`.

### 2026-09-09 · review loop for CG-381 (Make Inbox human-action counts and advice match actual ownership)

- Review loop: 4 rounds, $15.64 cumulative work/revise/review cost; head lineage 2f75bbf99ae5791bd41c5963d463da796917d6e4, cdcb4b9ebc68a40ab113c4df68f8d33fa4a51dbe, b13efb86c29c9b78c87c3a039c96749d898f2b11; cause: unknown; actionable evidence: Core ownership behavior is well covered by focused tests, but this head lacks the required affected Inbox interaction and exact-head CI. It also globally expands scoped Inbox captures to an unrelated task page.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T003625Z-work

- Open EventSource connections required a bounded forced shutdown in the disposable capture runner and emitted harmless cancellation diagnostics.

### 2026-09-09 · reported by CG-444 (Support configured SSH ports in canonical enterprise repository identity) in run 20260909T011350Z-revise

- No mypy or pyright configuration or installed module is available in this checkout; typecheck is not applicable.

### 2026-09-09 · reported by CG-392 (Reconcile remaining architecture and worker-protocol statements with implementation) in run 20260909T025632Z-work

- A pre-existing modification to docs/design/snapshot.json was present and intentionally left untouched.

### 2026-09-09 · reported by CG-392 (Reconcile remaining architecture and worker-protocol statements with implementation) in run 20260909T034358Z-revise

- No dedicated typecheck command is configured in this checkout.

### 2026-09-09 · reported by CG-386 (Prevent stale collected checks from reopening terminal tasks) in run 20260909T034111Z-revise

- The brief-listed context-garden/product.md and context-garden/phase-05/goals.md files were not present in this worker checkout.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T034634Z-revise

- The successful browser replay emits noisy ASGI CancelledError traces while closing screenshot stream connections.
- Declined review improvement: Add optional UI scope mapping for the three Now templates. — The revision changes only the existing live event mapping, not rendered scope; the tracked Now replay and captures already identify the affected page.

### 2026-09-09 · review loop for CG-428 (Keep remote worker runs alive across controller redeploys)

- Review loop: 4 rounds, $25.47 cumulative work/revise/review cost; head lineage 6138c793f1315f939e4e649a5578d946aa0ec8db, a9c1cacbb209bd2a23584cd82f354b1289ca6113, 91c3aefb2827c058da63b51eb5d5b87a2fb54129, 64b8e4faceb9a5b18ad9a4eca60b06df060384cf; cause: unknown; actionable evidence: Remote work survives bounded controller outages while stale, revoked, expired, and replaced generations remain fenced. Transcript and finish replay are durable and idempotent, and reconnecting state is surfaced clearly.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-389 (Negotiate capture CLI compatibility and diagnose renderer exit before requesting revisions) in run 20260909T094246Z-revise

- No project type-check command is configured; focused tests and Ruff were run.

### 2026-09-09 · reported by CG-465 (Omit unattached-artifact commentary from automated reviews) in run 20260909T094730Z-revise

- GitHub CLI is unauthenticated in this worker, so open PR comments and remote CI status could not be queried directly.

### 2026-09-09 · reported by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) in run 20260909T094250Z-revise

- Six interaction-replay tests expect mandatory replay dispatch even though current scheduler policy explicitly disables mandatory interaction admission under reviewer judgment.

### 2026-09-09 · review loop for CG-438 (Preserve review requests through unclaimed timeout and admission recovery)

- Review loop: 4 rounds, $13.04 cumulative work/revise/review cost; head lineage 7a9f8969e7c8f56f45bfa2dcba6ce0b75c4e4304, d42c82366df5f35ce5455725561a81a9954c94ce, cfeb8d6d799a5406d6434db70859eb972ea775b4, cacaa015fd113b3213195c8cf731663e144b6eba, f82bb07ee888d349addd376ec1b4edca19550acf; cause: unknown; actionable evidence: Started reviews ending in environment errors still lose collected usage and cost from their durable run records.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T094728Z-revise

- The worker intentionally lacks authenticated GitHub CLI access, so the failed workflow log was unavailable; public API metadata still exposed the duplicate passing run at the same SHA.

### 2026-09-09 · reported by CG-465 (Omit unattached-artifact commentary from automated reviews) in run 20260909T095810Z-revise

- The failed pull-request CI log could not be retrieved because GitHub CLI/API log access lacks authentication; the same SHA's push CI test run passed.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T100331Z-revise

- The actions analyser cannot authenticate GitHub CLI because the validation environment provides neither a gh login nor GH_TOKEN.

### 2026-09-09 · review loop for CG-455 (Redesign the Now page top summary as a useful thematic measurement)

- Review loop: 4 rounds, $5.47 cumulative work/revise/review cost; head lineage af74457a62f830ea1e6cbdb308bc2d2608d8655d, a06c1658976e44f3240de4b0709dbc136e546cb7, 7507b41acdfaf65b8906aa7c8cace3e09ffdc557; cause: unknown; actionable evidence: The field reading is clear, authentic, actionable, and responsive; the prior stale-capacity issue is resolved.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) in run 20260909T095937Z-revise

- The GitHub Actions status check could not authenticate because the environment has neither gh login state nor GH_TOKEN.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T101823Z-revise

- The optional GitHub Actions analyser cannot inspect remote checks because this worker has no authenticated gh session or GH_TOKEN.

### 2026-09-09 · reported by CG-465 (Omit unattached-artifact commentary from automated reviews) in run 20260909T101823Z-revise-2

- The supplied Actions check failure requires GitHub CLI authentication; no credentials are available in this worker.

### 2026-09-09 · review loop for CG-465 (Omit unattached-artifact commentary from automated reviews)

- Review loop: 4 rounds, $1.55 cumulative work/revise/review cost; head lineage bbad1846c4eb9f0b15cceabcac89fe11e2fa5627, 0b551e4cac723d9aaf871d7c7acd9cd774fe8090; cause: unknown; actionable evidence: Automated reviews now suppress optional unattached-artifact and metadata commentary while retaining internal diagnostics and genuine blockers.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T102341Z-revise

- The optional GitHub Actions analyser cannot run because the worker environment has no authenticated gh session.

### 2026-09-09 · reported by CG-465 (Omit unattached-artifact commentary from automated reviews) in run 20260909T103732Z-revise

- The failed CI test log is unavailable in this environment; the separate Actions check is blocked by missing GitHub CLI authentication.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T103731Z-revise

- The actions analyser requires GitHub CLI authentication unavailable on the worker; `gh auth status` exits 1 with the same setup message reported by CI.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T110520Z-revise

- The `actions` analyzer cannot authenticate because neither GitHub CLI credentials nor GH_TOKEN are available to the worker.
- The successful served replay logs benign ASGI CancelledError traces while shutting down open event streams.

### 2026-09-09 · reported by CG-437 (Escalate revision difficulty and surface explicit troubled-task decisions) in run 20260909T111209Z-revise

- The brief referenced context-garden/product.md and context-garden/phase-05/goals.md, but those paths are absent from this worktree.
- Declined review improvement: Add optional UI scope mapping metadata. — No configured mapping artifact or functional defect was identified; the changed Inbox interaction is directly covered by a rendered-form and submission regression.
- Declined review improvement: Act on the unavailable reviewer pre-check result. — Current-head focused tests and lint were run successfully; no source correction follows from a prior unavailable advisory check.

### 2026-09-09 · review loop for CG-437 (Escalate revision difficulty and surface explicit troubled-task decisions)

- Review loop: 7 rounds, $17.93 cumulative work/revise/review cost; head lineage 2906e069895c35ec46b1d31625a397d1bc11578b, a4279b47914ee033bde192ef10d37078a5af8f05, f70dc75edd421f5fa84971652bbcedbd1ded74dc, dff8c64ed53fd006d8367dd24f5508d76da0ba1f, 97ef703fd2228f9fad46ad75720859812539f8fb; cause: unknown; actionable evidence: The core escalation and investigation lifecycle is substantially implemented, but two policy/action paths do not honor their configured or displayed behavior.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-437 (Escalate revision difficulty and surface explicit troubled-task decisions) in run 20260909T112630Z-revise

- The required context-garden/product.md and context-garden/phase-05/goals.md paths are absent from this worktree.
- Declined review improvement: Optional UI scope mapping omitted for the touched web files — No concrete mapping format or functional defect was identified; the focused rendered-form regression directly covers the changed Inbox behavior.

### 2026-09-09 · reported by CG-438 (Preserve review requests through unclaimed timeout and admission recovery) in run 20260909T123529Z-revise

- The triage note identified the first failing transition assertion, but once restored the same tests exposed a subsequent redundant-backoff failure; both were resolved without weakening assertions.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T124456Z-revise-2

- The served replay logs benign ASGI CancelledError traces while closing open event-stream requests, although it exits successfully.
- Declined review improvement: Add optional UI scope mapping for the three Now templates. — The nit supplied no required mapping format or concrete UI defect; the existing focused page tests and scoped Now replay directly cover the affected surface.

### 2026-09-09 · reported by CG-465 (Omit unattached-artifact commentary from automated reviews) in run 20260909T125425Z-revise

- The supplied saved GitHub Actions failure log was unreadable from this worker (Permission denied); the named canary test passed locally on the current checkout.
- No type checker is configured in pyproject.toml or CI.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T130916Z-revise

- The served replay emits benign ASGI cancellation traces while shutting down, despite completing successfully and confirming the server thread exited.
- Declined review improvement: Add optional UI scope mapping for the three Now templates. — No repository mechanism or concrete mapping target was identified; the final diff, replay receipt, and page-specific captures already scope the affected rendered surface explicitly.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T132910Z-revise

- The served replay passes but uvicorn logs benign CancelledError traces while shutting down open SSE connections.
- Declined review improvement: Add optional UI scope mapping for the three Now templates. — The feedback identified no functional defect or required mapping format; the branch and existing design documentation already scope the visual change to the Now summary.

### 2026-09-09 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260909T124614Z-revise

- The listed context-garden/product.md and context-garden/phase-05/goals.md paths are absent from this product checkout; their content was available in the supplied brief.
- GitHub review and CI could not be queried directly because gh has no authentication in the worker environment.
- Declined review improvement: Add optional UI scope mapping for src/garden/web/pages/api.py. — The endpoint change only stores remote validation receipts and does not alter rendered appearance or interaction behavior; path-based UI evidence is explicitly advisory under current owner policy.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T134213Z-revise

- The successful served replay emits noisy Uvicorn CancelledError traces while closing long-lived event streams, although it exits successfully and confirms the server thread stopped.
- Declined review improvement: Provide optional UI scope mapping metadata for the three Now templates. — No concrete render, accessibility, or synchronization defect was identified, and the focused diff, tests, replay, and captures already establish the affected UI scope.

### 2026-09-09 · reported by CG-455 (Redesign the Now page top summary as a useful thematic measurement) in run 20260909T140820Z-revise

- Declined review improvement: Add optional UI scope mapping for the three Now templates. — The reviewer identified no functional defect or established mapping artifact; the change is already confined to the existing Now page and covered by focused tests and rendered interaction evidence.

### 2026-09-09 · reported by CG-480 (Make Inbox recovery prompts actionable and distinguish operator work from user decisions) in run 20260909T142731Z-revise

- Declined review improvement: Optional UI scope mapping for the decision-card and Inbox templates — No concrete defect or required mapping format was identified; targeted rendered tests directly cover the changed behavior.

### 2026-09-09 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260909T145739Z-revise

- The listed context-garden/product.md and context-garden/phase-05/goals.md paths do not exist in this worktree; their relevant contents were included in the supplied brief.

### 2026-09-09 · reported by CG-480 (Make Inbox recovery prompts actionable and distinguish operator work from user decisions) in run 20260909T151104Z-revise

- Declined review improvement: Add optional UI scope mapping for task.py, _decision_card.html, and inbox.html. — The review identified no concrete defect or required mapping mechanism; targeted rendered tests already cover the affected shared decision-card output.

### 2026-09-09 · reported by CG-479 (Optimize Garden page load times) in run 20260909T151342Z-revise

- The first revised benchmark attempt exposed an open Now-page SSE connection preventing isolated Uvicorn shutdown; the attempt was stopped, the harness was fixed, and only the successful rerun was reported.

### 2026-09-09 · reported by CG-437 (Escalate revision difficulty and surface explicit troubled-task decisions) in run 20260909T142544Z-revise

- Two required contextual reading-list paths, context-garden/product.md and context-garden/phase-05/goals.md, were absent from this checkout; the inlined brief and available repository documentation supplied the needed context.
- Declined review improvement: Add optional UI scope mapping for the touched web templates/actions. — This revision changes no rendered behavior or template markup; the frozen validation plan explicitly identifies no rendered-evidence requirement.

### 2026-09-09 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260909T151719Z-revise

- The supplied context-garden/product.md and context-garden/phase-05/goals.md paths were absent from this checkout; their contents were available inline in the task brief.
- Declined review improvement: Add optional UI scope mapping for src/garden/web/pages/api.py and src/garden/web/templates/task.html. — The receipt persistence and CI admission changes do not alter rendered behavior; adding visual scope would mischaracterize this backend-only revision.

### 2026-09-09 · review loop for CG-434 (Enforce current validation policy on old and stacked worker branches)

- Review loop: 4 rounds, $17.50 cumulative work/revise/review cost; head lineage 6fa3d5d0a1a60981727cf3f03acd35f84bae4330, 7a47262e55fe4240312a3eb46c9d4a371d1c5141, 9cff1f43bde5b073609034a07df69e8728eee4ff, e47ff030c497368c76c05903012a2364ef922069, 620794838e7f68b79f535ceeff0f7b4edd5e3fd2; cause: unknown; actionable evidence: Current-source validation behavior is well covered, but remotely supplied incomplete receipts can still satisfy the authoritative worker-check CI gate.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-480 (Make Inbox recovery prompts actionable and distinguish operator work from user decisions) in run 20260909T161455Z-revise

- Declined review improvement: Add optional UI scope mapping for task.py, _decision_card.html, and inbox.html — No concrete defect or required mapping mechanism was identified; the affected rendered behavior is covered directly by focused web and attention tests.

### 2026-09-09 · review loop for CG-480 (Make Inbox recovery prompts actionable and distinguish operator work from user decisions)

- Review loop: 4 rounds, $9.21 cumulative work/revise/review cost; head lineage caa1dd04122f13436dd5f64f2e013fe49b413182, 38accf6e81eefc3be58dc8b41f421f8741d7ca65, 6b080fe80d80016f2db2d57c51bb928455d5b2d6, c1ed4c1077d34a690f90f5e619d72bce0e9c5fb9; cause: unknown; actionable evidence: Interrupted CI recovery remains insufficiently guarded against stale PR heads, and an applicable focused web test fails.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-485 (Show accurate remote and manual run lifecycle without phantom process slots) in run 20260909T162039Z-revise

- Declined review improvement: Add further UI scope mapping beyond `_board.html` and `_now1_macros.html`. — Those templates are the direct Board and Now lifecycle presentation consumers; no concrete missing UI behavior was identified.

### 2026-09-09 · reported by CG-480 (Make Inbox recovery prompts actionable and distinguish operator work from user decisions) in run 20260909T163230Z-revise

- Declined review improvement: Add optional UI scope mapping for the previously changed templates and task page — This revision changes only scheduler recovery validation and tests; no rendered source or visual behavior changed, so additional UI scope metadata would not verify the reported defect.

### 2026-09-09 · reported by CG-437 (Escalate revision difficulty and surface explicit troubled-task decisions) in run 20260909T170045Z-revise

- The brief referenced context-garden/product.md and context-garden/phase-05/goals.md, which are not present in this checkout.
- The reported GitHub Actions analyser could not authenticate because the runner has neither gh login nor GH_TOKEN; local reproduction nevertheless found and fixed two genuine source-test failures.

### 2026-09-09 · reported by CG-417 (Reuse a fresh task snapshot within one controller operation) in run 20260909T173258Z-revise

- A merge-base diff included unrelated historical main divergence; direct task-commit diff was clean.

### 2026-09-09 · reported by CG-437 (Escalate revision difficulty and surface explicit troubled-task decisions) in run 20260909T173505Z-revise

- The required context-garden/product.md and context-garden/phase-05/goals.md paths were absent from this product checkout; equivalent task context was supplied inline in the brief.

### 2026-09-09 · reported by CG-480 (Make Inbox recovery prompts actionable and distinguish operator work from user decisions) in run 20260909T173507Z-revise

- Declined review improvement: Optional UI scope mapping for task.py and Inbox templates — This revision changes only scheduler provenance validation and test fixtures; the frozen validation plan explicitly identifies no rendered or lifecycle presentation change.

### 2026-09-09 · reported by CG-491 (Recover idle worker claims after transient or lost claim responses) in run 20260909T174137Z-revise

- GitHub CLI was unauthenticated, but the public Actions API exposed both job step summaries; detailed zipped logs require authentication.

### 2026-09-09 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260909T175130Z-revise

- The brief-listed context-garden/product.md and context-garden/phase-05/goals.md paths do not exist in this checkout.

### 2026-09-09 · reported by CG-437 (Escalate revision difficulty and surface explicit troubled-task decisions) in run 20260909T175722Z-revise

- The check feedback provides only a GitHub CLI authentication error and no failing pytest node or log.

### 2026-09-09 · reported by CG-480 (Make Inbox recovery prompts actionable and distinguish operator work from user decisions) in run 20260909T175859Z-revise

- The reported GitHub Actions check could not authenticate because its environment lacks gh credentials; this is separate from the passing focused source tests.

### 2026-09-09 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260909T185122Z-revise

- The brief-listed context-garden/product.md and context-garden/phase-05/goals.md were absent from this checkout; repository architecture, design, worker-protocol, and test-suite documentation were available and read.
- The reported GitHub Actions detail requires unavailable gh authentication, so CI was reproduced with affected local suites rather than polling GitHub.

### 2026-09-09 · reported by CG-493 (Retain RC14 discovery and CI guards) in run 20260909T194245Z-revise

- GitHub started duplicate workflows for the same SHA; one passed fully while the other had a non-reproducing canary failure.

### 2026-09-09 · review loop for CG-486 (Recover managed workers from failed checkout materialization)

- Review loop: 4 rounds, $4.66 cumulative work/revise/review cost; head lineage 975c70b6c2c4a88feb24327379c7843fcd4e590b, c596ca745c105f4dd56f3e36cadff44c145fcfaa, 944d7879fd8c73e01a3d96436a0fb10045fdc8bf; cause: unknown; actionable evidence: Core checkout recovery passes, but repository-lock materialization errors still escape the managed claim loop without a structured finish.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-09 · reported by CG-494 (Show standalone scheduler health and coordinate manual ticks) in run 20260909T215255Z-work

- The brief requests a typecheck, but the repository has no configured type checker or typecheck dependency.

### 2026-09-09 · reported by CG-494 (Show standalone scheduler health and coordinate manual ticks) in run 20260909T221135Z-revise

- The repository has no configured mypy or pyright type-check command; Ruff and focused runtime tests were used for the typed changes.

### 2026-09-09 · reported by CG-384 (Show deployed release identity and validate release artifacts) in run 20260909T232532Z-work

- The brief referenced docs/release-protocol.md, but it was absent on this branch; the release protocol was added as part of the change.

### 2026-09-09 · reported by CG-496 (Integrate the validated RC16 Now refresh into current main) in run 20260909T200930Z-work

- The successful browser replay emitted noisy Uvicorn CancelledError traces during controlled server shutdown.

### 2026-09-09 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260909T200813Z-revise

- The listed context-garden/product.md and context-garden/phase-05/goals.md paths do not exist in this product checkout; their relevant content was supplied inline in the brief.

### 2026-09-09 · reported by CG-384 (Show deployed release identity and validate release artifacts) in run 20260909T234848Z-revise

- Worker policy prohibits pushing, so fresh exact-head CI must be triggered by the runner after publication.

### 2026-09-10 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260910T005959Z-revise

- The brief listed context-garden/product.md and context-garden/phase-05/goals.md, but those paths are absent from this product checkout; the inlined brief supplied their relevant content.

### 2026-09-10 · reported by CG-434 (Enforce current validation policy on old and stacked worker branches) in run 20260910T014431Z-revise

- The listed context-garden/product.md and context-garden/phase-05/goals.md paths do not exist in this checkout; the equivalent material was inlined in the brief.

### 2026-09-10 · reported by CG-490 (Remove redundant two-review-round automerge hold for hard tasks) in run 20260910T015143Z-revise

- A base-range whitespace scan reports pre-existing generated replay artifacts outside this task; the revision itself passed git diff --check.

### 2026-09-10 · review loop for CG-494 (Show standalone scheduler health and coordinate manual ticks)

- Review loop: 4 rounds, $5.76 cumulative work/revise/review cost; head lineage 53974823153441486d48765f23b52e584a1715e5, 19fb3595a00cc99dc86f5c053292c77ab13b2624, dc55113a6032b8e31ebcdcfbde309a9a9a602734, 453100061f822d0b0c22b7863a7f72796fca363b; cause: unknown; actionable evidence: Locking and displayed state behavior are covered, but accumulated historical leases can hide the active watcher and falsely report it missing.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-536 (Make accepted-task costs and phase comparisons trustworthy) in run 20260910T151836Z-revise

- The prescribed typecheck could not be run because the repository has no configured type checker.

### 2026-09-10 · reported by CG-585 (Repair the RunStore import cycle on merged main) in run 20260910T145928Z-work

- The supplied incident reading-list path was unresolved, as already recorded in the brief.
- The final full suite exposed three failures outside the import/locking change; two passed in focused reruns, while the QA output assertion failed independently.

### 2026-09-10 · review loop for CG-536 (Make accepted-task costs and phase comparisons trustworthy)

- Review loop: 4 rounds, $11.58 cumulative work/revise/review cost; head lineage 2532823b6fc4fee854b2895cf8e575dc7b25259d, 20f6960cf62bf261e8c5bfd4e5b98aff3a40ca8a, e7b746535d1218753e36d385aefca10eff803744, cd97a38ed4a4dd20c898f6d331b1898a5cb2a021; cause: unknown; actionable evidence: The shared worker acceptance cohort is substantially improved, but unknown-priced operator spending is still silently converted to absence/zero and the Costs page uses inconsistent short-phase filtering.. Prevention work: CG-374 (routine recovery), CG-372 (review admission), CG-323 (worker preflight), CG-339 (proportional application evidence).

### 2026-09-10 · reported by CG-536 (Make accepted-task costs and phase comparisons trustworthy) in run 20260910T163758Z-revise

- The exact-head full suite had one unrelated transient store-discovery cache failure after 2,483 passes; the failing node passed alone immediately afterward.
- No static typecheck command or configuration exists in the repository.

### 2026-09-10 · reported by CG-593 (Repair merged-main operator metrics and import-order regressions) in run 20260910T173819Z-work

- No project type-check command was configured in the inspected project files.

### 2026-09-10 · reported by CG-600 (Finish model runs when a harness replaces the final-output FIFO) in run 20260910T222043Z-work

- The immutable RC19 validation supervisor itself exhibited the reported childless final-reader deadlock after completed pytest runs, requiring termination of only those test-validation supervisors; installed source was not hotpatched.
- No standalone typecheck command is configured in the repository.

### 2026-09-10 · reported by CG-600 (Finish model runs when a harness replaces the final-output FIFO) in run 20260910T231031Z-revise

- Current-head CI and renewed independent review cannot occur until the controller publishes the committed revision.

### 2026-09-11 · reported by CG-600 (Finish model runs when a harness replaces the final-output FIFO) in run 20260910T234412Z-revise

- The required 900-second full-suite ceiling expired at 90% before pytest could identify or summarize the second observed failure.

### 2026-09-11 · reported by CG-601 (Isolate old-branch validation policy fixtures from inherited pytest options) in run 20260911T030310Z-revise

- No type-check command is configured in pyproject.toml.

### 2026-09-11 · reported by CG-601 (Isolate old-branch validation policy fixtures from inherited pytest options) in run 20260911T032841Z-revise

- Exact-head CI and independent review are scheduler-owned and unavailable from this worker.

### 2026-09-11 · reported by CG-620 (Keep collection continuations behind durable Run finalization) in run 20260911T032842Z-work

- Exact-source ordinary CI could not pass on this host because the canary's scheduler resource gate requires 20 GB free disk and the host exposed about 8.9 GB.

### 2026-09-11 · reported by CG-622 (Bound branch cleanup reference matching at real scheduler state scale) in run 20260911T060230Z-work

- The referenced cleanup-reference-scaling diagnosis did not resolve and was unavailable; implementation used the frozen criteria and current checkout source.

### 2026-09-11 · reported by CG-623 (Honor explicit operator stabilization acceptance without rewriting measured evidence) in run 20260911T103209Z-work

- The broader tests/test_retro_verdict.py run was deferred by the environment resource-pressure gate because about 7.3 GiB was available versus the configured 20 GiB reserve; 5 tests passed and 9 setup-dependent tests failed before retro launch.
