import hashlib
import json
from pathlib import Path

import jsonschema
import pytest

from tools.evidence import update_evidence_index

CORE_ARTIFACTS = {
    "engine_core_purity_report": Path("artifacts/core/purity/purity_report.json"),
    "engine_core_two_run_logs": Path("artifacts/core/two_run/identity.json"),
    "engine_core_abba_logs": Path("artifacts/core/abba/ab_ba_parity.json"),
    "engine_core_json_compare_logs": Path("artifacts/core/json_compare/core_result_json_compare.json"),
}

CORE_SCHEMAS = {
    "engine_core_purity_report_schema": Path("docs/schemas/core/engine_core_purity_report.schema.json"),
    "engine_core_two_run_logs_schema": Path("docs/schemas/core/engine_core_two_run_logs.schema.json"),
    "engine_core_abba_logs_schema": Path("docs/schemas/core/engine_core_abba_logs.schema.json"),
    "engine_core_json_compare_logs_schema": Path("docs/schemas/core/engine_core_json_compare_logs.schema.json"),
}

ARTIFACT_SCHEMA_MAPPING = {
    "engine_core_purity_report": CORE_SCHEMAS["engine_core_purity_report_schema"],
    "engine_core_two_run_logs": CORE_SCHEMAS["engine_core_two_run_logs_schema"],
    "engine_core_abba_logs": CORE_SCHEMAS["engine_core_abba_logs_schema"],
    "engine_core_json_compare_logs": CORE_SCHEMAS["engine_core_json_compare_logs_schema"],
}


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _validate(instance: object, schema: dict) -> None:
    from tools.evidence.generate_engine_core_evidence import _schema_registry
    jsonschema.Draft202012Validator(schema, registry=_schema_registry()).validate(instance)


def test_engine_core_artifacts_registered_with_index_and_mirror():
    index_entries = _load_json(Path("docs/evidence/INDEX.json"))
    index_keys = {(entry["artifact_key"], entry["discovered_physical_path"]) for entry in index_entries}

    expected_entries = {**CORE_ARTIFACTS, **CORE_SCHEMAS}
    for key, path in expected_entries.items():
        tuple_key = (key, path.as_posix())
        assert tuple_key in index_keys, f"missing {tuple_key} in INDEX.json"

    mirror_path = Path("artifacts/evidence_index.jsonl")
    mirror_records = {
        (rec["artifact_key"], rec["discovered_physical_path"]): rec
        for rec in (json.loads(line) for line in mirror_path.read_text(encoding="utf-8").splitlines())
    }

    for key, path in expected_entries.items():
        tuple_key = (key, path.as_posix())
        assert tuple_key in mirror_records, f"missing mirror record for {tuple_key}"
        rec = mirror_records[tuple_key]
        proof_path = Path(rec["proof_anchor"])
        assert proof_path.exists(), f"missing path proof for {tuple_key}"
        proof = update_evidence_index._load_existing_proof(proof_path)
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        assert rec["sha256"] == sha
        assert proof.get("sha256") == sha
        assert int(proof.get("size_bytes")) == path.stat().st_size
        assert proof.get("path") == path.as_posix()


def test_engine_core_artifacts_match_schemas():
    for artifact_key, artifact_path in CORE_ARTIFACTS.items():
        schema_path = ARTIFACT_SCHEMA_MAPPING[artifact_key]
        schema = _load_json(schema_path)
        payload = _load_json(artifact_path)
        _validate(payload, schema)


def test_current_proofs_bind_actual_sources_and_behavior():
    from tools.evidence import generate_engine_core_evidence as writer
    for artifact in CORE_ARTIFACTS.values():
        payload = _load_json(artifact)
        assert payload["fixture_kind"] == "synthetic_complete_release_only"
        assert set(payload["source_sha256"]) == set(writer.SOURCE_PATHS)
        for name, digest in payload["source_sha256"].items():
            assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest
    two_run = _load_json(CORE_ARTIFACTS["engine_core_two_run_logs"])
    assert two_run["first_run"] == two_run["second_run"]
    assert [r["q"] for r in two_run["first_run"]["signals"]] == [25, 63, 0, 38, 40, 20, 0, 25, 50, 38, 50, 0, 0, 0, 50, 20, 0, 60, 0, 33]
    assert [r["score"] for r in two_run["first_run"]["categories"]] == [22, 10, 15, 6, 22, 13, 0, 18, 15, 8]
    abba = _load_json(CORE_ARTIFACTS["engine_core_abba_logs"])
    assert abba["ab_run"] == abba["ba_run"]
    assert all(abba[k] is True for k in ("complete_result_equal", "canonical_bytes_equal",
        "classification_equal", "normalized_owners_verified", "equal_masks_complete"))
    compare = _load_json(CORE_ARTIFACTS["engine_core_json_compare_logs"])
    raw = writer.sercanon(compare["core_result"])
    assert compare["canonical_sha256"] == compare["roundtrip_sha256"] == hashlib.sha256(raw).hexdigest()
    assert compare["size_bytes"] == len(raw)


def test_writer_repeated_proofs_preserve_bytes_and_mtimes(tmp_path, monkeypatch):
    from tools.evidence import generate_engine_core_evidence as writer
    payloads = writer._build_payloads()
    writer._validate_payloads(payloads)
    monkeypatch.setattr(writer, "ROOT", tmp_path)
    writer._write_payloads(payloads)
    paths = [tmp_path / p for p in writer.CORE_ARTIFACTS.values()]
    before = [(p.read_bytes(), p.stat().st_mtime_ns) for p in paths]
    for payload in payloads.values():
        payload["generated_at_utc"] = "2040-01-01T00:00:00Z"
    writer._write_payloads(payloads)
    assert before == [(p.read_bytes(), p.stat().st_mtime_ns) for p in paths]


@pytest.mark.parametrize("key,field,bad", [
    ("engine_core_two_run_logs", "identical", False),
    ("engine_core_abba_logs", "normalized_owners_verified", False),
    ("engine_core_json_compare_logs", "result_schema_valid", False),
    ("engine_core_purity_report", "behavioral_guard_exit_code", 1),
])
def test_evidence_schemas_refuse_unsupported_success(key, field, bad):
    payload = _load_json(CORE_ARTIFACTS[key])
    payload[field] = bad
    with pytest.raises(jsonschema.ValidationError):
        _validate(payload, _load_json(ARTIFACT_SCHEMA_MAPPING[key]))


def test_evidence_reuses_closed_owning_result_schema():
    key = "engine_core_two_run_logs"
    payload = _load_json(CORE_ARTIFACTS[key])
    payload["first_run"]["unexpected_field"] = 1
    with pytest.raises(jsonschema.ValidationError):
        _validate(payload, _load_json(ARTIFACT_SCHEMA_MAPPING[key]))


def test_writer_refuses_a_schema_valid_wrong_g004_before_publication(monkeypatch):
    import dataclasses
    from tools.evidence import generate_engine_core_evidence as writer
    original = writer.compute_core
    def wrong(*args):
        result = original(*args)
        categories = (dataclasses.replace(result.categories[0], score=23), *result.categories[1:])
        return dataclasses.replace(result, categories=categories)
    monkeypatch.setattr(writer, "compute_core", wrong)
    with pytest.raises(ValueError, match="fixed G004 oracle mismatch"):
        writer._build_payloads()
