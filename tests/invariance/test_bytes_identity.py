import hashlib
import json

import pytest

from engine.serializer.canon import sercanon
from engine.runtime.determinism_env import ensure_determinism_env

pytestmark = pytest.mark.epic006


def _h(x: bytes) -> str:
    return hashlib.sha256(x).hexdigest()


def test_bytes_identity_under_env_pins():
    ensure_determinism_env()
    obj = {"a": 1, "b": 2}
    b1 = sercanon(obj)
    b2 = sercanon(json.loads(b1))
    assert b1.endswith(b"\n") and b2.endswith(b"\n")
    assert _h(b1) == _h(b2)
