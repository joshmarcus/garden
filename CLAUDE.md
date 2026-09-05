# garden

The context garden for `joshmarcus/context-garden`: goals, specs and tasks for the tool, kept
apart from the tool's own code so that workers never run inside the garden they are driven by.

- The tool is installed in `.venv` from a pinned commit of https://github.com/joshmarcus/context-garden (currently ba46e30);
  upgrade on purpose with `.venv/bin/pip install --upgrade "context-garden[dev,plates] @ git+https://github.com/joshmarcus/context-garden@<sha>"`.
- `garden.yaml` names the product by URL; the clone lives under `.garden/repos/context-garden` and
  worktrees under `.garden/worktrees/<id>` are cut from it.
- Run: `.venv/bin/garden doctor`, `garden serve`, `garden inbox`.
- Task files under `**/tasks/` are owned by the scheduler; use `garden approve`, `garden set-status` or the UIs.
- `.claude/skills/` has `garden-take`, `garden-plan`, `garden-review` for interactive sessions.
