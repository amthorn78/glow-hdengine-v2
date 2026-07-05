#!/usr/bin/env python3
"""Generate HDE-EPIC036 PR-01 bg:resolve route-policy evidence."""
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

from engine.bodygraph.vendor_client import classify_bg_resolve_route_policy, route_auth_posture
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.evidence import update_evidence_index

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
AUDIT = ROOT / "audit" / "qa" / "hde-epic036"
ROUTE_POLICY = OUT / "bg_resolve_route_policy.snapshot.json"
BODYGRAPH_DETAIL = OUT / "bg_resolve_bodygraph_detail_proof.json"
RUNTIME_NONCLAIMS = OUT / "bg_resolve_runtime_nonclaims.json"
REQUEST_SHAPE = OUT / "bg_resolve_request_shape.snapshot.json"
POLICY_BINDING = OUT / "bg_resolve_policy_binding.snapshot.json"
DECISION_LOG = AUDIT / "route_policy_decision.log"
RESPONSE_MAPPING = OUT / "response_mapping.snapshot.json"
OPS_FINAL = ROOT / "audit" / "ops" / "hde-epic035" / "ops-01" / "hdapi-v2-open-rails-smoke" / "final_classification.txt"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"
INTERNAL_LOCI = (
    "engine/bodygraph/vendor_client.py",
    "engine/bodygraph/ingest.py",
    "engine/bodygraph/resolver.py",
    "engine/cli/main.py",
    "tests/bodygraph/test_bg_resolve_route_policy.py",
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
        raise DeterminismEnvError(f"HDE_EPIC036_ROUTE_POLICY_OPEN_RAILS:{mismatches!r}")
    return env


def _inspected_loci() -> list[dict[str, str]]:
    rows = []
    for rel in INTERNAL_LOCI:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"HDE_EPIC036_LOCUS_MISSING:{rel}")
        rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def _input_refs() -> dict[str, dict[str, str]]:
    refs = {}
    for name, path in (("response_mapping", RESPONSE_MAPPING), ("epic035_ops01_final_classification", OPS_FINAL)):
        if path.is_file():
            refs[name] = {"path": path.relative_to(ROOT).as_posix(), "sha256": _sha256_path(path)}
    return refs


def _common(produced_at: str) -> dict[str, Any]:
    return {
        "epic_id": "HDE-EPIC036",
        "generated_at_utc": produced_at,
        "pf09_document": PF09_DOCUMENT,
        "pf09_task_id": "HDE-FERM008",
        "pf09_subtask_id": "HDE-FERM008.6",
        "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"},
    }


def _epic036_historical_v2_policy() -> dict[str, Any]:
    """Return the EPIC036 PR-01 route-policy decision as historical evidence.

    EPIC037 PR-03 intentionally supersedes the shared runtime classifier for
    configured-v2 bases after the deterministic v2 adapter exists. EPIC036
    remains a closed-rails historical evidence family for the pre-adapter
    unsupported-runtime-nonclaim decision, so this generator isolates that
    recorded decision instead of re-evaluating the current classifier.
    """

    return {
        "classification": "unsupported_runtime_nonclaim",
        "configured_base_version": "v2",
        "error_code": "PROVIDER_ROUTE_UNSUPPORTED",
        "geocode_required": True,
        "reason": "configured v2 base cannot use legacy bodygraphs as final BodyGraph-detail behavior without a v2 ChartResult-to-BodyGraph adapter",
        "resource_path": "bodygraphs",
        "route_auth_posture": route_auth_posture("bodygraphs"),
        "route_family": "legacy_bodygraph",
        "supported": False,
    }


def build_outputs(produced_at: str) -> dict[Path, bytes]:
    v2_policy = _epic036_historical_v2_policy()
    legacy_policy = classify_bg_resolve_route_policy("https://vendor.example.test/v1")
    nonclaims = {
        **_common(produced_at),
        "artifact_kind": "bg_resolve_runtime_nonclaims",
        "selected_route_policy_classification": "unsupported_runtime_nonclaim",
        "unsupported_runtime_nonclaim": True,
        "no_claims": {
            "app_side_humandesignapi_credential_ownership": "NONE",
            "app_side_humandesignapi_call_path": "NONE",
            "full_hdapi_v2_runtime_conformance": "NONE",
            "new_http_home": "NONE",
            "public_flag": "NONE",
            "public_payload_change": "NONE",
            "public_reader_change": "NONE",
            "public_route": "NONE",
            "raw_payload_persistence": "NONE",
            "raw_request_body_persisted": "NONE",
            "raw_response_body_persisted": "NONE",
            "ai_scope": "NONE",
        },
        "no_compatibility_by_inference": True,
        "chart_simple_success_bodygraph_detail_claim": "NONE",
    }
    route_policy = {
        **_common(produced_at),
        "artifact_kind": "bg_resolve_route_policy",
        "selected_posture": "unsupported_runtime_nonclaim",
        "supported_postures": {
            "v2_chart_backed_bodygraph_resolution": "NOT_CLAIMED_NO_ADAPTER",
            "explicit_legacy_fallback": "PRESERVED_ONLY_FOR_NON_V2_CONFIGURED_BASE",
            "dual_route_policy": "NOT_IMPLEMENTED_ADR_REQUIRED",
            "unsupported_runtime_nonclaim": "SELECTED_FOR_CONFIGURED_V2_BASE",
        },
        "configured_v2_policy": v2_policy,
        "legacy_fallback_policy": legacy_policy,
        "route_family_identity": {
            "legacy_bodygraph": {"resource_path": "bodygraphs", "auth_header_posture": route_auth_posture("bodygraphs"), "geocode_required": True},
            "v2_chart_candidate": {"resource_path": "charts/simple", "auth_header_posture": route_auth_posture("charts/simple"), "geocode_required": True, "bodygraph_detail_sufficiency": "NOT_CLAIMED"},
        },
        "input_references": _input_refs(),
        "inspected_internal_loci": _inspected_loci(),
        "runtime_nonclaims": nonclaims["no_claims"],
    }
    bodygraph_detail = {
        **_common(produced_at),
        "artifact_kind": "bg_resolve_bodygraph_detail_proof",
        "bodygraph_detail_sufficiency": "UNSUPPORTED_RUNTIME_NONCLAIM",
        "adapter_sufficiency": "NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI",
        "v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows": False,
        "proof_basis": "Existing response_mapping.snapshot.json records normalized_data_path_proof_claim=NONE and schema_gap_status=GAP_RECORDED; PR-01 code now refuses configured-v2 bg:resolve legacy bodygraphs before request construction.",
        "inspected_internal_loci": _inspected_loci(),
        "input_references": _input_refs(),
    }
    request_shape = {
        **_common(produced_at),
        "artifact_kind": "bg_resolve_request_shape",
        "configured_v2_bg_resolve_request_shape": "NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM",
        "legacy_fallback_request_shape": {"configured_base": "non-v2", "resource_path": "bodygraphs", "method": "POST", "auth_header_posture": route_auth_posture("bodygraphs"), "geocode_header_posture": "HD-Geocode-Key: <redacted>"},
        "v2_chart_request_shape_not_used_for_bg_resolve": {"resource_path": "charts/simple", "auth_header_posture": route_auth_posture("charts/simple"), "bodygraph_detail_sufficiency": "NOT_CLAIMED"},
        "raw_request_body_persisted": False,
        "raw_response_body_persisted": False,
        "raw_vendor_payload_persisted": False,
    }
    binding = {
        **_common(produced_at),
        "artifact_kind": "bg_resolve_policy_binding",
        "policy_binding": {
            "selected_classification": "unsupported_runtime_nonclaim",
            "hde_ferm008_6_completion_role": "Complete in this epic for route-policy classification only",
            "ops_01_requirement": "OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence.",
            "follow_up": ["PR-02 evidence-loop binding", "OPS-01 live vendor observation if PO wants bounded live observation", "future adapter proof before full v2 runtime conformance"],
        },
        "artifacts": [
            "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
            "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
            "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
            "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
            "audit/qa/hde-epic036/route_policy_decision.log",
        ],
    }
    decision = "\n".join([
        "HDE-EPIC036 PR-01 bg:resolve route-policy decision",
        f"generated_at_utc={produced_at}",
        "selected_route_policy_classification=unsupported_runtime_nonclaim",
        "configured_v2_bg_resolve_request_shape=NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM",
        "explicit_legacy_fallback=PRESERVED_ONLY_FOR_NON_V2_CONFIGURED_BASE",
        "dual_route_policy=NOT_IMPLEMENTED_ADR_REQUIRED",
        "bodygraph_detail_sufficiency=UNSUPPORTED_RUNTIME_NONCLAIM",
        "v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows=false",
        "route_auth_posture=route_metadata_driven_redacted",
        "no_public_reader_change=true",
        "no_public_route=true",
        "no_public_flag=true",
        "no_public_payload_change=true",
        "no_new_http_home=true",
        "no_app_side_humandesignapi_credential_ownership=true",
        "no_raw_payload_persistence=true",
        "no_ai_scope=true",
        "no_full_hdapi_v2_runtime_conformance=true",
        "OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence.",
        "",
    ]).encode("utf-8")
    return {
        ROUTE_POLICY: canonical_json_bytes(route_policy),
        BODYGRAPH_DETAIL: canonical_json_bytes(bodygraph_detail),
        RUNTIME_NONCLAIMS: canonical_json_bytes(nonclaims),
        REQUEST_SHAPE: canonical_json_bytes(request_shape),
        POLICY_BINDING: canonical_json_bytes(binding),
        DECISION_LOG: decision,
    }


def _write_path_proof(path: Path, produced_at: str, *, check: bool) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel,
        sha256=_sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=None,
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=check,
        stat_mtime=stat.st_mtime,
    )


def write_outputs(outputs: dict[Path, bytes], *, produced_at: str, check: bool) -> None:
    stale: list[str] = []
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
        raise SystemExit("STALE_HDE_EPIC036_BG_RESOLVE_ROUTE_POLICY:" + ",".join(stale))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC036 PR-01 bg:resolve route-policy evidence")
    parser.add_argument("--check", action="store_true", help="verify generated artifacts are current")
    args = parser.parse_args(argv)
    try:
        enforce_closed_rails()
    except DeterminismEnvError as exc:
        raise SystemExit(f"HDE_EPIC036_ROUTE_POLICY_CLOSED_RAILS_REQUIRED:{exc}") from exc
    produced_at = _existing_generated_at(ROUTE_POLICY) if args.check else None
    if produced_at is None:
        produced_at = _current_produced_at()
    outputs = build_outputs(produced_at)
    write_outputs(outputs, produced_at=produced_at, check=args.check)
    print("checked HDE-EPIC036 PR-01 bg:resolve route-policy artifacts" if args.check else "generated HDE-EPIC036 PR-01 bg:resolve route-policy artifacts")


if __name__ == "__main__":
    main()
