#!/usr/bin/env python3
"""Generate EPIC030 PR-05 category-framework carry-forward evidence artifacts."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import compat_public
from engine.order import normalize_channel_id
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon

OUT_DIR = ROOT / "audit" / "qa" / "hde-epic030" / "pr-05"
CHANNELS_PATH = ROOT / "catalog" / "channels_v1.json"
COMPAT_AB_PATH = ROOT / "artifacts" / "compat" / "AB.json"
READER_A7_PATH = ROOT / "artifacts" / "audit" / "a7" / "reader_200_body.json"
INDEX_PATH = ROOT / "docs" / "evidence" / "INDEX.json"
MIRROR_PATH = ROOT / "artifacts" / "evidence_index.jsonl"

PR05_ARTIFACT_KEYS = (
    "epic030.pr05.category_framework_binding",
    "epic030.pr05.per_channel_mechanics",
    "epic030.pr05.category_canonical_compare",
)


def _iso_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _write_text(path: Path, text: str) -> None:
    if not text.endswith("\n"):
        text = f"{text}\n"
    _write_bytes(path, text.encode("utf-8"))


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _build_per_channel_mechanics(produced_at: str) -> dict[str, Any]:
    raw = _load_json(CHANNELS_PATH)
    channels_raw = raw.get("channels")
    if not isinstance(channels_raw, list):
        raise SystemExit("INVALID_CHANNELS_CATALOG")

    channels: list[dict[str, Any]] = []
    for item in channels_raw:
        if not isinstance(item, dict):
            continue
        channel_id = str(item.get("id", ""))
        normalized = normalize_channel_id(channel_id)
        gates_raw = item.get("gates")
        if not isinstance(gates_raw, list) or len(gates_raw) != 2:
            raise SystemExit(f"INVALID_CHANNEL_GATES:{channel_id}")
        gate_a, gate_b = int(gates_raw[0]), int(gates_raw[1])
        low_gate = min(gate_a, gate_b)
        high_gate = max(gate_a, gate_b)

        channels.append(
            {
                "channel_id": normalized,
                "canonical_edge": f"{low_gate:02d}-{high_gate:02d}",
                "input_id": channel_id,
                "gates": [low_gate, high_gate],
                "compromise_direction": f"{low_gate:02d}->{high_gate:02d}",
                "compromise_gate": high_gate,
                "circuit_primary": str(item.get("circuit_primary", "")),
                "bridge_analytics": {"supported": False, "status": "not_exposed_in_current_repo_surface"},
                "timing_analytics": {"supported": False, "status": "not_exposed_in_current_repo_surface"},
            }
        )

    channels.sort(key=lambda row: row["channel_id"])
    all_ids_are_canonical = all(row["channel_id"] == row["canonical_edge"] for row in channels)

    return {
        "schema": "hde_epic030.pr05.per_channel_mechanics.v1",
        "epic_id": "HDE-EPIC030",
        "task_id": "HDE-DISS006",
        "subtask_id": "HDE-DISS006.3",
        "produced_at_utc": produced_at,
        "category_order_source": "engine.compat.categories.CATEGORIES_ORDER_V1",
        "categories_order": list(CATEGORIES_ORDER_V1),
        "channel_catalog_source": "catalog/channels_v1.json",
        "channels": channels,
        "channel_count": len(channels),
        "all_channel_ids_canonical_nn_nn": all_ids_are_canonical,
        "notes": {
            "compromise_fields": "derived from canonical gate ordering only; no secondary runtime compromise surface exists",
            "circuit_scope": "channel-scoped via catalog channels_v1.circuit_primary",
        },
        "status": "PASS" if all_ids_are_canonical else "FAIL",
    }


def _canonical_compare_line(path: Path) -> tuple[str, bool, str]:
    raw = path.read_bytes()
    try:
        parsed = json.loads(raw.decode("utf-8"))
    except Exception as exc:  # pragma: no cover
        return path.relative_to(ROOT).as_posix(), False, f"json_decode_error={exc}"
    reparsed = sercanon(parsed, sort_keys=True)
    same = raw == reparsed
    detail = f"sha256={hashlib.sha256(raw).hexdigest()} bytes={len(raw)}"
    return path.relative_to(ROOT).as_posix(), same, detail


def _reader_public_posture_ok() -> bool:
    payload = _load_json(READER_A7_PATH)
    categories = payload.get("categories")
    if not isinstance(categories, list) or not categories:
        return False
    for cat in categories:
        if not isinstance(cat, dict):
            return False
        if set(cat.keys()) != {"band", "id"}:
            return False
    forbidden = {"score", "personal_key", "shared_key", "keys"}
    return all(key not in payload for key in forbidden)


def _index_has_pr05_bindings() -> bool:
    idx = _load_json(INDEX_PATH)
    if not isinstance(idx, list):
        return False
    found = {str(entry.get("artifact_key", "")) for entry in idx if isinstance(entry, dict)}
    return all(key in found for key in PR05_ARTIFACT_KEYS)


def _mirror_has_pr05_bindings() -> bool:
    found: set[str] = set()
    for line in MIRROR_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            return False
        key = obj.get("artifact_key")
        if isinstance(key, str):
            found.add(key)
    return all(key in found for key in PR05_ARTIFACT_KEYS)


def generate() -> None:
    ensure_determinism_env()

    produced_at = _iso_now()
    per_channel = _build_per_channel_mechanics(produced_at)
    per_channel_path = OUT_DIR / "per_channel_mechanics.json"
    _write_bytes(per_channel_path, sercanon(per_channel, sort_keys=True))

    compat_admin = compat_public(
        {"person_uid": "alpha"},
        {"person_uid": "beta"},
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights={category: 10 for category in CATEGORIES_ORDER_V1},
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
    )
    compat_categories = compat_admin.get("categories") if isinstance(compat_admin, dict) else None
    category_order_ok = isinstance(compat_categories, list) and [
        str(item.get("id", "")) for item in compat_categories if isinstance(item, dict)
    ] == list(CATEGORIES_ORDER_V1)

    compare_targets = [per_channel_path, COMPAT_AB_PATH]
    compare_lines = [
        "schema: hde_epic030.pr05.category_canonical_compare.v1",
        f"produced_at_utc: {produced_at}",
        "epic_id: HDE-EPIC030",
        "task_id: HDE-DISS006",
        "subtask_id: HDE-DISS006.4",
    ]
    compare_ok = True
    for target in compare_targets:
        rel, same, detail = _canonical_compare_line(target)
        compare_ok = compare_ok and same
        compare_lines.append(f"target: {rel} canonical_roundtrip_equal={same} {detail}")
    compare_lines.append("status: PASS" if compare_ok else "status: FAIL")
    _write_text(OUT_DIR / "category_canonical_compare.log", "\n".join(compare_lines))

    reader_public_ok = _reader_public_posture_ok()
    index_ok = _index_has_pr05_bindings()
    mirror_ok = _mirror_has_pr05_bindings()

    binding_status = all(
        (
            per_channel.get("status") == "PASS",
            compare_ok,
            category_order_ok,
            reader_public_ok,
            index_ok,
            mirror_ok,
        )
    )
    binding_lines = [
        "schema: hde_epic030.pr05.category_framework_binding.v1",
        f"produced_at_utc: {produced_at}",
        "epic_id: HDE-EPIC030",
        "task_id: HDE-DISS006",
        "subtask_ids: HDE-DISS006.3,HDE-DISS006.4,HDE-DISS006.5",
        "binding_family: category_framework_internal_admin",
        f"magic10_order_preserved_admin_compat: {category_order_ok}",
        f"public_reader_bands_only_numeric_free: {reader_public_ok}",
        f"index_binding_present: {index_ok}",
        f"mirror_binding_present: {mirror_ok}",
        f"per_channel_mechanics_status: {per_channel.get('status')}",
        "canonical_compare_artifact: audit/qa/hde-epic030/pr-05/category_canonical_compare.log",
        f"canonical_compare_status: {'PASS' if compare_ok else 'FAIL'}",
        "status: PASS" if binding_status else "status: FAIL",
    ]
    _write_text(OUT_DIR / "category_framework_binding.log", "\n".join(binding_lines))


if __name__ == "__main__":
    generate()
