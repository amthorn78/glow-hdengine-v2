from __future__ import annotations
import importlib
from engine.stable.sercanon import serialize

BANDS = {"Cool", "Open", "Warm", "Glow"}
VIEWER_TOP = "heat"
VIEWER_WEIGHTS = {
    "heat": 10,
    "harmony": 10,
    "communication": 10,
    "alignment": 10,
    "comfort": 10,
    "consistency": 10,
    "expansion": 10,
    "creativity": 10,
    "drive": 10,
    "balance": 10,
}

def _compat_public(a, b):
    mod = importlib.import_module("engine.compat.compute")
    return mod.compat_public(
        a,
        b,
        VIEWER_TOP,
        VIEWER_WEIGHTS,
        engine_tag="test-engine",
        release_id="test-release",
        invocation_tag="test-invocation",
    )

def _public_bytes(obj: dict) -> bytes:
    assert set(obj.keys()) == {"categories", "meta"}
    cats = obj["categories"]
    assert isinstance(cats, list) and cats
    for c in cats:
        assert set(c.keys()) >= {"id", "band", "score", "personal_key", "shared_key"}
        assert c["band"] in BANDS
    assert set(obj["meta"].keys()) == {"engine_tag", "release_id", "invocation_tag"}
    return serialize(obj)

def test_ab_ba_public_bytes_identical():
    left = {"person_uid": "alice"}
    right = {"person_uid": "bob"}

    pab = _compat_public(left, right)
    pba = _compat_public(right, left)

    bytes_ab = _public_bytes(pab)
    bytes_ba = _public_bytes(pba)

    assert bytes_ab == bytes_ba
    assert bytes_ab.endswith(b"\n")
    assert len(bytes_ab) == 0 or bytes_ab[-2:-1] != b"\n"
    assert not bytes_ab.startswith(b"\xef\xbb\xbf")
