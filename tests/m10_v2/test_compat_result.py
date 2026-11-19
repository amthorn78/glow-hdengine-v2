"""HDE-EPIC043 WU-PR-03: ``magic10_compat_result.v2`` conformance, bytes and cache key (HDE-CONJ010.4).

Acceptance item 1 of the work unit: the layer's compat v2 value validates
against ``schemas/magic10_compat_result_v2.schema.json`` with strict integers;
``q`` is shown at 0 and 1000 on real pairs (only the two Balance signals reach
1000; an ordinary signal saturates at 800 or 833); the canonical bytes are the
one producer both internal surfaces will print; and the cache key is the
loader's ``magic10:v2:<pair_key>``.

The bundle is the conftest's fixture bundle (labelled non-canon fixtures), so no
value here is a governed maxima or result. Expected ``q`` values are transcribed
from the instruction's S-1 measurement, never read back from the module.
"""
from __future__ import annotations

import copy
import json
import random

import pytest

from engine.bodygraph.gates import normalize_gates
from engine.config.magic10_v2_loader import magic10_v2_intrinsic_cache_key
from engine.config.registry_loader import SchemaValidationError
from engine.magic10_v2 import compat
from engine.narratives.router import route_keys
from engine.presenter.emitter import emit_public

# A well-formed explicit release_id, not any release's; the layer reads no active release.
RID = "0123456789abcdef" * 4
# All 64 Gates, paired with itself.
FULL = (1 << 64) - 1
# A real pair at which equilibrium_score reaches 1000 (seed 20261117 search).
E1000 = (0xDD21D71A78F26A4E, 0x2EF2B87542BFFFDC)
BALANCE_SIGNALS = ("equilibrium_score", "counterweight_ratio")
ORDINARY_CEILING = 833
FIELDS = {"schema", "config_id", "release_id", "pair_key", "signals", "categories"}


def _q(evaluation: compat.Magic10V2Evaluation) -> dict[str, int]:
    return {row["signal_id"]: row["q"] for row in evaluation.compat_payload()["signals"]}


def test_full_pair_reaches_q_1000_and_0(v2_bundle) -> None:
    q = _q(compat.evaluate_magic10_v2(FULL, FULL, v2_bundle, RID))
    assert q["counterweight_ratio"] == 1000
    assert q["equilibrium_score"] == 0
    assert q["rapport_delta"] == 800
    assert q["pattern_integrity"] == 833


def test_equilibrium_reaches_1000_on_a_real_pair(v2_bundle) -> None:
    assert _q(compat.evaluate_magic10_v2(*E1000, v2_bundle, RID))["equilibrium_score"] == 1000


def test_value_is_the_result_plus_the_router_keys(v2_bundle) -> None:
    evaluation = compat.evaluate_magic10_v2(*E1000, v2_bundle, RID)
    value, pure = evaluation.compat_payload(), evaluation.result.as_payload()
    assert set(value) == FIELDS
    assert value["schema"] == "magic10_compat_result.v2"
    assert (value["config_id"], value["release_id"], value["pair_key"]) == (pure["config_id"], RID, pure["pair_key"])
    assert value["signals"] == pure["signals"]
    assert [row["category_id"] for row in value["categories"]] == list(v2_bundle.registry.magic10_order)
    for row, expected in zip(value["categories"], pure["categories"], strict=True):
        assert (row["category_id"], row["score"], row["band"]) == (
            expected["category_id"], expected["score"], expected["band"]
        )
        lo_to_hi = route_keys(row["category_id"], row["band"], "a_to_b")
        hi_to_lo = route_keys(row["category_id"], row["band"], "b_to_a")
        assert row["shared_key"] == lo_to_hi["shared_key"] == hi_to_lo["shared_key"]
        assert row["personal_lo_to_hi_key"] == lo_to_hi["personal_key"]
        assert row["personal_hi_to_lo_key"] == hi_to_lo["personal_key"]
        assert all(isinstance(row[key], str) and row[key] for key in (
            "shared_key", "personal_lo_to_hi_key", "personal_hi_to_lo_key"
        ))


def test_bytes_are_canonical_symmetric_and_repeatable(v2_bundle) -> None:
    a, b = E1000
    first = compat.evaluate_magic10_v2(a, b, v2_bundle, RID)
    second = compat.evaluate_magic10_v2(a, b, v2_bundle, RID)
    reversed_pair = compat.evaluate_magic10_v2(b, a, v2_bundle, RID)
    assert first.compat_bytes == emit_public(first.compat_payload())
    assert first.compat_bytes.endswith(b"\n") and not first.compat_bytes.endswith(b"\n\n")
    assert json.loads(first.compat_bytes) == first.compat_payload()
    assert first.compat_bytes == second.compat_bytes == reversed_pair.compat_bytes
    assert first.cache_key == reversed_pair.cache_key


def test_random_real_pairs_validate_and_are_symmetric(v2_bundle) -> None:
    rng = random.Random(20261117)

    def mask() -> int:
        probability = rng.uniform(0.2, 0.8)
        return normalize_gates([gate for gate in range(1, 65) if rng.random() < probability] or [1]).mask

    for _ in range(300):
        a, b = mask(), mask()
        forward = compat.evaluate_magic10_v2(a, b, v2_bundle, RID)
        assert forward.compat_bytes == compat.evaluate_magic10_v2(b, a, v2_bundle, RID).compat_bytes
        for signal_id, q in _q(forward).items():
            if signal_id not in BALANCE_SIGNALS:
                assert q <= ORDINARY_CEILING, signal_id


def _full_value(v2_bundle) -> tuple[dict, str]:
    evaluation = compat.evaluate_magic10_v2(FULL, FULL, v2_bundle, RID)
    return evaluation.compat_payload(), evaluation.result.pair_key


@pytest.mark.parametrize("q", [-1, 1001, 1.0, 500.0, True])
def test_schema_refuses_q_outside_its_integer_domain(v2_bundle, q) -> None:
    value, pair_key = _full_value(v2_bundle)
    value["signals"][0]["q"] = q
    with pytest.raises(SchemaValidationError) as caught:
        compat.validate_compat_result_v2(value, v2_bundle, release_id=RID, pair_key=pair_key)
    assert caught.value.code == compat.RESULT_INVALID
    assert caught.value.details == {"check": "schema"}


@pytest.mark.parametrize("q", [0, 1000])
def test_schema_accepts_q_at_both_ends(v2_bundle, q) -> None:
    value, pair_key = _full_value(v2_bundle)
    value["signals"][0]["q"] = q
    compat.validate_compat_result_v2(value, v2_bundle, release_id=RID, pair_key=pair_key)


@pytest.mark.parametrize(
    ("field", "replacement", "check"),
    [("release_id", "b" * 64, "release_id"), ("config_id", "m10-other", "config_id"), ("pair_key", "c" * 64, "pair_key")],
)
def test_identity_mismatch_is_refused(v2_bundle, field, replacement, check) -> None:
    value, pair_key = _full_value(v2_bundle)
    value[field] = replacement
    with pytest.raises(SchemaValidationError) as caught:
        compat.validate_compat_result_v2(value, v2_bundle, release_id=RID, pair_key=pair_key)
    assert caught.value.code == compat.RESULT_INVALID
    assert caught.value.details == {"check": check}


@pytest.mark.parametrize(("field", "check"), [("categories", "category_order"), ("signals", "signal_order")])
def test_order_mismatch_is_refused(v2_bundle, field, check) -> None:
    value, pair_key = _full_value(v2_bundle)
    swapped = copy.deepcopy(value)
    swapped[field][0], swapped[field][1] = swapped[field][1], swapped[field][0]
    with pytest.raises(SchemaValidationError) as caught:
        compat.validate_compat_result_v2(swapped, v2_bundle, release_id=RID, pair_key=pair_key)
    assert caught.value.code == compat.RESULT_INVALID
    assert caught.value.details == {"check": check}


def _gates(mask: int) -> list[int]:
    return [gate for gate in range(1, 65) if mask >> (gate - 1) & 1]


def test_cache_key_is_the_loader_key_and_differs_from_v1(v2_bundle) -> None:
    from engine.compat.compute import INTRINSIC_CACHE_PREFIX, EvaluationParty, intrinsic_pair_key
    from engine.core.core import _chart_fingerprint

    a, b = E1000
    evaluation = compat.evaluate_magic10_v2(a, b, v2_bundle, RID)
    pair_key = evaluation.result.pair_key
    assert evaluation.cache_key == magic10_v2_intrinsic_cache_key(pair_key) == "magic10:v2:" + pair_key
    assert compat.intrinsic_cache_key_v2(evaluation.result) == evaluation.cache_key
    parties = []
    for person, mask in (("a", a), ("b", b)):
        gates = normalize_gates(_gates(mask))
        parties.append(EvaluationParty(person, {}, gates, _chart_fingerprint(gates)))
    v1_pair_key = intrinsic_pair_key(*parties, config_id="m10-channel-state-v1.0.0", release_id=RID)
    assert evaluation.cache_key != INTRINSIC_CACHE_PREFIX + v1_pair_key
    assert pair_key != v1_pair_key
    with pytest.raises(SchemaValidationError) as caught:
        magic10_v2_intrinsic_cache_key(pair_key.upper())
    assert caught.value.code == "M10V2_INVALID_PAIR_KEY"
