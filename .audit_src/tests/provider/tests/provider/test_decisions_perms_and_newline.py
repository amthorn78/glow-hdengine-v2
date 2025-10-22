import os
import pathlib
from engine.config import provider_loader

def test_decision_perms_and_single_newline(monkeypatch):
    # Clean env
    for k in ("ENGINE_PROVIDER","APP_ENV","ENGINE_ENV","SAFE_MODE","KEEP_REAL_SECRETS"):
        monkeypatch.delenv(k, raising=False)

    # Remove old artifact
    p = pathlib.Path("artifacts/provider/decision.txt")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.unlink(missing_ok=True)

    # Resolve (default -> fixtures)
    prov = provider_loader.resolve_provider()
    assert p.exists()

    data = p.read_bytes()
    # exactly one trailing LF
    assert data.endswith(b"\n")
    assert not data[:-1].endswith(b"\n")

    # perms 0600
    mode = os.stat(p).st_mode & 0o777
    assert mode == 0o600