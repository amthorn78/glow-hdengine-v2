
import json
from adapters.hdapi.normalize import normalize, derive_channels_from_gates

def test_derive_channels_from_gates_minfirst_sorted_unique():
    canon_pairs = [(1,8), (8,48), (2,14), (20,34)]
    gates = ["08", "48", "14", "02", "08", "01"]  # dupes, unsorted
    out = derive_channels_from_gates(gates, canon_pairs)
    assert out == ["01-08", "02-14", "08-48"]

def test_normalize_falls_back_to_derivation_when_vendor_channels_missing():
    raw = {
        "gates": ["1","8","48","14","2"],
        "centers": ["Head","Ajna"],  # simple center names
        # channels intentionally omitted
        "type": "Generator", "authority": "Emotional", "definition": "Split"
    }
    canon_pairs = [(1,8), (8,48), (2,14)]
    obj = normalize(
        raw,
        birth_date="2000-01-01",
        birth_time="12:00",
        tzid="Etc/UTC",
        location_name="Testville, TV",
        lat_str="0.0",
        lng_str="0.0",
        canon_channel_pairs=canon_pairs,
    )
    assert obj["mechanics"]["channels"] == ["01-08","02-14","08-48"]
    # centers are emitted in fixed canon order with defined/undefined states
    ids = [c["id"] for c in obj["mechanics"]["centers"]]
    assert ids == ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]
