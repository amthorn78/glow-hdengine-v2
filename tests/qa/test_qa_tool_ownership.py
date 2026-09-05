from __future__ import annotations

import importlib
import json
import runpy
import tempfile
from copy import deepcopy
from pathlib import Path

import pytest

from ci.checks import classify_ci_changes as classifier
import tools.qa
import tools.qa.examples
from tools.evidence import refresh_epic024_step_logs_manifest as evidence_refresh
from tools.qa import refresh_epic024_step_logs_manifest as qa_refresh
from tools.qa import step_log_header
from tools.qa.examples import d13_refactored_example as d13_example


ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(autouse=True)
def closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")


def test_qa_package_markers_are_importable() -> None:
    assert tools.qa.__name__ == "tools.qa"
    assert tools.qa.examples.__name__ == "tools.qa.examples"
    assert Path(tools.qa.__file__).is_file()
    assert Path(tools.qa.examples.__file__).is_file()


def test_qa_tool_registry_matches_candidate_sources() -> None:
    tracked = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "tools/qa").rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and path.suffix.lower() == ".py"
    }
    registered = set(classifier._QA_TOOL_TEST_OWNERS)
    blocked = classifier._QA_TOOLS_REQUIRING_OWNER
    assert registered | blocked == tracked
    assert not registered & blocked
    assert all(
        classifier._QA_TOOL_OWNERSHIP_TEST in owners
        for owners in classifier._QA_TOOL_TEST_OWNERS.values()
    )


def test_step_log_header_is_canonical_and_tmp_scoped(tmp_path: Path) -> None:
    header = step_log_header.create_header(
        check_id="owned-check",
        command="python -m pytest",
        status="PARKED",
        intended_tokens=["OWNED_TOKEN"],
    )
    assert header["captured_env"] == {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }
    assert step_log_header.update_header_status(header, "PASS") is header
    assert header["claimed_tokens"] == []

    output = tmp_path / "checks" / "primary.log"
    step_log_header.write_header(output, header)
    step_log_header.append_output(
        output, "PASS: bounded owner; OWNED_TOKEN not evaluated or claimed"
    )
    lines = output.read_text(encoding="utf-8").splitlines()
    assert json.loads(lines[0]) == header
    assert lines[1] == "PASS: bounded owner; OWNED_TOKEN not evaluated or claimed"
    assert output.read_bytes().endswith(b"\n")

    with pytest.raises(ValueError, match="Invalid status"):
        step_log_header.create_header("bad", "false", status="UNKNOWN")


def test_epic024_refresh_wrapper_delegates_to_current_implementation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert qa_refresh.main is evidence_refresh.main
    monkeypatch.setattr(evidence_refresh, "main", lambda: 37)
    wrapper = ROOT / "tools/qa/refresh_epic024_step_logs_manifest.py"
    with pytest.raises(SystemExit) as exc_info:
        runpy.run_path(str(wrapper), run_name="__main__")
    assert exc_info.value.code == 37


@pytest.mark.parametrize(
    "scenario,status,exit_code",
    [
        ("complete", "PASS", 0),
        ("missing-index", "TOOLING_BLOCKED", 13),
        ("missing-proof", "TOOLING_BLOCKED", 13),
        ("missing-entry", "FAIL_BEHAVIOR", 1),
        ("malformed-json", "FAIL_BEHAVIOR", 1),
        ("unexpected-error", "FAIL_TOOLING", 1),
    ],
)
def test_d13_example_writes_only_to_the_injected_output(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    scenario: str,
    status: str,
    exit_code: int,
) -> None:
    index = tmp_path / "INDEX.json"
    proof = tmp_path / "INDEX.json.path_proof.txt"
    output = tmp_path / "D13" / "primary.log"
    index.write_text(
        json.dumps([{"path": path} for path in sorted(d13_example.REQUIRED_PATHS)])
        + "\n",
        encoding="utf-8",
    )
    proof.write_text("proof\n", encoding="utf-8")
    monkeypatch.setattr(d13_example, "INDEX_PATH", index)
    monkeypatch.setattr(d13_example, "INDEX_PROOF", proof)
    monkeypatch.setattr(d13_example, "OUTPUT_PATH", output)

    if scenario == "missing-index":
        index.unlink()
    elif scenario == "missing-proof":
        proof.unlink()
    elif scenario == "missing-entry":
        index.write_text("[]\n", encoding="utf-8")
    elif scenario == "malformed-json":
        index.write_text("{invalid\n", encoding="utf-8")
    elif scenario == "unexpected-error":

        def fail_load(*args, **kwargs):
            raise RuntimeError("injected reader failure")

        monkeypatch.setattr(d13_example.json, "load", fail_load)

    assert d13_example.main() == exit_code
    lines = output.read_text(encoding="utf-8").splitlines()
    header = json.loads(lines[0])
    assert header["status"] == status
    assert header["intended_tokens"] == header["claimed_tokens"] == []
    assert lines[1]
    if scenario != "malformed-json":
        assert lines[1].startswith(status + ":")


@pytest.mark.parametrize(
    "status", ["PASS", "FAIL_BEHAVIOR", "FAIL_TOOLING", "TOOLING_BLOCKED", "PARKED"]
)
@pytest.mark.parametrize(
    "claims", [{}, {"claimed_tokens": None}, {"claimed_tokens": []}],
    ids=["omitted", "none", "empty"],
)
def test_new_headers_never_infer_claims(status: str, claims: dict) -> None:
    header = step_log_header.create_header(
        "synthetic", "fixture", status=status, intended_tokens=["A"], **claims
    )
    assert header["status"] == status
    assert header["intended_tokens"] == ["A"]
    assert header["claimed_tokens"] == []
    other = step_log_header.create_header("other", "fixture")
    assert other["claimed_tokens"] is not header["claimed_tokens"]


@pytest.fixture
def claimed_header() -> dict:
    header = step_log_header.create_header(
        "synthetic", "fixture", "PASS", ["PF27"], ["A", "B", "C"], ["A"], {}
    )
    header["evidence_outputs"] = ["fixture.json"]
    header["exit_code"] = 0
    return header


@pytest.mark.parametrize("prior_status", ["PARKED", "PASS"])
@pytest.mark.parametrize(
    "status", ["PASS", "FAIL_BEHAVIOR", "FAIL_TOOLING", "TOOLING_BLOCKED", "PARKED"]
)
@pytest.mark.parametrize(
    "claims", [{}, {"claimed_tokens": None}, {"claimed_tokens": []}],
    ids=["omitted", "none", "empty"],
)
def test_new_outcomes_replace_previous_claims(
    claimed_header: dict, prior_status: str, status: str, claims: dict,
) -> None:
    if prior_status == "PARKED":
        step_log_header.update_header_status(claimed_header, "PARKED")
    expected = deepcopy(claimed_header)
    expected.update(status=status, claimed_tokens=[])
    result = step_log_header.update_header_status(claimed_header, status, **claims)
    assert result is claimed_header
    assert claimed_header == expected


@pytest.mark.parametrize(
    "status,intentions,claims,message",
    [
        ("FAIL_BEHAVIOR", ["A"], ["A"], "require PASS"),
        ("FAIL_TOOLING", ["A"], ["A"], "require PASS"),
        ("TOOLING_BLOCKED", ["A"], ["A"], "require PASS"),
        ("PARKED", ["A"], ["A"], "require PASS"),
        ("PASS", ["A"], ["B"], "appear in intended_tokens"),
        ("PASS", None, ["A"], "appear in intended_tokens"),
        ("UNKNOWN", ["A"], ["B"], "Invalid status"),
    ],
)
def test_invalid_creation_and_updates_reject_without_mutation(
    claimed_header: dict,
    status: str,
    intentions: list | None,
    claims: list,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        step_log_header.create_header(
            "synthetic", "fixture", status=status,
            intended_tokens=intentions, claimed_tokens=claims,
        )
    if intentions is None:
        claimed_header.pop("intended_tokens")
    else:
        claimed_header["intended_tokens"] = intentions
    before = deepcopy(claimed_header)
    with pytest.raises(ValueError, match=message):
        step_log_header.update_header_status(claimed_header, status, claims)
    assert claimed_header == before


def test_explicit_pass_subset_retains_order_and_duplicates(
    claimed_header: dict, tmp_path: Path,
) -> None:
    claims = ["B", "A", "B"]
    created = step_log_header.create_header(
        "synthetic", "fixture", intended_tokens=["A", "B", "C"], claimed_tokens=claims
    )
    assert created["claimed_tokens"] == ["B", "A", "B"]
    assert step_log_header.update_header_status(claimed_header, "PASS", claims) is claimed_header
    assert claimed_header["claimed_tokens"] == ["B", "A", "B"]
    output = tmp_path / "primary.log"
    step_log_header.write_header(output, claimed_header)
    assert json.loads(output.read_text())["claimed_tokens"] == ["B", "A", "B"]


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize(
    "changes,error",
    [
        ({"status": "FAIL_BEHAVIOR"}, ValueError),
        ({"status": "FAIL_TOOLING"}, ValueError),
        ({"status": "TOOLING_BLOCKED"}, ValueError),
        ({"status": "PARKED"}, ValueError),
        ({"status": "UNKNOWN"}, ValueError),
        ({"intended_tokens": ["B"]}, ValueError),
        ({"extra": {1, 2}}, TypeError),
    ],
)
def test_rejected_publication_preserves_input_and_files(
    claimed_header: dict, tmp_path: Path, existing: bool, changes: dict, error: type,
) -> None:
    output = tmp_path / "new-directory" / "primary.log"
    if existing:
        step_log_header.write_header(output, claimed_header)
        step_log_header.append_output(
            output, "Earlier fixture outcome, not the rejected attempt."
        )
        prior_bytes = output.read_bytes()
    claimed_header.pop("pf_refs")  # Failed candidate normalization must not leak.
    claimed_header.update(changes)
    before = deepcopy(claimed_header)
    with pytest.raises(error):
        step_log_header.write_header(output, claimed_header)
    assert claimed_header == before
    if existing:
        assert output.read_bytes() == prior_bytes
    else:
        assert not output.parent.exists()


def test_valid_write_defaults_extra_fields_and_exact_bytes(tmp_path: Path) -> None:
    header = {
        "check_id": "fixture", "command": "fixture", "status": "PASS",
        "captured_env": {}, "exit_code": 0, "evidence_outputs": ["b", "a"],
    }
    output = tmp_path / "primary.log"
    assert step_log_header.write_header(output, header) is None
    assert header["pf_refs"] == header["intended_tokens"] == header["claimed_tokens"] == []
    expected = (
        b'{"captured_env":{},"check_id":"fixture","claimed_tokens":[],"command":"fixture",'
        b'"evidence_outputs":["b","a"],"exit_code":0,"intended_tokens":[],"pf_refs":[],"status":"PASS"}\n'
    )
    assert output.read_bytes() == expected
    assert step_log_header.serialize_header(header).encode("utf-8") == expected
    step_log_header.append_output(output, "body\n")
    assert output.read_bytes() == expected + b"body\n"


def test_publication_treats_none_claims_as_empty(tmp_path: Path) -> None:
    header = step_log_header.create_header("fixture", "fixture", intended_tokens=["A"])
    header["claimed_tokens"] = None
    output = tmp_path / "primary.log"
    step_log_header.write_header(output, header)
    assert header["claimed_tokens"] == []
    assert json.loads(output.read_text())["claimed_tokens"] == []


def test_historical_formatting_preserves_supplied_values(claimed_header: dict) -> None:
    claimed_header["status"] = "FAIL_BEHAVIOR"  # Contradictory retained history.
    claimed_header.pop("pf_refs")
    expected = deepcopy(claimed_header)
    expected["pf_refs"] = []
    assert step_log_header.normalize_header(claimed_header) is claimed_header
    assert step_log_header.normalize_header(claimed_header) == expected
    assert json.loads(step_log_header.serialize_header(claimed_header)) == expected
    minimal = {"status": "PARKED", "extra": {"retained": True}}
    assert step_log_header.normalize_header(minimal) is minimal
    assert minimal == {
        "status": "PARKED", "extra": {"retained": True},
        "pf_refs": [], "intended_tokens": [], "claimed_tokens": [],
    }


def test_environment_capture_is_exact_and_preserves_explicit_values(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    names = ["SAFE_MODE", "ALLOW_NETWORK", "APP_ENV", "LC_ALL", "LANG", "TZ"]
    for name in names:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("UNRELATED_SECRET", "synthetic-not-for-capture")
    assert step_log_header.capture_env() == dict.fromkeys(names)
    captured = step_log_header.create_header("fixture", "fixture")
    explicit = step_log_header.create_header("fixture", "fixture", captured_env={})
    assert captured["captured_env"] == dict.fromkeys(names)
    assert explicit["captured_env"] == {}


@pytest.mark.parametrize("status,exit_code", [("PASS", 0), ("FAIL_BEHAVIOR", 1)])
@pytest.mark.parametrize(
    "module_name",
    [
        "check_po_006_token_registry_validity",
        "check_epic024_acceptance_map_viability",
        "check_d23_evidence_index_snapshot_contract",
        "check_epic024_evidence_path_binding_validation",
    ],
)
def test_actual_evidence_callers_preserve_tokenless_outputs(
    tmp_path: Path, module_name: str, status: str, exit_code: int,
) -> None:
    module = importlib.import_module("tools.evidence." + module_name)
    module._write_primary_log(
        tmp_path, status=status, command="fixture", exit_code=exit_code,
        evidence_outputs=["fixture.json"], summary="Synthetic caller output",
    )
    lines = (tmp_path / "primary.log").read_text().splitlines()
    header = json.loads(lines[0])
    assert header["status"] == status
    assert header["claimed_tokens"] == header["intended_tokens"] == []
    assert header["exit_code"] == exit_code
    assert header["evidence_outputs"] == ["fixture.json"]
    assert lines[1] == "Synthetic caller output"


@pytest.mark.parametrize("status,exit_code", [("PASS", 0), ("FAIL_TOOLING", 2)])
def test_actual_epic024_writer_preserves_body_and_extra_fields(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, status: str, exit_code: int,
) -> None:
    from tools.qa import run_hde_epic024_harness as harness

    monkeypatch.setattr(harness, "QA_ROOT", tmp_path)
    output = harness._write_primary_log(
        check_id="fixture", command="fixture", status=status,
        exit_code=exit_code, evidence_outputs=["fixture.json"],
        stdout="synthetic stdout", stderr="synthetic stderr",
    )
    assert output == tmp_path / "checks" / "fixture" / "primary.log"
    lines = output.read_text().splitlines()
    header = json.loads(lines[0])
    assert header["status"] == status
    assert header["claimed_tokens"] == header["intended_tokens"] == []
    assert header["exit_code"] == exit_code
    assert header["evidence_outputs"] == ["fixture.json"]
    assert "synthetic stdout" in lines and "synthetic stderr" in lines
    assert lines[-1] == str(exit_code)


def test_current_template_is_isolated_and_explains_nonclaim(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(tempfile, "tempdir", str(tmp_path))
    exec(compile(step_log_header.EXAMPLE_TEMPLATE, "<step-log-template>", "exec"), {})
    lines = capsys.readouterr().out.splitlines()
    header = json.loads(lines[0])
    assert header["status"] == "PASS"
    assert header["intended_tokens"] == ["DEMO_REFERENCE"]
    assert header["claimed_tokens"] == []
    assert "predicate was not evaluated" in lines[1]
    assert list(tmp_path.iterdir()) == []
