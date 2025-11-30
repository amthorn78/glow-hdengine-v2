from __future__ import annotations

import hashlib
import json
from pathlib import Path

try:
    import jsonschema
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    jsonschema = None

from tools.evidence import update_evidence_index

SAMPLER_ARTIFACTS = {
    "sampler_pool_snapshots": Path("artifacts/sampler/pool_snapshots/baseline.json"),
    "sampler_two_run_logs": Path("artifacts/sampler/two_run/identity.json"),
    "sampler_abba_logs": Path("artifacts/sampler/abba/ab_ba_parity.json"),
    "sampler_diversity_artifacts": Path("artifacts/sampler/diversity/diversity_requirements.json"),
    "sampler_seed_replay_logs": Path("artifacts/sampler/seed_replay/cli_http_seed_replay.json"),
}

SAMPLER_SCHEMAS = {
    "sampler_pool_snapshots_schema": Path("docs/schemas/sampler/pool_snapshots.schema.json"),
    "sampler_two_run_logs_schema": Path("docs/schemas/sampler/two_run_logs.schema.json"),
    "sampler_abba_logs_schema": Path("docs/schemas/sampler/abba_logs.schema.json"),
    "sampler_diversity_artifacts_schema": Path("docs/schemas/sampler/diversity_artifacts.schema.json"),
    "sampler_seed_replay_logs_schema": Path("docs/schemas/sampler/seed_replay_logs.schema.json"),
}

ARTIFACT_SCHEMA_MAPPING = {
    "sampler_pool_snapshots": SAMPLER_SCHEMAS["sampler_pool_snapshots_schema"],
    "sampler_two_run_logs": SAMPLER_SCHEMAS["sampler_two_run_logs_schema"],
    "sampler_abba_logs": SAMPLER_SCHEMAS["sampler_abba_logs_schema"],
    "sampler_diversity_artifacts": SAMPLER_SCHEMAS["sampler_diversity_artifacts_schema"],
    "sampler_seed_replay_logs": SAMPLER_SCHEMAS["sampler_seed_replay_logs_schema"],
}


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _validate(instance: object, schema: dict) -> None:
    if jsonschema is not None:
        jsonschema.validate(instance=instance, schema=schema)
        return

    def _resolved(subschema: dict) -> dict:
        ref = subschema.get("$ref")
        if not ref or not ref.startswith("#/definitions/"):
            return subschema
        key = ref.split("/")[-1]
        return schema.get("definitions", {}).get(key, subschema)

    def _walk(obj, sch: dict) -> None:
        resolved = _resolved(sch)
        if resolved.get("type") == "object":
            required = set(resolved.get("required", []))
            props = resolved.get("properties", {})
            assert set(obj.keys()).issuperset(required)
            if resolved.get("additionalProperties") is False:
                for key in obj:
                    assert key in props
            for key, sub in props.items():
                if key not in obj:
                    continue
                _walk(obj[key], sub)
            return

        if resolved.get("type") == "array":
            assert isinstance(obj, list)
            item_schema = resolved.get("items", {})
            for item in obj:
                _walk(item, item_schema)
            return

        expected_type = resolved.get("type")
        if expected_type == "string":
            assert isinstance(obj, str)
        elif expected_type == "boolean":
            assert isinstance(obj, bool)
        elif expected_type == "number":
            assert isinstance(obj, (int, float))
        elif expected_type == "integer":
            assert isinstance(obj, int)

    _walk(instance, schema)


def test_sampler_artifacts_registered_with_index_and_mirror():
    index_entries = _load_json(Path("docs/evidence/INDEX.json"))
    index_keys = {(entry["artifact_key"], entry["discovered_physical_path"]) for entry in index_entries}

    expected_entries = {**SAMPLER_ARTIFACTS, **SAMPLER_SCHEMAS}
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


def test_sampler_artifacts_match_schemas():
    for artifact_key, artifact_path in SAMPLER_ARTIFACTS.items():
        schema_path = ARTIFACT_SCHEMA_MAPPING[artifact_key]
        schema = _load_json(schema_path)
        payload = _load_json(artifact_path)
        _validate(payload, schema)
