"""Secret-safe HDE-EPIC034 OPS-02 open-rails smoke procedure.

This file is remediation evidence for the original placeholder command record.
It documents a concrete repo-resident procedure for the bounded
HumanDesignAPI v2 `charts/coordinates` smoke. Running it performs one live
vendor call only when the operator has deliberately set open rails and
credential presence. It writes only redacted request/response-shape evidence;
it never persists raw credentials or full vendor payload bodies.
"""

from __future__ import annotations

import json
import os
import sys
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

from engine.bodygraph.vendor_client import (
    HdApiClient,
    VendorError,
    VendorRetryConfig,
    VendorTimeouts,
)

OUT_DIR = Path("audit/ops/hde-epic034/ops-02")
ROUTE_PATH = "charts/coordinates"
REQUEST_FIELDS = ("birthdate", "birthtime", "lat", "lng")

# Synthetic non-PII sample from repo-governed EPIC034 v2 route evidence.
SAMPLE_INPUT = {
    "birthdate": "1990-01-15",
    "birthtime": "14:30",
    "lat": 52.3676,
    "lng": 4.9041,
}

CHECKSUM_PATHS = (
    "audit/ops/hde-epic034/ops-02/commands.txt",
    "audit/ops/hde-epic034/ops-02/env_presence_redacted.json",
    "audit/ops/hde-epic034/ops-02/exit_codes.txt",
    "audit/ops/hde-epic034/ops-02/ops02_open_rails_smoke_procedure.py",
    "audit/ops/hde-epic034/ops-02/request_summary.json",
    "audit/ops/hde-epic034/ops-02/result_summary.json",
    "audit/ops/hde-epic034/ops-02/stderr.log",
    "audit/ops/hde-epic034/ops-02/stdout.log",
)


def _json_dumps(payload: Mapping[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.write_text(_json_dumps(payload), encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def _presence_env() -> dict[str, str | bool]:
    env = os.environ
    return {
        "ALLOW_NETWORK": env.get("ALLOW_NETWORK", ""),
        "APP_ENV": env.get("APP_ENV", ""),
        "GEO_API_KEY": "SET" if env.get("GEO_API_KEY") else "UNSET",
        "HDAPI_BASE_URL": "SET" if env.get("HDAPI_BASE_URL") else "UNSET",
        "HD_API_BASE_URL": "SET" if env.get("HD_API_BASE_URL") else "UNSET",
        "HD_API_BASE_URL_expected_v2": True,
        "HD_API_KEY": "SET" if env.get("HD_API_KEY") else "UNSET",
        "LANG": env.get("LANG", ""),
        "LC_ALL": env.get("LC_ALL", ""),
        "SAFE_MODE": env.get("SAFE_MODE", ""),
        "TZ": env.get("TZ", ""),
    }


def _response_shape(payload: Mapping[str, Any]) -> dict[str, Any]:
    data = payload.get("data")
    return {
        "data_kind": type(data).__name__,
        "errorCode_present": "errorCode" in payload,
        "success": bool(payload.get("success")),
        "top_level_keys": sorted(str(key) for key in payload.keys()),
        "type": payload.get("type"),
    }


def _write_checksums() -> None:
    lines = []
    for rel in CHECKSUM_PATHS:
        path = Path(rel)
        digest = sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {rel}")
    _write_text(OUT_DIR / "files_sha256.txt", "\n".join(lines))


def _write_blocked(reason: str, *, vendor_attempted: bool = False) -> int:
    _write_json(OUT_DIR / "env_presence_redacted.json", _presence_env())
    stdout = {"status": "TOOLING_BLOCKED", "vendor_attempted": vendor_attempted}
    stderr = {"reason": reason}
    _write_json(OUT_DIR / "stdout.log", stdout)
    _write_json(OUT_DIR / "result_summary.json", {
        "classification": "TOOLING_BLOCKED",
        "epic_id": "HDE-EPIC034",
        "exit_code": 2,
        "full_v2_conformance_claim": False,
        "full_vendor_payload_persisted": False,
        "geocode_used": False,
        "hde_ferm008_3_4_5_completion_claim": False,
        "hde_ferm008_parent_completion_claim": False,
        "legacy_hd_api_key_used_for_v2": False,
        "live_v2_success_claim": False,
        "ops_task": "OPS-02",
        "pf09_subtask_id": "HDE-FERM008.2",
        "raw_secret_persisted": False,
        "vendor_attempted": vendor_attempted,
    })
    _write_json(OUT_DIR / "request_summary.json", {
        "epic_id": "HDE-EPIC034",
        "method": "POST",
        "ops_task": "OPS-02",
        "pf09_subtask_id": "HDE-FERM008.2",
        "resource_path": ROUTE_PATH,
        "status": "not_attempted",
    })
    _write_text(OUT_DIR / "stderr.log", _json_dumps(stderr).rstrip("\n"))
    _write_text(OUT_DIR / "exit_codes.txt", "ops02_wrapper=2")
    _write_checksums()
    sys.stdout.write(_json_dumps(stdout))
    sys.stderr.write(_json_dumps(stderr))
    return 2


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if os.environ.get("SAFE_MODE") != "0" or os.environ.get("ALLOW_NETWORK") != "1":
        return _write_blocked("open rails not enabled")

    _write_json(OUT_DIR / "env_presence_redacted.json", _presence_env())
    try:
        client = HdApiClient.from_env(
            retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
            timeouts=VendorTimeouts(connect_timeout_ms=2000, read_timeout_ms=5000, total_timeout_ms=10000),
            release_id="0" * 64,
        )
        request = client.build_contract_route_request(
            path=ROUTE_PATH,
            request_fields=REQUEST_FIELDS,
            geocode_required=False,
            **SAMPLE_INPUT,
        )
    except VendorError as exc:
        return _write_blocked(exc.code)

    request_summary = {
        "auth_header_posture": "Authorization: Bearer <redacted>",
        "authorization_header_shape": "Authorization: Bearer <redacted>",
        "body_sha256": request.input_fingerprint,
        "configured_base_url_key": "HD_API_BASE_URL",
        "endpoint_path_posture": "/v2/charts/coordinates via HD_API_BASE_URL plus version-neutral resource path",
        "epic_id": "HDE-EPIC034",
        "geocode_key_requirement": "not needed",
        "hd_api_key_header_present": False,
        "hd_geocode_key_header_present": False,
        "header_names": sorted(request.headers.keys()),
        "input_fingerprint": request.input_fingerprint,
        "input_tuple_posture": "synthetic non-PII coordinates tuple; full request body not persisted",
        "legacy_v2_auth_header_posture": "HD-Api-Key not used for v2 chart routes",
        "method": "POST",
        "ops_task": "OPS-02",
        "pf09_subtask_id": "HDE-FERM008.2",
        "rails_required": {"ALLOW_NETWORK": "1", "SAFE_MODE": "0"},
        "request_fields": list(REQUEST_FIELDS),
        "request_url_posture": "redacted base URL; version-neutral resource path joined by HdApiClient",
        "resource_path": ROUTE_PATH,
    }
    _write_json(OUT_DIR / "request_summary.json", request_summary)

    try:
        result = client.fetch(request)
    except VendorError as exc:
        _write_text(OUT_DIR / "stderr.log", _json_dumps({"code": exc.code}).rstrip("\n"))
        _write_text(OUT_DIR / "exit_codes.txt", "ops02_wrapper=1")
        _write_json(OUT_DIR / "stdout.log", {"status": "FAIL", "vendor_attempted": True})
        _write_json(OUT_DIR / "result_summary.json", {
            "classification": "FAIL",
            "epic_id": "HDE-EPIC034",
            "exit_code": 1,
            "full_v2_conformance_claim": False,
            "full_vendor_payload_persisted": False,
            "geocode_used": False,
            "hde_ferm008_3_4_5_completion_claim": False,
            "hde_ferm008_parent_completion_claim": False,
            "legacy_hd_api_key_used_for_v2": False,
            "live_v2_success_claim": False,
            "ops_task": "OPS-02",
            "pf09_subtask_id": "HDE-FERM008.2",
            "raw_secret_persisted": False,
            "v2_auth_posture": "Authorization: Bearer <redacted>",
            "vendor_attempted": True,
        })
        _write_checksums()
        return 1

    stdout = {
        "attempts": result.attempts,
        "duration_ms_rounded": round(result.duration_ms, 3),
        "response_shape": _response_shape(result.payload),
        "status": "PASS",
        "vendor_attempted": True,
    }
    _write_json(OUT_DIR / "stdout.log", stdout)
    _write_text(OUT_DIR / "stderr.log", "")
    _write_text(OUT_DIR / "exit_codes.txt", "ops02_wrapper=0")
    _write_json(OUT_DIR / "result_summary.json", {
        "classification": "PASS",
        "epic_id": "HDE-EPIC034",
        "exit_code": 0,
        "follow_up": "bind OPS-02 evidence in PR-06 without overclaiming full v2 conformance",
        "full_v2_conformance_claim": False,
        "full_vendor_payload_persisted": False,
        "geocode_used": False,
        "hde_ferm008_3_4_5_completion_claim": False,
        "hde_ferm008_parent_completion_claim": False,
        "http_status_present": False,
        "legacy_hd_api_key_used_for_v2": False,
        "live_v2_success_claim": True,
        "ops_task": "OPS-02",
        "pf09_subtask_id": "HDE-FERM008.2",
        "raw_secret_persisted": False,
        "v2_auth_posture": "Authorization: Bearer <redacted>",
        "vendor_attempted": True,
    })
    _write_checksums()
    sys.stdout.write(_json_dumps(stdout))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
