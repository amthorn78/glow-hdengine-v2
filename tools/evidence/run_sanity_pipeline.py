#!/usr/bin/env python3
"""Run the HDE-EPIC038 closed-rails release-sanity chain."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env
from tools.evidence.retained_evidence_safety import validate_retained_text_safety

SANITY_LOG = ROOT / "audit/gates/sanity_pipeline/sanity_pipeline.log"
PIPELINE_ID = "HDE-EPIC038-PR06-release-sanity"
PR_A_NONFINAL_REASON = "pr_a_nonfinal_ops03_pr_b_binding_required"
PR_A_NONFINAL_EXIT = 3

HISTORICAL_OPS01_FILES = (
    "commands.txt",
    "stdout.log",
    "stderr.log",
    "exit_code.txt",
    "env_presence.json",
    "db_posture_summary.json",
    "provider_parity.proof.json",
    "bridge_consistency.result.json",
    "nonclaims.json",
    "result_summary.json",
    "checksums.sha256",
)
HISTORICAL_OPS01_LEDGER_SHA256 = (
    "f4fd52eff5c8f2b61bbb9d97c3889a4bff2d12f581ba8e26dfb2d250ad1049d8"
)
HISTORICAL_BRIDGE_PRIMARY_SHA256 = {
    "artifacts/db_bridge/adapter_selection.snapshot.json": "7b2dbb9e8b477b40cb5ad4de0a19d2c04e6590f6946fe250ee4796699e6717ed",
    "artifacts/db_bridge/caps.snapshot.json": "83421e71641febcf3b942fd6e31c91a5c11c2a4acff61008cc5ef3215329cfb8",
    "artifacts/db_bridge/health.json": "6489d6d7a33c5d40e18fc61eeb6c34c341279ee61816394dde5189aa4ad8fae5",
    "artifacts/db_bridge/provider_parity.proof.json": "27bca3f1e8d7fbf1dd32abfd5fffd831d6ce3e0380bdfa371ed4683706b533e0",
    "artifacts/db_bridge/query_select_1.json": "bd919ec13cc10567b72b81f4326a8b525d4db8a2d8914fc884b86a6530726862",
    "artifacts/db_bridge/root.json": "c3afa09727b1dfbfb1eb831658c392b2d20ab3843a5dfd946ad2bb0c12fd8ea5",
    "artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json": "40cb7dc2a668660f641df15ed054c731432dc17294a1810ab4aeae324c59270b",
    "artifacts/runtime/env_connectivity.nondev_failure.json": "596f7b6ac47c81b8786e49ab50f79663ba5e2c8ffbc32d954322f51eb1f81cfc",
    "artifacts/runtime/env_connectivity.snapshot.json": "5f5fc10c2335ed3497bbd658ad32b49932c8ab9ce49a0d2d87e3f075a9a16a45",
    "schemas/presenter_db_bridge_compare.v1.json": "33fd1bb4fdae92382f33f87fba09f2206b10e0a2b12882c920ea5ade060b469b",
}
OPS02_FILES = (
    "commands.txt",
    "stdout.log",
    "stderr.log",
    "exit_code.txt",
    "env_presence.json",
    "request_summary.json",
    "mapped_output_summary.json",
    "read_back_summary.json",
    "canonical_parity.log",
    "idempotence.log",
    "no_raw_vendor_payload_persistence.log",
    "legacy_fallback_preservation.log",
    "nonclaims.json",
    "result_summary.json",
    "checksums.sha256",
)
OPS02_COMMANDS_SHA256 = (
    "d3ca676d0157ce30bf64d4b419610e3a5ceebc0dc13785475028b90ed31f163b"
)
OPS03_TRACKED_ROOT = Path("audit/ops/hde-epic038/ops-03")

PR05_PRIMARY_PATHS = (
    "artifacts/bodygraph/v2_mapped_cache/write_transcript.json",
    "artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json",
    "artifacts/bodygraph/v2_mapped_cache/canonical_parity.log",
    "artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log",
    "artifacts/bodygraph/v2_mapped_cache/idempotence.log",
    "artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log",
    "artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log",
    "artifacts/bodygraph/v2_mapped_cache/manifest.json",
    "schemas/bodygraph_v2_mapped_cache_transcript.v1.json",
    "schemas/bodygraph_v2_mapped_cache_manifest.v1.json",
)
SAFE_ENV_REFERENCE = re.compile(
    r"\$(?:[A-Za-z_][A-Za-z0-9_]*|\{[A-Za-z_][A-Za-z0-9_]*\})\Z"
)


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


class Ops03PacketUnavailable(ValueError):
    """The downstream OPS-03 packet has not been admitted yet."""


STAGE_NAMES = (
    "01 Environment pins", "02 Identity and release provenance", "03 Canonical JSON",
    "04 Reader-to-CLI, AB-to-BA, two-run, and preimage checks", "05 A7 Catalog transport",
    "06 CI rails", "07 Direct DB selection contract", "08 Direct DB posture artifacts",
    "09 BodyGraph policy", "10 Architecture snapshot",
    "11 Configured-v2 mapped-cache local evidence",
    "12 Historical bridge evidence integrity",
    "13 OPS-02 mapped-cache packet validation",
    "14 OPS-03 direct DB posture packet validation",
    "15 Human Index and Machine Mirror refresh", "16 Evidence-path validation",
    "17 Mirror schema and index/mirror hash validation",
    "18 Topology orientation validation", "19 Final-LF validation",
)


def _py(path: str, *args: str) -> tuple[str, ...]:
    return (sys.executable, path, *args)


def default_steps() -> list[SanityStep]:
    return [
        SanityStep(STAGE_NAMES[0], (("ci/checks/check_env_pins.sh",),)),
        SanityStep(STAGE_NAMES[1], (
            _py("tools/config/generate_config_artifacts.py", "--check"),
            _py("tools/config/generate_bundles.py", "--check"),
            _py("tools/evidence/generate_identity_provenance.py", "--check"),
            _py("tools/evidence/generate_release_bindings.py", "--check"),
            _py("tools/evidence/generate_env_matrix_snapshot.py", "--check"),
            _py("scripts/release_id_recompute.py", "--check"),
            _py("ci/checks/check_release_identity.sh"),
        )),
        SanityStep(STAGE_NAMES[2], (_py("tools/evidence/run_canonical_json_gate.py", "--check-only"),)),
        SanityStep(STAGE_NAMES[3], (_py("tools/evidence/generate_determinism_gate_proofs.py", "--check"), _py("tools/evidence/generate_open_rails_abba_proof.py", "--check"), _py("tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check"))),
        SanityStep(STAGE_NAMES[4], (_py("tools/evidence/generate_a7_transport_proofs.py", "--check"),)),
        SanityStep(STAGE_NAMES[5], (_py("tools/evidence/generate_rails_gate_evidence.py", "--check"), _py("ci/checks/run_rails_job_definitions.py", "ci/jobs/rails_closed_refusal.yml", "ci/jobs/rails_open_conformance.yml", "ci/jobs/logs_keys_only_redaction.yml"))),
        SanityStep(STAGE_NAMES[6], (("__validate_direct_selection__",), _py("ci/checks/check_direct_db_contract.py"))),
        SanityStep(STAGE_NAMES[7], (_py("tools/evidence/generate_db_runtime_posture.py", "--check"),)),
        SanityStep(STAGE_NAMES[8], (_py("tools/evidence/generate_bodygraph_policy_proofs.py", "--check"),)),
        SanityStep(STAGE_NAMES[9], (_py("tools/evidence/generate_architecture_snapshot.py", "--check"),)),
        SanityStep(STAGE_NAMES[10], (
            ("__validate_pr05_proofs__",),
            _py("tools/evidence/generate_v2_mapped_cache_evidence.py", "--check"),
        )),
        SanityStep(STAGE_NAMES[11], (("__validate_historical_ops01__",),)),
        SanityStep(STAGE_NAMES[12], (("__validate_ops02__",),)),
        SanityStep(STAGE_NAMES[13], (("__validate_ops03__",),)),
        SanityStep(STAGE_NAMES[14], (_py("tools/evidence/update_evidence_index.py"), _py("tools/evidence/update_evidence_index.py", "--check"))),
        SanityStep(STAGE_NAMES[15], (_py("tools/evidence/validate_evidence_paths.py"),)),
        SanityStep(STAGE_NAMES[16], (("ci/checks/check_mirror_schema.sh",), ("bash", "ci/checks/check_evidence_index_hash.sh"))),
        SanityStep(
            STAGE_NAMES[17],
            (_py("tools/evidence/orientation_demo.py", "--check"),),
        ),
        SanityStep(STAGE_NAMES[18], (("ci/checks/check_final_lf.sh",),)),
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
    messages = {
        "NON_UTF8_RETAINED_TEXT": "is not UTF-8 secret-safe evidence",
        "FORBIDDEN_SERVICE_URI": "contains an unredacted service URI",
        "UNREDACTED_BEARER_VALUE": "contains an unredacted bearer value",
        "UNREDACTED_VENDOR_HEADER_VALUE": "contains an unredacted vendor header value",
        "UNREDACTED_CREDENTIAL_VALUE": "contains an unredacted credential value",
        "UNREDACTED_BIRTH_INPUT_VALUE": "contains an unredacted birth-input value",
        "UNSAFE_RAW_PAYLOAD_MARKER_VALUE": "contains persisted raw request, response, or vendor data",
    }
    for name in required:
        if name == "checksums.sha256":
            continue
        path = packet / name
        try:
            payload = path.read_bytes()
        except OSError as exc:
            raise ValueError(f"{packet.name}: {name} is not readable secret-safe evidence") from exc
        errors = validate_retained_text_safety(path, payload)
        if errors:
            raise ValueError(f"{packet.name}: {name} {messages[errors[0]]}")


def validate_pr05_path_proof_prerequisites(root: Path = ROOT) -> None:
    """Require the inherited PR-05 proof siblings before Stage 11 can rewrite primaries."""
    for rel in PR05_PRIMARY_PATHS:
        primary = root / rel
        proof = root / f"{rel}.path_proof.txt"
        if not primary.is_file() or primary.stat().st_size == 0:
            raise ValueError(f"pr-05: required primary is missing or empty: {rel}")
        if not proof.is_file() or proof.stat().st_size == 0:
            raise ValueError(f"pr-05: required path proof is missing or empty: {rel}.path_proof.txt")
        fields: dict[str, str] = {}
        try:
            for line in proof.read_text(encoding="utf-8").splitlines():
                if line.strip() and ":" in line:
                    key, value = line.split(":", 1)
                    fields[key.strip()] = value.strip()
        except (OSError, UnicodeError) as exc:
            raise ValueError(f"pr-05: path proof is not readable UTF-8: {rel}.path_proof.txt") from exc
        try:
            primary_stat = primary.stat()
            digest = hashlib.sha256(primary.read_bytes()).hexdigest()
            size_matches = int(fields.get("size_bytes", "")) == primary_stat.st_size
            mtime_utc = dt.datetime.fromisoformat(
                fields.get("mtime_utc", "").replace("Z", "+00:00")
            )
            produced_at_utc = dt.datetime.fromisoformat(
                fields.get("produced_at_utc", "").replace("Z", "+00:00")
            )
            timestamps_valid = (
                mtime_utc.tzinfo == dt.timezone.utc
                and produced_at_utc.tzinfo == dt.timezone.utc
                and mtime_utc.microsecond == 0
                and produced_at_utc.microsecond == 0
            )
        except (OSError, ValueError):
            digest = ""
            size_matches = False
            timestamps_valid = False
        if (
            fields.get("path") != rel
            or fields.get("sha256") != digest
            or not size_matches
            or not timestamps_valid
        ):
            raise ValueError(f"pr-05: path proof does not bind the inherited primary: {rel}.path_proof.txt")


def _require_log_predicates(path: Path, required: Sequence[str]) -> None:
    try:
        text = path.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"ops-02: {path.name} is not readable UTF-8 evidence") from exc
    if not text.startswith("PASS ") or any(token not in text.split() for token in required):
        raise ValueError(f"ops-02: {path.name} predicate failed")


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


def _validate_ops02_production_refusal(root: Path) -> None:
    """Corroborate the live OPS claim without substituting fixture evidence for it."""
    manifest_path = root / "artifacts/bodygraph/v2_mapped_cache/manifest.json"
    refusal_rel = "artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log"
    refusal_path = root / refusal_rel
    try:
        manifest = _read_json(manifest_path)
        refusal_bytes = refusal_path.read_bytes()
    except OSError as exc:
        raise ValueError(
            "ops-02: production-like refusal lacks independent PR-05 predicate evidence"
        ) from exc
    except ValueError as exc:
        raise ValueError(
            "ops-02: production-like refusal lacks independent PR-05 predicate evidence"
        ) from exc
    predicates = manifest.get("predicates")
    nonclaims = manifest.get("nonclaims")
    artifacts = manifest.get("artifacts")
    refusal_records = (
        [item for item in artifacts if isinstance(item, dict) and item.get("path") == refusal_rel]
        if isinstance(artifacts, list)
        else []
    )
    refusal_sha = hashlib.sha256(refusal_bytes).hexdigest()
    if (
        manifest.get("schema") != "bodygraph.v2_mapped_cache.manifest.v1"
        or manifest.get("status") != "PASS"
        or not isinstance(predicates, dict)
        or predicates.get("production_like_refused") is not True
        or predicates.get("closed_rails_zero_io") is not True
        or not isinstance(nonclaims, list)
        or "no_ops_execution" not in nonclaims
        or "no_production_authorization" not in nonclaims
        or len(refusal_records) != 1
        or refusal_records[0].get("sha256") != refusal_sha
        or refusal_records[0].get("size") != len(refusal_bytes)
        or refusal_bytes
        != b"PASS code=PROVIDER_REFUSED safe_mode=1 allow_network=0 vendor_calls=0 db_calls=0\n"
    ):
        raise ValueError(
            "ops-02: production-like refusal lacks independent PR-05 predicate evidence"
        )


def _validate_packet_inventory(
    root: Path, package: str, required: Sequence[str]
) -> Path:
    packet = root / "audit/ops/hde-epic038" / package
    for name in required:
        path = packet / name
        if path.is_symlink() or not path.is_file() or path.stat().st_size == 0:
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
    try:
        checksum_lines = (packet / "checksums.sha256").read_text(encoding="ascii").splitlines()
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"{package}: checksums.sha256 is not readable ASCII evidence") from exc
    for line_number, line in enumerate(checksum_lines, 1):
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
    return packet


def validate_historical_bridge_evidence(root: Path = ROOT) -> None:
    """Validate the frozen bridge family without re-deriving historical success."""

    bridge_root = root / "artifacts/db_bridge"
    expected_bridge_entries = {
        Path(relative).name
        for relative in HISTORICAL_BRIDGE_PRIMARY_SHA256
        if Path(relative).parent.as_posix() == "artifacts/db_bridge"
    }
    expected_bridge_entries |= {
        f"{name}.path_proof.txt" for name in expected_bridge_entries
    }
    if bridge_root.is_symlink() or not bridge_root.is_dir():
        raise ValueError("historical bridge directory is missing or unsafe")
    actual_bridge_entries = {entry.name for entry in bridge_root.iterdir()}
    unexpected = sorted(actual_bridge_entries - expected_bridge_entries)
    if unexpected:
        raise ValueError(
            f"historical bridge directory inventory drift: {unexpected[0]}"
        )

    for relative, frozen_sha256 in HISTORICAL_BRIDGE_PRIMARY_SHA256.items():
        primary = root / relative
        proof = root / f"{relative}.path_proof.txt"
        if primary.is_symlink() or not primary.is_file() or not primary.read_bytes():
            raise ValueError(f"historical bridge primary is missing: {relative}")
        payload = primary.read_bytes()
        if hashlib.sha256(payload).hexdigest() != frozen_sha256:
            raise ValueError(f"historical bridge primary drift: {relative}")
        if validate_retained_text_safety(primary, payload):
            raise ValueError(f"historical bridge primary is not secret-safe: {relative}")
        if relative.endswith(".json"):
            value = _read_json(primary)
            if payload != (
                json.dumps(
                    value,
                    ensure_ascii=True,
                    separators=(",", ":"),
                    sort_keys=True,
                )
                + "\n"
            ).encode("utf-8"):
                raise ValueError(f"historical bridge JSON is not canonical: {relative}")
        if proof.is_symlink() or not proof.is_file() or not proof.read_bytes():
            raise ValueError(f"historical bridge path proof is missing: {relative}")
        fields: dict[str, str] = {}
        for line in proof.read_text(encoding="utf-8").splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
        if (
            fields.get("path") != relative
            or fields.get("sha256") != frozen_sha256
            or fields.get("size_bytes") != str(primary.stat().st_size)
            or not fields.get("mtime_utc")
            or not fields.get("produced_at_utc")
        ):
            raise ValueError(f"historical bridge path proof drift: {relative}")

    packet = _validate_packet_inventory(root, "ops-01", HISTORICAL_OPS01_FILES)
    ledger = (packet / "checksums.sha256").read_bytes()
    if hashlib.sha256(ledger).hexdigest() != HISTORICAL_OPS01_LEDGER_SHA256:
        raise ValueError("ops-01: frozen historical checksum ledger drift")
    for name in HISTORICAL_OPS01_FILES:
        primary = packet / name
        proof = packet / f"{name}.path_proof.txt"
        if proof.is_symlink() or not proof.is_file() or not proof.read_bytes():
            raise ValueError(f"ops-01: historical path proof is missing: {name}")
        fields: dict[str, str] = {}
        for line in proof.read_text(encoding="utf-8").splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
        expected_path = f"audit/ops/hde-epic038/ops-01/{name}"
        if (
            fields.get("path") != expected_path
            or fields.get("sha256") != hashlib.sha256(primary.read_bytes()).hexdigest()
            or fields.get("size_bytes") != str(primary.stat().st_size)
            or not fields.get("mtime_utc")
            or not fields.get("produced_at_utc")
        ):
            raise ValueError(f"ops-01: historical path proof drift: {name}")
        if not name.endswith(".json"):
            continue
        value = _read_json(primary)
        if primary.read_bytes() != (
            json.dumps(value, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
            + "\n"
        ).encode("utf-8"):
            raise ValueError(f"ops-01: historical JSON is not canonical: {name}")
    nonclaims = _read_json(packet / "nonclaims.json").get("nonclaims")
    required_nonclaims = {
        "no_acceptance_token_claim",
        "no_epic_closeout_claim",
        "no_pf09_status_movement",
        "no_qa_pass_claim",
    }
    if not isinstance(nonclaims, list) or not required_nonclaims.issubset(nonclaims):
        raise ValueError("ops-01: historical nonclaims are incomplete")


def validate_ops02_package(root: Path = ROOT) -> None:
    package = "ops-02"
    packet = _validate_packet_inventory(root, package, OPS02_FILES)
    commands_bytes = (packet / "commands.txt").read_bytes()
    if hashlib.sha256(commands_bytes).hexdigest() != OPS02_COMMANDS_SHA256:
        raise ValueError("ops-02: commands.txt is not the approved command surface")
    if (packet / "exit_code.txt").read_text(encoding="utf-8").strip() != "0":
        raise ValueError(f"{package}: exit_code.txt is not successful")
    summary = _read_json(packet / "result_summary.json")
    nonclaims = _read_json(packet / "nonclaims.json").get("nonclaims", [])
    required_nonclaims = {"no_qa_pass_claim", "no_acceptance_token_claim", "no_pf09_status_movement", "no_epic_closeout_claim"}
    if not isinstance(nonclaims, list) or not all(isinstance(item, str) for item in nonclaims) or not required_nonclaims.issubset(nonclaims):
        raise ValueError(f"{package}: nonclaims.json is incomplete")
    if package == "ops-02":
        route_policy = _validate_ops02_environment(packet)
        predicates = summary.get("predicates", {})
        if not isinstance(predicates, dict):
            raise ValueError("ops-02: result_summary.json predicates must be an object")
        required_predicates = {"adapter_mapped", "exactly_one_vendor_request", "canonical_write_read_back_equivalence", "idempotent_repeated_write", "mapped_payload_only", "normalized_identity_single_row", "production_like_refused", "explicit_legacy_fallback_preserved", "retained_by_po_decision"}
        if summary.get("status") != "PASS" or summary.get("retention_decision") != "retain" or any(predicates.get(key) is not True for key in required_predicates):
            raise ValueError("ops-02: result_summary.json PASS predicate failed")
        _validate_ops02_production_refusal(root)
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
        durable_provider = read_back.get("provider")
        if not isinstance(canonical_sha, str) or not re.fullmatch(r"[0-9a-f]{64}", canonical_sha) or durable_provider != "psycopg" or read_back.get("canonical_sha256") != canonical_sha or read_back.get("read_back_match") is not True or read_back.get("identity_rows") != 1 or read_back.get("retention_decision") != "retain" or read_back.get("stored_payload_posture") != "adapter_mapped_no_raw_vendor_payload":
            raise ValueError("ops-02: read_back_summary.json predicate failed")
        if stdout.get("status") != "ok" or stdout.get("provider") != durable_provider or stdout.get("vendor_requests") != 1 or stdout.get("adapter_status") != "ADAPTER_MAPPED" or stdout.get("canonical_sha256") != canonical_sha or stdout.get("read_back_match") is not True or stdout.get("idempotent") is not True or stdout.get("identity_rows") != 1 or stdout.get("second_write_rows") != 0 or stdout.get("retention_decision") != "retain":
            raise ValueError("ops-02: stdout.log predicate failed")
        _require_log_predicates(packet / "canonical_parity.log", (f"canonical_sha256={canonical_sha}", "pre_write_post_read_match=true", "first_read_back_match=true", "second_read_back_match=true"))
        _require_log_predicates(packet / "idempotence.log", ("first_rows_written=1", "second_rows_written=0", "identity_rows=1", "canonical_hash_unchanged=true"))
        _require_log_predicates(packet / "no_raw_vendor_payload_persistence.log", ("payload_posture=adapter_mapped_no_raw_vendor_payload", "raw_standard_response=false", "raw_chart_result_envelope=false", "request_body=false", "response_body=false", "secrets=false"))
        _require_log_predicates(packet / "legacy_fallback_preservation.log", ("classification=explicit_legacy_fallback", "route_family=legacy_bodygraph", "configured_v2_legacy_fallback=false", "external_io=0"))


def validate_ops_packages(root: Path = ROOT) -> None:
    """Compatibility helper for tests; stages invoke the validators separately."""

    validate_historical_bridge_evidence(root)
    validate_ops02_package(root)


def validate_direct_selection_contract() -> None:
    """Exercise the direct-selection producer in memory without writing evidence."""

    from tools.evidence import generate_hde_epic038_direct_db_selection as direct

    first = direct.build()
    second = direct.build()
    if (
        direct.validate_contract(first)
        or first.get("result") != "PASS"
        or direct.canonical_bytes(first) != direct.canonical_bytes(second)
    ):
        raise ValueError("direct selection contract validation failed")


def _ops03_json(files: Mapping[str, bytes], name: str) -> dict:
    from tools.evidence import hde_epic038_ops03 as ops03

    try:
        value = json.loads(files[name].decode("utf-8", "strict"))
    except (KeyError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"ops-03: {name} is not canonical JSON") from exc
    if not isinstance(value, dict) or files[name] != ops03.canonical_bytes(value):
        raise ValueError(f"ops-03: {name} is not canonical JSON")
    schema_name = ops03.JSON_SCHEMAS[name]
    if not ops03._schema_valid(value, schema_name):
        raise ValueError(f"ops-03: {name} schema validation failed")
    return value


def validate_ops03_tracked_packet(root: Path = ROOT) -> None:
    """Validate an admitted packet without executing OPS-03 or external I/O."""

    from tools.evidence import hde_epic038_ops03 as ops03

    packet = root / OPS03_TRACKED_ROOT
    if packet.is_symlink():
        raise ValueError("ops-03: tracked packet root is not a real directory")
    if not packet.exists():
        raise Ops03PacketUnavailable(PR_A_NONFINAL_REASON)
    if not packet.is_dir():
        raise ValueError("ops-03: tracked packet root is not a real directory")
    try:
        entries = tuple(packet.iterdir())
    except OSError as exc:
        raise ValueError("ops-03: tracked packet is not readable") from exc
    expected = set(ops03.FINAL_FILES)
    allowed = expected | {f"{name}.path_proof.txt" for name in expected}
    unexpected = sorted(entry.name for entry in entries if entry.name not in allowed)
    if unexpected:
        raise ValueError(f"ops-03: unexpected tracked entry {unexpected[0]}")
    files: dict[str, bytes] = {}
    for name in expected:
        path = packet / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"ops-03: required file {name} is missing or unsafe")
        files[name] = path.read_bytes()
        if name != "stderr.log" and not files[name]:
            raise ValueError(f"ops-03: required file {name} is empty")
    _validate_secret_safety(packet, tuple(sorted(expected)))
    if files["stdout.log"] != b"OPS03_CAPTURE_PASS\n" or files["stderr.log"] != b"":
        raise ValueError("ops-03: success logs are not exact")
    if files["exit_code.txt"] != b"0\n":
        raise ValueError("ops-03: exit code is not exact")

    checksum_rows: dict[str, str] = {}
    for number, line in enumerate(files[ops03.CHECKSUM_FILE].decode("ascii").splitlines(), 1):
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if not match or match.group(2) in checksum_rows:
            raise ValueError(f"ops-03: checksum row {number} is malformed")
        checksum_rows[match.group(2)] = match.group(1)
    if tuple(sorted(checksum_rows)) != ops03.CHECKSUM_INPUTS:
        raise ValueError("ops-03: checksum inventory is not exact")
    if any(
        checksum_rows[name] != hashlib.sha256(files[name]).hexdigest()
        for name in ops03.CHECKSUM_INPUTS
    ):
        raise ValueError("ops-03: checksum mismatch")

    values = {
        name: _ops03_json(files, name)
        for name in ops03.JSON_SCHEMAS
    }
    posture = values["db_posture_summary.json"]
    env = values["env_presence.json"]
    nonclaims = values["nonclaims.json"]
    summary = values["result_summary.json"]
    receipt = values[ops03.RECEIPT_FILE]
    run_id = summary.get("run_id")
    source_commit = summary.get("source_commit")
    authorization_sha256 = summary.get("authorization_sha256")
    query_results = posture.get("query_results")
    if (
        not isinstance(run_id, str)
        or re.fullmatch(r"[a-z0-9][a-z0-9-]{15,63}", run_id) is None
        or any(value.get("run_id") != run_id for value in values.values())
        or not isinstance(source_commit, str)
        or re.fullmatch(r"[0-9a-f]{40}", source_commit) is None
        or posture.get("source_commit") != source_commit
        or not isinstance(authorization_sha256, str)
        or re.fullmatch(r"[0-9a-f]{64}", authorization_sha256) is None
        or receipt.get("authorization_sha256") != authorization_sha256
        or posture.get("provider") != "psycopg"
        or posture.get("selection_attempts")
        != [{"provider": "psycopg", "status": "ok", "reason": None}]
        or posture.get("ordered_query_ids") != list(ops03.ORDERED_QUERY_IDS)
        or not isinstance(query_results, list)
        or [row.get("query_id") for row in query_results if isinstance(row, dict)]
        != list(ops03.ORDERED_QUERY_IDS)
        or posture.get("counts") != ops03.EXPECTED_COUNTS
        or posture.get("result") != "PASS"
        or set(posture.get("predicates", {})) != set(ops03.POSTURE_PREDICATES)
        or not all(posture["predicates"].values())
        or nonclaims.get("nonclaims") != list(ops03.NONCLAIMS)
        or summary.get("capture_result") != "PASS"
        or summary.get("primary_files") != list(ops03.PRIMARY_FILES)
        or set(summary.get("decisive_predicates", {})) != set(ops03.POSTURE_PREDICATES)
        or not all(summary["decisive_predicates"].values())
        or receipt.get("validated_files") != list(ops03.PRIMARY_FILES)
        or set(receipt.get("predicates", {})) != set(ops03.RECEIPT_PREDICATES)
        or not all(receipt["predicates"].values())
        or receipt.get("result") != "PASS"
    ):
        raise ValueError("ops-03: packet contract disagreement")

    command_lines = files["commands.txt"].splitlines(keepends=True)
    if len(command_lines) != 3:
        raise ValueError("ops-03: command inventory is not exact")
    commands: list[list[str]] = []
    command_names = ("capture", "receipt", "validate")
    for name, line in zip(command_names, command_lines):
        prefix = f"{name}_argv=".encode("ascii")
        if not line.startswith(prefix):
            raise ValueError("ops-03: command row identity is invalid")
        try:
            command = json.loads(line[len(prefix):].decode("utf-8", "strict"))
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise ValueError("ops-03: command row is invalid") from exc
        if (
            not isinstance(command, list)
            or not command
            or not all(isinstance(item, str) for item in command)
            or line
            != prefix
            + (json.dumps(command, sort_keys=True, separators=(",", ":")) + "\n").encode(
                "utf-8"
            )
        ):
            raise ValueError("ops-03: command row is not canonical")
        commands.append(command)
    interpreter = commands[0][0]
    authorization = commands[0][5] if len(commands[0]) > 5 else ""
    candidate = f"/tmp/hde-epic038-ops03/{run_id}/candidate"
    runner_path = commands[0][3] if len(commands[0]) > 3 else ""
    validator_path = commands[1][3] if len(commands[1]) > 3 else ""
    if (
        not runner_path.endswith("/scripts/ops/hde_epic038_ops03.py")
        or not validator_path.endswith("/tools/evidence/hde_epic038_ops03.py")
        or not Path(authorization).is_absolute()
        or "\x00" in authorization
        or commands[2][3:4] != [validator_path]
        or commands[0]
        != [interpreter, "-I", "-B", runner_path, "--authorization", authorization]
        or commands[1]
        != [
            interpreter,
            "-I",
            "-B",
            validator_path,
            "--emit-receipt",
            "--authorization",
            authorization,
            "--candidate",
            candidate,
        ]
        or commands[2]
        != [
            interpreter,
            "-I",
            "-B",
            validator_path,
            "--validate",
            "--authorization",
            authorization,
            "--candidate",
            candidate,
        ]
    ):
        raise ValueError("ops-03: authorized command shape disagreement")


def _run_command(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(DETERMINISM_ENV_PINS)
    if any(item.endswith("generate_a7_transport_proofs.py") for item in command):
        env["HDE_WRITE_A7_PROOFS"] = "1"
    return subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True)


def _run_stage(step: SanityStep) -> int:
    for command in step.commands:
        if command == ("__validate_pr05_proofs__",):
            try:
                validate_pr05_path_proof_prerequisites()
            except Exception:
                print("pr05_path_proof_validation_failed", file=sys.stderr)
                return 1
        elif command == ("__validate_direct_selection__",):
            try:
                validate_direct_selection_contract()
            except Exception:
                print("direct_selection_contract_validation_failed", file=sys.stderr)
                return 1
        elif command == ("__validate_historical_ops01__",):
            try:
                validate_historical_bridge_evidence()
            except Exception:
                print("historical_ops01_integrity_validation_failed", file=sys.stderr)
                return 1
        elif command == ("__validate_ops02__",):
            try:
                validate_ops02_package()
            except Exception:
                print("ops02_packet_validation_failed", file=sys.stderr)
                return 1
        elif command == ("__validate_ops03__",):
            try:
                validate_ops03_tracked_packet()
            except Ops03PacketUnavailable as exc:
                print(str(exc), file=sys.stderr)
                return PR_A_NONFINAL_EXIT
            except Exception:
                print("ops03_packet_validation_failed", file=sys.stderr)
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
    lines = ["run:sanity-pipeline", f"pipeline_identity:{PIPELINE_ID}", "env:" + ",".join(f"{key}={DETERMINISM_ENV_PINS[key]}" for key in sorted(DETERMINISM_ENV_PINS)), "env_pins:audit/gates/determinism/env_pins.log", "ops_evidence:retained_integrity_provenance_secret_safe_only;historical_nonclaim=true;not_rerun=true"]
    if any(status == "NONFINAL_MISSING_OPS03" for _, status in results):
        lines.extend(
            (
                "pr_a_state:nonfinal_fail_closed",
                f"final_readiness_blocked:{PR_A_NONFINAL_REASON}",
            )
        )
    for name, status in results:
        canonical_status = "OK" if status == "OK" else "FAIL"
        lines.append(f"check {name}:{canonical_status}")
        if name == STAGE_NAMES[11] and status == "OK":
            lines.append("stage_result:12:HISTORICAL_INTEGRITY_OK")
        if status.startswith("NOT_EXECUTED_EARLIER_FAILURE:"):
            lines.append(f"not_executed {name}:earlier_mandatory_failure={status.split(':', 1)[1]}")
    lines.extend((f"first_failed_stage:{first_failure}", f"summary:{summary}"))
    return ("\n".join(lines) + "\n").encode("utf-8")


def _write_log(path: Path, results: Sequence[tuple[str, str]], first_failure: str, summary: str) -> bytes:
    data = _render_log(results, first_failure, summary)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        current = path.read_bytes()
    except OSError:
        current = None
    if current != data:
        path.write_bytes(data)
    return data


def _rebind_failure_log() -> int:
    """Bind only the final FAIL log while preserving the evidence topology."""
    result = _run_command(
        _py("tools/evidence/update_evidence_index.py", "--rebind-sanity-log")
    )
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
    sealing_index = next(
        (index for index, step in enumerate(roster) if step.name == STAGE_NAMES[14]),
        len(roster) - 1,
    )
    for index, step in enumerate(roster):
        # The final updater must bind the final sanity bytes, not an interim
        # version.  Render the prospective PASS log before that updater runs;
        # the normal final render below is byte-identical on success.
        if canonical_run and index == sealing_index and failure == "NONE":
            prospective_pass = _write_log(
                log_path,
                [*results, *((later.name, "OK") for later in roster[index:])],
                "NONE",
                "PASS",
            )
        code = _run_stage(step)
        status = (
            "OK"
            if code == 0
            else (
                "NONFINAL_MISSING_OPS03"
                if code == PR_A_NONFINAL_EXIT and step.name == STAGE_NAMES[13]
                else "FAIL"
            )
        )
        results.append((step.name, status))
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
                return 1 if seal_code == PR_A_NONFINAL_EXIT else seal_code
            return 1
        return 0

    try:
        prior_final_bytes = log_path.read_bytes()
    except OSError:
        prior_final_bytes = None
    _write_log(log_path, results, failure, "PASS" if passed else "FAIL")
    if not passed and canonical_run and prior_final_bytes != final_bytes:
        seal_code = _rebind_failure_log()
        if seal_code:
            print(f"canonical FAIL evidence finalization failed with exit code {seal_code}", file=sys.stderr)
            return 1 if seal_code == PR_A_NONFINAL_EXIT else seal_code
    return 0 if passed else (code or 1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-path", type=Path, default=SANITY_LOG)
    args = parser.parse_args(argv)
    return run_pipeline(log_path=args.log_path)


if __name__ == "__main__":
    raise SystemExit(main())
