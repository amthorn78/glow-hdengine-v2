#!/usr/bin/env python3
"""Generate the EPIC017 manifest from the machine evidence mirror."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MIRROR_PATH = ROOT / "artifacts/evidence_index.jsonl"
MANIFEST_PATH = ROOT / "audit/EPIC017_MANIFEST.json"

TOKEN_ARTIFACT_MAP: dict[str, list[str]] = {
    # Core acceptance rail tokens
    "TESTS_PASS_OK": ["qa.compat.coverage_summary"],
    "DOC_DELTA_PRESENT_OK": ["audit.pf09_functional_report_rails_closed"],
    # D1 — canonical serialization package
    "CLI_NO_ALT_JSON_OK": ["cli.showcompat.summary"],
    "CLI_READER_PARITY_OK": ["cli.showcompat.reader_cli_parity"],
    "CLI_SHOWCOMPAT_CANON_OK": ["cli.showcompat.summary"],
    "CLI_STDOUT_LF_OK": ["cli.showcompat.summary"],
    "JSON_CANONICAL_CHECK_OK": [
        "cli.showcompat.ab",
        "registry.registry_report",
        "engine.order.props_total_order.log",
    ],
    "TWO_RUN_IDENTITY_OK": ["cli.showcompat.preimage_recompute"],
    "COMPOSITE_ABBA_IDENTITY_OK": ["engine.order.abba_identity.bytes"],
    # D2 — evidence skeleton
    "EVIDENCE_INDEX_UPDATED_OK": ["index.machine_mirror"],
    "MACHINE_MIRROR_UPDATED_OK": ["index.machine_mirror"],
    "EVIDENCE_INDEX_HASH_OK": ["index.machine_mirror"],
    "EVIDENCE_INDEX_MIRROR_OK": ["index.machine_mirror"],
    "EVIDENCE_PATHS_VALIDATED_OK": ["topology.orientation_demo"],
    "EVIDENCE_PATH_PROOFS_OK": ["topology.orientation_demo"],
    "CI_CHECK_MIRROR_SCHEMA_OK": ["index.machine_mirror"],
    "CI_CHECK_FINAL_LF_OK": ["cli.showcompat.ab"],
    # D3 — configuration & registry
    "CONFIG_GEN_OK": ["registry.registry_report"],
    "UNKNOWN_IDS_FAIL_CLOSED_OK": ["registry.registry_report"],
    # D4 — deterministic ordering
    "TIEBREAK_TOTAL_ORDER_OK": ["engine.order.props_total_order.log"],
}


def _load_mirror() -> dict[str, dict[str, object]]:
    if not MIRROR_PATH.exists():
        raise SystemExit(f"MISSING_MIRROR:{MIRROR_PATH}")
    entries: dict[str, dict[str, object]] = {}
    for raw in MIRROR_PATH.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        entry = json.loads(raw)
        key = entry["artifact_key"]
        if key in entries:
            raise SystemExit(f"DUPLICATE_KEY:{key}")
        entries[key] = entry
    return entries


def _sha256_path(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest()


def build_manifest() -> dict[str, object]:
    mirror = _load_mirror()
    tokens: dict[str, list[dict[str, object]]] = {}

    for token, artifact_keys in sorted(TOKEN_ARTIFACT_MAP.items()):
        token_entries: list[dict[str, object]] = []
        for artifact_key in artifact_keys:
            if artifact_key not in mirror:
                raise SystemExit(f"ARTIFACT_MISSING:{artifact_key}")
            entry = mirror[artifact_key]
            rel_path = entry["discovered_physical_path"]
            path = ROOT / rel_path
            if not path.exists():
                raise SystemExit(f"PATH_MISSING:{rel_path}")
            proof_anchor = entry.get("proof_anchor")
            if not proof_anchor:
                raise SystemExit(f"MISSING_PROOF:{artifact_key}")

            mirror_sha = entry.get("sha256")
            mirror_size = entry.get("size_bytes")
            file_sha = _sha256_path(path)
            file_size = path.stat().st_size

            if mirror_size is None or mirror_sha is None:
                raise SystemExit(f"MIRROR_FIELDS:{artifact_key}")
            if mirror_size != file_size:
                raise SystemExit(f"SIZE_MISMATCH:{artifact_key}")
            if artifact_key != "index.machine_mirror" and mirror_sha != file_sha:
                raise SystemExit(f"SHA_MISMATCH:{artifact_key}")
            token_entries.append(
                {
                    "artifact_key": artifact_key,
                    "discovered_physical_path": rel_path,
                    "sha256": mirror_sha,
                    "size_bytes": mirror_size,
                    "proof_anchor": proof_anchor,
                }
            )
        tokens[token] = token_entries

    return {"epic_id": "HDE-EPIC017", "tokens": tokens}


def main() -> None:
    manifest = build_manifest()
    payload = json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n"
    MANIFEST_PATH.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
