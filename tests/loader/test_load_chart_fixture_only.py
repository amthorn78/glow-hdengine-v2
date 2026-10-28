
from __future__ import annotations
import pytest
from adapter.chart_orchestration import load_chart
from engine.charts.pure import ChartInputError

def test_fixture_path_requires_tz_and_returns_normalized_chart():
    lines: list[str] = []
    out = load_chart("1990-01-01","12:34","Amsterdam, NL", tz="Europe/Amsterdam", correlation_id="CID-deadbeefdeadbeef", log_sink=lines.append)
    assert isinstance(out, dict)
    assert "gates" in out and all(isinstance(g, int) for g in out["gates"])
    assert out.get("meta", {}).get("provider") == "fixtures"
    assert len(lines) == 1

def test_fixture_path_missing_tz_raises_typed():
    lines: list[str] = []
    with pytest.raises(ChartInputError) as ei:
        load_chart("1990-01-01","12:34","Amsterdam, NL", correlation_id="CID-deadbeefdeadbeef", log_sink=lines.append)
    err = ei.value
    assert getattr(err, "code", "") == "READER_INVALID_INPUT"
    assert getattr(err, "details", {}).get("field") == "tz"
    assert len(lines) == 1
