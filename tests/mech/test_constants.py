import pytest
pytestmark = pytest.mark.epic006
from engine.constants import EM_MAX, THROAT_EM_MAX, CENTER_MAX, MIND_THROAT_MAX, MOTOR_THROAT_MAX, COMP_MAX, DIRECT_MOTOR_THROAT

def test_denominators():
    assert (EM_MAX,THROAT_EM_MAX,CENTER_MAX,MIND_THROAT_MAX,MOTOR_THROAT_MAX,COMP_MAX) == (36,13,9,3,4,6)

def test_motor_throat_direct_set():
    assert set(DIRECT_MOTOR_THROAT) == {"12-22","21-45","20-34","35-36"}
