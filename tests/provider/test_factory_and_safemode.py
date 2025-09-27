import json, os, socket
from pathlib import Path
import pytest

from engine.config import provider_loader

def test_safe_mode_socket_trap_installs_and_blocks(monkeypatch):
    monkeypatch.setenv("SAFE_MODE","1")
    installed = provider_loader.install_socket_trap_if_enabled()
    assert installed is True
    with pytest.raises(OSError):
        socket.socket()  # any socket use must raise when SAFE_MODE=1

def test_factory_precedence_programmatic_over_secrets_over_env(tmp_path, monkeypatch):
    # env provider (would win if no programmatic and no secrets)
    monkeypatch.setenv("ENGINE_PROVIDER","env_choice")

    # secrets/provider.json present -> should beat env when programmatic not provided
    secrets = Path("secrets"); secrets.mkdir(exist_ok=True)
    (secrets/"provider.json").write_text(json.dumps({"provider":"secretspref"}), encoding="utf-8")

    # 1) programmatic wins outright
    p = provider_loader.get_provider(programmatic="fixtures")
    assert p.__class__.__name__ == "FixturesProvider"

    # 2) without programmatic, secrets wins and we can observe resolver output
    name, src = provider_loader._resolve_provider_name(None)
    assert (name, src) == ("secretspref","secrets")

def test_prod_env_override_forbidden(monkeypatch):
    monkeypatch.setenv("ENGINE_ENV","prod")
    monkeypatch.setenv("ENGINE_PROVIDER","fixtures")
    with pytest.raises(Exception):
        provider_loader.get_provider()
