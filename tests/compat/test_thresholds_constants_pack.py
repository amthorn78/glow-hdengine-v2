from __future__ import annotations

from engine.compat.thresholds import BANDS, THRESHOLDS_V1
from engine.magic10.thresholds import BANDS as PACK_BANDS
from engine.magic10.thresholds import THRESHOLD_EDGES


def test_compat_thresholds_are_sourced_from_constants_pack_edges() -> None:
    assert THRESHOLDS_V1 == {
        "cool_max": THRESHOLD_EDGES[0],
        "open_max": THRESHOLD_EDGES[1],
        "warm_max": THRESHOLD_EDGES[2],
    }
    assert tuple(BANDS) == tuple(PACK_BANDS)
