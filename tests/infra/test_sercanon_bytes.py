from engine.stable.sercanon import serialize, dumps_minified_sorted

def test_sorted_compact_single_lf():
    obj = {"b": 2, "a": 1}
    # string form (no trailing LF)
    assert dumps_minified_sorted(obj) == '{"a":1,"b":2}'
    # bytes form (exactly one trailing LF)
    b = serialize(obj)
    assert b == b'{"a":1,"b":2}\n'
    # idempotent bytes
    assert serialize(obj) == b
    # exactly one trailing LF (no double-LF)
    assert b.endswith(b"\n") and not b[:-1].endswith(b"\n")
