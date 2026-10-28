from __future__ import annotations

import json
import logging
from pathlib import Path
import re

import pytest

from adapter.chart_orchestration import load_chart
from adapter.no_io_guard import NoIoGuard
from engine.charts.pure import ChartInputError
from engine.serializer.canon import sercanon

ROOT = Path(__file__).resolve().parents[2]
CID = "CID-0123456789abcdef"
CID_RE = re.compile(r"^CID-[a-f0-9]{16}$")
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
BIRTH = ("1990-01-01", "12:34", "Amsterdam, NL")
TZ = "Europe/Amsterdam"
KEYS = ("ts", "route", "provider", "source", "status", "duration_ms", "safe_mode", "correlation_id")
FIXTURE_CHART = {
    "gates": [1, 2, 3], "channels_short": [], "centers": [], "type": "", "authority": "",
    "profile": "", "meta": {"provider": "fixtures", "source": "default"},
}
FIXTURE_CHART_BYTES = (
    b'{"authority":"","centers":[],"channels_short":[],"gates":[1,2,3],'
    b'"meta":{"provider":"fixtures","source":"default"},"profile":"","type":""}\n'
)


def _call(*args, **kwargs):
    lines: list[str] = []
    try:
        out = load_chart(*args, log_sink=lines.append, **kwargs)
    except Exception as e:
        out = e
    assert len(lines) == 1, lines
    return out, json.loads(lines[0]), lines[0]


def test_positional_and_keyword_forms_return_the_fixture_chart():
    out, line, _ = _call(*BIRTH, tz=TZ, correlation_id=CID)
    assert out == FIXTURE_CHART and list(out) == list(FIXTURE_CHART)
    assert sercanon(out) == FIXTURE_CHART_BYTES
    assert (line["status"], line["correlation_id"]) == ("ok", CID)
    # The compat-determinism generator's call form and inputs.
    for place in ("Austin, US", "New York, US"):
        out, line, _ = _call(birthdate="1990-05-04", birthtime="14:22", place=place, tz=TZ)
        assert sercanon(out) == FIXTURE_CHART_BYTES and line["status"] == "ok"


def test_each_chart_is_a_fresh_dict():
    first, _, _ = _call(*BIRTH, tz=TZ)
    first["gates"].append(99)
    first["meta"]["provider"] = "changed"
    assert _call(*BIRTH, tz=TZ)[0] == FIXTURE_CHART


@pytest.mark.parametrize(
    "args,field,message",
    [
        (("1990-02-30", "12:34", "Amsterdam, NL"), "date", "invalid date"),
        (("1990-01-01", "24:00", "Amsterdam, NL"), "time", "invalid time"),
        (("1990-01-01", "12:34", "Nowhere"), "place", "invalid place"),
    ],
)
def test_each_invalid_field_raises_the_typed_error_and_logs_one_error_line(args, field, message):
    err, line, _ = _call(*args, tz=TZ)
    assert isinstance(err, ChartInputError)
    assert (err.code, err.details, err.message) == ("READER_INVALID_INPUT", {"field": field}, message)
    assert line["status"] == "error"


def test_tz_absent_and_tz_invalid():
    for kwargs, message in (({}, "tz required on internal path"), ({"tz": "Europe/NotARealCity"}, "invalid tz")):
        for args, extra in ((BIRTH, {}), ((), dict(zip(("birthdate", "birthtime", "place"), BIRTH)))):
            err, line, _ = _call(*args, **extra, **kwargs)
            assert (err.code, err.details, err.message) == ("READER_INVALID_INPUT", {"field": "tz"}, message)
            assert line["status"] == "error"


def test_a_fourth_positional_argument_is_ignored():
    err, _, _ = _call(*BIRTH, TZ)
    assert (err.details, err.message) == ({"field": "tz"}, "tz required on internal path")


@pytest.mark.parametrize(
    "args,kwargs",
    [
        ((), {}),
        (("user-abc",), {"correlation_id": "CID-deadbeef"}),
        ((), {"birthdate": "user-abc", "birthtime": "12:34", "place": "Amsterdam, NL", "tz": TZ}),
        (("1990-01-01",), {}),
    ],
    ids=["no-arguments", "legacy-positional", "legacy-keyword", "date-only"],
)
def test_other_argument_shapes_raise_type_error_and_log_one_error_line(args, kwargs):
    err, line, _ = _call(*args, **kwargs)
    assert type(err) is TypeError and str(err) == "Invalid arguments to load_chart"
    assert line["status"] == "error"


@pytest.mark.parametrize("value,expected", [("1", True), ("0", False), (None, False)])
def test_safe_mode_field(monkeypatch, value, expected):
    if value is None:
        monkeypatch.delenv("SAFE_MODE", raising=False)
    else:
        monkeypatch.setenv("SAFE_MODE", value)
    assert _call(*BIRTH, tz=TZ)[1]["safe_mode"] is expected


def test_correlation_id_is_passed_through_or_synthesized():
    assert _call(*BIRTH, tz=TZ, correlation_id=CID)[1]["correlation_id"] == CID
    for kwargs in ({}, {"correlation_id": "CID-deadbeef"}):
        assert CID_RE.match(_call(*BIRTH, tz=TZ, **kwargs)[1]["correlation_id"])


def test_log_line_is_keys_only():
    _, line, raw = _call(*BIRTH, tz=TZ, correlation_id=CID)
    assert tuple(line) == KEYS
    assert (line["route"], line["provider"], line["source"]) == ("loader.load_chart", "fixtures", "default")
    assert type(line["duration_ms"]) is int and type(line["safe_mode"]) is bool
    # ts is the clock: pinned to its shape and left out of the substring check (at 12:34 UTC it holds "12:34").
    assert TS_RE.match(line["ts"])
    rest = raw.replace(line["ts"], "", 1)
    for forbidden in ("birthdate", "birthtime", "location", "place", "Amsterdam", "NL", "1990-01-01", "12:34", TZ):
        assert forbidden not in rest


def test_a_raising_sink_does_not_break_the_call():
    def sink(line):
        raise RuntimeError("sink down")
    assert load_chart(*BIRTH, tz=TZ, log_sink=sink) == FIXTURE_CHART
    with pytest.raises(ChartInputError):
        load_chart("1990-02-30", "12:34", "Amsterdam, NL", tz=TZ, log_sink=sink)


def test_default_sink_is_the_module_logger_and_writes_no_file(monkeypatch, tmp_path, caplog):
    monkeypatch.chdir(tmp_path)
    with caplog.at_level(logging.INFO, logger="adapter.chart_orchestration"):
        assert load_chart(*BIRTH, tz=TZ, correlation_id=CID) == FIXTURE_CHART
    records = [r for r in caplog.records if r.name == "adapter.chart_orchestration"]
    assert len(records) == 1 and json.loads(records[0].getMessage())["correlation_id"] == CID
    assert list(tmp_path.iterdir()) == []


def test_validation_does_not_depend_on_the_working_directory(monkeypatch, tmp_path):
    results = []
    for cwd in (ROOT, tmp_path):
        monkeypatch.chdir(cwd)
        results.append(_call(*BIRTH, tz=TZ)[0])
        results.append(_call("1990-01-01", "12:34", "Nowhere", tz=TZ)[0].details)
    assert results[0] == results[2] == FIXTURE_CHART
    assert results[1] == results[3] == {"field": "place"}
    assert list(tmp_path.iterdir()) == []


def test_no_socket_attempts():
    with NoIoGuard() as guard:
        _call(*BIRTH, tz=TZ)
        _call("1990-02-30", "12:34", "Amsterdam, NL", tz=TZ)
        _call()
    assert guard.attempts == 0
