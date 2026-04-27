from __future__ import annotations
import importlib
from engine.stable.sercanon import serialize
from engine.charts.loader import load_chart
from engine.compat.categories import CATEGORIES_ORDER_V1


VIEWER_TOP = CATEGORIES_ORDER_V1[0]
VIEWER_WEIGHTS = {cat: 10 for cat in CATEGORIES_ORDER_V1}

def test_public_bytes_lf_and_no_bom():
    mod = importlib.import_module("engine.compat.compute")
    # Use tz from pinned IANA list.
    ca = load_chart("1990-05-04","14:22","Austin, US", tz="Europe/Amsterdam")
    cb = load_chart("1992-07-19","08:05","New York, US", tz="Europe/Amsterdam")
    ca["person_uid"] = "lfbom_a"
    cb["person_uid"] = "lfbom_b"
    out = serialize(
        mod.compat_public(
            ca,
            cb,
            VIEWER_TOP,
            VIEWER_WEIGHTS,
            engine_tag="test-engine",
            release_id="test-release",
            invocation_tag="INV-TEST",
        )
    )
    assert out.endswith(b"\n")
    assert not out.startswith(b"\xef\xbb\xbf")
