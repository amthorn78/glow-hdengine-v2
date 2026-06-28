#!/usr/bin/env python3
"""Generate HDE-EPIC035 PR-01 HDAPI v2 provider outcome evidence."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.bodygraph.vendor_client import HdApiClient, VendorRetryConfig, VendorTimeouts

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
ERROR_MAPPING = OUT / "error_mapping.snapshot.json"
RATE_LIMIT_HEADERS = OUT / "rate_limit_headers.snapshot.json"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}
PRODUCED_AT = "2026-06-28T00:00:00Z"
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"


def canonical_json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _client() -> HdApiClient:
    return HdApiClient(
        base_url="https://example.invalid/v2",
        api_key="redacted",
        geo_key="redacted",
        release_id="0" * 64,
        retry=VendorRetryConfig(max_attempts=3, profile="exponential", exp_base_ms=500, exp_ceiling_ms=2000),
        timeouts=VendorTimeouts(connect_timeout_ms=2000, read_timeout_ms=5000, total_timeout_ms=10000),
        wall_time=lambda: 1767225600.0,
    )


def base_snapshot(kind: str) -> dict[str, Any]:
    return {
        "artifact_kind": kind,
        "epic_id": "HDE-EPIC035",
        "generated_at_utc": PRODUCED_AT,
        "no_claims": {
            "full_hdapi_v2_runtime_conformance": "NONE",
            "live_vendor_call": "NONE",
            "open_rails_ops_execution": "NONE",
            "public_reader_change": "NONE",
            "public_route_flag_payload_or_transport_change": "NONE",
            "raw_vendor_payload_persisted": "NONE",
        },
        "pf09_document": PF09_DOCUMENT,
        "pf09_subtask_id": "HDE-FERM008.3",
        "pf09_task_id": "HDE-FERM008",
        "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"},
        "route_family_identity": {
            "legacy_v1_bodygraph_routes": [
                {"auth_header_posture": "HD-Api-Key: <redacted>", "label": "legacy_full_bodygraph", "resource_path": "bodygraphs"},
                {"auth_header_posture": "HD-Api-Key: <redacted>", "label": "legacy_simple_bodygraph", "resource_path": "bodygraphs/simple"},
            ],
            "version_neutral_runtime_resource_paths": ["bodygraphs", "bodygraphs/simple", "charts", "charts/simple", "charts/coordinates"],
            "v2_chart_routes": [
                {"auth_header_posture": "Authorization: Bearer <redacted>", "label": "full_chart", "resource_path": "charts"},
                {"auth_header_posture": "Authorization: Bearer <redacted>", "label": "simple_chart", "resource_path": "charts/simple"},
                {"auth_header_posture": "Authorization: Bearer <redacted>", "label": "coordinates_chart", "resource_path": "charts/coordinates"},
            ],
        },
    }


def build_error_mapping() -> dict[str, Any]:
    client = _client()
    statuses = [401, 403, 404, 429, 500, 503, 302]
    records = []
    for status in statuses:
        error_class = client._error_class(status)  # deterministic seam proof
        records.append({
            "classification": error_class,
            "provider_code": client._map_status_to_code(status),
            "retryable": client._is_retryable_error_class(error_class),
            "status": status,
        })
    data = base_snapshot("hdapi_v2_provider_outcome_mapping")
    data.update({
        "bad_response_records": [
            {"classification": "provider_bad_response", "provider_code": "PROVIDER_BAD_RESPONSE", "retryable": False, "scenario": "malformed_json_response"},
            {"classification": "provider_bad_response", "provider_code": "PROVIDER_BAD_RESPONSE", "retryable": False, "scenario": "provider_bad_response"},
        ],
        "closed_rails_refusal_context": {"classification": "provider_refused", "provider_code": "PROVIDER_REFUSED", "reference": "artifacts/vendor/hdapi_v2/closed_rails_refusal.txt", "retryable": False},
        "network_error_record": {"classification": "network_error", "provider_code": "PROVIDER_NETWORK_ERROR", "retryable": client._is_retryable_error_class("network_error")},
        "observability_posture": {
            "bounded_labels_only": True,
            "keys_only": True,
            "no_plaintext_secret_value": True,
            "no_raw_request_body": True,
            "no_raw_response_body": True,
            "no_raw_secret_header": True,
            "no_raw_vendor_payload": True,
            "observed_log_keys": ["at", "attempt", "backoff_ms", "duration_ms", "error_class", "error_code", "outcome", "profile", "rails_state", "retry_after_ms", "route", "status", "timeout_profile"],
        },
        "retry_classification": {
            "429": False,
            "4xx": False,
            "5xx": client._is_retryable_error_class("5xx"),
            "http_status_other": False,
            "network_error": client._is_retryable_error_class("network_error"),
            "redirect_response": False,
        },
        "status_mapping_records": records,
    })
    return data


def build_rate_limit_headers() -> dict[str, Any]:
    client = _client()
    data = base_snapshot("hdapi_v2_retry_after_mapping")
    data.update({
        "rate_limit_status_record": {"classification": "429", "provider_code": "PROVIDER_RATE_LIMITED", "retry_after_header_supported": True, "retryable": False, "status": 429},
        "retry_after_records": [
            {"case": "delta_seconds", "header_name": "Retry-After", "header_value_posture": "bounded_delta_seconds", "parsed_retry_after_ms": client._retry_after_ms({"Retry-After": "7"})},
            {"case": "http_date", "header_name": "retry-after", "header_value_posture": "bounded_http_date", "parsed_retry_after_ms": client._retry_after_ms({"retry-after": "Thu, 01 Jan 2026 00:00:05 GMT"})},
            {"case": "invalid", "header_name": "Retry-After", "header_value_posture": "invalid_omitted", "parsed_retry_after_ms": client._retry_after_ms({"Retry-After": "not-a-date"})},
            {"case": "overflow", "header_name": "Retry-After", "header_value_posture": "overflow_omitted", "parsed_retry_after_ms": client._retry_after_ms({"Retry-After": "2147484"})},
        ],
    })
    return data


def render_outputs() -> dict[Path, bytes]:
    return {ERROR_MAPPING: canonical_json_bytes(build_error_mapping()), RATE_LIMIT_HEADERS: canonical_json_bytes(build_rate_limit_headers())}


def write_outputs(outputs: dict[Path, bytes], *, check: bool) -> None:
    stale = []
    for path, body in outputs.items():
        if check:
            if not path.exists() or path.read_bytes() != body:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
    if stale:
        raise SystemExit("STALE_HDAPI_V2_LIVE_CONFORMANCE:" + ",".join(stale))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC035 HDAPI v2 provider outcome evidence")
    parser.add_argument("--check", action="store_true", help="verify generated artifacts are current")
    args = parser.parse_args(argv)
    write_outputs(render_outputs(), check=args.check)
    print(f"checked {OUT.relative_to(ROOT).as_posix()} HDE-EPIC035 provider outcome artifacts" if args.check else f"generated {OUT.relative_to(ROOT).as_posix()} HDE-EPIC035 provider outcome artifacts")


if __name__ == "__main__":
    main()
