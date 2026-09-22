"""AB/BA byte identity of the complete internal result (HDE-EPIC040-PR04)."""
from __future__ import annotations

import pytest

from engine.bodygraph.resolver import ResolvedCompatChart
from engine.compat.compute import conjunction_public, evaluate_pair, evaluation_party
from engine.stable.sercanon import serialize
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams

BANDS = {"Cool", "Open", "Warm", "Glow"}
ROW_KEYS = {"category_id", "score", "band", "shared_key", "personal_lo_to_hi_key", "personal_hi_to_lo_key"}


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-abba-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-abba-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)


def _party(uid, gates):
    return evaluation_party(ResolvedCompatChart(uid, complete_chart(uid, gates), "resolved", None, None, None, None))


def _public_bytes(obj: dict) -> bytes:
    assert set(obj.keys()) == {"schema", "config_id", "release_id", "pair_key", "signals", "categories"}
    cats = obj["categories"]
    assert isinstance(cats, list) and len(cats) == 10
    for c in cats:
        assert set(c.keys()) == ROW_KEYS
        assert c["band"] in BANDS
    return serialize(obj)


def test_ab_ba_public_bytes_identical():
    left = _party(UUID_A, GATES_A)
    right = _party(UUID_B, GATES_B)

    bytes_ab = _public_bytes(evaluate_pair(left, right))
    bytes_ba = _public_bytes(evaluate_pair(right, left))

    assert bytes_ab == bytes_ba
    assert bytes_ab.endswith(b"\n")
    assert bytes_ab[-2:-1] != b"\n"
    assert not bytes_ab.startswith(b"\xef\xbb\xbf")


def test_conjunction_carrier_ab_ba_identical_and_normalized():
    left = _party(UUID_A, GATES_A)
    right = _party(UUID_B, GATES_B)
    ab = conjunction_public(left, right)
    ba = conjunction_public(right, left)
    assert serialize(ab) == serialize(ba)
    assert ab["conjunction"]["left"]["person_uid"] in {UUID_A, UUID_B}
    assert ab["conjunction"]["left"]["person_uid"] != ab["conjunction"]["right"]["person_uid"]
