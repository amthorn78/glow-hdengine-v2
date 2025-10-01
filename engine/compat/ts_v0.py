from __future__ import annotations

class CompatError(Exception):
    def __init__(self, code: str, details: dict | None = None):
        super().__init__(code)
        self.code = code
        self.details = details or {}
TYPE_TO_STRATEGY = {
    "Generator": "Wait to respond",
    "Manifesting Generator": "Wait to respond",
    "Projector": "Wait for the invitation",
    "Manifestor": "Inform",
    "Reflector": "Wait a lunar cycle",
}

def _canon_type(s: str) -> str:
    s = (s or "").strip()
    low = s.lower().replace("-", " ").replace("_", " ").replace("/", " ")
    aliases = {
        "mg": "Manifesting Generator",
        "manifesting generator": "Manifesting Generator",
        "generator": "Generator",
        "projector": "Projector",
        "manifestor": "Manifestor",
        "reflector": "Reflector",
    }
    # Prefer canonical casing when recognized
    if low in aliases:
        return aliases[low]
    titled = " ".join(w.capitalize() for w in low.split())
    return titled if titled in TYPE_TO_STRATEGY else s

def type_to_strategy(t: str) -> str:
    t_can = _canon_type(t)
    if t_can in TYPE_TO_STRATEGY:
        return TYPE_TO_STRATEGY[t_can]
    raise CompatError("TS_FEATURES_UNAVAILABLE", {"type": t})
def extract_ts(chart_norm: dict) -> dict:
    mech = chart_norm.get("mechanics") or {}
    raw_type = mech.get("type")
    if not isinstance(raw_type, str) or not raw_type.strip():
        raise CompatError("TS_FEATURES_UNAVAILABLE", {"have_type": bool(raw_type)})
    t_can = _canon_type(raw_type)
    strat = type_to_strategy(t_can)  # may raise CompatError for unknown types
    return {"type": t_can, "strategy": strat}

def compute_features(a_ts: dict, b_ts: dict) -> dict[str, bool]:
    sacral = {"Generator", "Manifesting Generator"}
    a_type, b_type = a_ts["type"], b_ts["type"]
    a_strat, b_strat = a_ts["strategy"], b_ts["strategy"]
    return {
        "strategy_match": (a_strat == b_strat),
        # REDLINE: True only when BOTH are sacral
        "sacral_pair": (a_type in sacral) and (b_type in sacral),
        "projector_to_generator": (
            (a_type == "Projector" and b_type in sacral) or
            (b_type == "Projector" and a_type in sacral)
        ),
    }

def band_v0(features: dict[str, bool]) -> str:
    # A3 rule: Warm iff sacral_pair else Open
    return "Warm" if features.get("sacral_pair") else "Open"
def extract_ts(chart_norm: dict) -> dict:
    mech = chart_norm.get("mechanics") or {}
    raw_type = mech.get("type")
    if not isinstance(raw_type, str) or not raw_type.strip():
        raise CompatError("TS_FEATURES_UNAVAILABLE", {"have_type": bool(raw_type)})
    t_can = _canon_type(raw_type)
    strat = type_to_strategy(t_can)  # may raise CompatError for unknown types
    return {"type": t_can, "strategy": strat}

def compute_features(a_ts: dict, b_ts: dict) -> dict[str, bool]:
    sacral = {"Generator", "Manifesting Generator"}
    a_type, b_type = a_ts["type"], b_ts["type"]
    a_strat, b_strat = a_ts["strategy"], b_ts["strategy"]
    return {
        "strategy_match": (a_strat == b_strat),
        # REDLINE: True only when BOTH are sacral
        "sacral_pair": (a_type in sacral) and (b_type in sacral),
        "projector_to_generator": (
            (a_type == "Projector" and b_type in sacral) or
            (b_type == "Projector" and a_type in sacral)
        ),
    }

def band_v0(features: dict[str, bool]) -> str:
    # A3 rule: Warm iff sacral_pair else Open
    return "Warm" if features.get("sacral_pair") else "Open"
