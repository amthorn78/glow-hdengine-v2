import os, pathlib, stat
from engine.config import provider_loader

def test_engine_provider_casing_normalized(monkeypatch, tmp_path):
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(tmp_path))  # empty secrets
    monkeypatch.setenv("ENGINE_PROVIDER", "FiXtUrEs")
    provider_loader.resolve_provider()
    p = pathlib.Path("artifacts/provider/decision.txt")
    assert p.exists()
    assert p.read_text(encoding="utf-8") == "provider=fixtures source=env\n"

def test_decision_perms_and_exactly_one_newline(monkeypatch, tmp_path):
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(tmp_path))  # empty secrets
    monkeypatch.delenv("ENGINE_PROVIDER", raising=False)     # default path
    provider_loader.resolve_provider()
    p = pathlib.Path("artifacts/provider/decision.txt")
    st = p.stat()
    assert stat.S_IMODE(st.st_mode) == 0o600
    data = p.read_bytes()
    # Exactly one trailing LF: endswith \n but the preceding byte is not \n
    assert data.endswith(b"\n")
    assert not data[:-1].endswith(b"\n")