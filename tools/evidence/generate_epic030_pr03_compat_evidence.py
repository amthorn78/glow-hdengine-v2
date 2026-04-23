#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon

OUT_DIR = ROOT / "audit" / "qa" / "hde-epic030" / "pr-03"
KEY_TABLE_PATH = ROOT / "artifacts" / "narratives" / "key_table_10x2.snapshot.json"
LEGACY_KEY_TABLE_PATH = ROOT / "artifacts" / "epic003" / "narrative_keys_table.json"
AB_PATH = ROOT / "artifacts" / "compat" / "AB.json"
BA_PATH = ROOT / "artifacts" / "compat" / "BA.json"
IDENTITY_HASH_PATH = ROOT / "artifacts" / "compat" / "identity_hash.txt"


def _iso_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_key_table_snapshot() -> str:
    if not LEGACY_KEY_TABLE_PATH.exists():
        raise SystemExit(f"MISSING:{LEGACY_KEY_TABLE_PATH.relative_to(ROOT).as_posix()}")
    payload = _load_json(LEGACY_KEY_TABLE_PATH)
    if not isinstance(payload, list):
        raise SystemExit("INVALID_LEGACY_KEY_TABLE")

    by_id: dict[str, dict[str, str]] = {}
    for row in payload:
        if not isinstance(row, dict):
            continue
        key_id = str(row.get("id", ""))
        if not key_id:
            continue
        by_id[key_id] = {
            "id": key_id,
            "band": str(row.get("band", "")),
            "personal_key": str(row.get("personal_key", "")),
            "shared_key": str(row.get("shared_key", "")),
        }

    ordered_rows = []
    for category in CATEGORIES_ORDER_V1:
        if category not in by_id:
            raise SystemExit(f"MISSING_CATEGORY_IN_LEGACY_KEY_TABLE:{category}")
        ordered_rows.append(by_id[category])

    snapshot = {
        "schema": "hde_diss002_6.key_table_10x2.snapshot.v1",
        "subtask_id": "HDE-DISS002.6",
        "epic_id": "HDE-EPIC030",
        "categories_order": list(CATEGORIES_ORDER_V1),
        "rows": ordered_rows,
        "source_table": LEGACY_KEY_TABLE_PATH.relative_to(ROOT).as_posix(),
    }
    KEY_TABLE_PATH.parent.mkdir(parents=True, exist_ok=True)
    KEY_TABLE_PATH.write_bytes(sercanon(snapshot, sort_keys=True))
    return hashlib.sha256(KEY_TABLE_PATH.read_bytes()).hexdigest()


def generate() -> None:
    ensure_determinism_env()

    ab_bytes = AB_PATH.read_bytes()
    ba_bytes = BA_PATH.read_bytes()
    parity_equal = ab_bytes == ba_bytes
    ab_json = json.loads(ab_bytes.decode("utf-8"))
    ba_json = json.loads(ba_bytes.decode("utf-8"))
    parity_structural_equal = ab_json == ba_json

    identity_hash = IDENTITY_HASH_PATH.read_text(encoding="utf-8").strip()
    identity_format_valid = bool(re.fullmatch(r"[0-9a-f]{64}", identity_hash))
    recomputed_ab_sha256 = hashlib.sha256(ab_bytes).hexdigest()
    recomputed_ba_sha256 = hashlib.sha256(ba_bytes).hexdigest()
    identity_matches_ab = identity_hash == recomputed_ab_sha256
    identity_matches_ba = identity_hash == recomputed_ba_sha256
    identity_valid = identity_format_valid and identity_matches_ab and identity_matches_ba

    key_table_sha = _write_key_table_snapshot()
    produced_at = _iso_now()

    parity_lines = [
        "schema: hde_epic030.pr03.compat_parity_binding.v1",
        f"produced_at_utc: {produced_at}",
        "epic_id: HDE-EPIC030",
        "task_id: HDE-DISS002",
        "subtask_id: HDE-DISS002.6",
        "binding_family: compat_parity_ab_ba",
        "source_artifact_ab: artifacts/compat/AB.json",
        "source_artifact_ba: artifacts/compat/BA.json",
        f"ab_sha256: {recomputed_ab_sha256}",
        f"ba_sha256: {recomputed_ba_sha256}",
        f"ab_equals_ba: {parity_equal}",
        f"ab_equals_ba_structural: {parity_structural_equal}",
        "status: PASS" if parity_equal else "status: FAIL",
        "",
    ]
    _write_text(OUT_DIR / "compat_parity_binding.log", "\n".join(parity_lines))

    identity_lines = [
        "schema: hde_epic030.pr03.compat_identity_binding.v1",
        f"produced_at_utc: {produced_at}",
        "epic_id: HDE-EPIC030",
        "task_id: HDE-DISS002",
        "subtask_id: HDE-DISS002.6",
        "binding_family: compat_identity_hash",
        "source_artifact: artifacts/compat/identity_hash.txt",
        f"identity_hash: {identity_hash}",
        f"identity_hash_valid_sha256_hex: {identity_format_valid}",
        f"recomputed_ab_sha256: {recomputed_ab_sha256}",
        f"recomputed_ba_sha256: {recomputed_ba_sha256}",
        f"identity_matches_ab: {identity_matches_ab}",
        f"identity_matches_ba: {identity_matches_ba}",
        "status: PASS" if identity_valid else "status: FAIL",
        "",
    ]
    _write_text(OUT_DIR / "compat_identity_binding.log", "\n".join(identity_lines))

    category_lines = [
        "schema: hde_epic030.pr03.category_order_binding.v1",
        f"produced_at_utc: {produced_at}",
        "epic_id: HDE-EPIC030",
        "task_id: HDE-DISS002",
        "subtask_id: HDE-DISS002.6",
        "binding_family: category_order_magic10_plus_narrative_key_table",
        "frozen_order_source: engine.compat.categories.CATEGORIES_ORDER_V1",
        f"categories_order: {','.join(CATEGORIES_ORDER_V1)}",
        "narrative_key_table_artifact: artifacts/narratives/key_table_10x2.snapshot.json",
        f"narrative_key_table_sha256: {key_table_sha}",
        "status: PASS",
        "",
    ]
    _write_text(OUT_DIR / "category_order_binding.log", "\n".join(category_lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate EPIC030 PR-03 compatibility evidence bindings")
    _ = parser.parse_args()
    generate()
