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


# Payloads that record the admitted release; the purity report carries no release_id.
RELEASE_ID_CARRIERS = (
    "engine_core_two_run_logs",
    "engine_core_abba_logs",
    "engine_core_json_compare_logs",
)


def _nested_release_ids(value: object) -> list[object]:
    found: list[object] = []
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "release_id":
                found.append(item)
            found.extend(_nested_release_ids(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(_nested_release_ids(item))
    return found


def _assert_payload_release_ids_are_admitted() -> None:
    from engine.runtime import identity

    admitted = identity.identity_meta()["release_id"]
    for key, artifact in CORE_ARTIFACTS.items():
        found = _nested_release_ids(_load_json(artifact))
        if key in RELEASE_ID_CARRIERS:
            assert found, f"{artifact} records no release_id"
        else:
            assert found == [], f"{artifact} unexpectedly records release_id"
        for value in found:
            assert value == admitted, f"{artifact} release_id drifted from the admitted release"


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _g004_expected() -> dict:
    """HDE-EPIC043 WU-PR-10 (D-21): the v2 M10-G004 values, the single source of the G004 pins."""
    goldens = _load_json(Path("tests/fixtures/magic10/v2/goldens.json"))
    return next(case for case in goldens["cases"] if case["case_id"] == "M10-G004")["expected"]


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
    # HDE-EPIC043 WU-PR-10 (D-7): the governed configuration and the cut maxima are bound inputs.
    assert {"catalog/magic10_mechanics_v2.json", "math/thresholds.json"} <= set(writer.SOURCE_PATHS)
    assert not any(path.startswith("tests/") for path in writer.SOURCE_PATHS)
    for artifact in CORE_ARTIFACTS.values():
        payload = _load_json(artifact)
        assert payload["fixture_kind"] == "synthetic_complete_release_only"
        assert set(payload["source_sha256"]) == set(writer.SOURCE_PATHS)
        for name, digest in payload["source_sha256"].items():
            assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest
    two_run = _load_json(CORE_ARTIFACTS["engine_core_two_run_logs"])
    assert two_run["first_run"] == two_run["second_run"]
    # D-21: the G004 pins are the v2 M10-G004 values, set at the cut maxima.
    expected = _g004_expected()
    assert [r["q"] for r in two_run["first_run"]["signals"]] == [r["q"] for r in expected["signals"]]
    assert [r["score"] for r in two_run["first_run"]["categories"]] == [r["score"] for r in expected["categories"]]
    assert [r["band"] for r in two_run["first_run"]["categories"]] == [r["band"] for r in expected["categories"]]
    assert two_run["fixed_g004_oracle_passed"] is True
    abba = _load_json(CORE_ARTIFACTS["engine_core_abba_logs"])
    assert abba["ab_run"] == abba["ba_run"]
    assert all(abba[k] is True for k in ("complete_result_equal", "canonical_bytes_equal",
        "classification_equal", "normalized_owners_verified", "equal_masks_complete"))
    compare = _load_json(CORE_ARTIFACTS["engine_core_json_compare_logs"])
    raw = writer.sercanon(compare["core_result"])
    assert compare["canonical_sha256"] == compare["roundtrip_sha256"] == hashlib.sha256(raw).hexdigest()
    assert compare["size_bytes"] == len(raw)


def _schema_refs(value: object) -> list[object]:
    if isinstance(value, dict):
        return [item for key, child in value.items() for item in ([child] if key == "$ref" else _schema_refs(child))]
    if isinstance(value, list):
        return [item for child in value for item in _schema_refs(child)]
    return []


def test_governed_schemas_bind_the_writer_inputs_and_the_v2_result():
    """HDE-EPIC043 WU-PR-10 (D-7): the four proof schemas moved with the writer."""
    from tools.evidence import generate_engine_core_evidence as writer
    for path in CORE_SCHEMAS.values():
        raw = path.read_bytes()
        schema = json.loads(raw)
        assert raw == (json.dumps(schema, indent=2) + "\n").encode("utf-8")
        source = schema["properties"]["source_sha256"]
        assert source["required"] == list(source["properties"]) == list(writer.SOURCE_PATHS)
        assert source["additionalProperties"] is False
        assert set(_schema_refs(schema)) <= {"schemas/magic10_result_v2.schema.json"}
    assert {path: len(_schema_refs(_load_json(path))) for path in CORE_SCHEMAS.values()} == {
        CORE_SCHEMAS["engine_core_purity_report_schema"]: 0, CORE_SCHEMAS["engine_core_two_run_logs_schema"]: 2,
        CORE_SCHEMAS["engine_core_abba_logs_schema"]: 3, CORE_SCHEMAS["engine_core_json_compare_logs_schema"]: 1}
    purity = _load_json(CORE_SCHEMAS["engine_core_purity_report_schema"])
    assert purity["properties"]["modules"]["items"]["properties"]["module"]["enum"] == list(writer.PURE_PATHS)
    two_run = _load_json(CORE_SCHEMAS["engine_core_two_run_logs_schema"])
    assert "fixed_g004_oracle_passed" in two_run["required"]
    assert two_run["properties"]["fixed_g004_oracle_passed"] == {"type": "boolean", "const": True}


def test_writer_refuses_a_schema_bound_to_another_source_list_before_publication(tmp_path, monkeypatch):
    from tools.evidence import generate_engine_core_evidence as writer
    key = "engine_core_two_run_logs_schema"
    schema = _load_json(CORE_SCHEMAS[key])
    schema["properties"]["source_sha256"]["required"] = schema["properties"]["source_sha256"]["required"][:-1]
    stale = tmp_path / "stale.schema.json"
    stale.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
    monkeypatch.setitem(writer.CORE_SCHEMAS, key, str(stale))
    monkeypatch.setattr(writer, "_write_payloads", lambda payloads: pytest.fail("proofs published"))
    with pytest.raises(ValueError, match=writer.SCHEMA_SOURCE_LIST_MISMATCH):
        writer.main(["--skip-index"])


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
    ("engine_core_two_run_logs", "fixed_g004_oracle_passed", False),
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


def test_evidence_refuses_a_v1_result_under_the_v2_binding():
    key = "engine_core_two_run_logs"
    payload = _load_json(CORE_ARTIFACTS[key])
    payload["first_run"]["schema"] = "magic10_result.v1"
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
    monkeypatch.setattr(writer, "_write_payloads", lambda payloads: pytest.fail("proofs published"))
    with pytest.raises(ValueError, match=writer.G004_ORACLE_MISMATCH):
        writer.main(["--skip-index"])


def test_writer_refuses_a_g004_golden_for_another_pair(tmp_path, monkeypatch):
    from tools.evidence import generate_engine_core_evidence as writer
    goldens = _load_json(Path(writer.GOLDENS_PATH))
    next(case for case in goldens["cases"] if case["case_id"] == "M10-G004")["inputs"]["gates_b"] = [9, 12, 15, 22, 23]
    other = tmp_path / "goldens.json"
    other.write_text(json.dumps(goldens), encoding="utf-8")
    monkeypatch.setattr(writer, "GOLDENS_PATH", str(other))
    with pytest.raises(ValueError, match=writer.G004_ORACLE_MISMATCH):
        writer._build_payloads()


def test_writer_refuses_a_synthetic_release_that_is_not_the_admitted_release(monkeypatch):
    from tests.config import helpers
    from tools.evidence import generate_engine_core_evidence as writer

    def other_release(tmp_path, *, source_root=None):
        root = helpers.synthetic_complete_release_root(tmp_path, source_root=source_root)
        member = root / "tools/bodygraph/check_magic10_gate_readiness.py"
        member.write_bytes(member.read_bytes() + b"# another release\n")
        helpers.write_synthetic_release_manifest(root)
        return root

    monkeypatch.setattr(writer, "synthetic_complete_release_root", other_release)
    monkeypatch.setattr(writer, "_write_payloads", lambda payloads: pytest.fail("proofs published"))
    with pytest.raises(ValueError, match=writer.RELEASE_MISMATCH):
        writer.main(["--skip-index"])


def test_core_evidence_binds_the_admitted_release_id():
    _assert_payload_release_ids_are_admitted()


def test_core_evidence_release_check_fails_when_the_admitted_release_id_differs(monkeypatch):
    from engine.runtime import identity

    real = identity.identity_meta()
    monkeypatch.setattr(identity, "identity_meta", lambda: {**real, "release_id": "0" * 64})
    with pytest.raises(AssertionError, match="drifted from the admitted release"):
        _assert_payload_release_ids_are_admitted()
