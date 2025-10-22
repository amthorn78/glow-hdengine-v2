from adapter.cache_keys import build_cache_key

def test_ab_ba_same_key_and_positions():
    rid = "rel_deadbeef"
    A, B = "user9", "user1"
    fpA, fpB = "fpA_xyz", "fpB_abc"

    k_ab = build_cache_key(A, B, rid, fpA, fpB)
    k_ba = build_cache_key(B, A, rid, fpB, fpA)

    # AB == BA (orientation-safe)
    assert k_ab == k_ba

    # Tuple shape and field positions
    assert isinstance(k_ab, tuple) and len(k_ab) == 5
    u_min, u_max, rid2, fp_min, fp_max = k_ab
    assert rid2 == rid
    assert (u_min, u_max) == tuple(sorted([A, B]))

    # Fingerprints follow oriented users
    expect_fp_min = fpA if A <= B else fpB
    expect_fp_max = fpB if A <= B else fpA
    assert (fp_min, fp_max) == (expect_fp_min, expect_fp_max)
