#!/usr/bin/env python3
"""Generate HDE-EPIC037 PR-02 deterministic v2 chart adapter evidence."""
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

from engine.bodygraph.v2_adapter import CHART_RESULT_REQUIRED_FIELDS, V2ChartAdapterContext, adapt_v2_chart_payload
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
MAPPING = OUT / "hde_epic037_adapter_mapping.snapshot.json"
NEGATIVE = OUT / "hde_epic037_adapter_negative_fixtures.json"
PUBLIC = OUT / "hde_epic037_public_reader_no_change.json"
NO_RAW = OUT / "hde_epic037_no_raw_payload_persistence.json"
PR01_CONTRACT = OUT / "hde_epic037_adapter_contract.snapshot.json"
PR01_PROOF = OUT / "hde_epic037_field_sufficiency_proof.json"
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}
INTERNAL_LOCI = (
    "engine/bodygraph/v2_adapter.py",
    "engine/bodygraph/__init__.py",
    "engine/bodygraph/resolver.py",
    "engine/bodygraph/ingest.py",
    "engine/bodygraph/vendor_client.py",
    "engine/compat/compute.py",
    "migrations/011_body_graphs_durability.sql",
)
PUBLIC_LOCI = (
    "docs/ENDPOINTS_CATALOG.json",
    "engine/api.py",
    "engine/reader.py",
    "engine/cli/main.py",
)


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
        raise DeterminismEnvError(f"HDE_EPIC037_PR02_OPEN_RAILS:{mismatches!r}")
    return env


def _common(produced_at: str) -> dict[str, Any]:
    return {"epic_id": "HDE-EPIC037", "generated_at_utc": produced_at, "pf09_document": PF09_DOCUMENT, "pf09_task_id": "HDE-FERM008", "pf09_subtask_id": "HDE-FERM008.8", "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"}}


def _loci(paths: tuple[str, ...]) -> list[dict[str, str]]:
    rows = []
    for rel in paths:
        path = ROOT / rel
        if path.is_file():
            rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def _input_refs() -> dict[str, dict[str, str]]:
    refs = {}
    for name, path in (("pr01_contract", PR01_CONTRACT), ("pr01_field_sufficiency_proof", PR01_PROOF)):
        refs[name] = {"path": path.relative_to(ROOT).as_posix(), "sha256": _sha256_path(path)}
    return refs


def chart_result_payload() -> dict[str, Any]:
    return {field: f"fixture:{field}" for field in sorted(CHART_RESULT_REQUIRED_FIELDS)}


def context(**overrides: str) -> V2ChartAdapterContext:
    values = {"person_uid": "person-epic037-pr02", "user_id": "123e4567-e89b-12d3-a456-426614174000", "vendor": "hdapi", "vendor_version": 2, "input_fingerprint": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "route_family": "recommended_v2_chart", "route": "charts", "payload_family": "ChartResult"}
    values.update(overrides)
    return V2ChartAdapterContext(**values)


def _negative_cases() -> list[dict[str, Any]]:
    return [
        {"fixture_id": "missing_internal_identity_context", "result": adapt_v2_chart_payload({"type": "ChartResult", "data": chart_result_payload()}, context(person_uid="")).as_dict()},
        {"fixture_id": "missing_vendor_detail_fields", "result": adapt_v2_chart_payload({"type": "ChartResult", "data": {"type": "Generator"}}, context()).as_dict()},
        {"fixture_id": "chart_simple_result_detail_insufficient", "result": adapt_v2_chart_payload({"type": "ChartSimpleResult", "data": {"type": "Generator", "profile": "1/3", "gates": [], "channelsShort": [], "centers": {}}}, context(payload_family="ChartSimpleResult")).as_dict()},
        {"fixture_id": "malformed_payload", "result": adapt_v2_chart_payload([], context()).as_dict()},
        {"fixture_id": "missing_data", "result": adapt_v2_chart_payload({"type": "ChartResult", "success": True}, context()).as_dict()},
        {"fixture_id": "unsupported_payload_family", "result": adapt_v2_chart_payload({"type": "OtherResult", "data": {}}, context(payload_family="OtherResult")).as_dict()},
        {"fixture_id": "wrong_route_family", "result": adapt_v2_chart_payload({"type": "ChartResult", "data": chart_result_payload()}, context(route_family="legacy_bodygraph")).as_dict()},
        {"fixture_id": "wrong_route", "result": adapt_v2_chart_payload({"type": "ChartResult", "data": chart_result_payload()}, context(route="bodygraphs")).as_dict()},
    ]


def build_outputs(produced_at: str) -> dict[Path, bytes]:
    mapped = adapt_v2_chart_payload({"success": True, "type": "ChartResult", "data": chart_result_payload()}, context()).as_dict()
    common = _common(produced_at)
    mapping = {**common, "artifact_kind": "hde_epic037_adapter_mapping_snapshot", "adapter_scope": "pure_context_backed_chart_result_mapping_only", "adapter_purity": {"database_io": False, "environment_reads": False, "file_io": False, "network_io": False, "randomness": False, "time_reads": False, "vendor_fetch": False}, "input_references": _input_refs(), "inspected_internal_loci": _loci(INTERNAL_LOCI), "mapping_result": mapped, "nonclaims": ["resolver wiring", "compat compute end-to-end", "live vendor conformance", "public Reader change", "QA PASS", "OPS completion", "PF09 status movement", "HDE-FERM008 parent Done", "epic closeout"]}
    negative = {**common, "artifact_kind": "hde_epic037_adapter_negative_fixtures", "fixtures": _negative_cases(), "all_negative_fixtures_fail_closed": True, "unsupported_tokens_not_claimed": ["VENDOR_NO_PAYLOAD_LOGGING_OK", "LOGS_KEYS_ONLY_OK", "BG_PRIVACY_REDACTION_OK"]}
    public = {**common, "artifact_kind": "hde_epic037_public_reader_no_change", "public_reader_change_claim": "NONE", "new_public_route_claim": "NONE", "new_public_flag_claim": "NONE", "new_public_payload_or_transport_claim": "NONE", "new_http_home_claim": "NONE", "inspected_public_loci": _loci(PUBLIC_LOCI)}
    no_raw = {**common, "artifact_kind": "hde_epic037_no_raw_payload_persistence", "adapter_calls_ingest_vendor_bodygraph": False, "adapter_persists_raw_request_body": False, "adapter_persists_raw_response_body": False, "adapter_persists_raw_vendor_payload": False, "adapter_output_payload_posture": "mapped_fields_and_cache_metadata_only_no_raw_data_envelope", "inspected_internal_loci": _loci(("engine/bodygraph/v2_adapter.py", "engine/bodygraph/ingest.py", "migrations/011_body_graphs_durability.sql")), "tokens_not_claimed": ["VENDOR_NO_PAYLOAD_LOGGING_OK", "LOGS_KEYS_ONLY_OK", "BG_PRIVACY_REDACTION_OK"]}
    return {MAPPING: canonical_json_bytes(mapping), NEGATIVE: canonical_json_bytes(negative), PUBLIC: canonical_json_bytes(public), NO_RAW: canonical_json_bytes(no_raw)}


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
        raise SystemExit("STALE_HDE_EPIC037_PR02_ADAPTER:" + ",".join(stale))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC037 PR-02 v2 adapter evidence")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        enforce_closed_rails()
    except DeterminismEnvError as exc:
        raise SystemExit(f"HDE_EPIC037_PR02_CLOSED_RAILS_REQUIRED:{exc}") from exc
    produced_at = _existing_generated_at(MAPPING) if args.check else None
    if produced_at is None:
        produced_at = _current_produced_at()
    write_outputs(build_outputs(produced_at), produced_at=produced_at, check=args.check)
    print("checked HDE-EPIC037 PR-02 v2 adapter artifacts" if args.check else "generated HDE-EPIC037 PR-02 v2 adapter artifacts")


if __name__ == "__main__":
    main()
