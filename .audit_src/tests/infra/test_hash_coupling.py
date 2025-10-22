from engine.stable.hashcouple import preimage_bytes, finalize_envelope, compute_hash

def test_preimage_hash_coupling_and_lf_and_identity():
    # Minimal public envelope (numeric-free except booleans); fields are exemplars
    env0 = {
        "schema": "v1",
        "eligible": True,
        "versions": {"reader": "v1"},
        "release_id": "deadbeef"*8,
        "meta": {"engine_tag": "Isis5", "invocation_tag": "INV-abc123"},
        # no idempotence_hash yet (preimage)
    }

    # Preimage bytes (LF-terminated) and hash
    pre_b = preimage_bytes(env0)
    assert pre_b.endswith(b"\n") and not pre_b[:-1].endswith(b"\n")
    h = compute_hash(pre_b)

    # Finalize and verify coupling + LF + two-run identity
    env1, out_b1, h1 = finalize_envelope(env0)
    env2, out_b2, h2 = finalize_envelope(env0)
    assert env1["idempotence_hash"] == h == h1 == h2
    assert out_b1 == out_b2
    assert out_b1.endswith(b"\n") and not out_b1[:-1].endswith(b"\n")
