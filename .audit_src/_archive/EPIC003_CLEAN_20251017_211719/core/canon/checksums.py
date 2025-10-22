"""
Checksums emitter for CANON_CHECKSUMS.json (v2).
Import-safe; no I/O at import time. Deterministic only.
"""
from typing import Dict, Any, Iterable, Tuple, List
import hashlib, re
from core.canon.validate import _iter_channel_pairs, _norm_channel_id

# Frozen top-level key set (v2)
V2_KEYS = (
    "adjacency_sha",
    "deg_vector",
    "channels_sorted",
    "gate_counts_by_center",
    "distinguished",
    "domain_coverage",
    "toggles_frozen_sha",
    "center_order",
)

CANON_CENTER_ORDER = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]
_HEX64 = re.compile(r"^[0-9a-f]{64}$")

def _sha256_hex_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def _deg_vector_from_pairs(pairs: Iterable[Tuple[int,int]]) -> List[int]:
    deg = [0]*65  # 1..64
    for a, b in pairs:
        if 1 <= a <= 64: deg[a] += 1
        if 1 <= b <= 64: deg[b] += 1
    return deg[1:]  # length 64

def _channels_sorted_from_pairs(pairs: Iterable[Tuple[int,int]]) -> List[str]:
    ids = {_norm_channel_id(a, b) for a, b in pairs}
    return sorted(ids)

def _gate_counts_by_center(gates: Any) -> Dict[str,int]:
    counts = {c: 0 for c in CANON_CENTER_ORDER}
    if isinstance(gates, list):
        for g in gates:
            if isinstance(g, dict):
                c = (g.get("center") or g.get("centre") or g.get("c") or "").lower()
                if c in counts:
                    counts[c] += 1
    return counts

def _toggles_frozen_sha(toggles: Any) -> str:
    # Stable JSON bytes for hashing using built-in canonicalization (sorted keys, separators)
    # We avoid importing sercanon here to keep this module pure; the outer scripts will enforce serializer guards.
    import json
    b = (json.dumps(toggles, ensure_ascii=False, separators=(",", ":"), sort_keys=True)).encode("utf-8")
    return _sha256_hex_bytes(b)

def _domain_coverage(gates: Any, channels_sorted: List[str]) -> Dict[str, Any]:
    # Coverage as sets (stable order): all centers; all channels by id; all gates 1..64 (if inferable)
    gates_list = list(range(1, 65))
    centers = list(CANON_CENTER_ORDER)
    chans = list(channels_sorted)
    return {"centers": centers, "channels": chans, "gates": gates_list}

def build_checksums(canon: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return the v2 checksums object with frozen top-level keys and deterministic values.
    """
    pairs = list(_iter_channel_pairs(canon.get("channels")))
    channels_sorted = _channels_sorted_from_pairs(pairs)
    # adjacency sha of the canonical edge-list (one per line, LF, no trailing blank line)
    edge_bytes = ("\n".join(channels_sorted)).encode("utf-8")
    deg_vector = _deg_vector_from_pairs(pairs)
    gate_counts = _gate_counts_by_center(canon.get("gates"))
    distinguished = {"degree_3_gates": [10, 20, 34, 57]}  # stable, contractually defined
    t_sha = _toggles_frozen_sha(canon.get("toggles"))
    center_order = list(CANON_CENTER_ORDER)
    dom = _domain_coverage(canon.get("gates"), channels_sorted)

    out = {
        "adjacency_sha": _sha256_hex_bytes(edge_bytes),
        "deg_vector": deg_vector,
        "channels_sorted": channels_sorted,
        "gate_counts_by_center": gate_counts,
        "distinguished": distinguished,
        "domain_coverage": dom,
        "toggles_frozen_sha": t_sha,
        "center_order": center_order,
    }
    # Ensure top-level key set exactly matches V2_KEYS (order enforced by serializer later)
    assert tuple(sorted(out.keys())) == tuple(sorted(V2_KEYS)), "v2 keys mismatch"
    return out
