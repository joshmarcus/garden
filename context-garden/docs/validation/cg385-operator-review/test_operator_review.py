pytest_plugins = ["tests.conftest"]
from tests.scheduler.test_resources import _cache_limited

def test_normal_tick_reaches_cache_reclaim(sched, monkeypatch, tmp_path):
    _cache_limited(sched, monkeypatch, tmp_path)
    attempts = []
    monkeypatch.setattr(sched, "_start_reclaim_if_eligible", lambda status: attempts.append(status) or False)
    sched.tick()
    assert attempts, "Normal tick remains blocked without attempting eligible reclaim"

def test_concurrent_state_publication_is_safe(sched, monkeypatch, tmp_path):
    import os
    import threading
    from concurrent.futures import ThreadPoolExecutor
    from garden.scheduler import resources
    target = tmp_path / "reclaim.json"
    temporary = target.with_suffix(f".{os.getpid()}.tmp")
    barrier = threading.Barrier(2)
    original = resources.os.replace
    def replace(src, dst):
        if src == temporary:
            barrier.wait(timeout=3)
        return original(src, dst)
    monkeypatch.setattr(resources.os, "replace", replace)
    def publish(i):
        try:
            sched._write_reclaim_state(target, {"running": False, "result": i})
        except Exception as error:
            return type(error).__name__
        return None
    with ThreadPoolExecutor(max_workers=2) as pool:
        errors = list(pool.map(publish, [1, 2]))
    assert errors == [None, None], errors
