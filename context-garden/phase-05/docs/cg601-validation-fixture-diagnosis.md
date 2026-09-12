# CG-601: inherited validation-policy fixture failure

The owner-approved scope is a synthetic fixture correction after CG-600 actually merges. No real stress workload is authorized. On September11 at00:13:02UTC, the exact same source passed with clean PYTEST_ADDOPTS and failed with inherited worker POLICY_ADDOPTS. The inherited default exclusions suppress three deliberate dummy failures, causing nested pytest to return0 where this test expects1.

The test and validation module match accepted main059a28e4277248b6782a759e0d2647e92b594553 byte-for-byte. The test calls resolve_validation directly, then subprocess.run without the environment normalization used by validation.main. This explains this named failure only, not the second unidentified full-suite failure or900-second timeout. Preserve default production enforcement and unrelated pytest options; isolate the fake subprocess or exercise the appropriate public normalization.

The controller's cached checkout lacks this newly added test file at brief-validation time. The exact pertinent source is therefore inlined below; once dispatched, read tests/test_validation.py and src/garden/validation.py in the task's own current checkout. Do not switch to another checkout.

Source hashes: {"src/garden/validation.py": "8b1caf5a657b05e21620ee59d647e008c2c03a039b0918ac09cf8971ce97af1b", "tests/test_validation.py": "c06ebb6ff4bb38d88b5158f740b91cd1a5da5b0e03a0ae0c6c651d1221810b19"}

## Synthetic checkout and affected tests

```python
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from garden import validation
from garden.validation import (
    POLICY_SOURCE_SHA,
    STRESS_NODES,
    ValidationPolicyError,
    enforce_validation_policy_env,
    resolve_validation,
)


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-c", "user.name=test", "-c", "user.email=test@example.com", *args],
        cwd=repo, check=True, capture_output=True, text=True,
    ).stdout.strip()


def _checkout(tmp_path: Path, shape: str) -> Path:
    repo = tmp_path / shape
    repo.mkdir()
    _git(repo, "init", "-q", "-b", "main")
    tests = repo / "tests"
    tests.mkdir()
    (tests / "test_web.py").write_text(
        "def test_functional(tmp_path):\n"
        "    (tmp_path / 'functional').write_text('ran')\n\n"
        "def test_initial_pages_stay_bounded_with_large_run_history():\n"
        "    raise AssertionError('stress workload ran')\n\n"
        "def test_retained_history_journey_stays_responsive_with_running_and_waiting_pytest():\n"
        "    raise AssertionError('stress workload ran')\n\n"
        "def test_served_incident_controls_retry_and_restart_during_overload():\n"
        "    raise AssertionError('stress workload ran')\n"
    )
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "old source")
    if shape == "current":
        (tests / "conftest.py").write_text(
            "def pytest_addoption(parser):\n"
            "    parser.addoption('--run-stress', action='store_true')\n"
        )
        _git(repo, "add", "-A")
        _git(repo, "commit", "-q", "-m", "current policy hook")
    elif shape == "stacked":
        _git(repo, "checkout", "-q", "-b", "parent")
        (repo / "parent.txt").write_text("parent implementation\n")
        _git(repo, "add", "-A")
        _git(repo, "commit", "-q", "-m", "parent implementation")
        _git(repo, "checkout", "-q", "-b", "child")
        (repo / "child.txt").write_text("child implementation\n")
        _git(repo, "add", "-A")
        _git(repo, "commit", "-q", "-m", "child implementation")
    elif shape == "dirty":
        (repo / "implementation.py").write_text("valuable_uncommitted_edit = True\n")
    return repo


@pytest.mark.parametrize("shape", ["old", "current", "stacked", "dirty"])
def test_current_policy_excludes_old_stress_without_rewriting_checkout(tmp_path, shape):
    repo = _checkout(tmp_path, shape)
    head_before = _git(repo, "rev-parse", "HEAD")
    diff_before = _git(repo, "diff", "--", ".")
    requested = [sys.executable, "-m", "pytest", "-q"]

    effective, policy = resolve_validation(requested, repo)
    result = subprocess.run(effective, cwd=repo, capture_output=True, text=True, timeout=15)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 passed" in result.stdout
    assert "3 deselected" in result.stdout
    assert policy["source_sha"] == POLICY_SOURCE_SHA
    assert policy["excluded_nodes"] == list(STRESS_NODES)
    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert _git(repo, "diff", "--", ".") == diff_before
    if shape == "dirty":
        assert (repo / "implementation.py").read_text() == "valuable_uncommitted_edit = True\n"


def test_old_branch_can_explicitly_opt_in_to_known_stress(tmp_path):
    repo = _checkout(tmp_path, "old")
    requested = [sys.executable, "-m", "pytest", "--run-stress", "-q"]

    effective, policy = resolve_validation(requested, repo)
    result = subprocess.run(effective, cwd=repo, capture_output=True, text=True, timeout=15)

    assert "--run-stress" not in effective  # the old pytest config does not define the option
    assert result.returncode == 1
    assert "3 failed, 1 passed" in result.stdout
    assert policy["stress_opt_in"] is True
    assert policy["excluded_nodes"] == []
```

## Policy resolver and environment normalization

```python
def enforce_validation_policy_env(env: dict[str, str]) -> None:
    """Make even a branch-issued plain pytest command obey the current default policy."""
    existing = shlex.split(env.get("PYTEST_ADDOPTS", ""))
    env["PYTEST_ADDOPTS"] = shlex.join([*existing, *(opt for opt in POLICY_ADDOPTS if opt not in existing)])


def _enable_stress_opt_in(env: dict[str, str]) -> None:
    existing = shlex.split(env.get("PYTEST_ADDOPTS", ""))
    env["PYTEST_ADDOPTS"] = shlex.join([opt for opt in existing if opt not in POLICY_ADDOPTS])


def _pytest_command(argv: list[str]) -> bool:
    executable = Path(argv[0]).name
    if executable in {"pytest", "py.test"}:
        return True
    return executable.startswith("python") and len(argv) > 2 and argv[1:3] == ["-m", "pytest"]


def resolve_validation(argv: list[str], cwd: Path) -> tuple[list[str], dict[str, object]]:
    """Apply the approved current test policy without modifying the source checkout."""
    requested = list(argv)
    if not _pytest_command(argv):
        launcher = Path(argv[0]).name
        raise ValidationPolicyError(
            f"validation command {launcher!r} cannot be proven non-pytest; "
            "invoke pytest directly through garden.validation and run other tools directly"
        )

    opted_in = "--run-stress" in argv
    policy_hook = cwd / "tests" / "conftest.py"
    branch_supports_opt_in = policy_hook.is_file() and "--run-stress" in policy_hook.read_text(
        errors="replace"
    )
    effective = list(argv)
    if opted_in and not branch_supports_opt_in:
        effective = [arg for arg in effective if arg != "--run-stress"]
    excluded: list[str] = []
    if not opted_in:
        excluded = list(STRESS_NODES)
        effective.extend(f"--deselect={node}" for node in excluded)
    return effective, {
        "version": 1,
        "source_sha": POLICY_SOURCE_SHA,
        "kind": "pytest",
        "stress_opt_in": opted_in,
        "excluded_nodes": excluded,
        "requested_selection": requested,
        "effective_selection": effective,
    }
```

The main entry point calls `_enable_stress_opt_in(os.environ)` when `policy["stress_opt_in"]` is true before launching its supervised validation. Evidence: `/home/joshua/work/operator-test-tmp/rc20-20260910/validation-fixture-diagnosis/receipt.json`, clean_env.log and inherited_worker_policy.log.
