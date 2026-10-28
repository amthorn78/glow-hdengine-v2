"""Pure chart validation and normalization (HDE-SEPA006.1).

Data in, data out: no time, randomness, environment, network, provider,
logging or filesystem access, at import or in any call. The pinned ISO-3166
and IANA lists arrive as arguments; ``adapter.chart_orchestration`` reads them.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any, Container, Dict, NamedTuple, Optional, Tuple

from engine.util.input_validators import parse_time_hh_mm

_MONTH_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


class ChartInputError(Exception):
    def __init__(self, code: str, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


class BirthInputs(NamedTuple):
    date: Tuple[int, int, int]
    time: Tuple[int, int]
    city: str
    country: str
    tz: str


def _invalid(field: str, message: str) -> ChartInputError:
    return ChartInputError("READER_INVALID_INPUT", message, {"field": field})


def _parse_date(s: Any) -> Tuple[int, int, int]:
    # Same acceptance as datetime.strptime(s, "%Y-%m-%d") behind its YYYY-MM-DD
    # shape check, without strptime's locale and TZ reads.
    if not isinstance(s, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        raise ValueError("date must be YYYY-MM-DD")
    year, month, day = int(s[0:4]), int(s[5:7]), int(s[8:10])
    if year < 1 or not 1 <= month <= 12:
        raise ValueError("date is not a real calendar date")
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if not 1 <= day <= _MONTH_DAYS[month - 1] + (1 if month == 2 and leap else 0):
        raise ValueError("date is not a real calendar date")
    return year, month, day


def validate_birth_inputs(
    birthdate: Any,
    birthtime: Any,
    place: Any,
    tz: Any,
    *,
    iso_codes: Container[str],
    iana_zones: Container[str],
) -> BirthInputs:
    """Validate in the loader's order: date, time, place, tz presence, tz value."""
    try:
        date = _parse_date(birthdate)
    except Exception as e:
        raise _invalid("date", "invalid date") from e
    try:
        hm = parse_time_hh_mm(birthtime)
    except Exception as e:
        raise _invalid("time", "invalid time") from e
    if not isinstance(place, str):
        raise _invalid("place", "invalid place")
    parts = [p.strip() for p in unicodedata.normalize("NFC", place).strip().split(",")]
    if len(parts) != 2 or not parts[0] or not parts[1] or parts[1].upper() not in iso_codes:
        raise _invalid("place", "invalid place")
    if tz is None:
        raise _invalid("tz", "tz required on internal path")
    if not isinstance(tz, str) or not tz.strip() or tz not in iana_zones:
        raise _invalid("tz", "invalid tz")
    return BirthInputs(date, hm, parts[0], parts[1].upper(), tz)


def normalize_chart(obj: Dict[str, Any]) -> Dict[str, Any]:
    """Keep integer gates, convert digit-string gates to int, drop the rest."""
    out = dict(obj)
    norm: list[int] = []
    for g in obj.get("gates", []):
        if isinstance(g, int):
            norm.append(g)
        elif isinstance(g, str) and g.isdigit():
            norm.append(int(g))
    out["gates"] = norm
    return out
