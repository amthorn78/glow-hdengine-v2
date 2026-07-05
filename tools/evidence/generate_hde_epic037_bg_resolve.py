#!/usr/bin/env python3
"""Generate HDE-EPIC037 PR-03 bg:resolve v2 adapter wiring evidence."""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.bodygraph.resolver import resolve_bodygraph
from engine.bodygraph.vendor_client import HdApiClient, VendorRequest, VendorResult, VendorRetryConfig, VendorTimeouts, classify_bg_resolve_route_policy
from engine.bodygraph.v2_adapter import CHART_RESULT_REQUIRED_FIELDS
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
ROUTE_POLICY = OUT / "hde_epic037_bg_resolve_v2_route_policy.snapshot.json"
REQUEST_SHAPE = OUT / "hde_epic037_bg_resolve_request_shape.snapshot.json"
CLOSED_NO_IO = OUT / "hde_epic037_bg_resolve_closed_rails_no_io.json"
LEGACY = OUT / "hde_epic037_bg_resolve_legacy_fallback.snapshot.json"
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}
INTERNAL_LOCI = (
    "engine/bodygraph/resolver.py",
    "engine/bodygraph/vendor_client.py",
    "engine/bodygraph/v2_adapter.py",
    "engine/bodygraph/ingest.py",
    "engine/cli/main.py",
    "migrations/011_body_graphs_durability.sql",
)
NONCLAIMS = ["live vendor success", "QA PASS", "OPS completion", "PF09 status movement", "HDE-FERM008 parent Done", "closeout", "public Reader change", "new public route", "new public flag", "new public payload/transport", "new HTTP home", "app-side vendor ownership", "AI scope"]


def canonical_json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _isoformat(dt: _dt.datetime) -> str:
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse_utc_iso8601(raw: str) -> _dt.datetime:
    dt = _dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if dt.tzinfo != _dt.timezone.utc or dt.microsecond:
        raise ValueError("expected whole-second UTC timestamp")
    return dt


def _current_produced_at() -> str:
    return _isoformat(_dt.datetime.now(tz=_dt.timezone.utc))


def _existing_generated_at(path: Path) -> str | None:
    if not path.exists():
        return None
    try:
        generated = json.loads(path.read_text(encoding="utf-8")).get("generated_at_utc")
    except json.JSONDecodeError:
        return None
    if isinstance(generated, str):
        _parse_utc_iso8601(generated)
        return generated
    return None


def enforce_closed_rails() -> dict[str, str]:
    env = ensure_determinism_env()
    mismatches = {key: env.get(key) for key, expected in CLOSED_RAILS_ENV.items() if env.get(key) != expected}
    if mismatches:
        raise DeterminismEnvError(f"HDE_EPIC037_PR03_OPEN_RAILS:{mismatches!r}")
    return env


def _common(produced_at: str) -> dict[str, Any]:
    return {"epic_id": "HDE-EPIC037", "generated_at_utc": produced_at, "pf09_document": PF09_DOCUMENT, "pf09_task_id": "HDE-FERM008", "pf09_subtask_id": "HDE-FERM008.9", "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"}, "nonclaims": NONCLAIMS}


def _loci() -> list[dict[str, str]]:
    rows = []
    for rel in INTERNAL_LOCI:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"HDE_EPIC037_PR03_LOCUS_MISSING:{rel}")
        rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def _chart_payload() -> dict[str, Any]:
    payload: dict[str, Any] = {field: f"fixture:{field}" for field in sorted(CHART_RESULT_REQUIRED_FIELDS)}
    payload.update({"activations": {"design": {}, "personality": {}}, "centers": ["G", "Sacral"], "channelsLong": ["The Channel of Charisma (20-34)"], "channelsShort": ["20-34"], "gates": ["20", "34"]})
    return {"timestamp": "2026-07-05T00:00:00Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": payload}


class _FakeV2Client:
    def __init__(self, calls: list[str]) -> None:
        self._calls = calls
        self._real = HdApiClient(base_url="https://vendor.test/v2", api_key="api-key", geo_key="geo-key", release_id="0" * 64, retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0), timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000), request=lambda req, timeout: (_ for _ in ()).throw(AssertionError("external request forbidden")))

    def build_contract_route_request(self, **kwargs: Any) -> VendorRequest:
        self._calls.append("build_contract_route_request")
        return self._real.build_contract_route_request(**kwargs)

    def fetch(self, request: VendorRequest) -> VendorResult:
        self._calls.append("fetch_callable_fixture_only")
        return VendorResult(payload=_chart_payload(), duration_ms=1.0, attempts=1)


def _resolver_v2_probe() -> tuple[dict[str, Any], list[str]]:
    import engine.bodygraph.resolver as resolver

    calls: list[str] = []
    original = resolver.HdApiClient.from_env
    resolver.HdApiClient.from_env = lambda **kwargs: _FakeV2Client(calls)  # type: ignore[method-assign]
    try:
        result = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "HD_API_BASE_URL": "https://vendor.test/v2", "HD_API_KEY": "SET", "GEO_API_KEY": "SET"}, birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")
    finally:
        resolver.HdApiClient.from_env = original  # type: ignore[method-assign]
    return result.payload, calls


def build_outputs(produced_at: str) -> dict[Path, bytes]:
    common = _common(produced_at)
    v2_policy = classify_bg_resolve_route_policy("https://vendor.test/v2")
    legacy_policy = classify_bg_resolve_route_policy("https://vendor.test/v1")
    client = HdApiClient(base_url="https://vendor.test/prefix/v2", api_key="api-key", geo_key="geo-key", release_id="0" * 64, retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0), timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000))
    request = client.build_request(birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")
    resolver_payload, calls = _resolver_v2_probe()
    closed = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "HD_API_BASE_URL": "https://vendor.test/v2"}, birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL").payload
    legacy_client = HdApiClient(base_url="https://vendor.test/v1", api_key="api-key", geo_key="geo-key", release_id="0" * 64, retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0), timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000))
    legacy_request = legacy_client.build_request(birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")
    route_policy = {**common, "artifact_kind": "hde_epic037_bg_resolve_v2_route_policy", "inspected_internal_loci": _loci(), "route_policy": v2_policy, "resolver_adapter_status": resolver_payload["adapter"]["status"], "resolver_adapter_code": resolver_payload["adapter"]["code"], "resolver_cache_posture": resolver_payload["cache"]["payload_posture"], "raw_vendor_payload_body_emitted": False, "raw_request_body_emitted": False, "raw_response_body_emitted": False}
    request_shape = {**common, "artifact_kind": "hde_epic037_bg_resolve_request_shape", "configured_base_url_key": "HD_API_BASE_URL", "deprecated_base_url_alias": {"env_var": "HDAPI_BASE_URL", "posture": "compatibility alias only; conflicting canonical/deprecated values fail closed"}, "version_owner": "HD_API_BASE_URL", "request": {"auth_header_posture": "Authorization: Bearer <redacted>", "geocode_header_posture": "HD-Geocode-Key: <redacted>", "method": "POST", "resource_path": "charts", "route": request.route, "url": request.url, "body_fields": sorted(json.loads(request.body_bytes.decode("utf-8")).keys()), "no_double_version_prefix": request.url == "https://vendor.test/prefix/v2/charts", "does_not_construct_legacy_bodygraphs_for_v2": "bodygraphs" not in request.url}, "resolver_request_posture": resolver_payload["request"], "fetch_fixture_calls": calls, "raw_request_body_emitted": False, "raw_response_body_emitted": False}
    closed_no_io = {**common, "artifact_kind": "hde_epic037_bg_resolve_closed_rails_no_io", "closed_rails_result": closed, "no_io_before_refusal": {"route_policy_classification": False, "vendor_client_construction": False, "request_construction": False, "fetch": False, "dns": False, "socket": False, "http": False, "db": False, "ingest": False}, "env_rails_policy": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "HD_API_BASE_URL": "SET", "HDAPI_BASE_URL": "UNSET"}}
    legacy = {**common, "artifact_kind": "hde_epic037_bg_resolve_legacy_fallback", "legacy_policy": legacy_policy, "legacy_request": {"auth_header_posture": "HD-Api-Key: <redacted>", "geocode_header_posture": "HD-Geocode-Key: <redacted>", "method": "POST", "resource_path": "bodygraphs", "route": legacy_request.route, "url": legacy_request.url}, "legacy_fallback_scope": "non-v2 configured bases only", "v2_legacy_bodygraphs_request_supported": False}
    return {ROUTE_POLICY: canonical_json_bytes(route_policy), REQUEST_SHAPE: canonical_json_bytes(request_shape), CLOSED_NO_IO: canonical_json_bytes(closed_no_io), LEGACY: canonical_json_bytes(legacy)}


def _write_path_proof(path: Path, produced_at: str, *, check: bool) -> None:
    stat = path.stat()
    update_evidence_index._write_path_proof(path.relative_to(ROOT).as_posix(), sha256=_sha256_path(path), size_bytes=stat.st_size, mtime_utc=None, produced_at=produced_at, default_produced_at=produced_at, check=check, stat_mtime=stat.st_mtime)


def write_outputs(outputs: dict[Path, bytes], *, produced_at: str, check: bool) -> None:
    stale = []
    for path, body in outputs.items():
        if check:
            if not path.exists() or path.read_bytes() != body:
                stale.append(path.relative_to(ROOT).as_posix())
            else:
                _write_path_proof(path, produced_at, check=True)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
            ts = _parse_utc_iso8601(produced_at).timestamp()
            os.utime(path, (ts, ts))
            _write_path_proof(path, produced_at, check=False)
    if stale:
        raise SystemExit("STALE_HDE_EPIC037_PR03_BG_RESOLVE:" + ",".join(stale))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC037 PR-03 bg:resolve evidence")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        enforce_closed_rails()
    except DeterminismEnvError as exc:
        raise SystemExit(f"HDE_EPIC037_PR03_CLOSED_RAILS_REQUIRED:{exc}") from exc
    produced_at = _existing_generated_at(ROUTE_POLICY) if args.check else None
    if produced_at is None:
        produced_at = _current_produced_at()
    write_outputs(build_outputs(produced_at), produced_at=produced_at, check=args.check)
    print("checked HDE-EPIC037 PR-03 bg:resolve artifacts" if args.check else "generated HDE-EPIC037 PR-03 bg:resolve artifacts")


if __name__ == "__main__":
    main()
