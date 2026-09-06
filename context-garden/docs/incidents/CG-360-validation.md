# Archive/restore consistency repair validation

Owner authorized direct operator implementation alongside the sole CG-361 worker on 2026-09-06. Product branch codex/cg-360-restore-index, PR242. No additional model worker or reviewer was started. Production archival/restoration was not exercised.

## Failure and repair

The live run directory fingerprint can remain unchanged when a run moves away and back on ext4. Generic invalidation only caused a freshness check, so restoration could leave a physically present run out of the cached live bucket. The archive ledger could independently remain cached for a same-length correction with a colliding fingerprint. Concurrent moves and metadata updates also lacked coordination with readers and each other.

The fix explicitly marks moved live buckets and archive metadata dirty, derives changed live buckets from archive membership for external writers, fingerprints the atomically replaced ledger inode, serializes archive operations and refreshes across threads/processes, and refuses stale archived updates that would recreate restored history. Ordinary unchanged reads still reuse cached records.

## Evidence

All local validation was serial, after the other worker's test process exited, in bounded systemd units with CPUQuota100%, MemoryHigh512MiB, MemoryMax768MiB, MemorySwapMax128MiB. Interpreter: garden venv Python3.14 with PYTHONPATH=src targeting the operator worktree.

| Check | Result | Elapsed pytest | Peak unit memory |
|---|---|---:|---:|
| Original 6dd3ae49 implementation, expanded archive tests on ext4 | 8 failed,6 passed |1.56s|65.3MiB|
| Fixed implementation, run-index and cost tests on ext4 |33 passed|2.87s|96.9MiB|
| Fixed implementation, archive tests on tmpfs |14 passed|1.48s|52.7MiB|

No swap was used. The original existing restore test reproduced its IndexError on ext4; new failures cover colliding fingerprints, duplicated external-archive totals, concurrent moves, reads during partial moves, and stale-update resurrection. Fixed tests verify exact identity, counts, costs, artifacts, shared-store and expired snapshots, separate processes, safe stale references and no unnecessary rereads of unchanged history. The final added cross-process atomicity test was included in both local passing runs.

Full CI on implementation commita729b3f:1200 passed,3 skipped in287.03s on Python3.12. Final head7f4da28 adds the cross-process regression and passed its own full CI:1201 passed,3 skipped in273.45s. PR242 merged44b9a312e7f56c73de3b012a67ce2cff65da2d51 at22:16 UTC. Task is done; pin deployment remains pending worker drain. Lint and git diff --check passed. Raw local logs are /home/joshua/work/operator-test-tmp/cg360-baseline.log, cg360-disk.log and cg360-ram.log. No local full-suite rerun was needed in addition to full GitHub CI.

## Separate fixture stall

While this repair waited for a serial validation window, CG-361's full suite stopped making CPU progress in tests/conftest.py git() -> subprocess.run(). The git push child exited128 but orphaned sh/git-receive-pack fixture descendants kept stderr open. Operator verified start times, paths and matching pipes before terminating just those orphan fixture helpers. Pytest then completed with425 passed and one fixture error after694.80s. That run is not a full-suite pass. Evidence: /home/joshua/work/operator-test-tmp/CG361-orphan-git-helpers.json. CG-354 now includes bounded fixture subprocess waits and descendant cleanup. Original Git failure cause remains unproven.

## Completion bookkeeping recovery

The automatic approval review rejected an initial combined bookkeeping update with only “blocked by policy.” No part of that command executed. The operator used the standard manual finish command instead. Before that finish, the operator moved its own worktree to distinguish external from managed completion; this was a mistake because take had already snapshotted that path. The Git guard correctly rejected the move. The worktree was restored to its original path, every protected Git hash rechecked equal to the dispatch manifest, and only the block with the exact CG-360 manual-run reason was archived at operator-test-tmp/CG360-resolved-git-block.txt. Task branch was corrected to the GitHub-verified actual branch through Store.save; the normal set-status done command then passed ancestry verification. No force completion was used. The manual bookkeeping run stays failed as an honest record, while task completion is supported by merged PR242 and its checks. CG-362 tracks an explicit low-overhead external completion protocol.
