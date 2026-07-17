#!/usr/bin/env python3
"""Run the HDE-EPIC038 closed-rails release-sanity chain."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env

SANITY_LOG = ROOT / "audit/gates/sanity_pipeline/sanity_pipeline.log"
PIPELINE_ID = "HDE-EPIC038-PR06-release-sanity"

OPS_FILES = {
    "ops-01": ("commands.txt", "stdout.log", "stderr.log", "exit_code.txt", "env_presence.json", "db_posture_summary.json", "provider_parity.proof.json", "bridge_consistency.result.json", "nonclaims.json", "result_summary.json", "checksums.sha256"),
    "ops-02": ("commands.txt", "stdout.log", "stderr.log", "exit_code.txt", "env_presence.json", "request_summary.json", "mapped_output_summary.json", "read_back_summary.json", "canonical_parity.log", "idempotence.log", "no_raw_vendor_payload_persistence.log", "legacy_fallback_preservation.log", "nonclaims.json", "result_summary.json", "checksums.sha256"),
}

OPS01_CORPUS_NAME = "hde_epic038_ops01_live_bodygraph_parity_v3"
OPS01_PARITY_ROWS = (
    "grants",
    "search_path",
    "select_one",
    "ddl_fingerprint",
    "bodygraph_payload_row",
)
OPS01_BRIDGE_COMMANDS = {
    "bridge_bodygraph_read",
    "canonical_comparison",
    "db_posture_capture",
    "direct_bodygraph_read",
    "governed_checker",
}
OPS01_BRIDGE_PREDICATES = {
    "all_actions_closed_rails",
    "bodygraph_bridge_available",
    "bodygraph_direct_available",
    "bodygraph_row_match",
    "bodygraph_selector_approved",
    "four_row_corpus_exact",
    "provider_selection_consistent",
    "search_path_exact",
}


@dataclass(frozen=True)
class SanityStep:
    name: str
    commands: tuple[tuple[str, ...], ...]

    def __init__(self, name: str, command: Sequence[str] | Sequence[Sequence[str]]):
        object.__setattr__(self, "name", name)
        if command and isinstance(command[0], str):
            object.__setattr__(self, "commands", (tuple(command),))
        else:
            object.__setattr__(self, "commands", tuple(tuple(item) for item in command))


STAGE_NAMES = (
    "01 Environment pins", "02 Identity and release provenance", "03 Canonical JSON",
    "04 Reader-to-CLI, AB-to-BA, two-run, and preimage checks", "05 A7 Catalog transport",
    "06 CI rails", "07 DB posture", "08 BodyGraph policy", "09 DB-bridge parity",
    "10 Architecture snapshot", "11 Configured-v2 mapped-cache local evidence",
    "12 OPS evidence checksum and summary validation", "13 Human Index and Machine Mirror refresh",
    "14 Path validation", "15 Mirror schema and hash validation",
    "16 Topology orientation validation", "17 Final LF validation",
)


def _py(path: str, *args: str) -> tuple[str, ...]:
    return (sys.executable, path, *args)


def _finalization_commands() -> tuple[tuple[str, ...], ...]:
    """Return the bounded writer/check sequence for the final evidence bytes."""
    return (
        _py("tools/evidence/update_evidence_index.py"),
        _py("tools/evidence/orientation_demo.py"),
        _py("tools/evidence/update_evidence_index.py"),
        _py("tools/evidence/update_evidence_index.py", "--check"),
        _py("tools/evidence/orientation_demo.py", "--check"),
        _py("tools/evidence/validate_evidence_paths.py"),
        ("ci/checks/check_mirror_schema.sh",),
        ("bash", "ci/checks/check_evidence_index_hash.sh"),
        ("ci/checks/check_final_lf.sh",),
    )


def default_steps() -> list[SanityStep]:
    return [
        SanityStep(STAGE_NAMES[0], (("ci/checks/check_env_pins.sh",),)),
        SanityStep(STAGE_NAMES[1], (_py("tools/evidence/generate_identity_provenance.py"), _py("tools/evidence/generate_release_bindings.py"), _py("tools/evidence/generate_env_matrix_snapshot.py"))),
        SanityStep(STAGE_NAMES[2], (_py("tools/evidence/run_canonical_json_gate.py", "--check-only"),)),
        SanityStep(STAGE_NAMES[3], (_py("tools/evidence/generate_determinism_gate_proofs.py"), _py("tools/evidence/generate_open_rails_abba_proof.py", "--check"), _py("tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check"))),
        SanityStep(STAGE_NAMES[4], (_py("tools/evidence/generate_a7_transport_proofs.py"),)),
        SanityStep(STAGE_NAMES[5], (_py("tools/evidence/generate_rails_gate_evidence.py"), _py("ci/checks/run_rails_job_definitions.py", "ci/jobs/rails_closed_refusal.yml", "ci/jobs/rails_open_conformance.yml", "ci/jobs/logs_keys_only_redaction.yml"))),
        SanityStep(STAGE_NAMES[6], (_py("tools/evidence/generate_db_runtime_posture.py"),)),
        SanityStep(STAGE_NAMES[7], (_py("tools/evidence/generate_bodygraph_policy_proofs.py"),)),
        SanityStep(STAGE_NAMES[8], (_py("tools/evidence/generate_db_bridge_parity.py"),)),
        SanityStep(STAGE_NAMES[9], (_py("tools/evidence/generate_architecture_snapshot.py"),)),
        SanityStep(STAGE_NAMES[10], (_py("tools/evidence/generate_v2_mapped_cache_evidence.py"),)),
        SanityStep(STAGE_NAMES[11], (("__validate_ops__",),)),
        SanityStep(STAGE_NAMES[12], (_py("tools/evidence/update_evidence_index.py"),)),
        SanityStep(STAGE_NAMES[13], (_py("tools/evidence/validate_evidence_paths.py"),)),
        SanityStep(STAGE_NAMES[14], (("ci/checks/check_mirror_schema.sh",), ("bash", "ci/checks/check_evidence_index_hash.sh"))),
        SanityStep(STAGE_NAMES[15], (_py("tools/evidence/orientation_demo.py"), _py("tools/evidence/update_evidence_index.py"), _py("tools/evidence/orientation_demo.py", "--check"))),
        SanityStep(STAGE_NAMES[16], _finalization_commands()),
    ]


def _read_json(path: Path) -> dict:
    display_path = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.as_posix()
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{display_path}: invalid JSON") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{display_path}: expected JSON object")
    return value


def _validate_secret_safety(packet: Path, required: Sequence[str]) -> None:
    """Reject recognizable secret values and persisted raw request/response data."""
    credential_assignment = re.compile(
        r"(?i)\b(DATABASE_URL|DB_BRIDGE_URL|HD_API_KEY|GEO_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL)\s*=\s*[\"']?([^\s,\"'}]+)"
    )
    credential_json = re.compile(
        r'(?i)"(?:DATABASE_URL|DB_BRIDGE_URL|HD_API_KEY|GEO_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL)"\s*:\s*"([^"]+)"'
    )
    bearer = re.compile(r"(?i)\bBearer\s+([^\s\"']+)")
    vendor_header = re.compile(
        r"(?i)(?:\"?HD-(?:Geocode|Api)-Key\"?\s*[:=]\s*[\"']?)([^\s,\"'}]+)"
    )
    forbidden_uri = re.compile(r"(?i)\b(?:postgres(?:ql)?|railway)://")
    for name in required:
        if name == "checksums.sha256":
            continue
        path = packet / name
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise ValueError(f"{packet.name}: {name} is not UTF-8 secret-safe evidence") from exc
        if forbidden_uri.search(text):
            raise ValueError(f"{packet.name}: {name} contains an unredacted service URI")
        for match in bearer.finditer(text):
            if match.group(1).lower() not in {"<redacted>", "redacted"}:
                raise ValueError(f"{packet.name}: {name} contains an unredacted bearer value")
        for match in vendor_header.finditer(text):
            value = match.group(1).lower()
            if value not in {"<redacted>", "redacted", "set:redacted", "set", "unset", "***"} and not value.startswith(("$", "${")):
                raise ValueError(f"{packet.name}: {name} contains an unredacted vendor header value")
        for match in credential_assignment.finditer(text):
            value = match.group(2).strip().lower()
            if value not in {"redacted", "<redacted>", "set:redacted", "set", "unset"} and not value.startswith(("$", "${")):
                raise ValueError(f"{packet.name}: {name} contains an unredacted credential value")
        for match in credential_json.finditer(text):
            if match.group(1).lower() not in {"redacted", "<redacted>", "set:redacted", "set", "unset"}:
                raise ValueError(f"{packet.name}: {name} contains an unredacted credential value")
        raw_payload_key = re.compile(
            r'(?i)"(?:raw_vendor_(?:payload|envelope)|raw_(?:request|response)_body)"\s*:'
        )
        safe_raw_value = re.compile(
            r'(?i)^(?:false|null|"(?:none|redacted)")(?=\s*(?:[,}\]\n]|$))'
        )
        for match in raw_payload_key.finditer(text):
            if not safe_raw_value.match(text[match.end():].lstrip()):
                raise ValueError(f"{packet.name}: {name} contains persisted raw request, response, or vendor data")


def _require_log_predicates(path: Path, required: Sequence[str]) -> None:
    try:
        text = path.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"ops-02: {path.name} is not readable UTF-8 evidence") from exc
    if not text.startswith("PASS ") or any(token not in text.split() for token in required):
        raise ValueError(f"ops-02: {path.name} predicate failed")


def _normalize_ddl_provider_value(value: object) -> tuple[tuple[str, str, tuple[tuple[str, str], ...]], ...]:
    if not isinstance(value, list) or not value:
        raise ValueError("ops-01: ddl_fingerprint provider value must be a non-empty list")
    normalized: list[tuple[str, str, tuple[tuple[str, str], ...]]] = []
    for item in value:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not isinstance(item.get("kind"), str):
            raise ValueError("ops-01: ddl_fingerprint provider object is malformed")
        columns = item.get("columns", [])
        if not isinstance(columns, list):
            raise ValueError("ops-01: ddl_fingerprint columns must be a list")
        normalized_columns: list[tuple[str, str]] = []
        for column in columns:
            if not isinstance(column, dict) or not isinstance(column.get("name"), str):
                raise ValueError("ops-01: ddl_fingerprint column is malformed")
            data_type = column.get("data_type", column.get("type"))
            if not isinstance(data_type, str):
                raise ValueError("ops-01: ddl_fingerprint column type is malformed")
            normalized_columns.append((column["name"], data_type))
        normalized.append((item["name"], item["kind"], tuple(sorted(normalized_columns))))
    return tuple(sorted(normalized))


def _normalized_provider_value(name: str, provider: dict) -> object:
    value = provider.get("value")
    if name == "grants":
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError("ops-01: grants provider value is malformed")
        return tuple(sorted(value))
    if name == "search_path":
        if not isinstance(value, str):
            raise ValueError("ops-01: search_path provider value is malformed")
        return tuple(part.strip() for part in value.split(","))
    if name == "select_one":
        if type(value) is not int:
            raise ValueError("ops-01: select_one provider value is malformed")
        return value
    if name == "ddl_fingerprint":
        return _normalize_ddl_provider_value(value)
    raise ValueError(f"ops-01: unsupported parity row {name}")


def _compare_provider_values(rows: Sequence[dict]) -> str:
    by_name = {row["name"]: row for row in rows}
    for name in OPS01_PARITY_ROWS[:-1]:
        row = by_name[name]
        if _normalized_provider_value(name, row["direct"]) != _normalized_provider_value(name, row["bridge"]):
            raise ValueError(f"ops-01: provider values disagree for {name}")
    bodygraph = by_name["bodygraph_payload_row"]
    direct_sha = bodygraph["direct"].get("canonical_sha256")
    bridge_sha = bodygraph["bridge"].get("canonical_sha256")
    if (
        not isinstance(direct_sha, str)
        or not re.fullmatch(r"[0-9a-f]{64}", direct_sha)
        or bridge_sha != direct_sha
        or bodygraph.get("comparison") != "FILE_EQ_CANON_BYTES_OK"
        or bodygraph["direct"].get("raw_bodygraph_payload_recorded") is not False
        or bodygraph["bridge"].get("raw_bodygraph_payload_recorded") is not False
    ):
        raise ValueError("ops-01: BodyGraph provider hashes or persistence posture disagree")
    return direct_sha


def _validate_ops01_environment(packet: Path) -> None:
    env = _read_json(packet / "env_presence.json")
    presence = env.get("environment_presence")
    rails = env.get("execution_rails")
    if (
        env.get("secret_posture") != "presence_only"
        or not isinstance(presence, dict)
        or presence.get("APP_ENV") != "SET:dev"
        or presence.get("DATABASE_URL") != "SET:REDACTED"
        or presence.get("DB_BRIDGE_URL") != "SET:REDACTED"
        or presence.get("ENGINE_ENV") != "UNSET"
        or not isinstance(rails, dict)
        or set(rails) != OPS01_BRIDGE_COMMANDS
    ):
        raise ValueError("ops-01: env_presence.json execution posture failed")
    if any(
        not isinstance(values, dict)
        or values.get("SAFE_MODE") != "1"
        or values.get("ALLOW_NETWORK") != "0"
        for values in rails.values()
    ):
        raise ValueError("ops-01: env_presence.json closed-rails predicates failed")
    if rails["direct_bodygraph_read"].get("DB_FORCE_PG") != "1" or rails["bridge_bodygraph_read"].get("DB_FORCE_BRIDGE") != "1":
        raise ValueError("ops-01: env_presence.json provider-selection rails failed")


def _validate_ops02_environment(packet: Path) -> dict:
    env = _read_json(packet / "env_presence.json")
    presence = env.get("environment_presence")
    route_policy = env.get("route_policy")
    required_presence = {
        "ALLOW_NETWORK": "1",
        "APP_ENV": "SET:dev",
        "DATABASE_URL": "SET:REDACTED",
        "GEO_API_KEY": "SET:REDACTED",
        "HD_API_BASE_URL": "SET:REDACTED",
        "HD_API_KEY": "SET:REDACTED",
        "LANG": "C",
        "LC_ALL": "C",
        "SAFE_MODE": "0",
        "TZ": "UTC",
    }
    required_route = {
        "classification": "adapter_backed_v2_chart",
        "configured_base_version": "v2",
        "resource_path": "charts",
        "route_auth_posture": "Authorization: Bearer <redacted>",
        "route_family": "recommended_v2_chart",
    }
    if (
        env.get("secret_posture") != "presence_only"
        or not isinstance(presence, dict)
        or any(presence.get(key) != value for key, value in required_presence.items())
        or not isinstance(route_policy, dict)
        or any(route_policy.get(key) != value for key, value in required_route.items())
    ):
        raise ValueError("ops-02: env_presence.json bounded dev open-rails posture failed")
    return route_policy


def _validate_ops01(packet: Path, summary: dict) -> None:
    """Derive OPS-01 PASS from its fixed corpus and lower-level primaries."""
    _validate_ops01_environment(packet)
    observations = summary.get("observations")
    if not isinstance(observations, dict):
        raise ValueError("ops-01: result_summary.json observations must be an object")

    db_posture = _read_json(packet / "db_posture_summary.json")
    boundary_views = db_posture.get("boundary_views")
    boundary_views_valid = (
        isinstance(boundary_views, list)
        and bool(boundary_views)
        and all(
            isinstance(view, dict)
            and view.get("readonly") is True
            and view.get("is_insertable_into") == "NO"
            and view.get("is_trigger_updatable") == "NO"
            and view.get("is_updatable") == "NO"
            for view in boundary_views
        )
    )
    if (
        db_posture.get("status") != "PASS"
        or db_posture.get("observation_mode") != "read_only"
        or db_posture.get("search_path") != "hde, public"
        or db_posture.get("search_path_exact") is not True
        or db_posture.get("boundary_views_readonly") is not True
        or db_posture.get("partition_plan_status") != "PASS"
        or not boundary_views_valid
    ):
        raise ValueError("ops-01: db_posture_summary.json PASS predicates failed")

    parity = _read_json(packet / "provider_parity.proof.json")
    corpus = parity.get("active_parity_corpus")
    live_parity = parity.get("live_provider_parity")
    provider_observations = parity.get("provider_observations")
    rows = parity.get("capabilities")
    rows_well_formed = (
        isinstance(rows, list)
        and bool(rows)
        and all(
            isinstance(row, dict)
            and isinstance(row.get("direct"), dict)
            and isinstance(row.get("bridge"), dict)
            for row in rows
        )
    )
    if not rows_well_formed:
        raise ValueError("ops-01: provider_parity.proof.json contains unavailable, errored, or malformed claimed row")
    row_names = tuple(row.get("name") for row in rows)
    if (
        not isinstance(corpus, dict)
        or corpus.get("name") != OPS01_CORPUS_NAME
        or corpus.get("ordered_rows") != list(OPS01_PARITY_ROWS)
        or row_names != OPS01_PARITY_ROWS
        or summary.get("active_parity_corpus") != OPS01_CORPUS_NAME
        or summary.get("active_parity_rows") != list(OPS01_PARITY_ROWS)
    ):
        raise ValueError("ops-01: provider parity exact corpus identity or ordered rows failed")
    if any(
        row.get("parity") != "match"
        or row["direct"].get("status") != "ok"
        or row["bridge"].get("status") != "ok"
        for row in rows
    ):
        raise ValueError("ops-01: provider_parity.proof.json contains unavailable, errored, or unmatched claimed row")
    bodygraph_sha = _compare_provider_values(rows)
    expected_count = len(OPS01_PARITY_ROWS)
    if (
        parity.get("status") != "PASS"
        or not isinstance(live_parity, dict)
        or live_parity.get("direct_provider_rows") != "available"
        or live_parity.get("bridge_provider_rows") != "available"
        or live_parity.get("claimed_row_count") != expected_count
        or live_parity.get("matched_row_count") != expected_count
        or live_parity.get("parity_status") != "pass"
        or not isinstance(provider_observations, dict)
        or provider_observations.get("direct") != "ok"
        or provider_observations.get("bridge") != "ok"
    ):
        raise ValueError("ops-01: provider_parity.proof.json PASS predicates failed")
    selector = corpus.get("selector")
    bodygraph_row = rows[-1]
    if not isinstance(selector, dict) or summary.get("bodygraph_selector") != selector or bodygraph_row.get("selector") != selector:
        raise ValueError("ops-01: provider parity selector identity disagreement")

    bridge = _read_json(packet / "bridge_consistency.result.json")
    command_exit_codes = bridge.get("command_exit_codes")
    governed_checker = bridge.get("governed_checker")
    comparator = bridge.get("bodygraph_comparator")
    bridge_predicates = bridge.get("predicates")
    exit_codes_valid = (
        isinstance(command_exit_codes, dict)
        and OPS01_BRIDGE_COMMANDS.issubset(command_exit_codes)
        and all(type(value) is int and value == 0 for value in command_exit_codes.values())
    )
    predicates_valid = (
        isinstance(bridge_predicates, dict)
        and OPS01_BRIDGE_PREDICATES.issubset(bridge_predicates)
        and all(value is True for value in bridge_predicates.values())
    )
    comparator_inputs = comparator.get("direct_input") if isinstance(comparator, dict) else None
    comparator_bridge_input = comparator.get("bridge_input") if isinstance(comparator, dict) else None
    if (
        bridge.get("status") != "PASS"
        or not exit_codes_valid
        or not isinstance(governed_checker, dict)
        or governed_checker.get("exit_code") != 0
        or governed_checker.get("result") != "PASS"
        or not isinstance(comparator, dict)
        or comparator.get("exit_code") != 0
        or comparator.get("result") != "FILE_EQ_CANON_BYTES_OK"
        or comparator.get("canonical_sha256") != bodygraph_sha
        or not isinstance(comparator_inputs, dict)
        or comparator_inputs.get("sha256") != bodygraph_sha
        or not isinstance(comparator_bridge_input, dict)
        or comparator_bridge_input.get("sha256") != bodygraph_sha
        or not predicates_valid
    ):
        raise ValueError("ops-01: bridge_consistency.result.json PASS predicates failed")

    if (
        summary.get("ops_observation_status") != "PASS"
        or observations.get("db_posture") != db_posture.get("status")
        or observations.get("bridge_consistency") != bridge.get("status")
        or observations.get("direct_provider") != "available"
        or observations.get("bridge_provider") != "available"
        or observations.get("bodygraph_row_parity") != "match"
        or observations.get("search_path") != db_posture.get("search_path")
        or observations.get("claimed_rows") != expected_count
        or observations.get("matched_rows") != expected_count
    ):
        raise ValueError("ops-01: result_summary.json disagrees with primary OPS evidence")


def _validate_packet(root: Path, package: str, required: Sequence[str]) -> None:
    packet = root / "audit/ops/hde-epic038" / package
    for name in required:
        path = packet / name
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"{package}: required file {name} is missing or empty")
    try:
        retained_entries = list(packet.iterdir())
    except OSError as exc:
        raise ValueError(f"{package}: packet directory is not readable") from exc
    retained_files = sorted(entry.name for entry in retained_entries if entry.is_file())
    _validate_secret_safety(packet, retained_files)
    allowed_files = set(required) | {f"{name}.path_proof.txt" for name in required}
    unexpected = sorted(entry.name for entry in retained_entries if entry.name not in allowed_files)
    if unexpected:
        raise ValueError(f"{package}: unexpected retained packet entry {unexpected[0]}")
    expected = set(required) - {"checksums.sha256"}
    rows: dict[str, str] = {}
    pattern = re.compile(r"^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$")
    for line_number, line in enumerate((packet / "checksums.sha256").read_text(encoding="ascii").splitlines(), 1):
        match = pattern.fullmatch(line)
        if not match:
            raise ValueError(f"{package}: checksums.sha256 malformed row {line_number}")
        digest, name = match.groups()
        if name in rows:
            raise ValueError(f"{package}: checksums.sha256 duplicate row for {name}")
        if name not in expected:
            raise ValueError(f"{package}: checksums.sha256 unknown or escaping path {name}")
        rows[name] = digest
    missing = expected - rows.keys()
    if missing:
        raise ValueError(f"{package}: checksums.sha256 missing {sorted(missing)[0]}")
    for name in sorted(expected):
        actual = hashlib.sha256((packet / name).read_bytes()).hexdigest()
        if actual != rows[name]:
            raise ValueError(f"{package}: checksums.sha256 mismatch for {name}")
    if (packet / "exit_code.txt").read_text(encoding="utf-8").strip() != "0":
        raise ValueError(f"{package}: exit_code.txt is not successful")
    summary = _read_json(packet / "result_summary.json")
    nonclaims = _read_json(packet / "nonclaims.json").get("nonclaims", [])
    required_nonclaims = {"no_qa_pass_claim", "no_acceptance_token_claim", "no_pf09_status_movement", "no_epic_closeout_claim"}
    if not isinstance(nonclaims, list) or not all(isinstance(item, str) for item in nonclaims) or not required_nonclaims.issubset(nonclaims):
        raise ValueError(f"{package}: nonclaims.json is incomplete")
    if package == "ops-01":
        _validate_ops01(packet, summary)
    else:
        route_policy = _validate_ops02_environment(packet)
        predicates = summary.get("predicates", {})
        if not isinstance(predicates, dict):
            raise ValueError("ops-02: result_summary.json predicates must be an object")
        required_predicates = {"adapter_mapped", "exactly_one_vendor_request", "canonical_write_read_back_equivalence", "idempotent_repeated_write", "mapped_payload_only", "normalized_identity_single_row", "production_like_refused", "explicit_legacy_fallback_preserved", "retained_by_po_decision"}
        if summary.get("status") != "PASS" or summary.get("retention_decision") != "retain" or any(predicates.get(key) is not True for key in required_predicates):
            raise ValueError("ops-02: result_summary.json PASS predicate failed")
        request = _read_json(packet / "request_summary.json")
        mapped = _read_json(packet / "mapped_output_summary.json")
        read_back = _read_json(packet / "read_back_summary.json")
        stdout = _read_json(packet / "stdout.log")
        if (
            request.get("vendor_requests") != 1
            or request.get("attempt_limit") != 1
            or request.get("request_values_persisted") is not False
            or request.get("configured_base") != "REDACTED"
            or request.get("auth_posture") != "Authorization: Bearer <redacted>"
            or request.get("route") != "vendor.hdapi.post:/charts"
            or request.get("resource_path") != "charts"
            or request.get("route_family") != "recommended_v2_chart"
            or request.get("payload_family") != "ChartResult"
            or request.get("geocode_required") is not True
            or request.get("request_field_names") != ["birthdate", "birthtime", "location"]
            or request.get("resource_path") != route_policy.get("resource_path")
            or request.get("route_family") != route_policy.get("route_family")
        ):
            raise ValueError("ops-02: request_summary.json predicate failed")
        if mapped.get("adapter_status") != "mapped" or mapped.get("adapter_code") != "ADAPTER_MAPPED" or mapped.get("raw_vendor_envelope_persisted") is not False or mapped.get("payload_posture") != "adapter_mapped_no_raw_vendor_payload" or mapped.get("payload_family") != request.get("payload_family"):
            raise ValueError("ops-02: mapped_output_summary.json predicate failed")
        identity = summary.get("identity")
        fingerprint = request.get("input_fingerprint")
        synthetic_user_id = read_back.get("synthetic_user_id")
        if (
            not isinstance(identity, dict)
            or not isinstance(fingerprint, str)
            or not re.fullmatch(r"[0-9a-f]{64}", fingerprint)
            or identity.get("input_fingerprint") != fingerprint
            or not isinstance(synthetic_user_id, str)
            or not re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", synthetic_user_id)
            or identity.get("synthetic_user_id") != synthetic_user_id
            or identity.get("vendor") != "hdapi"
            or identity.get("vendor_version") != 2
        ):
            raise ValueError("ops-02: mapped-cache identity disagreement")
        canonical_sha = mapped.get("canonical_sha256")
        if not isinstance(canonical_sha, str) or not re.fullmatch(r"[0-9a-f]{64}", canonical_sha) or read_back.get("canonical_sha256") != canonical_sha or read_back.get("read_back_match") is not True or read_back.get("identity_rows") != 1 or read_back.get("retention_decision") != "retain" or read_back.get("stored_payload_posture") != "adapter_mapped_no_raw_vendor_payload":
            raise ValueError("ops-02: read_back_summary.json predicate failed")
        if stdout.get("vendor_requests") != 1 or stdout.get("adapter_status") != "ADAPTER_MAPPED" or stdout.get("canonical_sha256") != canonical_sha or stdout.get("read_back_match") is not True or stdout.get("idempotent") is not True or stdout.get("identity_rows") != 1 or stdout.get("second_write_rows") != 0 or stdout.get("retention_decision") != "retain":
            raise ValueError("ops-02: stdout.log predicate failed")
        _require_log_predicates(packet / "canonical_parity.log", (f"canonical_sha256={canonical_sha}", "pre_write_post_read_match=true", "first_read_back_match=true", "second_read_back_match=true"))
        _require_log_predicates(packet / "idempotence.log", ("first_rows_written=1", "second_rows_written=0", "identity_rows=1", "canonical_hash_unchanged=true"))
        _require_log_predicates(packet / "no_raw_vendor_payload_persistence.log", ("payload_posture=adapter_mapped_no_raw_vendor_payload", "raw_standard_response=false", "raw_chart_result_envelope=false", "request_body=false", "response_body=false", "secrets=false"))
        _require_log_predicates(packet / "legacy_fallback_preservation.log", ("classification=explicit_legacy_fallback", "route_family=legacy_bodygraph", "configured_v2_legacy_fallback=false", "external_io=0"))


def validate_ops_packages(root: Path = ROOT) -> None:
    for package, required in OPS_FILES.items():
        _validate_packet(root, package, required)


def _run_command(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(DETERMINISM_ENV_PINS)
    if any(item.endswith("generate_a7_transport_proofs.py") for item in command):
        env["HDE_WRITE_A7_PROOFS"] = "1"
    return subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True)


def _run_stage(step: SanityStep) -> int:
    for command in step.commands:
        if command == ("__validate_ops__",):
            try:
                validate_ops_packages()
            except ValueError as exc:
                print(str(exc), file=sys.stderr)
                return 1
        else:
            result = _run_command(command)
            if result.returncode:
                print(
                    f"{step.name}: command exited {result.returncode}: {' '.join(command)}",
                    file=sys.stderr,
                )
                return result.returncode or 1
    return 0


def _render_log(results: Sequence[tuple[str, str]], first_failure: str, summary: str) -> bytes:
    lines = ["run:sanity-pipeline", f"pipeline_identity:{PIPELINE_ID}", "env:" + ",".join(f"{key}={DETERMINISM_ENV_PINS[key]}" for key in sorted(DETERMINISM_ENV_PINS)), "env_pins:audit/gates/determinism/env_pins.log", "ops_evidence:validated_existing_bytes_only;not_rerun=true"]
    for name, status in results:
        canonical_status = "OK" if status == "OK" else "FAIL"
        lines.append(f"check {name}:{canonical_status}")
        if status.startswith("NOT_EXECUTED_EARLIER_FAILURE:"):
            lines.append(f"not_executed {name}:earlier_mandatory_failure={status.split(':', 1)[1]}")
    lines.extend((f"first_failed_stage:{first_failure}", f"summary:{summary}"))
    return ("\n".join(lines) + "\n").encode("utf-8")


def _write_log(path: Path, results: Sequence[tuple[str, str]], first_failure: str, summary: str) -> bytes:
    data = _render_log(results, first_failure, summary)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def _rebind_failure_log() -> int:
    """Bind final FAIL bytes without replaying mandatory stages marked skipped."""
    result = _run_command(_py("tools/evidence/update_evidence_index.py"))
    return result.returncode or 0


def run_pipeline(*, log_path: Path = SANITY_LOG, steps: Sequence[SanityStep] | None = None, refresh_index: bool = True) -> int:
    ensure_determinism_env()
    log_path = (log_path if log_path.is_absolute() else ROOT / log_path).resolve()
    roster = list(default_steps() if steps is None else steps)
    canonical_run = log_path == SANITY_LOG.resolve() and steps is None
    results: list[tuple[str, str]] = []
    failure = "NONE"
    code = 0
    prospective_pass: bytes | None = None
    for index, step in enumerate(roster):
        # The final updater must bind the final sanity bytes, not an interim
        # version.  Render the prospective PASS log before that updater runs;
        # the normal final render below is byte-identical on success.
        if canonical_run and index == len(roster) - 1 and failure == "NONE":
            prospective_pass = _write_log(log_path, [*results, (step.name, "OK")], "NONE", "PASS")
        code = _run_stage(step)
        results.append((step.name, "OK" if code == 0 else "FAIL"))
        if code:
            failure = step.name
            results.extend((later.name, f"NOT_EXECUTED_EARLIER_FAILURE:{step.name}") for later in roster[index + 1:])
            break
    passed = code == 0 and len(results) == len(roster) and all(status == "OK" for _, status in results)
    final_bytes = _render_log(results, failure, "PASS" if passed else "FAIL")
    if passed and canonical_run:
        try:
            current_bytes = log_path.read_bytes()
        except OSError:
            current_bytes = b""
        if prospective_pass != final_bytes or current_bytes != final_bytes:
            print(
                "canonical PASS bytes changed during final evidence sealing: "
                f"prospective={hashlib.sha256(prospective_pass or b'').hexdigest()}:{len(prospective_pass or b'')} "
                f"current={hashlib.sha256(current_bytes).hexdigest()}:{len(current_bytes)} "
                f"final={hashlib.sha256(final_bytes).hexdigest()}:{len(final_bytes)}",
                file=sys.stderr,
            )
            results[-1] = (results[-1][0], "FAIL")
            failure = results[-1][0]
            _write_log(log_path, results, failure, "FAIL")
            seal_code = _rebind_failure_log()
            if seal_code:
                print(f"canonical FAIL evidence finalization failed with exit code {seal_code}", file=sys.stderr)
                return seal_code
            return 1
        return 0

    _write_log(log_path, results, failure, "PASS" if passed else "FAIL")
    if not passed and canonical_run:
        seal_code = _rebind_failure_log()
        if seal_code:
            print(f"canonical FAIL evidence finalization failed with exit code {seal_code}", file=sys.stderr)
            return seal_code
    return 0 if passed else (code or 1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-path", type=Path, default=SANITY_LOG)
    args = parser.parse_args(argv)
    return run_pipeline(log_path=args.log_path)


if __name__ == "__main__":
    raise SystemExit(main())
