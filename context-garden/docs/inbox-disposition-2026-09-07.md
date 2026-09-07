# Inbox disposition, 2026-09-07

Owner delegates all routine human-queue handling. Live CLI listed24 items; reviewed each category against persisted state and open PR inventory.

## Automated review, not an owner decision

CG-297, CG-300, CG-323, CG-327, CG-328, CG-332, CG-334, CG-336, CG-339, CG-356, CG-372, CG-376, CG-379 all have pending automated reviews. Preserve verdicts and normal admission; no manual completion or fabricated approval.

## Already decided: deferred

CG-213, CG-230, CG-283, CG-302, CG-319, CG-349, CG-350, CG-351, CG-352, CG-353 remain phase06 drafts by explicit freeze. AWS promotion is limited to CG216/345–348; it does not release these other features.

## Operator-owned deployment prerequisite

CG294/PR275 has an oversized rebase input stop; fixCG373/PR283 merged but is not installed. Cleared the owner stop using supported triage and applied a temporary manual runner hold. Deploy the validated fix at a safe boundary, restore its normal runner, then continue the existing branch. This is pending operator work, not completed implementation.

## Presentation defects

CG-381 logs queued reviews counted as human work, prior verdicts called no review yet, unsafe set-status done advice, and deferred drafts counted as unanswered decisions. Existing active CG374/362 briefs were not altered. Inbox cards may remain visible until that fix lands; a disposition is not a UI implementation.

## Follow-up: CG383 routine preservation question

Worker asked permission to stash unrelated snapshot solely for validation; persisted question was empty despite WAITING_HUMAN. Operator answered in the durable brief and used supported retry to make priority0 continuation eligible without immediate admission bypass. Existing commit4c5a956 and salvage stash preserved. This is another routine technical prompt/empty-question case relevant to CG381 and CG374, not a product decision.
