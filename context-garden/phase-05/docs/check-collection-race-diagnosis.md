# Check collection after a newer completion

Root reproduced this on accepted source69d903ace81528ee4056e663339eb70cd18b0d1a. The installed RC19 implementations of Run._merge_concurrent_record and Scheduler.reap_check are byte-identical to the tested methods. In a disposable scheduler, a synthetic committed completion arrives after the collector loaded its Run but before the terminal save. Run.save correctly preserves the newer worker record; reap_check nevertheless calls its continuation with status running, returns success and clears check_run. The final is retained, but the check remains active without its continuation. The regression assertion failed in0.56seconds on Linux through WSL. This is a deterministic interleaving test, not an instrumented trace of the original live race.

The live CG616 check20260911T023905Z-check has authenticated final_received_at, passing check/mechanical results, status running, no finished_at/exit metadata and no current check_run pointer, while its task progressed through later reviews/revisions. The original record is preserved privately in /home/joshua/work/operator-test-tmp/check-collection-race-20260911/cg616-original-orphan-run.json; do not print credentials/lease material from it. A similar older CG600 terminal check was retired through the supported terminal-check path. These observations are consistent with the reproduced gap; the exact historical interleaving was not recorded.

The authoritative reproduction and receipt are /home/joshua/work/operator-test-tmp/check-collection-race-20260911/{test_stale_completion.py,execution/receipt.json,execution/output.log,installed-method-comparison.json}. Remote workers receive this inline reproduction and should add a repository-native deterministic regression. Inspect scheduler/checkruns.py, runs.py and relevant work/review collection callers. Preserve CG584 shared locking and newer completion/generation protection; do not solve this by allowing stale scheduler writes to overwrite worker finalization. Report untested macOS accurately. No live run edits, cleanup or paid canary is needed.

```python
import json
from garden.model import Status
from garden.runs import Run
from garden.scheduler import TickReport
pytest_plugins = ['tests.conftest']

def test_check_cannot_advance_after_new_completion_supersedes_collection(sched, monkeypatch):
    task = sched.store.task('DM-001')
    task.status = Status.RUNNING
    sched.store.save(task)
    run = sched.runs.new_run(task.id, 'remote', mode='check')
    run.lease_token = 'synthetic-current-generation'
    run.save()
    sched.state.get(task.id)['check_run'] = {'run_id': run.run_id, 'stage': 'pre_pr', 'cont': {}, 'specs': []}
    sched.state.save()
    monkeypatch.setattr(sched, 'runner_for', lambda *args: object())
    monkeypatch.setattr(sched, '_finished_or_timed_out', lambda *args: True)
    calls = []

    def publish_completion_after_collector_loaded(stale):
        current = Run.load(stale.path)
        current.final_received_at = '2026-09-11T03:23:00+00:00'
        current.pushed_head = 'f' * 40
        (current.path / 'exit_code').write_text('0')
        (current.path / 'checks.json').write_text(json.dumps([{'name': 'lint', 'status': 'pass', 'summary': 'ok'}]))
        current.save()
        return [{'name': 'lint', 'status': 'pass', 'summary': 'ok'}]

    def continue_to_next_phase(task, run, results, cont, rep):
        calls.append(run.status)

    monkeypatch.setattr(sched, '_collect_check_results', publish_completion_after_collector_loaded)
    monkeypatch.setattr(sched, '_after_pre_pr_check', continue_to_next_phase)
    result = sched.reap_check(task, TickReport())
    durable = Run.load(run.path)
    pointer = sched.state.get(task.id).get('check_run')
    evidence = {'reap_returned': result, 'saved_status': durable.status,
                'continuation_called_with_status': calls, 'remaining_pointer': pointer,
                'authenticated_completion_retained': durable.final_received_at}
    print(json.dumps(evidence, sort_keys=True))
    assert durable.final_received_at == '2026-09-11T03:23:00+00:00'
    assert durable.status == 'done' or (not calls and pointer and pointer['run_id'] == run.run_id), evidence

```
