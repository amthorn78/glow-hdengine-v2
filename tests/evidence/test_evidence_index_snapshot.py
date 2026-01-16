import hashlib
import json
import shutil
import tempfile
from pathlib import Path

import pytest

from tools.evidence import generate_evidence_index_snapshot as snapshot


def _set_closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")


def _write_human_index(path: Path, artifact_key: str) -> None:
    payload = [{"artifact_key": artifact_key, "discovered_physical_path": "artifacts/demo.txt"}]
    path.write_text(json.dumps(payload), encoding="utf-8")


def _write_mirror(path: Path, lines: list[str]) -> None:
    path.write_text("".join(lines), encoding="utf-8")


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_snapshot(path: Path, *, human_sha: str, mirror_sha: str, generated_at: str, parity: bool) -> None:
    payload = {
        "generated_at_utc": generated_at,
        "inputs": {
            "human_index_path": snapshot.HUMAN_INDEX_REL,
            "human_index_sha256": human_sha,
            "machine_mirror_path": snapshot.MIRROR_REL,
            "machine_mirror_sha256": mirror_sha,
        },
        "parity": {"artifact_keys_match": parity},
        "schema_version": "1",
    }
    path.write_bytes(snapshot._render_snapshot(payload))


@pytest.fixture
def repo_tmp_path() -> Path:
    base = snapshot.ROOT / "tmp" / "pytest_evidence_index_snapshot"
    base.mkdir(parents=True, exist_ok=True)
    temp_dir = Path(tempfile.mkdtemp(dir=base))
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def test_snapshot_pass(repo_tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _set_closed_rails(monkeypatch)
    human_path = repo_tmp_path / "INDEX.json"
    mirror_path = repo_tmp_path / "evidence_index.jsonl"
    snapshot_path = repo_tmp_path / "snapshot.json"

    _write_human_index(human_path, "alpha")
    _write_mirror(mirror_path, [json.dumps({"artifact_key": "alpha"}) + "\n"])

    inputs = snapshot.Inputs(human_path=human_path, mirror_path=mirror_path, snapshot_path=snapshot_path)
    status, exit_code = snapshot.run_snapshot(inputs, check_only=False)
    output = capsys.readouterr().out

    assert "STATUS: PASS" in output
    assert status == "STATUS: PASS"
    assert exit_code == 0


def test_snapshot_non_object_mirror_line(
    repo_tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _set_closed_rails(monkeypatch)
    human_path = repo_tmp_path / "INDEX.json"
    mirror_path = repo_tmp_path / "evidence_index.jsonl"
    snapshot_path = repo_tmp_path / "snapshot.json"

    _write_human_index(human_path, "alpha")
    _write_mirror(mirror_path, ["[]\n"])

    _write_snapshot(
        snapshot_path,
        human_sha=_sha256_path(human_path),
        mirror_sha=_sha256_path(mirror_path),
        generated_at="2026-01-16T00:00:00Z",
        parity=False,
    )
    snapshot._write_path_proof(snapshot_path, produced_at="2026-01-16T00:00:00Z")

    inputs = snapshot.Inputs(human_path=human_path, mirror_path=mirror_path, snapshot_path=snapshot_path)
    status, exit_code = snapshot.run_snapshot(inputs, check_only=True)
    output = capsys.readouterr().out

    assert "STATUS: FAIL_BEHAVIOR" in output
    assert "Traceback" not in output
    assert status.startswith("STATUS: FAIL_BEHAVIOR")
    assert exit_code != 0


def test_snapshot_invalid_generated_at(
    repo_tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    _set_closed_rails(monkeypatch)
    human_path = repo_tmp_path / "INDEX.json"
    mirror_path = repo_tmp_path / "evidence_index.jsonl"
    snapshot_path = repo_tmp_path / "snapshot.json"

    _write_human_index(human_path, "alpha")
    _write_mirror(mirror_path, [json.dumps({"artifact_key": "alpha"}) + "\n"])

    _write_snapshot(
        snapshot_path,
        human_sha=_sha256_path(human_path),
        mirror_sha=_sha256_path(mirror_path),
        generated_at="2026-99-99",
        parity=True,
    )
    snapshot._write_path_proof(snapshot_path, produced_at="2026-01-16T00:00:00Z")

    inputs = snapshot.Inputs(human_path=human_path, mirror_path=mirror_path, snapshot_path=snapshot_path)
    status, exit_code = snapshot.run_snapshot(inputs, check_only=True)
    output = capsys.readouterr().out

    assert "STATUS: FAIL_BEHAVIOR" in output
    assert "GENERATED_AT_FORMAT" in output
    assert "Traceback" not in output
    assert status.startswith("STATUS: FAIL_BEHAVIOR")
    assert exit_code != 0
