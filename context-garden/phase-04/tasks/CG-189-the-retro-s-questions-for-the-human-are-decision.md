---
id: CG-189
title: 'The retro''s questions for the human are decision cards: answer each in the UI, the answers land
  in the retro document and the next phase''s goals, and the planner reads them'
status: draft
product: context-garden
phase: phase-04
depends_on:
- CG-178
priority: 1
difficulty: medium
reading:
- src/garden/retro.py
- src/garden/scheduler/retro.py
- src/garden/scheduler/discovered.py
- src/garden/inbox.py
- src/garden/web/actions/decisions.py
- context-garden/phase-03/docs/reviews/product-manager-vision-2026-09-05.md
created: '2026-09-05T10:23:11+00:00'
updated: '2026-09-05T10:23:11+00:00'
---

## Goal

When a retro (or a persona with a `questions` section, CG-188) puts a question to the owner, the owner answers it in the web UI. Each question is a decision card on the Inbox: the question, the context the retro gave, the options when it named some, and a free-text answer. An answer is recorded with who and when in the retro document under `## Answers`, and in the next phase's goals under `## Decisions`, so the planner and every later worker read it as settled. Unanswered questions stay on the Inbox as decisions and count in the badge.

## Context

Asked by the user on 2026-09-05 after reading the product manager's phase-03 report, which ended with five questions (whether the queue may merge hard-tier PRs, a structure gate at the start of phase 04, the phase budget and its definition of done, whether the retro may close a phase without approval, and which operator decisions to ratify). Today those questions live in a markdown file under `docs/reviews/`, the operator relays them in chat, and the answers are not written anywhere the loop reads. The decision-card machinery exists (CG-100, CG-112, `web/actions/decisions.py`); CG-178 adds the retro verdict card; this task adds the question cards beside it.

## Design

- The reconciliation result (and a persona's `questions` section) carries `questions: [{key, question, context, options: [..] or [], default}]`. On reap the garden files each as a decision of kind `retro_question` in state under the phase, and the Inbox shows one card per question with an answer form (radio options when given, plus a text field; "later" leaves it open).
- Answering posts `POST /phases/<product>/<phase>/retro-answer` with the key and the answer; the garden appends `- **<question>** — <answer> (<who>, <date>)` under `## Answers` in `docs/retro.md` and under `## Decisions` in the next phase's `goals.md`, commits nothing by itself (the owner runs `garden commit`), and emits a `retro_answered` event.
- The retro page (CG-146) lists the questions with their answers; `garden retro-answer <phase> <key> "<answer>"` is the CLI form; `garden plan` for the next phase includes the answered decisions in the planner brief.
- A question the retro marks as blocking the close (CG-178's `reopen` verdict) is answered before the verdict card can be accepted.

## Acceptance criteria

- [ ] Each retro question is a decision card on the Inbox with the question, its context, options when given and a free-text answer; unanswered ones count as decisions.
- [ ] Answering records the answer in `docs/retro.md` and the next phase's `goals.md` with who and when, and emits an event; the CLI form does the same.
- [ ] The planner brief for the next phase includes the answered decisions.
- [ ] Tests with the fake harness: a retro with two questions, one answered on the web and one on the CLI, both visible on the retro page and in the goals.

