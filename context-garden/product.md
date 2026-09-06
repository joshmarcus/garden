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

- Tests: `.venv/bin/pytest -q`
- Lint: `.venv/bin/ruff check src tests`
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

## Looking at pages: screenshots from a WSL worker

Workers on this machine have no browser inside WSL, but Windows Edge is reachable and renders both files and the running app. Use it to see what a person would see before you call a UI change done, and read the PNGs back with the Read tool.

```bash
EDGE="/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
OUT=/mnt/c/Users/joshm/AppData/Local/Temp/captures          # Edge reads Windows paths only
mkdir -p "$OUT" && cp -r docs/design "$OUT/"                  # for a static mock; skip for a live page
"$EDGE" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,2400 \
  --screenshot="C:\\Users\\joshm\\AppData\\Local\\Temp\\captures\\inbox-1280.png" "http://localhost:8765/inbox"
"$EDGE" --headless=new --disable-gpu --hide-scrollbars --window-size=390,2400 --force-dark-mode \
  --screenshot="C:\\Users\\joshm\\AppData\\Local\\Temp\\captures\\mock-390-dark.png" \
  "file:///C:/Users/joshm/AppData/Local/Temp/captures/design/now-1.html"
```

Windows sees WSL's localhost, so a page served by `garden serve` (or a test server you start on another port against a fake garden) captures directly. Edge writes only to Windows paths, so capture into the Windows temp folder and then copy the PNGs into your worktree (`cp /mnt/c/Users/joshm/AppData/Local/Temp/captures/*.png docs/design/captures/` or under the run's captures directory) so they travel with the PR and stay inside the fence. Take 1280 and 390 wide, light and dark, for every page a change touches, and say in the PR which captures you looked at. Fable's Now 1 design run found this route on 2026-09-06; CG-315 turns it into a check the garden runs itself.
