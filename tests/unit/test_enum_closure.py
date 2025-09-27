
import pytest
from adapters.hdapi.normalize import normalize, NormalizationEnumError

def _base_raw(**kw):
    raw = {
        "gates": ["1","8"],
        "centers": ["Head","Ajna"],  # valid
        "channels_short": [],
        "type": kw.get("type","Generator"),
        "authority": kw.get("authority","Emotional"),
        "definition": kw.get("definition","Split"),
    }
    return raw

def test_enum_mapping_accepts_common_variants():
    raw = _base_raw(type="manifesting generator", authority="emotional solar plexus", definition="quad split")
    obj = normalize(raw,
        birth_date="2000-01-01", birth_time="12:00", tzid="Etc/UTC",
        location_name="Testville, TV", lat_str="0.0", lng_str="0.0",
        canon_channel_pairs=[(1,8)]
    )
    assert obj["type"] == "Manifesting Generator"
    assert obj["authority"] == "Emotional"
    assert obj["definition"] == "Quadruple Split"

def test_unknown_type_raises():
    raw = _base_raw(type="Time Lord")
    with pytest.raises(NormalizationEnumError):
        normalize(raw,
            birth_date="2000-01-01", birth_time="12:00", tzid="Etc/UTC",
            location_name="X", lat_str="0.0", lng_str="0.0"
        )

def test_unknown_center_raises():
    raw = _base_raw()
    raw["centers"] = ["Head", "Pineal"]
    with pytest.raises(NormalizationEnumError):
        normalize(raw,
            birth_date="2000-01-01", birth_time="12:00", tzid="Etc/UTC",
            location_name="X", lat_str="0.0", lng_str="0.0"
        )
