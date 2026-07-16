from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError

from tools.evidence import generate_v2_mapped_cache_evidence as generator

ROOT = Path(__file__).resolve().parents[2]


def test_exact_primary_inventory_and_canonical_outputs() -> None:
    files = generator.build()
    relative = {path.relative_to(ROOT).as_posix() for path in files}
    expected = {f"artifacts/bodygraph/v2_mapped_cache/{name}" for name in generator.PRIMARY_NAMES} | {
        "schemas/bodygraph_v2_mapped_cache_transcript.v1.json", "schemas/bodygraph_v2_mapped_cache_manifest.v1.json"}
    assert relative == expected
    for path, data in files.items():
        assert data.endswith(b"\n") and not data.endswith(b"\n\n") and b"\r\n" not in data
        assert not path.name.endswith(".path_proof.txt")


def test_schema_validation_unknown_keys_and_manifest_bindings() -> None:
    files = generator.build()
    transcript_schema = json.loads(files[generator.TRANSCRIPT_SCHEMA])
    manifest_schema = json.loads(files[generator.MANIFEST_SCHEMA])
    write = json.loads(files[generator.OUT / "write_transcript.json"])
    manifest = json.loads(files[generator.OUT / "manifest.json"])
    Draft202012Validator(transcript_schema).validate(write)
    Draft202012Validator(manifest_schema).validate(manifest)
    bad = dict(write); bad["unknown"] = True
    with pytest.raises(ValidationError): Draft202012Validator(transcript_schema).validate(bad)
    bad = json.loads(files[generator.OUT / "write_transcript.json"]); bad["identity"]["unknown"] = True
    with pytest.raises(ValidationError): Draft202012Validator(transcript_schema).validate(bad)
    assert manifest["status"] == ("PASS" if all(manifest["predicates"].values()) else "FAIL")
    for binding in manifest["artifacts"] + manifest["schemas"]:
        data = files[ROOT / binding["path"]]
        import hashlib
        assert binding["sha256"] == hashlib.sha256(data).hexdigest() and binding["size"] == len(data)


def test_write_twice_and_check_are_fixed_point_and_nonwriting() -> None:
    subprocess.run([sys.executable, str(generator.__file__)], cwd=ROOT, check=True)
    paths = list(generator.build())
    first = {path:(path.read_bytes(),path.stat().st_mtime_ns) for path in paths}
    subprocess.run([sys.executable, str(generator.__file__)], cwd=ROOT, check=True)
    assert {path:path.read_bytes() for path in paths} == {path:value[0] for path,value in first.items()}
    before = {path:(path.read_bytes(),path.stat().st_mtime_ns) for path in paths}
    subprocess.run([sys.executable, str(generator.__file__), "--check"], cwd=ROOT, check=True)
    assert before == {path:(path.read_bytes(),path.stat().st_mtime_ns) for path in paths}


def test_negative_predicate_fails_before_writes() -> None:
    before = {path:path.read_bytes() for path in generator.build() if path.exists()}
    with pytest.raises(RuntimeError, match="PREDICATE_FAILURE"): generator.build(force_failure=True)
    assert before == {path:path.read_bytes() for path in before}


def test_outputs_are_bounded_and_secret_free() -> None:
    forbidden = (b"database_url",b"db_bridge_url",b"bearer ",b"birthdate",b"birthtime",b"ChartResult",b"StandardResponse",b"request_body",b"response_body")
    for data in generator.build().values():
        lowered=data.lower()
        assert all(item.lower() not in lowered for item in forbidden)
