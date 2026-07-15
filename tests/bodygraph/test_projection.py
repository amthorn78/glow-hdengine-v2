from __future__ import annotations

import builtins
import copy
import json
from pathlib import Path

import pytest

from engine.bodygraph.projection import BodyGraphProjectionError, project_bodygraph
from engine.bodygraph.v2_adapter import adapt_v2_chart_payload


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests/fixtures/bodygraph/source_invariance"


def _load(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def _db_payload():
    return _load("db_cached_payload.v1.json")["payload"]


def test_projection_exact_shape_and_nonmutation():
    source = _db_payload()
    original = copy.deepcopy(source)
    projected = project_bodygraph(source)
    assert set(projected) == {"bodygraph", "person", "person_uid"}
    assert set(projected["bodygraph"]) == {
        "authority",
        "birthDateUtc",
        "centers",
        "channelsLong",
        "channelsShort",
        "definition",
        "gates",
        "profile",
        "strategy",
        "type",
    }
    assert set(projected["person"]) == {"person_uid"}
    assert source == original
    assert projected is not source
    assert projected["bodygraph"] is not source["bodygraph"]


@pytest.mark.parametrize(
    ("mutator", "code", "field"),
    [
        (lambda value: value.pop("person"), "MISSING_FIELD", "root.person"),
        (
            lambda value: value["bodygraph"].pop("authority"),
            "MISSING_FIELD",
            "root.bodygraph.authority",
        ),
        (
            lambda value: value.__setitem__("extra", True),
            "UNKNOWN_FIELD",
            "root.extra",
        ),
        (
            lambda value: value["bodygraph"].__setitem__("zeta", True),
            "UNKNOWN_FIELD",
            "root.bodygraph.zeta",
        ),
        (
            lambda value: value["bodygraph"].__setitem__("headers", {}),
            "UNSAFE_FIELD",
            "root.bodygraph.headers",
        ),
        (
            lambda value: value["bodygraph"].__setitem__("profile", float("nan")),
            "INVALID_SHAPE",
            "root.bodygraph.profile",
        ),
        (
            lambda value: value["person"].__setitem__("person_uid", "different"),
            "PERSON_UID_MISMATCH",
            "root.person_uid",
        ),
    ],
)
def test_projection_rejections_are_stable_and_value_free(mutator, code, field):
    payload = _db_payload()
    mutator(payload)
    with pytest.raises(BodyGraphProjectionError) as raised:
        project_bodygraph(payload)
    assert raised.value.code == code
    assert raised.value.field_path == field
    assert str(raised.value) == f"{code}:{field}"


def test_projection_integrates_vendor_adapter_and_db_fixture():
    vendor = _load("vendor_chart_result.v1.json")
    mapped = adapt_v2_chart_payload(vendor["payload"], vendor["context"])
    assert mapped.status == "mapped"
    assert mapped.resolved is not None
    assert project_bodygraph(mapped.resolved) == project_bodygraph(_db_payload())


def test_projection_performs_no_file_io(monkeypatch):
    payload = _db_payload()

    def forbidden(*_args, **_kwargs):
        raise AssertionError("projection attempted file I/O")

    monkeypatch.setattr(builtins, "open", forbidden)
    assert project_bodygraph(payload)["person_uid"].endswith("0038")

