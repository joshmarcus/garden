# Inbox and repeat-loop investigation

Recorded: 2026-09-08T16:20:46.704878+00:00

The Inbox audit found scheduler and verification failures being presented alongside genuine owner decisions. Every card in the16:08 snapshot was assessed. Existing explicit holds remain acknowledged holds. No failed or unreviewed task was marked complete to clear the Inbox.

| Task | Evidence | Delegated disposition |
|---|---|---|
| CG332 | Six revisions, four reviews; functional criteria and current GitHub checks pass. Scheduler replay covers generic approval/revision flows instead of harness pause/probe/redispatch. Author evidence exists but its provenance and complete outcome coverage still need reconciliation. | Preserve implementation and the protective stop; operator investigates through CG436 before another revision. CG431 backend routing alone cannot fix semantic coverage. |
| CG328 | Six revisions and six reviews after latest review; functional criteria and current GitHub checks pass. Required replay omits no-change acceptance, and review also requests scalability evidence not present in the manifest. | Preserve branch/artifacts; investigate affected evidence and whether the broader validation demand is justified. Do not launch default stress work or repeat implementation merely for metadata. |
| CG397 | Two reviews, one revision; code/focused tests/current checks pass. Replay neither enables external stack ownership nor supplies readable affected-flow evidence. | Operator-owned verification investigation under CG436; keep outcome gate. |
| CG395/398/430 | Last remote review has no host, claim, PID or output; timeout inherited old worktree age. Both active review pointer and pending request were then empty. | Restored one replacement review each, locally under existing one-slot admission; original round count retained. CG430 replacement actually started. CG438 owns durable recovery; CG393 owns age classification. |
| CG405/411 | Automatic check/review and/or restack still owns the next action. | Preserve active/queued automation. Added fixtures to CG381 for false owner counts and misleading Mark done actions. |
| CG402/407 | Previously explicit owner holds. CG403/408 holds also remain. | Preserve; these are not newly requested approvals. |
| CG230 | Auto-retrying notice. | No owner action required. |

CG427 progressed after temporary local check routing: its renderer/captures reached actual review, which found duplicate command rows from item.started/item.completed. That is a concrete implementation issue and retains normal revision feedback. CG439 supplies the missing permanent pre-PR UI ownership declaration; CG431 added a resolver but no UI producer at8703380 actually sets execution_owner.

Revision count currently does not increase author difficulty. CG332 stayed easy/Luna through six revisions; CG375 stayed medium/Terra through eight reviews. Reviewers use hard/Sol independently. CG437 is approved for configurable N thresholds (proposed default2), durable escalation, a distinct troubled-task card and Pause for investigation. An operator or bounded investigation agent will return a report with evidence, confidence, options and a recommendation; completion will not silently resume/cancel. The unstarted CG388 cap-recovery scope was consolidated there so its original one-click recovery requirements are retained without duplicate implementation.

Additional repair tickets: CG436 affected replay selection/evidence handoff; CG438 lost review intent and bounded recovery; CG439 pre-PR controller-owned UI payloads. Existing CG381 and CG393 received the concrete cases. Duplicate CG435 supervisor discovery was consolidated into CG433 with both reporters' observations retained.

The three investigation stops still render as ordinary attention cards in installed rc5; they have recorded operator ownership and a decision, but the new investigation UI is not implemented. No release was deployed. Normal scheduling, six AWS hosts,7global/1local/reviewer3,90-minute timeout,20:00UTC host deadlines and the aggregate$80 AWS limit remain. Latest Windows Now request returned200 in0.98seconds. A WSL launch timed out once; its read-only retry succeeded while the web stayed healthy.

Evidence is retained beside this report in before.json, recovery-actions.json, after.json and ticket receipts. Current PR facts were read through the configured controller GitHub environment. CG395 current Actions runs34244003870/34243997845 were cancelled; no passing replacement was invented and no new GitHub suite was triggered. AWS authoritative validation/status integration remains CG396.
