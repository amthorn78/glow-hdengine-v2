#!/usr/bin/env python3
"""EPIC030 PR-05 category-framework carry-forward evidence: frozen history since HDE-EPIC043 WU-PR-09 (never regenerated)."""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.resolver import resolve_compat_chart
from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.compat.compute import evaluate_pair, evaluation_party
from engine.order import normalize_channel_id
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon
from tools.evidence.run_sanity_pipeline import ReleaseNotAdmitted, probe_release_admission

OUT_DIR = ROOT / "audit" / "qa" / "hde-epic030" / "pr-05"
CHANNELS_PATH = ROOT / "catalog" / "channels_v1.json"
COMPAT_AB_PATH = ROOT / "artifacts" / "compat" / "AB.json"
READER_A7_PATH = ROOT / "artifacts" / "audit" / "a7" / "reader_200_body.json"
INDEX_PATH = ROOT / "docs" / "evidence" / "INDEX.json"
MIRROR_PATH = ROOT / "artifacts" / "evidence_index.jsonl"
# Complete mapped fixture charts for the internal-admin compat evaluation.
ADMIN_FIXTURE_PATHS = (ROOT / "fixtures" / "charts" / "alice.json", ROOT / "fixtures" / "charts" / "bob.json")
REQUIRES_ADMITTED_RELEASE = "HDE_EPIC030_PR05_REQUIRES_ADMITTED_RELEASE"
# HDE-EPIC043 WU-PR-09: frozen history.  The PR-05 records are capture-time v1
# evaluations; write mode refuses and ``--check`` verifies these pins.
FROZEN_HISTORY_NOT_REGENERATED = "FROZEN_HISTORY_NOT_REGENERATED"
FROZEN_RECORD_MISMATCH = "FROZEN_RECORD_MISMATCH"
FROZEN_RECORDS = {
    "category_canonical_compare.log": ("a59d727047aecfe9c443fa654d64d288b42318cf3f50e9284d70734cc062f0ec", 496),
    "category_framework_binding.log": ("4d6530b77e4aac9fb89476f7e818b1111c97c9715c3f4071879b62e05dee3e42", 549),
    "per_channel_mechanics.json": ("1d7eb1b31469468b9482a588f0bc5632c93f0d51ee2df455679fdfa8bdb762c7", 12873),
}

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
        "category_order_source": "engine.categories.registry.FROZEN_MAGIC10_ORDER",
        "categories_order": list(FROZEN_MAGIC10_ORDER),
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


def _admin_compat_result() -> dict[str, Any]:
    """Evaluate the two complete fixture charts through the admitted mechanics bundle."""

    parties = [
        evaluation_party(resolve_compat_chart(_load_json(path), source_policy="local", env=None))
        for path in ADMIN_FIXTURE_PATHS
    ]
    return evaluate_pair(parties[0], parties[1])


def frozen_record_mismatches(out_dir: Path | None = None) -> list[str]:
    """Return the names of frozen records whose bytes differ from their pins."""
    base = OUT_DIR if out_dir is None else out_dir
    mismatched = []
    for name, (sha256, size) in FROZEN_RECORDS.items():
        path = base / name
        raw = path.read_bytes() if path.is_file() else None
        if raw is None or len(raw) != size or hashlib.sha256(raw).hexdigest() != sha256:
            mismatched.append(name)
    return mismatched


def generate() -> None:
    """Frozen history since HDE-EPIC043 WU-PR-09: the records are never regenerated."""

    raise SystemExit(FROZEN_HISTORY_NOT_REGENERATED)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check the frozen HDE-EPIC030 PR-05 category-framework records (never regenerated)."
    )
    parser.add_argument("--check", action="store_true", help="verify the frozen records against their pins")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Parse arguments before anything else (HDE-CRD-0003 S19-R04); write mode refuses."""

    args = parse_args([] if argv is None else list(argv))
    if not args.check:
        generate()
    mismatched = frozen_record_mismatches()
    if mismatched:
        print(f"{FROZEN_RECORD_MISMATCH}:{','.join(mismatched)}", file=sys.stderr)
        return 1
    print("checked frozen HDE-EPIC030 PR-05 category-framework records (pinned SHA-256 and size)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
