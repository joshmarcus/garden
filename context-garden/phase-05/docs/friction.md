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
