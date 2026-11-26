"""HDE-EPIC043 WU-PR-04: the v2 proof family, identity and Reader items (HDE-DIST008.1).

Items F-08 (``pair_key`` under ``m10-relevance-centers-type-v2.0.0``, the
``magic10:v2:`` cache key, ``magic10_result.v2`` and ``magic10_compat_result.v2``
closure with ``q`` in ``0..1000``), F-20 (the numeric-free public Reader
projection) and the v2 part of F-24 (equal masks of two distinct people give one
identity-free v2 ``pair_key``).

Each item has a check function that raises ``AssertionError`` when its rule is
broken; the passing case runs it on the landed code and the refused mutation
patches one rule in-process. Expected identities are recomputed from HDE Math
Spec §5.2.2 and HDE Schemas and Artifacts §2.9, not read back from the module.
The bundle is the labelled non-canon fixture bundle; ``release_id`` is an
explicit synthetic digest. F-08's candidate case (HDE-EPIC043 WU-PR-13) runs over
the repository root admitted as the active release, with its own ``release_id``,
and proves the release-member closure of the two v2 result schemas.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import pytest

from engine.config.magic10_v2_loader import (
    MAGIC10_V2_COMPAT_RESULT_SCHEMA,
    MAGIC10_V2_CONFIG_ID,
    MAGIC10_V2_INTRINSIC_CACHE_PREFIX,
    MAGIC10_V2_RESULT_SCHEMA,
)
from engine.config.registry_loader import SchemaValidationError
from engine.magic10_v2 import calculation, compat
from engine.serializer.canon import sercanon

ROOT = Path(__file__).resolve().parents[2]
RELEASE_ID = "b" * 64
PAIRS = (((1,), (2,)), ((1, 8), (2, 14)), ((1, 8, 20, 57, 32, 54), (3, 60, 21, 45, 47, 64)), ((20, 34), (47, 64)))


def _fingerprint(mask: int) -> str:
    preimage = {"schema": "magic10_chart_fingerprint.v1", "gate_mask_hex": format(mask, "016x")}
    return hashlib.sha256(sercanon(preimage, sort_keys=True)).hexdigest()


def _expected_pair_key(mask_a: int, mask_b: int, release_id: str = RELEASE_ID) -> str:
    low, high = sorted((mask_a, mask_b))
    preimage = {
        "schema": "magic10_pair_preimage.v1",
        "members": [_fingerprint(low), _fingerprint(high)],
        "config_id": MAGIC10_V2_CONFIG_ID,
        "release_id": release_id,
        "result_schema": MAGIC10_V2_RESULT_SCHEMA,
    }
    return hashlib.sha256(sercanon(preimage, sort_keys=True)).hexdigest()


# --- F-08 -------------------------------------------------------------------------------------

def _check_f08(bundle, mask_of) -> None:
    assert MAGIC10_V2_CONFIG_ID == "m10-relevance-centers-type-v2.0.0"
    assert MAGIC10_V2_INTRINSIC_CACHE_PREFIX == "magic10:v2:"
    for gates_a, gates_b in PAIRS:
        mask_a, mask_b = mask_of(*gates_a), mask_of(*gates_b)
        evaluation = compat.evaluate_magic10_v2(mask_a, mask_b, bundle, RELEASE_ID)
        result = evaluation.result
        assert (result.schema, result.config_id, result.release_id) == (
            MAGIC10_V2_RESULT_SCHEMA, MAGIC10_V2_CONFIG_ID, RELEASE_ID,
        )
        assert result.pair_key == _expected_pair_key(mask_a, mask_b)
        assert compat.intrinsic_cache_key_v2(result) == "magic10:v2:" + result.pair_key == evaluation.cache_key
        value = json.loads(evaluation.compat_bytes)
        assert value["schema"] == MAGIC10_V2_COMPAT_RESULT_SCHEMA
        compat.validate_compat_result_v2(value, bundle, release_id=RELEASE_ID, pair_key=result.pair_key)
        assert all(type(row["q"]) is int and 0 <= row["q"] <= 1000 for row in value["signals"])
        for bad in (-1, 1001):
            broken = json.loads(evaluation.compat_bytes)
            broken["signals"][0]["q"] = bad
            try:
                compat.validate_compat_result_v2(broken, bundle, release_id=RELEASE_ID, pair_key=result.pair_key)
            except SchemaValidationError as exc:
                assert exc.code == compat.RESULT_INVALID
            else:
                raise AssertionError(f"q {bad} accepted")


def test_f08_identity_cache_key_and_schema_closure(v2_bundle, mask_of) -> None:
    _check_f08(v2_bundle, mask_of)


def test_f08_mutation_pair_key_without_config_id_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    original = calculation._pair_key
    monkeypatch.setattr(
        calculation, "_pair_key",
        lambda mask_lo, mask_hi, config_id, release_id, result_schema: original(mask_lo, mask_hi, "", release_id, result_schema),
    )
    with pytest.raises(AssertionError):
        _check_f08(v2_bundle, mask_of)


def test_f08_mutation_cache_key_prefix_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    monkeypatch.setattr(compat, "intrinsic_cache_key_v2", lambda result: "magic10:v1:" + result.pair_key)
    with pytest.raises(AssertionError):
        _check_f08(v2_bundle, mask_of)


SCHEMA_CLOSURE = ("schemas/magic10_compat_result_v2.schema.json", "schemas/magic10_result_v2.schema.json")


def _check_f08_admitted(admitted, mask_of) -> None:
    """pair_key, cache key, release and schema closure on the admitted release (the candidate)."""
    manifest = (ROOT / "catalog" / "manifest.json").read_bytes()
    release_id = hashlib.sha256(manifest).hexdigest()
    assert admitted.release_id == admitted.manifest_sha256 == release_id, "F-08 admitted release"
    rows = {row["path"]: row for row in json.loads(manifest)["files"]}
    for rel in SCHEMA_CLOSURE:
        assert rows[rel]["sha256"] == hashlib.sha256((ROOT / rel).read_bytes()).hexdigest(), f"F-08 admitted closure {rel}"
    bundle = admitted.magic10_v2
    for gates_a, gates_b in PAIRS:
        mask_a, mask_b = mask_of(*gates_a), mask_of(*gates_b)
        evaluation = compat.evaluate_magic10_v2(mask_a, mask_b, bundle, release_id)
        result = evaluation.result
        assert (result.schema, result.config_id, result.release_id) == (
            MAGIC10_V2_RESULT_SCHEMA, MAGIC10_V2_CONFIG_ID, release_id), "F-08 admitted identity"
        assert result.pair_key == _expected_pair_key(mask_a, mask_b, release_id), "F-08 admitted pair_key"
        assert compat.intrinsic_cache_key_v2(result) == "magic10:v2:" + result.pair_key == evaluation.cache_key, (
            "F-08 admitted cache key")
        value = json.loads(evaluation.compat_bytes)
        assert value["schema"] == MAGIC10_V2_COMPAT_RESULT_SCHEMA, "F-08 admitted compat schema"
        compat.validate_compat_result_v2(value, bundle, release_id=release_id, pair_key=result.pair_key)


def test_f08_identity_cache_key_and_schema_closure_on_the_admitted_release(v2_admitted, mask_of) -> None:
    _check_f08_admitted(v2_admitted, mask_of)


def test_f08_mutation_pair_key_without_the_release_is_refused(v2_admitted, mask_of, monkeypatch) -> None:
    original = calculation._pair_key
    monkeypatch.setattr(
        calculation, "_pair_key",
        lambda mask_lo, mask_hi, config_id, release_id, result_schema: original(mask_lo, mask_hi, config_id, "", result_schema),
    )
    with pytest.raises(AssertionError, match=r"^F-08 admitted pair_key"):
        _check_f08_admitted(v2_admitted, mask_of)


def test_f08_mutation_v1_cache_key_prefix_on_the_admitted_release_is_refused(v2_admitted, mask_of, monkeypatch) -> None:
    monkeypatch.setattr(compat, "intrinsic_cache_key_v2", lambda result: "magic10:v1:" + result.pair_key)
    with pytest.raises(AssertionError, match=r"^F-08 admitted cache key"):
        _check_f08_admitted(v2_admitted, mask_of)


# --- F-20 -------------------------------------------------------------------------------------

def _numbers(value) -> list:
    if isinstance(value, bool):
        return []
    if isinstance(value, (int, float)):
        return [value]
    if isinstance(value, dict):
        return [number for item in value.values() for number in _numbers(item)]
    if isinstance(value, list):
        return [number for item in value for number in _numbers(item)]
    return []


def _check_f20(bundle, mask_of) -> None:
    for (gates_a, gates_b), version in itertools.product(PAIRS, ("v1", "v2")):
        result = calculation.compute_magic10_v2(mask_of(*gates_a), mask_of(*gates_b), bundle, RELEASE_ID)
        raw, envelope = compat.reader_projection_v2(result, version)
        decoded = json.loads(raw)
        assert decoded == envelope
        assert _numbers(decoded) == [], (gates_a, gates_b, version)
        assert all(set(item) == {"id", "band"} for item in decoded["categories"])


def test_f20_reader_projection_is_numeric_free(v2_bundle, mask_of) -> None:
    _check_f20(v2_bundle, mask_of)


def test_f20_mutation_a_numeric_field_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    original = compat.reader_projection_v2

    def with_score(result, version):
        raw, envelope = original(result, version)
        envelope = {**envelope, "categories": [{**item, "score": 0} for item in envelope["categories"]]}
        return sercanon(envelope, sort_keys=True), envelope

    monkeypatch.setattr(compat, "reader_projection_v2", with_score)
    with pytest.raises(AssertionError):
        _check_f20(v2_bundle, mask_of)


# --- F-24, v2 part ----------------------------------------------------------------------------

def _check_f24_v2(bundle, mask_of) -> None:
    for gates in ((1, 8), (20, 34, 47, 64), (3, 60, 21, 45)):
        mask = mask_of(*gates)
        first = calculation.compute_magic10_v2(mask, mask, bundle, RELEASE_ID)
        second = calculation.compute_magic10_v2(mask, mask, bundle, RELEASE_ID)
        assert first.pair_key == second.pair_key == _expected_pair_key(mask, mask), gates
        assert first.as_payload() == second.as_payload()


def test_f24_equal_masks_give_one_identity_free_v2_pair_key(v2_bundle, mask_of) -> None:
    _check_f24_v2(v2_bundle, mask_of)


def test_f24_mutation_identity_in_the_v2_preimage_is_refused(v2_bundle, mask_of, monkeypatch) -> None:
    original = calculation._pair_key
    people = itertools.count()

    def with_person(mask_lo, mask_hi, config_id, release_id, result_schema):
        return original(mask_lo, mask_hi, f"{config_id}#{next(people)}", release_id, result_schema)

    monkeypatch.setattr(calculation, "_pair_key", with_person)
    with pytest.raises(AssertionError):
        _check_f24_v2(v2_bundle, mask_of)
