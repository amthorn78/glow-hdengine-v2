from __future__ import annotations

import json
import runpy
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
    assert header["claimed_tokens"] == ["OWNED_TOKEN"]

    output = tmp_path / "checks" / "primary.log"
    step_log_header.write_header(output, header)
    step_log_header.append_output(output, "PASS: bounded owner")
    lines = output.read_text(encoding="utf-8").splitlines()
    assert json.loads(lines[0]) == header
    assert lines[1] == "PASS: bounded owner"
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


def test_d13_example_writes_only_to_the_injected_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
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

    assert d13_example.main() == 0
    lines = output.read_text(encoding="utf-8").splitlines()
    assert json.loads(lines[0])["status"] == "PASS"
    assert lines[1].startswith("PASS:")
