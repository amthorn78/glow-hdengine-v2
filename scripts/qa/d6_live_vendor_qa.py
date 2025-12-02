#!/usr/bin/env python3
"""Open-rails Live Vendor QA harness for EPIC019 D6.

- Runs vendor BodyGraph resolve against HDAPI under open rails.
- Captures happy-path and failure classifications per PF19.
- Writes governed evidence under audit/qa/hde-epic019/d6-vendor-live-qa/.
"""
from __future__ import annotations

import json
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = REPO_ROOT / "audit" / "qa" / "hde-epic019" / "d6-vendor-live-qa"
LOG_HAPPY = AUDIT_DIR / "happy_path.jsonl"
LOG_FAIL_VENDOR = AUDIT_DIR / "fail_vendor.jsonl"
LOG_FAIL_TOOLING = AUDIT_DIR / "fail_tooling.jsonl"
RAILS_SNAPSHOT = AUDIT_DIR / "rails_snapshot.json"
ENV_KEYS = ["SAFE_MODE", "ALLOW_NETWORK", "LC_ALL", "LANG", "TZ"]
REQUIRED_VENDOR_KEYS = ["HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY"]
PAYLOAD = {
    "birthdate": "03-Jan-1980",
    "birthtime": "09:30",
    "location": "Paris, FR",
}
PF_CANON_REFS = [
    "PF04 — HDE-Governance",
    "PF05 — HDE-CLI-API-Vendor-Ref",
    "PF07 — Glow Infrastructure",
    "PF19 — Glow QA Guide",
]


class HarnessError(RuntimeError):
    """Raised for hard failures that should exit the harness."""


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _set_open_rails() -> dict[str, str]:
    env = os.environ
    env.setdefault("ALLOW_NETWORK", "1")
    env.setdefault("SAFE_MODE", "0")
    env.setdefault("LC_ALL", "C")
    env.setdefault("LANG", "C")
    env.setdefault("TZ", "UTC")
    return {key: env.get(key, "<unset>") for key in ENV_KEYS}


def _redacted_url(url: str) -> str:
    parsed = urlsplit(url)
    if not parsed.netloc:
        return url
    return parsed.scheme + "://" + parsed.netloc


def _require_vendor_env() -> dict[str, str]:
    env = {}
    missing = []
    for key in REQUIRED_VENDOR_KEYS:
        value = (os.environ.get(key) or "").strip()
        if not value:
            missing.append(key)
        env[key] = value
    if missing:
        raise HarnessError(f"Missing required vendor env: {', '.join(missing)}")
    return env


def _log_record(path: Path, record: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def _build_request(base_url: str, api_key: str, geo_key: str) -> Request:
    url = base_url.rstrip("/") + "/bodygraphs"
    headers = {
        "HD-Api-Key": api_key,
        "HD-Geocode-Key": geo_key,
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
    }
    body = json.dumps(PAYLOAD, sort_keys=True).encode("utf-8")
    return Request(url, data=body, headers=headers, method="POST")


@dataclass
class ScenarioResult:
    name: str
    result: str
    status: int | None


def _classify(status: int | None, *, parse_error: bool) -> str:
    if status is None:
        return "FAIL_TOOLING"
    if 200 <= status < 300 and not parse_error:
        return "OK"
    if parse_error:
        return "FAIL_BEHAVIOR"
    if status >= 500:
        return "FAIL_VENDOR"
    if status >= 400:
        return "FAIL_VENDOR"
    return "FAIL_BEHAVIOR"


def _summarize_response(status: int | None, body: bytes | None) -> dict[str, Any]:
    summary: dict[str, Any] = {"status": status}
    if body:
        try:
            parsed = json.loads(body.decode("utf-8"))
            summary["body_keys"] = sorted(parsed.keys()) if isinstance(parsed, Mapping) else []
            summary["body_excerpt"] = parsed if isinstance(parsed, Mapping) else {"raw": parsed}
            return summary
        except Exception as exc:  # noqa: BLE001 - safe logging only
            summary["body_excerpt"] = {"decode_error": str(exc)}
            summary["body_keys"] = []
            summary["parse_error"] = True
            return summary
    summary["body_keys"] = []
    return summary


def _run_http(request: Request) -> tuple[int | None, bytes | None]:
    try:
        with urlopen(request, timeout=10) as resp:  # nosec - governed open rails
            status = resp.getcode()
            body = resp.read()
            return status, body
    except HTTPError as err:
        return err.code, err.read()
    except URLError:
        return None, None
    except Exception:
        return None, None


def _run_scenario(
    *,
    name: str,
    request: Request,
    rails: dict[str, str],
    log_path: Path,
    expect_headers: list[str],
    vendor_host: str,
    override_result: str | None = None,
) -> ScenarioResult:
    record: dict[str, Any] = {
        "timestamp_utc": _iso_now(),
        "scenario": name,
        "rails": rails,
        "vendor_host": vendor_host,
        "request": {
            "method": request.get_method(),
            "url": _redacted_url(request.full_url),
            "payload_keys": sorted(PAYLOAD.keys()),
            "headers_present": sorted(expect_headers),
        },
    }
    start = time.monotonic()
    status, body = _run_http(request)
    duration_ms = round((time.monotonic() - start) * 1000.0, 2)
    summary = _summarize_response(status, body)
    summary["duration_ms"] = duration_ms
    parse_error = bool(summary.get("parse_error")) if status is not None and 200 <= status < 300 else False
    result = override_result or _classify(status, parse_error=parse_error)
    record["response"] = summary
    record["result"] = result
    _log_record(log_path, record)
    return ScenarioResult(name=name, result=result, status=status)


def _write_rails_snapshot(rails: Mapping[str, str], vendor_host: str) -> None:
    snapshot = {
        "schema": "epic019-d6-vendor-live-qa",
        "rails": rails,
        "vendor_host": vendor_host,
        "surface": "engine.cli vendor HTTP POST /bodygraphs",
        "payload_keys": sorted(PAYLOAD.keys()),
        "pf_canon_refs": PF_CANON_REFS,
        "notes": "Open-rails vendor QA per PF04/PF19 with classification log",
    }
    RAILS_SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    RAILS_SNAPSHOT.write_text(json.dumps(snapshot, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    rails = _set_open_rails()
    try:
        vendor_env = _require_vendor_env()
    except HarnessError as exc:
        error_record = {
            "timestamp_utc": _iso_now(),
            "scenario": "preflight",
            "result": "FAIL_TOOLING",
            "error": str(exc),
            "rails": rails,
        }
        _log_record(LOG_FAIL_TOOLING, error_record)
        print(str(exc), file=sys.stderr)
        return 1

    vendor_host = urlsplit(vendor_env["HDAPI_BASE_URL"]).netloc or vendor_env["HDAPI_BASE_URL"]
    _write_rails_snapshot(rails, vendor_host)

    # Reset logs to avoid mixing runs
    for path in (LOG_HAPPY, LOG_FAIL_VENDOR, LOG_FAIL_TOOLING):
        if path.exists():
            path.unlink()

    happy_req = _build_request(
        vendor_env["HDAPI_BASE_URL"], vendor_env["HD_API_KEY"], vendor_env["GEO_API_KEY"]
    )
    happy = _run_scenario(
        name="happy_path",
        request=happy_req,
        rails=rails,
        log_path=LOG_HAPPY,
        expect_headers=["HD-Api-Key", "HD-Geocode-Key", "Accept", "Content-Type"],
        vendor_host=vendor_host,
    )

    vendor_req = _build_request(vendor_env["HDAPI_BASE_URL"], "invalid-key", "invalid-geo")
    fail_vendor = _run_scenario(
        name="invalid_credentials",
        request=vendor_req,
        rails=rails,
        log_path=LOG_FAIL_VENDOR,
        expect_headers=["HD-Api-Key", "HD-Geocode-Key", "Accept", "Content-Type"],
        vendor_host=vendor_host,
    )

    bad_req = _build_request("https://invalid.invalid/v1", vendor_env["HD_API_KEY"], vendor_env["GEO_API_KEY"])
    fail_tooling = _run_scenario(
        name="bad_base_url",
        request=bad_req,
        rails=rails,
        log_path=LOG_FAIL_TOOLING,
        expect_headers=["HD-Api-Key", "HD-Geocode-Key", "Accept", "Content-Type"],
        vendor_host="invalid.invalid",
        override_result="FAIL_TOOLING",
    )

    results = [happy, fail_vendor, fail_tooling]
    ok_found = any(res.result == "OK" for res in results)
    failure_logged = any(res.result != "OK" for res in results)

    if not ok_found:
        print("No happy-path OK result recorded", file=sys.stderr)
        return 1
    if not failure_logged:
        print("No failure classification recorded", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except HarnessError as exc:  # pragma: no cover - defensive
        print(f"d6_live_vendor_qa: {exc}", file=sys.stderr)
        raise SystemExit(1)
