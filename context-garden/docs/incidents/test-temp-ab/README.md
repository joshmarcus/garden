# RAM-backed versus disk-backed test temp — 2026-09-06

Owner requested a controlled test after asking whether CPU or I/O caused the observed pressure. Two full suites ran serially in the same detached c1f75cb checkout, same Python environment and command, with CPUQuota200%, MemoryHigh3GiB/Max4GiB/SwapMax512MiB. No ordinary garden workers were active at start; live admission remained paused. Changed only TMPDIR/PYTEST_DEBUG_TEMPROOT/pytest basetemp from a dedicated tmpfs directory to a dedicated ext4 directory. Live garden temp configuration was not changed.

| Metric | tmpfs | ext4 |
|---|---:|---:|
| Wall time |163.13s|222.01s|
| Peak cgroup memory (kernel counter)|968.79MiB|1522.57MiB|
| CPU time|130.02s|147.22s|
| CPU stall fraction|0.13%|0.10%|
| I/O stall fraction|0.19%|11.47%|
| Swap / memory.high events|0 / 0|0 / 0|
| Test outcome|1181 passed,3 skipped|1180 passed,1 failed,3 skipped|

Disk-backed temp was36% slower and had a57% larger peak charged footprint in this pair. Disk page cache and kernel filesystem metadata still consume RAM, although clean disk cache can be reclaimed; shmem peaked415MiB on tmpfs and0 on disk. Cgroup peak includes descendants, cache and kernel memory, not just pytest heap. Host disk counters showed about1.52GiB writes on ext4 versus32MiB on tmpfs; host counters are not exclusive attribution. The per-cgroup I/O pressure measurement provides direct evidence of waiting during the disk variant. CPU throttling was negligible in both isolated runs.

Limitations: one serial A/B pair, RAM first; cache/order effects are not controlled, and this does not reproduce simultaneous production harness/full-suite contention. It does not establish that CPU or I/O was absent during earlier incidents. Both runs stayed below memory.high; behavior under reclaim pressure may differ. Do not change live temp solely on an assumed speed/memory benefit from disk. Install/verify shared admission first; retain evidence for any later bounded concurrent comparison.

The ext4 run exposed test_archive_round_trip_preserves_summary_and_artifacts failing with an empty all_runs() after restore. A separate focused tests/test_run_index.py run on ext4 reproduced it (1failed,6passed). CG-360 tracks correctness; do not perform production archival/restoration until repaired and verified. No production history was moved or deleted. The process launcher itself exited normally even though disk pytest failed; the recorded exit_code and test outcome above are authoritative.

Raw result JSON and measurement source are adjacent. Full sample streams and pytest logs remain at /home/joshua/work/operator-test-tmp/io-ab-20260906. Temporary experiment data is preserved outside active garden run paths.
