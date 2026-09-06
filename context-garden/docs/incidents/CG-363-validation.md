# CG-363 — worker CI offload

Implemented directly by the operator under owner authority. PR243 merged58e13b99ddaf62b751b01771e5660039a421d46c at2026-09-06T22:49:56Z. Final branch ec0876b4e12984f2f9539d1afb9bcf9ea6d60bc4.

- 47 focused worker-CI/brief tests passed in1.12s,65.5MiB peak.30 merge-gate tests passed in6.03s,115.5MiB peak. Local units capped1CPU,512MiB high/768MiB max; serial. Full lint passed.
- Actual isolated worker HOME plus explicit GH_CONFIG_DIR and service PATH pushed a branch before any PR existed. Initial successful run34064715342 was correctly rejected after the checkout moved. Final branch run[34064850874](https://github.com/joshmarcus/context-garden/actions/runs/34064850874) passed1224 tests/3skipped in255.85s. A repeated helper invocation returned the same successful run without creating another.
- PR integration run[34064888618](https://github.com/joshmarcus/context-garden/actions/runs/34064888618) and main run[34065153856](https://github.com/joshmarcus/context-garden/actions/runs/34065153856) passed before deployment. Missing PR CI now holds automerge for opted-in products.
- Candidate configuration was exercised through actual run_check and generated CG361 briefs. It preserves the separate garden-documents product; unknown future products fail explicitly instead of silently skipping their checks.
- Live installation of58e13b99 completed at an accounted drained tick boundary; bounded installer peak135.4MiB. Existing service restarted as PID2008482 with persistent caps unchanged and ordinary admission paused. No additional model reviewer launched. Manual result recorded deployment pending at code completion; this document and task log record its subsequent fulfillment.
- Deployed setup.worker_push=true, full test command python3 scripts/check_ci.py, focused lint, explicit GH_CONFIG_DIR and isolated HOME. Pre-PR checks no longer repeat the full suite locally. Full PR CI remains required. Existing branches must incorporate the new workflow/helper; resource-specific local fixture checks remain bounded.
- Post-restart HTTP /,Now2,Inbox,Config returned200 in1.790/.563/.615/.253s. Windows Now2 returned200 in2.044s. Service142MiB,swap0,zero memory.high/max/OOM events. These idle deployment checks are not sustained loaded recovery or an unattended stabilization pass.

The helper is repository tooling and its branch push permission is an explicit briefing/configuration permission, not a new security sandbox. Raw logs remain in /home/joshua/work/operator-test-tmp/CG363-ci*.log. Operator spend remains unknown.

CG360's archive consistency repair is also included in the installed build. Its earlier installation hold is cleared; no production history has been moved or deleted. CG361 still owns per-run workload enforcement and web-capacity reservation. Incident recurrence observation and retrospective remain open.
