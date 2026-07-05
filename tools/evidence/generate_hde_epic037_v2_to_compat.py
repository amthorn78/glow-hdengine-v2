#!/usr/bin/env python3
"""Generate HDE-EPIC037 PR-04 v2 adapter-to-compat evidence."""
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

from engine.bodygraph.v2_adapter import CHART_RESULT_REQUIRED_FIELDS, V2ChartAdapterContext, adapt_v2_chart_payload
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import conjunction_public
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from engine.runtime.public import emit_reader_public_envelope
from tools.evidence import update_evidence_index

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "vendor" / "hdapi_v2"
PROOF = OUT / "hde_epic037_v2_to_compat_proof.json"
TWO_RUN = OUT / "hde_epic037_v2_to_compat_two_run.json"
PAIR_ORDER = OUT / "hde_epic037_v2_to_compat_pair_order.json"
BOUNDARY = OUT / "hde_epic037_admin_public_boundary.json"
PF09_DOCUMENT = "PF09.5 — HDE Build Checklist Fermentation"
CLOSED_RAILS_ENV = {"ALLOW_NETWORK": "0", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "1", "TZ": "UTC"}
INTERNAL_LOCI = (
    "engine/bodygraph/v2_adapter.py",
    "engine/bodygraph/resolver.py",
    "engine/compat/compute.py",
    "engine/compat/ordering.py",
    "engine/compat/ts_v0.py",
    "engine/runtime/public.py",
    "presenter/reader_v1/emitter.py",
    "adapter/http_reader.py",
)
INPUT_REFS = (
    "artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract.snapshot.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json",
    "artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json",
)
NONCLAIMS = [
    "live vendor success",
    "OPS completion",
    "QA PASS",
    "PF09 status movement",
    "HDE-FERM008 parent Done",
    "closeout",
    "public Reader change",
    "new public route",
    "new public flag",
    "new public payload/transport",
    "new HTTP home",
    "app-side vendor ownership",
    "raw secret persistence",
    "uncontrolled raw vendor payload persistence",
    "mapped-cache write persistence",
    "production deployment",
    "AI scope",
]
FORBIDDEN_PUBLIC_TERMS = [
    "score", "personal_key", "shared_key", "proof", "signals", "overall", "percent", "raw",
    "normalized", "clamped", "rounded", "mechanics", "bodygraph", "cache", "adapter",
    "input_fingerprint", "payload", "payload_posture", "vendor", "vendor_version", "birthDateUtc",
    "activations", "authority", "centers", "channelsLong", "channelsShort", "gates",
    "HD_API_KEY", "GEO_API_KEY", "Authorization", "HD-Api-Key", "HD-Geocode-Key",
    "configured_base_url", "raw_request_body", "raw_response_body",
]


def canonical_json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _sha256_bytes(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def _sha256_path(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


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


def enforce_closed_rails() -> dict[str, str]:
    env = ensure_determinism_env()
    mismatches = {key: env.get(key) for key, expected in CLOSED_RAILS_ENV.items() if env.get(key) != expected}
    if mismatches:
        raise DeterminismEnvError(f"HDE_EPIC037_PR04_OPEN_RAILS:{mismatches!r}")
    return {key: env.get(key, "") for key in sorted(CLOSED_RAILS_ENV)}


def _common(produced_at: str) -> dict[str, Any]:
    return {
        "epic_id": "HDE-EPIC037",
        "generated_at_utc": produced_at,
        "pf09_document": PF09_DOCUMENT,
        "pf09_task_id": "HDE-FERM008",
        "pf09_subtask_id": "HDE-FERM008.10",
        "rails": {"allow_network": "0", "closed_rails_only": True, "safe_mode": "1"},
        "nonclaims": NONCLAIMS,
    }


def _loci() -> list[dict[str, str]]:
    rows = []
    for rel in INTERNAL_LOCI:
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"HDE_EPIC037_PR04_LOCUS_MISSING:{rel}")
        rows.append({"path": rel, "sha256": _sha256_path(path)})
    return rows


def _input_refs() -> dict[str, dict[str, str]]:
    refs = {}
    for rel in INPUT_REFS:
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"MISSING_HDE_EPIC037_PR04_INPUT:{rel}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("epic_id") != "HDE-EPIC037" or payload.get("pf09_task_id") != "HDE-FERM008":
            raise SystemExit(f"INVALID_HDE_EPIC037_PR04_INPUT:{rel}")
        refs[Path(rel).stem] = {"path": rel, "sha256": _sha256_path(path)}
    return refs


def chart_result_payload(*, kind: str) -> dict[str, Any]:
    payload: dict[str, Any] = {field: f"fixture:{kind}:{field}" for field in sorted(CHART_RESULT_REQUIRED_FIELDS)}
    if kind == "a":
        payload.update({"type": "Generator", "strategy": "Wait to respond", "profile": "1/3", "authority": "Sacral", "birthDateUtc": "1990-01-01T12:00:00.000Z", "centers": ["G", "Sacral"], "channelsLong": ["The Channel of Charisma (20-34)"], "channelsShort": ["20-34"], "gates": ["20", "34"]})
    else:
        payload.update({"type": "Projector", "strategy": "Wait for the invitation", "profile": "4/6", "authority": "Splenic", "birthDateUtc": "1991-02-03T04:05:00.000Z", "centers": ["G", "Spleen"], "channelsLong": ["The Channel of the Brainwave (57-20)"], "channelsShort": ["57-20"], "gates": ["57", "20"]})
    payload["activations"] = {"design": {}, "personality": {}}
    return {"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": payload}


def context(kind: str) -> V2ChartAdapterContext:
    return V2ChartAdapterContext(
        person_uid=f"person-epic037-pr04-{kind}",
        user_id=f"123e4567-e89b-12d3-a456-42661417400{0 if kind == 'a' else 1}",
        vendor="hdapi",
        vendor_version=2,
        input_fingerprint=("a" if kind == "a" else "b") * 64,
        route_family="recommended_v2_chart",
        route="vendor.hdapi.post:/charts",
        payload_family="ChartResult",
    )


def _mapped_pair() -> dict[str, Mapping[str, Any]]:
    pair = {}
    for kind in ("a", "b"):
        result = adapt_v2_chart_payload(chart_result_payload(kind=kind), context(kind)).as_dict()
        if result.get("status") != "mapped" or result.get("code") != "ADAPTER_MAPPED":
            raise SystemExit(f"HDE_EPIC037_PR04_ADAPTER_FIXTURE_FAILED:{kind}")
        pair[kind] = result
    return pair


def _compat(left: Mapping[str, Any], right: Mapping[str, Any]) -> dict[str, object]:
    return conjunction_public(left, right, viewer_top="harmony", viewer_weights={}, engine_tag="hde-compat-v1", release_id="0" * 64, invocation_tag="epic037-pr04-fixture")


def _assert_shape(result: Mapping[str, Any]) -> dict[str, Any]:
    resolved = result["resolved"]
    cache = result["cache"]
    checks = {
        "resolved.person_uid": isinstance(resolved.get("person_uid"), str),
        "resolved.person.person_uid": isinstance(resolved.get("person", {}).get("person_uid"), str),
        "resolved.bodygraph": isinstance(resolved.get("bodygraph"), Mapping),
        "resolved.source": resolved.get("source") == "hdapi_v2_chart_adapter",
        "cache.user_id": isinstance(cache.get("user_id"), str),
        "cache.vendor": cache.get("vendor") == "hdapi",
        "cache.vendor_version": cache.get("vendor_version") == 2,
        "cache.input_fingerprint": isinstance(cache.get("input_fingerprint"), str),
        "cache.payload": cache.get("payload") == resolved,
        "cache.payload_posture": cache.get("payload_posture") == "adapter_mapped_no_raw_vendor_payload",
    }
    if not all(checks.values()):
        raise SystemExit(f"HDE_EPIC037_PR04_SHAPE_INSUFFICIENT:{checks!r}")
    return checks


def _reader_chart(resolved: Mapping[str, Any]) -> dict[str, object]:
    return {"mechanics": {"type": resolved["bodygraph"]["type"]}}


def _boundary(mapped: dict[str, Mapping[str, Any]], produced_at: str, common: dict[str, Any]) -> dict[str, Any]:
    public_bytes, public_envelope = emit_reader_public_envelope(_reader_chart(mapped["a"]["resolved"]), _reader_chart(mapped["b"]["resolved"]), engine_tag="hde-compat-v1", invocation_tag="epic037-pr04-fixture", release_id="0" * 64)
    text = public_bytes.decode("utf-8")
    forbidden_hits = [term for term in FORBIDDEN_PUBLIC_TERMS if term in text]
    category_keys = sorted(public_envelope["categories"][0].keys()) if public_envelope.get("categories") else []
    bands_only = all(sorted(item.keys()) == ["band", "id"] for item in public_envelope["categories"])
    numeric_free = not any(isinstance(value, (int, float)) and not isinstance(value, bool) for item in public_envelope["categories"] for value in item.values())
    if forbidden_hits or not bands_only or not numeric_free:
        raise SystemExit(f"HDE_EPIC037_PR04_PUBLIC_BOUNDARY_FAILED:{forbidden_hits!r}")
    return {
        **common,
        "artifact_kind": "hde_epic037_admin_public_boundary",
        "input_references": _input_refs(),
        "inspected_internal_loci": _loci(),
        "public_reader_bytes_sha256": _sha256_bytes(public_bytes),
        "public_reader_lf_terminated": public_bytes.endswith(b"\n") and not public_bytes.endswith(b"\n\n"),
        "public_reader_envelope_keys": sorted(public_envelope.keys()),
        "public_reader_category_keys": category_keys,
        "public_reader_bands_only": bands_only,
        "public_reader_numeric_free": numeric_free,
        "forbidden_public_terms": FORBIDDEN_PUBLIC_TERMS,
        "forbidden_public_term_hits": forbidden_hits,
        "admin_only_diagnostics_home": "governed PR-04 artifacts and admin/proof outputs only",
        "new_public_reader_surface": {"route": False, "flag": False, "payload_field": False, "transport_behavior": False, "http_home": False},
        "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
    }


def _proof_payload(produced_at: str) -> dict[str, Any]:
    mapped = _mapped_pair()
    compat = _compat(mapped["a"]["resolved"], mapped["b"]["resolved"])
    category_ids = [item["id"] for item in compat["conjunction"]["compat"]["categories"]]
    if category_ids != list(CATEGORIES_ORDER_V1):
        raise SystemExit("HDE_EPIC037_PR04_CATEGORY_ORDER_DRIFT")
    common = _common(produced_at)
    return {
        **common,
        "artifact_kind": "hde_epic037_v2_to_compat_proof",
        "input_references": _input_refs(),
        "inspected_internal_loci": _loci(),
        "fixture_count": 2,
        "adapter_results": {kind: {"status": item["status"], "code": item["code"], "payload_family": item["payload_family"], "shape_sufficiency": _assert_shape(item)} for kind, item in mapped.items()},
        "cache_payload_posture": {kind: item["cache"]["payload_posture"] for kind, item in mapped.items()},
        "compat_acceptance": {"function": "engine.compat.compute.conjunction_public", "accepted_mapped_resolved_parties": True, "category_count": len(category_ids), "category_ids": category_ids, "meta_keys": sorted(compat["conjunction"]["compat"]["meta"].keys())},
        "compat_output_sha256": _sha256_bytes(canonical_json_bytes(compat)),
        "raw_request_response_vendor_bodies_absent": True,
        "tokens": ["ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"],
    }


def build_outputs(produced_at: str) -> dict[Path, bytes]:
    common = _common(produced_at)
    mapped = _mapped_pair()
    proof = _proof_payload(produced_at)
    proof_bytes_1 = canonical_json_bytes(proof)
    proof_bytes_2 = canonical_json_bytes(_proof_payload(produced_at))
    if proof_bytes_1 != proof_bytes_2:
        raise SystemExit("HDE_EPIC037_PR04_TWO_RUN_DRIFT")
    ab = _compat(mapped["a"]["resolved"], mapped["b"]["resolved"])
    ba = _compat(mapped["b"]["resolved"], mapped["a"]["resolved"])
    ab_bytes = canonical_json_bytes(ab)
    ba_bytes = canonical_json_bytes(ba)
    pair_identity = ab_bytes == ba_bytes
    if not pair_identity:
        raise SystemExit("HDE_EPIC037_PR04_PAIR_ORDER_DRIFT")
    two_run = {**common, "artifact_kind": "hde_epic037_v2_to_compat_two_run", "input_references": _input_refs(), "inspected_internal_loci": _loci(), "first_run_sha256": _sha256_bytes(proof_bytes_1), "second_run_sha256": _sha256_bytes(proof_bytes_2), "canonical_bytes_identical": True, "rails_and_locale_pins": CLOSED_RAILS_ENV, "no_time_random_network_database_write_dependency": True, "tokens": ["TWO_RUN_IDENTITY_OK", "ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"]}
    pair_order = {**common, "artifact_kind": "hde_epic037_v2_to_compat_pair_order", "input_references": _input_refs(), "inspected_internal_loci": _loci(), "pair_order_rule": "engine.compat.ordering.normalize_pair sorts by person_uid before pair_key construction", "ab_sha256": _sha256_bytes(ab_bytes), "ba_sha256": _sha256_bytes(ba_bytes), "canonical_ab_ba_bytes_identical": pair_identity, "normalized_left_person_uid": ab["conjunction"]["left"]["person_uid"], "normalized_right_person_uid": ab["conjunction"]["right"]["person_uid"], "tokens": ["COMPOSITE_ABBA_IDENTITY_OK", "ENV_RAILS_POLICY_OK", "JSON_CANONICAL_CHECK_OK", "EVIDENCE_PATH_PROOFS_OK"]}
    boundary = _boundary(mapped, produced_at, common)
    return {PROOF: proof_bytes_1, TWO_RUN: canonical_json_bytes(two_run), PAIR_ORDER: canonical_json_bytes(pair_order), BOUNDARY: canonical_json_bytes(boundary)}


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
        raise SystemExit("STALE_HDE_EPIC037_PR04_V2_TO_COMPAT:" + ",".join(stale))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate HDE-EPIC037 PR-04 v2 adapter-to-compat evidence")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        enforce_closed_rails()
    except DeterminismEnvError as exc:
        raise SystemExit(f"HDE_EPIC037_PR04_CLOSED_RAILS_REQUIRED:{exc}") from exc
    produced_at = _existing_generated_at(PROOF) if args.check else None
    if produced_at is None:
        produced_at = _isoformat(_dt.datetime.now(tz=_dt.timezone.utc))
    write_outputs(build_outputs(produced_at), produced_at=produced_at, check=args.check)
    print("checked HDE-EPIC037 PR-04 v2-to-compat artifacts" if args.check else "generated HDE-EPIC037 PR-04 v2-to-compat artifacts")


if __name__ == "__main__":
    main()
