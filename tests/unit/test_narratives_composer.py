from engine.narratives import compose_text, get_pack


def test_compose_shared_success():
    pack = get_pack()
    result = compose_text(
        category="harmony",
        band="Cool",
        perspective="shared",
        viewer_top=None,
        flags=None,
        families_fired=["compat_harmony"],
        release_id="0" * 64,
        pack_sha=pack.pack_sha,
    )
    assert result.ok
    assert result.text is not None and "Together" in result.text
    assert result.key.startswith("harmony.cool.shared")


def test_compose_suppressed_unsorted_families():
    pack = get_pack()
    result = compose_text(
        category="harmony",
        band="Cool",
        perspective="shared",
        viewer_top=None,
        flags=None,
        families_fired=["z", "a"],
        release_id="0" * 64,
        pack_sha=pack.pack_sha,
    )
    assert not result.ok
    assert result.policy_reason == "conflict"


def test_compose_pack_mismatch():
    result = compose_text(
        category="harmony",
        band="Cool",
        perspective="shared",
        viewer_top=None,
        flags=None,
        families_fired=["compat_harmony"],
        release_id="0" * 64,
        pack_sha="f" * 64,
    )
    assert not result.ok
    assert result.policy_reason == "conflict"
