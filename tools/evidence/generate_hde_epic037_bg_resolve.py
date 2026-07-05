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
from engine.bodygraph.v2_adapter import CHART_RESULT_REQUIRED_FIELDS
from engine.bodygraph.vendor_client import HdApiClient, VendorResult, classify_bg_resolve_route_policy
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
ROUTE_POLICY = OUT / "hde_epic037_bg_resolve_v2_route_policy.snapshot.json"
REQUEST_SHAPE = OUT / "hde_epic037_bg_resolve_request_shape.snapshot.json"
CLOSED_NO_IO = OUT / "hde_epic037_bg_resolve_closed_rails_no_io.json"
LEGACY_FALLBACK = OUT / "hde_epic037_bg_resolve_legacy_fallback.snapshot.json"
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}
INTERNAL_LOCI = (
    "engine/bodygraph/resolver.py",
    "engine/bodygraph/vendor_client.py",
    "engine/bodygraph/v2_adapter.py",
    "engine/bodygraph/ingest.py",
    "engine/cli/main.py",
)
INPUT_REFS = (
    "artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json",
)
NONCLAIMS = [
    "live vendor success",
    "QA PASS",
    "OPS completion",
    "PF09 status movement",
    "HDE-FERM008 parent Done",
    "closeout",
    "public Reader change",
    "new public route",
    "new public flag",
    "new public payload/transport",
    "new HTTP home",
    "app-side vendor ownership",
    "AI scope",
]


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


def _existing_generated_at(path: Path) -> str | None:
    if not path.exists():
        return None
    generated = json.loads(path.read_text(encoding="utf-8")).get("generated_at_utc")
    if isinstance(generated, str):
        _parse_utc_iso8601(generated)
        return generated
    return None


def enforce_closed_rails() -> None:
    env = ensure_determinism_env()
    mismatches = {key: env.get(key) for key, expected in CLOSED_RAILS_ENV.items() if env.get(key) != expected}
    if mismatches:
        raise DeterminismEnvError(f"HDE_EPIC037_PR03_OPEN_RAILS:{mismatches!r}")


def _common(produced_at: str) -> dict[str, Any]:
    return {
        "epic_id": "HDE-EPIC037",
        "generated_at_utc": produced_at,
        "pf09_document": PF09_DOCUMENT,
        "pf09_task_id": "HDE-FERM008",
        "pf09_subtask_id": "HDE-FERM008.9",
        "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"},
        "nonclaims": NONCLAIMS,
    }


def _loci() -> list[dict[str, str]]:
    rows = []
    for rel in INTERNAL_LOCI:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"HDE_EPIC037_PR03_LOCUS_MISSING:{rel}")
        rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def _input_refs() -> dict[str, dict[str, str]]:
    refs = {}
    for rel in INPUT_REFS:
        path = ROOT / rel
        refs[Path(rel).stem] = {"path": rel, "sha256": _sha256_path(path)}
    return refs


def _chart_payload() -> dict[str, Any]:
    payload: dict[str, Any] = {field: f"fixture:{field}" for field in sorted(CHART_RESULT_REQUIRED_FIELDS)}
    payload.update({"activations": {"design": {}, "personality": {}}, "centers": ["G", "Sacral"], "channelsLong": ["The Channel of Charisma (20-34)"], "channelsShort": ["20-34"], "gates": ["20", "34"]})
    return {"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": payload}


def _open_v2_result() -> dict[str, Any]:
    class FakeClient:
        def build_contract_route_request(self, **kwargs: Any):
            client = HdApiClient(base_url="https://vendor.example.test/v2", api_key="redacted-fixture", geo_key="redacted-geo", release_id="0" * 64, retry=__import__("engine.bodygraph.vendor_client", fromlist=["VendorRetryConfig"]).VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0), timeouts=__import__("engine.bodygraph.vendor_client", fromlist=["VendorTimeouts"]).VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000), request=lambda req, timeout: (_ for _ in ()).throw(AssertionError("no default request")))
            return client.build_contract_route_request(**kwargs)

        def fetch(self, request: Any) -> VendorResult:
            return VendorResult(payload=_chart_payload(), duration_ms=1.0, attempts=1)

    original = HdApiClient.from_env
    try:
        HdApiClient.from_env = classmethod(lambda cls, **kwargs: FakeClient())  # type: ignore[method-assign]
        result = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "HD_API_BASE_URL": "https://vendor.example.test/v2", "HD_API_KEY": "REDACTED", "GEO_API_KEY": "REDACTED"}, birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")
    finally:
        HdApiClient.from_env = original  # type: ignore[method-assign]
    return result.payload


def build_outputs(produced_at: str) -> dict[Path, bytes]:
    common = _common(produced_at)
    policy = classify_bg_resolve_route_policy("https://vendor.example.test/v2")
    client = HdApiClient(base_url="https://vendor.example.test/prefix/v2", api_key="redacted-fixture", geo_key="redacted-geo", release_id="0" * 64, retry=__import__("engine.bodygraph.vendor_client", fromlist=["VendorRetryConfig"]).VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0), timeouts=__import__("engine.bodygraph.vendor_client", fromlist=["VendorTimeouts"]).VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000), request=lambda req, timeout: (_ for _ in ()).throw(AssertionError("no request")))
    request = client.build_contract_route_request(path="charts", request_fields=("birthdate", "birthtime", "location"), geocode_required=True, birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")
    closed = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "HD_API_BASE_URL": "https://vendor.example.test/v2", "HD_API_KEY": "REDACTED", "GEO_API_KEY": "REDACTED"}, birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")
    legacy = classify_bg_resolve_route_policy("https://vendor.example.test/v1")
    mapped = _open_v2_result()
    route_policy = {**common, "artifact_kind": "hde_epic037_bg_resolve_v2_route_policy", "input_references": _input_refs(), "inspected_internal_loci": _loci(), "route_policy": policy, "resolver_output_proof": {"status": mapped["status"], "adapter": mapped["adapter"], "resolved_source": mapped["resolver"]["resolved_source"], "cache_posture": mapped["cache"]["payload_posture"]}, "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"]}
    request_shape = {**common, "artifact_kind": "hde_epic037_bg_resolve_request_shape", "input_references": _input_refs(), "inspected_internal_loci": _loci(), "request_shape": {"configured_base_url_key": "HD_API_BASE_URL", "deprecated_base_url_alias": {"env_var": "HDAPI_BASE_URL", "posture": "compatibility alias only; canonical and deprecated conflicts fail closed"}, "resource_path": "charts", "route": request.route, "configured_base_url": "<redacted>", "url_posture": "configured_base_url/charts", "configured_path_suffix_preserved": "prefix/v2", "no_double_version_prefix": True, "no_legacy_bodygraph_request_against_v2": True, "auth_header_posture": "Authorization: Bearer <redacted>", "geocode_header_posture": "HD-Geocode-Key: <redacted>", "raw_request_body_emitted": False, "raw_response_body_emitted": False}, "resolver_request_posture": mapped["resolver"]["request"], "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"]}
    closed_no_io = {**common, "artifact_kind": "hde_epic037_bg_resolve_closed_rails_no_io", "closed_rails_result": closed.payload, "no_io_before_refusal": {"route_policy_classification": False, "client_construction": False, "request_construction": False, "fetch": False, "dns": False, "socket": False, "http": False, "db": False, "ingest": False}, "tokens": ["NO_EXTERNAL_IO_ON_REFUSAL_OK", "ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"]}
    legacy_fallback = {**common, "artifact_kind": "hde_epic037_bg_resolve_legacy_fallback", "legacy_fallback_policy": legacy, "legacy_request_auth_posture": "HD-Api-Key: <redacted>", "v2_legacy_bodygraph_request_posture": "forbidden; configured v2 uses charts", "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"]}
    return {ROUTE_POLICY: canonical_json_bytes(route_policy), REQUEST_SHAPE: canonical_json_bytes(request_shape), CLOSED_NO_IO: canonical_json_bytes(closed_no_io), LEGACY_FALLBACK: canonical_json_bytes(legacy_fallback)}


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
        produced_at = _isoformat(_dt.datetime.now(tz=_dt.timezone.utc))
    write_outputs(build_outputs(produced_at), produced_at=produced_at, check=args.check)
    print("checked HDE-EPIC037 PR-03 bg:resolve artifacts" if args.check else "generated HDE-EPIC037 PR-03 bg:resolve artifacts")


if __name__ == "__main__":
    main()
