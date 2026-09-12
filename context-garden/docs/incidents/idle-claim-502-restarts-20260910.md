# Renewed-worker idle claim 502 restarts, 2026-09-10

At 00:54 UTC, a read-only census of all six renewed RC16 workers found each service active and running, but with 38 systemd restarts since readiness: workers 0 through 5 recorded 6, 4, 10, 7, 4, and 7 restarts. Every selected prior exit followed the same idle path: `POST /api/runs/claim` raised `WorkerRequestError` after `HTTP Error 502: Bad Gateway`; systemd restarted the daemon five seconds later. No 401, 403, connection-refused, `TimeoutError`, or explicit timed-out message appeared. No execution claim was active in this sample, so these restarts did not interrupt child work.

The source receipt's `http_5xx` count matched two traceback lines per incident. Its `timeout` count matched `urlopen(... timeout=60)` source text and does not show a network timeout. Systemd `NRestarts` is the authoritative count.

The correlated blank-body gateway response across six hosts strongly indicates failure before the FastAPI claim handler, consistent with the Tailscale/WSL relay path. This is an inference; no direct relay telemetry was collected.

CG-491 and PR394 own this exact failure. They cover bounded transient idle-claim retry, stable request identity for lost successful responses, generation fencing, and permanent-error visibility. PR394 was open at `894a2d027fc2c5792b7724b9c7e6c8d9e51eacd4`, mergeable but unstable, with two failed reported CI runs. The task log identifies dependency-install infrastructure failures and records focused validation plus approving Garden reviews. The fix is absent from RC16.

The exact Actions logs confirm both failures occurred before lint or pytest. Run `34383729833` and run `34383509510` each completed checkout, Python setup, and editable dependency installation, then failed `python -m playwright install --with-deps chromium` because the Google Chrome apt repository returned a `Packages.gz` hash-sum mismatch. Ruff and pytest were skipped. This is external package-index inconsistency rather than a branch test failure. Both failed jobs were re-run at 01:00 UTC under the standing current-head recovery authority; no source or PR head changed.

Continue CG-491 at its current head through normal exact-head CI, review, merge, and versioned release. Preserve coverage for repeated pre-allocation 502 and lost-postcommit replay. CG-428 retains active-heartbeat scope. This evidence does not justify a worker restart, hotpatch, CG-423 expansion, or duplicate task.

Machine-readable evidence is `/home/joshua/work/operator-test-tmp/aws-renew-20260909/cg491-idle-claim-restart-addendum.json`.
