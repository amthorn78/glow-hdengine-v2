from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.ops import capture_rails_open_scope as capture


def test_capture_scope_uses_isolated_child_log_and_preserves_shared_log(tmp_path, monkeypatch):
    shared = tmp_path / "artifacts/logs/keys_only.sample.jsonl"
    shared.parent.mkdir(parents=True)
    original = b'{"route":"retained"}\n'
    shared.write_bytes(original)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("DATABASE_URL", "postgresql://redacted")
    for key, value in capture.REQUIRED_ENV.items():
        monkeypatch.setenv(key, value)

    def fake_run(command, *, log_path: Path):
        assert log_path != shared
        log_path.write_text(json.dumps({"route": "db.psycopg.health"}) + "\n", encoding="utf-8")

    monkeypatch.setattr(capture, "_run_command", fake_run)
    assert capture.main() == 0
    assert shared.read_bytes() == original
    assert (tmp_path / capture.SUMMARY_PATH).read_text(encoding="utf-8").count("db.psycopg.health") == 1


def test_capture_scope_failure_preserves_shared_log(tmp_path, monkeypatch):
    shared = tmp_path / "artifacts/logs/keys_only.sample.jsonl"
    shared.parent.mkdir(parents=True)
    original = b'{"route":"retained"}\n'
    shared.write_bytes(original)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("DATABASE_URL", "postgresql://redacted")
    for key, value in capture.REQUIRED_ENV.items():
        monkeypatch.setenv(key, value)

    def fake_run(command, *, log_path: Path):
        raise SystemExit("child failed")

    monkeypatch.setattr(capture, "_run_command", fake_run)
    with pytest.raises(SystemExit):
        capture.main()
    assert shared.read_bytes() == original


def test_capture_scope_vendor_route_fails_from_isolated_log(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("DATABASE_URL", "postgresql://redacted")
    for key, value in capture.REQUIRED_ENV.items():
        monkeypatch.setenv(key, value)

    def fake_run(command, *, log_path: Path):
        log_path.write_text(json.dumps({"route": "vendor.hdapi.post:/charts"}) + "\n", encoding="utf-8")

    monkeypatch.setattr(capture, "_run_command", fake_run)
    with pytest.raises(SystemExit, match="vendor HTTP calls"):
        capture.main()


def test_capture_scope_refuses_preplanted_log_symlink(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("DATABASE_URL", "postgresql://redacted")
    for key, value in capture.REQUIRED_ENV.items():
        monkeypatch.setenv(key, value)
    victim = tmp_path / "victim.txt"
    victim.write_text("unchanged\n", encoding="utf-8")
    relative = capture.CAPTURE_LOG_ROOT / "keys_only.123.20260722T120000Z.jsonl"
    (tmp_path / relative.parent).mkdir(parents=True)
    (tmp_path / relative).symlink_to(victim)
    monkeypatch.setattr(capture, "_child_log_path", lambda: relative)
    called = []
    monkeypatch.setattr(
        capture,
        "_run_command",
        lambda *args, **kwargs: called.append((args, kwargs)),
    )

    with pytest.raises(FileExistsError):
        capture.main()

    assert called == []
    assert victim.read_text(encoding="utf-8") == "unchanged\n"


def test_capture_summary_replaces_symlink_without_touching_target(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    victim = tmp_path / "victim.txt"
    victim.write_text("unchanged\n", encoding="utf-8")
    summary = tmp_path / capture.SUMMARY_PATH
    summary.parent.mkdir(parents=True)
    summary.symlink_to(victim)
    for key, value in capture.REQUIRED_ENV.items():
        monkeypatch.setenv(key, value)

    assert capture._write_summary(({"route": "db.psycopg.health"},)) == 0

    assert victim.read_text(encoding="utf-8") == "unchanged\n"
    assert not summary.is_symlink()
    assert "db.psycopg.health 1" in summary.read_text(encoding="utf-8")
