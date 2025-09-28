from __future__ import annotations
import re, unicodedata
from datetime import datetime
from typing import Tuple, List
import json
from pathlib import Path
import secrets

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TIME_RE = re.compile(r"^[0-2]\d:[0-5]\d$")  # 00:00..23:59 guarded later

_ISO_PATH = Path("artifacts/constants/iso_3166_1_alpha2.json")
_IANA_PATH = Path("artifacts/constants/iana_tz_list.json")

def _load_list(path: Path) -> List[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise RuntimeError(f"pinned list {path} invalid/empty")
    return data

def parse_date_yyyy_mm_dd(s: str) -> datetime.date:
    if not isinstance(s, str) or not _DATE_RE.match(s):
        raise ValueError("date must be YYYY-MM-DD")
    try:
        dt = datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("date is not a real calendar date")
    return dt

def parse_time_hh_mm(s: str) -> Tuple[int, int]:
    if not isinstance(s, str) or not _TIME_RE.match(s):
        raise ValueError("time must be HH:MM (24h)")
    h, m = map(int, s.split(":"))
    if h > 23:
        raise ValueError("hour must be 00..23")
    return h, m

def parse_place_city_cc(s: str) -> Tuple[str, str]:
    if not isinstance(s, str):
        raise ValueError("place must be 'City, CC'")
    s = unicodedata.normalize("NFC", s).strip()
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError("place must be 'City, CC' with ISO-2 country code")
    city, cc = parts[0], parts[1].upper()
    iso = _load_list(_ISO_PATH)
    if cc not in iso:
        raise ValueError("country code must be ISO-3166-1 alpha-2")
    return city, cc

def parse_tz_iana(s: str) -> str:
    if not isinstance(s, str) or not s.strip():
        raise ValueError("tz must be a non-empty IANA tz name")
    ianas = _load_list(_IANA_PATH)
    if s not in ianas:
        raise ValueError("tz must be a valid IANA tz")
    return s

_CID_RE = re.compile(r"^CID-[a-f0-9]{16}$")
def ensure_cid(maybe: str | None) -> str:
    """
    Ensure a correlation id of the form CID-<16 lower-hex>.
    If `maybe` matches ^CID-[a-f0-9]{16}$, return it; else synthesize securely.
    """
    CID_RE = re.compile(r"^CID-[a-f0-9]{16}$")
    if isinstance(maybe, str) and CID_RE.match(maybe):
        return maybe
    # 8 bytes -> 16 lowercase hex
    import secrets as _secrets
    return "CID-" + _secrets.token_hex(8)
