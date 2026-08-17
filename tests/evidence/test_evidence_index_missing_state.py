from __future__ import annotations

import json
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
IGNORES = shutil.ignore_patterns(
    ".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".venv", "__pycache__"
)
ENV = {
    **os.environ,
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "LANG": "C",
    "LC_ALL": "C",
    "PYTHONDONTWRITEBYTECODE": "1",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}
SKELETON = (
    "docs/evidence/INDEX.json",
    "docs/evidence/INDEX.json.path_proof.txt",
    "docs/evidence/INDEX.sha256",
    "docs/evidence/INDEX.sha256.path_proof.txt",
    "artifacts/evidence_index.jsonl",
    "artifacts/evidence_index.jsonl.path_proof.txt",
    "artifacts/evidence_index.jsonl.sha256",
    "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
    "audit/gates/topology/orientation_demo.txt",
    "audit/gates/topology/orientation_demo.txt.path_proof.txt",
)


def _run(repo: Path, relative: str, *args: str) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, relative, *args]
    if relative.endswith("check_evidence_index_hash.sh"):
        command = [relative, *args]
    return subprocess.run(
        command,
        cwd=repo,
        env=ENV,
        capture_output=True,
        text=True,
        check=False,
    )


def _success(result: subprocess.CompletedProcess[str]) -> None:
    assert result.returncode == 0, result.stdout + result.stderr


def _checks(repo: Path) -> None:
    for command, args in (
        ("tools/evidence/update_evidence_index.py", ("--check",)),
        ("tools/evidence/orientation_demo.py", ("--check",)),
        ("ci/checks/check_mirror_schema.sh", ()),
        ("tools/evidence/validate_evidence_paths.py", ()),
        ("ci/checks/check_evidence_index_hash.sh", ()),
        ("tools/evidence/check_lf_endings.py", ()),
    ):
        _success(_run(repo, command, *args))


def _snapshot(repo: Path) -> dict[str, tuple[bytes, int]]:
    return {
        relative: (
            (repo / relative).read_bytes(),
            stat.S_IMODE((repo / relative).stat().st_mode),
        )
        for relative in SKELETON
        if (repo / relative).exists()
    }


def test_updater_recovers_complete_missing_state_in_one_write(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)

    missing_families = (
        ("docs/evidence/INDEX.sha256",),
        ("docs/evidence/INDEX.sha256.path_proof.txt",),
        (
            "artifacts/evidence_index.jsonl",
            "artifacts/evidence_index.jsonl.path_proof.txt",
            "artifacts/evidence_index.jsonl.sha256",
            "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
        ),
        (
            "audit/gates/topology/orientation_demo.txt",
            "audit/gates/topology/orientation_demo.txt.path_proof.txt",
        ),
    )
    for family in missing_families:
        original_modes = {
            relative: stat.S_IMODE((repo / relative).stat().st_mode)
            for relative in family
        }
        for relative in family:
            (repo / relative).unlink()
        _success(_run(repo, "tools/evidence/update_evidence_index.py"))
        assert all((repo / relative).is_file() for relative in family)
        assert {
            relative: stat.S_IMODE((repo / relative).stat().st_mode)
            for relative in family
        } == original_modes
        before_checks = _snapshot(repo)
        _checks(repo)
        assert _snapshot(repo) == before_checks

    # Check mode must fail without repairing a missing proof or changing any
    # other member of the governed skeleton.
    missing_proof = repo / "docs/evidence/INDEX.sha256.path_proof.txt"
    missing_proof.unlink()
    before_failed_check = _snapshot(repo)
    result = _run(repo, "tools/evidence/update_evidence_index.py", "--check")
    assert result.returncode != 0
    assert "MISSING_PROOF" in result.stdout + result.stderr
    assert _snapshot(repo) == before_failed_check
    assert not missing_proof.exists()
    _success(_run(repo, "tools/evidence/update_evidence_index.py"))

    # Exercise updater-owned membership addition and removal through the real
    # index-rendering path, rather than by calling the publication helper.
    index_path = repo / "docs/evidence/INDEX.json"
    entries = json.loads(index_path.read_text(encoding="utf-8"))
    added_key = (
        "registry.registry_report",
        "artifacts/registry/registry_report.json",
    )
    removed_key = (
        "epic031.pr02.keys_only_sample",
        "artifacts/logs/keys_only.sample.jsonl",
    )
    entries = [
        entry
        for entry in entries
        if (entry["artifact_key"], entry["discovered_physical_path"]) != added_key
    ]
    entries.append(
        {
            "artifact_key": removed_key[0],
            "discovered_physical_path": removed_key[1],
        }
    )
    index_path.write_text(
        json.dumps(entries, separators=(",", ":"), sort_keys=True) + "\n",
        encoding="utf-8",
    )

    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    final_entries = json.loads(index_path.read_text(encoding="utf-8"))
    final_keys = {
        (entry["artifact_key"], entry["discovered_physical_path"])
        for entry in final_entries
    }
    assert added_key in final_keys
    assert removed_key not in final_keys
    before_checks = _snapshot(repo)
    _checks(repo)
    assert _snapshot(repo) == before_checks
