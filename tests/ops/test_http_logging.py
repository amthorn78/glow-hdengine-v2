from __future__ import annotations

import json

import pytest

from engine.ops import http_log


def test_log_http_call_keys_only(tmp_path, monkeypatch):
    log_path = tmp_path / "sample.jsonl"
    monkeypatch.setattr(http_log, "LOG_PATH", log_path)

    http_log.log_http_call(
        route="db_bridge.get:/health",
        status=200,
        duration_ms=12.3456,
        release_id="rel-123",
        idempotence_hash="idh-456",
    )

    raw = log_path.read_text(encoding="utf-8").splitlines()
    assert len(raw) == 1
    record = json.loads(raw[0])
    assert record["route"] == "db_bridge.get:/health"
    assert record["status"] == 200
    assert set(record) <= {"at", "route", "status", "duration_ms", "release_id", "idempotence_hash"}
    assert isinstance(record["duration_ms"], float)
    assert record["duration_ms"] == round(record["duration_ms"], 3)


@pytest.mark.parametrize(
    "override",
    [
        "/tmp/keys_only.jsonl",
        "../keys_only.jsonl",
        "artifacts/ops/rails_open_scope/../keys_only.jsonl",
        "artifacts/ops/rails_open_scope/arbitrary.jsonl",
    ],
)
def test_log_override_rejects_absolute_traversal_and_unowned_names(
    tmp_path, monkeypatch, override
):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv(http_log.LOG_PATH_ENV, override)
    fallback = tmp_path / "fallback.jsonl"
    monkeypatch.setattr(http_log, "LOG_PATH", fallback)

    http_log.log_http_call(route="db.read", status=200, duration_ms=1)

    assert not fallback.exists()
    assert tuple(tmp_path.rglob("*.jsonl")) == ()


def test_log_override_rejects_symlink_target(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    capture_root = tmp_path / http_log.CAPTURE_LOG_ROOT
    capture_root.mkdir(parents=True)
    victim = tmp_path / "victim.txt"
    victim.write_text("unchanged\n", encoding="utf-8")
    name = "keys_only.123.20260722T120000Z.jsonl"
    (capture_root / name).symlink_to(victim)
    monkeypatch.setenv(
        http_log.LOG_PATH_ENV,
        (http_log.CAPTURE_LOG_ROOT / name).as_posix(),
    )

    http_log.log_http_call(route="db.read", status=200, duration_ms=1)

    assert victim.read_text(encoding="utf-8") == "unchanged\n"


def test_log_override_rejects_symlink_parent(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    victim_root = tmp_path / "victim"
    victim_root.mkdir()
    (tmp_path / "artifacts").symlink_to(victim_root, target_is_directory=True)
    name = "keys_only.123.20260722T120000Z.jsonl"
    monkeypatch.setenv(
        http_log.LOG_PATH_ENV,
        (http_log.CAPTURE_LOG_ROOT / name).as_posix(),
    )

    http_log.log_http_call(route="db.read", status=200, duration_ms=1)

    assert tuple(victim_root.rglob("*")) == ()


def test_append_remains_anchored_when_checked_parent_name_is_swapped(
    tmp_path, monkeypatch
):
    monkeypatch.chdir(tmp_path)
    capture_root = tmp_path / http_log.CAPTURE_LOG_ROOT
    capture_root.mkdir(parents=True)
    victim_root = tmp_path / "victim"
    victim_root.mkdir()
    name = "keys_only.123.20260722T120000Z.jsonl"
    relative = http_log.CAPTURE_LOG_ROOT / name
    monkeypatch.setenv(http_log.LOG_PATH_ENV, relative.as_posix())
    real_open = http_log.os.open
    swapped = False

    def swapping_open(path, flags, mode=0o777, *, dir_fd=None):
        nonlocal swapped
        if path == name and dir_fd is not None and not swapped:
            swapped = True
            capture_root.rename(tmp_path / "pinned")
            capture_root.symlink_to(victim_root, target_is_directory=True)
        return real_open(path, flags, mode, dir_fd=dir_fd)

    monkeypatch.setattr(http_log.os, "open", swapping_open)
    http_log.log_http_call(route="db.read", status=200, duration_ms=1)

    assert swapped is True
    assert not (victim_root / name).exists()
    assert json.loads((tmp_path / "pinned" / name).read_text(encoding="utf-8"))[
        "route"
    ] == "db.read"


def test_owned_capture_override_writes_only_fixed_subtree(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    name = "keys_only.123.20260722T120000Z.jsonl"
    relative = http_log.CAPTURE_LOG_ROOT / name
    monkeypatch.setenv(http_log.LOG_PATH_ENV, relative.as_posix())

    http_log.log_http_call(route="db.read", status=200, duration_ms=1)

    assert json.loads((tmp_path / relative).read_text(encoding="utf-8"))["route"] == "db.read"
