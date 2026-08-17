import pytest
pytestmark = pytest.mark.epic006
from engine.mech.helpers import SetIdentityConflict, canonicalize_array, canonicalize_declared_set

def test_arrays_as_sets():
    assert canonicalize_array(["b","a","a"]) == ["a","b"]


def test_declared_object_set_deduplicates_and_sorts_without_normalizing():
    values = [{"path": "z", "size": 1}, {"path": "A", "size": 2}, {"path": "z", "size": 1}]
    assert canonicalize_declared_set(values, identity="path") == [values[1], values[0]]


def test_scalar_identity_preserves_json_type():
    assert canonicalize_declared_set([1, "1", 1, "1"], identity=None) == ["1", 1]


def test_conflicting_identity_reports_first_divergent_field():
    with pytest.raises(SetIdentityConflict, match=r"first_divergent_field:\$\.size"):
        canonicalize_declared_set([{"path": "a", "size": 1}, {"path": "a", "size": 2}], identity="path")


def test_object_set_requires_identity_and_ordered_array_is_untouched():
    ordered = [{"id": "b"}, {"id": "a"}]
    with pytest.raises(ValueError, match="set_object_identity_required"):
        canonicalize_declared_set(ordered, identity=None)
    assert ordered == [{"id": "b"}, {"id": "a"}]
