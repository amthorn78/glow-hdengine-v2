"""Shared fixtures for the Magic10 v2 kernel tests (HDE-EPIC043 WU-PR-01).

The v2 bundle is admitted from a temporary root assembled exactly as
``tests/config/test_magic10_v2_loader.py`` assembles it: the repository's
``catalog/``, ``math/`` and ``schemas/`` bytes, with the labelled non-canon
fixtures of ``tests/fixtures/magic10_v2/`` at ``math/thresholds.json`` and
``catalog/magic10_mechanics_v2.json``. Those fixtures are non-canon: this bundle
is not the cutover configuration, and no maxima value is asserted. Nothing is
written under the repository's own tree.

Masks are built by the repository's own Gate normalizer, so every constructed
mask is a value the HDE Math Spec §5.2.1 representation admits.
"""
from __future__ import annotations

import hashlib
import shutil
from pathlib import Path
from typing import Callable

import pytest

from engine.bodygraph.gates import normalize_gates
from engine.config import magic10_v2_loader as v2
from engine.config.registry_loader import ManifestEntry

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures" / "magic10_v2"
CONFIG = "catalog/magic10_mechanics_v2.json"
THRESHOLDS = "math/thresholds.json"


@pytest.fixture(scope="session")
def v2_bundle(tmp_path_factory: pytest.TempPathFactory) -> v2.Magic10V2Bundle:
    """An admitted v2 bundle over the repository catalogs and the labelled fixtures."""
    root = tmp_path_factory.mktemp("m10_v2_kernel") / "root"
    for directory in ("catalog", "math", "schemas"):
        shutil.copytree(ROOT / directory, root / directory)
    shutil.copyfile(FIXTURES / "thresholds_v2.fixture.json", root / THRESHOLDS)
    shutil.copyfile(FIXTURES / "magic10_mechanics_v2.fixture.json", root / CONFIG)
    raw = (root / CONFIG).read_bytes()
    rows = (ManifestEntry(CONFIG, hashlib.sha256(raw).hexdigest(), len(raw)),)
    return v2.load_magic10_v2_bundle_from_root(root, rows)


@pytest.fixture(scope="session")
def mask_of() -> Callable[..., int]:
    """Return ``mask_of(*gates)``: the Gate set's mask from ``normalize_gates``."""
    def build(*gates: int) -> int:
        return normalize_gates(list(gates)).mask
    return build
