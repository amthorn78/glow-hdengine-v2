"""HDE-EPIC043 WU-PR-03: Reader v1 and v2 projections of v2 results (HDE-CONJ010.4; AC-04, AC-20).

Acceptance item 1 of the work unit: each projection matches its Reader schema
and stays numeric-free, shown two ways: no JSON number appears in the bytes,
and two results that share their bands but differ in ``q`` and ``score``
project to identical bytes.

The Reader goldens carry synthetic identity tags (``Isis5``, ``INV-000000``),
while the layer takes ``engine_tag`` and ``invocation_tag`` from
``identity_meta()``. So the v1 goldens are compared outside ``meta`` and
``idempotence_hash``, and the idempotence recipe is checked on the layer's own
bytes; the v2 golden's hand-set bands are not reached by a real pair, so v2 is
compared for shape. The bands depend on the conftest's labelled non-canon
fixture maxima; the masks are real pairs found with seed 20261117.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import jsonschema
import pytest
from jsonschema import validators

from engine.magic10_v2 import compat
from engine.presenter.emitter import emit_public
from engine.runtime.identity import identity_meta

ROOT = Path(__file__).resolve().parents[2]
RID = "2d5a4ec485fde5dd51004e0286fff1cb1211e4ee79fa71bc62b2a5ecd0b6c129"
HARMONY_PAIRS = {
    "Open": (0x7BF7EF3DFFE8F3BF, 0x7C5582D3B7EA6F37),
    "Warm": (0xB71FDFB09CE03C35, 0x9DACFBED5ACE5519),
    "Cool": (0xEE2167164A871497, 0x930ED610C95D1014),
}
V1_GOLDENS = {"Open": "g03_harmony_open", "Warm": "g04_harmony_warm", "Cool": "g05_harmony_cool"}
# Two real pairs with all ten bands equal and different q and score.
SAME_BANDS = ((0xBF53FDBFF5FF3E7F, 0xDCFCE7C21ECEEBED), (0xFD1BFF4DBF1D9EFC, 0x7EFB7B2AFEF65FF5))
SYNTHETIC_TAGS = {"engine_tag": "Isis5", "invocation_tag": "INV-000000"}


def _strict_validator(name: str):
    schema = json.loads(ROOT.joinpath("schemas", name).read_bytes())
    strict = jsonschema.Draft202012Validator.TYPE_CHECKER.redefine("integer", lambda checker, value: type(value) is int)
    return validators.extend(jsonschema.Draft202012Validator, type_checker=strict)(schema)


def _numbers(value: object) -> list[object]:
    if isinstance(value, bool):
        return []
    if isinstance(value, (int, float)):
        return [value]
    if isinstance(value, dict):
        return [number for item in value.values() for number in _numbers(item)]
    if isinstance(value, list):
        return [number for item in value for number in _numbers(item)]
    return []


@pytest.mark.parametrize("version", ["v1", "v2"])
@pytest.mark.parametrize("band", sorted(HARMONY_PAIRS))
def test_projection_matches_its_schema_and_is_numeric_free(v2_bundle, band, version) -> None:
    a, b = HARMONY_PAIRS[band]
    result = compat.evaluate_magic10_v2(a, b, v2_bundle, RID).result
    raw, envelope = compat.reader_projection_v2(result, version)
    decoded = json.loads(raw)
    _strict_validator(f"reader.{version}.schema.json").validate(decoded)
    assert decoded == envelope
    assert raw == emit_public(envelope)
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n")
    assert _numbers(decoded) == []
    if version == "v1":
        assert decoded["categories"] == [{"id": "harmony", "band": band}]
    else:
        assert decoded["categories"] == [{"id": item.category_id, "band": item.band} for item in result.categories]
    meta = identity_meta()
    assert decoded["meta"] == {"engine_tag": meta["engine_tag"], "invocation_tag": meta["invocation_tag"]}
    assert decoded["release_id"] == RID
    reversed_result = compat.evaluate_magic10_v2(b, a, v2_bundle, RID).result
    assert compat.reader_projection_v2(reversed_result, version)[0] == raw


@pytest.mark.parametrize("version", ["v1", "v2"])
def test_projection_depends_on_bands_alone(v2_bundle, version) -> None:
    first, second = (compat.evaluate_magic10_v2(a, b, v2_bundle, RID).result for a, b in SAME_BANDS)
    assert [item.band for item in first.categories] == [item.band for item in second.categories]
    assert [signal.q for signal in first.signals] != [signal.q for signal in second.signals]
    assert [item.score for item in first.categories] != [item.score for item in second.categories]
    assert compat.reader_projection_v2(first, version)[0] == compat.reader_projection_v2(second, version)[0]


def _without_identity(envelope: dict) -> dict:
    return {key: value for key, value in envelope.items() if key not in ("meta", "idempotence_hash")}


@pytest.mark.parametrize("band", sorted(V1_GOLDENS))
def test_v1_golden_matches_outside_the_identity_tags(v2_bundle, band) -> None:
    golden = json.loads(ROOT.joinpath("goldens", "reader", "v1", f"{V1_GOLDENS[band]}.json").read_bytes())
    assert golden["meta"] == SYNTHETIC_TAGS
    result = compat.evaluate_magic10_v2(*HARMONY_PAIRS[band], v2_bundle, golden["release_id"]).result
    _raw, envelope = compat.reader_projection_v2(result, "v1")
    assert set(envelope) == set(golden)
    assert _without_identity(envelope) == _without_identity(golden)
    preimage = {key: value for key, value in envelope.items() if key != "idempotence_hash"}
    assert envelope["idempotence_hash"] == hashlib.sha256(emit_public(preimage)).hexdigest()


def test_v2_golden_shape(v2_bundle) -> None:
    golden = json.loads(ROOT.joinpath("goldens", "reader", "v2", "g03_eligible_ten_in_order.json").read_bytes())
    result = compat.evaluate_magic10_v2(*HARMONY_PAIRS["Open"], v2_bundle, golden["release_id"]).result
    _raw, envelope = compat.reader_projection_v2(result, "v2")
    assert set(envelope) == set(golden)
    assert [item["id"] for item in envelope["categories"]] == [item["id"] for item in golden["categories"]]
    assert all(set(item) == {"id", "band"} for item in envelope["categories"])
