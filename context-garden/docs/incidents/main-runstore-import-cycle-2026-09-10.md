# Main import regression after CG-584 merge

At the September10 operator audit, main was found to fail before collecting tests on Python3.12. The first failing main build after the last passing main build is the CG-584 merge; later branches inherit the same import chain. These are observed CI results, not a claim of deployed RC16 failure.

- Last passing main: https://github.com/joshmarcus/context-garden/actions/runs/34488489354 at 0eb7a66eabfbd7549938c2848eb8a275ecffee53.
- First failing main: https://github.com/joshmarcus/context-garden/actions/runs/34489071296 at 9565228279b58d754efd026d32be51bd2da368d9.
- Still failing main: https://github.com/joshmarcus/context-garden/actions/runs/34491506154 at c1b0022c0e5ff27318ec5fe75e6ed5c9ef1df9cc.
- Inherited sandbox branch failure: https://github.com/joshmarcus/context-garden/actions/runs/34491838535 at beebdc74762e21c9d359747a11e7e4fdedb300d7.

The pytest conftest imports garden.runner. runner/base.py imports Run from runs.py; runs.py imports file_lock from hosts.locking, which executes hosts/__init__.py and imports hosts.drain. drain.py imports RunStore before runs.py has initialized it. Python raises ImportError for the partially initialized garden.runs module, exiting pytest with code4.

CG-584's original exact-head CI, focused tests and independent approval remain valid historical evidence for that tested source and import context. They do not establish a healthy final merge on current main. Preserve the cross-process protection while restoring clean-process import order and full CI. RC16 is still installed and both controller processes are healthy; do not hotpatch the immutable installed runtime.
