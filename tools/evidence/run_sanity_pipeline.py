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
OPS01_PROVIDER_PROOF_SCHEMA = "hde_epic038.ops01.provider_parity.v4"
OPS01_STAGING_ROOT = "/tmp/hde-epic038-ops01-provider-selection-6d5de673-20260717t235802z"
OPS01_DIRECT_PROVIDER = "psycopg"
OPS01_BRIDGE_PROVIDER = "bridge"
OPS_COMMANDS_SHA256 = {
    "ops-01": "038c4f8fe7735c41a3679e7f80ba99f2cb23632fbf37a33bf70ddf0884087e45",
    "ops-02": "d3ca676d0157ce30bf64d4b419610e3a5ceebc0dc13785475028b90ed31f163b",
}
OPS01_MUTATING_SQL = re.compile(
    r"(?im)^\s*(?:INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE|CREATE|GRANT|REVOKE|MERGE|COPY)\b"
)
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
    "bodygraph_provider_selection_provenance",
    "bodygraph_selector_approved",
    "four_row_corpus_exact",
    "provider_selection_consistent",
    "search_path_exact",
}
OPS01_SELECTION_SNAPSHOT_CONTENT = {
    "direct": {
        "schema": "v1",
        "selected": OPS01_DIRECT_PROVIDER,
        "attempts": [{"provider": OPS01_DIRECT_PROVIDER, "status": "ok"}],
        "selection_order": [OPS01_DIRECT_PROVIDER],
        "flags": {
            "env": "dev",
            "force_pg": True,
            "force_bridge": False,
            "allow_bridge_prod": False,
        },
    },
    "bridge": {
        "schema": "v1",
        "selected": OPS01_BRIDGE_PROVIDER,
        "attempts": [{"provider": OPS01_BRIDGE_PROVIDER, "status": "ok"}],
        "selection_order": [OPS01_BRIDGE_PROVIDER],
        "flags": {
            "env": "dev",
            "force_pg": False,
            "force_bridge": True,
            "allow_bridge_prod": False,
        },
    },
}

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
        SanityStep(STAGE_NAMES[1], (
            _py("tools/evidence/generate_identity_provenance.py"),
            _py("tools/evidence/generate_release_bindings.py"),
            _py("tools/evidence/generate_env_matrix_snapshot.py"),
            _py("scripts/release_id_recompute.py", "--check"),
            _py("ci/checks/check_release_identity.sh"),
        )),
        SanityStep(STAGE_NAMES[2], (_py("tools/evidence/run_canonical_json_gate.py", "--check-only"),)),
        SanityStep(STAGE_NAMES[3], (_py("tools/evidence/generate_determinism_gate_proofs.py"), _py("tools/evidence/generate_open_rails_abba_proof.py", "--check"), _py("tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check"))),
        SanityStep(STAGE_NAMES[4], (_py("tools/evidence/generate_a7_transport_proofs.py"),)),
        SanityStep(STAGE_NAMES[5], (_py("tools/evidence/generate_rails_gate_evidence.py"), _py("ci/checks/run_rails_job_definitions.py", "ci/jobs/rails_closed_refusal.yml", "ci/jobs/rails_open_conformance.yml", "ci/jobs/logs_keys_only_redaction.yml"))),
        SanityStep(STAGE_NAMES[6], (_py("tools/evidence/generate_db_runtime_posture.py"),)),
        SanityStep(STAGE_NAMES[7], (_py("tools/evidence/generate_bodygraph_policy_proofs.py"),)),
        SanityStep(STAGE_NAMES[8], (_py("tools/evidence/generate_db_bridge_parity.py"),)),
        SanityStep(STAGE_NAMES[9], (_py("tools/evidence/generate_architecture_snapshot.py"),)),
        SanityStep(STAGE_NAMES[10], (
            ("__validate_pr05_proofs__",),
            _py("tools/evidence/generate_v2_mapped_cache_evidence.py"),
        )),
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
    retained_value = (
        r'(?:"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|'
        r'presence\((?:"[^"]*"|\'[^\']*\')\)|'
        r'\$\{[^}\r\n]*\}|[^\s,"\'}\]]+)'
    )
    credential_assignment = re.compile(
        rf"(?i)(?P<key_quote>[\"']?)\b(?:DATABASE_URL|DB_BRIDGE_URL|HD_API_KEY|GEO_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL)\b(?P=key_quote)\s*[:=]\s*(?P<value>{retained_value})"
    )
    bearer = re.compile(rf"(?i)\bBearer\s+(?P<value>{retained_value})")
    vendor_header = re.compile(
        rf"(?i)(?P<key_quote>[\"']?)\bHD-(?:Geocode|Api)-Key\b(?P=key_quote)\s*[:=]\s*(?P<value>{retained_value})"
    )
    birth_assignment = re.compile(
        rf"(?i)(?P<key_quote>[\"']?)\b(?:birth[-_]?date|date[-_]?of[-_]?birth|dob|birth[-_]?time|time[-_]?of[-_]?birth|birth[-_]?place|place[-_]?of[-_]?birth|birth[-_]?location|location)\b(?P=key_quote)\s*[:=]\s*(?P<value>{retained_value})"
    )
    birth_option = re.compile(
        rf"(?i)--(?:birth[-_]?date|date[-_]?of[-_]?birth|dob|birth[-_]?time|time[-_]?of[-_]?birth|birth[-_]?place|place[-_]?of[-_]?birth|birth[-_]?location|location)(?:=|\s+)(?P<value>{retained_value})"
    )
    forbidden_uri = re.compile(r"(?i)\b(?:postgres(?:ql)?|railway)://")

    def _normalized_value(raw: str) -> str:
        value = raw.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
            value = value[1:-1]
        return value

    def _value_is_safe(
        raw: str, allowed: set[str], *, allow_presence: bool = False
    ) -> bool:
        value = _normalized_value(raw)
        if value.lower() in allowed or SAFE_ENV_REFERENCE.fullmatch(value) is not None:
            return True
        return allow_presence and re.fullmatch(
            r"presence\((['\"])(?:DATABASE_URL|DB_BRIDGE_URL|HD_API_KEY|GEO_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL)\1\)",
            value,
            flags=re.IGNORECASE,
        ) is not None

    def _birth_value_is_safe(raw: str) -> bool:
        value = _normalized_value(raw)
        lowered = value.lower()
        if lowered in {
            "<redacted>",
            "redacted",
            "set:redacted",
            "unset",
            "none",
            "null",
            "false",
            "not-recorded",
            "not_recorded",
            "***",
        }:
            return True
        if SAFE_ENV_REFERENCE.fullmatch(value):
            return True
        return bool(
            re.fullmatch(
                r"<approved-synthetic-(?:birthdate|birthtime|location)>", lowered
            )
        )

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
            if not _value_is_safe(match.group("value"), {"<redacted>", "redacted"}):
                raise ValueError(f"{packet.name}: {name} contains an unredacted bearer value")
        for match in vendor_header.finditer(text):
            if not _value_is_safe(
                match.group("value"),
                {"<redacted>", "redacted", "set:redacted", "set", "unset", "***"},
            ):
                raise ValueError(f"{packet.name}: {name} contains an unredacted vendor header value")
        for match in credential_assignment.finditer(text):
            if not _value_is_safe(
                match.group("value"),
                {"redacted", "<redacted>", "set:redacted", "set", "unset"},
                allow_presence=True,
            ):
                raise ValueError(f"{packet.name}: {name} contains an unredacted credential value")
        for pattern in (birth_assignment, birth_option):
            for match in pattern.finditer(text):
                if not _birth_value_is_safe(match.group("value")):
                    raise ValueError(
                        f"{packet.name}: {name} contains an unredacted birth-input value"
                    )
        raw_payload_key = re.compile(
            r'(?i)"(?:raw_vendor_(?:payload|envelope)|raw_(?:request|response)_body)"\s*:'
        )
        safe_raw_value = re.compile(
            r'(?i)^(?:false|null|"(?:none|redacted)")(?=\s*(?:[,}\]\n]|$))'
        )
        for match in raw_payload_key.finditer(text):
            if not safe_raw_value.match(text[match.end():].lstrip()):
                raise ValueError(f"{packet.name}: {name} contains persisted raw request, response, or vendor data")


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
                mtime_utc.tzinfo is not None
                and produced_at_utc.tzinfo is not None
                and mtime_utc.astimezone(dt.timezone.utc)
                <= dt.datetime.fromtimestamp(primary_stat.st_mtime, tz=dt.timezone.utc)
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


def _canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
        + "\n"
    ).encode("utf-8")


def _validate_bodygraph_selection_snapshot(bodygraph: dict, side: str) -> None:
    provider = OPS01_DIRECT_PROVIDER if side == "direct" else OPS01_BRIDGE_PROVIDER
    provider_row = bodygraph.get(side)
    snapshot = provider_row.get("selection_snapshot") if isinstance(provider_row, dict) else None
    if not isinstance(snapshot, dict):
        raise ValueError(f"ops-01: {side} BodyGraph selection snapshot is missing or malformed")
    content = snapshot.get("content")
    expected_content = OPS01_SELECTION_SNAPSHOT_CONTENT[side]
    if not isinstance(content, dict) or _canonical_json_bytes(content) != _canonical_json_bytes(expected_content):
        raise ValueError(f"ops-01: {side} BodyGraph selection snapshot content drift")
    expected_path = (
        f"{OPS01_STAGING_ROOT}/{side}-cwd/artifacts/db_bridge/"
        "adapter_selection.snapshot.json"
    )
    if snapshot.get("path") != expected_path:
        raise ValueError(f"ops-01: {side} BodyGraph selection snapshot path substitution")
    digest = snapshot.get("sha256")
    recomputed = hashlib.sha256(_canonical_json_bytes(content)).hexdigest()
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest) or digest != recomputed:
        raise ValueError(f"ops-01: {side} BodyGraph selection snapshot hash drift")
    if content.get("selected") != provider or provider_row.get("provider") != provider:
        raise ValueError(f"ops-01: {side} BodyGraph selection snapshot provider substitution")


def _compare_provider_values(rows: Sequence[dict]) -> str:
    by_name = {row["name"]: row for row in rows}
    for name in OPS01_PARITY_ROWS[:-1]:
        row = by_name[name]
        if _normalized_provider_value(name, row["direct"]) != _normalized_provider_value(name, row["bridge"]):
            raise ValueError(f"ops-01: provider values disagree for {name}")
    bodygraph = by_name["bodygraph_payload_row"]
    _validate_bodygraph_selection_snapshot(bodygraph, "direct")
    _validate_bodygraph_selection_snapshot(bodygraph, "bridge")
    direct_sha = bodygraph["direct"].get("canonical_sha256")
    bridge_sha = bodygraph["bridge"].get("canonical_sha256")
    if (
        not isinstance(direct_sha, str)
        or not re.fullmatch(r"[0-9a-f]{64}", direct_sha)
        or bridge_sha != direct_sha
        or bodygraph["direct"].get("provider") != OPS01_DIRECT_PROVIDER
        or bodygraph["bridge"].get("provider") != OPS01_BRIDGE_PROVIDER
        or bodygraph.get("comparison") != "FILE_EQ_CANON_BYTES_OK"
        or bodygraph["direct"].get("raw_bodygraph_payload_recorded") is not False
        or bodygraph["bridge"].get("raw_bodygraph_payload_recorded") is not False
    ):
        raise ValueError("ops-01: BodyGraph provider identities, hashes, or persistence posture disagree")
    return direct_sha


def _validate_ops01_environment(packet: Path) -> None:
    env = _read_json(packet / "env_presence.json")
    presence = env.get("environment_presence")
    rails = env.get("execution_rails")
    if (
        env.get("secret_posture") != "presence_only"
        or not isinstance(presence, dict)
        or presence
        != {
            "ALLOW_DB_WRITE": "0",
            "ALLOW_NETWORK": "0",
            "APP_ENV": "SET:dev",
            "DATABASE_URL": "SET:REDACTED",
            "DB_BRIDGE_URL": "SET:REDACTED",
            "ENGINE_ENV": "UNSET",
            "LANG": "C",
            "LC_ALL": "C",
            "SAFE_MODE": "1",
            "TZ": "UTC",
        }
        or not isinstance(rails, dict)
        or set(rails) != OPS01_BRIDGE_COMMANDS
    ):
        raise ValueError("ops-01: env_presence.json execution posture failed")
    if any(
        not isinstance(values, dict)
        or values.get("SAFE_MODE") != "1"
        or values.get("ALLOW_NETWORK") != "0"
        or values.get("ALLOW_DB_WRITE") != "0"
        for values in rails.values()
    ):
        raise ValueError("ops-01: env_presence.json closed-rails predicates failed")
    if (
        rails["direct_bodygraph_read"].get("DB_FORCE_PG") != "1"
        or rails["direct_bodygraph_read"].get("DB_FORCE_BRIDGE") != "UNSET"
        or rails["bridge_bodygraph_read"].get("DB_FORCE_BRIDGE") != "1"
        or rails["bridge_bodygraph_read"].get("DB_FORCE_PG") != "UNSET"
    ):
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
    remediation_findings = summary.get("remediation_findings_resolved")
    if (
        parity.get("schema") != OPS01_PROVIDER_PROOF_SCHEMA
        or parity.get("remediation_marker")
        != "F-008_BODYGRAPH_PROVIDER_SELECTION_PROVENANCE"
        or not isinstance(corpus, dict)
        or corpus.get("name") != OPS01_CORPUS_NAME
        or corpus.get("ordered_rows") != list(OPS01_PARITY_ROWS)
        or row_names != OPS01_PARITY_ROWS
        or summary.get("active_parity_corpus") != OPS01_CORPUS_NAME
        or summary.get("active_parity_rows") != list(OPS01_PARITY_ROWS)
        or summary.get("literal_staging_root") != OPS01_STAGING_ROOT
        or summary.get("runner_sha256") != OPS_COMMANDS_SHA256["ops-01"]
        or not isinstance(remediation_findings, list)
        or "F-008_BODYGRAPH_PROVIDER_SELECTION_PROVENANCE"
        not in remediation_findings
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
        or parity.get("selected") != OPS01_DIRECT_PROVIDER
        or parity.get("attempts")
        != [{"provider": OPS01_DIRECT_PROVIDER, "status": "ok"}]
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
    commands_bytes = (packet / "commands.txt").read_bytes()
    if package == "ops-01" and OPS01_MUTATING_SQL.search(
        commands_bytes.decode("utf-8")
    ):
        raise ValueError("ops-01: commands.txt contains a mutating SQL command")
    if hashlib.sha256(commands_bytes).hexdigest() != OPS_COMMANDS_SHA256[package]:
        raise ValueError(f"{package}: commands.txt is not the approved command surface")
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
        if command == ("__validate_pr05_proofs__",):
            try:
                validate_pr05_path_proof_prerequisites()
            except ValueError as exc:
                print(str(exc), file=sys.stderr)
                return 1
        elif command == ("__validate_ops__",):
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
