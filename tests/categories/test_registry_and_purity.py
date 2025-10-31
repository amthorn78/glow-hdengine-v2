import pytest
pytestmark = pytest.mark.epic006
from engine.categories.registry import FROZEN_MAGIC10_ORDER, get_rank, all_ids

def test_frozen_order():
    assert list(all_ids()) == list(FROZEN_MAGIC10_ORDER)
    assert get_rank("harmony") == 0 and get_rank("balance") == 9

def test_register_unknown_id_hard_fails():
    import pytest
    from engine.categories.registry import register
    with pytest.raises(ValueError):
        register("not_a_category", lambda *_: None)
