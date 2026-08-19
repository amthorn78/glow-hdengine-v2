import hashlib
import json
from pathlib import Path

import pytest

from tools.qa import epic021_qa
from tools.evidence import run_sanity_pipeline
from tools.qa.epic021_qa import run_epic021_qa
from tools.qa.qa_harness import HarnessConfig, Status

CLOSED_RAILS = {
    "ALLOW_NETWORK": "0",
    "LANG": "C",
    "LC_ALL": "C",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}


@pytest.fixture(autouse=True)
def enforce_closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in CLOSED_RAILS.items():
        monkeypatch.setenv(key, value)


def _repo(root: Path) -> None:
    (root / "docs/pfcanon").mkdir(parents=True)
    (root / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md").write_text(
        "## **2.0 Acceptance Tokens (single-home roster)**\n"
        "* **QA_HARNESS_DISCIPLINE_OK** — registered.\n"
        "## **2.1 Next**\n",
        encoding="utf-8",
    )
    (root / "docs").mkdir(exist_ok=True)
    (root / "docs/acceptance_map_epic021.json").write_text(
        json.dumps(
            {
                "epic_id": "HDE-EPIC021",
                "tokens": [
                    {
                        "evidence_titles": ["proof.txt"],
                        "name": "QA_HARNESS_DISCIPLINE_OK",
                        "owner_pf": "PF04",
                        "status": "implemented",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    qa = root / "audit/qa/hde-epic021"
    qa.mkdir(parents=True)
    evidence = root / "proof.txt"
    evidence.write_text("proof\n", encoding="utf-8")
    digest = hashlib.sha256(evidence.read_bytes()).hexdigest()
    timestamp = "2026-01-01T00:00:00Z"
    (root / "proof.txt.path_proof.txt").write_text(
        "\n".join(
            (
                "path: proof.txt",
                f"size_bytes: {evidence.stat().st_size}",
                f"sha256: {digest}",
                f"mtime_utc: {timestamp}",
                f"produced_at_utc: {timestamp}",
                "",
            )
        ),
        encoding="utf-8",
    )
    human_rows = [
        {
            "artifact_key": "fixture.epic021_proof",
            "discovered_physical_path": "proof.txt",
        }
    ]
    mirror_rows = [
        {
            "artifact_key": "fixture.epic021_proof",
            "discovered_physical_path": "proof.txt",
            "produced_at_utc": timestamp,
            "proof_anchor": "proof.txt.path_proof.txt",
            "role": "snapshot",
            "sha256": digest,
            "size_bytes": evidence.stat().st_size,
        }
    ]
    body_bytes = b"".join(
        (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode()
        for row in mirror_rows
    )
    body_digest = hashlib.sha256(body_bytes).hexdigest()
    self_record = {
        "artifact_key": "index.machine_mirror",
        "discovered_physical_path": "artifacts/evidence_index.jsonl",
        "produced_at_utc": timestamp,
        "proof_anchor": "artifacts/evidence_index.jsonl.path_proof.txt",
        "role": "self_record",
        "sha256": body_digest,
        "size_bytes": 0,
    }
    mirror_rows.append(self_record)
    mirror_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    while True:
        mirror_bytes = b"".join(
            (
                json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
            ).encode()
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
    mirror.parent.mkdir(parents=True)
    mirror.write_bytes(mirror_bytes)
    (root / "artifacts/evidence_index.jsonl.path_proof.txt").write_text(
        "\n".join(
            (
                "path: artifacts/evidence_index.jsonl",
                f"size_bytes: {len(mirror_bytes)}",
                f"sha256: {hashlib.sha256(mirror_bytes).hexdigest()}",
                f"mirror_body_sha256: {body_digest}",
                f"mtime_utc: {timestamp}",
                f"produced_at_utc: {timestamp}",
                "",
            )
        ),
        encoding="utf-8",
    )
    (qa / "token_evidence_matrix.md").write_text(
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        "| QA_HARNESS_DISCIPLINE_OK | PF04 | proof.txt | "
        "python -m pytest -q tests/qa/test_epic021_scaffolding.py | "
        "checks/d00-bootstrap/primary.log | Implemented | fixture |\n",
        encoding="utf-8",
    )
    tests = root / "tests/qa"
    tests.mkdir(parents=True)
    (tests / "test_epic021_scaffolding.py").write_text(
        "def test_scaffold():\n    assert True\n", encoding="utf-8"
    )


def test_wrapper_delegates_to_current_state_harness(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    _repo(tmp_path)
    assert epic021_qa.ensure_determinism_env() == CLOSED_RAILS

    class Done:
        returncode = 0
        stdout = "passed"
        stderr = ""

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    result = run_epic021_qa(repo_root=tmp_path)
    assert result["bootstrap"].status is Status.PASS
    assert result["viability"].status is Status.PASS
    manifest = json.loads(
        (
            tmp_path / "audit/qa/hde-epic021/qa_step_logs_manifest.json"
        ).read_text()
    )
    assert set(manifest) == {"d00-bootstrap", "acceptance-map-viability"}
    assert "run_id" not in json.dumps(manifest)
    ledger = tmp_path / "audit/qa/hde-epic021/acceptance_map_viability.log"
    assert result["governed_ledger"] == ledger
    assert result["viability"].governed_ledger == ledger
    assert json.loads(ledger.read_text(encoding="utf-8"))["status"] == "PASS"

    # The legacy ID is absent after the first publication. A current-state
    # wrapper must remain safely repeatable rather than treating that absence
    # as a migration error.
    repeated = run_epic021_qa(repo_root=tmp_path)
    assert repeated["bootstrap"].status is Status.PASS
    assert repeated["viability"].status is Status.PASS
    repeated_manifest = json.loads(
        (
            tmp_path / "audit/qa/hde-epic021/qa_step_logs_manifest.json"
        ).read_text(encoding="utf-8")
    )
    assert set(repeated_manifest) == {"d00-bootstrap", "acceptance-map-viability"}


@pytest.mark.parametrize("posture", ("unset", "open"))
def test_imported_wrapper_rejects_invalid_rails_before_execution_or_write(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    posture: str,
):
    _repo(tmp_path)
    if posture == "unset":
        for key in CLOSED_RAILS:
            monkeypatch.delenv(key, raising=False)
    else:
        monkeypatch.setenv("SAFE_MODE", "0")
        monkeypatch.setenv("ALLOW_NETWORK", "1")

    before = {
        path.relative_to(tmp_path).as_posix(): path.read_bytes()
        for path in tmp_path.rglob("*")
        if path.is_file()
    }
    observed: list[str] = []

    def forbidden(boundary: str) -> None:
        observed.append(boundary)
        raise AssertionError(f"invalid rails crossed {boundary} boundary")

    monkeypatch.setattr(
        epic021_qa.qa_harness.subprocess,
        "run",
        lambda *_args, **_kwargs: forbidden("subprocess"),
    )
    monkeypatch.setattr(
        epic021_qa.qa_harness,
        "record_check",
        lambda *_args, **_kwargs: forbidden("governed-write"),
    )

    with pytest.raises(epic021_qa.DeterminismEnvError, match="env pins mismatch"):
        run_epic021_qa(repo_root=tmp_path)

    after = {
        path.relative_to(tmp_path).as_posix(): path.read_bytes()
        for path in tmp_path.rglob("*")
        if path.is_file()
    }
    assert observed == []
    assert after == before


def test_wrapper_never_creates_checkout_qa_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    _repo(tmp_path)
    before = {
        path.as_posix() for path in Path("audit/qa").rglob("*") if path.is_file()
    }

    class Done:
        returncode = 0
        stdout = "passed"
        stderr = ""

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    run_epic021_qa(repo_root=tmp_path)
    after = {
        path.as_posix() for path in Path("audit/qa").rglob("*") if path.is_file()
    }
    assert after == before


def test_outer_transaction_restores_bytes_modes_and_new_targets(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    existing = tmp_path / "existing.log"
    created = tmp_path / "nested/new.log"
    existing.write_bytes(b"before\n")
    existing.chmod(0o640)
    monkeypatch.setattr(epic021_qa, "ROOT", tmp_path)
    monkeypatch.setattr(
        epic021_qa, "_wrapper_write_paths", lambda: (existing, created)
    )

    with pytest.raises(RuntimeError, match="injected"):
        with epic021_qa._WrapperWriteTransaction():
            existing.write_bytes(b"after\n")
            existing.chmod(0o600)
            created.parent.mkdir(parents=True)
            created.write_bytes(b"new\n")
            raise RuntimeError("injected")

    assert existing.read_bytes() == b"before\n"
    assert existing.stat().st_mode & 0o777 == 0o640
    assert not created.exists()
    assert not created.parent.exists()


def test_main_rolls_back_input_writes_when_finalization_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    first = tmp_path / "acceptance.json"
    second = tmp_path / "matrix.md"
    first.write_bytes(b"old acceptance\n")
    second.write_bytes(b"old matrix\n")
    monkeypatch.setattr(epic021_qa, "ROOT", tmp_path)
    monkeypatch.setattr(
        epic021_qa, "_wrapper_write_paths", lambda: (first, second)
    )
    monkeypatch.setattr(epic021_qa, "ensure_determinism_env", lambda **_kwargs: None)

    def write_inputs() -> None:
        first.write_bytes(b"new acceptance\n")
        second.write_bytes(b"new matrix\n")

    monkeypatch.setattr(epic021_qa, "_write_acceptance_inputs", write_inputs)
    monkeypatch.setattr(epic021_qa, "_write_close_pack", lambda _timestamp: None)
    monkeypatch.setattr(
        epic021_qa,
        "_execute_current_family",
        lambda: (_ for _ in ()).throw(RuntimeError("updater failed")),
    )

    assert epic021_qa.main() == 1
    assert first.read_bytes() == b"old acceptance\n"
    assert second.read_bytes() == b"old matrix\n"


def test_fresh_postcommit_is_sealed_before_viability_and_failure_rolls_back(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    graph_state = tmp_path / "graph-state.txt"
    graph_state.write_bytes(b"before\n")
    events: list[str] = []
    graph_writes = 0

    def passed(check_id: str) -> epic021_qa.qa_harness.CheckResult:
        return epic021_qa.qa_harness.CheckResult(
            check_id=check_id,
            status=Status.PASS,
        )

    def record_check(_config, result, **_kwargs):
        events.append(f"record:{result.check_id}:{result.status.value}")
        if result.check_id == "po-postcommit" and result.status is Status.PASS:
            graph_state.write_bytes(b"fresh postcommit\n")
        return tmp_path / "primary.log", tmp_path / "manifest.json"

    def write_graph() -> None:
        nonlocal graph_writes
        graph_writes += 1
        events.append(f"write-graph:{graph_writes}")
        if graph_writes == 3:
            graph_state.write_bytes(b"fresh postcommit sealed\n")

    def verify_graph() -> None:
        events.append(f"verify-graph:{graph_writes}")
        if graph_writes == 3:
            raise RuntimeError("injected postcommit graph verification failure")

    def evaluate_viability(*_args, **_kwargs):
        events.append("viability")
        raise AssertionError("viability ran before the postcommit graph seal")

    monkeypatch.setattr(epic021_qa, "ROOT", tmp_path)
    monkeypatch.setattr(
        epic021_qa, "_wrapper_write_paths", lambda: (graph_state,)
    )
    monkeypatch.setattr(
        epic021_qa.qa_harness,
        "run_pytest_check",
        lambda _config, check_id, *_args, **_kwargs: passed(check_id),
    )
    monkeypatch.setattr(
        epic021_qa,
        "_tooling_classification_result",
        lambda **_kwargs: passed("bootstrap-tooling-classification"),
    )
    monkeypatch.setattr(
        epic021_qa,
        "_precommit_result",
        lambda **_kwargs: passed("po-precommit"),
    )
    monkeypatch.setattr(
        epic021_qa,
        "_live_qa_result",
        lambda **_kwargs: passed("po-epic021-live-qa"),
    )
    monkeypatch.setattr(
        epic021_qa,
        "_postcommit_result",
        lambda **_kwargs: (passed("po-postcommit"), b"sanity\n"),
    )
    monkeypatch.setattr(epic021_qa.qa_harness, "record_check", record_check)
    monkeypatch.setattr(epic021_qa, "_write_graph", write_graph)
    monkeypatch.setattr(epic021_qa, "_verify_graph", verify_graph)
    monkeypatch.setattr(
        epic021_qa.qa_harness,
        "generate_acceptance_map_viability",
        evaluate_viability,
    )

    with pytest.raises(
        RuntimeError, match="injected postcommit graph verification failure"
    ):
        with epic021_qa._WrapperWriteTransaction():
            epic021_qa._execute_current_family()

    postcommit = events.index("record:po-postcommit:PASS")
    assert events[postcommit:] == [
        "record:po-postcommit:PASS",
        "write-graph:3",
        "verify-graph:3",
    ]
    assert "viability" not in events
    assert graph_state.read_bytes() == b"before\n"


def test_controlled_tooling_probe_uses_actual_pytest_cause():
    result = epic021_qa._tooling_classification_result()
    assert result.status is Status.PASS
    assert result.exit_code == 0
    assert len(result.command) == 2
    assert result.command[0][-1] == epic021_qa.TOOLING_CLASSIFICATION_FIXTURE
    assert "ModuleNotFoundError" in result.output
    assert "_epic021_deliberately_missing_dependency" in result.output
    assert "summary:FAIL_TOOLING" in epic021_qa.CONTROLLED_TOOLING_FAILURE_CONTENT
    assert (
        "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC"
        in epic021_qa.CONTROLLED_TOOLING_FAILURE_CONTENT
    )


def test_precommit_env_pin_failure_is_tooling_causal(
    monkeypatch: pytest.MonkeyPatch,
):
    receipt = epic021_qa._CommandReceipt(
        epic021_qa.PRECOMMIT_COMMANDS[0],
        1,
        "",
        "mismatched rail",
    )
    monkeypatch.setattr(epic021_qa, "_run_commands", lambda *_args, **_kwargs: (receipt,))
    result = epic021_qa._precommit_result()
    assert result.status is Status.FAIL_TOOLING
    assert result.status_reason == "environment-pins gate failed"


def test_main_rejects_open_rails_before_any_write(monkeypatch: pytest.MonkeyPatch):
    writes: list[str] = []
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setattr(
        epic021_qa,
        "_write_acceptance_inputs",
        lambda: writes.append("inputs"),
    )
    assert epic021_qa.main() == 1
    assert writes == []


def test_transient_narrative_mounts_are_removed(tmp_path: Path):
    catalog = tmp_path / "catalog/narratives"
    catalog.mkdir(parents=True)
    (catalog / "manifest.json").write_text("{}\n", encoding="utf-8")
    (catalog / "manifest.json.sha256").write_text("digest\n", encoding="utf-8")
    mount_root = tmp_path / "narratives"
    mount_root.mkdir()
    retained = mount_root / ("a" * 64)
    retained.mkdir()

    with epic021_qa._TransientNarrativeMounts(tmp_path):
        created = mount_root / ("b" * 64)
        created.mkdir()
        (created / "manifest.json").write_text("{}\n", encoding="utf-8")
        (created / "manifest.json.sha256").write_text(
            "digest\n", encoding="utf-8"
        )

    assert retained.is_dir()
    assert not created.exists()


def test_sanity_failure_is_behavior_causal_but_malformed_is_tooling():
    failure = run_sanity_pipeline.STAGE_NAMES[2]
    results = []
    for index, name in enumerate(run_sanity_pipeline.STAGE_NAMES):
        if index < 2:
            status = "OK"
        elif index == 2:
            status = "FAIL"
        else:
            status = f"NOT_EXECUTED_EARLIER_FAILURE:{failure}"
        results.append((name, status))
    payload = run_sanity_pipeline._render_log(results, failure, "FAIL")

    status, reason = epic021_qa._sanity_status(payload)
    assert status is Status.FAIL_BEHAVIOR
    assert failure in reason
    assert epic021_qa._sanity_status(None)[0] is Status.FAIL_TOOLING
    assert epic021_qa._sanity_status(b"malformed\n")[0] is Status.FAIL_TOOLING


def test_close_pack_names_required_rails_and_same_run_receipts():
    captured_at = "2026-08-18T00:00:00Z"
    manifest = json.loads(epic021_qa._close_manifest_content(captured_at))
    report = epic021_qa._close_report_content(captured_at)

    assert "## Acceptance and evidence pointers" in report
    assert "## QA Rails — Open/Close (Final PR)" in report
    required_outputs = {
        "acceptance_map": "docs/acceptance_map_epic021.json",
        "token_matrix": "audit/qa/hde-epic021/token_evidence_matrix.md",
        "acceptance_viability": (
            "audit/qa/hde-epic021/acceptance_map_viability.log"
        ),
        "step_logs_manifest": (
            "audit/qa/hde-epic021/qa_step_logs_manifest.json"
        ),
        "doc_deltas": "audit/docdeltas/hde-epic021_doc_deltas.md",
        "close_report": "audit/EPIC-021_close_report.md",
        "close_manifest": "audit/EPIC-021_MANIFEST.json",
    }
    assert {
        key: manifest["key_outputs"][key] for key in required_outputs
    } == required_outputs
    assert not (
        epic021_qa.RETIRED_CLOSE_OUTPUT_KEYS & manifest["key_outputs"].keys()
    )
    expected_logs = {
        "qa_log_acceptance_map_viability": (
            "audit/qa/hde-epic021/checks/acceptance-map-viability/primary.log"
        ),
        "qa_log_bootstrap": (
            "audit/qa/hde-epic021/checks/d00-bootstrap/primary.log"
        ),
        "qa_log_bootstrap_tooling_classification": (
            "audit/qa/hde-epic021/checks/"
            "bootstrap-tooling-classification/primary.log"
        ),
        "qa_log_live_qa": (
            "audit/qa/hde-epic021/checks/po-epic021-live-qa/primary.log"
        ),
        "qa_log_postcommit": (
            "audit/qa/hde-epic021/checks/po-postcommit/primary.log"
        ),
        "qa_log_precommit": (
            "audit/qa/hde-epic021/checks/po-precommit/primary.log"
        ),
    }
    assert {
        key: manifest["key_outputs"][key] for key in expected_logs
    } == expected_logs

    assert manifest["tokens"] == epic021_qa._manifest_token_records()
    assert [record["name"] for record in manifest["tokens"]] == sorted(
        token["name"] for token in epic021_qa.TOKENS
    )
    assert all(
        set(record)
        == {
            "ci_tests_jobs",
            "evidence_artifacts",
            "name",
            "owner_pf",
            "qa_root_logs",
            "status",
        }
        for record in manifest["tokens"]
    )


def _acceptance_lockstep_fixture(
    tmp_path: Path,
) -> tuple[dict[str, object], dict[str, object], Path, Path]:
    acceptance_map = tmp_path / "acceptance_map.json"
    token_matrix = tmp_path / "token_evidence_matrix.md"
    acceptance_map.write_text(epic021_qa._acceptance_map_content(), encoding="utf-8")
    token_matrix.write_text(epic021_qa._token_matrix_content(), encoding="utf-8")
    manifest = json.loads(epic021_qa._close_manifest_content("2026-08-18T00:00:00Z"))
    disposition = {token["name"]: "VALID" for token in epic021_qa.TOKENS}
    viability = {
        "acceptance_map_path": "docs/acceptance_map_epic021.json",
        "epic_id": epic021_qa.EPIC_ID,
        "token_reference_disposition": dict(disposition),
        "token_status": dict(disposition),
    }
    return manifest, viability, acceptance_map, token_matrix


def _validate_fixture_lockstep(
    manifest: dict[str, object],
    viability: dict[str, object],
    acceptance_map: Path,
    token_matrix: Path,
) -> None:
    epic021_qa._validate_acceptance_lockstep(
        manifest,
        viability,
        acceptance_map_bytes=acceptance_map.read_bytes(),
        token_matrix_bytes=token_matrix.read_bytes(),
        token_matrix_path=token_matrix,
    )


def test_close_acceptance_bindings_validate_exact_lockstep(tmp_path: Path):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )

    _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


@pytest.mark.parametrize("mutation", ("omission", "extra", "substitution"))
def test_close_manifest_rejects_nonexact_token_roster(tmp_path: Path, mutation: str):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )
    records = manifest["tokens"]
    assert isinstance(records, list)
    if mutation == "omission":
        records.pop()
    elif mutation == "extra":
        extra = dict(records[-1])
        extra["name"] = "ZZZ_EPIC021_EXTRA_TOKEN_OK"
        records.append(extra)
    else:
        records[0]["name"] = "AAA_EPIC021_SUBSTITUTED_TOKEN_OK"

    with pytest.raises(ValueError, match="token rosters disagree"):
        _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


def test_close_manifest_rejects_token_evidence_contradiction(tmp_path: Path):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )
    records = manifest["tokens"]
    assert isinstance(records, list)
    records[0]["evidence_artifacts"] = ["contradictory-proof.txt"]

    with pytest.raises(ValueError, match="matrix and close manifest records disagree"):
        _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


def test_close_manifest_rejects_map_matrix_evidence_contradiction(tmp_path: Path):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )
    lines = token_matrix.read_text(encoding="utf-8").splitlines()
    token_name = epic021_qa.TOKENS[0]["name"]
    for index, line in enumerate(lines):
        if line.startswith(f"| {token_name} |"):
            cells = line.split("|")
            cells[3] = " contradictory-proof.txt "
            lines[index] = "|".join(cells)
            break
    else:  # pragma: no cover - canonical fixture invariant
        raise AssertionError(f"missing matrix row: {token_name}")
    token_matrix.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="map and token matrix bindings disagree"):
        _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


def test_close_manifest_rejects_map_matrix_status_contradiction(tmp_path: Path):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )
    payload = json.loads(acceptance_map.read_text(encoding="utf-8"))
    payload["tokens"][0]["status"] = "planned"
    acceptance_map.write_text(
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="map and token matrix bindings disagree"):
        _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


@pytest.mark.parametrize(
    ("field", "replacement"),
    (
        ("status", "planned"),
        ("ci_tests_jobs", ["python -m pytest contradictory_test.py"]),
        ("qa_root_logs", ["checks/contradictory/primary.log"]),
    ),
)
def test_close_manifest_rejects_status_test_and_qa_binding_drift(
    tmp_path: Path, field: str, replacement: object
):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )
    records = manifest["tokens"]
    assert isinstance(records, list)
    records[0][field] = replacement

    with pytest.raises(ValueError, match="matrix and close manifest records disagree"):
        _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


def test_close_manifest_rejects_duplicate_token_records(tmp_path: Path):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )
    records = manifest["tokens"]
    assert isinstance(records, list)
    records.append(dict(records[-1]))

    with pytest.raises(ValueError, match="invalid name"):
        _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


@pytest.mark.parametrize("field", ("token_status", "token_reference_disposition"))
@pytest.mark.parametrize("mutation", ("omission", "substitution"))
def test_close_manifest_rejects_nonexact_viability_token_keys(
    tmp_path: Path, field: str, mutation: str
):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )
    dispositions = viability[field]
    assert isinstance(dispositions, dict)
    removed = next(iter(dispositions))
    dispositions.pop(removed)
    if mutation == "substitution":
        dispositions["EPIC021_SUBSTITUTED_TOKEN_OK"] = "VALID"

    with pytest.raises(ValueError, match=field):
        _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


@pytest.mark.parametrize(
    ("field", "replacement", "message"),
    (
        ("epic_id", "HDE-EPIC999", "epic identity"),
        (
            "acceptance_map_path",
            "docs/acceptance_map_epic999.json",
            "acceptance_map_path",
        ),
    ),
)
def test_close_manifest_rejects_wrong_viability_identity(
    tmp_path: Path, field: str, replacement: str, message: str
):
    manifest, viability, acceptance_map, token_matrix = _acceptance_lockstep_fixture(
        tmp_path
    )
    viability[field] = replacement

    with pytest.raises(ValueError, match=message):
        _validate_fixture_lockstep(manifest, viability, acceptance_map, token_matrix)


def test_close_input_capture_rejects_symlink_alias(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    target = tmp_path / "manifest-target.json"
    target.write_text("{}\n", encoding="utf-8")
    alias = tmp_path / "manifest.json"
    alias.symlink_to(target.name)
    monkeypatch.setattr(epic021_qa, "ROOT", tmp_path)

    with pytest.raises(ValueError, match="cannot be captured safely"):
        epic021_qa._capture_close_input(alias, subject="test close manifest")



def test_doc_delta_pair_is_byte_identical_and_pf_referenced():
    primary = Path("audit/docdeltas/hde-epic021_doc_deltas.md").read_bytes()
    capture = Path("audit/qa/hde-epic021/00_meta/doc_deltas.md").read_bytes()
    assert primary == capture
    assert b"PF14" in primary
    assert b"PF06" in primary


def test_only_lowercase_bootstrap_is_current_authority():
    checks = Path("audit/qa/hde-epic021/checks")
    assert (checks / "d00-bootstrap/primary.log").is_file()
    assert not (checks / "D00_bootstrap").exists()
