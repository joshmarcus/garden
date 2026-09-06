---
id: CG-313
title: parse_result accepts the GARDEN_RESULT marker wrapped in markdown emphasis or code and a JSON payload
  that spans lines
status: ready
product: context-garden
phase: phase-05
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/harness.py
- src/garden/model.py
- tests/test_harness.py
- docs/worker-protocol.md
created: '2026-09-06T02:04:20+00:00'
updated: '2026-09-06T13:14:35+00:00'
---

## Goal

A worker's result is read whenever it is there. `parse_result` (and the persona, review and edit marker parsers) find the marker when a worker writes it as `**GARDEN_RESULT:**`, `` `GARDEN_RESULT:` `` or inside a fenced block, and read a JSON object that spans several lines after the marker. The worker protocol doc still asks for one line; the parser is forgiving and the brief keeps asking.

## Context

2026-09-06 01:57Z: CG-242's revise round (sonnet, $0.83) ended its final message with `**GARDEN_RESULT:** {"status": "done", ...}`; the parser saw no marker, the round was recorded as "revision failed: no GARDEN_RESULT in worker output", the task hit its retry cap and went to the Inbox as a failed worker, and the operator re-queued it by hand. A round's result must not be lost to markdown emphasis.

## Acceptance criteria

- [ ] `parse_result` returns the payload for `GARDEN_RESULT: {...}`, `**GARDEN_RESULT:** {...}`, `` `GARDEN_RESULT:` {...} `` and a marker followed by a JSON object that spans lines (matched by brace balance), and the same tolerance applies to GARDEN_REVIEW, GARDEN_PERSONA and GARDEN_EDIT.
- [ ] A line that merely mentions the marker inside prose (not at line start after stripping emphasis) is still ignored.
- [ ] Tests for each shape in tests/test_harness.py, including CG-242's exact final message.

## Log

- 2026-09-06T02:04:21+00:00 approved (cli)
- 2026-09-06T13:13:19+00:00 dispatch failed: [Errno 17] File exists: '/home/joshua/work/tmp'
- 2026-09-06T13:14:35+00:00 reset to ready by hand
