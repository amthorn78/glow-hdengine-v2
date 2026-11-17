"""HDE-EPIC043 WU-PR-02 acceptance item 3: per-category band assignment (HDE-CONJ010.3).

HDE Math Spec §5.3.7 and the §9.1 v2 statement: each category has its own
inclusive maxima ``[c1, c2, c3, 100]``; Cool when ``score <= c1``, Open when
``<= c2``, Warm when ``<= c3``, else Glow; cases at each maximum, the next integer
after each, and ``100``.

The labelled fixture maxima are the same in every category, so they cannot show
that a band comes from its own category. This module therefore admits a second
bundle from a temporary root, built as ``tests/config/test_magic10_v2_loader.py``
builds its roots, with category-specific maxima ``(5 + i, 20 + i, 40 + i, 100)``
for the category at index ``i`` of ``catalog/magic10.json``. These maxima are test
values, not canon and not the v2 cut; nothing is written under the repository's
own tree, and no file is created at a governed path.

Stated limit: no real pair scores ``100`` (the score is at most 93 on every
admitted bundle), so ``100 -> Glow`` is shown by ``assign_band`` only.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest

from engine.config import magic10_v2_loader as v2
from engine.config.registry_loader import ManifestEntry
from engine.magic10_v2.calculation import BANDS, assign_band, compute_category_components
from engine.magic10_v2.kernel import compute_kernel
from engine.magic10_v2.signals import compute_signals
from engine.serializer import canon

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures" / "magic10_v2"
CONFIG = "catalog/magic10_mechanics_v2.json"
THRESHOLDS = "math/thresholds.json"
ORDER = tuple(json.loads((ROOT / "catalog" / "magic10.json").read_bytes())["order"])
TEST_MAXIMA = {category: (5 + index, 20 + index, 40 + index, 100) for index, category in enumerate(ORDER)}
PAIRS = (
    ((1,), (2,)),
    ((1, 8), (2,)),
    ((1, 8), (1, 8)),
    ((1,), (8,)),
    ((20, 34), (20, 34)),
    ((21,), (45,)),
    ((1, 8), (20, 34)),
    ((18, 26, 44, 58), (18, 26, 44, 58)),
    ((1, 8, 3, 60), (2, 14)),
    ((4, 17, 23, 24, 47), (43, 61, 62, 63, 64)),
)


def _write_canonical(path: Path, data: object) -> None:
    path.write_bytes(canon.sercanon(data, sort_keys=True))


@pytest.fixture(scope="module")
def maxima_bundle(tmp_path_factory: pytest.TempPathFactory) -> v2.Magic10V2Bundle:
    """An admitted v2 bundle whose maxima differ by category (test values, not canon)."""
    root = tmp_path_factory.mktemp("m10_v2_bands") / "root"
    for directory in ("catalog", "math", "schemas"):
        shutil.copytree(ROOT / directory, root / directory)
    shutil.copyfile(FIXTURES / "thresholds_v2.fixture.json", root / THRESHOLDS)
    shutil.copyfile(FIXTURES / "magic10_mechanics_v2.fixture.json", root / CONFIG)
    thresholds = json.loads((root / THRESHOLDS).read_bytes())
    for entry in thresholds["categories"]:
        entry["maxima"] = list(TEST_MAXIMA[entry["category_id"]])
    _write_canonical(root / THRESHOLDS, thresholds)
    configuration = json.loads((root / CONFIG).read_bytes())
    configuration["sources"]["thresholds"]["sha256"] = hashlib.sha256((root / THRESHOLDS).read_bytes()).hexdigest()
    _write_canonical(root / CONFIG, configuration)
    raw = (root / CONFIG).read_bytes()
    rows = (ManifestEntry(CONFIG, hashlib.sha256(raw).hexdigest(), len(raw)),)
    return v2.load_magic10_v2_bundle_from_root(root, rows)


def test_test_maxima_differ_by_category(maxima_bundle) -> None:
    assert dict(maxima_bundle.maxima) == TEST_MAXIMA
    assert len({maxima[0] for maxima in maxima_bundle.maxima.values()}) == len(ORDER)


@pytest.mark.parametrize("category", ORDER)
def test_band_at_every_edge_of_each_category(maxima_bundle, category) -> None:
    maxima = maxima_bundle.maxima[category]
    first, second, third, top = maxima
    edges = (0, first, first + 1, second, second + 1, third, third + 1, top)
    expected = ("Cool", "Cool", "Open", "Open", "Warm", "Warm", "Glow", "Glow")
    assert tuple(assign_band(score, maxima) for score in edges) == expected
    bands = [assign_band(score, maxima) for score in range(101)]
    assert set(bands) <= set(BANDS)
    assert [BANDS.index(band) for band in bands] == sorted(BANDS.index(band) for band in bands)
    for other in ORDER:
        if other != category:
            other_maxima = maxima_bundle.maxima[other]
            assert any(assign_band(score, other_maxima) != assign_band(score, maxima) for score in edges), other


def _components(bundle, mask_of, gates_a, gates_b):
    kernel = compute_kernel(mask_of(*gates_a), mask_of(*gates_b), bundle)
    components = compute_category_components(kernel, compute_signals(kernel, bundle), bundle)
    return {item.category_id: item for item in components}


def test_real_pairs_land_in_their_own_categorys_bands(maxima_bundle, v2_bundle, mask_of) -> None:
    seen = set()
    for gates_a, gates_b in PAIRS:
        components = _components(maxima_bundle, mask_of, gates_a, gates_b)
        fixture_components = _components(v2_bundle, mask_of, gates_a, gates_b)
        for category, item in components.items():
            assert item.band == assign_band(item.score, TEST_MAXIMA[category])
            assert item.score == fixture_components[category].score  # band selection does not change the score
            seen.add(item.band)
    assert seen == set(BANDS)
    comfort = _components(maxima_bundle, mask_of, (1, 8), (2,))["comfort"]
    assert (comfort.score, comfort.band) == (11, "Open")
    assert assign_band(11, TEST_MAXIMA["expansion"]) == "Cool"
