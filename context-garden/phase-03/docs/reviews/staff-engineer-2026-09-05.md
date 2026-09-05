# staff-engineer review of context-garden/phase-03

**Persona:** staff-engineer · **Score:** 7/10 · 2026-09-05T10:21:05+00:00

Structurally the phase did what it promised: scheduler mixins, an action registry, in-process tests, trust edges closed without new dependencies, and a green suite. The maintenance cost is in what got copied rather than shared: the mechanical rebase now exists four times and only two copies feed the metric the phase is judged by; approve is written five times and the TUI copy skips the freeze gate; merge-queue state is written from seven places. One definition-of-done item, config changes without a restart, was not built and the Config page says so. The dispatch phase of tick is the one unguarded step, cost accounting still has a double-emit window, and the qa sandbox's GitHub stand-in already lags the real interface.

## High

- **scheduler/rebase** — The sync-rebase-force-push sequence is implemented four times and only mechanical_rebase and _reprobe_base_broken record a rebase run, so garden metrics undercounts rebases per merge.
  - suggestion: One _rebase_branch(task, base, reason, record=True) helper used by mechanical_rebase, _reprobe_base_broken, _restack and _handle_failed_checks; test that a restack and a stale-base rebase each leave exactly one rebase run_finished event.
- **layering/gates** — Approve is written five times across CLI, web and TUI, the TUI copy has no phase_refusal check, and the web done action bypasses _transition so CG-175's stop cleanup and the transition event never run.
  - suggestion: Add Scheduler.approve and Scheduler.mark_done that go through _transition and phase_refusal, and make every surface call them; test that a TUI approve into a frozen phase is refused.

## Medium

- **operability/config** — The definition-of-done item that a garden.yaml change takes effect within one tick was not built: Config loads once in Store.__init__, invalidate never reloads it, and the Config page tells the operator to edit YAML and restart.
  - suggestion: Reload Config in Store.invalidate when a source file's mtime changed and have Scheduler read store.config per tick; test that a max_parallel change between two ticks is honoured by the second.
- **scheduler/tick** — dispatch_edits and dispatch_ready are the only tick phases not wrapped in try/except, and state.save() is not in a finally, so an exception there drops unflushed state from reap, poll and the merge queue.
  - suggestion: Wrap the dispatch calls like the other phases and move self.state.save() into a finally; test with dispatch_ready raising that reap's state changes still reach disk.
- **events/cost** — finalize emits run_finished before the first terminal run.save(), so a kill during the fence check re-emits it, and digest/metrics sum every run_finished with no de-duplication by run id.
  - suggestion: Key cost by run id in events.digest and events.metrics with last event winning; test that two run_finished events for one run count once.
- **scheduler/merge queue** — merge_head, automerge_candidate, automerge_ready_at and automerge_blocked are written from seven places, and _current_merge_head exists partly to clean up markers other paths forgot.
  - suggestion: Make _queue_hold and _queue_leave the only writers of queue state so the next semantic change touches one function.
- **test doubles** — FakeGitHub and MemoryGitHub imitate GitHub with no shared contract; MemoryGitHub lacks reopen_pr, branch_exists, base_ref_deleted and is_trusted, so a garden qa flow on the base-deleted path raises AttributeError.
  - suggestion: Declare a GitHubLike Protocol in github.py and add one test asserting both fakes implement every public method of GitHub.

## Low

- **scheduler/review** — Deferred review batches are appended without de-duplication and a CG-177 test asserts two pending entries for two identical requests, which drain into two review rounds against review.max_rounds.
  - suggestion: De-duplicate pending_reviews by kind and persona name on append and change the test to expect one.
- **cli** — cli.py is 1995 lines and absorbed freeze, unfreeze, pr, doctor, qa, walkthrough and retro this phase.
  - suggestion: Split it into a cli/ package by command family, mirroring the web actions split.
- **tests/runner** — The real LocalRunner.launch shell wrapper and pid-based process_finished are covered only by two Popen-stubbed tests now that every scheduler test uses the in-process runner.
  - suggestion: Add one opt-in slow-marked test that runs LocalRunner.launch with the fake harness end to end.
- **tests/assertions** — Several new tests assert on task-log prose such as the verdict-kept line when an event carrying the same fact is emitted beside it.
  - suggestion: Assert on the rebase and merge_head events instead of log text so wording can change freely.
- **state store** — _TaskState.__getitem__ snapshots mutable values but dict.get is not overridden, so an in-place mutation of a value obtained via st.get would be invisible to save().
  - suggestion: Override get to snapshot mutable values the same way and add a test.

_garden persona run 20260905T101540Z-persona_
