"""HDE-EPIC043 WU-PR-02 acceptance items 4 and 5: the ``magic10_result.v2`` value (HDE-CONJ010.3; AC-03).

* Every result validates against ``schemas/magic10_result_v2.schema.json`` with
  strict integer typing (a ``bool`` is not an integer), with ``signals`` and
  ``categories`` in the governed order.
* ``pair_key`` (HDE Math Spec §5.2.2 and its v2 identity statement) equals a
  digest this test builds itself from the preimage under ``config_id``
  ``m10-relevance-centers-type-v2.0.0`` and ``result_schema``
  ``magic10_result.v2``.
* The whole result is identical for (A, B) and (B, A) and across two runs, and
  the computation reads no file.
"""
from __future__ import annotations

import dataclasses
import hashlib
import inspect
import json
import sys
from pathlib import Path

import jsonschema
import pytest
from jsonschema import validators

from engine.magic10_v2.calculation import compute_category_components, compute_magic10_v2
from engine.magic10_v2.kernel import compute_kernel
from engine.magic10_v2.signals import compute_signals

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "schemas" / "magic10_result_v2.schema.json").read_bytes())
ORDER = json.loads((ROOT / "catalog" / "magic10.json").read_bytes())["order"]
RELEASE_ID = "1f" * 32
OTHER_RELEASE_ID = "2e" * 32
V2_CONFIG_ID = "m10-relevance-centers-type-v2.0.0"
E_HALF = (
    (1, 2, 4, 5, 6, 7, 8, 10, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 39, 40, 41,
     44, 45, 46, 49, 50, 51, 52, 54, 55, 58, 59, 61, 63, 64),
    (3, 7, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 22, 23, 29, 35, 36, 37, 40, 42, 43, 44, 47, 48, 51, 52, 53, 56,
     57, 58, 60, 61, 64),
)
W_HALF = (
    (2, 6, 9, 12, 13, 17, 18, 19, 22, 23, 27, 31, 34, 37, 42, 43, 47, 50, 52, 58, 59, 63),
    (3, 7, 13, 14, 17, 18, 21, 22, 23, 25, 26, 32, 33, 34, 35, 38, 42, 44, 47, 49, 54, 57, 60, 62, 63, 64),
)
PAIRS = (
    ((1,), (2,)),
    ((1, 8), (2,)),
    ((1, 8), (1, 8)),
    ((1,), (8,)),
    ((20, 34), (20, 34)),
    ((21,), (45,)),
    ((1, 8), (20, 34)),
    ((1, 8), (20, 34, 21, 45)),
    ((18, 26, 44, 58), (18, 26, 44, 58)),
    ((1, 8, 3, 60), (2, 14)),
    ((4, 17, 23, 24, 47), (43, 61, 62, 63, 64)),
    E_HALF,
    W_HALF,
)

_BASE = jsonschema.Draft202012Validator
_STRICT = validators.extend(
    _BASE, type_checker=_BASE.TYPE_CHECKER.redefine("integer", lambda checker, value: type(value) is int)
)


def _canonical(value: object) -> bytes:
    """This test's own canonical bytes: sorted keys, compact, UTF-8, one trailing newline."""
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def _fingerprint(mask: int) -> str:
    preimage = {"schema": "magic10_chart_fingerprint.v1", "gate_mask_hex": format(mask, "016x")}
    return hashlib.sha256(_canonical(preimage)).hexdigest()


def _expected_pair_key(mask_a: int, mask_b: int, config_id: str, release_id: str, result_schema: str) -> str:
    low, high = sorted((mask_a, mask_b))
    preimage = {
        "schema": "magic10_pair_preimage.v1",
        "members": [_fingerprint(low), _fingerprint(high)],
        "config_id": config_id,
        "release_id": release_id,
        "result_schema": result_schema,
    }
    return hashlib.sha256(_canonical(preimage)).hexdigest()


@pytest.mark.parametrize("gates_a, gates_b", PAIRS)
def test_result_validates_and_follows_the_governed_order(v2_bundle, mask_of, gates_a, gates_b) -> None:
    mask_a, mask_b = mask_of(*gates_a), mask_of(*gates_b)
    result = compute_magic10_v2(mask_a, mask_b, v2_bundle, RELEASE_ID)
    payload = result.as_payload()
    _STRICT.check_schema(SCHEMA)
    assert list(_STRICT(SCHEMA).iter_errors(payload)) == []
    assert list(payload) == ["schema", "config_id", "release_id", "pair_key", "signals", "categories"]
    assert (payload["schema"], payload["config_id"], payload["release_id"]) == (
        "magic10_result.v2", V2_CONFIG_ID, RELEASE_ID,
    )
    kernel = compute_kernel(mask_a, mask_b, v2_bundle)
    signals = compute_signals(kernel, v2_bundle)
    components = compute_category_components(kernel, signals, v2_bundle)
    assert result.signals == signals
    assert [row["signal_id"] for row in payload["signals"]] == [
        row["signal_id"] for row in v2_bundle.configuration["signals"]
    ]
    assert [row["category_id"] for row in payload["categories"]] == ORDER
    assert [(row["score"], row["band"]) for row in payload["categories"]] == [
        (item.score, item.band) for item in components
    ]


def test_pair_key_is_the_v2_identity(v2_bundle, mask_of) -> None:
    mask_a, mask_b = mask_of(1, 8), mask_of(2)
    result = compute_magic10_v2(mask_a, mask_b, v2_bundle, RELEASE_ID)
    assert result.pair_key == _expected_pair_key(mask_a, mask_b, V2_CONFIG_ID, RELEASE_ID, "magic10_result.v2")
    assert result.pair_key != _expected_pair_key(
        mask_a, mask_b, "m10-channel-state-v1.0.0", RELEASE_ID, "magic10_result.v1"
    )
    assert compute_magic10_v2(mask_b, mask_a, v2_bundle, RELEASE_ID).pair_key == result.pair_key
    other = compute_magic10_v2(mask_a, mask_b, v2_bundle, OTHER_RELEASE_ID)
    assert other.pair_key != result.pair_key
    assert (other.signals, other.categories) == (result.signals, result.categories)
    equal = mask_of(1, 8)
    assert compute_magic10_v2(equal, equal, v2_bundle, RELEASE_ID).pair_key == hashlib.sha256(_canonical({
        "schema": "magic10_pair_preimage.v1",
        "members": [_fingerprint(equal), _fingerprint(equal)],
        "config_id": V2_CONFIG_ID,
        "release_id": RELEASE_ID,
        "result_schema": "magic10_result.v2",
    })).hexdigest()


def _tuples_all_the_way_down(value) -> bool:
    if dataclasses.is_dataclass(value):
        return all(_tuples_all_the_way_down(getattr(value, field.name)) for field in dataclasses.fields(value))
    if isinstance(value, (list, dict, set)):
        return False
    if isinstance(value, tuple):
        return all(_tuples_all_the_way_down(item) for item in value)
    return True


@pytest.mark.parametrize("gates_a, gates_b", PAIRS)
def test_result_is_symmetric_deterministic_and_immutable(v2_bundle, mask_of, gates_a, gates_b) -> None:
    mask_a, mask_b = mask_of(*gates_a), mask_of(*gates_b)
    first = compute_magic10_v2(mask_a, mask_b, v2_bundle, RELEASE_ID)
    assert compute_magic10_v2(mask_b, mask_a, v2_bundle, RELEASE_ID) == first
    assert compute_magic10_v2(mask_a, mask_b, v2_bundle, RELEASE_ID) == first
    assert _tuples_all_the_way_down(first)
    with pytest.raises(dataclasses.FrozenInstanceError):
        first.pair_key = "0" * 64  # type: ignore[misc]
    assert first.as_payload() == first.as_payload()
    assert first.as_payload() is not first.as_payload()


_OPENED: list[str] = []
_RECORDING = [False]
_HOOK_INSTALLED = [False]


def _record_open(event: str, args: tuple) -> None:
    if _RECORDING[0] and event == "open":
        _OPENED.append(str(args[0]))


def test_calculation_reads_no_file_and_takes_exactly_four_inputs(v2_bundle, mask_of) -> None:
    if not _HOOK_INSTALLED[0]:
        sys.addaudithook(_record_open)
        _HOOK_INSTALLED[0] = True
    mask_a, mask_b = mask_of(1, 8, 20, 57, 32, 54), mask_of(3, 60, 21, 45, 47, 64)
    _OPENED.clear()
    _RECORDING[0] = True
    try:
        compute_magic10_v2(mask_a, mask_b, v2_bundle, RELEASE_ID)
    finally:
        _RECORDING[0] = False
    assert _OPENED == []
    assert list(inspect.signature(compute_magic10_v2).parameters) == ["mask_a", "mask_b", "bundle", "release_id"]
