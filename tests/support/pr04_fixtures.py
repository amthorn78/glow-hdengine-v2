"""Shared HDE-EPIC040-PR04 test support: complete mapped charts, the synthetic
complete-release bundle seam and the temporary narrative-pack mount.

Every positive PR04 test injects the synthetic complete release through
``engine.compat.compute._BUNDLE_PROVIDER`` and presets the narrative pack from a
temporary mount so no test writes into the repository tree.  Nothing here
relaxes admission or claims a live vendor result.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Mapping

from engine.bodygraph.mapped_cache import MappedBodyGraphRow
from engine.compat import compute
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root
from engine.narratives import state as narrative_state
from engine.narratives.loader import load_pack
from tests.config.helpers import synthetic_complete_release_root

ROOT = Path(__file__).resolve().parents[2]
CLOSED_RAILS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
}
UUID_A = "11111111-1111-4111-8111-111111111111"
UUID_B = "22222222-2222-4222-8222-222222222222"
UUID_C = "33333333-3333-4333-8333-333333333333"
# Letter-bearing UUID for spelling tests (digit-only UUID_A makes ``.upper()`` a no-op).
UUID_MIXED = "3fa85f64-5717-4562-b3fc-2c963f66afaa"
GATES_A = ["10", "20", "34", "43", "49", "5"]
GATES_B = ["12", "15", "22", "23", "4", "52", "63", "9"]
BIRTH_LEFT = {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"}
BIRTH_RIGHT = {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"}


def complete_chart(uid: str, gates=None, **overrides: Any) -> dict[str, Any]:
    """A complete source-bound mapped ChartResult projection with one identity."""

    bodygraph = {
        "authority": "Emotional",
        "birthDateUtc": "2000-01-01T00:00:00Z",
        "centers": ["Ajna", "Solar Plexus"],
        "channelsLong": ["10-20"],
        "channelsShort": ["34-20"],
        "definition": "Single",
        "gates": list(gates if gates is not None else GATES_A),
        "profile": "1/3",
        "strategy": "Wait to Respond",
        "type": "Manifesting Generator",
    }
    bodygraph.update(overrides)
    return {"bodygraph": bodygraph, "person": {"person_uid": uid}, "person_uid": uid}


def fixture_chart(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "fixtures/charts" / f"{name}.json").read_text(encoding="utf-8"))


def current_row(uid: str, chart: Mapping[str, Any] | None = None, *, vendor_version: int = 2, fingerprint: str | None = None) -> MappedBodyGraphRow:
    from engine.bodygraph.projection import project_bodygraph

    payload = project_bodygraph(chart if chart is not None else complete_chart(uid))
    return MappedBodyGraphRow(user_id=uid, vendor="hdapi", vendor_version=vendor_version, input_fingerprint=fingerprint or ("a" * 64), payload=payload)


def build_bundle(tmp_root: Path):
    """Admit the synthetic complete release from an isolated copy (never the repo)."""

    return _load_active_mechanics_bundle_from_root(synthetic_complete_release_root(tmp_root))


def build_pack(tmp_root: Path):
    return load_pack(ROOT / "catalog/narratives", tmp_root / "narratives")


def inject_seams(monkeypatch, bundle, pack) -> None:
    for key, value in CLOSED_RAILS.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", lambda: bundle)
    monkeypatch.setattr(narrative_state, "_PACK", pack)


class RowStore:
    """Read-only in-memory current-view rows keyed by canonical UUID."""

    def __init__(self, rows: Mapping[str, MappedBodyGraphRow] | None = None) -> None:
        self.rows = dict(rows or {})
        self.lookups: list[str] = []

    def __call__(self, key: str):
        self.lookups.append(key)
        return self.rows.get(key)


class FakeCurrentViewDB:
    """A ``DBAccess`` stand-in whose ``query`` serves the five current-view columns."""

    def __init__(self, charts: Mapping[str, Mapping[str, Any]] | None = None, *, fail=None) -> None:
        self.charts = {uid: copy.deepcopy(chart) for uid, chart in (charts or {}).items()}
        self.queries: list[tuple[str, tuple]] = []
        self.fail = fail
        self.writes: list[Any] = []

    def query(self, sql: str, params=None):
        self.queries.append((sql, tuple(params or ())))
        if self.fail is not None:
            raise self.fail
        uid = params[0]
        chart = self.charts.get(uid)
        if chart is None:
            return []
        return [(uid, "hdapi", 2, "a" * 64, json.dumps(chart, sort_keys=True))]

    def tx(self, statements, **kwargs):  # pragma: no cover - asserted never reached
        self.writes.append(statements)
        raise AssertionError("read-only surface attempted a write")

    exec = tx
