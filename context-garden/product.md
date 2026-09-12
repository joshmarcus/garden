## Current owner policy: agent judgment and proportionate PR verification, 2026-09-09

Owner merge policy, September 9: merge an approved pull request when its current reviewed commit has passing applicable CI and GitHub reports it mergeable without conflicts. Do not force a rebase or another build solely because main advanced. Preserve current-head identity checks, substantive review rejection, actual failed checks, dependency constraints and atomic merge head guards. Latest-main validation may be an explicit opt-in policy; it is not the owner's default requirement. This is a requested scheduler implementation change; do not claim it is active in an installed immutable release until the new version is deployed.

The owner explicitly requests thoroughly relaxing PR requirements and letting workers and reviewers judge for themselves. Agents choose verification appropriate to the actual change and may supply relevant evidence or a clear, honest attestation of what they tested or inspected and the result. Reuse trustworthy existing checks. Focused tests, CLI checks, code inspection, CI, browser interaction, or a small integration exercise may each be sufficient according to the agent's judgment. Explain material uncertainty briefly; do not invent tests, observations, or success.

When a worker has not attached an artifact, assume the artifact is not included. Do not mention its absence in the review, summary, findings, nits, caveats, or revision feedback. Review the code and checks actually performed. Artifact absence alone is not material uncertainty and does not require an apology, limitation, or follow-up. Discuss a specific observed defect, failed applicable check, contradictory claim, or unmet explicit functional requirement when one exists; do not turn an unavailable optional attachment into such a finding.

Running-app journeys, generic HTTP replays, screenshots at prescribed widths/themes, empty and failure/recovery scenarios, scalability/load measurements, artifact manifests, exact evidence schemas, preflight checklists, and PR-description style are not blanket PR prerequisites. Missing such items alone must not block review or merge or trigger an unchanged implementation revision. File paths and keyword matches do not establish that these forms of evidence are required. A reviewer who needs more verification should identify the concrete changed behavior or unresolved correctness concern and choose a proportionate way to check it; a clear attestation is acceptable without prescribed artifact fields. Historical evidence may remain archived without creating new work.

Actual defects, actual failed applicable checks, contradictory claimed results/source identity, and genuinely unmet functional outcomes remain actionable. Distinguish them from optional presentation or evidence-form suggestions. Preserve full original findings and results, document current judgments separately, and respect current-head CI, versioned release/deployment rules, resource limits, AWS budget/deadlines, and explicit phase holds CG402/403/407/408. No production fault injection is implied. This policy supersedes earlier blanket verification, screenshot, running-app, lifecycle-state, or reporting-checklist language below. Reviewers need no further owner approval to exercise this judgment.

## Current owner policy: bounded validation and capture infrastructure, September8

Owner requests 120 seconds per ordinary test and 900 seconds per validation command. Keep stress/load tests opt-in. Use focused tests first. An AWS full ordinary suite is at most one attempt per unchanged source/environment; if it reveals a shared failure, preserve the exact failing node/log and compare the focused failing test with base in the same environment. Do not repeatedly run the same full suite or repair unrelated implementation inside this PR. Confirmed shared/environment failures go to the matching recovery task; genuine PR regressions still block. Local WSL workers use focused tests only.

Until native supervisor deadline enforcement is deployed, use `timeout --signal=TERM --kill-after=10s 900 "$GARDEN_VALIDATION_RUNNER" -m garden.validation -- .venv/bin/python -m pytest --timeout=120 --timeout-method=thread <affected test files> -q`. The setup installs pinned pytest-timeout. Keep execution in the foreground and report timeout/interruption honestly; never substitute pass or silently deselect a failing test. Queue-wait/environment interruption is not automatically an implementation failure.

Screenshot capture/return infrastructure failures are temporarily advisory. Try scoped captures for material visual changes when the browser/artifact path works; preserve available PNG/HTML/text evidence. Do not add review commentary about artifacts that were not attached. A missing browser, controller-only path or artifact-return failure alone must not force request_changes or another unchanged author revision. Focused behavior tests and actual affected UI/HTTP behavior remain required as appropriate. Observed UI defects, application/render failures, functional test regressions, mismatched source claims and genuinely unverified requested outcomes still block. This supersedes earlier absolute screenshot language; the explicit mechanical advisory switch is being implemented separately and is not yet claimed deployed.

Review feedback must keep the full substantive findings/fixes and criterion-specific reasons alongside any operator recovery summary. A short triage note supplements those findings, rather than silently replacing them. Historical/negated mentions of scalability, stress or performance do not add load criteria to a task that makes no such acceptance claim. Keep the actual frozen functional criteria; reuse equivalent evidence and do not demand diagnosis of an unrelated whole-system incident.

# context-garden

A tool for driving agent development from a repository of context files. Humans write
principles, product overviews, phase goals and specs. A planner turns a phase into task
files. A token-free scheduler dispatches headless agent workers per task, pushes their
branches, opens PRs, and re-dispatches when reviewers leave feedback. A local web UI and
a TUI show the board and the dependency graph.

Users: a single developer (or small team) who wants to specify work and review PRs, and
have the rest of the loop automated without an LLM sitting in the scheduler seat.

## Cost of the operator thread

The loop is driven by a token-free scheduler, but in practice a person or an operator agent
watches it, clears cards and moves pins. That operator thread is the most expensive seat in
the system when it is an agent: every observation is a turn that re-reads its whole context.
Keeping that thread cheap is a product goal, on a par with keeping worker runs cheap:

- the loop should need the operator rarely (every card is a defect to file), and when it
  does, one press should be enough;
- what the operator has to read should be small and configurable (`garden observe`, the
  observation profiles, the efficient-to-fast slider), so a quiet garden costs a few turns an
  hour and a watched one costs more only by choice;
- the operator should compact or restart its context at convenient boundaries: a phase
  closing, a retro merging, a pin moving, the start of a long wait;
- the operator's spend is recorded beside the workers' (`docs/operator-spend.jsonl`, the
  `operator` activity on the costs page) so the two are compared, not guessed.

## Repo

This repository is both the tool and its own first product. Python 3.11+, packaged with
`pyproject.toml` (hatchling), managed with `uv`.

- Focused tests: `.venv/bin/python -m pytest <affected test files> -q` (serial).
- Full ordinary tests on AWS: commit the final source, then run `"$GARDEN_VALIDATION_RUNNER" -m garden.validation -- .venv/bin/python -m pytest -q` in the foreground. Stress/load tests require separate explicit authorization and remain excluded by default. Local WSL workers use focused tests.
- Lint: `.venv/bin/ruff check src tests scripts`
- CLI: `.venv/bin/garden --help`

Layout:

- `src/garden/model.py` task frontmatter model and statuses
- `src/garden/store.py` discovery of products/phases/tasks on disk
- `src/garden/graph.py` dependency graph, ready set, mermaid export
- `src/garden/brief.py` builds the worker brief; `GARDEN_RESULT` parsing
- `src/garden/scheduler/` the tick state machine as a package: `__init__.py` assembles `Scheduler`
  from one mixin per tick phase (`reap`, `fence`, `discovered`, `review`, `edits`, `poll`,
  `dispatch`, `human`, `budget`, `upgrades`, `aux`, `trials`, `persona`, `retro`) plus
  `state.py` (the `state.json` side-store) and `report.py`; see the module map in
  `docs/architecture.md` of the product repo
- `src/garden/harness.py` harness definitions (claude, codex, custom) and output parsing
- `src/garden/runner/` runner backends (`local`, `ssh`, `manual`)
- `src/garden/review.py` automated review brief and verdict parsing
- `src/garden/events.py` append-only event log, digest and metrics
- `src/garden/trials.py` model trials: comparison brief, leaderboard
- `src/garden/personas.py` persona reviews of PRs and phases
- `src/garden/checks.py` token-free pre-PR and CI checks (plugin runner + helpers for writing CI analysers)
- `src/garden/plants.py` the botanical drawings (plants per phase, growth-stage glyphs) as SVG symbols
- `src/garden/gitops.py`, `src/garden/github.py` git worktrees and PRs
- `src/garden/planner.py` planning prompt and JSON import
- `src/garden/web/` FastAPI + HTMX web UI: `app.py` (`create_app`, templates), `common.py`
  (`Hub`, `Site`, shared helpers), `pages/` (one module per page family, GET routes) and
  `actions/` (the task-action registry in `tasks.py`, one function per action, plus
  `control`, `phases`, `decisions`, `friction`); `src/garden/tui/` Textual TUI
- `tests/` pytest; `tests/scheduler/` splits the scheduler tests by area with shared helpers
  in `conftest.py`; `tests/fake_claude.py` (modes as two tables: `SPECIAL` and `WORKERS`),
  `fake_codex.py`, `fake_ssh.py` stand in for the real binaries

## Conventions

- Type hints everywhere; `from __future__ import annotations`.
- No network calls in `model`, `store`, `graph`, `brief`; those must stay testable offline.
- Task files are the source of truth; `.garden/` holds only run records and PR bookkeeping.
- Keep the CLI, web and TUI thin: all logic lives in `scheduler`, `graph`, `brief`, `store`.

## The run ends when you stop

A worker runs headless: when you finish your turn, the process exits and nothing wakes it again. Never background the test suite, a build or a capture and wait for a notification; run long commands in the foreground and read their output before you write your result. Respect the owner test deadlines above; a timeout is a recorded failed/interrupted validation, not permission to wait indefinitely. A run that ends without its `GARDEN_RESULT` line is a failed run, however much it committed; five Fable runs were lost this way on 2026-09-06 while "waiting for the monitor to report".

## Looking at pages: screenshots from a WSL worker

Local WSL and AWS workers have configured Playwright Chromium. Use the supervised wrapper for browser work and inspect the resulting images. The following Windows Edge route is a historical fallback for local WSL only; it is unavailable on AWS.

```bash
EDGE="/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
OUT=/mnt/c/Users/joshm/AppData/Local/Temp/captures          # Edge reads Windows paths only
mkdir -p "$OUT" && cp -r docs/design "$OUT/"                  # for a static mock; skip for a live page
"$EDGE" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,2400 \
  --screenshot="C:\\Users\\joshm\\AppData\\Local\\Temp\\captures\\inbox-1280.png" "http://localhost:8765/inbox"
"$EDGE" --headless=new --disable-gpu --hide-scrollbars --window-size=600,2400 --force-dark-mode \
  --screenshot="C:\\Users\\joshm\\AppData\\Local\\Temp\\captures\\mock-390-dark.png" \
  "file:///C:/Users/joshm/AppData/Local/Temp/captures/narrow.html"
```

Windows sees WSL's localhost, so a page served by `garden serve` (or a test server you start on another port against a fake garden) captures directly. Edge writes only to Windows paths, so capture into the Windows temp folder and then copy the PNGs into your worktree (`cp /mnt/c/Users/joshm/AppData/Local/Temp/captures/*.png docs/design/captures/` or under the run's captures directory) so they travel with the PR and stay inside the fence. Take 1280 and 390 wide, light and dark, for every page a change touches, and say in the PR which captures you looked at. Fable's Now 1 design run found this route on 2026-09-06; CG-315 turns it into a check the garden runs itself.

### Verified narrow viewport

Edge on this host has an outer-window minimum around 496px, so `--window-size=390` does not establish a 390px page viewport. Before the narrow command above, create `narrow.html` in the Windows captures directory containing `<html><body style="margin:0"><iframe src="http://localhost:8765/now1" style="width:390px;height:2400px;border:0"></iframe></body></html>` (substitute the page being checked). Capture the wrapper at an outer width of 600. Inspect the embedded page at 390 CSS pixels and check its clientWidth and scrollWidth; the extra outer margin is not part of the page. The finding and measured clientWidth 390 / scrollWidth 390 were recorded by CG-308 in CG-326. A browser API that sets the actual page viewport to 390 is also suitable.

## AWS full-suite validation (owner instruction, 2026-09-08)

External AWS workers run the full ordinary suite on their host after focused iteration,
lint and self-review. Commit the final source, use the supervised validation wrapper and
wait for its result in the foreground. Report the exact tested commit, command, selection,
result and a durable log or equivalent receipt. Failed tests, contradictory provenance or
an unverified result still block; formatting or missing artifact metadata alone do not.

`setup.worker_push` is disabled. Do not run `scripts/check_ci.py` or push solely to trigger
or poll a full GitHub suite. The remote protocol returns committed work through its
assigned transport ref; the controller publishes the branch and owns remaining authenticated
GitHub status reads. CG-396 is implementing the authoritative AWS receipt provider. Until
that integration is deployed, the controller's existing checks remain in force; workers
should report an environment blocker rather than repeatedly polling public GitHub APIs.
This instruction supersedes the older full-suite-offload instructions in existing branches.

AWS hosts have gh, make, Chromium and its Linux dependencies, with task Python 3.12.14 and
pip25. Their shared browser cache is `/var/lib/garden-worker/browsers`; if a tool needs an
explicit setting, use `PLAYWRIGHT_BROWSERS_PATH` with that host-local path. Do not copy
controller credentials or paths. Use actual Playwright viewport dimensions for responsive
checks; the Windows Edge examples above are legacy local-machine alternatives only.

## Product architecture

See the [product specifications](specs/README.md) for the [overall system design](specs/system-architecture.md), enterprise integration and persona review contracts.
