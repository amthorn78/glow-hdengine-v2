#!/usr/bin/env python3
"""Generate HDE-EPIC035 PR-02 HDAPI v2 response-normalization gap evidence."""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
RESPONSE_MAPPING = OUT / "response_mapping.snapshot.json"
RELEASE_BINDING = OUT / "release_binding.snapshot.json"
ERROR_MAPPING = OUT / "error_mapping.snapshot.json"
RATE_LIMIT_HEADERS = OUT / "rate_limit_headers.snapshot.json"
CONTRACT_MAP = OUT / "contract_map.json"
REQUEST_SHAPING = OUT / "request_shaping.snapshot.json"
SOURCE_SELECTION = OUT / "source_selection.snapshot.json"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"
INTERNAL_LOCI = (
    "engine/bodygraph/vendor_client.py",
    "engine/bodygraph/ingest.py",
    "engine/bodygraph/resolver.py",
    "engine/compat/compute.py",
)


def canonical_json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _sha256_path(path: Path) -> str:
    import hashlib

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
        raise DeterminismEnvError(f"HDAPI_V2_RESPONSE_NORMALIZATION_OPEN_RAILS:{mismatches!r}")
    return env


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


REQUIRED_ROUTE_SCHEMAS = {
    "/v2/charts": "ChartResult",
    "/v2/charts/simple": "ChartSimpleResult",
    "/v2/charts/coordinates": "ChartResult",
}
REQUIRED_ENVELOPE_FIELDS = ["timestamp", "success", "message", "errorCode", "type", "data"]


def _route_rows(contract: dict[str, Any]) -> list[dict[str, Any]]:
    routes_by_path = {
        route.get("path"): route
        for route in contract.get("route_families", [])
        if isinstance(route, dict) and route.get("path") in REQUIRED_ROUTE_SCHEMAS
    }
    missing = sorted(set(REQUIRED_ROUTE_SCHEMAS) - set(routes_by_path))
    if missing:
        raise ValueError("HDAPI_V2_RESPONSE_NORMALIZATION_ROUTE_MISSING:" + ",".join(missing))
    rows = []
    for path, expected_schema in REQUIRED_ROUTE_SCHEMAS.items():
        route = routes_by_path[path]
        expected_envelope = f"StandardResponse with type={expected_schema} and data={expected_schema}"
        if route.get("method") != "POST":
            raise ValueError(f"HDAPI_V2_RESPONSE_NORMALIZATION_METHOD_DRIFT:{path}:{route.get('method')}")
        if route.get("success_envelope") != expected_envelope:
            raise ValueError(f"HDAPI_V2_RESPONSE_NORMALIZATION_ENVELOPE_DRIFT:{path}:{route.get('success_envelope')}")
        if route.get("response_envelope_fields") != REQUIRED_ENVELOPE_FIELDS:
            raise ValueError(f"HDAPI_V2_RESPONSE_NORMALIZATION_FIELDS_DRIFT:{path}:{route.get('response_envelope_fields')}")
        rows.append({
            "auth_header_posture": "Authorization: Bearer <redacted>",
            "data_schema": expected_schema,
            "endpoint_path": path,
            "method": route.get("method"),
            "response_envelope_fields": route.get("response_envelope_fields"),
            "route_family": "recommended_v2_chart",
            "source_spec": route.get("source_spec"),
            "success_envelope": route.get("success_envelope"),
        })
    return sorted(rows, key=lambda row: row["endpoint_path"])


def _inspected_loci() -> list[dict[str, str]]:
    rows = []
    for rel in INTERNAL_LOCI:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"RESPONSE_NORMALIZATION_LOCUS_MISSING:{rel}")
        rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def build_response_mapping(*, produced_at: str) -> dict[str, Any]:
    contract = _load_json(CONTRACT_MAP)
    return {
        "adapter_schema_gap": {
            "admin_boundary": "No admin runtime behavior, HTTP home, route, flag, payload, response shape, or transport behavior is changed or proven by this evidence.",
            "bodygraph_boundary": "engine.bodygraph.ingest.ingest_vendor_bodygraph fetches via HdApiClient, emits the vendor_result.payload, and persists it into hde.body_graphs; no ChartResult/ChartSimpleResult-to-BodyGraph adapter exists in the inspected loci.",
            "cache_boundary": "hde.body_graphs can persist JSON payloads, but cache compatibility for v2 ChartResult/ChartSimpleResult is not proven because no adapter maps v2 chart data into the existing BodyGraph/person cache shape.",
            "compat_boundary": "engine.compat.compute compat/conjunction helpers consume resolved person/bodygraph inputs such as person_uid; raw v2 ChartResult/ChartSimpleResult data is not accepted as that input shape.",
            "required_follow_up": "A bounded adapter/schema proof or implementation must map v2 ChartResult/ChartSimpleResult data into the existing BodyGraph/person cache contract before compatibility can be claimed.",
        },
        "ai_scope_claim": "NONE",
        "artifact_kind": "hdapi_v2_response_normalization_gap",
        "data_payload_body_emitted": False,
        "data_payload_identity_posture": "identity is not emitted as a vendor payload body; HDE-FERM008.4 records schema/adapter gap only",
        "epic_id": "HDE-EPIC035",
        "generated_at_utc": produced_at,
        "input_references": {
            "contract_map": {"path": "artifacts/vendor/hdapi_v2/contract_map.json", "sha256": _sha256_path(CONTRACT_MAP)},
            "request_shaping_snapshot": {"path": "artifacts/vendor/hdapi_v2/request_shaping.snapshot.json", "sha256": _sha256_path(REQUEST_SHAPING)},
            "source_selection_snapshot": {"path": "artifacts/vendor/hdapi_v2/source_selection.snapshot.json", "sha256": _sha256_path(SOURCE_SELECTION)},
        },
        "inspected_internal_loci": _inspected_loci(),
        "internal_target_posture": {
            "admin": {"consumer_status": "inspected_evidence_only", "mapping_result": "no_public_or_admin_runtime_behavior_change_claimed", "proof_basis": "no new HTTP home, public route, flag, payload, response shape, or transport behavior is introduced"},
            "bodygraph": {"consumer_status": "inspected engine.bodygraph.vendor_client, engine.bodygraph.ingest, and engine.bodygraph.resolver", "mapping_result": "schema_gap_recorded", "proof_basis": "existing ingest path is v1 BodyGraph-oriented and no ChartResult/ChartSimpleResult-to-BodyGraph adapter exists in the inspected loci"},
            "cache": {"consumer_status": "inspected hde.body_graphs persistence path through engine.bodygraph.ingest", "mapping_result": "not_truthfully_proven_for_v2_chart_data", "proof_basis": "opaque JSON persistence mechanics exist, but v2 ChartResult/cache compatibility is not claimed without adapter proof"},
            "compatibility": {"consumer_status": "inspected engine.compat.compute person/bodygraph input helpers", "mapping_result": "schema_gap_recorded", "proof_basis": "compat/conjunction helpers consume person_uid-style resolved BodyGraph/person inputs; v2 ChartResult data is not proven to provide that internal shape"},
            "sampler": {"consumer_status": "inspected as non-public/dev evidence boundary", "mapping_result": "no_runtime_feed_claimed", "proof_basis": "sampler/admin/public surfaces are not changed by this evidence slice"}
        },
        "live_vendor_call_claim": "NONE",
        "no_ai_transformation_posture": "no AI interpretation, model-generated transformation, prompt, embedding, chatbot, model call, or AI-provider credential is introduced",
        "no_claims": {
            "app_side_humandesignapi_call_path": "NONE",
            "full_hdapi_v2_runtime_conformance": "NONE",
            "hde_ferm008_5_closure": "NONE",
            "live_vendor_call": "NONE",
            "new_http_home": "NONE",
            "public_reader_change": "NONE",
            "public_route_flag_payload_or_transport_change": "NONE",
            "raw_request_body_persisted": "NONE",
            "raw_response_body_persisted": "NONE",
            "raw_vendor_payload_persisted": "NONE",
        },
        "no_compatibility_by_inference": True,
        "normalized_data_path_proof_claim": "NONE",
        "pf09_document": PF09_DOCUMENT,
        "pf09_subtask_id": "HDE-FERM008.4",
        "pf09_task_id": "HDE-FERM008",
        "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"},
        "public_reader_change_claim": "NONE",
        "response_envelope_mapping_scope": "HDE-FERM007.3 proof-level v2 StandardResponse envelope mapping only",
        "response_normalization_posture": "EXACT_SCHEMA_ADAPTER_GAP_RECORDED",
        "route_family": "recommended_v2_chart",
        "routes": [dict(row, response_type=row["data_schema"], route_variant={"/v2/charts":"full_chart","/v2/charts/simple":"simple_chart","/v2/charts/coordinates":"coordinates_chart"}[row["endpoint_path"]], data_payload_identity_posture="preserve data object identity by reference/digest posture only; vendor payload body is not emitted in proof artifacts", success_status_handling="preserve StandardResponse.success as boolean success status posture without claiming live runtime status", errorCode_handling="preserve StandardResponse.errorCode as envelope error_code posture") for row in _route_rows(contract)],
        "runtime_conformance_claim": "NONE",
        "open_rails_vendor_smoke_claim": "NONE",
        "route_family_identity": {
            "legacy_v1_bodygraph_routes": [
                {"auth_header_posture": "HD-Api-Key: <redacted>", "resource_path": "bodygraphs"},
                {"auth_header_posture": "HD-Api-Key: <redacted>", "resource_path": "bodygraphs/simple"},
            ],
            "version_neutral_runtime_resource_paths": ["bodygraphs", "bodygraphs/simple", "charts", "charts/simple", "charts/coordinates"],
            "v2_chart_routes": _route_rows(contract),
        },
        "schema_gap_status": "GAP_RECORDED",
        "schema_gap_summary": "HDE-FERM008.4 remains an exact adapter/schema gap: v2 ChartResult/ChartSimpleResult StandardResponse data is not proven to feed existing BodyGraph cache or compat input paths without a ChartResult-to-BodyGraph/person adapter proof.",
    }


def build_release_binding(*, produced_at: str, response_mapping: dict[str, Any], response_sha256: str) -> dict[str, Any]:
    error_mapping = _load_json(ERROR_MAPPING)
    rate_limit = _load_json(RATE_LIMIT_HEADERS)
    return {
        "artifact_kind": "hdapi_v2_release_binding",
        "epic_id": "HDE-EPIC035",
        "generated_at_utc": produced_at,
        "no_claims": response_mapping["no_claims"],
        "pf09_document": PF09_DOCUMENT,
        "pf09_task_id": "HDE-FERM008",
        "pr_evidence_bindings": {
            "pr01_hde_ferm008_3_provider_outcome": {
                "artifacts": [
                    {"path": "artifacts/vendor/hdapi_v2/error_mapping.snapshot.json", "sha256": _sha256_path(ERROR_MAPPING)},
                    {"path": "artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json", "sha256": _sha256_path(RATE_LIMIT_HEADERS)},
                ],
                "generated_at_utc": error_mapping.get("generated_at_utc"),
                "posture": "provider outcome evidence only; error, retry, rate-limit, malformed-response, redirect, network-error, and provider-status evidence is reused without duplication",
                "subtask_id": "HDE-FERM008.3",
            },
            "pr02_hde_ferm008_4_response_normalization": {
                "artifacts": [{"path": "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json", "sha256": response_sha256}],
                "generated_at_utc": response_mapping.get("generated_at_utc"),
                "normalized_data_path_proof_claim": response_mapping.get("normalized_data_path_proof_claim"),
                "posture": response_mapping.get("response_normalization_posture"),
                "schema_gap_status": response_mapping.get("schema_gap_status"),
                "subtask_id": "HDE-FERM008.4",
            },
            "follow_up_hde_ferm008_5_evidence_loop_closure": {
                "artifacts": [],
                "posture": "FOLLOW_UP_NOT_CLAIMED_BY_PR02",
                "subtask_id": "HDE-FERM008.5",
            },
        },
        "prerequisite_chronology": {
            "pr01_error_mapping_generated_at_utc": error_mapping.get("generated_at_utc"),
            "pr01_rate_limit_generated_at_utc": rate_limit.get("generated_at_utc"),
            "pr02_response_mapping_generated_at_utc": response_mapping.get("generated_at_utc"),
        },
        "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"},
        "release_binding_posture": "PR02 binds PR01 HDE-FERM008.3 provider outcome evidence to PR02 HDE-FERM008.4 exact schema/adapter gap evidence without claiming full HumanDesignAPI v2 runtime conformance or HDE-FERM008.5 closure.",
    }


def render_outputs(*, produced_at: str | None = None) -> dict[Path, bytes]:
    timestamp = produced_at or _current_produced_at()
    response = build_response_mapping(produced_at=timestamp)
    response_body = canonical_json_bytes(response)
    import hashlib

    release = build_release_binding(produced_at=timestamp, response_mapping=response, response_sha256=hashlib.sha256(response_body).hexdigest())
    return {RESPONSE_MAPPING: response_body, RELEASE_BINDING: canonical_json_bytes(release)}


def write_outputs(outputs: dict[Path, bytes], *, check: bool) -> None:
    stale = []
    for path, body in outputs.items():
        if check:
            if not path.exists() or path.read_bytes() != body:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
            payload = json.loads(body.decode("utf-8"))
            ts = _parse_utc_iso8601(str(payload["generated_at_utc"])).timestamp()
            os.utime(path, (ts, ts))
    if stale:
        raise SystemExit("STALE_HDAPI_V2_RESPONSE_NORMALIZATION:" + ",".join(stale))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC035 PR-02 HDAPI v2 response-normalization evidence")
    parser.add_argument("--check", action="store_true", help="verify generated artifacts are current")
    args = parser.parse_args(argv)
    try:
        enforce_closed_rails()
    except DeterminismEnvError as exc:
        raise SystemExit(f"HDAPI_V2_RESPONSE_NORMALIZATION_CLOSED_RAILS_REQUIRED:{exc}") from exc
    produced_at = _existing_generated_at(RESPONSE_MAPPING) if args.check else None
    outputs = render_outputs(produced_at=produced_at)
    write_outputs(outputs, check=args.check)
    print("checked HDE-EPIC035 PR-02 response-normalization artifacts" if args.check else "generated HDE-EPIC035 PR-02 response-normalization artifacts")


if __name__ == "__main__":
    main()
