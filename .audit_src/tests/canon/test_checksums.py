import re, json, pathlib
from core.canon.validate import load_repo_canon
from core.canon.checksums import build_checksums, V2_KEYS

HEX64 = re.compile(r"^[0-9a-f]{64}$")
CID  = re.compile(r"^[0-9]{2}-[0-9]{2}$")

def test_checksums_v2_shape_and_patterns():
    canon = load_repo_canon(pathlib.Path("."))
    c = build_checksums(canon)

    # exact top-level keys
    assert tuple(sorted(c.keys())) == tuple(sorted(V2_KEYS))

    # adjacency sha & toggles sha look like hex-64
    assert HEX64.match(c["adjacency_sha"])
    assert HEX64.match(c["toggles_frozen_sha"])

    # channels_sorted are normalized, sorted, unique
    chans = c["channels_sorted"]
    assert all(CID.match(x) for x in chans)
    assert chans == sorted(chans)
    assert len(chans) == len(set(chans))

    # deg_vector length 64; all ints >= 0
    dv = c["deg_vector"]
    assert isinstance(dv, list) and len(dv) == 64
    assert all(isinstance(x, int) and x >= 0 for x in dv)

    # center order is canonical; counts sum to 64 (or 0 if centers absent)
    assert c["center_order"] == ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]
    counts = c["gate_counts_by_center"]
    total = sum(int(v) for v in counts.values())
    assert total in (0, 64)

    # distinguished includes degree_3_gates exactly as contract
    assert c["distinguished"].get("degree_3_gates") == [10,20,34,57]

    # domain_coverage has sets with sensible sizes
    dc = c["domain_coverage"]
    assert isinstance(dc, dict)
    assert len(dc.get("centers", [])) == 9
    assert isinstance(dc.get("channels", []), list)
    assert len(dc.get("gates", [])) == 64
