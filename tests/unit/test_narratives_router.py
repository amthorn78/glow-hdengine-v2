from engine.narratives import MISSING_NARRATIVE_KEY, get_pack, route_keys
from engine.narratives.constants import BANDS, PERSPECTIVES

EXPECTED_CATEGORIES = (
    "heat",
    "harmony",
    "communication",
    "alignment",
    "comfort",
    "consistency",
    "expansion",
    "creativity",
    "drive",
    "balance",
)
EXPECTED_KEY_TABLE_ROWS = 40


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


def test_router_covers_supported_category_band_perspective_matrix():
    pack = get_pack()
    assert pack.categories == set(EXPECTED_CATEGORIES)
    assert len(EXPECTED_CATEGORIES) * len(BANDS) == EXPECTED_KEY_TABLE_ROWS

    for category in EXPECTED_CATEGORIES:
        for band in BANDS:
            for perspective in PERSPECTIVES:
                result = route_keys(
                    category,
                    band,
                    perspective,
                    viewer_top="ignored",
                    flags=["b", "a", "b"],
                )
                assert set(result) == {"personal_key", "shared_key"}
                assert result["shared_key"] == f"{category}.{band.lower()}.shared.1"
                assert result["personal_key"] == f"{category}.{band.lower()}.personal.1"
                assert result["shared_key"] in pack.keys
                assert result["personal_key"] in pack.keys


def test_router_two_run_identity_for_supported_and_missing_cases():
    cases = [
        ("harmony", "Cool", "shared"),
        ("heat", "Open", "a_to_b"),
        ("balance", "Glow", "b_to_a"),
        ("unknown", "Cool", "shared"),
        ("harmony", "Unknown", "shared"),
        ("harmony", "Cool", "unknown"),
    ]

    for category, band, perspective in cases:
        first = route_keys(category, band, perspective, viewer_top=None, flags=["demo"])
        second = route_keys(category, band, perspective, viewer_top=None, flags=["demo"])
        assert first == second


def test_router_ab_ba_coherence_for_directional_perspectives():
    pack = get_pack()
    assert pack.categories == set(EXPECTED_CATEGORIES)

    for category in EXPECTED_CATEGORIES:
        for band in BANDS:
            a_to_b = route_keys(category, band, "a_to_b", viewer_top=None, flags=None)
            b_to_a = route_keys(category, band, "b_to_a", viewer_top=None, flags=None)
            assert a_to_b == b_to_a
            assert a_to_b["personal_key"] == f"{category}.{band.lower()}.personal.1"
            assert a_to_b["shared_key"] == f"{category}.{band.lower()}.shared.1"


def test_router_missing_mappings_return_missing_key_without_fallbacks():
    missing_cases = [
        ("unknown", "Cool", "shared"),
        ("harmony", "Unknown", "shared"),
        ("harmony", "Cool", "unknown"),
        ("unknown", "Unknown", "unknown"),
    ]

    for category, band, perspective in missing_cases:
        result = route_keys(category, band, perspective, viewer_top=None, flags=None)
        assert result == {
            "personal_key": MISSING_NARRATIVE_KEY,
            "shared_key": MISSING_NARRATIVE_KEY,
        }
