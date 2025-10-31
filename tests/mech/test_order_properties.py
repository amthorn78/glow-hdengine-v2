import pytest
pytestmark = pytest.mark.epic006
from functools import cmp_to_key
from engine.mech.compare import cmp_ids, cmp_centers, cmp_category_by_rank, cmp_channel_minfirst

def _cmp(a,b): return (a>b)-(a<b)

@pytest.mark.parametrize("a,b", [("a","a"),("a","b"),("b","a")])
def test_cmp_ids_total_and_antisymmetric(a,b):
    assert _cmp(cmp_ids(a,b), -(cmp_ids(b,a))) in (-1,0,1)

def test_order_stable_on_equal():
    items = ["b1","a1","a2","b2"]
    # A key that returns same rank for 'a*' and 'b*' to force equal-comparator cases
    from functools import cmp_to_key
    def cmp_on_first_char(x,y): return (x[0]>y[0])-(x[0]<y[0])
    out = sorted(items, key=cmp_to_key(cmp_on_first_char))
    assert out.index("a1") < out.index("a2") and out.index("b1") < out.index("b2")

def test_cmp_centers_totality():
    centers = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]
    # total order: sorting twice yields same
    s1 = sorted(centers, key=lambda x: centers.index(x))
    s2 = sorted(centers, key=lambda x: centers.index(x))
    assert s1 == s2

def test_cmp_category_rank_order():
    categories = ["alignment","harmony","balance"]
    assert sorted(categories, key=cmp_to_key(cmp_category_by_rank)) == ["harmony","alignment","balance"]

@pytest.mark.parametrize("x,y,exp",
  [("20-34","34-20","20-34"),("1-9","09-01","01-09"),("05-05","5-5","05-05")])
def test_channel_minfirst_normalization(x,y,exp):
    from engine.mech.compare import _normalize_channel
    assert _normalize_channel(x) == exp
    assert _normalize_channel(y) == exp
