import json
import pytest
from engine.compliance.invocation_tag import is_valid_invocation_tag, validate_invocation_tag
from engine.stable.sercanon import serialize

def test_invocation_tag_accepts_and_rejects():
    # Accept exact spec
    assert is_valid_invocation_tag("INV-0123456789abcdef")
    assert is_valid_invocation_tag("INV-" + "a"*16)

    # Reject wrong lengths (12/14/18) and bad case/suffix
    for bad in [
        "INV-0123456789abcd",          # 15 nibbles
        "INV-0123456789abc",           # 13 nibbles
        "INV-0123456789abcdef00",      # 18 nibbles
        "INV-0123456789ABCDEF",        # UPPER hex
        "INV-0123456789abcdef-A",      # suffix
        "inv-0123456789abcdef",        # wrong INV case
        "INV-01234g6789abcdef",        # non-hex
        "", None, 123,                  # non-strings
    ]:
        assert not is_valid_invocation_tag(bad)

    # validate_* path raises typed ValueError on bad input
    with pytest.raises(ValueError) as ei:
        validate_invocation_tag("INV-XYZ")
    assert "INVOCATION_TAG_INVALID" in str(ei.value)

def test_roundtrip_meta_invocation_tag_unchanged():
    tag = "INV-0123456789abcdef"
    # Simulate a minimal public envelope carry; we only care that meta round-trips unchanged
    env = {
        "reader_version":"v1",
        "eligible": False,
        "categories": [],
        "meta": {"engine_tag":"Isis5","invocation_tag": tag},
        "release_id": "deadbeef"*8,
        # idempotence_hash is computed elsewhere; we don't need it for round-trip meta proof
    }
    b = serialize(env)             # canonical serializer → bytes + single LF
    env2 = json.loads(b.decode("utf-8"))
    assert env2["meta"]["invocation_tag"] == tag
