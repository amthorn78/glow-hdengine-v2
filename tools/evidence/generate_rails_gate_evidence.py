#!/usr/bin/env python3
"""Generate reusable current HDE SAFE-rails gate evidence."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Callable, Mapping
from urllib import request as urlrequest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.vendor_client import (  # noqa: E402
    HdApiClient,
    PINNED_BACKOFF_PROFILES,
    PINNED_MAX_ATTEMPTS,
    PINNED_TIMEOUT_PROFILES,
    VendorError,
    VendorRequest,
    VendorRetryConfig,
    VendorTimeouts,
)
from tools.evidence import update_evidence_index  # noqa: E402

PRODUCED_AT = "2026-07-13T00:00:00Z"
OPS_REFUSAL_REL = "artifacts/proofs/ops_refusal_proof.txt"
RETRY_AFTER_REL = "artifacts/vendor/retry_after_parse.log"
KEYS_ONLY_REL = "artifacts/bodygraph/keys_only.logs.sample"
ALLOWED_KEYS = {
    "at", "attempt", "backoff_ms", "duration_ms", "error_class", "error_code", "outcome",
    "profile", "rails_state", "retry_after_ms", "route", "status", "timeout_profile",
}
BOUNDED = {
    "error_class": {"none", "network_error", "4xx", "5xx", "429", "http_status_other", "provider_bad_response", "provider_refused"},
    "outcome": {"success", "failure"},
    "profile": {"none", "fixed", "exponential"},
    "rails_state": {"closed_default", "open_exception"},
    "route": {"vendor.hdapi.post:/bodygraphs"},
    "timeout_profile": {"connect=1000;read=2000;total=5000"},
}
FORBIDDEN = [
    "\"body\"", "body_bytes", "payload", "headers", "authorization", "x-api-key", "hd-api-key",
    "hd-geocode-key", "birthdate", "birthtime", "location", "secret", "token", "api-key", "geo-key",
    "fixture-api-key-value", "fixture-geo-key-value", "fixture-secret-city", "https://", "http://",
]


def _json_line(payload: object) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def _write_governed(rel: str, text: str, *, check: bool) -> None:
    data = text.encode("utf-8")
    path = ROOT / rel
    if check:
        if not path.exists() or path.read_bytes() != data:
            raise SystemExit(json.dumps({"status": "FAIL", "stale": rel}, sort_keys=True))
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel,
        sha256=update_evidence_index._sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=None,
        produced_at=PRODUCED_AT,
        default_produced_at=PRODUCED_AT,
        check=check,
        stat_mtime=stat.st_mtime,
    )


def _client(log_path: Path, request: Callable[[urlrequest.Request, float], tuple[int, bytes, Mapping[str, str]]]) -> HdApiClient:
    return HdApiClient(
        base_url="https://vendor.test/v1",
        api_key="fixture-api-key-value",
        geo_key="fixture-geo-key-value",
        release_id="0" * 64,
        retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
        timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        log_path=log_path,
        request=request,
        monotonic_ms=lambda: 0.0,
        wall_time=lambda: 1_700_000_000.0,
    )


def build_ops_refusal() -> str:
    req = urlrequest.Request("https://vendor.test/v1/bodygraphs", data=b"{}\n", method="POST")
    try:
        HdApiClient._default_request(req, 1.0)
    except VendorError as exc:
        if exc.code != "PROVIDER_REFUSED":
            raise SystemExit("unexpected refusal code")
    else:  # pragma: no cover
        raise SystemExit("closed rails did not refuse")
    body = {"code": "rails_closed", "error": "rails remain closed", "ok": False, "schema": "rails_closed"}
    return "cache-control: no-store\ncontent-type: application/json; charset=utf-8\nx-rails-mode: closed\n\n" + _json_line(body)


def build_retry_after() -> str:
    client = _client(ROOT / ".tmp-unused", lambda req, timeout: (200, b"{}", {}))
    cases = [
        ("delta_seconds", "4"),
        ("http_date_future", "Tue, 14 Nov 2023 23:13:20 GMT"),
        ("http_date_past", "Tue, 14 Nov 2023 21:13:20 GMT"),
        ("invalid", "not-a-date"),
        ("unsupported_fractional_delta", "1.5"),
        ("overflow_delta", "2147484"),
    ]
    rows = []
    for case, raw in cases:
        ms = client._retry_after_ms({"retry-after": raw})
        row = {"case": case, "input": raw, "retry_after_ms": ms, "status": "parsed" if ms is not None else "omitted"}
        if case.startswith("http_date"):
            row["now_epoch_seconds"] = 1700000000
        rows.append(row)
    return "".join(_json_line(row) for row in rows)


def build_keys_only() -> str:
    tmp = ROOT / ".rails_gate_keys_only.tmp"
    tmp.write_text("", encoding="utf-8")
    request = VendorRequest(
        url="https://vendor.test/v1/bodygraphs",
        headers={"HD-Api-Key": "fixture-api-key-value", "HD-Geocode-Key": "fixture-geo-key-value"},
        body_bytes=b'{"birthdate":"01-Jan-1990","birthtime":"12:00","location":"fixture-secret-city"}\n',
        input_fingerprint="fixture-input-fingerprint",
    )
    cases = [
        lambda req, timeout: (200, b'{"ok":true}', {"authorization": "Bearer fixture-token"}),
        lambda req, timeout: (_ for _ in ()).throw(OSError("fixture network failure")),
        lambda req, timeout: (403, b'{"error":"forbidden"}', {}),
        lambda req, timeout: (503, b'{"error":"unavailable"}', {}),
        lambda req, timeout: (429, b'{"error":"rate_limited"}', {"retry-after": "4"}),
        lambda req, timeout: (_ for _ in ()).throw(VendorError("PROVIDER_REFUSED", "fixture refused")),
    ]
    for func in cases:
        try:
            _client(tmp, func).fetch(request)
        except VendorError:
            pass
    text = tmp.read_text(encoding="utf-8")
    tmp.unlink(missing_ok=True)
    return text


def validate_outputs(outputs: dict[str, str]) -> None:
    for rel, text in outputs.items():
        if not text.endswith("\n") or "\r" in text:
            raise SystemExit(f"invalid line ending: {rel}")
        lower = text.lower()
        hits = [frag for frag in FORBIDDEN if frag in lower and rel == KEYS_ONLY_REL]
        if hits:
            raise SystemExit(json.dumps({"status": "FAIL", "forbidden": hits, "path": rel}, sort_keys=True))
        if rel == KEYS_ONLY_REL:
            records = [json.loads(line) for line in text.splitlines() if line.strip()]
            for record in records:
                extra = set(record) - ALLOWED_KEYS
                if extra:
                    raise SystemExit(f"unbounded log keys: {sorted(extra)}")
                for key, allowed in BOUNDED.items():
                    if key in record and record[key] not in allowed:
                        raise SystemExit(f"unbounded {key}: {record[key]}")
            classes = {r.get("error_class") for r in records}
            if not {"none", "network_error", "4xx", "5xx", "429", "provider_refused"}.issubset(classes):
                raise SystemExit("missing required failure classes")


def expected_outputs() -> dict[str, str]:
    outputs = {OPS_REFUSAL_REL: build_ops_refusal(), RETRY_AFTER_REL: build_retry_after(), KEYS_ONLY_REL: build_keys_only()}
    validate_outputs(outputs)
    return outputs


def generate(*, check: bool = False) -> None:
    outputs = expected_outputs()
    # complete validation occurred above; now write/check only.
    for rel, text in outputs.items():
        _write_governed(rel, text, check=check)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    generate(check=args.check)
    print("RAILS_GATE_EVIDENCE_OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
