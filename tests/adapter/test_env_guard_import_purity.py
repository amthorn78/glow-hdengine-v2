from __future__ import annotations
import sys

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

    # Force a fresh import under the patches; monkeypatch restores the original
    # module object (sys.modules entry and package attribute) after the test.
    import adapter
    monkeypatch.setattr(adapter, "env_guard", getattr(adapter, "env_guard", None), raising=False)
    monkeypatch.delitem(sys.modules, "adapter.env_guard", raising=False)
    import adapter.env_guard  # noqa: F401

def test_wsgi_import_collects():
    import adapter.wsgi  # noqa: F401
