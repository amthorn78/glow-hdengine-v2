import json

import pytest

import tools.qa.run_hde_epic024_harness as harness
from tools.qa.run_hde_epic024_harness import (
    _derive_retained_bootstrap_status,
    _one_path_diff_ok,
    _render_acceptance_map,
    _render_token_matrix,
    _selective_acceptance_bindings,
    _status_from_bootstrap,
)


def test_bootstrap_missing_pytest_maps_to_tooling_failure():
    stderr = "ModuleNotFoundError: No module named 'pytest'\n"
    assert _status_from_bootstrap(1, stderr) == "FAIL_TOOLING"


def test_bootstrap_exit_code_one_still_counts_as_behavior_failure():
    stderr = "E   AssertionError: failed test\n"
    assert _status_from_bootstrap(1, stderr) == "FAIL_BEHAVIOR"


def test_renderers_preserve_bootstrap_status_byte_identity():
    passing_map = json.loads(_render_acceptance_map(bootstrap_status="PASS"))
    passing_matrix = _render_token_matrix(bootstrap_status="PASS").decode("utf-8")
    assert _derive_retained_bootstrap_status(passing_map, passing_matrix) == "PASS"

    blocked_map = json.loads(_render_acceptance_map(bootstrap_status="TOOLING_BLOCKED"))
    blocked_matrix = _render_token_matrix(bootstrap_status="TOOLING_BLOCKED").decode("utf-8")
    assert _derive_retained_bootstrap_status(blocked_map, blocked_matrix) == "TOOLING_BLOCKED"
    assert _render_acceptance_map(bootstrap_status="PASS").endswith(b"\n")
    assert _render_token_matrix(bootstrap_status="PASS").endswith(b"\n")


def test_retained_bootstrap_status_conflict_refuses():
    acceptance = json.loads(_render_acceptance_map(bootstrap_status="PASS"))
    matrix = _render_token_matrix(bootstrap_status="TOOLING_BLOCKED").decode("utf-8")
    with pytest.raises(ValueError, match="conflicting retained bootstrap status"):
        _derive_retained_bootstrap_status(acceptance, matrix)


def test_one_path_diff_allows_exact_sanity_path_only():
    old = b'{"path":"artifacts/sanity/sanity.log"}\n'
    new = b'{"path":"audit/gates/sanity_pipeline/sanity_pipeline.log"}\n'
    assert _one_path_diff_ok(old, new)
    assert not _one_path_diff_ok(old + old, new + new)
    assert not _one_path_diff_ok(old, b'{"path":"other"}\n')


def test_selective_acceptance_bindings_exact_write_set_and_no_check_specs(tmp_path, monkeypatch):
    acceptance_path = tmp_path / "docs/acceptance_map_epic024.json"
    matrix_path = tmp_path / "audit/qa/hde-epic024/token_evidence_matrix.md"
    acceptance_path.parent.mkdir(parents=True)
    matrix_path.parent.mkdir(parents=True)
    current_map = _render_acceptance_map(bootstrap_status="PASS")
    current_matrix = _render_token_matrix(bootstrap_status="PASS")
    old_map = current_map.replace(
        b"audit/gates/sanity_pipeline/sanity_pipeline.log",
        b"artifacts/sanity/sanity.log",
        1,
    )
    old_matrix = current_matrix.replace(
        b"audit/gates/sanity_pipeline/sanity_pipeline.log",
        b"artifacts/sanity/sanity.log",
        1,
    )
    acceptance_path.write_bytes(old_map)
    matrix_path.write_bytes(old_matrix)

    monkeypatch.setattr(harness, "ACCEPTANCE_MAP_PATH", acceptance_path)
    monkeypatch.setattr(harness, "TOKEN_MATRIX_PATH", matrix_path)
    monkeypatch.setattr(harness, "_check_specs", lambda: pytest.fail("_check_specs called"))

    assert _selective_acceptance_bindings(write=False) == 1
    assert acceptance_path.read_bytes() == old_map
    assert matrix_path.read_bytes() == old_matrix

    assert _selective_acceptance_bindings(write=True) == 0
    assert acceptance_path.read_bytes() == current_map
    assert matrix_path.read_bytes() == current_matrix


def test_check_acceptance_bindings_no_write_when_current(tmp_path, monkeypatch):
    acceptance_path = tmp_path / "docs/acceptance_map_epic024.json"
    matrix_path = tmp_path / "audit/qa/hde-epic024/token_evidence_matrix.md"
    acceptance_path.parent.mkdir(parents=True)
    matrix_path.parent.mkdir(parents=True)
    acceptance_bytes = _render_acceptance_map(bootstrap_status="PASS")
    matrix_bytes = _render_token_matrix(bootstrap_status="PASS")
    acceptance_path.write_bytes(acceptance_bytes)
    matrix_path.write_bytes(matrix_bytes)

    monkeypatch.setattr(harness, "ACCEPTANCE_MAP_PATH", acceptance_path)
    monkeypatch.setattr(harness, "TOKEN_MATRIX_PATH", matrix_path)
    assert _selective_acceptance_bindings(write=False) == 0
    assert acceptance_path.read_bytes() == acceptance_bytes
    assert matrix_path.read_bytes() == matrix_bytes
