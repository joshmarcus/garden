# staff-engineer review of context-garden/phase-02-friction

**Persona:** staff-engineer · **Score:** 6/10 · 2026-09-05T02:48:52+00:00

The phase delivered substantial, well-tested operability work: the base probe, the worktree fence, atomic state and task writes, automerge gates, the stuck audit, and structured decision cards. The cost is concentrated in scheduler.py, now a 3,200-line single class that every PR touched: the run-collection block is copied seven times with drifting status rules, one fix landed twice in retry(), and the remote-commit rule from CG-129 covers only one of three rebase paths. Two defects were confirmed by reproduction: the state-file merge-on-save marks keys dirty on read, so a read-only tick clobbers a concurrent 'garden set' despite the architecture doc's guarantee, and a resumed reap re-emits run_finished so event-derived cost double-counts. Four flake-fix PRs point at the subprocess-driven test style. Everything here is fixable now and compounds if left.

## High

- **state.json concurrency** — _TaskState marks a key dirty on any read of a nested dict or list (and on setdefault), so a tick that only reads _control.overrides writes it back and clobbers a concurrent 'garden set'; reproduced.
  - suggestion: Snapshot entries at load and compute dirty keys by value comparison at save so reads never dirty; add a test where a read-only State saves after another process's write and the write survives; correct the architecture doc.
- **scheduler structure** — Scheduler is a 3,200-line single class touched by every PR; the finished-run collection block is duplicated seven times with different status rules and retry() cancels the active run twice.
  - suggestion: Add Run.finish(runner) owning collect/status/save; move trials, personas, retro, upgrade, fence and suggestions into modules that take the scheduler as a collaborator; delete the duplicate cancel block in retry().

## Medium

- **events / cost accounting** — A resumed reap (CG-083) re-runs finalize() and re-emits run_finished, so digest, metrics and phase_summary count the run's cost twice; reproduced (0.10 vs 0.05).
  - suggestion: Emit run_finished once where the run record goes terminal, guarded by a flag on the run; extend the interrupted-reap test to assert a single event.
- **needs_human shape** — Four sites (_start_check_revise x2, _fence_fail, _audit_stuck) still write bare strings, so the Inbox guesses the kind and a fence violation renders as 'The loop stalled'.
  - suggestion: Route all stops through _set_needs_human with explicit kinds (check_unfinished, fence, stuck) and collapse the repeated set/emit/notify/transition ritual into one method; test each kind's card title.
- **rebase paths** — sync_remote_branch (CG-129) runs only in _restack; _handle_pr_conflict and the moved-base branch of _handle_failed_checks still rebase and force-push without it, and force=True is a bare --force-with-lease right after a fetch.
  - suggestion: One _rebase_branch helper that always syncs remote-only commits before rebasing, used by all three paths; mirror test_restack_keeps_remote_only_commits for the conflict path.
- **test determinism** — Scheduler tests drive real subprocess fake workers and real git; four PRs this phase were flake fixes from tick/worker timing.
  - suggestion: Add a synchronous in-process test Runner that completes in start(), use it for state-machine tests, keep subprocess fakes for runner/harness tests only.

## Low

- **CLI layering** — garden doctor holds ~115 lines of checks (auth, git identity, self-product and work_dir refusals) in cli.py, unusable from the web Configuration page.
  - suggestion: Move to a doctor.py returning structured check results and render from both CLI and web.
- **consistency hazards** — draft_pr is read with default False for the API call and True for the stored flag; the scheduler's timeout ignores per-runner config; the CI retry_command has no TimeoutExpired handling after state was mutated; the base probe re-runs setup and checks per task with no cache keyed on base sha.
  - suggestion: Read draft_pr once; pass the runner's timeout into _finished_or_timed_out; wrap retry_command; cache probe results in state keyed on (base_sha, check name).

_garden persona run 20260905T024302Z-persona_
