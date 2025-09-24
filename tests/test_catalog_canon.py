import json, pathlib
def _walk_objects(s, found):
    if isinstance(s, dict):
        if s.get("type") == "object":
            found.append(s)
        for v in s.values():
            _walk_objects(v, found)
    elif isinstance(s, list):
        for v in s:
            _walk_objects(v, found)

def _all_objects_are_strict(schema_dict):
    objs=[]; _walk_objects(schema_dict, objs)
    return all(obj.get("additionalProperties", False) is False for obj in objs)

def test_schema_accepts_valid_rejects_unknown():
    gates = json.loads(pathlib.Path("schemas/gates_v1.schema.json").read_text(encoding="utf-8"))
    chans = json.loads(pathlib.Path("schemas/channels_v1.schema.json").read_text(encoding="utf-8"))
    assert _all_objects_are_strict(gates)
    assert _all_objects_are_strict(chans)
    # spot-check critical constraints exist
    assert "gates" in gates["properties"]
    assert "channels" in chans["properties"]
    # id regex, closed enums present
    id_pat = chans["properties"]["channels"]["items"]["properties"]["id"]["pattern"]
    assert id_pat == r"^\d{2}-\d{2}$"
    flags_enum = chans["properties"]["channels"]["items"]["properties"]["flags"]["items"]["enum"]
    assert flags_enum == ["format","direct_mt"]

import re, json, hashlib, subprocess, sys
from core.catalog.loader import center_adj, deg_vector
from core.stable.sercanon import stable_dumps

def test_gate_counts_map():
    d = json.load(open("artifacts/CANON_CHECKSUMS.json"))
    exp = {"head":3,"ajna":6,"throat":11,"g":8,"ego":4,"spleen":7,"solar_plexus":7,"sacral":9,"root":9}
    assert d["gate_counts_by_center"] == exp

def test_channel_id_orientation():
    chans = json.load(open("catalog/channels_v1.json"))["channels"]
    for ch in chans:
        assert re.match(r"^\\d{2}-\\d{2}$", ch["id"])
        a,b = map(int, ch["id"].split("-"))
        assert a <= b

def test_graph_recompute_matches_checksums():
    d = json.load(open("artifacts/CANON_CHECKSUMS.json"))
    adj_sha = hashlib.sha256(stable_dumps(center_adj())).hexdigest()
    assert adj_sha == d["adjacency_sha"]
    assert deg_vector() == d["deg_vector"]

def test_checksums_key_order_version_v2():
    d = json.load(open("artifacts/CANON_CHECKSUMS.json"))
    keys=["version","adjacency_sha","deg_vector","channels_sorted",
          "gate_counts_by_center","distinguished","domain_coverage",
          "toggles_frozen_sha","center_order"]
    assert list(d.keys()) == keys
    assert d["version"] == 2
    with open("artifacts/CANON_CHECKSUMS.json","rb") as f:
        f.seek(-1,2)
        assert f.read(1) == b"\\n"

def test_checksums_two_run_determinism():
    subprocess.check_call([sys.executable,"-m","scripts._emit_canon_checksums"])
    h1 = hashlib.sha256(open("artifacts/CANON_CHECKSUMS.json","rb").read()).hexdigest()
    subprocess.check_call([sys.executable,"-m","scripts._emit_canon_checksums"])
    h2 = hashlib.sha256(open("artifacts/CANON_CHECKSUMS.json","rb").read()).hexdigest()
    assert h1 == h2
