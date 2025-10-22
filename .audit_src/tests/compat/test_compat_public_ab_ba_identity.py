from __future__ import annotations
import importlib
from engine.stable.sercanon import serialize
from engine.charts.loader import load_chart

BANDS = {"Cool", "Open", "Warm", "Glow"}

def _compat_public(a, b):
    mod = importlib.import_module("engine.compat.compute")
    return mod.compat_public(a, b)

def _public_bytes(obj: dict) -> bytes:
    assert set(obj.keys()) >= {"band", "categories"}
    assert obj["band"] in BANDS
    cats = obj["categories"]
    assert isinstance(cats, list) and cats
    for c in cats:
        assert set(c.keys()) >= {"id", "band"}
        assert c["id"] == "harmony"
        assert c["band"] in BANDS
    return serialize(obj)

def test_ab_ba_public_bytes_identical():
    # Use a tz we pinned in S1 (Europe/Amsterdam) to satisfy validator.
    a = {"birthdate":"1990-05-04","birthtime":"14:22","place":"Austin, US","tz":"Europe/Amsterdam"}
    b = {"birthdate":"1992-07-19","birthtime":"08:05","place":"New York, US","tz":"Europe/Amsterdam"}
    ca = load_chart(**a)
    cb = load_chart(**b)

    pab = _compat_public(ca, cb)
    pba = _compat_public(cb, ca)

    bytes_ab = _public_bytes(pab)
    bytes_ba = _public_bytes(pba)

    assert bytes_ab == bytes_ba
    assert bytes_ab.endswith(b"\n")
    assert len(bytes_ab) == 0 or bytes_ab[-2:-1] != b"\n"
    assert not bytes_ab.startswith(b"\xef\xbb\xbf")
