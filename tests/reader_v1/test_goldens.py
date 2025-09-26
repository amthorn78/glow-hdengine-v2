import json, hashlib, pathlib, jsonschema

SCHEMA = json.loads(pathlib.Path("schemas/reader.v1.schema.json").read_text(encoding="utf-8"))
G = pathlib.Path("goldens/reader/v1")

def _sha256(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

def test_json_goldens_schema_and_hashes_and_lf():
    # All *.json except the jsonl files
    for p in sorted(G.glob("*.json")):
        if p.name.endswith(".jsonl"):  # safety, though glob excludes by suffix
            continue
        b = p.read_bytes()
        # LF termination
        assert b.endswith(b"\n")
        # schema valid for success/error shapes
        doc = json.loads(b.decode("utf-8"))
        jsonschema.validate(instance=doc, schema=SCHEMA)
        # sha256 matches sidecar
        side = p.with_suffix(p.suffix + ".sha256")
        want = side.read_text(encoding="utf-8").strip()
        assert _sha256(b) == want

def test_ab_ba_jsonl_identity_and_hashes():
    for name in ("g02_ab_ba_parity_A.jsonl","g02_ab_ba_parity_B.jsonl"):
        p = G / name
        b = p.read_bytes()
        # Should contain exactly two LF-terminated lines (two JSON objs)
        lines = b.splitlines(keepends=True)
        assert len(lines) == 2
        # Identity: AB bytes == BA bytes
        assert lines[0] == lines[1]
        # Hash matches sidecar
        side = p.with_suffix(p.suffix + ".sha256")
        want = side.read_text(encoding="utf-8").strip()
        assert _sha256(b) == want
