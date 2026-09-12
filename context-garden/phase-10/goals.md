---
plant: apple
latin: Malus domestica
plate: X
---

# True multiplayer

## Status and intent

Owner released implementation on September12 and requested two remote workers.
The twelve multiplayer tasks now follow ordinary dependency, review and CI gates.
This phase is unfrozen; all unrelated holds and resource constraints remain.
Each person running their UI and scheduler locally remains the product requirement.

Several people share one garden with their own local UI and scheduler. Each issue
has an accountable assignee, and only that person's scheduler may advance it within
their assigned project/phase. Unassigned people can start the application and remain
idle. A project selector focuses all normal views; a viewer-only process serves an
explicitly published read-only projection.

## Specification

[True multiplayer gardens](../specs/multiplayer.md) is the product-level contract.
Reuse completed CG-414's owner metadata; implement identity and execution authority
as explicit extensions. Project means the existing Garden product, not a new layer.

## Delivery sequence

Identity and assignment -> shared coordination -> local clients -> full scheduler
enforcement -> handoff and safe startup. Project views can follow the client boundary;
personal Inbox and public viewing then use the same authorization. Migration and the
integrated two-person acceptance follow those foundations. Dependencies require the
prerequisite to merge; dispatch approved work through the native scheduler.

## Task breakdown

| Task | Outcome | Depends on |
| --- | --- | --- |
| [CG-629](tasks/CG-629-introduce-authenticated-garden-members-and-expli.md) | Introduce authenticated garden members and explicit multiplayer roles | None |
| [CG-630](tasks/CG-630-bind-issue-ownership-and-per-user-project-phase.md) | Bind issue ownership and per-user project phase assignments to membership | CG-629, CG-414 |
| [CG-631](tasks/CG-631-add-shared-transactional-coordination-and-fenced.md) | Add shared transactional coordination and fenced mutation operations | CG-629, CG-630 |
| [CG-632](tasks/CG-632-connect-local-garden-checkouts-to-authoritative.md) | Connect local garden checkouts to authoritative multiplayer state | CG-631 |
| [CG-633](tasks/CG-633-enforce-assignee-authority-throughout-the-schedu.md) | Enforce assignee authority throughout the scheduler lifecycle | CG-632, CG-630 |
| [CG-634](tasks/CG-634-preserve-work-through-reassignment-and-multiplay.md) | Preserve work through reassignment and multiplayer lease recovery | CG-633 |
| [CG-635](tasks/CG-635-make-local-multiplayer-startup-and-unassigned-id.md) | Make local multiplayer startup and unassigned idle state explicit | CG-632, CG-633 |
| [CG-636](tasks/CG-636-focus-all-garden-views-with-a-shared-project-sel.md) | Focus all garden views with a shared project selector | CG-632, CG-630 |
| [CG-637](tasks/CG-637-personalize-inbox-and-authorize-issue-actions-fo.md) | Personalize Inbox and authorize issue actions for the current assignee | CG-633, CG-636 |
| [CG-638](tasks/CG-638-serve-an-isolated-public-read-only-garden-projec.md) | Serve an isolated public read-only garden projection | CG-629, CG-631, CG-636, CG-637 |
| [CG-639](tasks/CG-639-migrate-single-user-gardens-to-multiplayer-with.md) | Migrate single-user gardens to multiplayer with a recoverable cutover | CG-634, CG-635, CG-637, CG-638 |
| [CG-640](tasks/CG-640-verify-the-complete-multiplayer-workflow-across.md) | Verify the complete multiplayer workflow across independent local users | CG-639 |

## Completion boundary

The first complete release supports two independent local users, one shared
coordinator, one active project/phase scope per user, idle unassigned startup and an
isolated viewer projection. It preserves existing dependency, hold, quality and
resource gates. The final integration exercise covers real local concurrency,
reassignment/recovery and direct authorization requests, with proportionate evidence.
Implementation is authorized; source completion
does not itself authorize production rollout, public hosting or infrastructure spend.
