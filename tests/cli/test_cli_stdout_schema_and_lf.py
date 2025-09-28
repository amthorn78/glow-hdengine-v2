from __future__ import annotations
import subprocess, sys, json, hashlib, pathlib
from jsonschema import Draft7Validator

A = "tests/fixtures/reader_v1/abba_A.json"
B = "tests/fixtures/reader_v1/abba_B.json"
SCHEMA = pathlib.Path("schemas/reader.v1.schema.json")
SCHEMA_SHA = pathlib.Path("schemas/reader.v1.schema.json.sha256")

def _cli(a: str, b: str) -> bytes:
    p = subprocess.run([sys.executable, "scripts/hd_cli.py", a, b],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return p.stdout

def test_stdout_is_schema_valid_and_lf_and_schema_file_hash_is_pinned():
    # 1) Schema file hash pin (prevents silent drift)
    raw = SCHEMA.read_bytes()
    calc = hashlib.sha256(raw).hexdigest()
    exp = SCHEMA_SHA.read_text(encoding="utf-8").strip().split()[0]
    assert calc == exp, f"schema sha256 mismatch: calc={calc} exp={exp}"

    # 2) CLI stdout is LF-terminated and valid JSON against pinned schema
    out = _cli(A, B)
    assert out.endswith(b"\n"), "stdout must end with exactly one LF"
    obj = json.loads(out)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft7Validator(schema).validate(obj)
