---
id: CG-084
title: The garden upgrades its own pinned install after the tool's PRs merge
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 1
difficulty: medium
reading:
- src/garden/scheduler.py
- src/garden/cli.py
- CLAUDE.md
created: '2026-09-04T19:25:35+00:00'
updated: '2026-09-04T19:25:35+00:00'
---

## Goal

When the garden's tool is installed from a pinned commit of a product this garden manages (as `joshmarcus/garden` installs `context-garden`), a merge into that product can move the pin forward and restart the loop on the new code, on purpose and visibly, so merged fixes reach the running garden without a person running pip and restarting by hand.

## Context

Since the split, the garden runs `garden` from `.venv`, installed with `pip install "context-garden @ git+…@<sha>"`. Every merged fix today (marker-based feedback, lease push, live log, doctor checks) needed a person to fetch, reinstall at a new sha, verify the installed commit, and restart `garden serve`; twice pip silently kept the old build because the version number had not changed. CG-050 handles the `repo: .` layout; this task is the pinned-install layout.

Config under the product: `provides_tool: true`. On a merge into that product's base branch, the tick records `_control.upgrade_available = <sha>` and the Inbox shows "tool update available: <sha>, <n> merged PRs since <current>" with an Upgrade button; `garden upgrade` does the same from the CLI: pip install at the sha with `--force-reinstall --no-deps`, verify `direct_url.json` reports that commit and that `garden doctor` passes, then re-exec `garden serve` when no tick is in progress and no manual finish is running (workers are detached and unaffected; CG-083 makes the reap safe across the restart). With `upgrade: auto` in config it happens without the button. `garden version` prints the installed commit. Keep `site-packages` writable only during the upgrade if the read-only stopgap from the live run is kept.

## Acceptance criteria

- [ ] a merge into the tool's product shows the update on the Inbox and `garden status` with the sha and PR count.
- [ ] `garden upgrade` (and the button) installs the sha, verifies the installed commit, restarts the loop, and logs an event; a failed verify leaves the old install running.
- [ ] `upgrade: auto` does it on the next idle tick.
- [ ] tests with a fake installer.

## Log

- 2026-09-04T19:25:35+00:00 approved
