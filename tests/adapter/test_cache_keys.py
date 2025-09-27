from adapter.cache_keys import reader_cache_key

def test_ab_ba_tuple_equality():
    a = reader_cache_key("alice","bob","rel1","fpA","fpB")
    b = reader_cache_key("bob","alice","rel1","fpA","fpB")
    assert a == b
    assert a[0] <= a[1]  # min,max order

def test_tuple_fields_are_stable():
    t = reader_cache_key("u1","u2","relX","fA","fB")
    assert t == ("u1","u2","relX","fA","fB")
