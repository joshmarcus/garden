# project-manager review of context-garden/phase-02-friction

**Persona:** project-manager · **Score:** 7/10 · 2026-09-05T02:47:50+00:00

The phase delivered its structural goals and the tool is green with nothing open, but it is not closed: the friction document has no harvested section, the notification hook was built and never switched on, the brief-cost goal has no evidence, and the close-out task CG-029 is about to run a harvester that drops the first-run notes and a retro that cannot see the post-CG-136 friction record. The automerge non-goal was reversed in config without the goals or a closing document recording the decision.

## High

- **friction doc** — write_friction_doc regenerates friction.md keeping only the Reported section, so CG-029's first step (garden friction) deletes the hand-written First live run record that the retro README and CG-029 both assume survives.
  - suggestion: Preserve every non-harvested ## section (or write harvested entries under their own heading) before running the harvest; at minimum verify friction.md is committed first.
- **retro inputs** — The retro reconciliation only harvests PR-body Friction sections, so the 16 Reported entries and marked-comment friction routed there by CG-136 are invisible to the reconciliation agent.
  - suggestion: Have _retro_materials include collect_comment_friction and the Reported section of friction.md so the reconciliation sees the whole record.

## Medium

- **goal 2** — The notification hook (CG-010) shipped but notify.command is unset in the live garden; 24 needs-human stops and about 105 hand interventions happened without one notification.
  - suggestion: Configure notify.command before phase 03 and have the retro record that the hook was never exercised live.
- **goal 4** — Nothing measured the brief's fixed cost over the phase; the per-dispatch brief estimate in task logs rose from a median of about 5.6k to 7.7k tokens across the day.
  - suggestion: Add the fixed brief cost to garden metrics per phase and make phase 03's done criterion a number.
- **non-goals** — Automatic merging is listed as a non-goal but automerge is on and merged 25 PRs.
  - suggestion: Record the reversal and the CG-129 evidence in the closing document, or turn automerge off until CG-139/CG-141 land.
- **definition of done** — Five tasks landed by hand or without a PR (CG-027, CG-092, CG-113, CG-011, CG-039) and CG-029 is set to run manually although CG-123 now lets a worker edit the garden repo.
  - suggestion: Run CG-029 through the self product as CG-123's first real test and list the manual exceptions in the closing document.
- **review pass** — The review-pass spec's open follow-ups (line-anchored comments, a digest of what reviews keep flagging) have no task in phase 02 or draft for phase 03.
  - suggestion: File both as phase-03 drafts or strike them from the spec.

## Low

- **unowned follow-ups** — Worker suggestions with no task: CG-065's audit of old PRs for ignored bot feedback, CG-064's refresh of local main before revise checks, CG-131's conflict-plus-red-base corner.
  - suggestion: Triage each into a draft or an explicit won't-do note.
- **close-out loose ends** — Phase-01 is still not closed, the roadmap Next still names phase 02, no phase-03 directory exists, principles/00-index.md still says to put friction in the PR body, and review.difficulty is hard with a note to revert.
  - suggestion: Fold these into CG-029's checklist so the phase closes clean.

_garden persona run 20260905T024121Z-persona_
