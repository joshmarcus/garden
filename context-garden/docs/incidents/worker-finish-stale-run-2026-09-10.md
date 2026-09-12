# Worker completion metadata lost to a stale standalone scheduler write

Observed September 10, 2026 in the deployed RC16 split controller (serve --no-watch plus standalone watch). This incident is distinct from the earlier physical-disk exhaustion.

CG-516 revision 20260910T131231Z-revise completed its requested credential-redaction change in commit 06bcf53ed5297f16a697a0763fa78c4402c6e3ef, directly above 6949a2208f0c2d94607ecf4d8ffa249bb932146b. The worker published the exact commit to its assigned staging ref. Its final output and exit zero are preserved and match the controller copies; final SHA25635725be1dd082300b5a4f3101d0a32b9d5d68af1009e49f23db3c802fb3a29af. Independent read-only audit checked the actual renewed host identity and source.

The serve journal recorded authenticated finish HTTP200 at13:19:34, and the native event recorded run_finished done at13:19:34. The final, posted result and exit files were written. At13:19:36 the standalone watch reaper saved a previously loaded Run with empty pushed_head/final_received_at and reported that the remote worker finished without pushing commits. The staging ref and lease/claim history remained, but finish-written fields were lost. The remote_result payload intentionally does not duplicate pushed_ref/pushed_head; those belong to Run state.

The worker API uses a process-local threading.Lock for hub.action_lock. That cannot serialize mutations against the separate watch process. Source inspection found the same finish guard in published, undeployed RC17. Atomic file replacement by itself does not preserve concurrent fields from a stale object.

The operator recovered the existing published commit through an exact-parent, old-head-guarded non-force fast-forward of the task branch, then returned the task to native review. The original failed Run, final bytes, source and usage/cost remain unchanged; no new implementation or accepted final result was invented. CI and independent review must assess the recovered head normally.

Existing ownership: CG-497 serializes worker answers, CG-488/535 protect state subtrees, and CG-487 concerns terminal results. None supplies the shared worker claim/heartbeat/finish versus standalone-watch Run mutation contract identified here. Preserve those changes and add the missing cross-process regression. Private operational receipts are cg516-recovery-readonly.json and cg516-publication-recovered.json under the operator receipt directory; they are not required checkout files.
