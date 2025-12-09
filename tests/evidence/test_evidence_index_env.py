import pytest

from engine.runtime.determinism_env import DeterminismEnvError
from tools.evidence import update_evidence_index


def test_update_evidence_index_requires_closed_rails(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    with pytest.raises(DeterminismEnvError):
        update_evidence_index.ensure_determinism_env()
