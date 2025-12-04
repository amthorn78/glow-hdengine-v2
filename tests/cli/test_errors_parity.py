import json
from pathlib import Path

import pytest

from engine.compat.error_tokens import ERROR_TOKEN_MAP
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


@pytest.mark.parametrize("scenario", SCENARIOS)
def test_http_and_cli_parity(monkeypatch, scenario):
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


def test_token_map_snapshot_matches_canonical():
    snapshot = json.loads(Path("errors/token_map/token_map.json").read_text(encoding="utf-8"))
    assert snapshot == render_token_map()
    for record in snapshot:
        assert record["code"] in ERROR_TOKEN_MAP
