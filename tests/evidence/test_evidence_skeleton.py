from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
from pathlib import Path

from tools.evidence import update_evidence_index


def test_path_proof_validation_is_independent_of_clone_mtime(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)
    artifact = tmp_path / "artifact.log"
    artifact.write_bytes(b"bound bytes\n")
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    kwargs = {
        "rel": "artifact.log",
        "sha256": digest,
        "size_bytes": artifact.stat().st_size,
        "mtime_utc": "2026-07-23T00:00:00Z",
        "produced_at": "2026-07-23T00:00:01Z",
        "default_produced_at": "2026-07-23T00:00:01Z",
        "stat_mtime": artifact.stat().st_mtime,
    }
    update_evidence_index._write_path_proof(check=False, **kwargs)
    proof = tmp_path / "artifact.log.path_proof.txt"
    original = proof.read_bytes()

    os.utime(artifact, (1, 1))
    clone_kwargs = {**kwargs, "stat_mtime": artifact.stat().st_mtime}
    update_evidence_index._write_path_proof(check=True, **clone_kwargs)
    update_evidence_index._write_path_proof(check=False, **clone_kwargs)
    assert proof.read_bytes() == original


def test_unchanged_legacy_proof_is_not_retimestamped(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)
    rel = "artifacts/proofs/success_get.txt"
    artifact = tmp_path / rel
    artifact.parent.mkdir(parents=True)
    artifact.write_bytes(b"bound bytes\n")
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    kwargs = {
        "rel": rel,
        "sha256": digest,
        "size_bytes": artifact.stat().st_size,
        "mtime_utc": "2026-07-23T00:00:00Z",
        "produced_at": "2026-07-23T00:00:01Z",
        "default_produced_at": "2026-07-23T00:00:01Z",
        "stat_mtime": artifact.stat().st_mtime,
    }
    update_evidence_index._write_path_proof(check=False, **kwargs)
    proof = tmp_path / f"{rel}.path_proof.txt"
    original = proof.read_bytes()

    update_evidence_index._write_path_proof(
        check=False,
        **{
            **kwargs,
            "default_produced_at": "2099-01-01T00:00:00Z",
            "stat_mtime": 4_070_908_800.0,
        },
    )
    assert proof.read_bytes() == original


def test_isolated_path_proof_uses_immutable_manifest_timestamp(
    tmp_path,
    monkeypatch,
):
    monkeypatch.setattr(update_evidence_index, "ROOT", tmp_path)
    monkeypatch.setenv("HDE_ISOLATED_RELEASE_BUILD", "1")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    (catalog / "manifest.json").write_text(
        json.dumps({"built_at_utc": "2026-07-23T00:00:00Z"}) + "\n",
        encoding="utf-8",
    )
    artifact = tmp_path / "artifact.log"
    artifact.write_bytes(b"bound bytes\n")

    update_evidence_index._write_path_proof(
        "artifact.log",
        sha256=hashlib.sha256(artifact.read_bytes()).hexdigest(),
        size_bytes=artifact.stat().st_size,
        mtime_utc="2099-01-01T00:00:00Z",
        produced_at="2099-01-01T00:00:00Z",
        default_produced_at="2099-01-01T00:00:00Z",
        check=False,
        stat_mtime=artifact.stat().st_mtime,
    )

    proof = update_evidence_index._load_existing_proof(
        tmp_path / "artifact.log.path_proof.txt"
    )
    assert proof["mtime_utc"] == "2026-07-23T00:00:00Z"
    assert proof["produced_at_utc"] == "2026-07-23T00:00:00Z"


def test_index_canonical_and_hash_matches(tmp_path):
    entries = update_evidence_index._load_human_index()
    rendered = update_evidence_index._render_human_index(entries)
    assert rendered.endswith(b"\n")

    expected_hash = hashlib.sha256(rendered).hexdigest()
    sentinel_line = Path("docs/evidence/INDEX.sha256").read_text(encoding="utf-8").strip()
    assert sentinel_line == f"{expected_hash}  docs/evidence/INDEX.json"

    on_disk = Path("docs/evidence/INDEX.json").read_bytes()
    assert on_disk == rendered


def test_mirror_schema_and_parity():
    entries = update_evidence_index._load_human_index()
    mirror = Path("artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines(True)

    seen = set()
    prev = None
    required_fields = {
        "artifact_key",
        "discovered_physical_path",
        "produced_at_utc",
        "proof_anchor",
        "role",
        "sha256",
        "size_bytes",
    }
    optional_fields = {
        "epic_id",
        "notes",
        "record_type",
        "schema_version",
        "tokens",
    }
    acceptance_tokens = set(json.loads(Path("docs/acceptance_map_epic020.json").read_text()).get("token_status", {}))
    for line in mirror:
        assert line.endswith("\n")
        rec = json.loads(line)
        key_set = set(rec.keys())
        assert required_fields.issubset(key_set)
        assert key_set - (required_fields | optional_fields) == set()
        if "tokens" in rec:
            assert rec["tokens"], f"tokens missing for {rec['artifact_key']}"
            if rec.get("epic_id") == "HDE-EPIC020":
                assert acceptance_tokens, "EPIC020 acceptance token roster is required"
                assert set(rec["tokens"]).issubset(acceptance_tokens)
        key = (rec["artifact_key"], rec["discovered_physical_path"])
        assert key not in seen
        seen.add(key)
        if prev:
            assert key >= prev
        prev = key

        proof_path = Path(rec["proof_anchor"])
        assert proof_path.exists()
        proof = update_evidence_index._load_existing_proof(proof_path)
        assert proof.get("path") == rec["discovered_physical_path"]
        if rec["artifact_key"] == "index.machine_mirror":
            # Self-record: mirror sha256 is the canonical body digest; proof sha256 is the file digest.
            mirror_file_sha = hashlib.sha256(Path(rec["discovered_physical_path"]).read_bytes()).hexdigest()
            assert proof.get("sha256") == mirror_file_sha, f"file sha mismatch for {rec['artifact_key']}"
            assert proof.get("mirror_body_sha256") == rec["sha256"], f"body sha mismatch for {rec['artifact_key']}"
        else:
            assert proof.get("sha256") == rec["sha256"], f"sha mismatch for {rec['artifact_key']}"
        assert int(proof.get("size_bytes")) == rec["size_bytes"], f"size mismatch for {rec['artifact_key']}"
        assert "mtime_utc" in proof
        assert "produced_at_utc" in proof
        parsed_mtime = _dt.datetime.fromisoformat(proof["mtime_utc"].replace("Z", "+00:00"))
        assert parsed_mtime.tzinfo == _dt.timezone.utc
        assert parsed_mtime.microsecond == 0
        parsed_produced = _dt.datetime.fromisoformat(
            proof["produced_at_utc"].replace("Z", "+00:00")
        )
        assert parsed_produced.tzinfo == _dt.timezone.utc
        assert parsed_produced.microsecond == 0

    mirror_path = Path("artifacts/evidence_index.jsonl")
    lines = mirror_path.read_text(encoding="utf-8").splitlines(True)
    self_records = [
        (idx, json.loads(line))
        for idx, line in enumerate(lines, 1)
        if json.loads(line)["artifact_key"] == "index.machine_mirror"
    ]
    assert len(self_records) == 1
    self_idx, self_rec = self_records[0]
    assert self_rec["role"] == "self_record"
    body_lines = [line for idx, line in enumerate(lines, 1) if idx != self_idx]
    canonical_sha = hashlib.sha256("".join(body_lines).encode("utf-8")).hexdigest()
    assert self_rec["sha256"] == canonical_sha

    expected_keys = {
        (entry["artifact_key"], entry["discovered_physical_path"]) for entry in entries
    }
    assert expected_keys == seen


def test_index_entries_have_mirrors_and_path_proofs():
    entries = update_evidence_index._load_human_index()
    mirror = Path("artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines()

    mirror_by_key = {}
    for raw in mirror:
        rec = json.loads(raw)
        mirror_by_key[(rec["artifact_key"], rec["discovered_physical_path"])] = rec

    for entry in entries:
        key = (entry["artifact_key"], entry["discovered_physical_path"])
        assert key in mirror_by_key, f"missing mirror record for {key}"
        rec = mirror_by_key[key]
        proof_path = Path(rec["proof_anchor"])
        assert proof_path.exists(), f"missing path proof for {key}"
        proof = update_evidence_index._load_existing_proof(proof_path)
        assert proof.get("path") == entry["discovered_physical_path"]
        if rec["artifact_key"] == "index.machine_mirror":
            mirror_file_sha = hashlib.sha256(Path(rec["discovered_physical_path"]).read_bytes()).hexdigest()
            assert proof.get("sha256") == mirror_file_sha, f"file sha mismatch for {key}"
            assert proof.get("mirror_body_sha256") == rec["sha256"], f"body sha mismatch for {key}"
        else:
            assert proof.get("sha256") == rec["sha256"], f"sha mismatch for {key}"
        assert int(proof.get("size_bytes", "0")) == rec["size_bytes"], f"size mismatch for {key}"
        assert proof.get("mtime_utc")
        assert proof.get("produced_at_utc")


def test_runtime_env_connectivity_is_historical_only_in_current_indexes():
    target = ("runtime.env_connectivity", "artifacts/runtime/env_connectivity.snapshot.json")
    retired = {
        ("epic038.pr04.env_connectivity", "artifacts/runtime/env_connectivity.snapshot.json"),
        ("epic032.pr03.env_connectivity", "artifacts/runtime/env_connectivity.snapshot.json"),
    }
    entries = update_evidence_index._load_human_index()
    matching_entries = [
        entry for entry in entries
        if entry["discovered_physical_path"] == target[1]
        or (entry["artifact_key"], entry["discovered_physical_path"]) in retired
    ]
    assert [(entry["artifact_key"], entry["discovered_physical_path"]) for entry in matching_entries] == [target]
    assert matching_entries[0]["record_type"] == "historical_bridge_evidence"
    assert "tokens" not in matching_entries[0]
    assert "do not prove current service availability" in matching_entries[0]["notes"]

    # The frozen primary retains its capture-time label, while current index
    # metadata prevents that historical label from satisfying a current token.
    artifact = json.loads(Path(target[1]).read_text(encoding="utf-8"))
    proof_labels = artifact.get("proof_labels", [])
    assert {label.get("name") for label in proof_labels} == {"DEV_DB_BRIDGE_FALLBACK_OK"}
    assert {label.get("type") for label in proof_labels} == {"acceptance_token"}

    mirror_records = [json.loads(raw) for raw in Path("artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines() if raw]
    matching_mirror = [
        rec for rec in mirror_records
        if rec["discovered_physical_path"] == target[1]
        or (rec["artifact_key"], rec["discovered_physical_path"]) in retired
    ]
    assert [(rec["artifact_key"], rec["discovered_physical_path"]) for rec in matching_mirror] == [target]
    assert matching_mirror[0]["record_type"] == "historical_bridge_evidence"
    assert "tokens" not in matching_mirror[0]
    assert "do not prove current service availability" in matching_mirror[0]["notes"]
