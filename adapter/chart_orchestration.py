"""Adapter-owned chart orchestration entry (HDE-SEPA006.1).

Owns the chart path's operational concerns: the SAFE_MODE read for the log
field, both clocks, the correlation id, the pinned-list file reads (anchored to
the repository root, not the working directory), fixture-chart acquisition and
one keys-only log line per call. Validation and normalization are delegated to
the pure ``engine.charts.pure``. It registers no route and writes no file.
"""
from __future__ import annotations

import datetime as _dt
import json as _json
import logging
import os as _os
import re
import time as _time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from engine.charts.pure import normalize_chart, validate_birth_inputs
from engine.util.input_validators import ensure_cid

_LOG = logging.getLogger(__name__)
_ROOT = Path(__file__).resolve().parents[1]
_ISO_PATH = _ROOT / "artifacts/constants/iso_3166_1_alpha2.json"
_IANA_PATH = _ROOT / "artifacts/constants/iana_tz_list.json"
_DATE_SHAPE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TIME_SHAPE = re.compile(r"^\d{2}:\d{2}$")


def _load_list(path: Path) -> List[str]:
    data = _json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise RuntimeError(f"pinned list {path} invalid/empty")
    return data


def _birth_args(args: tuple) -> bool:
    return (
        len(args) >= 3
        and all(isinstance(a, str) for a in args[:3])
        and bool(_DATE_SHAPE.match(args[0]))
        and bool(_TIME_SHAPE.match(args[1]))
    )


def _fixture_chart() -> Dict[str, Any]:
    return {
        "gates": [1, 2, 3],
        "channels_short": [],
        "centers": [],
        "type": "",
        "authority": "",
        "profile": "",
        "meta": {"provider": "fixtures", "source": "default"},
    }


def _emit(line: str, sink: Optional[Callable[[str], Any]]) -> None:
    try:
        if sink is None:
            _LOG.info(line)
        else:
            sink(line)
    except Exception:
        # Logging must never break the call
        pass


def load_chart(*args, **kwargs) -> Dict[str, Any]:
    """
    load_chart(birthdate, birthtime, place, *, tz=None, correlation_id=None, log_sink=None) -> dict
    load_chart(*, birthdate, birthtime, place, tz=None, correlation_id=None, log_sink=None) -> dict

    Any other argument shape raises TypeError; the legacy ``load_chart(user_id)``
    signature is retired.
    """
    started = _time.perf_counter()
    safe_mode = str(_os.getenv("SAFE_MODE", "0")).strip() == "1"
    cid = ensure_cid(kwargs.get("correlation_id"))
    status = "error"
    try:
        if _birth_args(args):
            birth = args[:3]
        elif args and isinstance(args[0], str) and not _DATE_SHAPE.match(args[0]):
            raise TypeError("Invalid arguments to load_chart")
        elif {"birthdate", "birthtime", "place"} <= set(kwargs):
            birth = (kwargs["birthdate"], kwargs["birthtime"], kwargs["place"])
            if not _birth_args(birth):
                raise TypeError("Invalid arguments to load_chart")
        else:
            raise TypeError("Invalid arguments to load_chart")
        validate_birth_inputs(
            *birth,
            kwargs.get("tz"),
            iso_codes=frozenset(_load_list(_ISO_PATH)),
            iana_zones=frozenset(_load_list(_IANA_PATH)),
        )
        chart = normalize_chart(_fixture_chart())
        status = "ok"
        return chart
    finally:
        line = {
            "ts": _dt.datetime.now(_dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "route": "loader.load_chart",
            "provider": "fixtures",
            "source": "default",
            "status": status,
            "duration_ms": int(round((_time.perf_counter() - started) * 1000.0)),
            "safe_mode": safe_mode,
            "correlation_id": cid,
        }
        _emit(_json.dumps(line, separators=(",", ":"), ensure_ascii=False), kwargs.get("log_sink"))
