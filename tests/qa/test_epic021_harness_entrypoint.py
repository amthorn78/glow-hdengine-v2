import hashlib
import json
from pathlib import Path

import pytest

from tools.qa import epic021_qa
from tools.qa.epic021_qa import run_epic021_qa
from tools.qa.qa_harness import Status

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
