import json, hashlib, pathlib, jsonschema

from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.compat.errors import error_envelope
from engine.presenter.emitter import emit_public

SCHEMA = json.loads(pathlib.Path("schemas/reader.v1.schema.json").read_text(encoding="utf-8"))
SCHEMA_V2 = json.loads(pathlib.Path("schemas/reader.v2.schema.json").read_text(encoding="utf-8"))
G = pathlib.Path("goldens/reader/v1")
G2 = pathlib.Path("goldens/reader/v2")
V1_FILES = {
    "g01_minimal_ineligible.json", "g02_ab_ba_parity_A.jsonl", "g02_ab_ba_parity_B.jsonl",
    "g03_harmony_open.json", "g04_harmony_warm.json", "g05_harmony_cool.json",
    "g06_error_invalid_input.json", "g07_harmony_glow.json",
}
V2_FILES = {
    "g01_ineligible.json", "g02_ab_ba_parity_A.jsonl", "g02_ab_ba_parity_B.jsonl",
    "g03_eligible_ten_in_order.json", "g04_error_invalid_version.json",
}

def _sha256(b: bytes) -> str: return hashlib.sha256(b).hexdigest()


def _check_json_goldens(root: pathlib.Path, schema, expected_names: set[str]):
    names = {p.name for p in root.iterdir() if not p.name.endswith(".sha256")}
    assert names == expected_names
    for name in expected_names:
        assert (root / (name + ".sha256")).is_file(), name
    for p in sorted(root.glob("*.json")):
        b = p.read_bytes()
        # LF termination, exactly one line
        assert b.endswith(b"\n") and b.count(b"\n") == 1
        # schema valid for success/error shapes
        doc = json.loads(b.decode("utf-8"))
        jsonschema.Draft202012Validator(schema).validate(doc)
        # sha256 matches sidecar (hash-only, LF-terminated)
        side = p.with_suffix(p.suffix + ".sha256")
        raw_side = side.read_text(encoding="utf-8")
        assert raw_side.endswith("\n") and raw_side.count("\n") == 1
        assert _sha256(b) == raw_side.strip()


def _check_jsonl_goldens(root: pathlib.Path, schema):
    for name in ("g02_ab_ba_parity_A.jsonl", "g02_ab_ba_parity_B.jsonl"):
        p = root / name
        b = p.read_bytes()
        # Should contain exactly two LF-terminated lines (two JSON objs)
        lines = b.splitlines(keepends=True)
        assert len(lines) == 2
        # Identity: AB bytes == BA bytes
        assert lines[0] == lines[1]
        doc = json.loads(lines[0])
        jsonschema.Draft202012Validator(schema).validate(doc)
        assert doc["eligible"] is True
        # Hash matches sidecar
        side = p.with_suffix(p.suffix + ".sha256")
        want = side.read_text(encoding="utf-8").strip()
        assert _sha256(b) == want
    assert (root / "g02_ab_ba_parity_A.jsonl").read_bytes() == (root / "g02_ab_ba_parity_B.jsonl").read_bytes()


# --- Reader v1 -----------------------------------------------------------------------------------

def test_json_goldens_schema_and_hashes_and_lf():
    _check_json_goldens(G, SCHEMA, V1_FILES)
    for p in G.iterdir():
        assert "_leader" not in p.name
        assert b"_leader" not in p.read_bytes()


def test_v1_goldens_are_the_harmony_covenant():
    for name, band in (("g03_harmony_open.json", "Open"), ("g04_harmony_warm.json", "Warm"), ("g05_harmony_cool.json", "Cool"), ("g07_harmony_glow.json", "Glow")):
        doc = json.loads((G / name).read_bytes())
        assert doc["reader_version"] == "v1" and doc["eligible"] is True
        assert doc["categories"] == [{"band": band, "id": "harmony"}]
    ineligible = json.loads((G / "g01_minimal_ineligible.json").read_bytes())
    assert ineligible["reader_version"] == "v1" and ineligible["eligible"] is False and ineligible["categories"] == []
    error = json.loads((G / "g06_error_invalid_input.json").read_bytes())
    assert error == {"code": "InvalidInput", "error": "bad gates", "ok": False}


def test_ab_ba_jsonl_identity_and_hashes():
    _check_jsonl_goldens(G, SCHEMA)
    doc = json.loads((G / "g02_ab_ba_parity_A.jsonl").read_bytes().splitlines()[0])
    assert doc["reader_version"] == "v1" and doc["categories"] == [{"band": "Warm", "id": "harmony"}]


# --- Reader v2 -----------------------------------------------------------------------------------

def test_v2_json_goldens_schema_and_hashes_and_lf():
    _check_json_goldens(G2, SCHEMA_V2, V2_FILES)


def test_v2_eligible_golden_is_the_ordered_ten_covering_every_band():
    doc = json.loads((G2 / "g03_eligible_ten_in_order.json").read_bytes())
    assert doc["reader_version"] == "v2" and doc["eligible"] is True
    assert [item["id"] for item in doc["categories"]] == list(FROZEN_MAGIC10_ORDER)
    assert {item["band"] for item in doc["categories"]} == {"Cool", "Open", "Warm", "Glow"}
    ineligible = json.loads((G2 / "g01_ineligible.json").read_bytes())
    assert ineligible["reader_version"] == "v2" and ineligible["eligible"] is False and ineligible["categories"] == []


def test_v2_error_golden_is_the_real_error_envelope_bytes():
    assert (G2 / "g04_error_invalid_version.json").read_bytes() == emit_public(error_envelope("ERR_READER_INVALID_VERSION"))


def test_v2_ab_ba_jsonl_identity_and_hashes():
    _check_jsonl_goldens(G2, SCHEMA_V2)
    doc = json.loads((G2 / "g02_ab_ba_parity_A.jsonl").read_bytes().splitlines()[0])
    assert doc["reader_version"] == "v2" and len(doc["categories"]) == 10
