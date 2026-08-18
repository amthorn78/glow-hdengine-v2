import json
from pathlib import Path

import pytest

from tools.qa.epic021_qa import run_epic021_qa
from tools.qa.qa_harness import Status


def _repo(root: Path) -> None:
    (root / "docs/pfcanon").mkdir(parents=True)
    (root / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md").write_text("## **2.0 Acceptance Tokens (single-home roster)**\n* **QA_HARNESS_DISCIPLINE_OK** — registered.\n## **2.1 Next**\n", encoding="utf-8")
    (root / "docs").mkdir(exist_ok=True)
    (root / "docs/acceptance_map_epic021.json").write_text(json.dumps({"epic_id": "HDE-EPIC021", "tokens": [{"name": "QA_HARNESS_DISCIPLINE_OK"}]}), encoding="utf-8")
    qa = root / "audit/qa/hde-epic021"
    qa.mkdir(parents=True)
    (root / "proof.txt").write_text("proof\n", encoding="utf-8")
    (qa / "token_evidence_matrix.md").write_text("| token_name | owner | evidence_artifacts |\n| --- | --- | --- |\n| QA_HARNESS_DISCIPLINE_OK | PF04 | proof.txt |\n", encoding="utf-8")
    tests = root / "tests/qa"
    tests.mkdir(parents=True)
    (tests / "test_epic021_scaffolding.py").write_text("def test_scaffold():\n    assert True\n", encoding="utf-8")


def test_wrapper_delegates_to_current_state_harness(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    _repo(tmp_path)
    class Done:
        returncode = 0
        stdout = "passed"
        stderr = ""
    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done())
    result = run_epic021_qa(repo_root=tmp_path)
    assert result["bootstrap"].status is Status.PASS
    assert result["viability"].status is Status.PASS
    manifest = json.loads((tmp_path / "audit/qa/hde-epic021/qa_step_logs_manifest.json").read_text())
    assert set(manifest["checks"]) == {"D00_bootstrap", "acceptance-map-viability"}
    assert "run_id" not in json.dumps(manifest)


def test_wrapper_never_creates_checkout_qa_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    _repo(tmp_path)
    before = {path.as_posix() for path in Path("audit/qa").rglob("*") if path.is_file()}
    class Done:
        returncode = 0
        stdout = "passed"
        stderr = ""
    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done())
    run_epic021_qa(repo_root=tmp_path)
    after = {path.as_posix() for path in Path("audit/qa").rglob("*") if path.is_file()}
    assert after == before
