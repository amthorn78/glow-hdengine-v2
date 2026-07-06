#!/usr/bin/env python3
"""Generate HDE-EPIC037 PR-01 v2 BodyGraph-detail field-sufficiency evidence."""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Mapping

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
FIELD_PROOF = OUT / "hde_epic037_field_sufficiency_proof.json"
CONTRACT = OUT / "hde_epic037_adapter_contract.snapshot.json"
NONCLAIMS = OUT / "hde_epic037_adapter_contract_nonclaims.json"
DOC_DELTA = ROOT / "audit" / "docdeltas" / "hde-epic037_doc_deltas.md"
QA_DOC_DELTA = ROOT / "audit" / "qa" / "hde-epic037" / "00_meta" / "doc_deltas.md"
CONTRACT_MAP = OUT / "contract_map.json"
RESPONSE_MAPPING = OUT / "response_mapping.snapshot.json"
V2_ROUTES = OUT / "source_cache" / "v2-routes.yaml"
MIGRATION = ROOT / "migrations" / "011_body_graphs_durability.sql"
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}
INTERNAL_LOCI = (
    "engine/bodygraph/vendor_client.py",
    "engine/bodygraph/ingest.py",
    "engine/bodygraph/resolver.py",
    "engine/compat/compute.py",
    "engine/compat/ordering.py",
    "migrations/011_body_graphs_durability.sql",
)

CHART_RESULT_FIELDS = {
    "type", "profile", "channelsShort", "centers", "strategy", "authority", "incarnationCross",
    "definition", "signature", "notSelfTheme", "cognition", "determination", "variables", "motivation",
    "transference", "perspective", "distraction", "environment", "circuitries", "channelsLong",
    "gates", "activations", "birthDateUtc",
}
CHART_SIMPLE_FIELDS = {"type", "profile", "gates", "channelsShort", "centers"}

INTERNAL_CONTRACT = [
    {"contract_area": "person", "internal_field": "person_uid", "required": True, "consumer": "engine.compat.compute._person_from_resolved and engine.compat.ordering._uid", "vendor_source": None, "status": "unsupported_vendor_field", "reason": "ChartResult and ChartSimpleResult schemas do not define a stable HDE person_uid/user_id field."},
    {"contract_area": "cache", "internal_field": "hde.body_graphs.user_id", "required": True, "consumer": "engine.bodygraph.ingest._persist_bodygraph", "vendor_source": None, "status": "caller_supplied_not_vendor", "reason": "Cache identity is supplied by the resolver/app caller, not by the v2 chart payload."},
    {"contract_area": "cache", "internal_field": "hde.body_graphs.vendor", "required": True, "consumer": "engine.bodygraph.ingest._persist_bodygraph", "vendor_source": None, "status": "internal_constant", "reason": "Existing cache stores vendor='hdapi'."},
    {"contract_area": "cache", "internal_field": "hde.body_graphs.vendor_version", "required": True, "consumer": "engine.bodygraph.ingest._persist_bodygraph", "vendor_source": None, "status": "route_metadata_required", "reason": "Existing ingest stores a numeric vendor_version; a chart-backed adapter would need explicit version metadata without persisting raw payload bodies as proof."},
    {"contract_area": "cache", "internal_field": "hde.body_graphs.input_fingerprint", "required": True, "consumer": "engine.bodygraph.vendor_client.HdApiClient.build_request", "vendor_source": None, "status": "request_metadata_required", "reason": "Fingerprint is request-body metadata, not a field in ChartResult/ChartSimpleResult."},
    {"contract_area": "cache", "internal_field": "hde.body_graphs.payload", "required": True, "consumer": "hde.body_graphs_current view and resolver cache reads", "vendor_source": "StandardResponse.data", "status": "schema_change_or_adapter_required", "reason": "Existing persistence can hold JSONB, but compute-ready BodyGraph/person cache semantics are not proven for raw v2 chart data."},
    {"contract_area": "compat", "internal_field": "left.person_uid and right.person_uid", "required": True, "consumer": "engine.compat.compute.conjunction_public", "vendor_source": None, "status": "unsupported_vendor_field", "reason": "Compatibility computation normalizes pairs by person_uid only; chart fields such as type/profile/gates/channels/centers do not replace person_uid."},
    {"contract_area": "bodygraph", "internal_field": "resolved bodygraph/person mapping", "required": True, "consumer": "engine.bodygraph.resolver.resolve_bodygraph", "vendor_source": "ChartResult or ChartSimpleResult", "status": "adapter_required", "reason": "No inspected runtime adapter maps v2 chart schema into HDE resolved BodyGraph/person/cache contract."},
]

NEGATIVE_FIXTURE_INPUTS = (
    ("chart_result_typed_insufficient_contract", "ChartResult", CHART_RESULT_FIELDS),
    ("chart_simple_typed_insufficient_contract_and_vendor_detail", "ChartSimpleResult", CHART_SIMPLE_FIELDS),
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
    if mismatches:  # pragma: no cover
        raise DeterminismEnvError(f"HDE_EPIC037_FIELD_SUFFICIENCY_OPEN_RAILS:{mismatches!r}")
    return env


def _inspected_loci() -> list[dict[str, str]]:
    rows = []
    for rel in INTERNAL_LOCI:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"HDE_EPIC037_LOCUS_MISSING:{rel}")
        rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def _input_refs() -> dict[str, dict[str, str]]:
    refs = {}
    for name, path in (("contract_map", CONTRACT_MAP), ("response_mapping", RESPONSE_MAPPING), ("v2_routes_source_cache", V2_ROUTES)):
        if path.is_file():
            refs[name] = {"path": path.relative_to(ROOT).as_posix(), "sha256": _sha256_path(path)}
    return refs


def evaluate_payload_family(payload_family: str, fields: set[str]) -> dict[str, Any]:
    missing_required = [row["internal_field"] for row in INTERNAL_CONTRACT if row["required"] and row["status"] in {"unsupported_vendor_field", "adapter_required", "schema_change_or_adapter_required"}]
    if payload_family == "ChartSimpleResult":
        missing_vendor_detail = sorted(CHART_RESULT_FIELDS - fields)
        classification = "TYPED_INSUFFICIENT_CLASSIFICATION"
    elif payload_family == "ChartResult":
        missing_vendor_detail = []
        classification = "TYPED_INSUFFICIENT_CLASSIFICATION"
    else:
        missing_vendor_detail = []
        classification = "UNSUPPORTED_PAYLOAD_FAMILY"
    return {
        "payload_family": payload_family,
        "fields_present": sorted(fields),
        "missing_internal_contract_fields": missing_required,
        "missing_vendor_detail_fields": missing_vendor_detail,
        "field_sufficiency": "INSUFFICIENT",
        "classification": classification,
        "compute_ready": False,
        "fail_closed": True,
    }


def _negative_fixtures() -> list[dict[str, Any]]:
    fixtures = []
    for fixture_id, payload_family, fields in NEGATIVE_FIXTURE_INPUTS:
        evaluation = evaluate_payload_family(payload_family, set(fields))
        fixtures.append({
            "fixture_id": fixture_id,
            "payload_family": payload_family,
            "fields_present": evaluation["fields_present"],
            "expected_classification": evaluation["classification"],
            "expected_field_sufficiency": evaluation["field_sufficiency"],
            "expected_compute_ready": evaluation["compute_ready"],
            "expected_fail_closed": evaluation["fail_closed"],
            "missing_internal_contract_fields": evaluation["missing_internal_contract_fields"],
            "missing_vendor_detail_fields": evaluation["missing_vendor_detail_fields"],
        })
    return fixtures


def _common(produced_at: str) -> dict[str, Any]:
    return {"epic_id": "HDE-EPIC037", "generated_at_utc": produced_at, "pf09_document": PF09_DOCUMENT, "pf09_task_id": "HDE-FERM008", "pf09_subtask_id": "HDE-FERM008.7", "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"}}


def build_outputs(produced_at: str) -> dict[Path, bytes]:
    chart_result = evaluate_payload_family("ChartResult", CHART_RESULT_FIELDS)
    chart_simple = evaluate_payload_family("ChartSimpleResult", CHART_SIMPLE_FIELDS)
    selected = "typed_insufficient_classification"
    contract = {
        **_common(produced_at),
        "artifact_kind": "hde_epic037_adapter_contract_snapshot",
        "selected_payload_family": selected,
        "candidate_payload_families": [chart_result, chart_simple],
        "internal_contract": INTERNAL_CONTRACT,
        "required_internal_fields": [row for row in INTERNAL_CONTRACT if row["required"]],
        "optional_internal_fields": [],
        "unsupported_or_absent_fields": [row for row in INTERNAL_CONTRACT if row["status"] in {"unsupported_vendor_field", "adapter_required", "schema_change_or_adapter_required"}],
        "schema_changes_required": ["Define a deterministic v2 ChartResult-to-HDE BodyGraph/person/cache adapter or schema extension before resolver/compat runtime use."],
        "inspected_internal_loci": _inspected_loci(),
        "input_references": _input_refs(),
    }
    proof = {
        **_common(produced_at),
        "artifact_kind": "hde_epic037_field_sufficiency_proof",
        "selected_payload_family": selected,
        "field_sufficiency_status": "INSUFFICIENT_FAIL_CLOSED",
        "v2_chart_data_feeds_existing_bodygraph_person_cache_compat_contract": False,
        "machine_checkable_contract_sha256": hashlib.sha256(canonical_json_bytes(contract)).hexdigest(),
        "candidate_evaluations": {"ChartResult": chart_result, "ChartSimpleResult": chart_simple},
        "negative_fixtures": _negative_fixtures(),
        "adapter_compatibility_proof": {"schema_adapter_gap_status": "GAP_RECORDED", "runtime_adapter_implemented": False, "resolver_rewired": False, "compat_compute_ready": False},
        "no_raw_vendor_payload_body_persisted_in_evidence": True,
        "inspected_internal_loci": _inspected_loci(),
        "input_references": _input_refs(),
    }
    nonclaims = {
        **_common(produced_at),
        "artifact_kind": "hde_epic037_adapter_contract_nonclaims",
        "selected_payload_family": selected,
        "unsupported_hde_paths": ["bg:resolve --source vendor v2 chart-backed BodyGraph-detail runtime", "compat/conjunction compute from raw ChartResult or ChartSimpleResult", "cache-read proof for raw v2 chart payload as resolved BodyGraph/person"],
        "unsupported_vendor_fields_or_gaps": ["person_uid absent from ChartResult/ChartSimpleResult schema", "ChartSimpleResult omits activations/birthDateUtc/authority/definition detail present in ChartResult", "no deterministic adapter maps chart fields to HDE resolved BodyGraph/person contract"],
        "no_claims": {"public_reader_change": "NONE", "public_route": "NONE", "public_flag": "NONE", "public_payload_or_transport_change": "NONE", "new_http_home": "NONE", "app_side_humandesignapi_call_path": "NONE", "live_vendor_call": "NONE", "open_rails_vendor_smoke": "NONE", "raw_request_body_persisted": "NONE", "raw_response_body_persisted": "NONE", "raw_vendor_payload_persisted": "NONE", "ai_llm_model_call_behavior": "NONE", "full_hdapi_v2_runtime_conformance": "NONE", "hde_ferm008_parent_done": "NONE", "qa_pass": "NONE", "ops_completion": "NONE", "pf09_status_movement": "NONE", "epic_closeout": "NONE"},
        "no_compatibility_by_inference": True,
    }
    doc = "\n".join([
        "# HDE-EPIC037 PR-01 doc deltas", "", "- Recorded HDE-FERM008.7 field-sufficiency evidence for v2 BodyGraph-detail readiness.", "- Selected payload family is a typed insufficient classification, not runtime conformance.", "- No public Reader, route, flag, payload, transport, AI, live-vendor, OPS, or PF-Canon change is claimed.", "",
    ]).encode("utf-8")
    return {FIELD_PROOF: canonical_json_bytes(proof), CONTRACT: canonical_json_bytes(contract), NONCLAIMS: canonical_json_bytes(nonclaims), DOC_DELTA: doc, QA_DOC_DELTA: doc}


def _write_path_proof(path: Path, produced_at: str, *, check: bool) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(rel, sha256=_sha256_path(path), size_bytes=stat.st_size, mtime_utc=None, produced_at=produced_at, default_produced_at=produced_at, check=check, stat_mtime=stat.st_mtime)


def write_outputs(outputs: dict[Path, bytes], *, produced_at: str, check: bool) -> None:
    stale = []
    for path, body in outputs.items():
        if check:
            actual = path.read_bytes() if path.exists() else b""
            if path in {DOC_DELTA, QA_DOC_DELTA}:
                matches = actual.startswith(body)
            else:
                matches = actual == body
            if not path.exists() or not matches:
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
        raise SystemExit("STALE_HDE_EPIC037_FIELD_SUFFICIENCY:" + ",".join(stale))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC037 PR-01 field-sufficiency evidence")
    parser.add_argument("--check", action="store_true", help="verify generated artifacts are current")
    args = parser.parse_args(argv)
    try:
        enforce_closed_rails()
    except DeterminismEnvError as exc:
        raise SystemExit(f"HDE_EPIC037_FIELD_SUFFICIENCY_CLOSED_RAILS_REQUIRED:{exc}") from exc
    produced_at = _existing_generated_at(FIELD_PROOF) if args.check else None
    if produced_at is None:
        produced_at = _current_produced_at()
    write_outputs(build_outputs(produced_at), produced_at=produced_at, check=args.check)
    print("checked HDE-EPIC037 PR-01 field-sufficiency artifacts" if args.check else "generated HDE-EPIC037 PR-01 field-sufficiency artifacts")


if __name__ == "__main__":
    main()
