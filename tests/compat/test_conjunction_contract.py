"""
Tests for the conjunction computation contract (HDE-EPIC026 PR-01).

Proves:
  1. Conjunction output is emittable through the canonical JSON emitter.
  2. Conjunction output is deterministic (same inputs → identical bytes).
  3. AB↔BA identity: compute_conjunction(a,b) and compute_conjunction(b,a)
     produce byte-identical canonical JSON (COMPOSITE_ABBA_IDENTITY_OK).
  4. Envelope shape matches the expected contract.
"""
from __future__ import annotations

import json

from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.conjunction import (
    build_conjunction_envelope,
    compute_conjunction,
)
from engine.presenter import emit_public


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_WEIGHTS = {cat: 10 for cat in CATEGORIES_ORDER_V1}
_TOP = CATEGORIES_ORDER_V1[0]

_PERSON_A = {"person_uid": "alice"}
_PERSON_B = {"person_uid": "bob"}


def _make_envelope(a=_PERSON_A, b=_PERSON_B):
    return build_conjunction_envelope(a, b, _TOP, _WEIGHTS)


# ---------------------------------------------------------------------------
# 1. Emittable through canonical JSON emitter
# ---------------------------------------------------------------------------

def test_conjunction_emits_valid_canonical_json():
    envelope = _make_envelope()
    canonical_bytes = emit_public(envelope)

    # Must be valid JSON
    parsed = json.loads(canonical_bytes)
    assert isinstance(parsed, dict)

    # Canonical format: UTF-8, single trailing LF, no BOM
    assert canonical_bytes.endswith(b"\n")
    assert not canonical_bytes[:-1].endswith(b"\n")
    assert not canonical_bytes.startswith(b"\xef\xbb\xbf")


# ---------------------------------------------------------------------------
# 2. Deterministic: same inputs → identical bytes
# ---------------------------------------------------------------------------

def test_conjunction_deterministic_bytes():
    bytes_1 = emit_public(_make_envelope())
    bytes_2 = emit_public(_make_envelope())
    assert bytes_1 == bytes_2


def test_conjunction_deterministic_repeated():
    """Five consecutive runs produce identical bytes."""
    runs = [emit_public(_make_envelope()) for _ in range(5)]
    assert all(r == runs[0] for r in runs)


# ---------------------------------------------------------------------------
# 3. AB↔BA identity (COMPOSITE_ABBA_IDENTITY_OK)
# ---------------------------------------------------------------------------

def test_conjunction_ab_ba_byte_identity():
    """compute_conjunction(a,b) and compute_conjunction(b,a) produce
    byte-identical canonical JSON."""
    result_ab = compute_conjunction(
        _PERSON_A, _PERSON_B, _TOP, _WEIGHTS,
    )
    result_ba = compute_conjunction(
        _PERSON_B, _PERSON_A, _TOP, _WEIGHTS,
    )

    bytes_ab = emit_public(result_ab)
    bytes_ba = emit_public(result_ba)
    assert bytes_ab == bytes_ba


def test_conjunction_envelope_ab_ba_byte_identity():
    """Full envelope path: build_conjunction_envelope(a,b) vs (b,a)."""
    env_ab = build_conjunction_envelope(_PERSON_A, _PERSON_B, _TOP, _WEIGHTS)
    env_ba = build_conjunction_envelope(_PERSON_B, _PERSON_A, _TOP, _WEIGHTS)

    bytes_ab = emit_public(env_ab)
    bytes_ba = emit_public(env_ba)
    assert bytes_ab == bytes_ba


def test_conjunction_ab_ba_with_different_uids():
    """AB↔BA with UIDs that reverse lexicographic order."""
    a = {"person_uid": "zara"}
    b = {"person_uid": "adam"}

    bytes_ab = emit_public(build_conjunction_envelope(a, b, _TOP, _WEIGHTS))
    bytes_ba = emit_public(build_conjunction_envelope(b, a, _TOP, _WEIGHTS))
    assert bytes_ab == bytes_ba


# ---------------------------------------------------------------------------
# 4. Envelope shape contract
# ---------------------------------------------------------------------------

def test_conjunction_envelope_shape():
    envelope = _make_envelope()
    assert envelope["kind"] == "conjunction"
    assert envelope["ok"] is True
    assert envelope["schema"] == "v1"

    result = envelope["result"]
    assert "categories" in result
    assert "meta" in result
    assert "pair_key" in result

    cats = result["categories"]
    assert isinstance(cats, list)
    assert len(cats) == len(CATEGORIES_ORDER_V1)

    for i, cat in enumerate(cats):
        assert cat["id"] == CATEGORIES_ORDER_V1[i]
        assert isinstance(cat["score"], int)
        assert 0 <= cat["score"] <= 100
        assert cat["band"] in {"Cool", "Open", "Warm", "Glow"}
        assert isinstance(cat["personal_key"], str)
        assert isinstance(cat["shared_key"], str)

    meta = result["meta"]
    assert "engine_tag" in meta
    assert "release_id" in meta
    assert "invocation_tag" in meta


def test_conjunction_pair_key_stable():
    """pair_key is the same regardless of argument order."""
    env_ab = _make_envelope(_PERSON_A, _PERSON_B)
    env_ba = _make_envelope(_PERSON_B, _PERSON_A)
    assert env_ab["result"]["pair_key"] == env_ba["result"]["pair_key"]


# ---------------------------------------------------------------------------
# 5. Canonical JSON sorted keys
# ---------------------------------------------------------------------------

def test_conjunction_canonical_keys_sorted():
    """Canonical JSON bytes have sorted keys at every level."""
    envelope = _make_envelope()
    canonical_bytes = emit_public(envelope)
    text = canonical_bytes.decode("utf-8").rstrip("\n")

    # Re-parse and re-serialize with sorted keys — must match
    parsed = json.loads(text)
    reserialized = json.dumps(parsed, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    assert text == reserialized
