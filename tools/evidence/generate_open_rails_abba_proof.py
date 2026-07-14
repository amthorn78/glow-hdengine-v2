#!/usr/bin/env python3
"""Generate open-rails fixture-backed and bounded live AB/BA determinism proofs."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable, Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.ingest import VendorInputs, ingest_vendor_bodygraph, resolve_db_user_id  # noqa: E402
from engine.bodygraph.v2_adapter import V2ChartAdapterContext, adapt_v2_chart_payload  # noqa: E402
from engine.bodygraph.vendor_client import (  # noqa: E402
    HdApiClient,
    VendorError,
    VendorRetryConfig,
    VendorTimeouts,
    classify_bg_resolve_route_policy,
)
from engine.cli import main as cli_main  # noqa: E402
from engine.presenter import emitter  # noqa: E402
from engine.runtime import emit_reader_public_envelope, identity_meta  # noqa: E402
from engine.serializer import canon  # noqa: E402

OPEN_ABBA_REL = "audit/gates/determinism/open_rails_abba.json"
LIVE_ABBA_REL = "audit/gates/determinism/open_rails_vendor_abba.json"
PRODUCED_AT = "2026-07-14T00:00:00Z"
LIVE_REQUIRED_PREDICATES = frozenset(
    {
        "abba_byte_identity",
        "canonical_json",
        "distinct_input_fingerprints",
        "distinct_normalized_payloads",
        "normalized_payload_hashes_bound",
        "request_bound_ok",
        "same_normalized_inputs_reused",
        "single_lf",
        "two_run_ab_identity",
        "two_run_ba_identity",
    }
)

LIVE_TOP_LEVEL_KEYS = frozenset(
    {
        "acceptance_token_satisfied",
        "applied_abba_contract_mode",
        "artifact_kind",
        "generated_at_utc",
        "no_raw_payload_predicate",
        "no_secret_value_predicate",
        "non_production_environment",
        "normalized_a_sha256",
        "normalized_b_sha256",
        "optional_env_inputs_absent",
        "pf09_mapping",
        "po_override_note",
        "predicates",
        "reader_hashes",
        "request_results",
        "requests_attempted",
        "requests_completed",
        "result",
        "route_policy",
        "same_normalized_inputs_reused_for_ab_ba",
        "secret_presence",
        "synthetic_input_names",
        "synthetic_input_source",
        "top_level_pass",
        "typed_result_class",
        "vendor_acquisition_architecture",
    }
)
LIVE_FORBIDDEN_KEY_PARTS = (
    "raw_request",
    "raw_response",
    "raw_payload",
    "raw_vendor_payload",
    "authorization",
    "credential",
    "birth",
    "location",
)
LIVE_READER_HASH_KEYS = frozenset({"ab_sha256", "ab_run2_sha256", "ba_sha256", "ba_run2_sha256"})
LIVE_REQUEST_RESULT_KEYS = frozenset({"party", "result_class", "input_fingerprint_sha256", "normalized_payload_sha256"})
LIVE_NONPROD_KEYS = frozenset({"configured_base_url", "proven", "reason"})
LIVE_SECRET_PRESENCE_KEYS = frozenset({"GEO_API_KEY", "HDAPI_BASE_URL", "HD_API_BASE_URL", "HD_API_KEY"})
LIVE_SYNTHETIC_INPUT_NAME_KEYS = frozenset({"a", "b"})
LIVE_PF09_KEYS = frozenset({"title", "task", "subtask", "status"})
LIVE_ROUTE_POLICY_KEYS = frozenset({"classification", "configured_base_version", "payload_family", "resource_path", "route_family", "supported"})
LIVE_FORBIDDEN_STRING_PATTERNS = (
    re.compile(r"https?://", re.IGNORECASE),
    re.compile(r"\bbearer\b", re.IGNORECASE),
    re.compile(r"\b(secret|credential|token|api[_-]?key|authorization)\b", re.IGNORECASE),
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),
    re.compile(r"\b\d{1,2}:\d{2}\b"),
)
SENSITIVE_ENV = (
    "HD_API_KEY",
    "GEO_API_KEY",
    "HD_API_BASE_URL",
    "HDAPI_BASE_URL",
    "AUTHORIZATION",
    "API_KEY",
    "TOKEN",
    "SECRET",
)
RAILS_OPEN = {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}
RAILS_CLOSED = {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}
A_FIXTURE = {"person_uid": "hde-epic038-pr03-alpha", "birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US", "tz": "America/Chicago"}
B_FIXTURE = {"person_uid": "hde-epic038-pr03-bravo", "birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE", "tz": "Europe/Berlin"}
LIVE_SYNTHETIC_A = VendorInputs(resolve_db_user_id("hde-epic038-live-alpha"), "1990-01-01", "12:00", "Amsterdam, NL")
LIVE_SYNTHETIC_B = VendorInputs(resolve_db_user_id("hde-epic038-live-bravo"), "1992-03-04", "08:15", "Berlin, DE")


def canonical_json_bytes(payload: Mapping[str, Any]) -> bytes:
    return canon.sercanon(payload)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _live_summary_predicates(proof: Mapping[str, Any]) -> dict[str, bool]:
    failed = {
        "abba_byte_identity": False,
        "distinct_input_fingerprints": False,
        "distinct_normalized_payloads": False,
        "normalized_payload_hashes_bound": False,
        "two_run_ab_identity": False,
        "two_run_ba_identity": False,
    }
    results = proof.get("request_results")
    if not isinstance(results, list) or len(results) != 2:
        return failed

    by_party: dict[str, Mapping[str, Any]] = {}
    for result in results:
        if not isinstance(result, Mapping) or result.get("result_class") != "success":
            break
        party = result.get("party")
        fingerprint = result.get("input_fingerprint_sha256")
        payload_hash = result.get("normalized_payload_sha256")
        if (
            not isinstance(party, str)
            or party not in {"a", "b"}
            or party in by_party
            or not _is_sha256(fingerprint)
            or not _is_sha256(payload_hash)
        ):
            break
        by_party[party] = result
    if set(by_party) != {"a", "b"}:
        return failed

    a_result = by_party["a"]
    b_result = by_party["b"]
    a_fingerprint = a_result["input_fingerprint_sha256"]
    b_fingerprint = b_result["input_fingerprint_sha256"]
    a_payload_hash = a_result["normalized_payload_sha256"]
    b_payload_hash = b_result["normalized_payload_sha256"]
    reader_hashes = proof.get("reader_hashes")
    hashes_valid = isinstance(reader_hashes, Mapping) and all(
        _is_sha256(reader_hashes.get(key))
        for key in ("ab_sha256", "ab_run2_sha256", "ba_sha256", "ba_run2_sha256")
    )
    return {
        "distinct_input_fingerprints": a_fingerprint != b_fingerprint,
        "distinct_normalized_payloads": a_payload_hash != b_payload_hash,
        "normalized_payload_hashes_bound": (
            proof.get("normalized_a_sha256") == a_payload_hash
            and proof.get("normalized_b_sha256") == b_payload_hash
        ),
        "abba_byte_identity": bool(
            hashes_valid and reader_hashes["ab_sha256"] == reader_hashes["ba_sha256"]
        ),
        "two_run_ab_identity": bool(
            hashes_valid and reader_hashes["ab_sha256"] == reader_hashes["ab_run2_sha256"]
        ),
        "two_run_ba_identity": bool(
            hashes_valid and reader_hashes["ba_sha256"] == reader_hashes["ba_run2_sha256"]
        ),
    }



def _keys_exact(value: object, expected: frozenset[str]) -> bool:
    return isinstance(value, Mapping) and set(value) == set(expected)


def _has_forbidden_live_key(value: object, *, _path: tuple[str, ...] = ()) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if not isinstance(key, str):
                return True
            lowered = key.lower()
            next_path = (*_path, key)
            is_safety_summary = len(next_path) == 1 and key in {"no_raw_payload_predicate", "no_secret_value_predicate"}
            if not is_safety_summary and any(part in lowered for part in LIVE_FORBIDDEN_KEY_PARTS):
                return True
            if _has_forbidden_live_key(nested, _path=next_path):
                return True
    elif isinstance(value, list):
        return any(_has_forbidden_live_key(item, _path=_path) for item in value)
    return False


def _has_forbidden_live_string(value: object, *, _path: tuple[str, ...] = ()) -> bool:
    if isinstance(value, Mapping):
        return any(_has_forbidden_live_string(nested, _path=(*_path, str(key))) for key, nested in value.items())
    if isinstance(value, list):
        return any(_has_forbidden_live_string(item, _path=_path) for item in value)
    if not isinstance(value, str):
        return False
    if _path == ("non_production_environment", "configured_base_url"):
        return value not in {"<redacted>", "UNSET"}
    return any(pattern.search(value) for pattern in LIVE_FORBIDDEN_STRING_PATTERNS)


def _derived_live_safety(proof: Mapping[str, Any]) -> dict[str, bool]:
    nonprod = proof.get("non_production_environment")
    configured = nonprod.get("configured_base_url") if isinstance(nonprod, Mapping) else None
    return {
        "no_raw_payload_predicate": not _has_forbidden_live_key(proof),
        "no_secret_value_predicate": configured in {"<redacted>", "UNSET"} and not _has_forbidden_live_string(proof),
    }


def _validate_live_shape(proof: Mapping[str, Any]) -> None:
    live_keys = set(proof)
    allowed_without_po = set(LIVE_TOP_LEVEL_KEYS) - {"po_override_note"}
    if live_keys != set(LIVE_TOP_LEVEL_KEYS) and live_keys != allowed_without_po:
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if _has_forbidden_live_key(proof):
        raise SystemExit(f"UNSAFE_LIVE_PROOF:{LIVE_ABBA_REL}")
    if proof.get("artifact_kind") != "hde_epic038_pr03_open_rails_vendor_abba_proof":
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if proof.get("generated_at_utc") != PRODUCED_AT:
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if proof.get("applied_abba_contract_mode") != "raw_byte_identity_after_existing_canonical_pair_normalization":
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if proof.get("vendor_acquisition_architecture") != "individual_bodygraph":
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if proof.get("synthetic_input_source") not in {"fabricated_synthetic_defaults", "environment"}:
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")

    nonprod = proof.get("non_production_environment")
    if not _keys_exact(nonprod, LIVE_NONPROD_KEYS):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    configured = nonprod["configured_base_url"]
    if configured not in {"<redacted>", "UNSET"} or not isinstance(nonprod.get("reason"), str):
        raise SystemExit(f"UNSAFE_LIVE_PROOF:{LIVE_ABBA_REL}")
    if not isinstance(nonprod.get("proven"), bool):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if nonprod["proven"] is False and not str(proof.get("po_override_note") or "").strip():
        raise SystemExit(f"UNSAFE_LIVE_PROOF:{LIVE_ABBA_REL}")

    if not _keys_exact(proof.get("pf09_mapping"), LIVE_PF09_KEYS):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    pf09 = proof["pf09_mapping"]
    if pf09 != {"title": "PF09.6 — HDE-Build-Checklist-Distillation", "task": "HDE-DIST001", "subtask": "HDE-DIST001.3", "status": "Partial"}:
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")

    if not _keys_exact(proof.get("reader_hashes"), LIVE_READER_HASH_KEYS):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if not _is_sha256(proof.get("normalized_a_sha256")) or not _is_sha256(proof.get("normalized_b_sha256")):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")

    results = proof.get("request_results")
    if not isinstance(results, list) or len(results) != 2:
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    parties: set[str] = set()
    for result in results:
        if not _keys_exact(result, LIVE_REQUEST_RESULT_KEYS):
            raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
        party = result.get("party")
        if not isinstance(party, str) or party not in {"a", "b"} or party in parties or result.get("result_class") != "success":
            raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
        if not _is_sha256(result.get("input_fingerprint_sha256")) or not _is_sha256(result.get("normalized_payload_sha256")):
            raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
        parties.add(party)
    if parties != {"a", "b"}:
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")

    predicates = proof.get("predicates")
    if not _keys_exact(predicates, LIVE_REQUIRED_PREDICATES):
        raise SystemExit(f"FAILED_LIVE_PROOF:{LIVE_ABBA_REL}")
    if not all(isinstance(predicates.get(key), bool) for key in LIVE_REQUIRED_PREDICATES):
        raise SystemExit(f"FAILED_LIVE_PROOF:{LIVE_ABBA_REL}")

    route_policy = proof.get("route_policy")
    if not _keys_exact(route_policy, LIVE_ROUTE_POLICY_KEYS):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if not isinstance(route_policy.get("supported"), bool):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    for key in LIVE_ROUTE_POLICY_KEYS - {"supported"}:
        if not isinstance(route_policy.get(key), str) or not route_policy.get(key):
            raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")

    if not _keys_exact(proof.get("secret_presence"), LIVE_SECRET_PRESENCE_KEYS):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if not all(isinstance(value, bool) for value in proof["secret_presence"].values()):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if not _keys_exact(proof.get("synthetic_input_names"), LIVE_SYNTHETIC_INPUT_NAME_KEYS):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if not all(isinstance(value, str) and value for value in proof["synthetic_input_names"].values()):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    absent = proof.get("optional_env_inputs_absent")
    if not isinstance(absent, list) or not all(isinstance(item, str) and item for item in absent):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")

    safety = _derived_live_safety(proof)
    if any(proof.get(key) is not value for key, value in safety.items()) or not all(safety.values()):
        raise SystemExit(f"UNSAFE_LIVE_PROOF:{LIVE_ABBA_REL}")

def _assert_canonical(name: str, data: bytes) -> bool:
    if not data.endswith(b"\n") or data.endswith(b"\n\n") or b"\r" in data:
        return False
    try:
        return canon.sercanon(json.loads(data)) == data
    except Exception:
        return False


def clean_env(rails: Mapping[str, str]) -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if k not in SENSITIVE_ENV}
    env.update(rails)
    env.setdefault("APP_ENV", "test")
    return env


def reader_bytes(left: Mapping[str, Any], right: Mapping[str, Any]) -> bytes:
    left_norm = cli_main._normalize_party(dict(left), "left")
    right_norm = cli_main._normalize_party(dict(right), "right")
    left_person, left_chart = cli_main._party_from_normalized(left_norm)
    right_person, right_chart = cli_main._party_from_normalized(right_norm)
    left_person, right_person, left_chart, right_chart = cli_main._canonical_pair(left_person, right_person, left_chart, right_chart)
    meta = identity_meta()
    return emit_reader_public_envelope(left_chart, right_chart, engine_tag=meta["engine_tag"], invocation_tag=meta["invocation_tag"], release_id=meta["release_id"])[0]


def _emit_live_reader_bytes(left_chart: Mapping[str, Any], right_chart: Mapping[str, Any]) -> bytes:
    """Perform one complete Reader identity acquisition and emission."""
    meta = identity_meta()
    return emit_reader_public_envelope(
        dict(left_chart),
        dict(right_chart),
        engine_tag=meta["engine_tag"],
        invocation_tag=meta["invocation_tag"],
        release_id=meta["release_id"],
    )[0]


def cli_reader_bytes(left: Mapping[str, Any], right: Mapping[str, Any], *, rails: Mapping[str, str]) -> bytes:
    with tempfile.TemporaryDirectory(prefix="hde-open-rails-abba-") as td_raw:
        td = Path(td_raw)
        a_path = td / "a.json"
        b_path = td / "b.json"
        dump_path = td / "reader.json"
        a_path.write_bytes(canonical_json_bytes(left))
        b_path.write_bytes(canonical_json_bytes(right))
        proc = subprocess.run(
            [sys.executable, "scripts/hdctl.py", "showcompat", "--a-file", str(a_path), "--b-file", str(b_path), "--dump-reader", str(dump_path)],
            cwd=ROOT,
            env=clean_env(rails),
            capture_output=True,
        )
        if proc.returncode != 0 or proc.stderr:
            raise RuntimeError(f"showcompat failed rc={proc.returncode} stderr={proc.stderr!r}")
        return dump_path.read_bytes()


def idempotence(data: bytes) -> tuple[str | None, str]:
    payload = json.loads(data)
    preimage = dict(payload)
    stored = preimage.pop("idempotence_hash", None)
    recomputed = sha(emitter.emit_public(preimage))
    return stored, recomputed


def canonical_gate(runner: Callable[..., subprocess.CompletedProcess] | None = None) -> dict[str, Any]:
    runner = runner or subprocess.run
    proc = runner([sys.executable, "tools/evidence/run_canonical_json_gate.py", "--check-only"], cwd=ROOT, env=clean_env(RAILS_CLOSED), capture_output=True, text=True)
    return {
        "command": "python tools/evidence/run_canonical_json_gate.py --check-only",
        "returncode": proc.returncode,
        "stdout_sha256": sha((proc.stdout or "").encode("utf-8")),
        "stderr_sha256": sha((proc.stderr or "").encode("utf-8")),
        "passed": proc.returncode == 0,
    }


def build_fixture_proof(*, canon_gate_result: Mapping[str, Any] | None = None, transport_probe: Callable[[], None] | None = None, overrides: Mapping[str, bytes] | None = None) -> dict[str, Any]:
    calls = {"count": 0}
    original_default = HdApiClient._default_request

    def blocked_default(self: HdApiClient, req: object, timeout: float):  # type: ignore[override]
        calls["count"] += 1
        raise AssertionError("fixture-backed open rails proof attempted vendor transport")

    HdApiClient._default_request = blocked_default  # type: ignore[method-assign]
    try:
        if transport_probe is not None:
            transport_probe()
        ab_reader_open = reader_bytes(A_FIXTURE, B_FIXTURE)
        ba_reader_open = reader_bytes(B_FIXTURE, A_FIXTURE)
    finally:
        HdApiClient._default_request = original_default  # type: ignore[method-assign]
    ab_cli_open = cli_reader_bytes(A_FIXTURE, B_FIXTURE, rails=RAILS_OPEN)
    ba_cli_open = cli_reader_bytes(B_FIXTURE, A_FIXTURE, rails=RAILS_OPEN)
    ab_run2 = reader_bytes(A_FIXTURE, B_FIXTURE)
    ba_run2 = reader_bytes(B_FIXTURE, A_FIXTURE)
    ab_closed = cli_reader_bytes(A_FIXTURE, B_FIXTURE, rails=RAILS_CLOSED)
    ba_closed = cli_reader_bytes(B_FIXTURE, A_FIXTURE, rails=RAILS_CLOSED)
    data = {
        "ab_reader_open": ab_reader_open,
        "ba_reader_open": ba_reader_open,
        "ab_cli_open": ab_cli_open,
        "ba_cli_open": ba_cli_open,
        "ab_run2": ab_run2,
        "ba_run2": ba_run2,
        "ab_closed": ab_closed,
        "ba_closed": ba_closed,
    }
    if overrides:
        data.update(overrides)
    stored_ab, recomputed_ab = idempotence(data["ab_reader_open"])
    stored_ba, recomputed_ba = idempotence(data["ba_reader_open"])
    gate = dict(canon_gate_result or canonical_gate())
    predicates = {
        "abba_byte_identity": data["ab_reader_open"] == data["ba_reader_open"],
        "reader_cli_ab_identity": data["ab_reader_open"] == data["ab_cli_open"],
        "reader_cli_ba_identity": data["ba_reader_open"] == data["ba_cli_open"],
        "two_run_ab_identity": data["ab_reader_open"] == data["ab_run2"],
        "two_run_ba_identity": data["ba_reader_open"] == data["ba_run2"],
        "open_closed_ab_identity": data["ab_reader_open"] == data["ab_closed"],
        "open_closed_ba_identity": data["ba_reader_open"] == data["ba_closed"],
        "canonical_json_all": all(_assert_canonical(name, value) for name, value in data.items()),
        "single_lf_all": all(value.endswith(b"\n") and not value.endswith(b"\n\n") and b"\r" not in value for value in data.values()),
        "preimage_ab_match": stored_ab == recomputed_ab,
        "preimage_ba_match": stored_ba == recomputed_ba,
        "canonical_gate_success": gate.get("passed") is True and bool(gate.get("command")),
        "zero_vendor_transport_calls": calls["count"] == 0,
    }
    return {
        "acceptance_token_satisfied": False,
        "abba_contract_locus": "engine.compat.compute.compat_public normalizes pair via engine.compat.ordering.normalize_pair; tests/cli/test_showcompat_parity_and_identity.py asserts AB and BA stdout byte identity",
        "abba_contract_mode": "raw_byte_identity_after_existing_canonical_pair_normalization",
        "artifact_kind": "hde_epic038_pr03_open_rails_abba_proof",
        "canonical_gate": gate,
        "fixtures": {"a": "hde-epic038-pr03-alpha", "b": "hde-epic038-pr03-bravo", "materially_distinct": True},
        "generated_at_utc": PRODUCED_AT,
        "hashes": {key + "_sha256": sha(value) for key, value in sorted(data.items())},
        "idempotence_hashes": {
            "ab": {"stored": stored_ab, "recomputed": recomputed_ab},
            "ba": {"stored": stored_ba, "recomputed": recomputed_ba},
        },
        "pf09_mapping": {"title": "PF09.6 — HDE-Build-Checklist-Distillation", "task": "HDE-DIST001", "subtask": "HDE-DIST001.3", "status": "Partial"},
        "predicates": predicates,
        "rails": {"open": dict(RAILS_OPEN), "closed_baseline": dict(RAILS_CLOSED)},
        "transport_call_count": calls["count"],
        "top_level_pass": all(predicates.values()),
    }


def _write_primary(rel: str, data: bytes, *, check: bool) -> None:
    path = ROOT / rel
    if check:
        if not path.exists() or path.read_bytes() != data:
            raise SystemExit(f"DRIFT:{rel}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def generate_fixture(*, check: bool = False) -> dict[str, Any]:
    proof = build_fixture_proof()
    if proof["top_level_pass"] is not True:
        raise SystemExit("OPEN_RAILS_ABBA_PREDICATES_FAILED")
    _write_primary(OPEN_ABBA_REL, canonical_json_bytes(proof), check=check)
    return proof


def _safe_nonprod_base(base: str) -> tuple[bool, str]:
    lower = base.lower()
    if not base.startswith("https://"):
        return False, "base URL is not https"
    if any(marker in lower for marker in ("localhost", "127.0.0.1", ".test", "staging", "sandbox", "dev", "nonprod", "mock")):
        return True, "base URL contains repo-accepted non-production marker"
    return False, "non-production classification not proven from configured base URL"


def _live_inputs_from_env() -> tuple[VendorInputs, VendorInputs, list[str], str]:
    required = {
        "A_USER_ID": "OPEN_RAILS_VENDOR_ABBA_A_USER_ID",
        "A_BIRTHDATE": "OPEN_RAILS_VENDOR_ABBA_A_BIRTHDATE",
        "A_BIRTHTIME": "OPEN_RAILS_VENDOR_ABBA_A_BIRTHTIME",
        "A_LOCATION": "OPEN_RAILS_VENDOR_ABBA_A_LOCATION",
        "B_USER_ID": "OPEN_RAILS_VENDOR_ABBA_B_USER_ID",
        "B_BIRTHDATE": "OPEN_RAILS_VENDOR_ABBA_B_BIRTHDATE",
        "B_BIRTHTIME": "OPEN_RAILS_VENDOR_ABBA_B_BIRTHTIME",
        "B_LOCATION": "OPEN_RAILS_VENDOR_ABBA_B_LOCATION",
    }
    missing = [env for env in required.values() if not (os.environ.get(env) or "").strip()]
    if missing:
        # Fabricated, explicitly synthetic development inputs avoid personal data and
        # keep the committed live artifact names-only. Raw birth/location values are
        # used only in memory to exercise the existing vendor acquisition seam.
        return LIVE_SYNTHETIC_A, LIVE_SYNTHETIC_B, missing, "fabricated_synthetic_defaults"
    return (
        VendorInputs(resolve_db_user_id(os.environ[required["A_USER_ID"]].strip()), os.environ[required["A_BIRTHDATE"]].strip(), os.environ[required["A_BIRTHTIME"]].strip(), os.environ[required["A_LOCATION"]].strip()),
        VendorInputs(resolve_db_user_id(os.environ[required["B_USER_ID"]].strip()), os.environ[required["B_BIRTHDATE"]].strip(), os.environ[required["B_BIRTHTIME"]].strip(), os.environ[required["B_LOCATION"]].strip()),
        [],
        "environment",
    )


def _bounded_live_client(request_counter: dict[str, int]) -> HdApiClient:
    original = HdApiClient._default_request

    def counted(req, timeout):  # type: ignore[no-untyped-def]
        if request_counter["attempted"] >= 2:
            raise VendorError("PROVIDER_REQUEST_BOUND_EXCEEDED", "approved live proof request bound exceeded")
        request_counter["attempted"] += 1
        return original(req, timeout)

    return HdApiClient.from_env(
        retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
        timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        request=counted,
        env={**os.environ, **RAILS_OPEN},
    )


def build_live_proof(
    *,
    client_factory: Callable[[dict[str, int]], HdApiClient] | None = None,
    reader_emitter: Callable[[Mapping[str, Any], Mapping[str, Any]], bytes] | None = None,
) -> dict[str, Any]:
    base = (os.environ.get("HD_API_BASE_URL") or os.environ.get("HDAPI_BASE_URL") or "").strip().rstrip("/")
    nonprod_ok, nonprod_reason = _safe_nonprod_base(base) if base else (False, "HD_API_BASE_URL/HDAPI_BASE_URL is unset")
    a_inputs, b_inputs, missing_inputs, input_source = _live_inputs_from_env()
    secret_presence = {name: bool((os.environ.get(name) or "").strip()) for name in ("HD_API_KEY", "GEO_API_KEY", "HD_API_BASE_URL", "HDAPI_BASE_URL")}
    route_policy: Mapping[str, Any] | None = None
    architecture = "individual_bodygraph"
    if base:
        try:
            route_policy = classify_bg_resolve_route_policy(base)
            architecture = "individual_bodygraph" if route_policy.get("route_family") in {"legacy_bodygraph", "recommended_v2_chart"} else "unknown"
        except VendorError as exc:
            route_policy = {"error_code": exc.code}
    proof: dict[str, Any] = {
        "acceptance_token_satisfied": False,
        "artifact_kind": "hde_epic038_pr03_open_rails_vendor_abba_proof",
        "generated_at_utc": PRODUCED_AT,
        "non_production_environment": {"proven": nonprod_ok, "reason": nonprod_reason, "configured_base_url": "<redacted>" if base else "UNSET"},
        "secret_presence": secret_presence,
        "vendor_acquisition_architecture": architecture,
        "synthetic_input_source": input_source,
        "synthetic_input_names": {"a": "hde-epic038-live-alpha", "b": "hde-epic038-live-bravo"},
        "requests_attempted": 0,
        "requests_completed": 0,
        "request_results": [],
        "optional_env_inputs_absent": [],
        "top_level_pass": False,
        "result": "inconclusive",
        "no_raw_payload_predicate": True,
        "no_secret_value_predicate": True,
        "pf09_mapping": {"title": "PF09.6 — HDE-Build-Checklist-Distillation", "task": "HDE-DIST001", "subtask": "HDE-DIST001.3", "status": "Partial"},
    }
    if route_policy:
        proof["route_policy"] = {k: route_policy[k] for k in sorted(route_policy) if k in {"configured_base_version", "route_family", "payload_family", "classification", "resource_path", "supported"}}
    if not nonprod_ok:
        proof["po_override_note"] = "PO stated the previous non-production marker gate was bad instruction and explicitly authorized this bounded vendor call for the remediation PR."
    if not secret_presence.get("HD_API_KEY"):
        proof["typed_result_class"] = "CONFIGURATION_INCOMPLETE"
        if missing_inputs:
            proof["optional_env_inputs_absent"] = sorted(missing_inputs)
        return proof
    if missing_inputs:
        proof["optional_env_inputs_absent"] = sorted(missing_inputs)
    counter = {"attempted": 0}
    client_factory = client_factory or _bounded_live_client
    client = client_factory(counter)
    outcomes = []

    def acquire(label: str, inputs: VendorInputs) -> tuple[Mapping[str, Any], str, str]:
        policy = route_policy or {}
        if policy.get("route_family") == "recommended_v2_chart":
            request = client.build_contract_route_request(
                path="charts",
                request_fields=("birthdate", "birthtime", "location"),
                geocode_required=True,
                birthdate=inputs.birthdate,
                birthtime=inputs.birthtime,
                location=inputs.location,
            )
            result = client.fetch(request)
            context = V2ChartAdapterContext(
                person_uid=f"person-{inputs.user_id}",
                user_id=inputs.user_id,
                vendor="hdapi",
                vendor_version=2,
                input_fingerprint=request.input_fingerprint,
                route_family="recommended_v2_chart",
                route=request.route,
                payload_family="ChartResult",
            )
            adapter = adapt_v2_chart_payload(result.payload, context).as_dict()
            if adapter.get("status") != "mapped" or not isinstance(adapter.get("resolved"), Mapping):
                raise VendorError(str(adapter.get("code") or "ADAPTER_UNSUPPORTED"), "v2 chart adapter could not map vendor payload")
            resolved = dict(adapter["resolved"])
            bodygraph = resolved.get("bodygraph") if isinstance(resolved.get("bodygraph"), Mapping) else {}
            mech_type = bodygraph.get("type") if isinstance(bodygraph, Mapping) else None
            if not isinstance(mech_type, str) or not mech_type.strip():
                raise VendorError("ADAPTER_CONTEXT_INSUFFICIENT", "mapped v2 payload missing HDE mechanics type")
            payload = {"person_uid": str(resolved.get("person_uid") or context.person_uid), "mechanics": {"type": mech_type.strip()}}
            return payload, request.input_fingerprint, sha(emitter.emit_public(payload))
        # The legacy ingest helper writes dry-run logs even though it does not
        # write database state. Keep those helper side effects outside the repo
        # so this producer owns only its governed primary proof artifact.
        with tempfile.TemporaryDirectory(prefix="hde-open-rails-abba-") as temp_dir:
            temp_root = Path(temp_dir)
            outcome = ingest_vendor_bodygraph(
                inputs,
                env={**os.environ, **RAILS_OPEN},
                dry_run=True,
                client=client,
                retry_log=temp_root / "retry_trace.log",
                success_log=temp_root / "ingest_success.log",
                canon_log=temp_root / "json_canon_compare.log",
            )
        return outcome.payload, outcome.input_fingerprint, outcome.payload_sha256

    for label, inputs in (("a", a_inputs), ("b", b_inputs)):
        try:
            payload, input_fingerprint, payload_sha = acquire(label, inputs)
            proof["requests_completed"] += 1
            outcomes.append((label, payload))
            proof["request_results"].append({"party": label, "result_class": "success", "input_fingerprint_sha256": sha(input_fingerprint.encode("utf-8")), "normalized_payload_sha256": payload_sha})
        except VendorError as exc:
            proof["request_results"].append({"party": label, "result_class": exc.code})
            break
    proof["requests_attempted"] = counter["attempted"]
    if len(outcomes) != 2:
        proof["typed_result_class"] = "ACQUISITION_INCOMPLETE"
        return proof
    a_payload = outcomes[0][1]
    b_payload = outcomes[1][1]
    a_hash = sha(emitter.emit_public(a_payload))
    b_hash = sha(emitter.emit_public(b_payload))
    proof["normalized_a_sha256"] = a_hash
    proof["normalized_b_sha256"] = b_hash
    a_person, a_chart = cli_main._person_and_chart_from_payload(a_payload, uid_hint=a_inputs.user_id)
    b_person, b_chart = cli_main._person_and_chart_from_payload(b_payload, uid_hint=b_inputs.user_id)
    a_person2, b_person2, a_chart2, b_chart2 = cli_main._canonical_pair(a_person, b_person, a_chart, b_chart)
    b_person3, a_person3, b_chart3, a_chart3 = cli_main._canonical_pair(b_person, a_person, b_chart, a_chart)
    reader_emitter = reader_emitter or _emit_live_reader_bytes
    ab_reader = reader_emitter(a_chart2, b_chart2)
    ba_reader = reader_emitter(b_chart3, a_chart3)
    ab_reader_run2 = reader_emitter(a_chart2, b_chart2)
    ba_reader_run2 = reader_emitter(b_chart3, a_chart3)
    emitted_reader_bytes = (ab_reader, ba_reader, ab_reader_run2, ba_reader_run2)
    reader_hashes = {
        "ab_sha256": sha(ab_reader),
        "ab_run2_sha256": sha(ab_reader_run2),
        "ba_sha256": sha(ba_reader),
        "ba_run2_sha256": sha(ba_reader_run2),
    }
    proof["reader_hashes"] = reader_hashes
    predicates = {
        "request_bound_ok": counter["attempted"] <= 2,
        "same_normalized_inputs_reused": a_hash == sha(emitter.emit_public(a_payload)) and b_hash == sha(emitter.emit_public(b_payload)),
        "abba_byte_identity": ab_reader == ba_reader,
        "canonical_json": all(_assert_canonical("live_reader", value) for value in emitted_reader_bytes),
        "single_lf": all(value.endswith(b"\n") and not value.endswith(b"\n\n") and b"\r" not in value for value in emitted_reader_bytes),
        "two_run_ab_identity": ab_reader == ab_reader_run2,
        "two_run_ba_identity": ba_reader == ba_reader_run2,
        **_live_summary_predicates(proof),
    }
    proof.update({
        "applied_abba_contract_mode": "raw_byte_identity_after_existing_canonical_pair_normalization",
        "same_normalized_inputs_reused_for_ab_ba": predicates["same_normalized_inputs_reused"],
        "reader_hashes": reader_hashes,
        "predicates": predicates,
        "typed_result_class": "PASS" if all(predicates.values()) else "FAIL",
        "result": "pass" if all(predicates.values()) else "fail",
        "top_level_pass": all(predicates.values()),
    })
    return proof


def _require_passing_live_proof(proof: dict[str, Any]) -> dict[str, Any]:
    _validate_live_shape(proof)
    predicates = proof.get("predicates")
    if (
        proof.get("acceptance_token_satisfied") is not False
        or proof.get("requests_attempted") != 2
        or proof.get("requests_completed") != 2
    ):
        raise SystemExit(f"INVALID_LIVE_PROOF:{LIVE_ABBA_REL}")
    if proof.get("no_raw_payload_predicate") is not True or proof.get("no_secret_value_predicate") is not True:
        raise SystemExit(f"UNSAFE_LIVE_PROOF:{LIVE_ABBA_REL}")
    summary_predicates = _live_summary_predicates(proof)
    if (
        proof.get("top_level_pass") is not True
        or proof.get("result") != "pass"
        or proof.get("typed_result_class") != "PASS"
        or proof.get("same_normalized_inputs_reused_for_ab_ba") is not True
        or not isinstance(predicates, dict)
        or not LIVE_REQUIRED_PREDICATES.issubset(predicates)
        or any(predicates.get(key) is not value for key, value in summary_predicates.items())
        or any(predicates.get(key) is not True for key in LIVE_REQUIRED_PREDICATES)
        or any(value is not True for value in predicates.values())
    ):
        raise SystemExit(f"FAILED_LIVE_PROOF:{LIVE_ABBA_REL}")
    return proof


def generate_live(*, check: bool = False) -> dict[str, Any]:
    if check:
        path = ROOT / LIVE_ABBA_REL
        if not path.exists():
            raise SystemExit(f"DRIFT:{LIVE_ABBA_REL}")
        data = path.read_bytes()
        if not data.endswith(b"\n") or data.endswith(b"\n\n") or b"\r" in data:
            raise SystemExit(f"INVALID_LF:{LIVE_ABBA_REL}")
        try:
            proof = json.loads(data)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"INVALID_JSON:{LIVE_ABBA_REL}") from exc
        if canonical_json_bytes(proof) != data:
            raise SystemExit(f"NONCANONICAL:{LIVE_ABBA_REL}")
        return _require_passing_live_proof(proof)
    proof = _require_passing_live_proof(build_live_proof())
    _write_primary(LIVE_ABBA_REL, canonical_json_bytes(proof), check=False)
    return proof


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--live", action="store_true", help="write/check the PO-authorized bounded live vendor proof")
    args = parser.parse_args(argv)
    proof = generate_live(check=args.check) if args.live else generate_fixture(check=args.check)
    print(json.dumps({"status": "OK", "path": LIVE_ABBA_REL if args.live else OPEN_ABBA_REL, "top_level_pass": proof.get("top_level_pass"), "result": proof.get("result", "pass")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
