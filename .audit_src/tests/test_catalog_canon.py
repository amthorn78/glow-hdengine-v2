import re, json, hashlib, subprocess, sys, os
from core.catalog.loader import center_adj, deg_vector
from core.stable.sercanon import stable_dumps

def _emit():
    cp = subprocess.run([sys.executable, "-m", "scripts._emit_canon_checksums"], capture_output=True, text=True)
    assert cp.returncode == 0, cp.stdout + cp.stderr

def test_gate_counts_map():
    d = json.load(open("artifacts/CANON_CHECKSUMS.json"))
    exp = {"head":3,"ajna":6,"throat":11,"g":8,"ego":4,"spleen":7,"solar_plexus":7,"sacral":9,"root":9}
    assert d["gate_counts_by_center"] == exp

def test_channel_id_orientation():
    chans = json.load(open("catalog/channels_v1.json"))["channels"]
    for ch in chans:
        assert re.match(r"^\d{2}-\d{2}$", ch["id"]), ch["id"]
        a,b = map(int, ch["id"].split("-"))
        assert a <= b, ch["id"]

def test_graph_recompute_matches_checksums():
    d = json.load(open("artifacts/CANON_CHECKSUMS.json"))
    adj_sha = hashlib.sha256(stable_dumps(center_adj())).hexdigest()
    assert adj_sha == d["adjacency_sha"]
    assert deg_vector() == d["deg_vector"]

def test_checksums_key_order_version_v2():
    d = json.load(open("artifacts/CANON_CHECKSUMS.json"))
    keys = ["version","adjacency_sha","deg_vector","channels_sorted",
            "gate_counts_by_center","distinguished","domain_coverage",
            "toggles_frozen_sha","center_order"]
    assert list(d.keys()) == keys
    assert d["version"] == 2
    with open("artifacts/CANON_CHECKSUMS.json", "rb") as f:
        f.seek(-1, os.SEEK_END)
        assert f.read(1) == b"\n"

def test_checksums_two_run_determinism():
    _emit()
    h1 = hashlib.sha256(open("artifacts/CANON_CHECKSUMS.json","rb").read()).hexdigest()
    _emit()
    h2 = hashlib.sha256(open("artifacts/CANON_CHECKSUMS.json","rb").read()).hexdigest()
    assert h1 == h2