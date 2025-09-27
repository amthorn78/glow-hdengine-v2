
from __future__ import annotations
from typing import Dict, Any, Iterable, Tuple

_CANON_CENTERS = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]

_VENDOR_CENTER_ALIASES = {
    "head":"head","crown":"head",
    "ajna":"ajna",
    "throat":"throat",
    "g":"g","g center":"g","identity":"g","identity center":"g",
    "ego":"ego","heart":"ego","will":"ego","heart/ego":"ego","will center":"ego",
    "spleen":"spleen","splenic":"spleen",
    "solar plexus":"solar_plexus","emotional solar plexus":"solar_plexus","emotional":"solar_plexus",
    "sacral":"sacral",
    "root":"root"
}

def _norm_center_name(v: str) -> str | None:
    return _VENDOR_CENTER_ALIASES.get(v.strip().lower())

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
        nid = _norm_center_name(name)
        if nid:
            defined.add(nid)
    return [{"id": cid, "state": ("defined" if cid in defined else "undefined")} for cid in _CANON_CENTERS]

def derive_channels_from_gates(gates_02: Iterable[str], canon_pairs: Iterable[Tuple[int,int]]) -> list[str]:
    """
    Given a set/list of %02d gate ids and a canon list of gate pairs (as ints),
    return sorted, deduped %02d-%02d channel ids, min-first.
    """
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
    Arrays sorted; channels %02d-%02d min-first.
    If vendor omits channels, we optionally derive from canon gate pairs.
    """
    gates_02 = _norm_gate_list(raw.get("gates", []))
    channels = _norm_channels_minfirst(raw.get("channels_short") or raw.get("channels", []))
    if (not channels) and canon_channel_pairs:
        channels = derive_channels_from_gates(gates_02, canon_channel_pairs)

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
        "type": raw.get("type", ""),
        "authority": raw.get("authority", ""),
        "definition": raw.get("definition", ""),
    }
