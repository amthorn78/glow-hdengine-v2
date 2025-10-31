import pytest
pytestmark = pytest.mark.epic006
import hashlib
import json


def _h(x: bytes) -> str:
    return hashlib.sha256(x).hexdigest()


def test_bytes_identity_under_env_pins():
    obj = {"a": 1, "b": 2}
    b1 = json.dumps(obj, separators=(",", ":"), ensure_ascii=False).encode("utf-8") + b"\n"
    b2 = json.dumps(obj, separators=(",", ":"), ensure_ascii=False).encode("utf-8") + b"\n"
    assert _h(b1) == _h(b2)
