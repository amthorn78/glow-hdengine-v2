import pytest
pytestmark = pytest.mark.epic006
from engine.testsupport import GATES_ON

def test_change_gates_on():
    assert GATES_ON is True
