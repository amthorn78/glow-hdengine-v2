import pathlib
from core.canon.validate import load_repo_canon, validate_centers_strict
from core.canon.checksums import build_checksums

PIN_ORDER = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]

def test_center_order_and_counts_are_frozen():
    canon = load_repo_canon(pathlib.Path("."))
    # Strict counts by center (unordered key/value equality)
    issues = validate_centers_strict(canon)
    assert issues == [], f"strict center validation failed: {issues}"
    # Canonical order is validated through checksums center_order
    chs = build_checksums(canon)
    assert chs["center_order"] == PIN_ORDER
