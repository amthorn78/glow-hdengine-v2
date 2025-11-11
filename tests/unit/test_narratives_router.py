from engine.narratives import MISSING_NARRATIVE_KEY, get_pack, route_keys


def test_router_returns_primary_keys():
    get_pack()  # ensure pack loaded
    result = route_keys("harmony", "Cool", "shared", viewer_top=None, flags=None)
    assert result["shared_key"].startswith("harmony.cool.shared")
    assert result["personal_key"].startswith("harmony.cool.personal")


def test_router_handles_missing_category():
    get_pack()
    result = route_keys("unknown", "Cool", "shared", viewer_top=None, flags=None)
    assert result == {
        "personal_key": MISSING_NARRATIVE_KEY,
        "shared_key": MISSING_NARRATIVE_KEY,
    }
