from __future__ import annotations
import hashlib, math
from typing import Any, Dict, List, Mapping, Tuple
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.resolver import resolve_bodygraph
from engine.bodygraph.vendor_client import VendorError
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


def _resolved_person_with_hint(raw: Mapping[str, Any], *, uid_hint: str | None = None) -> Dict[str, str] | None:
    try:
        return _person_from_resolved(raw)
    except ValueError:
        if isinstance(uid_hint, str) and uid_hint.strip():
            return {"person_uid": uid_hint.strip()}
    return None


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


def _conjunction_user_id(raw: object) -> str | None:
    if isinstance(raw, str) and raw.strip():
        return raw.strip()
    if not isinstance(raw, Mapping):
        return None
    direct = raw.get("user_id")
    if isinstance(direct, str) and direct.strip():
        return direct.strip()
    person = raw.get("person")
    if isinstance(person, Mapping):
        nested = person.get("user_id")
        if isinstance(nested, str) and nested.strip():
            return nested.strip()
    return None


def _birth_fields(raw: object) -> Tuple[str | None, str | None, str | None]:
    if not isinstance(raw, Mapping):
        return None, None, None
    birthdate = raw.get("birthdate")
    birthtime = raw.get("birthtime")
    location = raw.get("location")
    values: list[str | None] = []
    for value in (birthdate, birthtime, location):
        if isinstance(value, str) and value.strip():
            values.append(value.strip())
        else:
            values.append(None)
    return values[0], values[1], values[2]


def conjunction_public_resolved(
    left: Mapping[str, Any] | str,
    right: Mapping[str, Any] | str,
    *,
    viewer_top: str,
    viewer_weights: Dict[str, int],
    engine_tag: str,
    release_id: str,
    invocation_tag: str,
    env: Mapping[str, object] | None = None,
    local_lookup: Any | None = None,
) -> Dict[str, object]:
    """Resolve unresolved conjunction inputs via the bodygraph resolver, then emit deterministic payload."""

    def _lookup(user_id: str) -> Mapping[str, Any] | None:
        if local_lookup is None:
            return None
        entry = local_lookup(user_id)
        if isinstance(entry, Mapping):
            return entry
        return None

    def _resolve_party(raw: Mapping[str, Any] | str) -> Mapping[str, Any]:
        if isinstance(raw, Mapping):
            hinted = _resolved_person_with_hint(raw)
            if hinted is not None:
                return hinted
        user_id = _conjunction_user_id(raw)
        if not user_id:
            raise ValueError("conjunction input must be resolved bodygraph or include user_id")
        normalized = resolve_db_user_id(user_id)
        local = _lookup(normalized)
        if local is not None:
            hinted = _resolved_person_with_hint(local, uid_hint=normalized)
            if hinted is not None:
                return hinted
        birthdate, birthtime, location = _birth_fields(raw)
        outcome = resolve_bodygraph(
            normalized,
            source="vendor",
            upsert=True,
            dry_run=False,
            env=env,
            birthdate=birthdate,
            birthtime=birthtime,
            location=location,
        )
        if outcome.status != "ok":
            error = outcome.payload.get("error") if isinstance(outcome.payload, Mapping) else None
            if isinstance(error, Mapping):
                code = str(error.get("code") or "PROVIDER_UNAVAILABLE")
                message = str(error.get("message") or "resolver unavailable")
                details = error.get("details")
                if isinstance(details, Mapping):
                    raise VendorError(code, message, details=details)
                raise VendorError(code, message)
            raise VendorError("PROVIDER_UNAVAILABLE", "resolver unavailable")
        local_after = _lookup(normalized)
        if local_after is not None:
            hinted = _resolved_person_with_hint(local_after, uid_hint=normalized)
            if hinted is not None:
                return hinted
        raise VendorError("PROVIDER_UNAVAILABLE", "resolved bodygraph unavailable in local cache")

    left_resolved = _resolve_party(left)
    right_resolved = _resolve_party(right)
    return conjunction_public(
        left_resolved,
        right_resolved,
        viewer_top=viewer_top,
        viewer_weights=viewer_weights,
        engine_tag=engine_tag,
        release_id=release_id,
        invocation_tag=invocation_tag,
    )
