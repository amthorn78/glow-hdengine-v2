import hashlib
import json
from pathlib import Path

import pytest

from tools.qa import qa_harness
from tools.qa.qa_harness import (
    CheckResult,
    HarnessConfig,
    Status,
    evaluate_acceptance_map_viability,
    read_primary_header,
    record_check,
    record_check_family,
)

MATRIX_HEADER = (
    "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |\n"
    "| --- | --- | --- | --- | --- | --- | --- |\n"
)
TOKEN = "QA_HARNESS_DISCIPLINE_OK"
FIXED_TIMESTAMP = "2026-01-01T00:00:00Z"


def _write_evidence_graph(
    root: Path, bindings: dict[str, tuple[str, ...]]
) -> None:
    human_rows: list[dict[str, object]] = []
    mirror_rows: list[dict[str, object]] = []
    for path, artifact_keys in bindings.items():
        payload = (root / path).read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        size = len(payload)
        proof = root / f"{path}.path_proof.txt"
        proof.parent.mkdir(parents=True, exist_ok=True)
        proof.write_text(
            "\n".join(
                (
                    f"path: {path}",
                    f"size_bytes: {size}",
                    f"sha256: {digest}",
                    f"mtime_utc: {FIXED_TIMESTAMP}",
                    f"produced_at_utc: {FIXED_TIMESTAMP}",
                    "",
                )
            ),
            encoding="utf-8",
        )
        for artifact_key in artifact_keys:
            human_rows.append(
                {
                    "artifact_key": artifact_key,
                    "discovered_physical_path": path,
                }
            )
            mirror_rows.append(
                {
                    "artifact_key": artifact_key,
                    "discovered_physical_path": path,
                    "produced_at_utc": FIXED_TIMESTAMP,
                    "proof_anchor": f"{path}.path_proof.txt",
                    "role": "snapshot",
                    "sha256": digest,
                    "size_bytes": size,
                }
            )
    human_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    mirror_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    body_bytes = b"".join(
        (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode(
            "utf-8"
        )
        for row in mirror_rows
    )
    body_sha = hashlib.sha256(body_bytes).hexdigest()
    self_record: dict[str, object] = {
        "artifact_key": "index.machine_mirror",
        "discovered_physical_path": "artifacts/evidence_index.jsonl",
        "produced_at_utc": FIXED_TIMESTAMP,
        "proof_anchor": "artifacts/evidence_index.jsonl.path_proof.txt",
        "role": "self_record",
        "sha256": body_sha,
        "size_bytes": 0,
    }
    mirror_rows.append(self_record)
    mirror_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    while True:
        mirror_bytes = b"".join(
            (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode(
                "utf-8"
            )
            for row in mirror_rows
        )
        if self_record["size_bytes"] == len(mirror_bytes):
            break
        self_record["size_bytes"] = len(mirror_bytes)
    human_rows.append(
        {
            "artifact_key": "index.machine_mirror",
            "discovered_physical_path": "artifacts/evidence_index.jsonl",
        }
    )
    human_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    human_index = root / "docs/evidence/INDEX.json"
    human_index.parent.mkdir(parents=True, exist_ok=True)
    human_index.write_text(
        json.dumps(human_rows, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    mirror = root / "artifacts/evidence_index.jsonl"
    mirror.parent.mkdir(parents=True, exist_ok=True)
    mirror.write_bytes(mirror_bytes)
    (root / "artifacts/evidence_index.jsonl.path_proof.txt").write_text(
        "\n".join(
            (
                "path: artifacts/evidence_index.jsonl",
                f"size_bytes: {len(mirror_bytes)}",
                f"sha256: {hashlib.sha256(mirror_bytes).hexdigest()}",
                f"mirror_body_sha256: {body_sha}",
                f"mtime_utc: {FIXED_TIMESTAMP}",
                f"produced_at_utc: {FIXED_TIMESTAMP}",
                "",
            )
        ),
        encoding="utf-8",
    )


def _write_self_record_graph(root: Path) -> None:
    mirror_path = "artifacts/evidence_index.jsonl"
    body_sha = hashlib.sha256(b"").hexdigest()
    record: dict[str, object] = {
        "artifact_key": "index.machine_mirror",
        "discovered_physical_path": mirror_path,
        "produced_at_utc": FIXED_TIMESTAMP,
        "proof_anchor": f"{mirror_path}.path_proof.txt",
        "role": "self_record",
        "sha256": body_sha,
        "size_bytes": 0,
    }
    while True:
        mirror_bytes = (
            json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
        ).encode("utf-8")
        if record["size_bytes"] == len(mirror_bytes):
            break
        record["size_bytes"] = len(mirror_bytes)
    mirror = root / mirror_path
    mirror.parent.mkdir(parents=True, exist_ok=True)
    mirror.write_bytes(mirror_bytes)
    human = root / "docs/evidence/INDEX.json"
    human.parent.mkdir(parents=True, exist_ok=True)
    human.write_text(
        json.dumps(
            [
                {
                    "artifact_key": "index.machine_mirror",
                    "discovered_physical_path": mirror_path,
                }
            ],
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
        encoding="utf-8",
    )
    (root / f"{mirror_path}.path_proof.txt").write_text(
        "\n".join(
            (
                f"path: {mirror_path}",
                f"size_bytes: {len(mirror_bytes)}",
                f"sha256: {hashlib.sha256(mirror_bytes).hexdigest()}",
                f"mirror_body_sha256: {body_sha}",
                f"mtime_utc: {FIXED_TIMESTAMP}",
                f"produced_at_utc: {FIXED_TIMESTAMP}",
                "",
            )
        ),
        encoding="utf-8",
    )


def _matrix_row(
    evidence: str = "evidence/proof.json",
    *,
    ci: str = "python tools/check.py",
    qa: str = "checks/acceptance-map-viability/primary.log",
    token: str = TOKEN,
) -> str:
    return f"| {token} | PF04 | {evidence} | {ci} | {qa} | Implemented | fixture |\n"


@pytest.fixture
def repository(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    for key, value in {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "APP_ENV": "test",
    }.items():
        monkeypatch.setenv(key, value)
    (tmp_path / "docs/pfcanon").mkdir(parents=True)
    (tmp_path / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md").write_text(
        "## **2.0 Acceptance Tokens (single-home roster)**\n"
        "* **QA\\_HARNESS\\_DISCIPLINE\\_OK** — declared.\n"
        "* **QA\\_HARNESS\\_DISCIPLINE\\_OK** — duplicate declaration is harmless.\n"
        "`RETIRED_PROSE_OK` is not a token.\n"
        "## **2.1 Next**\n",
        encoding="utf-8",
    )
    (tmp_path / "evidence").mkdir()
    (tmp_path / "evidence/proof.json").write_text('{"ok":true}\n', encoding="utf-8")
    _write_evidence_graph(
        tmp_path, {"evidence/proof.json": ("fixture.primary_evidence",)}
    )
    (tmp_path / "tools").mkdir()
    (tmp_path / "tools/check.py").write_text("raise SystemExit(0)\n", encoding="utf-8")
    return tmp_path


def _configure(
    root: Path,
    epic_id: str,
    *,
    evidence_titles: tuple[str, ...] = ("evidence/proof.json",),
    evidence: str = "evidence/proof.json",
    ci: str = "python tools/check.py",
    qa: str = "checks/acceptance-map-viability/primary.log",
    step_names: tuple[str, ...] = (),
) -> HarnessConfig:
    config = HarnessConfig(epic_id, repo_root=root, step_names=step_names)
    config.acceptance_map_path.parent.mkdir(parents=True, exist_ok=True)
    config.acceptance_map_path.write_text(
        json.dumps(
            {
                "epic_id": epic_id,
                "tokens": [
                    {
                        "name": TOKEN,
                        "owner_pf": "PF04",
                        "status": "implemented",
                        "evidence_titles": list(evidence_titles),
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    config.token_matrix_path.parent.mkdir(parents=True, exist_ok=True)
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(evidence, ci=ci, qa=qa), encoding="utf-8"
    )
    return config


def test_normal_governance_binding_rejects_stale_artifact_bytes(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    (repository / "evidence/proof.json").write_text(
        '{"ok":false}\n', encoding="utf-8"
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "hash/size" in result.status_reason


def test_normal_governance_binding_rejects_wrong_proof_anchor(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    mirror = repository / "artifacts/evidence_index.jsonl"
    records = [
        json.loads(line) for line in mirror.read_text(encoding="utf-8").splitlines()
    ]
    record = next(item for item in records if item["role"] != "self_record")
    record["proof_anchor"] = "evidence/not-the-sibling.path_proof.txt"
    mirror.write_text(
        "".join(
            json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n"
            for item in records
        ),
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "proof_anchor" in result.status_reason


def test_normal_governance_binding_rejects_duplicate_proof_field(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    proof = repository / "evidence/proof.json.path_proof.txt"
    proof.write_text(
        proof.read_text(encoding="utf-8")
        + "sha256: "
        + hashlib.sha256((repository / "evidence/proof.json").read_bytes()).hexdigest()
        + "\n",
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "duplicate field" in result.status_reason


def test_normal_governance_binding_allows_informational_proof_field(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC039")
    proof = repository / "evidence/proof.json.path_proof.txt"
    proof.write_text(
        proof.read_text(encoding="utf-8") + "capture_note: fixture-only\n",
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.PASS


def test_governance_binding_rejects_external_proof_symlink(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    proof = repository / "evidence/proof.json.path_proof.txt"
    outside = repository.parent / f"{repository.name}-external-proof.txt"
    outside.write_bytes(proof.read_bytes())
    proof.unlink()
    proof.symlink_to(outside)

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "sibling path proof is not a regular repository file" in result.status_reason


def test_governance_binding_rejects_aliased_proof_parent(repository: Path):
    real = repository / "real-evidence"
    real.mkdir()
    (real / "proof.json").write_text('{"ok":true}\n', encoding="utf-8")
    (repository / "aliased-evidence").symlink_to(real, target_is_directory=True)
    _write_evidence_graph(
        repository,
        {"aliased-evidence/proof.json": ("fixture.aliased_evidence",)},
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("aliased-evidence/proof.json",),
        evidence="aliased-evidence/proof.json",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "parent path is aliased" in result.status_reason


def test_governance_binding_rejects_transient_proof_symlink_swap(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    config = _configure(repository, "HDE-EPIC039")
    proof = repository / "evidence/proof.json.path_proof.txt"
    outside = repository.parent / f"{repository.name}-transient-proof.txt"
    outside.write_bytes(proof.read_bytes())
    original_reader = qa_harness._read_stable_repo_file_bytes
    swapped = False

    def swap_during_secure_open(
        repo_root: Path, path: Path, *, subject: str
    ) -> tuple[Status, str, bytes | None]:
        nonlocal swapped
        if path != proof or swapped:
            return original_reader(repo_root, path, subject=subject)
        swapped = True
        original_bytes = proof.read_bytes()
        proof.unlink()
        proof.symlink_to(outside)
        try:
            return original_reader(repo_root, path, subject=subject)
        finally:
            proof.unlink()
            proof.write_bytes(original_bytes)

    monkeypatch.setattr(
        qa_harness, "_read_stable_repo_file_bytes", swap_during_secure_open
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "sibling path proof could not be opened without following aliases" in (
        result.status_reason
    )


def test_self_record_proof_is_validated_before_ordinary_evidence_passes(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC039")
    proof = repository / "artifacts/evidence_index.jsonl.path_proof.txt"
    proof.write_text(
        "\n".join(
            "mirror_body_sha256: " + "0" * 64
            if line.startswith("mirror_body_sha256: ")
            else line
            for line in proof.read_text(encoding="utf-8").splitlines()
        )
        + "\n",
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "path proof body hash" in result.status_reason


@pytest.mark.parametrize(
    ("ledger", "field", "value"),
    [
        ("human", "tokens", "NOT_A_LIST"),
        ("human", "tokens", None),
        ("human", "produced_at_utc", None),
        ("human", "sha256", None),
        ("human", "size_bytes", None),
        ("mirror", "epic_id", []),
        ("mirror", "notes", {"not": "text"}),
        ("mirror", "schema_version", 1),
        ("mirror", "tokens", None),
    ],
)
def test_governance_graph_rejects_invalid_optional_metadata_types(
    repository: Path, ledger: str, field: str, value: object
):
    config = _configure(repository, "HDE-EPIC039")
    if ledger == "human":
        path = repository / "docs/evidence/INDEX.json"
        rows = json.loads(path.read_text(encoding="utf-8"))
        row = next(item for item in rows if item["artifact_key"] != "index.machine_mirror")
        row[field] = value
        path.write_text(
            json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
    else:
        path = repository / "artifacts/evidence_index.jsonl"
        rows = [
            json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
        ]
        row = next(item for item in rows if item["role"] != "self_record")
        row[field] = value
        path.write_text(
            "".join(
                json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n"
                for item in rows
            ),
            encoding="utf-8",
        )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert f"{field} metadata" in result.status_reason


def test_governance_graph_allows_minimal_historical_human_rows(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    rows = json.loads(
        (repository / "docs/evidence/INDEX.json").read_text(encoding="utf-8")
    )

    assert all(
        set(row) == {"artifact_key", "discovered_physical_path"} for row in rows
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.PASS


@pytest.mark.parametrize("mutation", ["pretty", "reordered"])
def test_governance_graph_rejects_noncanonical_human_index(
    repository: Path,
    mutation: str,
):
    path = repository / "docs/evidence/INDEX.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    if mutation == "pretty":
        content = json.dumps(rows, sort_keys=True, indent=2) + "\n"
        expected_reason = "is not canonical JSON with a final LF"
    else:
        content = (
            json.dumps(list(reversed(rows)), sort_keys=True, separators=(",", ":"))
            + "\n"
        )
        expected_reason = "records are not sorted by key/path"
    path.write_text(content, encoding="utf-8")

    result, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039")
    )

    assert result.status is Status.FAIL_TOOLING
    assert expected_reason in result.status_reason


def test_governance_validator_rechecks_artifact_bytes_within_evaluation(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC039")
    target = repository / "evidence/proof.json"
    validator = qa_harness._EvidenceGovernanceValidator(config)

    first = validator.validate("evidence/proof.json", target, target.read_bytes())
    target.write_text('{"ok":false}\n', encoding="utf-8")
    second = validator.validate("evidence/proof.json", target, target.read_bytes())

    assert first == (Status.PASS, "")
    assert second[0] is Status.FAIL_TOOLING
    assert "changed path identity or bytes" in second[1]


def test_governance_validator_final_stability_check_rejects_late_change(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC039")
    target = repository / "evidence/proof.json"
    validator = qa_harness._EvidenceGovernanceValidator(config)

    assert validator.validate(
        "evidence/proof.json", target, target.read_bytes()
    ) == (Status.PASS, "")
    target.write_text('{"ok":false}\n', encoding="utf-8")
    stability = validator.verify_stability()

    assert stability[0] is Status.FAIL_TOOLING
    assert "changed during evaluation" in stability[1]


def test_governance_validator_rechecks_proof_bytes_within_evaluation(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC039")
    target = repository / "evidence/proof.json"
    proof = repository / "evidence/proof.json.path_proof.txt"
    validator = qa_harness._EvidenceGovernanceValidator(config)

    first = validator.validate("evidence/proof.json", target, target.read_bytes())
    proof.write_text(
        proof.read_text(encoding="utf-8") + "capture_note: changed\n",
        encoding="utf-8",
    )
    second = validator.validate("evidence/proof.json", target, target.read_bytes())

    assert first == (Status.PASS, "")
    assert second[0] is Status.FAIL_TOOLING
    assert "proof changed during evaluation" in second[1]


def test_json_validation_and_governance_use_the_same_captured_bytes(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    target = repository / "evidence/proof.json"
    governed_invalid = b"not-json\n"
    target.write_bytes(governed_invalid)
    _write_evidence_graph(
        repository, {"evidence/proof.json": ("fixture.primary_evidence",)}
    )
    target.write_text('{"ok":true}\n', encoding="utf-8")
    config = _configure(repository, "HDE-EPIC039")
    original = qa_harness._validate_json_evidence_bytes

    def validate_then_swap(payload: bytes) -> None:
        original(payload)
        target.write_bytes(governed_invalid)

    monkeypatch.setattr(qa_harness, "_validate_json_evidence_bytes", validate_then_swap)
    diagnostic = qa_harness._file_diagnostic(
        config,
        token=TOKEN,
        source_field="acceptance_map.evidence_titles",
        item_index=1,
        value="evidence/proof.json",
        planned_paths=set(),
        referenced_manifests=set(),
        require_governance=True,
        governance_validator=qa_harness._EvidenceGovernanceValidator(config),
    )

    assert diagnostic.status is Status.FAIL_TOOLING
    assert diagnostic.reason == "acceptance evidence changed bytes during evaluation"


@pytest.mark.parametrize("missing_side", ["human", "mirror"])
def test_governance_binding_requires_membership_in_both_ledgers(
    repository: Path, missing_side: str
):
    other = repository / "evidence/other.txt"
    other.write_text("other\n", encoding="utf-8")
    _write_evidence_graph(
        repository,
        {
            "evidence/other.txt": ("fixture.other",),
            "evidence/proof.json": ("fixture.primary_evidence",),
        },
    )
    if missing_side == "human":
        path = repository / "docs/evidence/INDEX.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload = [
            row
            for row in payload
            if row["discovered_physical_path"] != "evidence/proof.json"
        ]
        path.write_text(
            json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
    else:
        path = repository / "artifacts/evidence_index.jsonl"
        payload = [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
        ]
        payload = [
            row
            for row in payload
            if row["discovered_physical_path"] != "evidence/proof.json"
        ]
        path.write_text(
            "".join(
                json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
                for row in payload
            ),
            encoding="utf-8",
        )
    config = _configure(repository, "HDE-EPIC039")

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "key/path bindings disagree" in result.status_reason


def test_governance_membership_uses_lexical_declared_path(repository: Path):
    alias = repository / "evidence/alias.json"
    alias.symlink_to("proof.json")
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("evidence/alias.json",),
        evidence="evidence/alias.json",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "not an approved governed-primary symlink" in result.status_reason


def test_canonical_endpoint_catalog_symlink_can_be_governed_evidence(
    repository: Path,
):
    target = repository / "artifacts/audit/ENDPOINTS_CATALOG.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('{"endpoints":[]}\n', encoding="utf-8")
    catalog = repository / "docs/ENDPOINTS_CATALOG.json"
    catalog.symlink_to("../artifacts/audit/ENDPOINTS_CATALOG.json")
    _write_evidence_graph(
        repository,
        {"docs/ENDPOINTS_CATALOG.json": ("fixture.endpoint_catalog",)},
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("docs/ENDPOINTS_CATALOG.json",),
        evidence="docs/ENDPOINTS_CATALOG.json",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.PASS


def test_canonical_endpoint_catalog_target_symlink_cannot_pass(repository: Path):
    target = repository / "artifacts/audit/ENDPOINTS_CATALOG.json"
    alternate = repository / "artifacts/audit/alternate.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    alternate.write_text('{"endpoints":[]}\n', encoding="utf-8")
    target.symlink_to(alternate.name)
    catalog = repository / "docs/ENDPOINTS_CATALOG.json"
    catalog.symlink_to("../artifacts/audit/ENDPOINTS_CATALOG.json")
    _write_evidence_graph(
        repository,
        {"docs/ENDPOINTS_CATALOG.json": ("fixture.endpoint_catalog",)},
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("docs/ENDPOINTS_CATALOG.json",),
        evidence="docs/ENDPOINTS_CATALOG.json",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "target is not a regular file" in result.status_reason


def test_canonical_endpoint_catalog_target_parent_alias_cannot_pass(
    repository: Path,
):
    real_audit = repository / "artifacts/real-audit"
    real_audit.mkdir(parents=True)
    (real_audit / "ENDPOINTS_CATALOG.json").write_text(
        '{"endpoints":[]}\n', encoding="utf-8"
    )
    (repository / "artifacts/audit").symlink_to(
        real_audit.name, target_is_directory=True
    )
    catalog = repository / "docs/ENDPOINTS_CATALOG.json"
    catalog.symlink_to("../artifacts/audit/ENDPOINTS_CATALOG.json")
    _write_evidence_graph(
        repository,
        {"docs/ENDPOINTS_CATALOG.json": ("fixture.endpoint_catalog",)},
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("docs/ENDPOINTS_CATALOG.json",),
        evidence="docs/ENDPOINTS_CATALOG.json",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "without following aliases" in result.status_reason


def test_canonical_endpoint_catalog_retarget_during_evaluation_fails(
    repository: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    target = repository / "artifacts/audit/ENDPOINTS_CATALOG.json"
    alternate = repository / "artifacts/audit/alternate.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('{"endpoints":[]}\n', encoding="utf-8")
    alternate.write_bytes(target.read_bytes())
    catalog = repository / "docs/ENDPOINTS_CATALOG.json"
    catalog.symlink_to("../artifacts/audit/ENDPOINTS_CATALOG.json")
    _write_evidence_graph(
        repository,
        {"docs/ENDPOINTS_CATALOG.json": ("fixture.endpoint_catalog",)},
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("docs/ENDPOINTS_CATALOG.json",),
        evidence="docs/ENDPOINTS_CATALOG.json",
    )
    original = qa_harness._validate_json_evidence_bytes

    def validate_then_retarget(payload: bytes) -> None:
        original(payload)
        catalog.unlink()
        catalog.symlink_to("../artifacts/audit/alternate.json")

    monkeypatch.setattr(
        qa_harness,
        "_validate_json_evidence_bytes",
        validate_then_retarget,
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "not an approved governed-primary symlink" in result.status_reason


def test_canonical_endpoint_catalog_target_replacement_during_evaluation_fails(
    repository: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    target = repository / "artifacts/audit/ENDPOINTS_CATALOG.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('{"endpoints":[]}\n', encoding="utf-8")
    catalog = repository / "docs/ENDPOINTS_CATALOG.json"
    catalog.symlink_to("../artifacts/audit/ENDPOINTS_CATALOG.json")
    _write_evidence_graph(
        repository,
        {"docs/ENDPOINTS_CATALOG.json": ("fixture.endpoint_catalog",)},
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("docs/ENDPOINTS_CATALOG.json",),
        evidence="docs/ENDPOINTS_CATALOG.json",
    )
    original = qa_harness._validate_json_evidence_bytes
    replaced = False

    def validate_then_replace_target(payload: bytes) -> None:
        nonlocal replaced
        original(payload)
        if replaced:
            return
        replaced = True
        replacement = target.with_name("ENDPOINTS_CATALOG.replacement.json")
        replacement.write_bytes(payload)
        replacement.replace(target)

    monkeypatch.setattr(
        qa_harness,
        "_validate_json_evidence_bytes",
        validate_then_replace_target,
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "changed path identity or bytes" in result.status_reason


def test_canonical_endpoint_catalog_external_symlink_fails(repository: Path):
    external = repository.parent / f"{repository.name}-external-catalog.json"
    external.write_text('{"endpoints":[]}\n', encoding="utf-8")
    catalog = repository / "docs/ENDPOINTS_CATALOG.json"
    catalog.symlink_to(external)
    _write_evidence_graph(
        repository,
        {"docs/ENDPOINTS_CATALOG.json": ("fixture.endpoint_catalog",)},
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("docs/ENDPOINTS_CATALOG.json",),
        evidence="docs/ENDPOINTS_CATALOG.json",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_BEHAVIOR
    assert "reference escapes repository" in result.status_reason


def test_registered_symlinked_acceptance_evidence_cannot_pass(repository: Path):
    alias = repository / "evidence/alias.json"
    alias.symlink_to("proof.json")
    _write_evidence_graph(
        repository,
        {"evidence/alias.json": ("fixture.aliased_evidence",)},
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("evidence/alias.json",),
        evidence="evidence/alias.json",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "not an approved governed-primary symlink" in result.status_reason


def test_cyclic_acceptance_evidence_alias_fails_causally(repository: Path):
    alias = repository / "evidence/loop.json"
    alias.symlink_to(alias.name)
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("evidence/loop.json",),
        evidence="evidence/loop.json",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "reference cannot be resolved safely" in result.status_reason


def test_symlinked_human_index_cannot_govern_acceptance(repository: Path):
    human_index = repository / "docs/evidence/INDEX.json"
    external_index = repository.parent / f"{repository.name}-external-index.json"
    external_index.write_bytes(human_index.read_bytes())
    human_index.unlink()
    human_index.symlink_to(external_index)
    config = _configure(repository, "HDE-EPIC039")

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "without following aliases" in result.status_reason


def test_internally_aliased_machine_mirror_cannot_govern_acceptance(
    repository: Path,
):
    mirror = repository / "artifacts/evidence_index.jsonl"
    alternate = repository / "artifacts/evidence_index.actual.jsonl"
    mirror.rename(alternate)
    mirror.symlink_to(alternate.name)
    config = _configure(repository, "HDE-EPIC039")

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "without following aliases" in result.status_reason


@pytest.mark.parametrize(
    "input_name",
    ["pf04", "acceptance_map", "matrix", "pf04_source_set"],
)
def test_viability_rechecks_all_causal_inputs_before_pass(
    repository: Path,
    monkeypatch: pytest.MonkeyPatch,
    input_name: str,
):
    config = _configure(repository, "HDE-EPIC039")
    original_apply = qa_harness._apply_pytest_collection

    def mutate_after_collection(*args: object, **kwargs: object):
        receipts = original_apply(*args, **kwargs)
        if input_name == "pf04_source_set":
            extra = repository / "docs/pfcanon/PF04-Canon-HDE-Governance-v999.md"
            extra.write_text("additional source\n", encoding="utf-8")
        else:
            paths = {
                "pf04": repository
                / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md",
                "acceptance_map": config.acceptance_map_path,
                "matrix": config.token_matrix_path,
            }
            path = paths[input_name]
            path.write_bytes(path.read_bytes() + b"\n")
        return receipts

    monkeypatch.setattr(
        qa_harness,
        "_apply_pytest_collection",
        mutate_after_collection,
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "changed during acceptance evaluation" in result.status_reason


def test_machine_mirror_self_record_uses_body_and_full_file_hashes(
    repository: Path,
):
    _write_self_record_graph(repository)
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("artifacts/evidence_index.jsonl",),
        evidence="artifacts/evidence_index.jsonl",
    )

    result, _ = evaluate_acceptance_map_viability(config)
    record = json.loads(
        (repository / "artifacts/evidence_index.jsonl").read_text(encoding="utf-8")
    )
    proof = {
        key: value
        for key, value in (
            line.split(": ", 1)
            for line in (
                repository / "artifacts/evidence_index.jsonl.path_proof.txt"
            ).read_text(encoding="utf-8").splitlines()
        )
    }

    assert result.status is Status.PASS
    assert record["sha256"] == hashlib.sha256(b"").hexdigest()
    assert proof["sha256"] != record["sha256"]
    assert proof["mirror_body_sha256"] == record["sha256"]


@pytest.mark.parametrize(
    ("mutation", "reason"),
    [
        ("row_body", "self-record body hash"),
        ("row_size", "self-record size"),
        ("proof_full", "path proof hash/size"),
        ("proof_body", "path proof body hash"),
    ],
)
def test_machine_mirror_self_record_rejects_incoherent_hash_or_size(
    repository: Path, mutation: str, reason: str
):
    _write_self_record_graph(repository)
    mirror = repository / "artifacts/evidence_index.jsonl"
    proof = repository / "artifacts/evidence_index.jsonl.path_proof.txt"
    if mutation.startswith("row_"):
        record = json.loads(mirror.read_text(encoding="utf-8"))
        if mutation == "row_body":
            record["sha256"] = "0" * 64
        else:
            record["size_bytes"] += 1
        mirror.write_text(
            json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        replacements = {
            "sha256": hashlib.sha256(mirror.read_bytes()).hexdigest(),
            "size_bytes": str(mirror.stat().st_size),
        }
        proof.write_text(
            "\n".join(
                (
                    f"{key}: {replacements.get(key, value)}"
                    for key, value in (
                        line.split(": ", 1)
                        for line in proof.read_text(encoding="utf-8").splitlines()
                    )
                )
            )
            + "\n",
            encoding="utf-8",
        )
    else:
        field = "sha256" if mutation == "proof_full" else "mirror_body_sha256"
        lines = proof.read_text(encoding="utf-8").splitlines()
        proof.write_text(
            "\n".join(
                f"{field}: {'0' * 64}" if line.startswith(f"{field}: ") else line
                for line in lines
            )
            + "\n",
            encoding="utf-8",
        )
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("artifacts/evidence_index.jsonl",),
        evidence="artifacts/evidence_index.jsonl",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert reason in result.status_reason


def _write_v1(config: HarnessConfig, check_id: str, *, status: str = "PASS") -> Path:
    path = config.qa_root / "checks" / check_id / "primary.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "schema_version": "pf27.step_log_header.v1",
                "check_id": check_id,
                "status": status,
            },
            sort_keys=True,
        )
        + "\nhistorical body\n",
        encoding="utf-8",
    )
    return path


def _entry(
    config: HarnessConfig, check_id: str, *, full: bool = False
) -> dict[str, str]:
    path = f"checks/{check_id}/primary.log"
    if full:
        path = f"audit/qa/hde-epic{config.epic_number}/{path}"
    return {"check_id": check_id, "log_path": path, "status": "STALE_MANIFEST_VALUE"}


def _pass(check_id: str, *, command=("true",)) -> CheckResult:
    return CheckResult(
        check_id,
        Status.PASS,
        exit_code=0,
        command=command,
        command_provenance="test fixture",
    )


def test_epic027_flat_v1_transition_retains_all_historical_identities(repository: Path):
    config = _configure(repository, "HDE-EPIC027")
    check_ids = ("d0_discovery", *(f"po-{index:03d}" for index in range(1, 11)))
    before = {}
    manifest = {}
    for index, check_id in enumerate(check_ids):
        path = _write_v1(config, check_id)
        before[check_id] = path.read_bytes()
        manifest[check_id] = _entry(config, check_id, full=index % 2 == 0)
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )

    record_check(config, _pass("acceptance-map-viability"))

    transitioned = json.loads(
        (config.qa_root / "qa_step_logs_manifest.json").read_text()
    )
    assert set(transitioned) == {*check_ids, "acceptance-map-viability"}
    for check_id in check_ids:
        assert transitioned[check_id] == {
            "check_id": check_id,
            "log_path": f"audit/qa/hde-epic027/checks/{check_id}/primary.log",
            "status": "PASS",
        }
        assert (
            config.qa_root / "checks" / check_id / "primary.log"
        ).read_bytes() == before[check_id]


@pytest.mark.parametrize("schema_version", ["v1", "v2"])
def test_uppercase_legacy_entry_cannot_be_carried_into_current_manifest(
    repository: Path, schema_version: str
):
    config = _configure(repository, "HDE-EPIC027")
    check_id = "D00_legacy"
    if schema_version == "v1":
        primary = _write_v1(config, check_id)
    else:
        relative = f"audit/qa/hde-epic027/checks/{check_id}/primary.log"
        primary = config.repo_root / relative
        primary.parent.mkdir(parents=True)
        primary.write_text(
            json.dumps(
                {
                    "captured_env": {},
                    "check_id": check_id,
                    "check_name": "historical uppercase check",
                    "claimed_tokens": [],
                    "command": ["true"],
                    "command_provenance": "historical test fixture",
                    "evidence_artifacts": [relative],
                    "exit_code": 0,
                    "intended_tokens": [],
                    "pf_refs": [],
                    "schema_version": "pf27.step_log_header.v2",
                    "status": "PASS",
                    "status_reason": "",
                    "timestamp_utc": "2026-08-18T00:00:00Z",
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n",
            encoding="utf-8",
        )
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    entry = _entry(config, check_id)
    if schema_version == "v2":
        entry["status"] = "PASS"
    manifest.write_text(
        json.dumps({check_id: entry}), encoding="utf-8"
    )
    manifest_before = manifest.read_bytes()
    primary_before = primary.read_bytes()

    with pytest.raises(ValueError, match="lowercase ASCII"):
        record_check(config, _pass("current"))

    assert manifest.read_bytes() == manifest_before
    assert primary.read_bytes() == primary_before
    assert not (config.qa_root / "checks/current/primary.log").exists()


def test_epic028_wrapped_v1_transition_becomes_flat(repository: Path):
    config = _configure(repository, "HDE-EPIC028")
    for check_id in ("d0", "po-001"):
        _write_v1(config, check_id)
    manifest = {
        "epic_id": config.epic_id,
        "checks": {check_id: _entry(config, check_id) for check_id in ("d0", "po-001")},
    }
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )
    record_check(config, _pass("current"))
    transitioned = json.loads(
        (config.qa_root / "qa_step_logs_manifest.json").read_text()
    )
    assert set(transitioned) == {"d0", "po-001", "current"}
    assert "epic_id" not in transitioned and "checks" not in transitioned


def test_epic021_runs_envelope_is_recognized_without_import(repository: Path):
    config = _configure(repository, "HDE-EPIC021")
    historical = config.qa_root / "old-run/step.log"
    historical.parent.mkdir(parents=True)
    historical.write_text("historical bytes\n", encoding="utf-8")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "epic_id": config.epic_id,
                "runs": [{"run_id": "old", "steps": [{"log_path": str(historical)}]}],
            }
        ),
        encoding="utf-8",
    )
    original = historical.read_bytes()
    record_check(config, _pass("current"))
    assert set(json.loads(manifest.read_text())) == {"current"}
    assert historical.read_bytes() == original


def test_epic029_bracket_headers_fail_closed_without_writes(repository: Path):
    config = _configure(repository, "HDE-EPIC029")
    check_ids = ("po-epic-close-live-qa", "po-precommit", "po-postcommit")
    checks = {}
    for check_id in check_ids:
        path = config.qa_root / "checks" / check_id / "primary.log"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"[check_id] {check_id}\n[exit_code] 0\n", encoding="utf-8")
        checks[check_id] = _entry(config, check_id)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps({"epic_id": config.epic_id, "checks": checks}), encoding="utf-8"
    )
    before = manifest.read_bytes()
    with pytest.raises(
        ValueError,
        match="unsupported primary-log schema without governed status: po-epic-close-live-qa",
    ):
        record_check(config, _pass("acceptance-map-viability"))
    assert manifest.read_bytes() == before
    assert not (config.qa_root / "checks/acceptance-map-viability/primary.log").exists()


def test_manifest_key_entry_and_header_identity_must_agree(repository: Path):
    config = _configure(repository, "HDE-EPIC027")
    _write_v1(config, "po-001")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps({"po-001": {**_entry(config, "po-001"), "check_id": "po-002"}})
    )
    with pytest.raises(ValueError, match="identity disagree"):
        record_check(config, _pass("current"))


def test_transition_rejects_invalid_header_status(repository: Path):
    config = _configure(repository, "HDE-EPIC027")
    _write_v1(config, "po-001", status="SUCCESS")
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps({"po-001": _entry(config, "po-001")}), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="invalid status"):
        record_check(config, _pass("current"))


@pytest.mark.parametrize(
    "log_path",
    [
        "checks/po-001/missing.log",
        "../checks/po-001/primary.log",
        "/tmp/primary.log",
        "audit/qa/hde-epic028/checks/po-001/primary.log",
        "checks/po-002/primary.log",
    ],
)
def test_transition_rejects_missing_traversing_foreign_or_mismatched_paths(
    repository: Path, log_path: str
):
    config = _configure(repository, "HDE-EPIC027")
    _write_v1(config, "po-001")
    entry = _entry(config, "po-001")
    entry["log_path"] = log_path
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps({"po-001": entry}), encoding="utf-8"
    )
    with pytest.raises(ValueError):
        record_check(config, _pass("current"))


def test_transition_rejects_unsupported_json_header_schema(repository: Path):
    config = _configure(repository, "HDE-EPIC027")
    path = config.qa_root / "checks/po-001/primary.log"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps(
            {"schema_version": "unknown", "check_id": "po-001", "status": "PASS"}
        )
        + "\n",
        encoding="utf-8",
    )
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps({"po-001": _entry(config, "po-001")}), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="unsupported primary-log JSON schema"):
        record_check(config, _pass("current"))


def test_canonical_v2_entry_is_idempotently_replaced(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    _, manifest = record_check(config, _pass("current"))
    record_check(
        config,
        CheckResult(
            "current",
            Status.FAIL_BEHAVIOR,
            "new contradiction",
            exit_code=1,
            command=("false",),
            command_provenance="fixture",
        ),
    )
    payload = json.loads(manifest.read_text())
    assert list(payload) == ["current"]
    assert payload["current"]["status"] == "FAIL_BEHAVIOR"


def test_complete_legacy_family_replacement_admits_only_viability(repository: Path):
    config = _configure(repository, "HDE-EPIC029")
    legacy_ids = ("po-epic-close-live-qa", "po-precommit", "po-postcommit")
    checks = {}
    for check_id in legacy_ids:
        path = config.qa_root / "checks" / check_id / "primary.log"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"[check_id] {check_id}\n[exit_code] 0\n", encoding="utf-8")
        checks[check_id] = _entry(config, check_id)
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps({"epic_id": config.epic_id, "checks": checks}), encoding="utf-8"
    )
    captured_env = (
        ("ALLOW_NETWORK", "0"),
        ("APP_ENV", "dev"),
        ("LANG", "C"),
        ("LC_ALL", "C"),
        ("SAFE_MODE", "1"),
        ("TZ", "UTC"),
    )
    results = [
        CheckResult(
            check_id,
            Status.PASS,
            exit_code=0,
            command=(("python", "-m", "pytest", "--version"), ("python", "check.py")),
            command_provenance="fresh requalification",
            captured_env=captured_env,
        )
        for check_id in legacy_ids
    ]
    results.append(_pass("acceptance-map-viability"))
    ledger = config.viability_ledger_path
    ledger_content = '{"status":"PASS"}\n'

    logs, manifest = record_check_family(
        config,
        results,
        additional_files=((ledger, ledger_content),),
        coherence_verifier=lambda: json.loads(ledger.read_text()),
        replace_legacy_family_ids=legacy_ids,
        admit_new_check_ids=("acceptance-map-viability",),
        captured_at_utc="2026-08-18T12:00:00Z",
    )

    assert set(json.loads(manifest.read_text())) == {
        *legacy_ids,
        "acceptance-map-viability",
    }
    assert ledger.read_text() == ledger_content
    for log in logs:
        header = read_primary_header(log)
        assert header["timestamp_utc"] == "2026-08-18T12:00:00Z"
    assert isinstance(read_primary_header(logs[0])["command"][0], list)
    assert read_primary_header(logs[0])["captured_env"] == dict(captured_env)


def test_complete_legacy_family_replacement_rejects_partial_fresh_family(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC029")
    legacy_ids = ("po-epic-close-live-qa", "po-precommit", "po-postcommit")
    checks = {}
    for check_id in legacy_ids:
        path = config.qa_root / "checks" / check_id / "primary.log"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("[exit_code] 0\n", encoding="utf-8")
        checks[check_id] = _entry(config, check_id)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(json.dumps({"epic_id": config.epic_id, "checks": checks}))
    before = manifest.read_bytes()
    with pytest.raises(ValueError, match="partial, extra"):
        record_check_family(
            config,
            [_pass(legacy_ids[0])],
            replace_legacy_family_ids=legacy_ids,
        )
    assert manifest.read_bytes() == before


def test_pass_with_intended_tokens_records_explicit_nonclaim(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    log, _ = record_check(
        config,
        CheckResult(
            "current",
            Status.PASS,
            exit_code=0,
            command=("true",),
            command_provenance="fixture",
            intended_tokens=(TOKEN,),
        ),
    )
    assert (
        "token_claim_posture: intended tokens are recorded but not claimed"
        in log.read_text()
    )


def test_pytest_collection_deduplicates_by_file_and_checks_exact_nodes(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text(
        "def test_one():\n    pass\n\ndef test_two():\n    pass\n", encoding="utf-8"
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        ci="pytest tests/test_sample.py::test_one; python -m pytest tests/test_sample.py::test_two",
    )
    calls = []

    class Done:
        returncode = 0
        stdout = "tests/test_sample.py::test_one\ntests/test_sample.py::test_two\n"
        stderr = ""

    def fake_run(command, **kwargs):
        calls.append((tuple(command), kwargs))
        return Done()

    for key, value in {
        "PYTEST_ADDOPTS": "--ignore=tests/test_sample.py",
        "PYTHONPATH": "/hostile/pythonpath",
        "PYTHONHOME": "/hostile/pythonhome",
        "PYTEST_PLUGINS": "hostile_plugin",
    }.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result, ledger = evaluate_acceptance_map_viability(config)
    assert result.status is Status.PASS
    assert len(calls) == 1
    assert calls[0][0][:8] == (
        calls[0][0][0],
        "-m",
        "pytest",
        "--collect-only",
        "-q",
        "-p",
        "no:cacheprovider",
        calls[0][0][7],
    )
    collection_env = calls[0][1]["env"]
    assert collection_env["PYTHONDONTWRITEBYTECODE"] == "1"
    assert {
        key: collection_env[key]
        for key in ("ALLOW_NETWORK", "LANG", "LC_ALL", "SAFE_MODE", "TZ")
    } == {
        "ALLOW_NETWORK": "0",
        "LANG": "C",
        "LC_ALL": "C",
        "SAFE_MODE": "1",
        "TZ": "UTC",
    }
    assert not {
        "PYTEST_ADDOPTS",
        "PYTHONPATH",
        "PYTHONHOME",
        "PYTEST_PLUGINS",
    } & collection_env.keys()
    assert result.command == calls[0][0]
    assert result.exit_code == 0
    assert json.loads(ledger)["resolved_reference_counts"]["matrix.ci_tests_jobs"] == 2


def test_collection_receipts_are_ordered_and_exclude_unlaunched_commands(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    for name in ("test_one.py", "test_two.py"):
        path = repository / "tests" / name
        path.parent.mkdir(exist_ok=True)
        path.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    config = _configure(
        repository,
        "HDE-EPIC039",
        ci="pytest tests/test_one.py; pytest tests/test_two.py",
    )
    calls: list[tuple[str, ...]] = []

    class Done:
        returncode = 0
        stderr = ""

        def __init__(self, test_file: str):
            self.stdout = f"{test_file}::test_ok\n"

    def fake_run(command, **kwargs):
        del kwargs
        frozen = tuple(command)
        calls.append(frozen)
        if len(calls) == 2:
            raise OSError("collection launch failed")
        return Done("tests/test_one.py")

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.FAIL_TOOLING
    assert result.command == calls[0]
    assert result.exit_code == 0


def test_collection_stops_on_controlling_failure_and_blocks_pending_requests(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    for name in ("test_one.py", "test_two.py", "test_three.py"):
        path = repository / "tests" / name
        path.parent.mkdir(exist_ok=True)
        path.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    config = _configure(
        repository,
        "HDE-EPIC039",
        ci="pytest tests/test_one.py; pytest tests/test_two.py",
    )
    governance = repository / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md"
    governance.write_text(
        governance.read_text(encoding="utf-8").replace(
            "## **2.1 Next**",
            "* **QA\\_HARNESS\\_ENTRYPOINT\\_SELFTEST\\_OK** — declared.\n"
            "## **2.1 Next**",
        ),
        encoding="utf-8",
    )
    acceptance = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    acceptance["tokens"].append(
        {
            "name": "QA_HARNESS_ENTRYPOINT_SELFTEST_OK",
            "owner_pf": "PF04",
            "status": "implemented",
            "evidence_titles": ["evidence/proof.json"],
        }
    )
    config.acceptance_map_path.write_text(json.dumps(acceptance), encoding="utf-8")
    config.token_matrix_path.write_text(
        config.token_matrix_path.read_text(encoding="utf-8")
        + _matrix_row(
            token="QA_HARNESS_ENTRYPOINT_SELFTEST_OK",
            ci="pytest tests/test_three.py",
        ),
        encoding="utf-8",
    )
    calls: list[tuple[str, ...]] = []

    class Done:
        def __init__(self, returncode: int, test_file: str):
            self.returncode = returncode
            self.stdout = (
                f"{test_file}::test_ok\n" if returncode == 0 else "collection error\n"
            )
            self.stderr = (
                "ImportError while importing test module" if returncode else ""
            )

    def fake_run(command, **kwargs):
        del kwargs
        frozen = tuple(command)
        calls.append(frozen)
        test_file = next(value for value in frozen if value.startswith("tests/"))
        return Done(2 if len(calls) == 2 else 0, test_file)

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result, ledger = evaluate_acceptance_map_viability(config)
    payload = json.loads(ledger)

    assert result.status is Status.FAIL_TOOLING
    assert result.command == tuple(calls)
    assert result.exit_code == 2
    assert len(calls) == 2
    assert (
        payload["token_status"]["QA_HARNESS_ENTRYPOINT_SELFTEST_OK"]
        == "TOOLING_BLOCKED"
    )
    pending = [
        item
        for item in payload["broken_references"]
        if item["token"] == "QA_HARNESS_ENTRYPOINT_SELFTEST_OK"
    ]
    assert len(pending) == 1
    assert pending[0]["status"] == "TOOLING_BLOCKED"
    assert "not executed after controlling FAIL_TOOLING" in pending[0]["reason"]


def test_exact_node_miss_stops_later_collection_requests(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    for name in ("test_one.py", "test_two.py"):
        path = repository / "tests" / name
        path.parent.mkdir(exist_ok=True)
        path.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    config = _configure(
        repository,
        "HDE-EPIC039",
        ci=(
            "pytest tests/test_one.py::test_missing; "
            "pytest tests/test_two.py"
        ),
    )
    calls: list[tuple[str, ...]] = []

    class Done:
        returncode = 0
        stdout = "tests/test_one.py::test_ok\n"
        stderr = ""

    def fake_run(command, **kwargs):
        del kwargs
        calls.append(tuple(command))
        return Done()

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result, ledger = evaluate_acceptance_map_viability(config)
    payload = json.loads(ledger)

    assert result.status is Status.TOOLING_BLOCKED
    assert result.command == calls[0]
    assert result.exit_code == 0
    assert len(calls) == 1
    reasons = [item["reason"] for item in payload["broken_references"]]
    assert any("pytest node was not collected exactly" in reason for reason in reasons)
    assert any(
        "not executed after controlling TOOLING_BLOCKED" in reason
        for reason in reasons
    )


def test_collection_launch_failure_before_completion_records_no_command(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    config = _configure(repository, "HDE-EPIC039", ci="pytest tests/test_sample.py")
    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run",
        lambda *args, **kwargs: (_ for _ in ()).throw(OSError("launch failed")),
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.FAIL_TOOLING
    assert result.command == ()
    assert result.exit_code is None


def test_bare_script_requires_executable_bit_but_python_form_does_not(
    repository: Path,
):
    script = repository / "tools/check.py"
    script.chmod(0o644)
    bare, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci="tools/check.py")
    )
    interpreted, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci="python tools/check.py")
    )
    script.chmod(0o755)
    executable, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci="tools/check.py")
    )
    assert bare.status is Status.TOOLING_BLOCKED
    assert "not executable" in bare.status_reason
    assert interpreted.status is Status.PASS
    assert executable.status is Status.PASS


@pytest.mark.parametrize(
    ("ci", "expected", "reason_fragment"),
    [
        (
            "pytest --definitely-invalid tests/test_sample.py",
            Status.TOOLING_BLOCKED,
            "unsupported option",
        ),
        (
            "pytest -k no_such_test tests/test_sample.py",
            Status.TOOLING_BLOCKED,
            "pytest file is unavailable",
        ),
    ],
)
def test_pytest_locator_options_are_preserved_during_collection(
    repository: Path,
    ci: str,
    expected: Status,
    reason_fragment: str,
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    result, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci=ci)
    )
    assert result.status is expected
    assert reason_fragment in result.status_reason
    if "-k" in ci:
        serialized = result.command
        if serialized and isinstance(serialized[0], tuple):
            flattened = " ".join(serialized[0])
        else:
            flattened = " ".join(serialized)
        assert "no_such_test" in flattened
    else:
        assert result.command == ()


def test_exact_node_locator_with_quiet_flag_uses_one_quiet_collection_command(
    repository: Path,
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text(
        "def test_exact():\n    pass\n\ndef test_other():\n    pass\n",
        encoding="utf-8",
    )
    result, _ = evaluate_acceptance_map_viability(
        _configure(
            repository,
            "HDE-EPIC039",
            ci="python -m pytest -q tests/test_sample.py::test_exact",
        )
    )

    assert result.status is Status.PASS
    assert result.command and isinstance(result.command[0], str)
    assert result.command.count("-q") == 1
    assert "--quiet" not in result.command
    assert result.command.count("--collect-only") == 1
    assert result.command[-1] == "tests/test_sample.py"


def test_collection_normalization_preserves_selector_options(
    repository: Path,
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text(
        "def test_exact():\n    pass\n\ndef test_other():\n    pass\n",
        encoding="utf-8",
    )
    result, _ = evaluate_acceptance_map_viability(
        _configure(
            repository,
            "HDE-EPIC039",
            ci=(
                "python -m pytest --quiet --collect-only -k test_exact "
                "-m 'not slow' -p no:cacheprovider "
                "tests/test_sample.py::test_exact"
            ),
        )
    )

    assert result.status is Status.PASS
    assert result.command and isinstance(result.command[0], str)
    assert result.command.count("-q") == 1
    assert "--quiet" not in result.command
    assert result.command.count("--collect-only") == 1
    assert result.command.count("-p") == 1
    assert result.command[result.command.index("-p") + 1] == "no:cacheprovider"
    assert result.command[result.command.index("-k") + 1] == "test_exact"
    marker_index = max(
        index for index, argument in enumerate(result.command) if argument == "-m"
    )
    assert result.command[marker_index + 1] == "not slow"


@pytest.mark.parametrize(
    "ci",
    [
        "pytest --ignore tests/test_sample.py tests/test_sample.py",
        "pytest --basetemp=/tmp/foreign tests/test_sample.py",
        "pytest -c /tmp/foreign.ini tests/test_sample.py",
        "pytest -p arbitrary_plugin tests/test_sample.py",
    ],
)
def test_pytest_locator_rejects_path_and_plugin_control_options(
    repository: Path, ci: str
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    result, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci=ci)
    )
    assert result.status is Status.TOOLING_BLOCKED
    assert "pytest locator" in result.status_reason


def test_missing_pytest_node_is_tooling_blocked(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("def test_one():\n    pass\n", encoding="utf-8")
    config = _configure(
        repository, "HDE-EPIC039", ci="pytest tests/test_sample.py::test_missing"
    )

    class Done:
        returncode = 0
        stdout = "tests/test_sample.py::test_one\n"
        stderr = ""

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.TOOLING_BLOCKED


def test_collection_import_failure_is_fail_tooling(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("raise RuntimeError('import')\n", encoding="utf-8")
    config = _configure(repository, "HDE-EPIC039", ci="pytest tests/test_sample.py")

    class Done:
        returncode = 2
        stdout = ""
        stderr = "ERROR collecting tests/test_sample.py"

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.FAIL_TOOLING


@pytest.mark.parametrize(
    ("locator", "expected"),
    [
        ("python tools/missing.py", Status.TOOLING_BLOCKED),
        ("pytest tests/missing.py::test_x", Status.TOOLING_BLOCKED),
        ("Existing epic-close output only", Status.TOOLING_BLOCKED),
        ("python <repository-script>", Status.TOOLING_BLOCKED),
    ],
)
def test_missing_or_prose_ci_locators_are_tooling_blocked(
    repository: Path, locator: str, expected: Status
):
    config = _configure(repository, "HDE-EPIC039", ci=locator)
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is expected


def test_cyclic_ci_script_alias_fails_causally(repository: Path):
    script = repository / "tools/loop.py"
    script.symlink_to(script.name)
    config = _configure(repository, "HDE-EPIC039", ci="python tools/loop.py")

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "command path cannot be resolved safely" in result.status_reason


@pytest.mark.parametrize(
    ("locator", "expected"),
    [
        ("audit/qa/hde-epic028/checks/other/primary.log", Status.FAIL_BEHAVIOR),
        ("../escape.log", Status.FAIL_BEHAVIOR),
        ("checks/<run-id>/primary.log", Status.TOOLING_BLOCKED),
        ("checks/missing/primary.log", Status.TOOLING_BLOCKED),
    ],
)
def test_invalid_qa_locators_fail_causally(
    repository: Path, locator: str, expected: Status
):
    config = _configure(repository, "HDE-EPIC039", qa=locator)
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is expected


def test_cyclic_qa_locator_alias_fails_causally(repository: Path):
    qa_log = repository / "audit/qa/hde-epic039/checks/loop/primary.log"
    qa_log.parent.mkdir(parents=True, exist_ok=True)
    qa_log.symlink_to(qa_log.name)
    config = _configure(repository, "HDE-EPIC039", qa="checks/loop/primary.log")

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "QA locator cannot be resolved safely" in result.status_reason


def test_declared_planned_qa_output_is_valid(repository: Path):
    config = _configure(
        repository,
        "HDE-EPIC039",
        qa="checks/future-step/primary.log",
        step_names=("future-step",),
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.PASS


def test_existing_unindexed_qa_log_cannot_pass(repository: Path):
    qa_log = repository / "audit/qa/hde-epic039/checks/arbitrary/primary.log"
    qa_log.parent.mkdir(parents=True, exist_ok=True)
    qa_log.write_text("arbitrary nonempty bytes\n", encoding="utf-8")
    config = _configure(
        repository,
        "HDE-EPIC039",
        qa="checks/arbitrary/primary.log",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.TOOLING_BLOCKED
    assert "absent from the Human Index and Machine Mirror" in result.status_reason


def test_existing_governed_qa_log_can_pass(repository: Path):
    qa_path = "audit/qa/hde-epic039/checks/governed/primary.log"
    qa_log = repository / qa_path
    qa_log.parent.mkdir(parents=True, exist_ok=True)
    qa_log.write_text("governed QA receipt\n", encoding="utf-8")
    _write_evidence_graph(
        repository,
        {
            "evidence/proof.json": ("fixture.primary_evidence",),
            qa_path: ("fixture.qa_log",),
        },
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        qa="checks/governed/primary.log",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.PASS


def test_existing_governed_qa_log_is_rechecked_before_pass(
    repository: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    qa_path = "audit/qa/hde-epic039/checks/governed/primary.log"
    qa_log = repository / qa_path
    qa_log.parent.mkdir(parents=True, exist_ok=True)
    qa_log.write_text("governed QA receipt\n", encoding="utf-8")
    _write_evidence_graph(
        repository,
        {
            "evidence/proof.json": ("fixture.primary_evidence",),
            qa_path: ("fixture.qa_log",),
        },
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        qa="checks/governed/primary.log",
    )
    original_apply = qa_harness._apply_pytest_collection

    def mutate_after_collection(*args: object, **kwargs: object):
        receipts = original_apply(*args, **kwargs)
        qa_log.write_text("changed QA receipt\n", encoding="utf-8")
        return receipts

    monkeypatch.setattr(
        qa_harness,
        "_apply_pytest_collection",
        mutate_after_collection,
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "acceptance evidence changed during evaluation" in result.status_reason


def test_governed_ledger_self_output_requires_explicit_publication_plan(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC039", qa="acceptance_map_viability.log")
    blocked, _ = evaluate_acceptance_map_viability(config)
    planned, _ = evaluate_acceptance_map_viability(config, planned_governed_ledger=True)
    assert blocked.status is Status.TOOLING_BLOCKED
    assert blocked.evidence_artifacts == ()
    assert planned.status is Status.PASS
    assert planned.evidence_artifacts == (
        "audit/qa/hde-epic039/acceptance_map_viability.log",
    )


def test_referenced_manifest_with_broken_nested_log_is_fail_tooling(repository: Path):
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("audit/qa/hde-epic039/qa_step_logs_manifest.json",),
        evidence="audit/qa/hde-epic039/qa_step_logs_manifest.json",
    )
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "broken": {
                    "check_id": "broken",
                    "log_path": "checks/broken/primary.log",
                    "status": "PASS",
                }
            }
        ),
        encoding="utf-8",
    )
    result, ledger = evaluate_acceptance_map_viability(config)
    payload = json.loads(ledger)
    assert result.status is Status.FAIL_TOOLING
    assert payload["referenced_manifests"] == [
        "audit/qa/hde-epic039/qa_step_logs_manifest.json"
    ]
    assert payload["broken_references"]


def test_post_write_coherence_failure_restores_every_preimage(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    original_manifest = json.dumps({"epic_id": config.epic_id, "runs": []})
    manifest.write_text(original_manifest, encoding="utf-8")
    additional = config.qa_root / "acceptance_map_viability.log"
    additional.write_text("old ledger\n", encoding="utf-8")

    def reject() -> None:
        raise RuntimeError("post-write coherence failed")

    with pytest.raises(RuntimeError, match="post-write coherence failed"):
        record_check_family(
            config,
            (_pass("one"), _pass("two")),
            additional_files=((additional, "new ledger\n"),),
            coherence_verifier=reject,
        )
    assert manifest.read_text() == original_manifest
    assert additional.read_text() == "old ledger\n"
    assert not (config.qa_root / "checks/one/primary.log").exists()
    assert not (config.qa_root / "checks/two/primary.log").exists()


def test_empty_preimage_is_restored_after_publication_failure(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps({"epic_id": config.epic_id, "runs": []}))
    additional = config.qa_root / "acceptance_map_viability.log"
    additional.write_bytes(b"")

    with pytest.raises(RuntimeError, match="reject staged family"):
        record_check_family(
            config,
            (_pass("current"),),
            additional_files=((additional, "replacement\n"),),
            coherence_verifier=lambda: (_ for _ in ()).throw(
                RuntimeError("reject staged family")
            ),
        )

    assert additional.exists() and additional.read_bytes() == b""
    assert not (config.qa_root / "checks/current/primary.log").exists()


def test_publication_rejects_symlink_output_without_mutation(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps({"epic_id": config.epic_id, "runs": []}))
    outside = repository / "outside.log"
    outside.write_text("protected\n", encoding="utf-8")
    primary = config.qa_root / "checks/current/primary.log"
    primary.parent.mkdir(parents=True)
    primary.symlink_to(outside)

    with pytest.raises(ValueError, match="cannot be a symlink"):
        record_check(config, _pass("current"))

    assert primary.is_symlink()
    assert outside.read_text(encoding="utf-8") == "protected\n"
    assert json.loads(manifest.read_text(encoding="utf-8")) == {
        "epic_id": config.epic_id,
        "runs": [],
    }


def test_flat_v2_status_mismatch_fails_before_any_write(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    current_log, manifest = record_check(config, _pass("current"))
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["current"]["status"] = "FAIL_BEHAVIOR"
    manifest.write_text(json.dumps(payload), encoding="utf-8")
    before_manifest = manifest.read_bytes()
    before_log = current_log.read_bytes()

    with pytest.raises(ValueError, match="status disagrees"):
        record_check(config, _pass("new"))

    assert manifest.read_bytes() == before_manifest
    assert current_log.read_bytes() == before_log
    assert not (config.qa_root / "checks/new/primary.log").exists()


def test_flat_v2_legacy_pf_ref_fails_before_any_write(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    current_log, manifest = record_check(config, _pass("current"))
    lines = current_log.read_text(encoding="utf-8").splitlines()
    header = json.loads(lines[0])
    header["pf_refs"] = ["PF19 §4.4"]
    current_log.write_text(
        json.dumps(header, sort_keys=True, separators=(",", ":"))
        + "\n"
        + "\n".join(lines[1:])
        + ("\n" if len(lines) > 1 else ""),
        encoding="utf-8",
    )
    before_manifest = manifest.read_bytes()

    with pytest.raises(ValueError, match="exact in-document PF titles"):
        record_check(config, _pass("new"))

    assert manifest.read_bytes() == before_manifest
    assert not (config.qa_root / "checks/new/primary.log").exists()


@pytest.mark.parametrize(
    "kwargs",
    [
        {"command": ("true",), "exit_code": None},
        {"command": (), "exit_code": 0},
        {"command": ("true",), "exit_code": True},
    ],
)
def test_check_result_rejects_command_exit_contradictions(kwargs: dict[str, object]):
    with pytest.raises(ValueError, match="exit_code|command execution"):
        CheckResult("invalid", Status.FAIL_TOOLING, "invalid receipt", **kwargs)


def test_check_result_rejects_section_qualified_pf_aliases():
    with pytest.raises(ValueError, match="exact in-document PF titles"):
        CheckResult(
            "invalid-pf-ref",
            Status.FAIL_TOOLING,
            "invalid receipt",
            pf_refs=("PF19 — Glow QA Guide §4.4",),
        )


def test_unmocked_epic027_viability_wrapper_uses_shared_evaluator(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    from tools.qa import generate_epic027_close_pack as module

    config = _configure(
        repository,
        "HDE-EPIC027",
        qa="acceptance_map_viability.log",
        step_names=("acceptance_map_viability",),
    )
    monkeypatch.setattr(module, "ROOT", repository)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", config.viability_ledger_path)
    module._write_viability_log()
    assert config.viability_ledger_path.is_file()
    payload = json.loads((config.qa_root / "qa_step_logs_manifest.json").read_text())
    assert payload["acceptance-map-viability"]["status"] == "PASS"
