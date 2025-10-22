from __future__ import annotations

import datetime as _dt
import json as _json
import os as _os
import re
import time as _time
from pathlib import Path as _Path
from typing import Any, Dict, Optional

from engine.util.input_validators import (
    parse_date_yyyy_mm_dd,
    parse_time_hh_mm,
    parse_place_city_cc,
    parse_tz_iana,
    ensure_cid,
)

# Legacy provider resolve (kept for backward compatibility with old tests)
try:
    from engine.config.provider_loader import resolve_provider  # type: ignore
except Exception:  # pragma: no cover
    resolve_provider = None  # type: ignore


class LoaderInputError(Exception):
    def __init__(self, code: str, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


def _normalize_chart(obj: Dict[str, Any]) -> Dict[str, Any]:
    """Ensure gates are ints where possible; otherwise leave as-is."""
    out = dict(obj)
    gates = obj.get("gates", [])
    norm: list[int] = []
    for g in gates:
        if isinstance(g, int):
            norm.append(g)
        elif isinstance(g, str) and g.isdigit():
            norm.append(int(g))
    out["gates"] = norm
    return out


def _now_ts() -> str:
    return _dt.datetime.now(_dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _safe_mode_flag() -> bool:
    # "1" => True, anything else => False
    return str(_os.getenv("SAFE_MODE", "0")).strip() == "1"


def _log_call(*, provider: str, source: str, status: str, duration_ms: int, safe_mode: bool, correlation_id: str) -> None:
    """Keys-only JSONL; no payloads or PII."""
    line = {
        "ts": _now_ts(),
        "route": "loader.load_chart",
        "provider": provider,
        "source": source,
        "status": status,                 # "ok" | "error"
        "duration_ms": int(duration_ms),
        "safe_mode": bool(safe_mode),
        "correlation_id": correlation_id,
    }
    d = _Path("artifacts/logs")
    d.mkdir(parents=True, exist_ok=True)
    f = d / "loader_call.jsonl"
    with f.open("ab") as fh:
        fh.write(_json.dumps(line, separators=(",", ":"), ensure_ascii=False).encode("utf-8") + b"\n")


def _call_legacy(user_id: str, correlation_id: Optional[str]) -> Dict[str, Any]:
    """Support the previous loader interface: load_chart(user_id, *, correlation_id=...)."""
    if resolve_provider is None:
        return {"gates": [1, 2, 3]}
    provider = resolve_provider()
    res = provider.get_chart(user_id, correlation_id=correlation_id)  # type: ignore[attr-defined]
    return _normalize_chart(res)


def load_chart(*args, **kwargs) -> Dict[str, Any]:
    """
    Dual-signature loader:

      New (this card):
        load_chart(birthdate: str, birthtime: str, place: str, tz: str | None = None, *, correlation_id: str | None = None) -> dict

      Legacy (back-compat for earlier tests/cards):
        load_chart(user_id: str, *, correlation_id: str | None = None) -> dict
    """
    started = _time.perf_counter()
    safe_mode = _safe_mode_flag()
    cid = ensure_cid(kwargs.get("correlation_id"))
    provider_name = "fixtures"
    source = "default"
    status = "error"

    try:
        # --- New signature detection (positional 3 args matching date/time) ---
        if (
            len(args) >= 3
            and isinstance(args[0], str)
            and isinstance(args[1], str)
            and isinstance(args[2], str)
            and re.match(r"^\d{4}-\d{2}-\d{2}$", args[0])  # YYYY-MM-DD
            and re.match(r"^\d{2}:\d{2}$", args[1])        # HH:MM
        ):
            birthdate: str = args[0]
            birthtime: str = args[1]
            place: str = args[2]
            tz = kwargs.get("tz")

            # Validate inputs, map failures to typed LoaderInputError
            try:
                parse_date_yyyy_mm_dd(birthdate)
            except Exception as e:
                raise LoaderInputError("READER_INVALID_INPUT", "invalid date", {"field": "date"}) from e
            try:
                parse_time_hh_mm(birthtime)
            except Exception as e:
                raise LoaderInputError("READER_INVALID_INPUT", "invalid time", {"field": "time"}) from e
            try:
                parse_place_city_cc(place)
            except Exception as e:
                raise LoaderInputError("READER_INVALID_INPUT", "invalid place", {"field": "place"}) from e

            # For S2 internal/fixtures path we REQUIRE tz (hdapi path will IGNORE tz in S3)
            if tz is None:
                raise LoaderInputError("READER_INVALID_INPUT", "tz required on internal path", {"field": "tz"})
            try:
                parse_tz_iana(tz)
            except Exception as e:
                raise LoaderInputError("READER_INVALID_INPUT", "invalid tz", {"field": "tz"}) from e

            # Minimal normalized fixtures result (no network here)
            chart = {
                "gates": [1, 2, 3],
                "channels_short": [],
                "centers": [],
                "type": "",
                "authority": "",
                "profile": "",
                "meta": {"provider": "fixtures", "source": "default"},
            }
            status = "ok"
            return chart

        # --- Legacy signature path ---
        if len(args) >= 1 and isinstance(args[0], str) and not re.match(r"^\d{4}-\d{2}-\d{2}$", args[0]):
            user_id: str = args[0]
            provider_name = "legacy"
            res = _call_legacy(user_id, correlation_id=cid)
            status = "ok"
            return res

        # --- kwargs form of new signature (birthdate/birthtime/place passed as kwargs) ---
        if {"birthdate", "birthtime", "place"} <= set(kwargs.keys()):
            res = load_chart(kwargs["birthdate"], kwargs["birthtime"], kwargs["place"], tz=kwargs.get("tz"), correlation_id=cid)
            status = "ok"
            return res

        raise TypeError("Invalid arguments to load_chart")
    finally:
        duration_ms = int(round((_time.perf_counter() - started) * 1000.0))
        try:
            _log_call(provider=provider_name, source=source, status=status, duration_ms=duration_ms, safe_mode=safe_mode, correlation_id=cid)
        except Exception:
            # Logging must never break the call
            pass
