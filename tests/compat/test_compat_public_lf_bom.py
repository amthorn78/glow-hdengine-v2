"""Canonical LF-terminated, BOM-free bytes for the complete internal result."""
from __future__ import annotations

import pytest

from engine.bodygraph.resolver import ResolvedCompatChart
from engine.compat.compute import evaluate_pair, evaluation_party
from engine.stable.sercanon import serialize
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-lfbom-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-lfbom-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)


def test_public_bytes_lf_and_no_bom():
    left = evaluation_party(ResolvedCompatChart(UUID_A, complete_chart(UUID_A, GATES_A), "resolved", None, None, None, None))
    right = evaluation_party(ResolvedCompatChart(UUID_B, complete_chart(UUID_B, GATES_B), "resolved", None, None, None, None))
    out = serialize(evaluate_pair(left, right))
    assert out.endswith(b"\n")
    assert out.count(b"\n") == 1
    assert b"\r" not in out
    assert not out.startswith(b"\xef\xbb\xbf")
