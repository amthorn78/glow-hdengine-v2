from __future__ import annotations
import importlib
from engine.stable.sercanon import serialize
from engine.charts.loader import load_chart

def test_public_bytes_lf_and_no_bom():
    mod = importlib.import_module("engine.compat.compute")
    # Use tz from pinned IANA list.
    ca = load_chart("1990-05-04","14:22","Austin, US", tz="Europe/Amsterdam")
    cb = load_chart("1992-07-19","08:05","New York, US", tz="Europe/Amsterdam")
    out = serialize(mod.compat_public(ca, cb))
    assert out.endswith(b"\n")
    assert not out.startswith(b"\xef\xbb\xbf")
