---
name: garden-operate
description: Observe and troubleshoot a live context-garden loop as its operator. Use when the user says "watch the garden", "what's stuck", "why isn't X moving", "/garden-operate", or hands you the loop to run. Covers where the state lives, what each stall looks like, which product action clears it, and what must never be done by hand.
---

# garden-operate

You are the person's agent at the controls of a running garden: `garden serve` ticks every
minute, workers run detached in worktrees, PRs open and merge on GitHub. Your job is to
notice when the loop stops moving, name why, clear it with the loop's own actions, and file
every gap as a task so the loop needs you less next time. Written from the first live run
(2026-09-04/05), when the loop merged 83 PRs in a day and needed a hand about 100 times.

## Where the truth is

- `garden.yaml` (plus `garden.<env>.yaml`, `garden.local.yaml`): read once at start.
  **Any config change needs a restart.**
- `.garden/state.json`: per-task scheduler state (`revisions`, `review_rounds`,
  `pending_feedback`, `needs_human`, `automerge_blocked`, `last_review`), plus `_control`
  (pause) and `_phase:*`. Re-read by every tick; written at the end of every tick, so its
  mtime is the tick clock.
- `.garden/events.jsonl`: every transition, dispatch, review verdict, conflict, merge.
  `garden digest --since 2h` summarises it; the raw file answers "what happened at 01:41".
- `.garden/runs/<task>/<run>/`: `brief.md` (what the worker saw), `stdout.json` (the
  transcript, one JSON event per line), `final.md` (its last message and `GARDEN_RESULT`),
  `run.json` (status, cost, error), `setup.log`, `stderr.log`.
- Task files under `<product>/<phase>/tasks/`: status, log lines, PR link. The scheduler
  owns them; you change them only through commands and web actions.
- Worktrees under `work_dir/worktrees/<task>`; the product clone under `work_dir/repos/`.
- The web UI at `http://127.0.0.1:8765`: Inbox (cards that need a decision), Board,
  Trellis, task pages with the live log, run pages, Config (pause/resume, live overrides).

## First look, every time

```bash
garden status                      # counts, cost, "dispatch paused" if it is
garden inbox                       # decisions vs notices
gh pr list --repo <owner/repo> --state open --json number,title,mergeable,statusCheckRollup
python3 - <<'EOF'                  # active runs and whether they are alive
import json,glob,os,time
for p in glob.glob('.garden/runs/*/*/run.json'):
    r=json.load(open(p))
    if r['status']=='running':
        so=os.path.join(os.path.dirname(p),'stdout.json'); age=int(time.time()-os.path.getmtime(so)) if os.path.exists(so) else -1
        print(r['task_id'], r['mode'], r.get('model'), r['started_at'][11:19], f'last output {age}s ago')
EOF
tail -5 .garden/events.jsonl | cut -c1-200
stat -c %y .garden/state.json      # last tick; if it is minutes old, the server is dead or wedged
```

A worker writing to `stdout.json` within the last minute is working. Silence for ten
minutes with no events and no active runs means the loop is waiting on a person: read
`needs_human` for every non-terminal task before assuming a crash.

## Act through the product, not around it

Web actions are `POST /tasks/<id>/<action>` with an optional `note` field; the CLI has the
same verbs. Use them in this order of preference: web action, CLI command, and only then a
hand edit of `state.json` (never of a task's status field). Actions you will use:

| need | action |
|---|---|
| approve / cancel a discovered draft | `approve`, `cancel` (with a note naming the duplicate or the fix) |
| move a task's rank | `priority` (note = number), `difficulty` |
| one more automated review after the cap | `triage-ready` then `review` |
| clear a revision-cap stop and rebase again | `reset-revisions` then `retry` |
| accept a "nothing to change" / "won't do" card | `accept` / `reject` (note) |
| answer a worker's question | `answer` (note = your answer) |
| send a PR back with a note | `triage-changes` (note) |
| stop / start automatic dispatch | `POST /pause` (field `reason`), `POST /resume` |
| run a task now regardless of slots or pause | `dispatch` |
| commit task-file state to the garden repo | `garden commit`, then `git push` |

Before pressing anything on a task, confirm its PR is still open: an action landing seconds
after automerge moves a `done` task back into the loop (seen once; CG-142).

Before merging a PR by hand (hard tier does not automerge), confirm nothing merged since its
CI last ran: `gh pr view N --json mergeStateStatus` must say `CLEAN`, not `BLOCKED` or
`BEHIND`. If something did, wait for the scheduler's rebase round rather than merging a
green-but-stale branch (2026-09-05: two such merges a minute apart left main red).

## Stall patterns and what they mean

| what you see | what it is | what to do |
|---|---|---|
| `no active run found; back to ready` right after a run finished | the run was swept or its reap was interrupted; the worker's commits are in the worktree | read `final.md`; if the work is done and committed, push the branch, `triage-ready`, then `review`; if not, let it re-run (it reuses the worktree) |
| `2 automated review round(s) used; this PR is yours` | review cap (`review.max_rounds`); happens after rebases too | if the last verdict was approve or the code is fine: `triage-ready` + `review`; a description-only verdict is rewritten by the reviewer without a round |
| `revision cap reached; needs a human` on a conflict | rebase rounds counted against `max_revisions` | `reset-revisions` + `retry` |
| `worker says nothing to change` card | the failure was not the branch's (usually the base) | check main is green on a clean checkout first; if the branch is behind, rebase it, then `accept`; accepting on a stale base fails the checks again |
| pre-PR `test` failing on every branch at once | main is red, or the check environment is wrong | run the suite on a clean checkout of main; if red, `POST /pause`, dispatch the fix with `dispatch`, resume when it merges; if green, read the check command and the worktree's env |
| `CI failure` with 0 review items | a CI job failed | read `gh run view <id> --log-failed`; a known flake belongs in `checks.ci[].flaky_patterns`, a real failure belongs to the branch |
| task `in_review`, `automerge_blocked` says "feedback is pending" | stale `pending_feedback` on a task nothing dispatches from | `retry` (starts the description round) |
| `automerge_blocked` says "GitHub reports the PR unknown" | mergeability being recomputed after a merge | wait one tick |
| a PR shows `CONFLICTING` seconds after another merged | the cascade: PRs sharing a file rebase against each other | let the rebase round run; it is the cost of many PRs in one file |
| a worker asks about files in the garden repo | the task's deliverable is not in the product checkout | park it: `runner: manual` in the frontmatter, `set-status <id> ready --note`, or move it to a `self: true` product; never answer "make the fix yourself" |
| task page returns 500 | a template assumption broke on real data | read the traceback in the serve log; hot-patch the installed template (auto-reloads) and file the fix |
| check recorded as `exit -15` | the check was killed, usually by a restart mid-tick | wait for the next round; restart only right after a tick |
| every worker and reviewer exits within a minute with `Not logged in · Please run /login` | the scrubbed environment hides the harness's credentials (workers have a private HOME since CG-194) | the service's environment must carry `CLAUDE_CONFIG_DIR=<home>/.claude` (and `CODEX_HOME` for codex); check `tr '\\0' '\\n' < /proc/<serve pid>/environ`, fix the unit, restart after a tick, then `retry` the failed tasks and `review` the PRs whose reviews returned no verdict |
| a worker commit appears in the garden repo's history | a worker wrote outside its worktree | revert it, keep the diff as a patch, check the fence config; never push before reading `git log` |
| `PR merged` from `changes_requested` or `failed` | someone merged on GitHub; the poll caught it | nothing; the task is done |
| `base branch main is itself broken ... waiting for the base` on several tasks at once | main is red: two PRs that were each green alone merged within a minute of each other (a branch's CI is against the main of its last push, not the main it lands on) | `POST /pause`; run lint and the suite on a scratch checkout of `origin/main`; fix on a branch, PR, merge on green CI; `POST /resume`. Parked tasks re-probe main on the next tick |

## Restarting the server safely

The server is a systemd user service (`~/.config/systemd/user/garden-serve.service`, lingering
on, `KillMode=process` so detached workers survive). Never stop it with the harness's task-stop
and never start a second `garden serve` by hand: port 8765 is taken and two loops would race.

```bash
# wait for .garden/state.json's mtime to change (the tick just saved), sleep 1.5s, then:
systemctl --user restart garden-serve.service
systemctl --user is-active garden-serve.service
journalctl --user -u garden-serve.service --since "5 min ago"   # tracebacks land here
```

Then confirm `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:8765/` is 200, the
first tick's events look sane, and the worker count did not drop. A restart loses any review
verdict the old process reaped in its last tick (seen twice on 2026-09-05); if a task then says
"the automated review verdict is not in yet" with a green PR, press `review` once.

If the whole WSL instance stopped (`uptime` is younger than the last tick), the service comes
back by itself, but killed workers leave uncommitted edits in their worktrees and the next
dispatch fails with `git merge --ff-only`: `git stash push -u` in that worktree, then `retry`.

## Moving the pin (the garden runs a pinned install of the tool)

```bash
chmod -R u+w .venv/bin .venv/lib      # the lock is recursive
.venv/bin/pip install --force-reinstall --no-deps "context-garden[dev,plates] @ git+https://github.com/<owner>/context-garden@<sha>"
chmod -R a-w .venv/bin .venv/lib
grep -o '"commit_id": "[0-9a-f]\{7\}' .venv/lib/python3*/site-packages/context_garden-*.dist-info/direct_url.json
```

Grep the installed package for a symbol from each merged PR you expect, update the pin
line in the garden's `CLAUDE.md`, then restart the service as above. Do it when merges have landed that
change what the running loop does (sweep, automerge, fence, checks), not for every merge.

## Cost hygiene

- `garden metrics` per tier: revise rounds, first-pass approval, cost per task.
- Description-only review requests should cost nothing (the reviewer rewrites the body). If
  you see revise rounds for descriptions, the rewrite path is broken.
- Rebase rounds: count them (`PR conflicts with main` events per merge). Above about 0.3
  per merge, merges are cascading; hold same-file PRs or serialise merges.
- Bot review comments: a notice ("usage limit", "no issues") must not start a round.
- Watch for the same failure across many tasks in one tick; that is the environment, and
  every round spent on it is waste. Pause first, then find it.

## Filing friction

Every time the loop needed you, file the reason as a task with provenance:

```bash
garden new-task <product>/<phase> "<one-line goal>" --difficulty easy|medium|hard --priority N [--ready]
```

Then replace the template body with Goal / Context (what happened, when, the evidence) /
Acceptance criteria, and `garden commit && git push`. Under a feature freeze, leave feature
ideas as drafts with a log line "deferred by the feature freeze (date)". Judge discovered
drafts the same way: cancel duplicates and already-fixed items with a note naming why.

## Never

- Edit a task's `status:` by hand, or `state.json` while a tick may be writing it.
- Answer a worker with an instruction that sends it outside its worktree.
- Push the garden repo without reading `git log` for commits you did not make.
- Merge or mark PRs ready unless the person delegated it (they can; check).
- Stop the serve task with the harness's task-stop.
- Restart mid-tick, or reinstall the pin without restarting right after.
