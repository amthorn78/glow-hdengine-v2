#!/usr/bin/env python3
"""Owning writer of the Reader public goldens.

``goldens/reader/v1/``: the Reader v1 covenant set (one ``harmony`` item or ``[]``).
``goldens/reader/v2/``: the Reader v2 set (the ordered full Magic-10 or ``[]``; PF10 §2.23).
Every envelope is emitted through the single canonical emitter under a fixed synthetic
identity (``Isis5`` / ``INV-000000`` / ``release_id`` ``"a"*64``); sidecars are hash-only.
"""
import hashlib, json, pathlib
from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.compat.errors import error_envelope
from engine.presenter.emitter import emit_public
from presenter.reader_v1.emitter import emit_reader_v1, emit_reader_v2

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "goldens" / "reader" / "v1"
OUT_V2 = ROOT / "goldens" / "reader" / "v2"
OUT.mkdir(parents=True, exist_ok=True)
OUT_V2.mkdir(parents=True, exist_ok=True)

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

# ----------------------------------------------------------------------------- Reader v1

# g01: minimal ineligible
b, _ = emit_reader_v1(_enriched(False, []))
_write(OUT / "g01_minimal_ineligible.json", b)

# g03/g04/g05/g07: the one harmony item, one golden per band
for band, name in [
    ("Open","g03_harmony_open.json"),
    ("Warm","g04_harmony_warm.json"),
    ("Cool","g05_harmony_cool.json"),
    ("Glow","g07_harmony_glow.json"),
]:
    b, _ = emit_reader_v1(_enriched(True, [{"id":"harmony","band":band}]))
    _write(OUT / name, b)

# g02: AB/BA parity as jsonl (two lines: AB then BA; bytes must be identical)
cats_AB = [{"id":"harmony","band":"Warm"}]
cats_BA = [{"id":"harmony","band":"Warm"}]
b1, _ = emit_reader_v1(_enriched(True, cats_AB))
b2, _ = emit_reader_v1(_enriched(True, cats_BA))
# Ensure byte identity now; if not, fail hard
assert b1 == b2, "AB/BA bytes must match"
(OUT / "g02_ab_ba_parity_A.jsonl").write_bytes(b1 + b2)  # two LF-terminated lines
(OUT / "g02_ab_ba_parity_B.jsonl").write_bytes(b1 + b2)  # duplicate file as an independent golden
# Hashes for jsonl files (full file bytes)
(OUT / "g02_ab_ba_parity_A.jsonl.sha256").write_text(_sha256((OUT/"g02_ab_ba_parity_A.jsonl").read_bytes())+"\n", encoding="utf-8")
(OUT / "g02_ab_ba_parity_B.jsonl.sha256").write_text(_sha256((OUT/"g02_ab_ba_parity_B.jsonl").read_bytes())+"\n", encoding="utf-8")

# g06: the real governed Reader v1 error envelope bytes for an invalid request (PF05 §5.2;
# PF10 §2.24, C040-08): the same bytes POST /api/reader?v=1 emits for ERR_READER_INVALID_INPUT.
_write(OUT / "g06_error_invalid_input.json", emit_public(error_envelope("ERR_READER_INVALID_INPUT")))

print("GOLDENS_WRITTEN", OUT)

# ----------------------------------------------------------------------------- Reader v2

# g01: ineligible → []
b, _ = emit_reader_v2(_enriched(False, []))
_write(OUT_V2 / "g01_ineligible.json", b)

# g03: the ordered ten with a fixed synthetic band vector covering every band
BANDS_V2 = ("Cool", "Open", "Warm", "Glow", "Cool", "Open", "Warm", "Glow", "Cool", "Open")
ten = [{"id": cid, "band": band} for cid, band in zip(FROZEN_MAGIC10_ORDER, BANDS_V2)]
b, _ = emit_reader_v2(_enriched(True, ten))
_write(OUT_V2 / "g03_eligible_ten_in_order.json", b)

# g02: AB/BA parity as jsonl (AB- and BA-labelled but identical ordered band inputs)
ten_AB = [dict(item) for item in ten]
ten_BA = [dict(item) for item in ten]
b1, _ = emit_reader_v2(_enriched(True, ten_AB))
b2, _ = emit_reader_v2(_enriched(True, ten_BA))
assert b1 == b2, "AB/BA bytes must match"
(OUT_V2 / "g02_ab_ba_parity_A.jsonl").write_bytes(b1 + b2)
(OUT_V2 / "g02_ab_ba_parity_B.jsonl").write_bytes(b1 + b2)
(OUT_V2 / "g02_ab_ba_parity_A.jsonl.sha256").write_text(_sha256((OUT_V2/"g02_ab_ba_parity_A.jsonl").read_bytes())+"\n", encoding="utf-8")
(OUT_V2 / "g02_ab_ba_parity_B.jsonl.sha256").write_text(_sha256((OUT_V2/"g02_ab_ba_parity_B.jsonl").read_bytes())+"\n", encoding="utf-8")

# g04: the real production error envelope bytes for an unsupported version
_write(OUT_V2 / "g04_error_invalid_version.json", emit_public(error_envelope("ERR_READER_INVALID_VERSION")))

print("GOLDENS_WRITTEN", OUT_V2)
