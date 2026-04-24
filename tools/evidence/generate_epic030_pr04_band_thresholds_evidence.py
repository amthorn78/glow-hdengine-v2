#!/usr/bin/env python3
"""Generate EPIC030 PR-04 band-threshold/tuning evidence artifacts."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.compat.thresholds import BANDS, THRESHOLDS_V1
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon

OUT_DIR = ROOT / "audit" / "qa" / "hde-epic030" / "pr-04"
COMPAT_AB_PATH = ROOT / "artifacts" / "compat" / "AB.json"
COMPAT_BA_PATH = ROOT / "artifacts" / "compat" / "BA.json"
BAND_EDGES_PATH = ROOT / "artifacts" / "thresholds" / "band_edges.json"


def _iso_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(sercanon(payload, sort_keys=True))


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text = f"{text}\n"
    path.write_text(text, encoding="utf-8")


def generate() -> None:
    ensure_determinism_env()

    produced_at = _iso_now()
    band_edges = json.loads(BAND_EDGES_PATH.read_text(encoding="utf-8"))
    edges = [int(v) for v in band_edges["edges"]]

    expected_thresholds = {
        "cool_max": edges[0],
        "open_max": edges[1],
        "warm_max": edges[2],
    }

    compact_diffs: list[dict[str, object]] = []
    for key, expected in expected_thresholds.items():
        observed = int(THRESHOLDS_V1[key])
        compact_diffs.append(
            {
                "field": key,
                "expected": expected,
                "observed": observed,
                "delta": observed - expected,
                "match": observed == expected,
            }
        )

    band_name_match = list(BANDS) == list(band_edges.get("bands", []))
    compact_diffs.append(
        {
            "field": "bands",
            "expected": list(band_edges.get("bands", [])),
            "observed": list(BANDS),
            "match": band_name_match,
        }
    )

    diff_payload = {
        "schema": "hde_epic030.pr04.band_thresholds_diff.v1",
        "epic_id": "HDE-EPIC030",
        "task_id": "HDE-DISS005",
        "subtask_ids": ["HDE-DISS005.2", "HDE-DISS005.3", "HDE-DISS005.4"],
        "produced_at_utc": produced_at,
        "constants_pack_source": "artifacts/thresholds/band_edges.json",
        "compat_thresholds_source": "engine.compat.thresholds.THRESHOLDS_V1",
        "diffs": compact_diffs,
        "status": "PASS" if all(bool(item.get("match")) for item in compact_diffs) else "FAIL",
    }
    _write_json(OUT_DIR / "band_thresholds_diff.json", diff_payload)

    runs: list[tuple[str, Path]] = [("AB", COMPAT_AB_PATH), ("BA", COMPAT_BA_PATH)]
    identity_lines = [
        "schema: hde_epic030.pr04.band_thresholds_identity_hash.v1",
        f"produced_at_utc: {produced_at}",
        "epic_id: HDE-EPIC030",
        "task_id: HDE-DISS005",
        "subtask_id: HDE-DISS005.3",
        "hash_basis: sha256 of LF-terminated compat body",
    ]
    run_hashes: dict[str, str] = {}
    all_ok = True
    for run_id, path in runs:
        data = path.read_bytes()
        if not data.endswith(b"\n"):
            data = data + b"\n"
        digest = hashlib.sha256(data).hexdigest()
        run_hashes[run_id] = digest
        identity_lines.extend(
            [
                f"run_{run_id}_source: {path.relative_to(ROOT).as_posix()}",
                f"run_{run_id}_identity_hash: {digest}",
            ]
        )
    ab_ba_identity_match = run_hashes.get("AB") == run_hashes.get("BA")
    all_ok = all_ok and ab_ba_identity_match
    identity_lines.append(f"ab_ba_identity_match: {ab_ba_identity_match}")
    if (OUT_DIR / "band_thresholds_identity_hash.txt").exists():
        previous = {
            line.split(":", 1)[0]: line.split(":", 1)[1].strip()
            for line in (OUT_DIR / "band_thresholds_identity_hash.txt").read_text(encoding="utf-8").splitlines()
            if ":" in line
        }
        for run_id, _ in runs:
            key = f"run_{run_id}_identity_hash"
            now = next((line.split(":", 1)[1].strip() for line in identity_lines if line.startswith(f"{key}:")), "")
            before = previous.get(key)
            if before and before != now:
                all_ok = False
                identity_lines.append(f"run_{run_id}_changed_from_previous: true")
    identity_lines.append(f"status: {'PASS' if all_ok else 'FAIL'}")
    _write_text(OUT_DIR / "band_thresholds_identity_hash.txt", "\n".join(identity_lines))

    binding_lines = [
        "schema: hde_epic030.pr04.band_edges_binding.v1",
        f"produced_at_utc: {produced_at}",
        "epic_id: HDE-EPIC030",
        "task_id: HDE-DISS005",
        "subtask_id: HDE-DISS005.2",
        "constants_pack_artifact: artifacts/thresholds/band_edges.json",
        "compat_thresholds_binding: engine.compat.thresholds.THRESHOLDS_V1",
        f"bands: {','.join(BANDS)}",
        f"edges: {','.join(str(v) for v in edges)}",
        f"thresholds_v1: cool_max={THRESHOLDS_V1['cool_max']},open_max={THRESHOLDS_V1['open_max']},warm_max={THRESHOLDS_V1['warm_max']}",
        f"status: {'PASS' if diff_payload['status'] == 'PASS' else 'FAIL'}",
    ]
    _write_text(OUT_DIR / "band_edges_binding.log", "\n".join(binding_lines))


if __name__ == "__main__":
    generate()
