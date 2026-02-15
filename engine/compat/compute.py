from __future__ import annotations
import hashlib, math
from typing import Any, Dict, List, Mapping, Tuple
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.thresholds import THRESHOLDS_V1, BANDS
from engine.compat.ordering import normalize_pair, pair_key

def _round_half_up(x: float) -> int:
    return int(math.floor(x + 0.5))

def _clamp(v: int) -> int:
    return 0 if v < 0 else 100 if v > 100 else v

def band_for(score: int) -> str:
    if score <= THRESHOLDS_V1["cool_max"]: return "Cool"
    if score <= THRESHOLDS_V1["open_max"]: return "Open"
    if score <= THRESHOLDS_V1["warm_max"]: return "Warm"
    return "Glow"

def _score_for(cat: str, pair_k: str, weights: Dict[str,int]) -> int:
    # Base (0..100) from stable hash of (pair_key, category)
    h = hashlib.sha256(f"{pair_k}:{cat}".encode("utf-8")).digest()
    base = h[0] % 101
    w = weights.get(cat, 0) / 100.0  # 0..1
    # Weighting: lift range linearly toward 100 as weight increases
    val = base * (0.5 + 0.5*w)
    return _clamp(_round_half_up(val))

def _keys_for(cat: str, band: str) -> Tuple[str,str]:
    b = band.lower()
    return (f"{cat}_{b}_personal_v1", f"{cat}_{b}_shared_v1")

def compat_public(a: Dict[str,object], b: Dict[str,object],
                  viewer_top: str, viewer_weights: Dict[str,int],
                  engine_tag: str, release_id: str, invocation_tag: str) -> Dict[str,object]:
    # AB↔BA identity by normalization
    a1,b1 = normalize_pair(a,b)
    pkey = pair_key(a1,b1)
    cats: List[Dict[str,object]] = []
    for cat in CATEGORIES_ORDER_V1:
        sc = _score_for(cat, pkey, viewer_weights)
        bd = band_for(sc)
        pk, sk = _keys_for(cat, bd)
        cats.append({"id":cat, "score":sc, "band":bd, "personal_key":pk, "shared_key":sk})
    return {"categories": cats, "meta":{"engine_tag":engine_tag,"release_id":release_id,"invocation_tag":invocation_tag}}


def _person_from_resolved(resolved: Mapping[str, Any]) -> Dict[str, str]:
    if "person_uid" in resolved and isinstance(resolved["person_uid"], str):
        return {"person_uid": resolved["person_uid"]}
    person = resolved.get("person")
    if isinstance(person, Mapping) and isinstance(person.get("person_uid"), str):
        return {"person_uid": person["person_uid"]}
    raise ValueError("resolved bodygraph must include person_uid")


def conjunction_public(
    left_resolved: Mapping[str, Any],
    right_resolved: Mapping[str, Any],
    *,
    viewer_top: str,
    viewer_weights: Dict[str, int],
    engine_tag: str,
    release_id: str,
    invocation_tag: str,
) -> Dict[str, object]:
    """Build a deterministic conjunction contract payload for canonical emission."""
    left = _person_from_resolved(left_resolved)
    right = _person_from_resolved(right_resolved)
    left, right = normalize_pair(left, right)
    compat = compat_public(
        left,
        right,
        viewer_top,
        viewer_weights,
        engine_tag=engine_tag,
        release_id=release_id,
        invocation_tag=invocation_tag,
    )
    return {
        "conjunction": {
            "left": left,
            "right": right,
            "compat": compat,
        }
    }
