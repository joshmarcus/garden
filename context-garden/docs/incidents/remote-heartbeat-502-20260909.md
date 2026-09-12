# Remote heartbeat 502 incident — 2026-09-09

The existing CG428 transport-recovery work is the implementation owner. The deployed RC9 worker permanently records its first heartbeat request failure; a later publication fence raises that stored failure and the managed service exits. A replacement claim can reset the same task checkout and repeat completed work. This behavior is distinct from the execution-age accounting already deployed through CG457.

## Observed failure and preserved work

Worker journals correlate CG463 heartbeat HTTP 502 responses with empty bodies at 02:36:13 and 02:39:01 UTC on host0, 02:43:38 on host3, and 02:49:27 on host2. These were gateway errors, not explicit lease revocation responses. Other workers also received 502 responses while claiming work. CG463 reached five claim generations. Earlier model transcripts show real implementation and validation; current controller output alone did not represent all prior execution. Host0's five-file patch and the remote transcripts were retained. Host3/host2 checkout edits had already been reset by later claims before capture.

The fifth CG463 generation ultimately returned durable source `5c82faf1e90940ce4264093923e0aa188b01e573` and a final result at 02:55:21 UTC. Its result reports 24 focused web/upgrade checks and lint; the normal pre-PR continuation is preserved. Do not dispatch a duplicate author to reconstruct this completed source.

The upstream route is Windows Tailscale Serve (`https://babel.taild4d2ae.ts.net:443`) to `http://localhost:8765`, whose current Windows listener is the WSL relay at `127.0.0.1:8765`. WSL does not run this Tailscale service. The controller journal retains the same serving PID with no restart and no matching Uvicorn request for the worker-side 502 timestamps, while neighboring requests succeeded. This localizes the isolated failures to the Windows Serve/localhost relay path before the application. The exact proxy or relay cause remains under investigation; the IPv4-only listener alone does not establish a DNS or IPv6 defect. No blind controller or Tailscale restart was used for this investigation.

## Temporary lease mitigation

At 02:56:40 UTC the operator changed only `workers.lease_seconds` from 120 to 600 in `garden.local.yaml`, through the supported local configuration layer. The normal controller reload accepted that non-executable configuration change at 02:57:40. Actual later authenticated claim renewals for CG411, CG437, CG438 and CG412 received 600-second leases; CG230 completed after a valid 600-second renewal. Proof distinguishes a new claim from a later renewal of that same generation.

No run record or expired generation was rewritten. The fixed 90-minute execution limit plus the existing five-minute controller grace, six-host allocation, global/local/reviewer limits of 7/1/3, host termination deadlines and budget remain unchanged. The mitigation increases the time available to recover from a transient upstream failure; it does not repair the first-error worker behavior.

After the versioned CG428 transport fix is deployed and actual heartbeat/stream/finish recovery is verified, restore only `workers.lease_seconds` to its prior value of 120. Preserve any newer owner configuration changes; do not restore the whole backup file. Verify native config reload and subsequent valid 120-second renewals. Do not shorten or manually reassign existing accepted generations merely to make their historical lease fields match the restored default.

## WSL orphan-Relay mitigation

At03:33UTC, the kernel capture contained1,102 long-accept warnings from70 distinct Linux `Relay` processes. The captured ring covered03:17:22–03:33:05UTC, so those entries cannot establish timestamp correlation with the earlier02:36–02:49 worker502s. A root-readable census at03:38:03 found all70 still had exact orphan signatures. The serving controller had10 open file descriptors against its1024 soft limit; controller descriptor exhaustion was not observed.

The observed signature matches Microsoft's documented [create-process relay accept leak](https://github.com/microsoft/WSL/issues/41242). Its [merged fix](https://github.com/microsoft/WSL/pull/41252) adds a30-second accept timeout. Direct tagged-source comparison confirmed installed2.6.3 and lateststable[2.7.13](https://github.com/microsoft/WSL/releases/tag/2.7.13) still omit the timeout in that create-process loop; prerelease[2.9.8](https://github.com/microsoft/WSL/releases/tag/2.9.8) contains it. No WSL upgrade or VM restart was performed.

The first cleanup dry run stopped safely before signals because it queried the system service instead of Joshua's user service. After correcting that query using verified UID1000, the successful03:51:21 dry run verified all70 identities,43 dead session/group pairs, and the one live `Relay(12601)` plus root-PTY/controller ancestry to preserve. Each candidate had matching census start ticks, exact `Relay` and `/init` identity, orphan parent, a single thread, no children or interop endpoint, ageover600seconds, the same PIDnamespace, absent session/group leaders and no unrelated process sharing its session/group. Every signal was bound to a pidfd and preceded by a fresh identity/session/ancestry assessment; there was no numericPID or process-name fallback.

Root executed the three-PID pilot at03:52:00UTC and the separate remaining67 mode at03:52:41. All70 exits were confirmed. Both reports verified unchanged controllerPID1608933, exactRC9/6c5ff192 and all188 installed-source hashes, plus preserved liveRelay and protected ancestry. LocalInbox returned200 in1.117seconds after the pilot and2.089seconds after the remaining cleanup. Root's subsequent fresh Windows `wsl.exe` process probe exited0 in0.265seconds; Windows Tailscale Now/Input returned200 in2.81/2.63seconds. An independent freshWSL operator Input sweep completed successfully at03:54:43.

This demonstrates mitigation of the accumulated orphan-resource problem and restored creation of WSL sessions. It does not prove permanent repair, quantify the reclaimed hv-socket resources, or establish that the leak caused every observedAWS502. No VM, controller or Tailscale restart, host launch, capacity change, deadline extension, or package hotpatch accompanied the cleanup. The600-second lease mitigation remains until the existing versionedCG428 fix is deployed and actual recovery is verified.

## Evidence

- `/home/joshua/work/operator-test-tmp/cg463-reclaim-20260909/worker-{0,3,2}-capture.json`: worker error journals, source and transcript preservation.
- `/home/joshua/work/operator-test-tmp/input-sweep-20260908T2125/remote-lease-600-mitigation.json`: prior policy, single changed line, current generation fingerprints and restoration rule.
- `/home/joshua/work/operator-test-tmp/input-sweep-20260908T2125/lease600-valid-heartbeat-receipts.json`: actual post-claim renewal proof.
- `/home/joshua/work/operator-test-tmp/input-sweep-20260908T2125/controller-502-investigation.json`: controller journal and service facts; WSL Tailscale absence is expected.
- `/home/joshua/work/operator-test-tmp/input-sweep-20260908T2125/windows-tailscale-live-0303.log`: bounded read-only Windows daemon log tap.
- `/home/joshua/work/operator-test-tmp/cg463-reclaim-20260909/kernel-relay-{readonly,analysis}.json` and `relay-process-census.json`: bounded kernel evidence and all70 original identities.
- `/home/joshua/work/operator-test-tmp/cg463-reclaim-20260909/relay-gc-{dry-run,pilot,remaining}.json`: candidate/preservation guards, exact signal receipts, controller/source snapshots and HTTP verification.
- `/home/joshua/work/operator-test-tmp/cg463-reclaim-20260909/gc-confirmed-orphan-relays.py`: reviewed helper; default read-only, separate three-process pilot and remaining modes, pidfd identity guards.
- `/home/joshua/work/operator-test-tmp/cg463-reclaim-20260909/wsl-release-accept-source-comparison.json`: official tagged-source excerpts proving timeout presence/absence.

Current permanent transport candidate at03:56UTC: CG428/PR334, native-rebased head `a3dbd8be1de301af44a7b6882fa233e3ccf4f637`, with both exact full CI runs passing. Its native pre-PR check `20260909T034055Z-check` owns further progress. The earlier reconciliation `64b8e4faceb9a5b18ad9a4eca60b06df060384cf` and its actual results remain preserved. Neither source is described as deployed or merged until those facts are independently verified.

