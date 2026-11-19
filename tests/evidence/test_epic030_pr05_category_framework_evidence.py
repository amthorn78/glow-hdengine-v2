from __future__ import annotations

import hashlib
import importlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from engine.compat import compute
from engine.config.registry_loader import SchemaValidationError
from engine.runtime.identity import identity_meta
from tests.support.pr04_fixtures import build_bundle, build_pack, inject_seams


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-epic030-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-epic030-pack"))


@pytest.fixture
def admitted(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    return bundle


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# HDE-EPIC043 WU-PR-09: the PR-05 records are frozen history. Retired with their
# subject (regenerating capture-time v1 evaluations):
# test_pr05_binding_passes_when_index_and_mirror_include_pr05_artifacts and
# test_pr05_binding_fails_when_canonical_compare_fails. The tests below pin the
# frozen bytes instead.


def test_pr05_generation_refuses_as_frozen_history_and_writes_nothing(monkeypatch):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr05_category_framework_evidence")
    monkeypatch.setattr(mod, "_write_bytes", lambda *a, **k: pytest.fail("write attempted"))
    with pytest.raises(SystemExit, match=mod.FROZEN_HISTORY_NOT_REGENERATED):
        mod.generate()
    with pytest.raises(SystemExit, match=mod.FROZEN_HISTORY_NOT_REGENERATED):
        mod.main([])


def test_pr05_frozen_pins_equal_the_committed_records(capsys):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr05_category_framework_evidence")
    for name, (sha256, size) in mod.FROZEN_RECORDS.items():
        raw = (mod.OUT_DIR / name).read_bytes()
        assert (hashlib.sha256(raw).hexdigest(), len(raw)) == (sha256, size), name
    assert mod.main(["--check"]) == 0
    assert "pinned SHA-256 and size" in capsys.readouterr().out


def test_pr05_check_names_an_altered_record(tmp_path, monkeypatch, capsys):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr05_category_framework_evidence")
    copy = tmp_path / "pr-05"
    shutil.copytree(mod.OUT_DIR, copy)
    target = copy / "category_framework_binding.log"
    target.write_bytes(target.read_bytes() + b"x")
    assert mod.frozen_record_mismatches(copy) == ["category_framework_binding.log"]
    monkeypatch.setattr(mod, "OUT_DIR", copy)
    assert mod.main(["--check"]) == 1
    assert capsys.readouterr().err == "FROZEN_RECORD_MISMATCH:category_framework_binding.log\n"


def test_pr05_admission_probe_admits_the_repository_root(monkeypatch):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr05_category_framework_evidence")
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", compute.load_active_mechanics_bundle)
    assert mod.probe_release_admission().release_id == identity_meta()["release_id"]

_CLOSED_RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev"}
_ROOT = Path(__file__).resolve().parents[2]


# --- HDE-CRD-0003 S19-R04: asking an owner tool for usage changes nothing ------------------

_FIXED_TIME_NS = 1_000_000_000_000_000_000


def _tracked_copy(destination: Path) -> Path:
    """Copy every tracked file, with one fixed old mtime, so any rewrite is visible."""

    listed = subprocess.run(
        ["git", "-C", str(_ROOT), "ls-files", "-z"], check=True, capture_output=True
    ).stdout
    for raw in listed.split(b"\0"):
        if not raw:
            continue
        rel = raw.decode("utf-8")
        source, target = _ROOT / rel, destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_symlink():
            target.symlink_to(os.readlink(source))
        elif source.is_file():
            shutil.copy2(source, target)
            os.utime(target, ns=(_FIXED_TIME_NS, _FIXED_TIME_NS))
    return destination


def _tree_state(root: Path) -> dict[str, tuple[object, ...]]:
    state: dict[str, tuple[object, ...]] = {}
    for directory, names, files in os.walk(root):
        for name in names + files:
            path = Path(directory) / name
            info = path.lstat()
            body = (
                hashlib.sha256(path.read_bytes()).hexdigest()
                if path.is_file() and not path.is_symlink()
                else None
            )
            state[path.relative_to(root).as_posix()] = (
                info.st_mode, info.st_size, info.st_mtime_ns, info.st_ino, body,
            )
    return state


def _run_in_copy(copy: Path, tool: str, *args: str) -> subprocess.CompletedProcess[str]:
    env = {**os.environ, **_CLOSED_RAILS, "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run(
        [sys.executable, tool, *args], cwd=copy, env=env, capture_output=True, text=True, timeout=600
    )


_TOOL = "tools/evidence/generate_epic030_pr05_category_framework_evidence.py"


def test_pr05_generator_help_changes_no_file(tmp_path):
    copy = _tracked_copy(tmp_path / "tree")
    before = _tree_state(copy)
    result = _run_in_copy(copy, _TOOL, "--help")
    assert result.returncode == 0
    assert result.stdout.startswith("usage:") and result.stderr == ""
    assert _tree_state(copy) == before


def test_pr05_generator_main_parses_an_empty_argument_list(monkeypatch):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr05_category_framework_evidence")
    calls: list[str] = []
    monkeypatch.setattr(mod, "generate", lambda: calls.append("generate"))
    monkeypatch.setattr(sys, "argv", ["pytest", "--unknown-pytest-option"])
    assert mod.main() == 0
    assert mod.main([]) == 0
    assert calls == ["generate", "generate"]
    with pytest.raises(SystemExit) as usage:
        mod.main(["--help"])
    assert usage.value.code == 0 and calls == ["generate", "generate"]
