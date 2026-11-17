"""HDE-EPIC043 WU-PR-05 (HDE-DIST008.3): the release-attestation predicate list as a contract.

The predicate list of HDE Schemas and Artifacts 6.2.1 (rows P-01 to P-12) is asserted over a
bundle in the attestation builder's on-disk layout, written outside the repository, under the
two parameter sets of the Product Owner's decision Q-03. The admission value is the same for
both, so a bundle is bound to its release by its identity: the manifest digest and the exact
source. The real builder is not run here; CI's release lane builds and verifies the real bundle.
The condition names are plan-local labels, not tokens.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from engine.serializer.canon import sercanon
from tools.evidence import build_release_attestation as builder

ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class ParameterSet:
    label: str
    condition: str
    admission: str


V1 = ParameterSet("V1", "M10_CURRENT_RELEASE_ATTESTATION_MATCH", "PR06R_B_FINAL_PASS")
V2 = ParameterSet("V2", "M10_V2_CURRENT_RELEASE_ATTESTATION_MATCH", "PR06R_B_FINAL_PASS")
ROWS = tuple(f"P-{i:02d}" for i in range(1, 13))
SANITY_LOG = "audit/gates/sanity_pipeline/sanity_pipeline.log"
SANITY_IDENTITY = "pipeline_identity:hde-release-sanity-v1"
SANITY_TAIL = "check 15 Final-LF validation:OK\nfirst_failed_stage:NONE\nsummary:PASS\n"
VERIFIER_ROW = {
    "attestation_root_inventory_invalid": "P-09",
    "attestation_bytes_invalid": "P-01",
    "attestation_contract_invalid": "P-01",
    "attestation_not_secret_safe": "P-11",
    "attestation_source_not_exact": "P-07",
    "attestation_checksum_invalid": "P-08",
    "attestation_file_path_unsafe": "P-09",
    "attestation_evidence_symlink_refused": "P-09",
    "attestation_file_binding_invalid": "P-09",
    "attestation_evidence_not_secret_safe": "P-11",
    "attestation_file_inventory_invalid": "P-09",
    "attestation_omitted_file_collision": "P-09",
    "attestation_transcript_binding_invalid": "P-10",
    "attestation_transcript_not_secret_safe": "P-11",
    "attestation_failure_receipt_present": "P-09",
    "attestation_unreadable": "P-01",
}
NONCLAIMS = ["builder_executes_no_ops", "no_database_write", "no_deployment_or_migration",
             "no_qa_pass_or_acceptance", "no_pf09_status_movement"]


@dataclass(frozen=True)
class Candidate:
    root: Path
    commit: str
    tree_sha256: str
    manifest: bytes

    @property
    def release_id(self) -> str:
        return hashlib.sha256(self.manifest).hexdigest()


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", "-c", "user.name=contract", "-c", "user.email=contract@invalid",
                    "-c", "commit.gpgsign=false", *args], cwd=root, check=True, capture_output=True,
                   env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "GIT_CONFIG_NOSYSTEM": "1",
                        "GIT_CONFIG_GLOBAL": "/dev/null",
                        "GIT_AUTHOR_DATE": "2026-01-01T00:00:00Z", "GIT_COMMITTER_DATE": "2026-01-01T00:00:00Z"})


def candidate(tmp_path: Path, name: str, manifest: bytes) -> Candidate:
    """A clean, committed candidate holding ``catalog/manifest.json``; identity read the builder's way."""
    root = tmp_path / f"candidate-{name}"
    (root / "catalog").mkdir(parents=True)
    (root / "catalog/manifest.json").write_bytes(manifest)
    _git(root, "init", "-q")
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "-m", f"candidate {name}")
    commit, clean = builder._git_identity(root)
    assert clean
    tree = builder._source_tree_digest(builder._snapshot(root, builder._tracked_paths(root)))
    return Candidate(root, commit, tree, manifest)


def evidence_bytes(name: str, manifest: bytes) -> bytes:
    if name == "catalog/manifest.json":
        return manifest
    if name == SANITY_LOG:
        return f"{SANITY_IDENTITY}\nconstructed contract-test log\n{SANITY_TAIL}".encode()
    return f"constructed contract-test evidence {name}\n".encode()


def build_bundle(out: Path, cand: Candidate, **overrides) -> Path:
    """A bundle in the builder's layout for ``cand``, outside the repository."""
    evidence = out / "evidence"
    names = sorted(set(builder.REQUIRED_EVIDENCE) | set(builder.ATTESTATION_GENERATED_OUTPUTS))
    for name in names:
        (evidence / name).parent.mkdir(parents=True, exist_ok=True)
        (evidence / name).write_bytes(evidence_bytes(name, cand.manifest))
    (out / "build.log").write_bytes(b"stage=contract_test\nexit_code=0\n")
    payload = {
        "schema": builder.SCHEMA, "source_commit": cand.commit, "source_commit_exact": True,
        "source_tree_sha256": cand.tree_sha256, "release_id": cand.release_id,
        "manifest_sha256": cand.release_id, "validation_result": "PASS",
        "release_admission": "PR06R_B_FINAL_PASS", "pipeline_stop": None,
        "rails": dict(sorted(builder.CLOSED_RAILS.items())),
        "files": [builder._file_record(evidence, Path(name)) for name in names],
        "omitted_files": [], "transcript": builder._file_record(out, Path("build.log")),
        "nonclaims": list(NONCLAIMS),
    }
    payload.update(overrides)
    seal(out, payload)
    return out


def seal(out: Path, payload: dict) -> None:
    raw = sercanon(payload, sort_keys=True)
    (out / "attestation.json").write_bytes(raw)
    (out / "attestation.json.sha256").write_bytes(f"{hashlib.sha256(raw).hexdigest()}  attestation.json\n".encode())


def evaluate(bundle: Path, params: ParameterSet, cand: Candidate) -> tuple[dict[str, bool | None], str | None]:
    """The predicate table: each row's result (None where the verifier stopped first), and the
    verifier's own code."""
    payload = json.loads((bundle / "attestation.json").read_bytes())
    schema = json.loads(builder.SCHEMA_PATH.read_text(encoding="utf-8"))
    retained = bundle / "evidence/catalog/manifest.json"
    retained_sha = hashlib.sha256(retained.read_bytes()).hexdigest() if retained.is_file() else None
    sanity = bundle / "evidence" / SANITY_LOG
    sanity_text = sanity.read_text(encoding="utf-8") if sanity.is_file() else ""
    table: dict[str, bool | None] = {
        "P-01": not tuple(Draft202012Validator(schema).iter_errors(payload)),
        "P-02": payload.get("source_commit_exact") is True,
        "P-03": payload.get("validation_result") == "PASS",
        "P-04": payload.get("release_id") == payload.get("manifest_sha256") == retained_sha == cand.release_id,
        "P-05": payload.get("release_admission") == params.admission,
        "P-06": "pipeline_stop" in payload and payload["pipeline_stop"] is None,
        "P-12": ("summary:FAIL" not in sanity_text and SANITY_IDENTITY in sanity_text
                 and sanity_text.endswith(SANITY_TAIL)),
    }
    code = None
    try:
        builder.verify_attestation(bundle, require_exact=True, source=cand.root)
    except builder.AttestationBuildError as exc:
        code = exc.code
    for row in ("P-07", "P-08", "P-09", "P-10", "P-11"):
        table[row] = None if code else True
    if code:
        # A P-01 code also covers _validate_payload's roster and identity rules.
        table[VERIFIER_ROW[code]] = False
    return {row: table[row] for row in ROWS}, code


def failed(table) -> set[str]:
    return {row for row, ok in table.items() if ok is False}


def active_release() -> tuple[ParameterSet, bytes]:
    """The checkout's release, read from its bytes (no admission): the label is the version of
    the thresholds the manifest binds."""
    manifest = (ROOT / "catalog/manifest.json").read_bytes()
    rows = [row for row in json.loads(manifest)["files"] if row["path"] == "math/thresholds.json"]
    assert len(rows) == 1
    thresholds = (ROOT / "math/thresholds.json").read_bytes()
    assert hashlib.sha256(thresholds).hexdigest() == rows[0]["sha256"]
    return {"1": V1, "2": V2}[json.loads(thresholds)["version"]], manifest


def constructed_manifest(label: str) -> bytes:
    return sercanon({"constructed": f"contract-test {label} binding; not a release"}, sort_keys=True)


@pytest.fixture
def pair(tmp_path):
    return {label: candidate(tmp_path, label, constructed_manifest(label)) for label in ("V1", "V2")}


def test_active_release_passes_its_own_parameter_set(tmp_path) -> None:
    params, manifest = active_release()
    cand = candidate(tmp_path, "active", manifest)
    table, code = evaluate(build_bundle(tmp_path / "bundle", cand), params, cand)
    assert (failed(table), code) == (set(), None), table
    assert all(table.values())


@pytest.mark.parametrize("own,other", [(V1, V2), (V2, V1)], ids=["V1", "V2"])
def test_each_set_passes_its_own_binding_and_refuses_the_other(tmp_path, pair, own, other) -> None:
    cand, wrong = pair[own.label], pair[other.label]
    bundle = build_bundle(tmp_path / f"bundle-{own.label}", cand)
    table, code = evaluate(bundle, own, cand)
    assert (failed(table), code) == (set(), None)
    table, code = evaluate(bundle, other, wrong)
    assert failed(table) == {"P-04", "P-07"} and code == "attestation_source_not_exact"


def test_admission_value_does_not_discriminate() -> None:
    assert V1.admission == V2.admission == "PR06R_B_FINAL_PASS"
    assert V1.condition != V2.condition


def _payload(bundle: Path) -> dict:
    return json.loads((bundle / "attestation.json").read_bytes())


@pytest.mark.parametrize("field,value,rows,code", [
    ("source_commit_exact", False, {"P-01", "P-02"}, "attestation_contract_invalid"),
    ("validation_result", "FAIL", {"P-01", "P-03"}, "attestation_contract_invalid"),
    ("release_admission", "PR06R_B_OTHER", {"P-01", "P-05"}, "attestation_contract_invalid"),
    ("pipeline_stop", "release_sanity", {"P-01", "P-06"}, "attestation_contract_invalid"),
    ("manifest_sha256", "e" * 64, {"P-01", "P-04"}, "attestation_contract_invalid"),
    ("unknown", True, {"P-01"}, "attestation_contract_invalid"),
], ids=["P-02", "P-03", "P-05", "P-06", "P-04-unequal", "P-01-unknown-key"])
def test_payload_perturbations_fail_on_their_rows(tmp_path, pair, field, value, rows, code) -> None:
    cand = pair["V2"]
    bundle = build_bundle(tmp_path / "bundle", cand, **{field: value})
    table, got = evaluate(bundle, V2, cand)
    assert (failed(table), got) == (rows, code)


def _rebind(bundle: Path) -> None:
    """Re-record every evidence file's binding and reseal, so only the perturbed predicate fails."""
    payload = _payload(bundle)
    payload["files"] = [builder._file_record(bundle / "evidence", Path(row["path"])) for row in payload["files"]]
    seal(bundle, payload)


def test_retained_manifest_not_the_release_fails_p04(tmp_path, pair) -> None:
    # The payload names the right release, but the retained manifest is another release's bytes.
    # The verifier does not compare them (its bindings are consistent), so only P-04 refuses.
    cand = pair["V1"]
    bundle = build_bundle(tmp_path / "bundle", cand)
    (bundle / "evidence/catalog/manifest.json").write_bytes(pair["V2"].manifest)
    _rebind(bundle)
    table, code = evaluate(bundle, V1, cand)
    assert (failed(table), code) == ({"P-04"}, None)


@pytest.mark.parametrize("field", ["source_commit", "source_tree_sha256"])
def test_source_identity_mismatch_fails_p07(tmp_path, pair, field) -> None:
    cand = pair["V1"]
    value = "a" * 40 if field == "source_commit" else "a" * 64
    table, code = evaluate(build_bundle(tmp_path / "bundle", cand, **{field: value}), V1, cand)
    assert (failed(table), code) == ({"P-07"}, "attestation_source_not_exact")


def test_wrong_sidecar_fails_p08(tmp_path, pair) -> None:
    cand = pair["V1"]
    bundle = build_bundle(tmp_path / "bundle", cand)
    (bundle / "attestation.json.sha256").write_bytes(b"0" * 64 + b"  attestation.json\n")
    table, code = evaluate(bundle, V1, cand)
    assert (failed(table), code) == ({"P-08"}, "attestation_checksum_invalid")


@pytest.mark.parametrize("mutation,code", [
    ("mutate", "attestation_file_binding_invalid"),
    ("extra", "attestation_file_inventory_invalid"),
    ("symlink", "attestation_evidence_symlink_refused"),
])
def test_evidence_inventory_perturbations_fail_p09(tmp_path, pair, mutation, code) -> None:
    cand = pair["V1"]
    bundle = build_bundle(tmp_path / "bundle", cand)
    target = bundle / "evidence/artifacts/math/release_id.txt"
    if mutation == "mutate":
        target.write_bytes(b"mutated\n")
    elif mutation == "extra":
        (bundle / "evidence/extra.txt").write_bytes(b"extra\n")
    else:
        target.unlink()
        target.symlink_to(bundle / "build.log")
    table, got = evaluate(bundle, V1, cand)
    assert (failed(table), got) == ({"P-09"}, code)


def test_tampered_transcript_fails_p10(tmp_path, pair) -> None:
    cand = pair["V1"]
    bundle = build_bundle(tmp_path / "bundle", cand)
    (bundle / "build.log").write_bytes(b"stage=contract_test\nexit_code=1\n")
    table, code = evaluate(bundle, V1, cand)
    assert (failed(table), code) == ({"P-10"}, "attestation_transcript_binding_invalid")


def test_unsafe_retained_text_fails_p11(tmp_path, pair) -> None:
    cand = pair["V1"]
    bundle = build_bundle(tmp_path / "bundle", cand)
    (bundle / "build.log").write_bytes(b"DATABASE_URL=postgres://user:secret@host/db\n")
    payload = _payload(bundle)
    payload["transcript"] = builder._file_record(bundle, Path("build.log"))
    seal(bundle, payload)
    table, code = evaluate(bundle, V1, cand)
    assert (failed(table), code) == ({"P-11"}, "attestation_transcript_not_secret_safe")


@pytest.mark.parametrize("text", [
    f"{SANITY_IDENTITY}\nconstructed\n",
    f"{SANITY_IDENTITY}\nsummary:FAIL\n{SANITY_TAIL}",
    f"pipeline_identity:other\n{SANITY_TAIL}",
], ids=["no-tail", "fail", "wrong-identity"])
def test_sanity_tail_fails_p12(tmp_path, pair, text) -> None:
    cand = pair["V1"]
    bundle = build_bundle(tmp_path / "bundle", cand)
    log = bundle / "evidence" / SANITY_LOG
    log.write_text(text, encoding="utf-8")
    _rebind(bundle)
    table, code = evaluate(bundle, V1, cand)
    assert (failed(table), code) == ({"P-12"}, None)


def test_p12_matches_the_builder_and_names_are_plan_local() -> None:
    source = (ROOT / "tools/evidence/build_release_attestation.py").read_text(encoding="utf-8")
    assert repr(SANITY_TAIL)[1:-1] in source and SANITY_IDENTITY in source
    schema = builder.SCHEMA_PATH.read_text(encoding="utf-8")
    for name in (V1.condition, V2.condition, "RELEASE_ID_RECOMPUTE_OK"):
        assert name not in source and name not in schema
