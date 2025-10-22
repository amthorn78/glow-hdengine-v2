
from __future__ import annotations
import pytest
from engine.charts.loader import load_chart, LoaderInputError

def test_fixture_path_requires_tz_and_returns_normalized_chart():
    out = load_chart("1990-01-01","12:34","Amsterdam, NL", tz="Europe/Amsterdam", correlation_id="CID-deadbeefdeadbeef")
    assert isinstance(out, dict)
    assert "gates" in out and all(isinstance(g, int) for g in out["gates"])
    assert out.get("meta", {}).get("provider") in {"fixtures", "legacy", "internal_engine", "fixtures"}

def test_fixture_path_missing_tz_raises_typed():
    with pytest.raises(LoaderInputError) as ei:
        load_chart("1990-01-01","12:34","Amsterdam, NL", correlation_id="CID-deadbeefdeadbeef")
    err = ei.value
    assert getattr(err, "code", "") == "READER_INVALID_INPUT"
    assert getattr(err, "details", {}).get("field") == "tz"
