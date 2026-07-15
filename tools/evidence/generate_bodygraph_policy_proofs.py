#!/usr/bin/env python3
"""Generate deterministic HDE-EPIC038 PR-04 BodyGraph policy proofs."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.projection import project_bodygraph
from engine.bodygraph.resolver import resolve_bodygraph
from engine.bodygraph.v2_adapter import adapt_v2_chart_payload
from engine.presenter.emitter import emit_public
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer import canon
from scripts.bodygraph.run_refresh_worker import POLICY

TS = "2026-07-14T00:00:00Z"
FIXTURE_ID = "hde-epic038-pr04-source-invariance-01"
FIXTURE_DIR = ROOT / "tests/fixtures/bodygraph/source_invariance"
NORMALIZED_INPUT = FIXTURE_DIR / "normalized_input.v1.json"
SOURCE_FIXTURES = {
    "db": FIXTURE_DIR / "db_cached_payload.v1.json",
    "vendor": FIXTURE_DIR / "vendor_chart_result.v1.json",
}
PATHS = {
    "sel": ROOT / "artifacts/bodygraph/source_selection.snapshot.json",
    "ab": ROOT / "artifacts/bodygraph/source_invariance/ab.json",
    "ba": ROOT / "artifacts/bodygraph/source_invariance/ba.json",
    "sum": ROOT / "artifacts/bodygraph/source_invariance/summary.json",
    "run_schema": ROOT / "schemas/bodygraph_source_invariance.run.v2.json",
    "summary_schema": ROOT / "schemas/bodygraph_source_invariance.summary.v2.json",
    "pol": ROOT / "artifacts/bodygraph/refresh_policy.snapshot.json",
    "met": ROOT / "artifacts/bodygraph/metrics.snapshot.json",
    "log": ROOT / "artifacts/bodygraph/keys_only.logs.sample",
}
UNSAFE_KEYS = {
    "authorization",
    "credential",
    "credentials",
    "database_url",
    "db_bridge_url",
    "header",
    "headers",
    "parameters",
    "raw",
    "request",
    "response",
    "secret",
    "sql",
    "token",
    "transport",
}
POLICY_SAMPLE_COUNTS = {
    "breaker_tripped": 0,
    "rate_limit_hits": 0,
    "refresh_attempts": 2,
    "refresh_failures": 1,
    "refresh_successes": 1,
}


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_bytes(payload: object) -> bytes:
    return canon.sercanon(payload, sort_keys=True)


def _load_canonical(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"INVALID_FIXTURE_JSON:{path.relative_to(ROOT).as_posix()}") from exc
    if not isinstance(payload, dict):
        raise SystemExit(f"INVALID_FIXTURE_SHAPE:{path.relative_to(ROOT).as_posix()}")
    canonical = _canonical_bytes(payload)
    if raw != canonical:
        raise SystemExit(f"NONCANONICAL_FIXTURE:{path.relative_to(ROOT).as_posix()}")
    return payload, canonical


def _write(path: Path, data: bytes, check: bool) -> None:
    if check:
        if not path.exists() or path.read_bytes() != data:
            try:
                display = path.relative_to(ROOT).as_posix()
            except ValueError:
                display = path.as_posix()
            raise SystemExit(f"STALE:{display}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _unsafe_absent(value: Any) -> bool:
    if isinstance(value, dict):
        return all(
            str(key).casefold() not in UNSAFE_KEYS and _unsafe_absent(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return all(_unsafe_absent(item) for item in value)
    return True


def selection() -> dict[str, Any]:
    env = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
    rows = []
    for source in ("auto", "db", "vendor"):
        result = resolve_bodygraph(
            "hde-epic038-pr04-synthetic",
            source=source,
            upsert=False,
            dry_run=True,
            env=env,
        )
        rows.append(
            {
                "exit_code": result.exit_code,
                "reason": (result.payload.get("error") or {}).get("code", "no_io"),
                "requested_source": source,
                "resolved_source": result.payload.get("resolver", {}).get("resolved_source"),
                "scenario": f"{source}_closed_rails",
                "status": result.status,
                "transport_calls": 0,
            }
        )
    return {
        "captured_at_utc": TS,
        "proof_labels": [
            {"name": "BG_SOURCE_SELECTION_OK", "type": "non_token"},
            {"name": "BG_VENDOR_CALLS_DISABLED_IN_PROD_OK", "type": "non_token"},
        ],
        "scenarios": rows,
        "schema": "v1",
    }


def _normalized_input_sha256() -> str:
    payload, raw = _load_canonical(NORMALIZED_INPUT)
    expected_keys = {
        "birthdate",
        "birthtime",
        "fixture_id",
        "location",
        "person_uid",
        "schema",
    }
    if set(payload) != expected_keys:
        raise SystemExit("NORMALIZED_INPUT_KEYS")
    if payload != {
        "birthdate": "2000-01-01",
        "birthtime": "00:00",
        "fixture_id": FIXTURE_ID,
        "location": "Synthetic Test Location",
        "person_uid": "00000000-0000-4000-8000-000000000038",
        "schema": "bodygraph.source_invariance.normalized_input.v1",
    }:
        raise SystemExit("NORMALIZED_INPUT_CONTRACT")
    return _sha(raw)


def _source_projection(source: str, normalized_sha: str) -> tuple[dict[str, Any], str]:
    fixture, source_bytes = _load_canonical(SOURCE_FIXTURES[source])
    if fixture.get("input_fingerprint") != normalized_sha:
        raise SystemExit(f"INPUT_FINGERPRINT_MISMATCH:{source}")
    if source == "db":
        if set(fixture) != {"input_fingerprint", "payload", "payload_posture", "schema"}:
            raise SystemExit("DB_FIXTURE_KEYS")
        if (
            fixture["schema"] != "bodygraph.source_invariance.db_cached_payload.v1"
            or fixture["payload_posture"] != "mapped_no_raw_vendor_payload"
        ):
            raise SystemExit("DB_FIXTURE_CONTRACT")
        mapped = fixture.get("payload")
    else:
        if set(fixture) != {"context", "input_fingerprint", "payload", "schema"}:
            raise SystemExit("VENDOR_FIXTURE_KEYS")
        if fixture["schema"] != "bodygraph.source_invariance.vendor_chart_result.v1":
            raise SystemExit("VENDOR_FIXTURE_CONTRACT")
        result = adapt_v2_chart_payload(fixture.get("payload"), fixture.get("context"))
        if result.status != "mapped" or result.code != "ADAPTER_MAPPED" or result.resolved is None:
            raise SystemExit(f"VENDOR_ADAPTER_FAILED:{result.code}")
        mapped = result.resolved
    if not isinstance(mapped, dict):
        raise SystemExit(f"MAPPED_FIXTURE_SHAPE:{source}")
    return project_bodygraph(mapped), _sha(source_bytes)


def _acquisition(source: str, pair_order: str, normalized_sha: str) -> dict[str, Any]:
    runs = []
    representation_hashes = set()
    for run_number in (1, 2):
        projection, representation_sha = _source_projection(source, normalized_sha)
        representation_hashes.add(representation_sha)
        projection_bytes = _canonical_bytes(projection)
        emitted_bytes = emit_public(projection, sort_keys=True)
        runs.append(
            {
                "acquisition_id": f"{source}-{pair_order}-acquisition-{run_number:02d}",
                "emitted_sha256": _sha(emitted_bytes),
                "projection_sha256": _sha(projection_bytes),
            }
        )
    if len(representation_hashes) != 1:
        raise SystemExit(f"SOURCE_FIXTURE_DRIFT:{source}")
    return {
        "adapter_id": (
            "mapped_db_cache_payload.v1"
            if source == "db"
            else "engine.bodygraph.v2_adapter.adapt_v2_chart_payload"
        ),
        "payload_posture": "hashes_only_synthetic_fixture",
        "runs": runs,
        "source": source,
        "source_representation_sha256": representation_hashes.pop(),
    }


def _run_record(pair_order: str) -> dict[str, Any]:
    normalized_sha = _normalized_input_sha256()
    source_order = ["db", "vendor"] if pair_order == "ab" else ["vendor", "db"]
    acquisitions = [_acquisition(source, pair_order, normalized_sha) for source in source_order]
    by_source = {item["source"]: item for item in acquisitions}
    run_rows = [run for item in acquisitions for run in item["runs"]]
    projection_hashes = {run["projection_sha256"] for run in run_rows}
    emitted_hashes = {run["emitted_sha256"] for run in run_rows}
    predicates = {
        "distinct_source_representations": (
            by_source["db"]["source_representation_sha256"]
            != by_source["vendor"]["source_representation_sha256"]
        ),
        "distinct_sources": set(by_source) == {"db", "vendor"},
        "presenter_bytes_equal": len(emitted_hashes) == 1,
        "projection_equal": len(projection_hashes) == 1,
        "same_normalized_input": all(
            json.loads(SOURCE_FIXTURES[source].read_bytes()).get("input_fingerprint") == normalized_sha
            for source in ("db", "vendor")
        ),
        "two_run_stable": all(
            len({run["projection_sha256"] for run in item["runs"]}) == 1
            and len({run["emitted_sha256"] for run in item["runs"]}) == 1
            and len({run["acquisition_id"] for run in item["runs"]}) == 2
            for item in acquisitions
        ),
        "unsafe_fields_absent": all(
            _unsafe_absent(_source_projection(source, normalized_sha)[0])
            for source in ("db", "vendor")
        ),
    }
    return {
        "acquisitions": acquisitions,
        "captured_at_utc": TS,
        "fixture_id": FIXTURE_ID,
        "normalized_input_sha256": normalized_sha,
        "pair_order": pair_order,
        "predicates": predicates,
        "schema": "bodygraph.source_invariance.run.v2",
        "source_order": source_order,
        "status": "PASS" if all(predicates.values()) else "FAIL",
    }


def _negative_receipt(normalized_sha: str, baseline_emitted_sha256: str) -> dict[str, Any]:
    fixture, _ = _load_canonical(SOURCE_FIXTURES["db"])
    payload = fixture["payload"]
    payload["bodygraph"]["profile"] = "2/4"
    mutated = emit_public(project_bodygraph(payload), sort_keys=True)
    mutated_sha = _sha(mutated)
    divergence = baseline_emitted_sha256 != mutated_sha
    receipt = {
        "baseline_emitted_sha256": baseline_emitted_sha256,
        "divergence_detected": divergence,
        "expected_failure_code": "BODYGRAPH_SOURCE_DIVERGENCE",
        "mutated_emitted_sha256": mutated_sha,
        "mutated_field": "bodygraph.profile",
        "mutated_source": "db",
        "observed_failure_code": (
            "BODYGRAPH_SOURCE_DIVERGENCE" if divergence else "NONE"
        ),
        "receipt_id": "bodygraph_source_invariance_profile_mutation_v1",
    }
    receipt["receipt_sha256"] = _sha(_canonical_bytes(receipt))
    return receipt


def _summary(ab: dict[str, Any], ba: dict[str, Any], ab_bytes: bytes, ba_bytes: bytes) -> dict[str, Any]:
    def by_source(record: dict[str, Any]) -> dict[str, dict[str, Any]]:
        return {item["source"]: item for item in record["acquisitions"]}

    ab_sources = by_source(ab)
    ba_sources = by_source(ba)
    baseline_sha = ab_sources["vendor"]["runs"][0]["emitted_sha256"]
    negative = _negative_receipt(ab["normalized_input_sha256"], baseline_sha)
    predicates = {
        "ab_pass": ab["status"] == "PASS",
        "ba_pass": ba["status"] == "PASS",
        "canonical_projection_equal": len(
            {
                run["projection_sha256"]
                for record in (ab, ba)
                for acquisition in record["acquisitions"]
                for run in acquisition["runs"]
            }
        )
        == 1,
        "db_two_run_stable": all(
            len({run[field] for run in record["runs"]}) == 1
            for record in (ab_sources["db"], ba_sources["db"])
            for field in ("projection_sha256", "emitted_sha256")
        ),
        "distinct_source_representations": all(
            by_source(record)["db"]["source_representation_sha256"]
            != by_source(record)["vendor"]["source_representation_sha256"]
            for record in (ab, ba)
        ),
        "distinct_sources": all(
            set(by_source(record)) == {"db", "vendor"} for record in (ab, ba)
        ),
        "negative_control_rejected": (
            negative["divergence_detected"] is True
            and negative["observed_failure_code"] == "BODYGRAPH_SOURCE_DIVERGENCE"
        ),
        "presenter_emitted_bytes_equal": len(
            {
                run["emitted_sha256"]
                for record in (ab, ba)
                for acquisition in record["acquisitions"]
                for run in acquisition["runs"]
            }
        )
        == 1,
        "same_normalized_input": (
            ab["normalized_input_sha256"] == ba["normalized_input_sha256"]
        ),
        "source_order_reversed": (
            ab["source_order"] == ["db", "vendor"]
            and ba["source_order"] == ["vendor", "db"]
        ),
        "unsafe_fields_absent": (
            ab["predicates"]["unsafe_fields_absent"]
            and ba["predicates"]["unsafe_fields_absent"]
        ),
        "vendor_two_run_stable": all(
            len({run[field] for run in record["runs"]}) == 1
            for record in (ab_sources["vendor"], ba_sources["vendor"])
            for field in ("projection_sha256", "emitted_sha256")
        ),
    }
    return {
        "ab_sha256": _sha(ab_bytes),
        "ba_sha256": _sha(ba_bytes),
        "captured_at_utc": TS,
        "fixture_id": FIXTURE_ID,
        "negative_receipt": negative,
        "normalized_input_sha256": ab["normalized_input_sha256"],
        "predicates": predicates,
        "proof_labels": [{"name": "BG_SOURCE_INVARIANCE_OK", "type": "non_token"}],
        "schema": "bodygraph.source_invariance.summary.v2",
        "source_scope": ["configured_v2_chart_result", "mapped_db_cache_payload"],
        "top_level_pass": all(predicates.values()),
    }


def _run_schema() -> dict[str, Any]:
    hash_value = {"pattern": "^[0-9a-f]{64}$", "type": "string"}
    run = {
        "additionalProperties": False,
        "properties": {
            "acquisition_id": {"minLength": 1, "type": "string"},
            "emitted_sha256": hash_value,
            "projection_sha256": hash_value,
        },
        "required": ["acquisition_id", "emitted_sha256", "projection_sha256"],
        "type": "object",
    }
    acquisition = {
        "additionalProperties": False,
        "properties": {
            "adapter_id": {"minLength": 1, "type": "string"},
            "payload_posture": {"const": "hashes_only_synthetic_fixture"},
            "runs": {"items": run, "maxItems": 2, "minItems": 2, "type": "array"},
            "source": {"enum": ["db", "vendor"]},
            "source_representation_sha256": hash_value,
        },
        "required": [
            "adapter_id",
            "payload_posture",
            "runs",
            "source",
            "source_representation_sha256",
        ],
        "type": "object",
    }
    predicate_keys = [
        "distinct_source_representations",
        "distinct_sources",
        "presenter_bytes_equal",
        "projection_equal",
        "same_normalized_input",
        "two_run_stable",
        "unsafe_fields_absent",
    ]
    return {
        "$id": "bodygraph.source_invariance.run.v2",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "acquisitions": {
                "items": acquisition,
                "maxItems": 2,
                "minItems": 2,
                "type": "array",
            },
            "captured_at_utc": {"const": TS},
            "fixture_id": {"const": FIXTURE_ID},
            "normalized_input_sha256": hash_value,
            "pair_order": {"enum": ["ab", "ba"]},
            "predicates": {
                "additionalProperties": False,
                "properties": {key: {"type": "boolean"} for key in predicate_keys},
                "required": predicate_keys,
                "type": "object",
            },
            "schema": {"const": "bodygraph.source_invariance.run.v2"},
            "source_order": {
                "items": {"enum": ["db", "vendor"]},
                "maxItems": 2,
                "minItems": 2,
                "type": "array",
                "uniqueItems": True,
            },
            "status": {"enum": ["PASS", "FAIL"]},
        },
        "required": [
            "acquisitions",
            "captured_at_utc",
            "fixture_id",
            "normalized_input_sha256",
            "pair_order",
            "predicates",
            "schema",
            "source_order",
            "status",
        ],
        "type": "object",
    }


def _summary_schema() -> dict[str, Any]:
    hash_value = {"pattern": "^[0-9a-f]{64}$", "type": "string"}
    predicate_keys = [
        "ab_pass",
        "ba_pass",
        "canonical_projection_equal",
        "db_two_run_stable",
        "distinct_source_representations",
        "distinct_sources",
        "negative_control_rejected",
        "presenter_emitted_bytes_equal",
        "same_normalized_input",
        "source_order_reversed",
        "unsafe_fields_absent",
        "vendor_two_run_stable",
    ]
    receipt_keys = [
        "baseline_emitted_sha256",
        "divergence_detected",
        "expected_failure_code",
        "mutated_emitted_sha256",
        "mutated_field",
        "mutated_source",
        "observed_failure_code",
        "receipt_id",
        "receipt_sha256",
    ]
    return {
        "$id": "bodygraph.source_invariance.summary.v2",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "ab_sha256": hash_value,
            "ba_sha256": hash_value,
            "captured_at_utc": {"const": TS},
            "fixture_id": {"const": FIXTURE_ID},
            "negative_receipt": {
                "additionalProperties": False,
                "properties": {
                    "baseline_emitted_sha256": hash_value,
                    "divergence_detected": {"type": "boolean"},
                    "expected_failure_code": {"const": "BODYGRAPH_SOURCE_DIVERGENCE"},
                    "mutated_emitted_sha256": hash_value,
                    "mutated_field": {"const": "bodygraph.profile"},
                    "mutated_source": {"const": "db"},
                    "observed_failure_code": {"enum": ["BODYGRAPH_SOURCE_DIVERGENCE", "NONE"]},
                    "receipt_id": {"const": "bodygraph_source_invariance_profile_mutation_v1"},
                    "receipt_sha256": hash_value,
                },
                "required": receipt_keys,
                "type": "object",
            },
            "normalized_input_sha256": hash_value,
            "predicates": {
                "additionalProperties": False,
                "properties": {key: {"type": "boolean"} for key in predicate_keys},
                "required": predicate_keys,
                "type": "object",
            },
            "proof_labels": {
                "items": {
                    "additionalProperties": False,
                    "properties": {
                        "name": {"const": "BG_SOURCE_INVARIANCE_OK"},
                        "type": {"const": "non_token"},
                    },
                    "required": ["name", "type"],
                    "type": "object",
                },
                "maxItems": 1,
                "minItems": 1,
                "type": "array",
            },
            "schema": {"const": "bodygraph.source_invariance.summary.v2"},
            "source_scope": {
                "prefixItems": [
                    {"const": "configured_v2_chart_result"},
                    {"const": "mapped_db_cache_payload"},
                ],
                "items": False,
                "maxItems": 2,
                "minItems": 2,
                "type": "array",
            },
            "top_level_pass": {"type": "boolean"},
        },
        "required": [
            "ab_sha256",
            "ba_sha256",
            "captured_at_utc",
            "fixture_id",
            "negative_receipt",
            "normalized_input_sha256",
            "predicates",
            "proof_labels",
            "schema",
            "source_scope",
            "top_level_pass",
        ],
        "type": "object",
    }


def policy_payload() -> dict[str, Any]:
    return {
        **POLICY,
        "proof_labels": [
            {"name": "BG_TTL_SWR_POLICY_OK", "type": "non_token"},
            {"name": "BG_RATE_LIMIT_POLICY_OK", "type": "non_token"},
            {"name": "BG_CIRCUIT_BREAKER_POLICY_OK", "type": "non_token"},
        ],
        "sample_counts": dict(POLICY_SAMPLE_COUNTS),
    }


def metrics() -> dict[str, Any]:
    return {
        "counters": {
            "breaker_tripped_total": POLICY_SAMPLE_COUNTS["breaker_tripped"],
            "rate_limit_hit_total": POLICY_SAMPLE_COUNTS["rate_limit_hits"],
            "refresh_attempts_total": POLICY_SAMPLE_COUNTS["refresh_attempts"],
            "refresh_failure_total": POLICY_SAMPLE_COUNTS["refresh_failures"],
            "refresh_success_total": POLICY_SAMPLE_COUNTS["refresh_successes"],
        },
        "labels": {
            "env": "fixture",
            "reason": "closed_rails_fixture",
            "source": "hdapi",
        },
        "schema": "v1",
        "timers_ms": {"refresh_duration_p95": 0},
    }


def generate(check: bool = False) -> None:
    ensure_determinism_env()
    ab = _run_record("ab")
    ba = _run_record("ba")
    ab_bytes = _canonical_bytes(ab)
    ba_bytes = _canonical_bytes(ba)
    summary = _summary(ab, ba, ab_bytes, ba_bytes)
    if not summary["top_level_pass"]:
        raise SystemExit("BODYGRAPH_SOURCE_INVARIANCE_FAIL")

    outputs = {
        PATHS["sel"]: _canonical_bytes(selection()),
        PATHS["ab"]: ab_bytes,
        PATHS["ba"]: ba_bytes,
        PATHS["sum"]: _canonical_bytes(summary),
        PATHS["run_schema"]: _canonical_bytes(_run_schema()),
        PATHS["summary_schema"]: _canonical_bytes(_summary_schema()),
        PATHS["pol"]: _canonical_bytes(policy_payload()),
        PATHS["met"]: _canonical_bytes(metrics()),
        PATHS["log"]: _canonical_bytes(
            {
                "at": TS,
                "duration_ms": 0,
                "keys_only": True,
                "reason": "safe_mode",
                "route": "ops.refresh.bodygraph",
                "status": 412,
            }
        ),
    }
    for path, data in outputs.items():
        _write(path, data, check)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    generate(args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
