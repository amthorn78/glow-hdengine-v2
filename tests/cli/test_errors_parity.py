import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from engine.compat.error_tokens import ERROR_TOKEN_MAP, admission_token_for
import tools.errors.generate_error_artifacts as error_artifacts
from tools.errors.generate_error_artifacts import (
    SCENARIOS,
    capture_cli,
    capture_http,
    render_token_map,
)

pytestmark = pytest.mark.epic020

DETERMINISM_PINS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
}


@pytest.fixture(autouse=True)
def _rails(monkeypatch):
    for key, value in DETERMINISM_PINS.items():
        monkeypatch.setenv(key, value)


def _load_cli_artifact(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    payload: dict[str, object] = {"returncode": int(lines[0].split(":", 1)[1].strip())}
    stdout_line = lines[1].split(":", 1)[1] if ":" in lines[1] else ""
    payload["stdout"] = stdout_line
    # Remaining lines after "stderr:" belong to stderr payload
    stderr_lines = []
    for line in lines[3:]:
        stderr_lines.append(line)
    payload["stderr"] = "\n".join(stderr_lines)
    return payload


def test_parity_scenarios_are_bound():
    names = [scenario.name for scenario in SCENARIOS]
    assert names == [
        "invalid_json",
        "invalid_viewer_prefs",
        "db_unavailable",
        "vendor_attempt_closed_rails",
    ]

def _assert_http_and_cli_parity(scenario):
    stored_http = json.loads(
        Path(f"parity/errors_reader_cli.{scenario.name}.http.json").read_text(encoding="utf-8")
    )
    http_result = capture_http(scenario)

    assert http_result["body"]["code"] == scenario.token
    assert http_result["body"]["code"] in ERROR_TOKEN_MAP
    assert http_result == stored_http

    stored_cli = _load_cli_artifact(
        Path(f"parity/errors_reader_cli.{scenario.name}.cli.txt")
    )
    cli_result = capture_cli(scenario)

    assert cli_result["returncode"] != 0
    assert cli_result["stdout"] == ""
    assert scenario.stderr_expectation in cli_result["stderr"]
    assert cli_result == stored_cli


@pytest.mark.parametrize("scenario", SCENARIOS)
def test_http_and_cli_parity(monkeypatch, scenario):
    _assert_http_and_cli_parity(scenario)


def test_known_errors_parity(monkeypatch):
    for scenario in SCENARIOS:
        _assert_http_and_cli_parity(scenario)


def test_token_map_snapshot_matches_canonical():
    snapshot = json.loads(Path("errors/token_map/token_map.json").read_text(encoding="utf-8"))
    assert snapshot == render_token_map()
    for record in snapshot:
        assert record["code"] in ERROR_TOKEN_MAP


def test_token_map_bytes_are_canonical():
    """The token map is a release member: its owner writes exact canonical bytes."""
    from engine.serializer import canon

    raw = Path("errors/token_map/token_map.json").read_bytes()
    assert raw == canon.sercanon(render_token_map(), sort_keys=True)
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n")


# Every code the registry loader raises, split by what PF05 §5.2.3 says each one
# is. Both classes carry 503, so a misclassification is a wrong governed token
# rather than a wrong status -- which is exactly why a test has to pin it.
MANIFEST_ADMISSION_CODES = (
    "INVALID_MANIFEST",
    "INVALID_MANIFEST_KEYS",
    "INVALID_MANIFEST_ORDER",
    "INVALID_MANIFEST_PATH",
    "INVALID_MANIFEST_ROOT",
    "INVALID_MANIFEST_TIMESTAMP",
    "INVALID_MANIFEST_VERSION",
    "SELF_LISTING_MANIFEST_FORBIDDEN",
    "DUPLICATE_MANIFEST_ENTRY",
    "MANIFEST_MEMBER_HASH_MISMATCH",
    "MANIFEST_MEMBER_SIZE_MISMATCH",
    "ADMITTED_RELEASE_ROSTER_INVALID",
    "INCOMPLETE_RELEASE_ROSTER",
    "RELEASE_ROSTER_MISMATCH",
    "RELEASE_TIMESTAMP_MISMATCH",
    "RELEASE_VERSION_MISMATCH",
)
CONFIG_ADMISSION_CODES = (
    # Source-hash and source-binding disagreement: configuration, not manifest.
    "MECHANICS_SOURCE_MISMATCH",
    "INVALID_JSON_SOURCE",
    "SOURCE_CHANGED",
    "SOURCE_READ_FAILED",
    "UNBOUND_SOURCE",
    "UNSAFE_SOURCE_PATH",
    # Registry content rosters, which say nothing about the release roster.
    "CHANNEL_ID_ROSTER_MISMATCH",
    "FROZEN_CHANNEL_CENTER_ROSTER_MISMATCH",
    "PROFILE_ROSTER_MISMATCH",
    # Ordinary registry/schema defects.
    "SIGNAL_ORDER_MISMATCH",
    "CATEGORY_ORDER_MISMATCH",
    "INVALID_SCHEMA",
    "SCHEMA_VALIDATION_FAILED",
)


@pytest.mark.parametrize("code", MANIFEST_ADMISSION_CODES)
def test_manifest_and_release_roster_codes_are_manifest_mismatch(code):
    assert admission_token_for(code) == "ERR_M10_MANIFEST_MISMATCH"


@pytest.mark.parametrize("code", CONFIG_ADMISSION_CODES)
def test_every_other_admission_code_is_config_mismatch(code):
    assert admission_token_for(code) == "ERR_M10_CONFIG_MISMATCH"


def test_admission_classes_are_disjoint_and_unknown_codes_fail_to_config():
    assert not set(MANIFEST_ADMISSION_CODES) & set(CONFIG_ADMISSION_CODES)
    # An unrecognised or absent code is configuration, never a manifest claim.
    for code in (None, "", "SOMETHING_NEW"):
        assert admission_token_for(code) == "ERR_M10_CONFIG_MISMATCH"


def test_both_admission_tokens_carry_the_governed_503_status():
    from engine.compat.error_tokens import MAGIC10_HTTP_STATUS

    for token in ("ERR_M10_MANIFEST_MISMATCH", "ERR_M10_CONFIG_MISMATCH"):
        assert token in ERROR_TOKEN_MAP
        assert MAGIC10_HTTP_STATUS[token] == 503


# --- HDE-CRD-0003 S19-R04: asking an owner tool for usage changes nothing ------------------

_FIXED_TIME_NS = 1_000_000_000_000_000_000


def _tracked_copy(destination: Path) -> Path:
    """Copy every tracked file, with one fixed old mtime, so any rewrite is visible."""

    listed = subprocess.run(
        ["git", "-C", str(error_artifacts.ROOT), "ls-files", "-z"], check=True, capture_output=True
    ).stdout
    for raw in listed.split(b"\0"):
        if not raw:
            continue
        rel = raw.decode("utf-8")
        source, target = error_artifacts.ROOT / rel, destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_symlink():
            target.symlink_to(os.readlink(source))
        elif source.is_file():
            shutil.copy2(source, target)
            os.utime(target, ns=(_FIXED_TIME_NS, _FIXED_TIME_NS))
    return destination


def _tree_state(root: Path) -> dict[str, tuple[object, ...]]:
    state: dict[str, tuple[object, ...]] = {}
    for directory, names, files in os.walk(root):
        for name in names + files:
            path = Path(directory) / name
            info = path.lstat()
            body = (
                hashlib.sha256(path.read_bytes()).hexdigest()
                if path.is_file() and not path.is_symlink()
                else None
            )
            state[path.relative_to(root).as_posix()] = (
                info.st_mode, info.st_size, info.st_mtime_ns, info.st_ino, body,
            )
    return state


def _run_in_copy(copy: Path, tool: str, *args: str) -> subprocess.CompletedProcess[str]:
    env = {**os.environ, **DETERMINISM_PINS, "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run(
        [sys.executable, tool, *args], cwd=copy, env=env, capture_output=True, text=True, timeout=600
    )


_TOOL = "tools/errors/generate_error_artifacts.py"


def test_error_artifact_tool_help_changes_no_file(tmp_path):
    copy = _tracked_copy(tmp_path / "tree")
    before = _tree_state(copy)
    result = _run_in_copy(copy, _TOOL, "--help")
    assert result.returncode == 0
    assert result.stdout.startswith("usage:") and result.stderr == ""
    assert _tree_state(copy) == before


def test_error_artifact_tool_without_arguments_reproduces_the_tracked_outputs(tmp_path):
    copy = _tracked_copy(tmp_path / "tree")
    result = _run_in_copy(copy, _TOOL)
    assert result.returncode == 0, result.stderr
    changed = sorted(
        rel
        for rel, (_mode, _size, mtime, _ino, _body) in _tree_state(copy).items()
        if (copy / rel).is_file() and mtime != _FIXED_TIME_NS
    )
    assert "errors/token_map/token_map.json" in changed
    for rel in changed:
        assert (copy / rel).read_bytes() == (error_artifacts.ROOT / rel).read_bytes(), rel


def test_error_artifact_tool_main_parses_an_empty_argument_list(monkeypatch):
    calls: list[str] = []
    monkeypatch.setattr(error_artifacts, "write_parity_artifacts", lambda: calls.append("write"))
    monkeypatch.setattr(sys, "argv", ["pytest", "--unknown-pytest-option"])
    assert error_artifacts.main() == 0
    assert error_artifacts.main([]) == 0
    assert calls == ["write", "write"]
    with pytest.raises(SystemExit) as usage:
        error_artifacts.main(["--help"])
    assert usage.value.code == 0 and calls == ["write", "write"]
