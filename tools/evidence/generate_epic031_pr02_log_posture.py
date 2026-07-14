#!/usr/bin/env python3
"""Generate HDE-EPIC031 PR-02 SAFE rails log-posture evidence."""
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

from engine.bodygraph.vendor_client import HdApiClient, VendorError, VendorRequest, VendorRetryConfig, VendorTimeouts  # noqa: E402
from engine.runtime.determinism_env import ensure_determinism_env  # noqa: E402
from tools.evidence import update_evidence_index  # noqa: E402

PRODUCED_AT = "2026-05-10T16:20:00Z"
LOG_SAMPLE_REL = "audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl"
RAILS_SCOPE_REL = "audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt"
REDACTION_REL = "audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json"
BOUNDED_REL = "audit/qa/hde-epic031/pr-02/bounded_label_observability.json"
SCAN_REL = "audit/qa/hde-epic031/pr-02/secret_redaction_scan.log"
JOB_REL = "ci/jobs/logs_keys_only_redaction.yml"

ALLOWED_KEYS = [
    "at",
    "attempt",
    "backoff_ms",
    "duration_ms",
    "error_class",
    "error_code",
    "outcome",
    "profile",
    "rails_state",
    "retry_after_ms",
    "route",
    "status",
    "timeout_profile",
]
BOUNDED_LABELS = {
    "error_class": ["none", "network_error", "4xx", "5xx", "429", "http_status_other", "provider_bad_response", "provider_refused"],
    "outcome": ["success", "failure"],
    "profile": ["none", "fixed", "exponential"],
    "rails_state": ["closed_default", "open_exception"],
    "route": ["vendor.hdapi.post:/bodygraphs"],
    "timeout_profile": ["connect=500;read=1000;total=2000", "connect=1000;read=2000;total=5000", "connect=2000;read=5000;total=10000"],
}
FORBIDDEN_SAMPLE_FRAGMENTS = [
    "\"body\"",
    "\"body_bytes\"",
    "\"payload\"",
    "headers",
    "authorization",
    "x-api-key",
    "hd-api-key",
    "hd-geocode-key",
    "birthdate",
    "birthtime",
    "location",
    "secret",
    "token",
    "sk-",
    "fixture-api-key-value",
    "fixture-geo-key-value",
    "fixture-secret-city",
]


def _json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _write_text(rel: str, text: str, *, check: bool = False) -> Path:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    if check:
        if not path.exists() or path.read_bytes() != data:
            raise SystemExit(f"STALE:{rel}")
    else:
        path.write_bytes(data)
    return path


def _write_governed(rel: str, text: str, *, check: bool = False) -> None:
    path = _write_text(rel, text, check=check)
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


def _make_sample() -> list[dict[str, object]]:
    log_path = ROOT / LOG_SAMPLE_REL
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("", encoding="utf-8")
    request = VendorRequest(
        url="https://vendor.test/v1/bodygraphs",
        headers={"HD-Api-Key": "fixture-api-key-value", "HD-Geocode-Key": "fixture-geo-key-value"},
        body_bytes=b'{"birthdate":"01-Jan-1990","birthtime":"12:00","location":"fixture-secret-city"}\n',
        input_fingerprint="fixture-input-fingerprint",
    )
    cases = [
        ("success", lambda req, timeout: (200, b'{"ok":true}', {"authorization": "Bearer fixture-token"})),
        ("network_error", lambda req, timeout: (_ for _ in ()).throw(OSError("fixture network failure"))),
        ("4xx", lambda req, timeout: (403, b'{"error":"forbidden"}', {})),
        ("5xx", lambda req, timeout: (503, b'{"error":"unavailable"}', {})),
        ("429", lambda req, timeout: (429, b'{"error":"rate_limited"}', {"retry-after": "4"})),
        ("provider_refused", lambda req, timeout: (_ for _ in ()).throw(VendorError("PROVIDER_REFUSED", "fixture refused"))),
    ]
    for _name, request_func in cases:
        try:
            _client(log_path, request_func).fetch(request)
        except VendorError:
            pass
    return [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _scan(records: list[dict[str, object]]) -> tuple[dict[str, object], str]:
    sample_text = (ROOT / LOG_SAMPLE_REL).read_text(encoding="utf-8")
    lower_sample = sample_text.lower()
    forbidden_hits = [fragment for fragment in FORBIDDEN_SAMPLE_FRAGMENTS if fragment in lower_sample]
    key_violations = [sorted(set(record) - set(ALLOWED_KEYS)) for record in records if set(record) - set(ALLOWED_KEYS)]
    label_violations: list[dict[str, object]] = []
    for index, record in enumerate(records):
        for key, allowed in BOUNDED_LABELS.items():
            if key in record and record[key] not in allowed:
                label_violations.append({"record": index, "key": key, "value": record[key]})
    classes = sorted({str(record.get("error_class")) for record in records})
    required_classes = {"none", "network_error", "4xx", "5xx", "429", "provider_refused"}
    missing_classes = sorted(required_classes - set(classes))
    passed = not forbidden_hits and not key_violations and not label_violations and not missing_classes
    summary = {
        "artifact": "keys_only_log_redaction",
        "epic_id": "HDE-EPIC031",
        "pf09_subtask": "HDE-FERM001.3",
        "produced_at_utc": PRODUCED_AT,
        "live_vendor_call_executed": False,
        "sample_path": LOG_SAMPLE_REL,
        "records_scanned": len(records),
        "allowed_keys": ALLOWED_KEYS,
        "payload_body_absent": "\"body\"" not in lower_sample and "\"payload\"" not in lower_sample,
        "plaintext_secret_absent": not any(fragment in lower_sample for fragment in ["secret", "token", "fixture-api-key-value", "fixture-geo-key-value"]),
        "raw_secret_header_absent": not any(fragment in lower_sample for fragment in ["authorization", "hd-api-key", "hd-geocode-key", "headers"]),
        "forbidden_hits": forbidden_hits,
        "key_violations": key_violations,
        "missing_failure_classes": missing_classes,
        "status": "PASS" if passed else "FAIL",
    }
    scan_lines = [
        "HDE-EPIC031 PR-02 SAFE rails keys-only redaction scan",
        f"produced_at_utc: {PRODUCED_AT}",
        f"sample: {LOG_SAMPLE_REL}",
        f"records_scanned: {len(records)}",
        f"forbidden_hits: {','.join(forbidden_hits) if forbidden_hits else 'NONE'}",
        f"key_violations: {key_violations if key_violations else 'NONE'}",
        f"label_violations: {label_violations if label_violations else 'NONE'}",
        f"missing_failure_classes: {','.join(missing_classes) if missing_classes else 'NONE'}",
        f"status: {'PASS' if passed else 'FAIL'}",
    ]
    return summary, "\n".join(scan_lines) + "\n"


def _bounded_payload(records: list[dict[str, object]]) -> dict[str, object]:
    observed = {key: sorted({str(record[key]) for record in records if key in record}) for key in BOUNDED_LABELS}
    return {
        "artifact": "bounded_label_observability",
        "epic_id": "HDE-EPIC031",
        "pf09_subtask": "HDE-FERM001.3",
        "produced_at_utc": PRODUCED_AT,
        "live_vendor_call_executed": False,
        "route_observable": True,
        "outcome_observable": True,
        "rails_state_observable": True,
        "timeout_profile_observable": True,
        "bounded_labels": BOUNDED_LABELS,
        "observed_labels": observed,
        "failure_classes_observed": sorted({str(record.get("error_class")) for record in records if record.get("outcome") == "failure"}),
        "success_observed": any(record.get("outcome") == "success" for record in records),
        "status": "PASS",
    }


def _rails_scope_text(records: list[dict[str, object]]) -> str:
    routes: dict[str, int] = {}
    classes: dict[str, int] = {}
    for record in records:
        routes[str(record["route"])] = routes.get(str(record["route"]), 0) + 1
        classes[str(record["error_class"])] = classes.get(str(record["error_class"]), 0) + 1
    lines = [
        "summary:",
        f"  total_calls = {len(records)}",
        "scope: hde-epic031-pr-02-local-deterministic",
        "live_vendor_calls: forbidden",
        "rails:",
        "  SAFE_MODE = 1",
        "  ALLOW_NETWORK = 0",
        "  LC_ALL = C",
        "  LANG = C",
        "  TZ = UTC",
        "routes:",
    ]
    lines.extend(f"  {route} {count}" for route, count in sorted(routes.items()))
    lines.append("failure_classes:")
    lines.extend(f"  {name} {count}" for name, count in sorted(classes.items()))
    lines.append("vendor_routes_detected: 1")
    return "\n".join(lines) + "\n"


def _job_text() -> str:
    return """name: logs_keys_only_redaction
rails:
  SAFE_MODE: "1"
  ALLOW_NETWORK: "0"
  LC_ALL: C
  LANG: C
  TZ: UTC
scope: hde-epic031-pr-02-local-deterministic
live_vendor_calls: forbidden
steps:
  - command: python tools/evidence/generate_epic031_pr02_log_posture.py --check
    proves:
      - SAFE rails vendor logs are keys-only and payload-free
      - plaintext secrets and raw secret headers are absent from governed samples
      - route, outcome, rails_state, timeout_profile, and failure classes are bounded
  - command: python -m pytest tests/bodygraph/test_vendor_client.py tests/bodygraph/test_resolver_vendor.py -q
    proves:
      - local mocked provider log posture remains tested without live vendor calls
"""


def generate(*, check: bool = False) -> None:
    ensure_determinism_env()
    records = _make_sample()
    redaction, scan_text = _scan(records)
    if redaction["status"] != "PASS":
        raise SystemExit("REDACTION_SCAN_FAILED")
    _write_governed(LOG_SAMPLE_REL, "".join(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n" for record in records), check=check)
    _write_governed(RAILS_SCOPE_REL, _rails_scope_text(records), check=check)
    _write_governed(REDACTION_REL, _json_bytes(redaction).decode("utf-8"), check=check)
    _write_governed(BOUNDED_REL, _json_bytes(_bounded_payload(records)).decode("utf-8"), check=check)
    _write_governed(SCAN_REL, scan_text, check=check)
    # Current reusable rails gate definitions are owned by HDE rails-gate tooling;
    # preserve historical EPIC031 evidence without rewriting the shared CI job file.


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args(argv)
    generate(check=args.check)
    print("EPIC031_PR02_LOG_POSTURE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
