# context-garden

A tool for driving agent development from a repository of context files. Humans write
principles, product overviews, phase goals and specs. A planner turns a phase into task
files. A token-free scheduler dispatches headless agent workers per task, pushes their
branches, opens PRs, and re-dispatches when reviewers leave feedback. A local web UI and
a TUI show the board and the dependency graph.

Users: a single developer (or small team) who wants to specify work and review PRs, and
have the rest of the loop automated without an LLM sitting in the scheduler seat.

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
