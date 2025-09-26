import os, sys, json, subprocess
from pathlib import Path

def _run_with_admin(a: Path, b: Path) -> tuple[bytes, dict]:
    side = Path(str(a) + "__admin.json")
    out = subprocess.check_output([sys.executable, "scripts/hd_cli.py", str(a), str(b), "--admin-out", str(side)])
    admin = json.loads(side.read_text(encoding="utf-8"))
    return out, admin

def _get_num(d: dict, key: str, default=0):
    if key in d and isinstance(d[key], (int, float)): return d[key]
    dbg = d.get("_admin_debug", {})
    if isinstance(dbg, dict) and key in dbg and isinstance(dbg[key], (int, float)): return dbg[key]
    return default

def _has_single_lf(b: bytes) -> bool:
    return b.endswith(b"\n") and not b[:-1].endswith(b"\n")

def test_throat_em_bonus_applies_only_when_emotional_paced(tmp_path: Path):
    A = Path("tests/fixtures/g08_paced_A.json")
    B = Path("tests/fixtures/g08_paced_B.json")

    os.environ["HD_EMOTIONAL_TIMING_HONORED"] = "1"
    out1, admin1 = _run_with_admin(A,B)
    assert _has_single_lf(out1)
    val_paced = int(_get_num(admin1, "throat_em_bonus", 0))
    assert 1 <= val_paced <= 2

    os.environ["HD_EMOTIONAL_TIMING_HONORED"] = "0"
    out2, admin2 = _run_with_admin(A,B)
    assert _has_single_lf(out2)
    val_not = int(_get_num(admin2, "throat_em_bonus", 0))
    assert val_not == 0

def test_adjacency_small_plus_one_cap_three(tmp_path: Path):
    A = Path("tests/fixtures/g05_adj_A.json")
    B = Path("tests/fixtures/g05_adj_B.json")
    os.environ["HD_EMOTIONAL_TIMING_HONORED"] = "1"
    _, admin = _run_with_admin(A,B)
    hits = int(_get_num(admin, "adjacency_hits", 0))
    bonus = int(_get_num(admin, "adjacency_bonus", 0))
    assert hits >= 0
    assert bonus == min(hits, 3)
