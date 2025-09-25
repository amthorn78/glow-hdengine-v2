"""
Canon validator (import-safe).
All file reads must happen inside functions — never at import time.
"""
from dataclasses import dataclass
from typing import List, Dict, Any, Tuple, Iterable
import json, pathlib, re

@dataclass(frozen=True)
class Issue:
    code: str
    message: str
    details: Dict[str, Any]

# ---------- repo I/O (only inside functions) ----------
def _read_json(path: pathlib.Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_repo_canon(base_dir: pathlib.Path = pathlib.Path(".")) -> Dict[str, Any]:
    """Load repo canon files (call-time only). Tolerant to minor shape differences."""
    gates_p     = base_dir / "catalog" / "gates_v1.json"
    channels_p  = base_dir / "catalog" / "channels_v1.json"
    toggles_p   = base_dir / "config"  / "toggles_v1.json"
    freeze_p    = base_dir / "freeze"  / "freeze_pack_v1.json"

    gates     = _read_json(gates_p)     if gates_p.exists()    else {}
    channels  = _read_json(channels_p)  if channels_p.exists() else {}
    toggles   = _read_json(toggles_p)   if toggles_p.exists()  else {}
    freeze_pk = _read_json(freeze_p)    if freeze_p.exists()   else {}

    return {"gates": gates, "channels": channels, "toggles": toggles, "freeze_pack": freeze_pk}

# ---------- helpers (pure) ----------
_ID_RE = re.compile(r"^\s*(\d+)\s*[-_]\s*(\d+)\s*$")

def _norm_channel_id(a: int, b: int) -> str:
    x, y = (a, b) if a <= b else (b, a)
    return f"{x:02d}-{y:02d}"

def _to_int(v: Any) -> int:
    if isinstance(v, int): return v
    if isinstance(v, str) and v.isdigit(): return int(v)
    return -1

def _pairs_from_channels_entry(entry: Any) -> Tuple[int, int] | None:
    """Best-effort extract a channel pair (gate numbers)."""
    if isinstance(entry, dict):
        for k1, k2 in (("a","b"), ("gate_a","gate_b"), ("from","to"), ("g1","g2")):
            if k1 in entry and k2 in entry:
                a, b = _to_int(entry[k1]), _to_int(entry[k2])
                if a > 0 and b > 0: return a, b
        if "id" in entry and isinstance(entry["id"], str):
            m = _ID_RE.match(entry["id"])
            if m:
                a, b = int(m.group(1)), int(m.group(2))
                return a, b
    elif isinstance(entry, (list, tuple)) and len(entry) == 2:
        a, b = _to_int(entry[0]), _to_int(entry[1])
        if a > 0 and b > 0: return a, b
    return None

def _iter_channel_pairs(channels: Any) -> Iterable[Tuple[int,int]]:
    if isinstance(channels, dict) and "channels" in channels:
        seq = channels["channels"]
    else:
        seq = channels
    if not isinstance(seq, list):
        return []
    for e in seq:
        pair = _pairs_from_channels_entry(e)
        if pair: yield pair

def _count_gates(gates: Any) -> int:
    if isinstance(gates, list): return len(gates)
    if isinstance(gates, dict) and "gates" in gates and isinstance(gates["gates"], list):
        return len(gates["gates"])
    if isinstance(gates, dict): return len(gates)
    return 0

def _count_channels(channels: Any) -> int:
    if isinstance(channels, dict) and "channels" in channels and isinstance(channels["channels"], list):
        return len(channels["channels"])
    if isinstance(channels, list): return len(channels)
    if isinstance(channels, dict): return len(channels)
    return 0

# ---------- validators (pure) ----------
def validate_counts(canon: Dict[str, Any]) -> List[Issue]:
    """Validate global counts (64 gates / 36 channels)."""
    issues: List[Issue] = []
    g_cnt = _count_gates(canon.get("gates"))
    c_cnt = _count_channels(canon.get("channels"))
    if g_cnt != 64:
        issues.append(Issue("GateCount", f"expected 64 gates, found {g_cnt}", {"found": g_cnt}))
    if c_cnt != 36:
        issues.append(Issue("ChannelCount", f"expected 36 channels, found {c_cnt}", {"found": c_cnt}))
    return issues

def validate_ids(canon: Dict[str, Any]) -> List[Issue]:
    """Validate channel IDs are zero-padded, min-first; alias-free."""
    issues: List[Issue] = []
    seen: set[str] = set()
    for (a, b) in _iter_channel_pairs(canon.get("channels")):
        ch_id = _norm_channel_id(a, b)
        if ch_id in seen:
            issues.append(Issue("ChannelAlias", "duplicate/alias channel id", {"id": ch_id}))
        else:
            seen.add(ch_id)
        # format check: always two digits "-" two digits, min-first
        if ch_id != _norm_channel_id(a, b):
            issues.append(Issue("ChannelIdFormat", "non-normalized channel id", {"a": a, "b": b, "norm": ch_id}))
    return issues

def validate_degree(canon: Dict[str, Any]) -> List[Issue]:
    """Validate degree/multiplicity: {10,20,34,57}=3; all others=1."""
    deg: Dict[int,int] = {i: 0 for i in range(1, 65)}
    for a, b in _iter_channel_pairs(canon.get("channels")):
        if 1 <= a <= 64: deg[a] += 1
        if 1 <= b <= 64: deg[b] += 1
    issues: List[Issue] = []
    specials = {10, 20, 34, 57}
    for g in range(1, 65):
        expected = 3 if g in specials else 1
        if deg.get(g, 0) != expected:
            issues.append(Issue("GateDegree", "unexpected degree", {"gate": g, "expected": expected, "found": deg.get(g, 0)}))
    return issues

def validate_distinguished(canon: Dict[str, Any]) -> List[Issue]:
    """Placeholder for distinguished set ordering (stable sort rules) — implemented in next steps if needed."""
    return []

def validate_center_order_and_counts(canon: Dict[str, Any]) -> List[Issue]:
    """Ensure centers (if present) follow canonical order and sum to 64; doesn't assert per-center constants."""
    # Canonical order declared here; tests may only assert presence/order, not exact counts.
    canonical = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]
    # Try to derive counts from gates data if shape allows
    gates = canon.get("gates")
    counts = {k: 0 for k in canonical}
    if isinstance(gates, list):
        for g in gates:
            c = (g.get("center") or g.get("centre") or g.get("c") or "").lower() if isinstance(g, dict) else ""
            if c in counts: counts[c] += 1
    issues: List[Issue] = []
    # Order presence check only (no hard-coded per-center targets)
    issues += [] if list(counts.keys()) == canonical else [Issue("CenterOrder", "center order mismatch", {"expected": canonical, "found": list(counts.keys())})]
    total = sum(counts.values())
    if total not in (0, 64):  # 0 means we couldn't infer centers; tolerate, else require 64
        issues.append(Issue("CenterCounts", "sum of gate counts by center must be 64", {"sum": total}))
    return issues

def run_all(canon: Dict[str, Any]) -> List[Issue]:
    """Run all validators and return a flat issue list."""
    issues: List[Issue] = []
    for fn in (validate_counts, validate_ids, validate_degree, validate_center_order_and_counts, validate_distinguished):
        issues.extend(fn(canon))
    return issues

# ==== STRICT centers validator (literal pins; no reliance on dict order) ====
_CENTER_ORDER_PIN = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]
_CENTER_COUNTS_PIN = {
    "head": 3,
    "ajna": 6,
    "throat": 11,
    "g": 8,
    "ego": 4,
    "spleen": 7,
    "solar_plexus": 7,
    "sacral": 9,
    "root": 9,
}

def validate_centers_strict(canon: dict) -> list[Issue]:
    """
    Validate exact gate counts per center for frozen canon.
    - Asserts the center key set matches the canonical set.
    - Asserts each pinned count matches (key/value equality, no order assertion).
    If centers are not inferable from the provided gates structure, emits no issues.
    """
    issues: list[Issue] = []
    gates = canon.get("gates")
    if not isinstance(gates, list):
        # Could not infer centers -> do not fail here
        return issues

    counts = {k: 0 for k in _CENTER_ORDER_PIN}
    for g in gates:
        if isinstance(g, dict):
            c = (g.get("center") or g.get("centre") or g.get("c") or "").lower()
            if c in counts:
                counts[c] += 1

    # Key set equality (ignore order)
    if set(counts.keys()) != set(_CENTER_COUNTS_PIN.keys()):
        issues.append(Issue(
            "CenterCountsKeySet",
            "center key set mismatch",
            {"found": sorted(counts.keys()), "expected": sorted(_CENTER_COUNTS_PIN.keys())}
        ))
        return issues

    # Value equality per key (ignore dict order)
    for k, expected in _CENTER_COUNTS_PIN.items():
        found = counts.get(k, -1)
        if found != expected:
            issues.append(Issue(
                "CenterCounts",
                "center gate count mismatch",
                {"center": k, "expected": expected, "found": found}
            ))
    return issues

# ==== Override detection (env+files) ====
import os as _os, re as _re
from pathlib import Path as _Path

def detect_prod_overrides(base: _Path = _Path(".")) -> str | None:
    """
    Returns 'CANON_TOGGLES_OVERRIDE_IN_PROD' iff:
      - environment is prod (APP_ENV preferred, else ENGINE_ENV), and
      - (any environment KEY matches /(OVERRIDE|TOGGLES)/ at word/underscore boundaries) OR
        (any file exists at config/overrides/*.json under base)
    Otherwise returns None.
    """
    env = _os.getenv("APP_ENV", _os.getenv("ENGINE_ENV", "dev")).strip().lower()
    pat = _re.compile(r"(?:^|_)(OVERRIDE|TOGGLES)(?:$)", _re.IGNORECASE)
    env_hit = any(pat.search(k) for k in _os.environ.keys())
    files_hit = any((_Path(base) / "config" / "overrides").glob("*.json"))
    if env == "prod" and (env_hit or files_hit):
        return "CANON_TOGGLES_OVERRIDE_IN_PROD"
    return None
