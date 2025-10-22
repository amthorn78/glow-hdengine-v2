import json
import logging
import os
import pathlib
import importlib
import re

import pytest
from engine.config import provider_loader

CID_RE = re.compile(r"^CID-[0-9a-f]{8}$")

def _json_messages(records):
    for r in records:
        try:
            yield json.loads(r.message)
        except Exception:
            # tolerate any non-json logs in the stream
            continue

def test_provider_startup_logs_once(caplog, tmp_path, monkeypatch):
    # fresh env & artifact
    for k in ("ENGINE_PROVIDER", "APP_ENV", "ENGINE_ENV", "SAFE_MODE", "KEEP_REAL_SECRETS"):
        monkeypatch.delenv(k, raising=False)
    dec = pathlib.Path("artifacts/provider/decision.txt")
    dec.parent.mkdir(parents=True, exist_ok=True)
    dec.unlink(missing_ok=True)

    # isolated empty secrets
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(tmp_path))
    monkeypatch.setenv("SAFE_MODE", "1")

    # reload module to reset once-per-process globals for this test
    import engine.config.provider_loader as loader
    importlib.reload(loader)

    caplog.set_level(logging.INFO, logger="engine.provider")

    # 1st resolve -> should emit provider.startup (once)
    prov1 = loader.resolve_provider()
    # 2nd resolve -> should not emit provider.startup again
    prov2 = loader.resolve_provider()

    msgs = list(_json_messages(caplog.records))
    startups = [m for m in msgs if m.get("route") == "provider.startup"]
    assert len(startups) == 1
    s = startups[0]
    assert s.get("provider") in {"fixtures", "internal_engine", "vendor_http"}
    assert s.get("source") in {"default", "env", "secrets"}
    assert isinstance(s.get("safe_mode"), bool)
    assert CID_RE.match(s.get("correlation_id", "")), s

    # sanity: decision artifact exists and matches provider/source shape
    assert dec.exists()
    txt = dec.read_text(encoding="utf-8").strip()
    assert txt.startswith("provider=") and " source=" in txt