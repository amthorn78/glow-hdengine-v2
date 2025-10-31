import pytest
pytestmark = pytest.mark.epic006
from engine.mech.helpers import canonicalize_array

def test_arrays_as_sets():
    assert canonicalize_array(["b","a","a"]) == ["a","b"]
