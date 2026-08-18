from pathlib import Path

from tools.qa.qa_harness import HarnessConfig, Status, run_pytest_check


def test_missing_bootstrap_entrypoint_is_tooling_blocked(tmp_path: Path):
    result = run_pytest_check(HarnessConfig("HDE-EPIC021", repo_root=tmp_path), "bootstrap", ("missing_test.py",))
    assert result.status is Status.TOOLING_BLOCKED


def test_parked_is_not_placeholder_success():
    assert Status.PARKED is not Status.PASS
