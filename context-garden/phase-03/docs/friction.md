# Friction

_No friction reported yet._

## Reported

### 2026-09-05 · reported by CG-137 (Split the scheduler by tick phase and the web actions into a registry so features stop colliding) in run 20260905T032209Z-work

- The acceptance criterion names product.md, which lives in the driving garden repo, not in this checkout; it cannot be edited from a product worktree.
- Baseline flake: tests/test_isolation.py::test_conftest_fixture_clears_ambient_env failed once under the runner's ambient GARDEN_ROOT and passed on later runs.
