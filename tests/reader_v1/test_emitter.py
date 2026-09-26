"""presenter/reader_v1/emitter: Reader v1 (harmony only, set semantics) and Reader v2
(ordered full Magic-10, PF10 §2.23) through the single canonical emitter."""
import hashlib
import json
import pathlib

import jsonschema
import pytest

from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.stable.sercanon import serialize
from presenter.reader_v1.emitter import emit_reader_v1, emit_reader_v2

SCHEMA_V1 = json.loads(pathlib.Path("schemas/reader.v1.schema.json").read_text(encoding="utf-8"))
SCHEMA_V2 = json.loads(pathlib.Path("schemas/reader.v2.schema.json").read_text(encoding="utf-8"))
BANDS = ("Cool", "Open", "Warm", "Glow")


def _hex64(ch: str) -> str:
    return ch * 64


def _enriched(categories, eligible=True):
    return {
        "eligible": eligible,
        "categories": categories,
        "meta": {"engine_tag": "Isis5", "invocation_tag": "INV-abc123"},
        "release_id": _hex64("a"),
    }


def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _ten(bands=None):
    bands = bands or [BANDS[i % 4] for i in range(10)]
    return [{"id": cid, "band": band} for cid, band in zip(FROZEN_MAGIC10_ORDER, bands)]


def _assert_envelope_contract(raw: bytes, env: dict, schema, version: str) -> None:
    assert raw.endswith(b"\n") and raw.count(b"\n") == 1
    decoded = json.loads(raw.decode("utf-8"))
    assert decoded == env
    assert list(decoded) == ["categories", "eligible", "idempotence_hash", "meta", "reader_version", "release_id"]
    assert decoded["reader_version"] == version
    pre = dict(decoded)
    pre.pop("idempotence_hash")
    assert decoded["idempotence_hash"] == _sha256(serialize(pre))
    jsonschema.Draft202012Validator(schema).validate(decoded)


# --- Reader v1 ------------------------------------------------------------------------------------

@pytest.mark.parametrize("band", BANDS)
def test_v1_harmony_item_two_run_identity_hash_lf_and_schema(band):
    cats = [{"id": "harmony", "band": band}]
    b1, env1 = emit_reader_v1(_enriched(cats))
    b2, env2 = emit_reader_v1(_enriched(list(cats)))
    assert b1 == b2 and env1 == env2
    assert env1["categories"] == [{"id": "harmony", "band": band}]
    _assert_envelope_contract(b1, env1, SCHEMA_V1, "v1")


def test_v1_ineligible_is_empty_categories():
    raw, env = emit_reader_v1(_enriched([], eligible=False))
    assert env["eligible"] is False and env["categories"] == []
    _assert_envelope_contract(raw, env, SCHEMA_V1, "v1")


def test_v1_set_semantics_sort_by_id():
    # v1 keeps set semantics: the same logical set in either order gives the same bytes.
    cat_a = [{"id": "heat", "band": "Cool"}, {"id": "harmony", "band": "Open"}]
    b1, _ = emit_reader_v1(_enriched(cat_a))
    b2, env = emit_reader_v1(_enriched(list(reversed(cat_a))))
    assert b1 == b2
    assert [item["id"] for item in env["categories"]] == ["harmony", "heat"]


def test_v1_duplicate_category_ids_fail():
    cats = [{"id": "harmony", "band": "Cool"}, {"id": "harmony", "band": "Cool"}]
    with pytest.raises(ValueError):
        emit_reader_v1(_enriched(cats))


@pytest.mark.parametrize(
    "item",
    [
        {"id": "harmony", "band": "Cool", "prompt": "x"},
        {"id": "harmony", "band": "Cool", "prompt": None},
        {"id": "harmony", "band": "Cool", "score": 1},
        {"id": "harmony"},
        {"band": "Cool"},
        {"id": "harmony", "band": "Hot"},
        {"id": "", "band": "Cool"},
        "harmony",
    ],
)
def test_v1_refuses_any_key_but_id_and_band(item):
    with pytest.raises(ValueError):
        emit_reader_v1(_enriched([item]))


# --- Reader v2 ------------------------------------------------------------------------------------

def test_v2_ten_in_order_bytes_hash_lf_and_schema():
    b1, env1 = emit_reader_v2(_enriched(_ten()))
    b2, env2 = emit_reader_v2(_enriched(_ten()))
    assert b1 == b2 and env1 == env2
    assert [item["id"] for item in env1["categories"]] == list(FROZEN_MAGIC10_ORDER)
    assert len(env1["categories"]) == 10
    _assert_envelope_contract(b1, env1, SCHEMA_V2, "v2")


def test_v2_preserves_the_canonical_order_and_never_sorts():
    raw, env = emit_reader_v2(_enriched(_ten()))
    ids = [item["id"] for item in json.loads(raw)["categories"]]
    assert ids == list(FROZEN_MAGIC10_ORDER)
    assert ids != sorted(ids)
    # Object keys are still canonical (sorted) inside every item; array order is the caller's.
    assert raw.startswith(b'{"categories":[{"band":"Cool","id":"harmony"},{"band":"Open","id":"heat"}')


def test_v2_ineligible_is_empty_categories():
    raw, env = emit_reader_v2(_enriched([], eligible=False))
    assert env["eligible"] is False and env["categories"] == []
    _assert_envelope_contract(raw, env, SCHEMA_V2, "v2")


@pytest.mark.parametrize(
    "categories",
    [
        list(reversed(_ten())),
        _ten()[:9],
        _ten() + [{"id": "balance", "band": "Cool"}],
        _ten()[:9] + [{"id": "harmony", "band": "Cool"}],
        [dict(item, prompt="x") if item["id"] == "harmony" else item for item in _ten()],
        [dict(item, band="Hot") if item["id"] == "heat" else item for item in _ten()],
        [dict(item, score=3) if item["id"] == "drive" else item for item in _ten()],
        [],
        [{"id": "harmony", "band": "Cool"}],
    ],
    ids=["wrong_order", "nine", "eleven", "duplicate", "prompt", "unknown_band", "score", "empty", "harmony_only"],
)
def test_v2_refuses_anything_but_the_ordered_ten(categories):
    with pytest.raises(ValueError):
        emit_reader_v2(_enriched(categories))


def test_v2_ineligible_with_items_is_refused():
    with pytest.raises(ValueError):
        emit_reader_v2(_enriched(_ten(), eligible=False))


def test_v2_and_v1_share_the_preimage_recipe():
    raw_v2, env_v2 = emit_reader_v2(_enriched(_ten()))
    raw_v1, env_v1 = emit_reader_v1(_enriched([{"id": "harmony", "band": "Cool"}]))
    for raw, env in ((raw_v2, env_v2), (raw_v1, env_v1)):
        pre = {k: v for k, v in env.items() if k != "idempotence_hash"}
        assert set(pre) == {"reader_version", "eligible", "categories", "meta", "release_id"}
        assert env["idempotence_hash"] == _sha256(serialize(pre))
    assert raw_v1 != raw_v2
