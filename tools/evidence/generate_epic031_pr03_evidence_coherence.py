#!/usr/bin/env python3
"""Generate HDE-EPIC031 PR-03 SAFE rails evidence coherence artifacts."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env  # noqa: E402
from tools.evidence import update_evidence_index  # noqa: E402

PRODUCED_AT = "2026-05-10T17:05:00Z"
EPIC_ID = "HDE-EPIC031"
PF09_SUBTASK = "HDE-FERM001.4"
PR03_ROOT = "audit/qa/hde-epic031/pr-03"
FAMILY_MAP_REL = f"{PR03_ROOT}/evidence_family_map.json"
COHERENCE_REL = f"{PR03_ROOT}/safe_rails_evidence_coherence.json"
REFRESH_LOG_REL = f"{PR03_ROOT}/evidence_refresh.log"
HUMAN_INDEX_REL = "docs/evidence/INDEX.json"
HUMAN_INDEX_SHA_REL = "docs/evidence/INDEX.sha256"
MIRROR_REL = "artifacts/evidence_index.jsonl"
MIRROR_SHA_REL = "artifacts/evidence_index.jsonl.sha256"

PR01_ARTIFACTS = [
    "artifacts/vendor/policies_pinned.md",
    "artifacts/vendor/retry_after_parse.log",
    "audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json",
    "audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json",
    "audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json",
]
PR02_ARTIFACTS = [
    "audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl",
    "audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt",
    "audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json",
    "audit/qa/hde-epic031/pr-02/bounded_label_observability.json",
    "audit/qa/hde-epic031/pr-02/secret_redaction_scan.log",
]
PR03_ARTIFACTS = [FAMILY_MAP_REL, COHERENCE_REL, REFRESH_LOG_REL]
SAFE_RAILS_ARTIFACTS = [*PR01_ARTIFACTS, *PR02_ARTIFACTS]
INDEXED_SAFE_RAILS_ARTIFACTS = [*SAFE_RAILS_ARTIFACTS, *PR03_ARTIFACTS]
INDEX_MIRROR_REFRESH_ARTIFACTS = [HUMAN_INDEX_REL, HUMAN_INDEX_SHA_REL, MIRROR_REL, MIRROR_SHA_REL]
GOVERNED_PR03_PROOF_ARTIFACTS = [*INDEXED_SAFE_RAILS_ARTIFACTS, *INDEX_MIRROR_REFRESH_ARTIFACTS]

FAMILY_MAP: dict[str, dict[str, list[str]]] = {
    "SAFE rails open-posture proof family": {
        "artifact_paths": [
            "artifacts/vendor/policies_pinned.md",
            "audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json",
            "audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json",
        ],
        "supporting_paths": [
            "ci/jobs/rails_closed_refusal.yml",
            "ci/jobs/rails_open_conformance.yml",
        ],
    },
    "SAFE retry/backoff/typed 429 proof family": {
        "artifact_paths": [
            "artifacts/vendor/retry_after_parse.log",
            "audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json",
        ],
        "supporting_paths": [],
    },
    "SAFE rails keys-only log-redaction proof family": {
        "artifact_paths": [
            "audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl",
            "audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt",
            "audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json",
            "audit/qa/hde-epic031/pr-02/bounded_label_observability.json",
            "audit/qa/hde-epic031/pr-02/secret_redaction_scan.log",
        ],
        "supporting_paths": ["ci/jobs/logs_keys_only_redaction.yml"],
    },
    "SAFE rails governed evidence-index coherence family": {
        "artifact_paths": [FAMILY_MAP_REL, COHERENCE_REL, REFRESH_LOG_REL],
        "supporting_paths": [],
    },
    "Human Evidence Index refresh family": {
        "artifact_paths": [
            HUMAN_INDEX_REL,
            HUMAN_INDEX_SHA_REL,
            f"{HUMAN_INDEX_REL}.path_proof.txt",
            f"{HUMAN_INDEX_SHA_REL}.path_proof.txt",
        ],
        "supporting_paths": [],
    },
    "Machine Mirror refresh family": {
        "artifact_paths": [
            MIRROR_REL,
            MIRROR_SHA_REL,
            f"{MIRROR_REL}.path_proof.txt",
            f"{MIRROR_SHA_REL}.path_proof.txt",
        ],
        "supporting_paths": [],
    },
    "Path-proof validation family": {
        "artifact_paths": [f"{path}.path_proof.txt" for path in GOVERNED_PR03_PROOF_ARTIFACTS],
        "supporting_paths": [],
    },
}


BOUNDED_SIDE_EFFECT_REFRESHES = [
    {
        "family_name": "writer proof companions",
        "classification": "expected updater convergence",
        "rationale": "Global evidence-index regeneration refreshes registered writer proof companions and their Machine Mirror rows while converging path-proof metadata; no writer primary artifact behavior changed in PR-03.",
        "paths": [
            "artifacts/writer/conjunction_write_readback.log.path_proof.txt",
            "artifacts/writer/conjunction_writer_summary.json.path_proof.txt",
        ],
        "mirror_rows": [
            {
                "artifact_key": "conjunction.writer.write_readback",
                "discovered_physical_path": "artifacts/writer/conjunction_write_readback.log",
            },
            {
                "artifact_key": "conjunction.writer.summary",
                "discovered_physical_path": "artifacts/writer/conjunction_writer_summary.json",
            },
        ],
    },
    {
        "family_name": "topology orientation refresh",
        "classification": "required dependency refresh",
        "rationale": "Orientation evidence and its Machine Mirror row are regenerated after Human Index and Machine Mirror changes so topology counts and its proof companion remain coherent with the PR-03 evidence-index fixed point.",
        "paths": [
            "audit/gates/topology/orientation_demo.txt",
            "audit/gates/topology/orientation_demo.txt.path_proof.txt",
        ],
        "mirror_rows": [
            {
                "artifact_key": "topology.orientation_demo",
                "discovered_physical_path": "audit/gates/topology/orientation_demo.txt",
            },
        ],
    },
    {
        "family_name": "HDE-EPIC030 PR-03 proof companions",
        "classification": "expected updater convergence",
        "rationale": "Global path-proof convergence refreshes existing EPIC030 PR-03 proof companions and Machine Mirror rows as registered evidence-index rows are rewritten; no EPIC030 implementation scope is changed by PR-03.",
        "paths": [
            "audit/qa/hde-epic030/pr-03/category_order_binding.log.path_proof.txt",
            "audit/qa/hde-epic030/pr-03/compat_identity_binding.log.path_proof.txt",
            "audit/qa/hde-epic030/pr-03/compat_parity_binding.log.path_proof.txt",
        ],
        "mirror_rows": [
            {
                "artifact_key": "epic030.pr03.category_order_binding",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-03/category_order_binding.log",
            },
            {
                "artifact_key": "epic030.pr03.compat_identity_binding",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-03/compat_identity_binding.log",
            },
            {
                "artifact_key": "epic030.pr03.compat_parity_binding",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-03/compat_parity_binding.log",
            },
        ],
    },
    {
        "family_name": "HDE-EPIC030 PR-04 proof companions",
        "classification": "expected updater convergence",
        "rationale": "Global path-proof convergence refreshes existing EPIC030 PR-04 proof companions and Machine Mirror rows as registered evidence-index rows are rewritten; no EPIC030 implementation scope is changed by PR-03.",
        "paths": [
            "audit/qa/hde-epic030/pr-04/band_edges_binding.log.path_proof.txt",
            "audit/qa/hde-epic030/pr-04/band_thresholds_diff.json.path_proof.txt",
            "audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt.path_proof.txt",
        ],
        "mirror_rows": [
            {
                "artifact_key": "epic030.pr04.band_edges_binding",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-04/band_edges_binding.log",
            },
            {
                "artifact_key": "epic030.pr04.band_thresholds_diff",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-04/band_thresholds_diff.json",
            },
            {
                "artifact_key": "epic030.pr04.band_thresholds_identity_hash",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt",
            },
        ],
    },
    {
        "family_name": "HDE-EPIC030 PR-05 proof companions",
        "classification": "expected updater convergence",
        "rationale": "Global path-proof convergence refreshes existing EPIC030 PR-05 proof companions and Machine Mirror rows as registered evidence-index rows are rewritten; no EPIC030 implementation scope is changed by PR-03.",
        "paths": [
            "audit/qa/hde-epic030/pr-05/category_canonical_compare.log.path_proof.txt",
            "audit/qa/hde-epic030/pr-05/category_framework_binding.log.path_proof.txt",
            "audit/qa/hde-epic030/pr-05/per_channel_mechanics.json.path_proof.txt",
        ],
        "mirror_rows": [
            {
                "artifact_key": "epic030.pr05.category_canonical_compare",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-05/category_canonical_compare.log",
            },
            {
                "artifact_key": "epic030.pr05.category_framework_binding",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-05/category_framework_binding.log",
            },
            {
                "artifact_key": "epic030.pr05.per_channel_mechanics",
                "discovered_physical_path": "audit/qa/hde-epic030/pr-05/per_channel_mechanics.json",
            },
        ],
    },
]

VALIDATION_COMMANDS = [
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_epic031_pr03_evidence_coherence.py",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_epic031_pr03_evidence_coherence.py --check",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_mirror_schema.sh",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC ci/checks/check_evidence_index_hash.sh",
    "SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/check_lf_endings.py",
    "git diff --check",
]


def _sha256_path(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def _json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _write_governed(rel: str, content: bytes, *, check: bool) -> None:
    path = ROOT / rel
    if check:
        if not path.exists() or path.read_bytes() != content:
            raise SystemExit(f"STALE:{rel}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel,
        sha256=update_evidence_index._sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=None,
        produced_at=PRODUCED_AT,
        default_produced_at=PRODUCED_AT,
        check=check,
        stat_mtime=stat.st_mtime,
    )


def _load_human_paths() -> set[str]:
    if not (ROOT / HUMAN_INDEX_REL).exists():
        return set()
    payload = json.loads((ROOT / HUMAN_INDEX_REL).read_text(encoding="utf-8"))
    return {str(record.get("discovered_physical_path")) for record in payload}


def _load_mirror() -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    if not (ROOT / MIRROR_REL).exists():
        return records
    for raw in (ROOT / MIRROR_REL).read_text(encoding="utf-8").splitlines():
        if not raw:
            continue
        record = json.loads(raw)
        records[str(record["discovered_physical_path"])] = record
    return records


def _read_proof(rel: str) -> dict[str, str]:
    proof = ROOT / f"{rel}.path_proof.txt"
    data: dict[str, str] = {}
    if not proof.exists():
        return data
    for line in proof.read_text(encoding="utf-8").splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def _proof_ok(rel: str) -> bool:
    path = ROOT / rel
    proof = _read_proof(rel)
    if not path.exists() or not proof:
        return False
    if proof.get("path") != rel:
        return False
    if proof.get("sha256") != _sha256_path(rel):
        return False
    try:
        recorded_size = int(proof.get("size_bytes", ""))
    except ValueError:
        return False
    if recorded_size != path.stat().st_size:
        return False
    mtime_raw = proof.get("mtime_utc")
    produced_raw = proof.get("produced_at_utc")
    if not mtime_raw or not produced_raw:
        return False
    try:
        update_evidence_index._parse_utc_iso8601(mtime_raw)
        update_evidence_index._parse_utc_iso8601(produced_raw)
    except Exception:  # noqa: BLE001 - match evidence gate fail-closed parsing posture
        return False
    return True


def _mirror_row_ok(path: str, mirror: dict[str, dict[str, Any]], *, strict_hash: bool = True) -> bool:
    artifact = ROOT / path
    record = mirror.get(path)
    if record is None or not artifact.exists():
        return False
    if record.get("proof_anchor") != f"{path}.path_proof.txt":
        return False
    if not strict_hash:
        return True
    if record.get("sha256") != _sha256_path(path):
        return False
    if record.get("size_bytes") != artifact.stat().st_size:
        return False
    return True


def _hash_statuses() -> dict[str, str]:
    index_ok = False
    mirror_ok = False
    if (ROOT / HUMAN_INDEX_REL).exists() and (ROOT / HUMAN_INDEX_SHA_REL).exists():
        expected = f"{_sha256_path(HUMAN_INDEX_REL)}  {HUMAN_INDEX_REL}\n"
        index_ok = (ROOT / HUMAN_INDEX_SHA_REL).read_text(encoding="utf-8") == expected
    if (ROOT / MIRROR_REL).exists() and (ROOT / MIRROR_SHA_REL).exists():
        expected = f"{_sha256_path(MIRROR_REL)}  {MIRROR_REL}\n"
        mirror_ok = (ROOT / MIRROR_SHA_REL).read_text(encoding="utf-8") == expected
    return {
        "human_index_hash_sentinel": "PASS" if index_ok else "FAIL",
        "machine_mirror_checksum": "PASS" if mirror_ok else "FAIL",
    }


def _all_family_artifact_paths() -> list[str]:
    return sorted({path for family in FAMILY_MAP.values() for path in family["artifact_paths"]})


def _all_supporting_paths() -> list[str]:
    return sorted({path for family in FAMILY_MAP.values() for path in family["supporting_paths"]})


def _side_effect_proof_target(path: str) -> str:
    suffix = ".path_proof.txt"
    if path.endswith(suffix):
        return path[: -len(suffix)]
    return path


def _side_effect_path_status(path: str) -> dict[str, Any]:
    target = _side_effect_proof_target(path)
    proof_required = path.endswith(".path_proof.txt") or (ROOT / f"{target}.path_proof.txt").exists()
    proof_valid = _proof_ok(target) if proof_required else None
    return {
        "path": path,
        "exists": (ROOT / path).exists(),
        "proof_target": target,
        "proof_required": proof_required,
        "proof_valid": proof_valid,
    }


def _side_effect_mirror_status(
    expected_row: dict[str, str], mirror: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    path = expected_row["discovered_physical_path"]
    artifact_key = expected_row["artifact_key"]
    record = mirror.get(path)
    artifact = ROOT / path
    row_present = record is not None
    artifact_key_matches = row_present and record.get("artifact_key") == artifact_key
    row_valid = row_present and artifact_key_matches and _mirror_row_ok(path, mirror, strict_hash=True)
    return {
        "artifact_key": artifact_key,
        "discovered_physical_path": path,
        "artifact_exists": artifact.exists(),
        "row_present": row_present,
        "artifact_key_matches": artifact_key_matches,
        "proof_anchor": record.get("proof_anchor") if record else None,
        "sha256_size_match": row_valid,
        "mirror_row_valid": row_valid,
    }


def _side_effect_payload(mirror: dict[str, dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    mirror_records = mirror if mirror is not None else _load_mirror()
    return [
        {
            "classification": group["classification"],
            "family_name": group["family_name"],
            "paths": [_side_effect_path_status(path) for path in group["paths"]],
            "machine_mirror_rows": [
                _side_effect_mirror_status(row, mirror_records)
                for row in group["mirror_rows"]
            ],
            "rationale": group["rationale"],
        }
        for group in BOUNDED_SIDE_EFFECT_REFRESHES
    ]


def _side_effects_ok(side_effects: list[dict[str, Any]]) -> bool:
    for group in side_effects:
        for path_status in group["paths"]:
            if not path_status["exists"]:
                return False
            if path_status["proof_required"] and path_status["proof_valid"] is not True:
                return False
        for mirror_status in group["machine_mirror_rows"]:
            if not mirror_status["mirror_row_valid"]:
                return False
    return True


def _family_payload() -> dict[str, Any]:
    return {
        "artifact": "evidence_family_map",
        "epic_id": EPIC_ID,
        "pf09_subtask": PF09_SUBTASK,
        "produced_at_utc": PRODUCED_AT,
        "schema_version": "1.3",
        "bounded_side_effect_refreshes": _side_effect_payload(),
        "proof_families": [
            {
                "family_name": name,
                "artifact_paths": paths["artifact_paths"],
                "supporting_paths": paths["supporting_paths"],
                "proof_label_is_acceptance_token": False,
            }
            for name, paths in FAMILY_MAP.items()
        ],
        "scope_guardrails": {
            "acceptance_tokens_created": False,
            "follow_up_scope_implemented": False,
            "live_vendor_call_executed": False,
            "public_reader_contract_changed": False,
        },
    }


def _coherence_payload(*, check: bool = False) -> dict[str, Any]:
    human_paths = _load_human_paths()
    mirror = _load_mirror()
    indexed = {path: path in human_paths for path in INDEXED_SAFE_RAILS_ARTIFACTS}
    mirror_rows = {
        path: _mirror_row_ok(path, mirror, strict_hash=check or path not in PR03_ARTIFACTS)
        for path in INDEXED_SAFE_RAILS_ARTIFACTS
    }
    side_effects = _side_effect_payload(mirror)
    proofs = {path: _proof_ok(path) for path in GOVERNED_PR03_PROOF_ARTIFACTS}
    hashes = _hash_statuses()
    supporting_paths = _all_supporting_paths()
    family_artifact_paths = _all_family_artifact_paths()
    sections = {
        "indexed_artifact_presence": all((ROOT / path).exists() for path in family_artifact_paths),
        "supporting_path_presence": all((ROOT / path).exists() for path in supporting_paths),
        "path_proof_status": all(proofs.values()),
        "pr03_output_path_proofs": all(proofs[path] for path in PR03_ARTIFACTS),
        "human_index_binding": all(indexed.values()),
        "machine_mirror_binding": all(mirror_rows.values()),
        "hash_status": all(value == "PASS" for value in hashes.values()),
        "bounded_side_effects_validated": _side_effects_ok(side_effects),
    }
    status = "PASS" if all(sections.values()) else "FAIL"
    return {
        "artifact": "safe_rails_evidence_coherence",
        "epic_id": EPIC_ID,
        "pf09_subtask": PF09_SUBTASK,
        "produced_at_utc": PRODUCED_AT,
        "schema_version": "1.3",
        "bounded_side_effect_refreshes": side_effects,
        "local_deterministic_posture": {
            "ALLOW_NETWORK": "0",
            "LANG": "C",
            "LC_ALL": "C",
            "SAFE_MODE": "1",
            "TZ": "UTC",
            "live_vendor_call_executed": False,
            "secret_values_required": False,
            "secret_values_recorded": False,
        },
        "family_artifact_paths": [
            {"path": path, "exists": (ROOT / path).exists()} for path in family_artifact_paths
        ],
        "supporting_paths": [
            {"path": path, "exists": (ROOT / path).exists(), "path_proof_required": False}
            for path in supporting_paths
        ],
        "safe_rails_artifacts": [
            {
                "path": path,
                "exists": (ROOT / path).exists(),
                "path_proof": "PASS" if proofs[path] else "FAIL",
                "human_index_binding": "PASS" if indexed[path] else "FAIL",
                "machine_mirror_binding": "PASS" if mirror_rows[path] else "FAIL",
            }
            for path in SAFE_RAILS_ARTIFACTS
        ],
        "pr03_outputs": [
            {
                "path": path,
                "exists": (ROOT / path).exists(),
                "path_proof": "PASS" if proofs[path] else "FAIL",
                "human_index_binding": "PASS" if indexed[path] else "FAIL",
                "machine_mirror_binding": "PASS" if mirror_rows[path] else "FAIL",
            }
            for path in PR03_ARTIFACTS
        ],
        "index_mirror_refresh_artifacts": [
            {
                "path": path,
                "exists": (ROOT / path).exists(),
                "path_proof": "PASS" if proofs[path] else "FAIL",
            }
            for path in INDEX_MIRROR_REFRESH_ARTIFACTS
        ],
        "coherence_checks": {key: "PASS" if value else "FAIL" for key, value in sections.items()},
        "hash_checks": hashes,
        "machine_mirror_self_record_note": {
            "paths": PR03_ARTIFACTS,
            "posture": "non-check generation checks proof anchors for self-generated artifacts before update_evidence_index.py binds final sha256 and size_bytes; --check validates final sha256 and size_bytes for every PR-03 Machine Mirror row.",
        },
        "out_of_scope_confirmations": {
            "hdapi_v2_runtime_conformance_implemented": False,
            "live_vendor_call_executed": False,
            "po_only_open_rails_v2_smoke_executed": False,
            "public_reader_output_changed": False,
            "token_evidence_matrix_rows_created": False,
        },
        "status": status,
    }


def _refresh_log_payload(coherence_status: str) -> bytes:
    generator_steps = [
        f"write {FAMILY_MAP_REL}",
        f"write {COHERENCE_REL}",
        f"write {REFRESH_LOG_REL}",
        "write co-located PR-03 path proofs",
    ]
    lines = [
        "HDE-EPIC031 PR-03 SAFE rails governed evidence refresh",
        f"produced_at_utc: {PRODUCED_AT}",
        f"epic_id: {EPIC_ID}",
        f"pf09_subtask: {PF09_SUBTASK}",
        "rails: SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC",
        "live_vendor_call_executed: false",
        "secret_values_recorded: false",
        "generator_step_outcomes:",
    ]
    lines.extend(f"  - step: {step}\n    outcome: PASS" for step in generator_steps)
    lines.append("bounded_side_effect_refreshes:")
    for group in BOUNDED_SIDE_EFFECT_REFRESHES:
        lines.extend(
            [
                f"  - family: {group['family_name']}",
                f"    classification: {group['classification']}",
                f"    rationale: {group['rationale']}",
                "    paths:",
            ]
        )
        lines.extend(f"      - {path}" for path in group["paths"])
        lines.append("    machine_mirror_rows:")
        lines.extend(
            f"      - artifact_key: {row['artifact_key']} discovered_physical_path: {row['discovered_physical_path']}"
            for row in group["mirror_rows"]
        )
    lines.extend(
        [
            "validation_command_roster:",
            "  execution_record: external validation commands are listed for reproducibility; this generator does not mark unexecuted commands PASS or FAIL.",
        ]
    )
    lines.extend(f"  - command: {command}" for command in VALIDATION_COMMANDS)
    lines.append(f"coherence_status: {coherence_status}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _materialize_pr03_files(*, check: bool) -> None:
    family_payload = _family_payload()
    _write_governed(FAMILY_MAP_REL, _json_bytes(family_payload), check=check)
    if not check:
        # Fresh checkout/cleaned evidence bootstrap: materialize self-generated artifacts and
        # their path proofs before computing coherence over the complete PR-03 family.
        if not (ROOT / COHERENCE_REL).exists():
            _write_governed(COHERENCE_REL, _json_bytes({"artifact": "safe_rails_evidence_coherence", "status": "BOOTSTRAP"}), check=False)
        if not (ROOT / REFRESH_LOG_REL).exists():
            _write_governed(REFRESH_LOG_REL, _refresh_log_payload("BOOTSTRAP"), check=False)


def _write_coherence_pair(coherence_payload: dict[str, Any], *, check: bool) -> None:
    _write_governed(COHERENCE_REL, _json_bytes(coherence_payload), check=check)
    _write_governed(REFRESH_LOG_REL, _refresh_log_payload(str(coherence_payload["status"])), check=check)


def generate(*, check: bool) -> None:
    ensure_determinism_env()
    _materialize_pr03_files(check=check)
    if check:
        coherence_payload = _coherence_payload(check=True)
        _write_coherence_pair(coherence_payload, check=True)
        if coherence_payload["status"] != "PASS":
            raise SystemExit("EPIC031_PR03_COHERENCE_FAIL")
        return

    final_payload: dict[str, Any] | None = None
    for _ in range(4):
        coherence_payload = _coherence_payload()
        _write_coherence_pair(coherence_payload, check=False)
        recomputed_payload = _coherence_payload()
        if _json_bytes(recomputed_payload) == (ROOT / COHERENCE_REL).read_bytes():
            final_payload = recomputed_payload
            break
        final_payload = recomputed_payload
    if final_payload is None or final_payload["status"] != "PASS":
        raise SystemExit("EPIC031_PR03_COHERENCE_FAIL")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args(argv)
    generate(check=args.check)
    print("EPIC031_PR03_EVIDENCE_COHERENCE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
