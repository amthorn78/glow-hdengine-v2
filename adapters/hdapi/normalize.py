from __future__ import annotations
from typing import Dict, Any, Iterable

_CANON_CENTERS = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]

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

def _norm_center_name(v: str) -> str | None:
    key = v.strip().lower()
    return _VENDOR_CENTER_ALIASES.get(key)

def _norm_gate_list(vendor_gates: Iterable[str]) -> list[str]:
    uniq = {str(int(g)).zfill(2) for g in vendor_gates if str(g).strip()}
    return sorted(uniq)

def _norm_channels_minfirst(ch_list: Iterable[str]) -> list[str]:
    out = set()
    for s in ch_list or []:
        if not s or "-" not in s:
            continue
        a,b = s.split("-",1)
        try:
            x,y = int(a), int(b)
        except ValueError:
            continue
        lo,hi = sorted((x,y))
        out.add(f"{lo:02d}-{hi:02d}")
    return sorted(out)

def _centers_state(vendor_defined: Iterable[str]) -> list[dict]:
    defined_ids = set()
    for name in vendor_defined or []:
        nid = _norm_center_name(name)
        if nid:
            defined_ids.add(nid)
    out = []
    for cid in _CANON_CENTERS:
        out.append({"id": cid, "state": "defined" if cid in defined_ids else "undefined"})
    return out

def normalize(
    raw: Dict[str, Any],
    *,
    birth_date: str,
    birth_time: str,
    tzid: str,
    location_name: str,
    lat_str: str,
    lng_str: str,
) -> Dict[str, Any]:
    """
    Map vendor bodygraph JSON → Glow normalized schema (admin/private).
    All arrays sorted; %02d channels min-first.
    """
    return {
        "schema": "chart.normalized.v1",
        "source": "hdapi",
        "birth": {"date": birth_date, "time": birth_time, "timezone": tzid},
        "location": {"name": location_name, "lat": f"{float(lat_str):.6f}", "lng": f"{float(lng_str):.6f}"},
        "mechanics": {
            "gates": _norm_gate_list(raw.get("gates", [])),
            "channels": _norm_channels_minfirst(raw.get("channels_short") or raw.get("channels", [])),
            "centers": _centers_state(raw.get("centers", [])),
        },
        "type": raw.get("type", ""),
        "authority": raw.get("authority", ""),
        "definition": raw.get("definition", "")
    }
