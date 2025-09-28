from __future__ import annotations
import sys, pytest

def test_env_guard_import_is_pure(monkeypatch):
    # Any accidental I/O at import should blow up this test.
    def bomb(*a, **k): raise AssertionError("I/O at import-time")

    # File I/O
    monkeypatch.setattr("builtins.open", bomb)
    try:
        import pathlib
        monkeypatch.setattr(pathlib.Path, "open", bomb, raising=False)
        monkeypatch.setattr(pathlib.Path, "read_text", bomb, raising=False)
        monkeypatch.setattr(pathlib.Path, "write_text", bomb, raising=False)
    except Exception:
        pass

    # Sockets / subprocess
    monkeypatch.setattr("socket.socket", bomb, raising=False)
    monkeypatch.setattr("subprocess.Popen", bomb, raising=False)

    # Force a fresh import under the patches
    sys.modules.pop("adapter.env_guard", None)
    import adapter.env_guard  # noqa: F401

def test_wsgi_import_collects_or_skips():
    try:
        import adapter.wsgi  # noqa: F401
    except ModuleNotFoundError:
        pytest.skip("adapter.wsgi not present; skip collect test")
