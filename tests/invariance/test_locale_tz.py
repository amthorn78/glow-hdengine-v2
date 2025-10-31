import pytest
pytestmark = pytest.mark.epic006
import os

def test_invariance_env_pins():
    assert os.environ.get("LC_ALL") == "C"
    assert os.environ.get("TZ") == "UTC"
