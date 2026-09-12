# Delegated operator Inbox audit

Owner requested resolution of all actionable cards and logging of misleading human actions.

## Stale holds recovered

CG-253, CG-300, CG-327, CG-328, CG-332, CG-336, CG-356, CG-362, CG-374, CG-375, CG-380, CG-381, CG-382 had normal runners restored at17:01 but stale manual-task human stops remained. Supported Scheduler.retry clears each stop and preserves pending feedback and implementation. These are delegated operator interventions, not owner repairs.

## Other dispositions in progress

Frozen phase06 drafts retain the owner freeze; do not approve or cancel useful future work just to clear a badge. CG381 owns excluding these notices from human counts. CG385/386 repeatedly replay collected failed checks; preserve saved results and recover the check continuation without restarting implementation. CG386 owns idempotent check parking. CG216 needs its substantive automated findings restored instead of overwritten capture-only feedback. CG345 AWS infrastructure and budget already supplied; bootstrap code and tailnet configuration remain operator/worker work.


## Owner-authorized audit and phase07 approvals

Phase07 unfrozen; all22 tasks CG395–416 approved, dependency graph and reading/criteria validation passed. CG391/392 now have concrete criteria and are approved. CG388 environment retry queued. CG385/386 preserved failed check records and continuation with one fresh ordinary-admission retry; no fake pass or implementation restart. CG378 required further automated review queued.

Readback still labels eleven cards as needing the owner: CG378/385 are pending automated review/check recovery, and nine phase06 drafts remain deliberately frozen. No owner decision is required for these. This is additional evidence for existing CG381 ownership/counts correction and CG386/393 check recovery, not grounds to bypass approval or phase holds. Recovery remains queued, not verified complete.


## Retry recurrence, 2026-09-07T20:15Z

The authorized single check retry failed again: CG385 run20260907T201104Z-check reports idle115min, CG386 run20260907T201227Z-check idle118min, although these runs are minutes old. Do not repeat retries without fixing startup/idle accounting (CG393). Web Inbox/Now1 remain200 at1.99/1.94s, controller memory~2.90GiB/noSwap; four actual runtime users account for capacity. Preserve continuations and prioritize the idle-accounting repair through admission.
