# CG619: exact run identity in recovery references

The authoritative source is accepted main69cc62f4fc345928fdfe3aec5f407ddf978138e4, staged at /home/joshua/work/operator-test-tmp/ci-run-id-prefix-20260911/source. The older cached reading index lacks branch_cleanup.py and scheduler/cleanup.py, but these files exist in the actual accepted source. Read src/garden/branch_cleanup.py, src/garden/scheduler/cleanup.py, tests/test_branch_cleanup.py and tests/test_storage_cleanup.py there when working on or reviewing this task.

The existing recovery predicate is run.run_id in state_text. The scheduler supplies JSON-serialized state, excluding only its branch-cleanup bookkeeping. RunStore.next_run_id generates same-second sibling IDs by appending -2,-3. Consequently a pointer to the suffixed ID also matches its shorter-prefix sibling as a substring.

Actual GitHub push CI34552728651 at8e4321c8 reports one failing storage-cleanup integration test,2753passes,4skips,4deselected. Its expected-removable branch was incorrectly needed because of a recovery reference. The source of that predicate is unchanged by the local-startup repair.

Root's deterministic new regression explicitly creates a completed shorter-prefix branch and a completed suffixed branch, both already preserved in main, then references only the latter. On unmodified main all four forms failed with the same false recovery hold: direct ID, nested JSON state, backup path and colon-delimited stash name. The red receipt and full output are preserved in red-execution beneath the directory above.

The working correction keeps literal complete run references with ID boundaries, including -N suffixes and literal regexp characters. The referenced suffixed run remains held. The full focused branch/storage cleanup selection passes31tests, including the original integration failure and eight explicit prefix cases. No live cleanup occurred. Execution was Linux through WSL; macOS was not exercised. Actual exact-source CI and independent review remain publication/merge gates.


Evidence digests:
- /home/joshua/work/operator-test-tmp/ci-run-id-prefix-20260911/red-execution/receipt.json: ea2205fe0ff8df5d16da0427dfe6d2a38e2a42313eb60c8a7409dbe0eceb485d
- /home/joshua/work/operator-test-tmp/ci-run-id-prefix-20260911/red-execution/output.log: aadc3bb0a1f498e8b7915c71bb5cd10d3a9a27a38a5ecd9c8ecf11d9aa8c8548
- /home/joshua/work/operator-test-tmp/ci-run-id-prefix-20260911/green-execution/receipt.json: 96c3c839a58099d734ad6e6e98f2082a31f032bd30fe2b54407d6f6fa9886b06
- /home/joshua/work/operator-test-tmp/ci-run-id-prefix-20260911/green-execution/output.log: bb750032bb685c51d18d5afad2b1bb9b9ecff362e42798f5e24ee4cd2147ae05
