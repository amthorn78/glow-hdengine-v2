#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.runtime.determinism_env import ensure_determinism_env
from engine.sampler.core import CandidateFeatures, ViewerProfile, build_candidate_pool
from engine.serializer.canon import sercanon
from engine.validation.viewer_prefs import normalize_viewer_prefs, validate_viewer_prefs

OUT_DIR = ROOT / "audit" / "qa" / "hde-epic030" / "pr-01"


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _valid_prefs() -> dict[str, object]:
    return {
        "top_category": CATEGORIES_ORDER_V1[0],
        "weights": {category: 1 for category in CATEGORIES_ORDER_V1},
    }


def generate() -> None:
    ensure_determinism_env()

    prefs = _valid_prefs()
    excluded_category = CATEGORIES_ORDER_V1[2]
    retained_category = CATEGORIES_ORDER_V1[3]
    weights = prefs["weights"]
    assert isinstance(weights, dict)
    weights[excluded_category] = 0
    weights[retained_category] = 2

    err = validate_viewer_prefs(prefs)
    if err is not None:
        raise SystemExit("VALID_PREFS_REJECTED")
    normalized = normalize_viewer_prefs(prefs)
    normalized_weights = normalized["weights"]
    assert isinstance(normalized_weights, dict)

    candidates = [
        CandidateFeatures(
            person_uid="zero-weight-candidate",
            weight=float(normalized_weights[excluded_category]),
            compat_score=80,
            categories=(excluded_category,),
        ),
        CandidateFeatures(
            person_uid="positive-weight-candidate",
            weight=float(normalized_weights[retained_category]),
            compat_score=80,
            categories=(retained_category,),
        ),
    ]
    pool = build_candidate_pool(ViewerProfile(person_uid="viewer-pr01"), candidates)

    handoff_payload = {
        "schema": "hde_epic030.pr01.zero_weight_handoff.v1",
        "viewer_prefs_normalized": normalized,
        "candidate_weight_projection": [
            {
                "person_uid": candidate.person_uid,
                "category": list(candidate.categories or [None])[0],
                "weight": candidate.weight,
            }
            for candidate in candidates
        ],
        "sampler_pool_candidate_ids": [cand.person_uid for cand in pool.candidates],
        "excluded_ids": sorted({candidate.person_uid for candidate in candidates} - {cand.person_uid for cand in pool.candidates}),
    }
    _write_bytes(OUT_DIR / "zero_weight_handoff.json", sercanon(handoff_payload, sort_keys=True))

    normalized_bytes = sercanon(normalized, sort_keys=True)
    reparsed_bytes = sercanon(json.loads(normalized_bytes.decode("utf-8")), sort_keys=True)
    canonical_log = "\n".join(
        [
            "schema: hde_epic030.pr01.normalization_canonical_compare.v1",
            f"normalized_sha256_matches_reparse: {normalized_bytes == reparsed_bytes}",
            f"normalized_len: {len(normalized_bytes)}",
            f"reparsed_len: {len(reparsed_bytes)}",
            "status: PASS" if normalized_bytes == reparsed_bytes else "status: FAIL",
            "",
        ]
    )
    _write_text(OUT_DIR / "normalization_canonical_compare.log", canonical_log)

    invalid_cases = {
        "missing_weights": {"top_category": CATEGORIES_ORDER_V1[0]},
        "unknown_top_category": {"top_category": "unknown", "weights": {category: 1 for category in CATEGORIES_ORDER_V1}},
        "out_of_range_weight": {
            "top_category": CATEGORIES_ORDER_V1[0],
            "weights": {**{category: 1 for category in CATEGORIES_ORDER_V1}, CATEGORIES_ORDER_V1[0]: 101},
        },
    }
    lines = ["schema: hde_epic030.pr01.invalid_viewer_prefs.v1"]
    for name, case in invalid_cases.items():
        lines.append(f"{name}: {'PASS' if validate_viewer_prefs(case) is not None else 'FAIL'}")
    lines.append("")
    _write_text(OUT_DIR / "invalid_viewer_prefs.log", "\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate EPIC030 PR-01 normalization evidence artifacts")
    _ = parser.parse_args()
    generate()


if __name__ == "__main__":
    main()
