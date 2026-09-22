import json
from pathlib import Path

import pytest

from engine.compat.error_tokens import ERROR_TOKEN_MAP, admission_token_for
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
