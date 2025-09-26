#!/usr/bin/env python3
import hashlib, json, pathlib
from presenter.reader_v1.emitter import emit_reader_v1

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "goldens" / "reader" / "v1"
OUT.mkdir(parents=True, exist_ok=True)

def _hex64(ch: str) -> str: return ch * 64
def _sha256(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

def _write(path: pathlib.Path, b: bytes):
    path.write_bytes(b)
    (path.with_suffix(path.suffix + ".sha256")).write_text(_sha256(b) + "\n", encoding="utf-8")

def _enriched(eligible, cats):
    return {
        "eligible": eligible,
        "categories": cats,
        "meta": {"engine_tag":"Isis5","invocation_tag":"INV-000000"},
        "release_id": _hex64("a"),
    }

# g01: minimal ineligible
b, _ = emit_reader_v1(_enriched(False, []))
_write(OUT / "g01_minimal_ineligible.json", b)

# g03/g04/g05: one category each, prompt omitted
for cid, band, name in [
    ("open_leader","Open","g03_open_leader.json"),
    ("warm_leader","Warm","g04_warm_leader.json"),
    ("cool_leader","Cool","g05_cool_leader.json"),
]:
    b, _ = emit_reader_v1(_enriched(True, [{"id":cid,"band":band}]))
    _write(OUT / name, b)

# g02: AB/BA parity as jsonl (two lines: AB then BA; bytes must be identical)
cats_AB = [{"id":"cool_leader","band":"Cool"},{"id":"open_leader","band":"Open"}]
cats_BA = list(reversed(cats_AB))
b1, _ = emit_reader_v1(_enriched(True, cats_AB))
b2, _ = emit_reader_v1(_enriched(True, cats_BA))
# Ensure byte identity now; if not, fail hard
assert b1 == b2, "AB/BA bytes must match"
(OUT / "g02_ab_ba_parity_A.jsonl").write_bytes(b1 + b2)  # two LF-terminated lines
(OUT / "g02_ab_ba_parity_B.jsonl").write_bytes(b1 + b2)  # duplicate file as an independent golden
# Hashes for jsonl files (full file bytes)
(OUT / "g02_ab_ba_parity_A.jsonl.sha256").write_text(_sha256((OUT/"g02_ab_ba_parity_A.jsonl").read_bytes())+"\n", encoding="utf-8")
(OUT / "g02_ab_ba_parity_B.jsonl.sha256").write_text(_sha256((OUT/"g02_ab_ba_parity_B.jsonl").read_bytes())+"\n", encoding="utf-8")

# g06: error envelope (public error; not produced by emitter)
err = { "ok": False, "code": "InvalidInput", "error": "bad gates" }
b = (json.dumps(err, ensure_ascii=False, separators=(",",":"), sort_keys=True) + "\n").encode("utf-8")
_write(OUT / "g06_error_invalid_input.json", b)

print("GOLDENS_WRITTEN", OUT)
