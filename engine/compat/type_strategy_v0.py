from __future__ import annotations
from typing import Any, Dict, Iterable, List

# Import-time caches must remain None (tests rely on this)
_type_strategy_map: Dict[str, Any] | None = None
_band_rules: Dict[str, str] | None = None
_band_order: List[str] | None = None

# Minimal stubs so import succeeds; real logic will land later.
def extract_ts(chart_norm: Dict[str, Any]) -> Dict[str, str]:
    return {"type": "", "strategy": ""}

def features(a: Dict[str, str], b: Dict[str, str]) -> Dict[str, bool]:
    return {"strategy_match": False, "sacral_pair": False, "projector_to_generator": False}

def band_v0(feat: Dict[str, bool]) -> str:
    return "Warm"

def compute_fingerprint(gates: Iterable[int]) -> str:
    import json, hashlib
    ints = sorted({int(g) for g in gates if isinstance(g, int) or (isinstance(g, str) and str(g).isdigit())})
    canon = json.dumps({"gates": ints}, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()
