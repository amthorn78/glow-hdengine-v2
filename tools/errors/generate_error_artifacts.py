#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter import wsgi as adapter_wsgi
from engine.compat.error_tokens import ERROR_TOKEN_MAP
from engine.runtime.determinism_env import ensure_determinism_env

ERROR_SCHEMA_PATH = ROOT / "adapter/schemas/error_v1.schema.json"

try:
    import jsonschema  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    jsonschema = None


@dataclass
class ParityScenario:
    name: str
    token: str
    http_call: Callable[[Any], Any]
    cli_args: Callable[[Path], list[str]]
    stderr_expectation: str


def _cli_env() -> dict[str, str]:
    env = dict(os.environ)
    ensure_determinism_env(environ=env, apply=True)
    env.update({
        "PYTHONPATH": str(ROOT),
        "APP_ENV": env.get("APP_ENV", "dev"),
        "DB_FORCE_PG": "1",
        "HDE_FORCE_DB_UNAVAILABLE": "1",
    })
    return env


def _cli_args_invalid_json(tmpdir: Path) -> list[str]:
    bad = tmpdir / "bad.json"
    bad.write_text("{bad}\n", encoding="utf-8")
    return [sys.executable, "-m", "engine.cli", "showcompat", "--pair-file", str(bad)]


def _cli_args_invalid_viewer_prefs(tmpdir: Path) -> list[str]:
    pair = tmpdir / "pair.json"
    pair.write_text(
        json.dumps(
            {
                "left": {
                    "birthdate": "2000-01-01",
                    "birthtime": "00:00",
                    "location": "Moon",
                },
                "right": {
                    "birthdate": "2000-02-02",
                    "birthtime": "01:01",
                    "location": "Sun",
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )
    prefs = tmpdir / "prefs.json"
    prefs.write_text("{}\n", encoding="utf-8")
    return [
        sys.executable,
        "-m",
        "engine.cli",
        "showcompat",
        "--pair-file",
        str(pair),
        "--viewer-prefs-file",
        str(prefs),
    ]


def _cli_args_db_unavailable() -> list[str]:
    return [
        sys.executable,
        "-m",
        "engine.cli",
        "showcompat",
        "--source",
        "db",
        "--user-a",
        "db-user-a",
        "--user-b",
        "db-user-b",
    ]


def _cli_args_vendor_closed_rails() -> list[str]:
    return [
        sys.executable,
        "-m",
        "engine.cli",
        "showcompat",
        "--source",
        "vendor",
        "--birthdate-a",
        "2000-01-01",
        "--birthtime-a",
        "00:00",
        "--location-a",
        "Moon",
        "--birthdate-b",
        "2000-02-02",
        "--birthtime-b",
        "01:01",
        "--location-b",
        "Sun",
    ]


def _http_db_unavailable(client) -> object:
    return client.get("/ops/db/unavailable")


def _http_vendor_closed_rails(client) -> object:
    return client.post("/ops/rails/refusal")


SCENARIOS: tuple[ParityScenario, ...] = (
    ParityScenario(
        name="invalid_json",
        token="ERR_COMPAT_INVALID_JSON",
        http_call=lambda client: client.post(
            "/api/compat/v1",
            data=b"{bad",
            headers={"Content-Type": "application/json; charset=utf-8"},
        ),
        cli_args=lambda tmpdir: _cli_args_invalid_json(tmpdir),
        stderr_expectation="INVALID_JSON",
    ),
    ParityScenario(
        name="invalid_viewer_prefs",
        token="ERR_INVALID_VIEWER_PREFS",
        http_call=lambda client: client.post(
            "/api/compat/v1",
            json={
                "a": {"person_uid": "A"},
                "b": {"person_uid": "B"},
                "viewer_prefs": {"top_category": "not_a_category"},
            },
        ),
        cli_args=lambda tmpdir: _cli_args_invalid_viewer_prefs(tmpdir),
        stderr_expectation="INVALID_VIEWER_PREFS",
    ),
    ParityScenario(
        name="db_unavailable",
        token="ERR_WRITER_RAILS_CLOSED",
        http_call=_http_db_unavailable,
        cli_args=lambda tmpdir: _cli_args_db_unavailable(),
        stderr_expectation="DB_QUERY_FAILED",
    ),
    ParityScenario(
        name="vendor_attempt_closed_rails",
        token="ERR_WRITER_RAILS_CLOSED",
        http_call=_http_vendor_closed_rails,
        cli_args=lambda tmpdir: _cli_args_vendor_closed_rails(),
        stderr_expectation="PROVIDER_REFUSED",
    ),
)


def _minimal_validate(instance: Mapping[str, object], schema: Mapping[str, object]) -> None:
    required = set(schema.get("required", []))
    props = schema.get("properties", {}) if isinstance(schema.get("properties"), Mapping) else {}
    if schema.get("type") == "object":
        if not isinstance(instance, Mapping):
            raise AssertionError("error payload must be object")
    if not set(instance.keys()).issuperset(required):
        raise AssertionError("error payload missing required keys")
    if schema.get("additionalProperties") is False:
        for key in instance.keys():
            if key not in props:
                raise AssertionError(f"unexpected key: {key}")


def validate_error_payload(payload: Mapping[str, object]) -> None:
    schema = json.loads(ERROR_SCHEMA_PATH.read_text(encoding="utf-8"))
    if jsonschema:
        jsonschema.validate(instance=payload, schema=schema)  # type: ignore[attr-defined]
        return
    _minimal_validate(payload, schema)


def capture_http(scenario: ParityScenario) -> dict[str, object]:
    client = adapter_wsgi.app.test_client()
    resp = scenario.http_call(client)
    body = json.loads(resp.data.decode("utf-8"))
    validate_error_payload(body)
    code = body.get("code")
    if code not in ERROR_TOKEN_MAP:
        raise AssertionError(f"unknown error token: {code}")
    return {
        "status": resp.status_code,
        "headers": {k.lower(): v for k, v in resp.headers.items() if k.lower() in {"cache-control", "content-type"}},
        "body": body,
    }


def capture_cli(scenario: ParityScenario) -> dict[str, object]:
    with tempfile.TemporaryDirectory() as td:
        args = scenario.cli_args(Path(td))
        proc = subprocess.run(
            args,
            cwd=ROOT,
            capture_output=True,
            text=True,
            env=_cli_env(),
        )
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout.rstrip("\n"),
        "stderr": proc.stderr.rstrip("\n"),
    }


def render_token_map() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for code, meta in sorted(ERROR_TOKEN_MAP.items()):
        records.append(
            {
                "code": code,
                "message": meta.get("message", ""),
                "aliases": sorted(meta.get("aliases", ())),
            }
        )
    return records


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_cli_text(path: Path, payload: Mapping[str, object]) -> None:
    lines = [
        f"returncode: {payload['returncode']}",
        f"stdout: {payload['stdout'].rstrip()}" if payload.get("stdout") else "stdout:",
        "stderr:",
        payload.get("stderr", "").rstrip(),
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def generate_schema_logs(results: list[tuple[ParityScenario, dict[str, object]]]) -> None:
    base = ROOT / "errors/schema_check"
    base.mkdir(parents=True, exist_ok=True)
    for scenario, http_result in results:
        body = http_result["body"]
        log_lines = [
            f"scenario: {scenario.name}",
            f"status: {http_result['status']}",
            f"code: {body.get('code')}",
            "schema: ok",
            "",
        ]
        (base / f"error_envelope_{scenario.name}.log").write_text("\n".join(log_lines), encoding="utf-8")


def write_parity_artifacts() -> None:
    ensure_determinism_env(apply=True)
    parity_dir = ROOT / "parity"
    parity_dir.mkdir(parents=True, exist_ok=True)

    http_results: list[tuple[ParityScenario, dict[str, object]]] = []
    cli_results: list[tuple[ParityScenario, dict[str, object]]] = []

    for scenario in SCENARIOS:
        http_result = capture_http(scenario)
        http_results.append((scenario, http_result))
        cli_result = capture_cli(scenario)
        cli_results.append((scenario, cli_result))

        _write_json(parity_dir / f"errors_reader_cli.{scenario.name}.http.json", http_result)
        _write_cli_text(parity_dir / f"errors_reader_cli.{scenario.name}.cli.txt", cli_result)

    generate_schema_logs(http_results)
    _write_json(ROOT / "errors/token_map/token_map.json", render_token_map())

    scenario_list = ", ".join(s.name for s in SCENARIOS)
    readme = (
        "Error parity artifacts between HTTP Reader/Compat endpoints and CLI error handling.\n"
        f"Scenarios: {scenario_list}.\n"
        "Artifacts include HTTP error envelopes, CLI stderr snapshots, schema validation logs, and token map snapshot.\n"
    )
    (parity_dir / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    write_parity_artifacts()
