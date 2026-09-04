---
id: CG-104
title: 'Live log: a tool result whose content is a string no longer breaks the task page'
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 0
difficulty: easy
reading:
- src/garden/web/templates/_stdout.html
- src/garden/tui.py
- tests/test_web.py
created: '2026-09-04T21:13:24+00:00'
updated: '2026-09-04T21:13:24+00:00'
---

## Goal

The task page's live log renders every tool result from a stream-json run, whether the result's `content` is a string or a list of blocks.

## Context

Found on the first live run. `_stdout.html` reads a `tool_result` block with `c[0].get("text")`, but the Claude stream puts most tool results in `content` as a plain string (git log, diffs, pytest output), so `c[0]` is the first character and the page fails with `'str object' has no attribute 'get'`. Every task page with a running worker returned 500 (CG-091, CG-093) for as long as the worker used tools. The live garden's copy was hand-patched to `{% if c is string %}{{ c[:160] }}{% elif c and c[0] is mapping and c[0].get("text") %}...`; make the same change in the template, check the TUI's event formatter for the same assumption, and make the fake stream fixture emit both shapes so the test suite would have caught it.

## Acceptance criteria

- [ ] a stream with a string `tool_result.content` renders the first line of it; a list of blocks renders the first text block.
- [ ] `tests/fake_claude.py` emits both shapes and a web test loads a task page over that stream.
- [ ] the TUI formatter handles both shapes (or a note that it does not read tool results).
