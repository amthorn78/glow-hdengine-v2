
from __future__ import annotations
from pathlib import Path
import importlib

def test_env_guard_artifact_bytes_and_perms(tmp_path, monkeypatch):
    mod = importlib.import_module("scripts.emit_env_guard_artifact")
    mod.main()  # emit

    p = Path("artifacts/hotfix/env_guard_import_ok.txt")
    assert p.exists(), "artifact missing"
    data = p.read_bytes()

    # hygiene
    assert not data.startswith(b"\xef\xbb\xbf"), "no BOM"
    assert data.endswith(b"\n"), "must end with single LF"
    assert data.count(b"\n") >= 1

    # perms
    mode = p.stat().st_mode & 0o777
    assert mode == 0o600
