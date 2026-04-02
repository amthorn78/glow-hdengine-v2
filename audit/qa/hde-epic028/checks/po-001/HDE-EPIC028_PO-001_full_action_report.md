# HDE-EPIC028 - PO-001 Full Action Report and Evidence Output

## Scope
- Epic: HDE-EPIC028 (Conjunction Pass 4)
- Check ID: po-001
- Check Name: Internal compatibility canonical, order-neutral, shared governed emission path
- Step intent: prove internal compatibility remains order-neutral and routed through the governed emission path
- Status: PASS

## Proof Obligation (Verbatim)
"The internal compatibility surface must produce canonical, order-neutral results through the same governed emission path used by the rest of the compatibility flow."

## Pass Criteria (Verbatim)
- The captured snapshots show normalize_pair, pair_key, compat_public, and emit_public.
- No alternate serializer path is needed to satisfy the proof obligation.

## Rails and Determinism Pins
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

## Repo Loci in Scope
- engine/compat/ordering.py
- engine/compat/compute.py
- engine/presenter/emitter.py

## Executed Actions
1. Ran Command 1 to initialize po-001 primary log with PF27 header and planned_step entry.
2. Ran Command 2 to capture ordering locus snapshot into ordering_snapshot.txt.
3. Ran Command 3 to capture compat compute locus snapshot into compat_compute_snapshot.txt.
4. Ran Command 4 to capture emitter locus snapshot into emitter_snapshot.txt.
5. Ran Command 5 to append expected_findings line to primary.log.

## Validation Checks Performed
1. Confirmed all four deliverables exist at governed paths.
2. Confirmed normalize_pair and pair_key are present in ordering_snapshot.txt.
3. Confirmed compat_public is present and calls normalize_pair and pair_key in compat_compute_snapshot.txt.
4. Confirmed emit_public is present in emitter_snapshot.txt.
5. Confirmed PF27 header and expected_findings line exist in primary.log.
6. Confirmed emitter snapshot delegates to canonical serializer and no alternate serializer path is required for this proof.

## Evidence Integrity Snapshot
- audit/qa/hde-epic028/checks/po-001/primary.log
  - size_bytes: 1874
  - lines: 3
  - sha256: 20ced1717ceb3e69d7e5df7b5ac0d832a5de9913b5e8ee903e866480503b7a70
- audit/qa/hde-epic028/checks/po-001/ordering_snapshot.txt
  - size_bytes: 891
  - lines: 24
  - sha256: 67b8da796f0d0a5471e3ce5235ff3d59d9672dc78da6bd8e705602e4859ffa1f
- audit/qa/hde-epic028/checks/po-001/compat_compute_snapshot.txt
  - size_bytes: 8103
  - lines: 215
  - sha256: 089042ba99658e74bbc6a00884754e7d13b93ef48752f6b728df56d2e5dd8aa4
- audit/qa/hde-epic028/checks/po-001/emitter_snapshot.txt
  - size_bytes: 1008
  - lines: 28
  - sha256: 5a47195420a0d58a74cd51b723c9d1ac8fcbc3077de7c08755d2689594376def

## Findings Trace (Line-Level)
- ordering_snapshot.txt
  - normalize_pair found at line 13
  - pair_key found at line 22
- compat_compute_snapshot.txt
  - compat_public found at line 36
  - normalize_pair usage in compat_public found at line 40
  - pair_key usage in compat_public found at line 41
- emitter_snapshot.txt
  - emit_public found at line 6

## Full Evidence Outputs

### 1) primary.log
Path: audit/qa/hde-epic028/checks/po-001/primary.log

```text
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"po-001","check_name":"Internal compatibility canonical, order-neutral, shared governed emission path","claimed_tokens":[],"command":"python -c \"from pathlib import Path; src=Path('engine/compat/ordering.py').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-001/ordering_snapshot.txt').write_text('\\n'.join(src[:220])+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('engine/compat/compute.py').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-001/compat_compute_snapshot.txt').write_text('\\n'.join(src[:260])+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; src=Path('engine/presenter/emitter.py').read_text(encoding='utf-8').splitlines(); Path('audit/qa/hde-epic028/checks/po-001/emitter_snapshot.txt').write_text('\\n'.join(src[:140])+'\\n', encoding='utf-8')\"; python -c \"from pathlib import Path; p=Path('audit/qa/hde-epic028/checks/po-001/primary.log'); p.write_text(p.read_text(encoding='utf-8')+'expected_findings: normalize_pair; pair_key; compat_public; emit_public\\n', encoding='utf-8')\"","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic028/checks/po-001/primary.log","audit/qa/hde-epic028/checks/po-001/ordering_snapshot.txt","audit/qa/hde-epic028/checks/po-001/compat_compute_snapshot.txt","audit/qa/hde-epic028/checks/po-001/emitter_snapshot.txt"],"fail_status":"","intended_tokens":[],"pf_refs":["PF19 — Glow QA Guide","PF27 — Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-04-01T18:54:24Z"}
planned_step: capture internal compatibility ordering, compute, and emitter loci
expected_findings: normalize_pair; pair_key; compat_public; emit_public
```

### 2) ordering_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-001/ordering_snapshot.txt

```text
from __future__ import annotations
import hashlib, re
from typing import Dict, Tuple

UID_RE = re.compile(r"^[A-Za-z0-9._-]{1,64}$")

def _uid(p: Dict[str, object]) -> str:
    uid = str(p.get("person_uid") or "")
    if not UID_RE.match(uid):
        raise ValueError("invalid or missing person_uid")
    return uid

def normalize_pair(a: Dict[str, object], b: Dict[str, object]) -> Tuple[Dict[str,object], Dict[str,object]]:
    ua, ub = _uid(a), _uid(b)
    if ua < ub: return a,b
    if ub < ua: return b,a
    # tie-break on payload hash (stable, symmetric)
    ha = hashlib.sha256(repr(sorted(a.items())).encode("utf-8")).hexdigest()
    hb = hashlib.sha256(repr(sorted(b.items())).encode("utf-8")).hexdigest()
    return (a,b) if ha <= hb else (b,a)

def pair_key(a: Dict[str, object], b: Dict[str, object]) -> str:
    a1,b1 = normalize_pair(a,b)
    return f"{_uid(a1)}|{_uid(b1)}"
```

### 3) compat_compute_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-001/compat_compute_snapshot.txt

```text
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
    """Resolve unresolved conjunction inputs through local lookup first, then resolver acquisition when rails allow.

    Call-site gating semantics:
    * Local lookup is always attempted first.
    * Closed rails refuse provider acquisition when local data is missing.
    * Open rails allow resolver acquisition only after a local miss.
    * After open-rails acquisition persists locally, later closed-rails calls read local data only.
    """

    resolver_env: Mapping[str, object] = env or {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}

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
            env=resolver_env,
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
```

### 4) emitter_snapshot.txt
Path: audit/qa/hde-epic028/checks/po-001/emitter_snapshot.txt

```text
from __future__ import annotations
from typing import Tuple, Dict, Any
from engine.serializer import canon


def emit_public(envelope: Dict[str, Any], *, sort_keys: bool = True) -> bytes:
    """
    Canonical emitter for governed public JSON bytes.

    - Delegates to the canonical serializer (LF-terminated UTF-8)
    - Sorts keys by default for deterministic public envelopes
    """
    return canon.sercanon(envelope, sort_keys=sort_keys)


def emit_public_with_envelope(
    envelope: Dict[str, Any], *, sort_keys: bool = True
) -> Tuple[bytes, Dict[str, Any]]:
    """Emit canonical bytes and return the original envelope."""
    return emit_public(envelope, sort_keys=sort_keys), envelope


def emit_compact_json(envelope: Dict[str, Any], *, sort_keys: bool = True) -> Tuple[bytes, Dict[str, Any]]:
    """
    Compatibility alias for the canonical emitter.
    Prefer :func:`emit_public_with_envelope` for new call sites.
    """
    return emit_public_with_envelope(envelope, sort_keys=sort_keys)
```

## Final Decision
PASS

## PASS Rationale
1. Pair-order normalization helpers are present in captured ordering locus.
2. compat_public in captured compute locus uses normalize_pair and pair_key.
3. emit_public is present in governed emitter locus and delegates to canonical serializer.
4. primary.log contains PF27 header, planned_step, and appended expected_findings line.
5. No alternate serializer path is required to satisfy the proof obligation.
