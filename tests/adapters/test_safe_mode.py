
import os, pytest
from adapters._net import require_network, NetworkDisabledError, safe_mode_enabled

def test_require_network_raises_in_safe_mode(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    assert safe_mode_enabled() is True
    with pytest.raises(NetworkDisabledError):
        require_network("hdapi")
