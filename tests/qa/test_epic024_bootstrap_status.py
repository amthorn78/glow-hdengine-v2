from tools.qa.run_hde_epic024_harness import _status_from_bootstrap


def test_bootstrap_missing_pytest_maps_to_tooling_failure():
    stderr = "ModuleNotFoundError: No module named 'pytest'\n"
    assert _status_from_bootstrap(1, stderr) == "FAIL_TOOLING"


def test_bootstrap_exit_code_one_still_counts_as_behavior_failure():
    stderr = "E   AssertionError: failed test\n"
    assert _status_from_bootstrap(1, stderr) == "FAIL_BEHAVIOR"
