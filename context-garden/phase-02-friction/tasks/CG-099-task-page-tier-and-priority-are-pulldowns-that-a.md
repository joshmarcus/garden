---
id: CG-099
title: 'Task page: tier and priority are pulldowns that apply on change, with priority in words'
status: ready
product: context-garden
phase: phase-02-friction
depends_on: []
priority: 2
difficulty: easy
reading:
- src/garden/web/templates/task.html
- src/garden/web/app.py
- src/garden/model.py
created: '2026-09-04T21:09:47+00:00'
updated: '2026-09-04T21:09:47+00:00'
---

## Goal

On the task page the tier and priority controls are pulldowns that apply as soon as they change, with no Set button, and priority is chosen by words that make the order plain.

## Context

Asked during the first live run, after CG-071 delivered the two controls. The tier select has a Set button beside it, which is a click nobody wants; priority is a number box, and nobody remembers whether 0 or 4 goes first. Submit each form on change (`onchange="this.form.submit()"` on the select is enough; no script framework) and reload the page showing the new value with a log line. Replace the number box with a select whose options are words in order from first to last, with the number after the word so the CLI and the task files stay as they are: for example "first · 0", "next · 1", "normal · 2", "later · 3", "someday · 4". Pick the words, keep them plain, and put the scale in one place (`model.py`) so `garden priority`, the trellis and the phase tables can show the same words. A priority outside the scale shows as its number and stays selectable. The same on-change rule applies to any other select the task page grows.

## Acceptance criteria

- [ ] neither control has a button; changing either one posts and the page reloads with the new value.
- [ ] priority options are words with the number beside them, ordered first to last.
- [ ] a test that the page renders the priority words and that posting each value stores the number.
