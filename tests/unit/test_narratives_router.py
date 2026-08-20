from pathlib import Path

import pytest

from engine.narratives import MISSING_NARRATIVE_KEY, get_pack, route_keys
from engine.narratives.constants import BANDS, PERSPECTIVES
from engine.narratives.loader import load_pack
from engine.narratives import state as narrative_state

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


@pytest.fixture(autouse=True)
def _isolated_current_pack(tmp_path, monkeypatch):
    pack = load_pack(Path("catalog/narratives"), tmp_path / "mounted")
    monkeypatch.setattr(narrative_state, "_PACK", pack)
    return pack


def test_router_returns_primary_keys():
    get_pack()  # ensure pack loaded
    result = route_keys("harmony", "Cool", "shared", viewer_top=None, flags=None)
    assert result["shared_key"].startswith("nar.harmony.cool.shared")
    assert result["personal_key"] == MISSING_NARRATIVE_KEY


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
                assert result["shared_key"].startswith(
                    f"nar.{category}.{band.lower()}.shared."
                )
                if perspective == "shared":
                    assert result["personal_key"] == MISSING_NARRATIVE_KEY
                else:
                    assert result["personal_key"].startswith(
                        f"nar.{category}.{band.lower()}.{perspective}."
                    )
                assert result["shared_key"] in pack.keys
                if perspective != "shared":
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
            assert a_to_b["shared_key"] == b_to_a["shared_key"]
            assert a_to_b["personal_key"] != b_to_a["personal_key"]
            assert a_to_b["personal_key"].startswith(
                f"nar.{category}.{band.lower()}.a_to_b."
            )
            assert b_to_a["personal_key"].startswith(
                f"nar.{category}.{band.lower()}.b_to_a."
            )


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
