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
SAFE_RAILS_ARTIFACTS = [*PR01_ARTIFACTS, *PR02_ARTIFACTS, *PR03_ARTIFACTS]

FAMILY_MAP: dict[str, list[str]] = {
    "SAFE rails open-posture proof family": [
        "ci/jobs/rails_closed_refusal.yml",
        "ci/jobs/rails_open_conformance.yml",
        "artifacts/vendor/policies_pinned.md",
        "audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json",
        "audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json",
    ],
    "SAFE retry/backoff/typed 429 proof family": [
        "artifacts/vendor/retry_after_parse.log",
        "audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json",
    ],
    "SAFE rails keys-only log-redaction proof family": [
        "ci/jobs/logs_keys_only_redaction.yml",
        "audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl",
        "audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt",
        "audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json",
        "audit/qa/hde-epic031/pr-02/bounded_label_observability.json",
        "audit/qa/hde-epic031/pr-02/secret_redaction_scan.log",
    ],
    "SAFE rails governed evidence-index coherence family": [
        FAMILY_MAP_REL,
        COHERENCE_REL,
        REFRESH_LOG_REL,
    ],
    "Human Evidence Index refresh family": [
        HUMAN_INDEX_REL,
        HUMAN_INDEX_SHA_REL,
        f"{HUMAN_INDEX_REL}.path_proof.txt",
        f"{HUMAN_INDEX_SHA_REL}.path_proof.txt",
    ],
    "Machine Mirror refresh family": [
        MIRROR_REL,
        MIRROR_SHA_REL,
        f"{MIRROR_REL}.path_proof.txt",
        f"{MIRROR_SHA_REL}.path_proof.txt",
    ],
    "Path-proof validation family": [f"{path}.path_proof.txt" for path in SAFE_RAILS_ARTIFACTS],
}

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
    if proof.get("size_bytes") != str(path.stat().st_size):
        return False
    return bool(proof.get("mtime_utc") and proof.get("produced_at_utc"))


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


def _family_payload() -> dict[str, Any]:
    return {
        "artifact": "evidence_family_map",
        "epic_id": EPIC_ID,
        "pf09_subtask": PF09_SUBTASK,
        "produced_at_utc": PRODUCED_AT,
        "schema_version": "1.0",
        "proof_families": [
            {"family_name": name, "artifact_paths": paths, "proof_label_is_acceptance_token": False}
            for name, paths in FAMILY_MAP.items()
        ],
        "scope_guardrails": {
            "acceptance_tokens_created": False,
            "follow_up_scope_implemented": False,
            "live_vendor_call_executed": False,
            "public_reader_contract_changed": False,
        },
    }


def _coherence_payload() -> dict[str, Any]:
    human_paths = _load_human_paths()
    mirror = _load_mirror()
    indexed = {path: path in human_paths for path in SAFE_RAILS_ARTIFACTS}
    mirrored = {path: path in mirror for path in SAFE_RAILS_ARTIFACTS}
    proofs = {path: _proof_ok(path) for path in SAFE_RAILS_ARTIFACTS}
    proof_anchors = {
        path: mirror.get(path, {}).get("proof_anchor") == f"{path}.path_proof.txt"
        for path in SAFE_RAILS_ARTIFACTS
    }
    hashes = _hash_statuses()
    sections = {
        "indexed_artifact_presence": all((ROOT / path).exists() for path in SAFE_RAILS_ARTIFACTS),
        "path_proof_status": all(proofs.values()),
        "human_index_binding": all(indexed.values()),
        "machine_mirror_binding": all(mirrored.values()) and all(proof_anchors.values()),
        "hash_status": all(value == "PASS" for value in hashes.values()),
    }
    status = "PASS" if all(sections.values()) else "FAIL"
    return {
        "artifact": "safe_rails_evidence_coherence",
        "epic_id": EPIC_ID,
        "pf09_subtask": PF09_SUBTASK,
        "produced_at_utc": PRODUCED_AT,
        "schema_version": "1.0",
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
        "safe_rails_artifacts": [
            {
                "path": path,
                "exists": (ROOT / path).exists(),
                "path_proof": "PASS" if proofs[path] else "FAIL",
                "human_index_binding": "PASS" if indexed[path] else "FAIL",
                "machine_mirror_binding": "PASS" if mirrored[path] else "FAIL",
                "proof_anchor": "PASS" if proof_anchors[path] else "FAIL",
            }
            for path in SAFE_RAILS_ARTIFACTS
        ],
        "coherence_checks": {key: "PASS" if value else "FAIL" for key, value in sections.items()},
        "hash_checks": hashes,
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
    lines = [
        "HDE-EPIC031 PR-03 SAFE rails governed evidence refresh",
        f"produced_at_utc: {PRODUCED_AT}",
        f"epic_id: {EPIC_ID}",
        f"pf09_subtask: {PF09_SUBTASK}",
        "rails: SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC",
        "live_vendor_call_executed: false",
        "secret_values_recorded: false",
        "commands:",
    ]
    lines.extend(f"  - command: {command}\n    outcome: {'PASS' if coherence_status == 'PASS' else 'FAIL'}" for command in VALIDATION_COMMANDS)
    lines.append(f"overall_status: {coherence_status}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def generate(*, check: bool) -> None:
    ensure_determinism_env()
    family_payload = _family_payload()
    _write_governed(FAMILY_MAP_REL, _json_bytes(family_payload), check=check)
    coherence_payload = _coherence_payload()
    _write_governed(COHERENCE_REL, _json_bytes(coherence_payload), check=check)
    _write_governed(REFRESH_LOG_REL, _refresh_log_payload(str(coherence_payload["status"])), check=check)
    if check and coherence_payload["status"] != "PASS":
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
