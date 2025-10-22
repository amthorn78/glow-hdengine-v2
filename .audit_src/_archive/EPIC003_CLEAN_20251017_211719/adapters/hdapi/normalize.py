
from __future__ import annotations
from typing import Dict, Any, Iterable, Tuple

# ----- Typed error for enum closure -----
class NormalizationEnumError(ValueError):
    """Raised when a vendor enum value is unknown/unsupported."""

# ----- Canon: centers (fixed order) -----
_CANON_CENTERS = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]

# Vendor → canon aliases for centers
_VENDOR_CENTER_ALIASES = {
    "head":"head", "crown":"head",
    "ajna":"ajna",
    "throat":"throat",
    "g":"g", "g center":"g", "identity":"g", "identity center":"g",
    "ego":"ego", "heart":"ego", "will":"ego", "heart/ego":"ego", "will center":"ego",
    "spleen":"spleen", "splenic":"spleen",
    "solar plexus":"solar_plexus", "emotional solar plexus":"solar_plexus", "emotional":"solar_plexus",
    "sacral":"sacral",
    "root":"root"
}

# ----- Canon + aliases for type/authority/definition -----
_CANON_TYPES = {"Manifestor","Generator","Manifesting Generator","Projector","Reflector"}
_TYPE_ALIASES = {
    "manifestor":"Manifestor",
    "generator":"Generator",
    "manifesting generator":"Manifesting Generator",
    "manifestinggenerator":"Manifesting Generator",
    "mg":"Manifesting Generator",
    "projector":"Projector",
    "reflector":"Reflector",
}

_CANON_AUTHORITIES = {
    "Emotional","Sacral","Splenic","Ego Manifested","Ego Projected","Self Projected","Environment","Lunar"
}
_AUTH_ALIASES = {
    "emotional":"Emotional", "emotional solar plexus":"Emotional",
    "sacral":"Sacral",
    "splenic":"Splenic", "spleen":"Splenic",
    "ego manifested":"Ego Manifested", "ego-manifested":"Ego Manifested",
    "ego projected":"Ego Projected", "ego-projected":"Ego Projected",
    "self projected":"Self Projected", "self-projected":"Self Projected",
    "environmental":"Environment", "no inner authority":"Environment", "none":"Environment", "mental":"Environment",
    "lunar":"Lunar"
}

_CANON_DEFINITIONS = {"Single","Split","Triple Split","Quadruple Split","None"}
_DEF_ALIASES = {
    "single":"Single",
    "split":"Split",
    "triple split":"Triple Split", "triple-split":"Triple Split", "triple":"Triple Split",
    "quadruple split":"Quadruple Split", "quad split":"Quadruple Split", "quad-split":"Quadruple Split", "quad":"Quadruple Split",
    "none":"None", "no definition":"None", "no-definition":"None"
}

def _norm_center_name(v: str) -> str | None:
    return _VENDOR_CENTER_ALIASES.get(v.strip().lower())

def _map_enum(value: str, aliases: dict[str,str], allowed: set[str], field: str) -> str:
    """Map vendor enum to canon or raise NormalizationEnumError."""
    if value is None or str(value).strip() == "":
        return ""  # allow empty when vendor omitted
    key = str(value).strip().lower()
    canon = aliases.get(key, str(value).strip())
    if canon not in allowed:
        raise NormalizationEnumError(f"{field}: unknown '{value}'")
    return canon

def _norm_gate_list(vendor_gates: Iterable[str]) -> list[str]:
    uniq = {str(int(g)).zfill(2) for g in vendor_gates if str(g).strip()}
    return sorted(uniq)

def _norm_channels_minfirst(ch_list: Iterable[str]) -> list[str]:
    out = set()
    for s in ch_list or []:
        if not s or "-" not in s:
            continue
        a, b = s.split("-", 1)
        try:
            x, y = int(a), int(b)
        except ValueError:
            continue
        lo, hi = sorted((x, y))
        out.add(f"{lo:02d}-{hi:02d}")
    return sorted(out)

def _centers_state(vendor_defined: Iterable[str]) -> list[dict]:
    defined = set()
    for name in vendor_defined or []:
        if not str(name).strip():
            continue
        nid = _norm_center_name(str(name))
        if not nid:
            raise NormalizationEnumError(f"centers: unknown '{name}'")
        defined.add(nid)
    return [{"id": cid, "state": ("defined" if cid in defined else "undefined")} for cid in _CANON_CENTERS]

def derive_channels_from_gates(gates_02: Iterable[str], canon_pairs: Iterable[Tuple[int,int]]) -> list[str]:
    have = {int(g) for g in gates_02}
    out = set()
    for a, b in canon_pairs or []:
        if a in have and b in have:
            lo, hi = sorted((a, b))
            out.add(f"{lo:02d}-{hi:02d}")
    return sorted(out)

def normalize(
    raw: Dict[str, Any],
    *,
    birth_date: str,
    birth_time: str,
    tzid: str,
    location_name: str,
    lat_str: str,
    lng_str: str,
    canon_channel_pairs: Iterable[Tuple[int,int]] | None = None,
) -> Dict[str, Any]:
    """
    Map vendor bodygraph JSON → Glow normalized schema (admin/private).
    Arrays sorted; channels %02d-%02d min-first. Enum fields closed via mapping.
    """
    gates_02 = _norm_gate_list(raw.get("gates", []))
    channels = _norm_channels_minfirst(raw.get("channels_short") or raw.get("channels", []))
    if (not channels) and canon_channel_pairs:
        channels = derive_channels_from_gates(gates_02, canon_channel_pairs)

    type_canon = _map_enum(raw.get("type",""), _TYPE_ALIASES, _CANON_TYPES, "type")
    auth_canon = _map_enum(raw.get("authority",""), _AUTH_ALIASES, _CANON_AUTHORITIES, "authority")
    def_canon  = _map_enum(raw.get("definition",""), _DEF_ALIASES, _CANON_DEFINITIONS, "definition")

    return {
        "schema": "chart.normalized.v1",
        "source": "hdapi",
        "birth": {"date": birth_date, "time": birth_time, "timezone": tzid},
        "location": {
            "name": location_name,
            "lat": f"{float(lat_str):.6f}",
            "lng": f"{float(lng_str):.6f}",
        },
        "mechanics": {
            "gates": gates_02,
            "channels": channels,
            "centers": _centers_state(raw.get("centers", [])),
        },
        "type": type_canon,
        "authority": auth_canon,
        "definition": def_canon,
    }
