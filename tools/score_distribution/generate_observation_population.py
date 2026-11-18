#!/usr/bin/env python3
"""Governed generator of the Magic10 v2 observation population (HDE-FERM009; HDE-EPIC043 WU-PR-08).

HDE-FERM009 observes the v2 band mix on a governed synthetic population that is
independent of the reference corpus (HDE Build Notes, the FERM009 addendum). This
generator writes that population, ``observation_population_v1.json``, by the reference
corpus's recipe with its own seed:

* one ``random.Random(SEED)`` drives everything, birth instants first, then pairs;
* 2,000 birth instants, uniform over 1950-01-01 to 2006-01-01, naive UTC;
* each person's gate set from the chart computation of ``hdchart.py``, Appendix A of
  ``docs/ephemeral/HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md`` in
  ``amthorn78/glow-docs`` (SHA-256 5969513b1177b9b9086dc7abb2a38e0a7eca5f365d7ad3472bb6e25285d3b159),
  restated below with the mean lunar node, which the recipe uses;
* identities ``uuid5(NAMESPACE_URL, '<label>-<seed>-<i>')``;
* 20,000 distinct unordered pairs from the same generator, kept in draw order.

With the reference corpus's seed and label the same code rebuilds the corpus's people
and pairs exactly; the owner test checks that.

Usage, from the repository root under the closed determinism rails::

    python tools/score_distribution/generate_observation_population.py --check
    python tools/score_distribution/generate_observation_population.py --write

``--check`` regenerates the population in memory and compares it with the tracked file;
``--write`` writes it to that one path and prints its SHA-256. Nothing else is written,
and no database, network or vendor is reached. The score-distribution utility never
imports this module.

Exit codes: ``0`` -- equal (``--check``) or written (``--write``); ``1`` -- the tracked
file differs (``OBSERVATION_POPULATION_STALE``); ``5`` -- refusal, one value-free token on
stderr (open rails, another working directory, a PyEphem version other than 4.2.1);
argparse usage errors keep the parser's exit status.

Stated limits: the population is synthetic and cannot show how real people fall. Only
PyEphem 4.2.1 is accepted. The provenance names the interpreter line CI pins (Python
3.12); another interpreter is outside the pin, and the pinned bytes are authoritative.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import math
import random
import sys
import uuid
from pathlib import Path
from typing import Sequence

import ephem

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, expected_env  # noqa: E402
from engine.serializer.canon import sercanon  # noqa: E402

SCHEMA = "score_distribution_observation_population.v1"
OUTPUT_PATH = ROOT / "tools/score_distribution/observation_population_v1.json"
SEED = 20261118
REFERENCE_SEED = 20261101
LABEL = "observation-synthetic"
PEOPLE = 2000
PAIRS = 20000
EPHEM_VERSION = "4.2.1"
BIRTH_START = dt.datetime(1950, 1, 1)
BIRTH_END = dt.datetime(2006, 1, 1)

REFUSAL_EXIT_CODE = 5
STALE_EXIT_CODE = 1
WORKING_DIRECTORY_INVALID = "OBSERVATION_POPULATION_WORKING_DIRECTORY_INVALID"
EPHEMERIS_UNSUPPORTED = "OBSERVATION_POPULATION_EPHEMERIS_UNSUPPORTED"
STALE = "OBSERVATION_POPULATION_STALE"
WRITTEN = "OBSERVATION_POPULATION_WRITTEN"

PROVENANCE = {
    "births": ("2,000 instants, datetime(1950, 1, 1) + timedelta(seconds=random.Random(seed).random() * span), "
               "span to datetime(2006, 1, 1), naive UTC"),
    "chart_builder": {
        "ephemeris": "PyEphem 4.2.1",
        "lunar_node": "mean",
        "python": "3.12",
        "script": "hdchart.py, the record's Appendix A, restated in the generator with the mean node",
        "sha256": "5969513b1177b9b9086dc7abb2a38e0a7eca5f365d7ad3472bb6e25285d3b159",
    },
    "generator": "tools/score_distribution/generate_observation_population.py",
    "identities": "uuid5(NAMESPACE_URL, 'observation-synthetic-20261118-<i>')",
    "independence": ("its own seed 20261118, not the reference corpus seed 20261101; no identity or birth instant "
                     "shared with tools/score_distribution/reference_corpus_v1.json, and not a subset of it"),
    "pairs": ("20,000 distinct unordered pairs from the same generator, rng.sample(range(2000), 2), kept in draw "
              "order, a draw that repeats an earlier unordered pair skipped"),
    "record": {
        "git_blob": "cbef6c7b4f9c787c60e81efee2c1053075644e81",
        "path": "docs/ephemeral/HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md",
        "repository": "amthorn78/glow-docs",
    },
    "seed": 20261118,
    "synthetic": ("synthetic people only: invented birth instants and the gate sets computed from them; "
                  "no real person's data"),
}


class Refusal(RuntimeError):
    """Value-free refusal: nothing is written."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


# --- the chart computation (hdchart.py, the record's Appendix A; mean node) ---------------
# Tropical, geocentric ecliptic longitudes of date from PyEphem; the lunar node is Meeus's
# mean node (Astronomical Algorithms, ch. 47). Design moment: when the Sun stood 88 degrees
# of arc before its natal longitude. Gate wheel: Gate 41 begins at 302 degrees; 64 gates of
# 5.625 degrees each.

WHEEL = [41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3, 27, 24, 2, 23, 8, 20, 16, 35,
         45, 12, 15, 52, 39, 53, 62, 56, 31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
         28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60]
WHEEL_START = 302.0
PLANETS = (ephem.Moon, ephem.Mercury, ephem.Venus, ephem.Mars, ephem.Jupiter, ephem.Saturn,
           ephem.Uranus, ephem.Neptune, ephem.Pluto)


def gate_of(lon: float) -> int:
    return WHEEL[int(((lon - WHEEL_START) % 360.0) / 5.625)]


def _eclon(body, d: ephem.Date) -> float:
    body.compute(d, epoch=d)
    return math.degrees(float(ephem.Ecliptic(body, epoch=d).lon)) % 360.0


def _mean_node(d: ephem.Date) -> float:
    t = (ephem.julian_date(d) - 2451545.0) / 36525.0
    om = 125.0445479 - 1934.1362891 * t + 0.0020754 * t * t + t ** 3 / 467441 - t ** 4 / 60616000
    return om % 360.0


def _sun(d: ephem.Date) -> float:
    return _eclon(ephem.Sun(), d)


def _design_date(birth: ephem.Date) -> ephem.Date:
    target = (_sun(birth) - 88.0) % 360.0
    d = ephem.Date(birth - 88.5)
    for _ in range(60):  # Newton steps on the Sun's ~0.9856 deg/day motion
        diff = ((_sun(d) - target + 180.0) % 360.0) - 180.0
        if abs(diff) < 1e-7:
            break
        d = ephem.Date(d - diff / 0.9856)
    return d


def _activations(d: ephem.Date) -> list[float]:
    sun = _sun(d)
    node = _mean_node(d)
    lons = [sun, (sun + 180.0) % 360.0, node, (node + 180.0) % 360.0]
    lons += [_eclon(body(), d) for body in PLANETS]
    return lons


def gates_utc(when_utc: dt.datetime) -> list[int]:
    """The sorted gate set of the 26 activations for a naive UTC birth instant."""
    birth = ephem.Date(when_utc.replace(tzinfo=None))
    design = _design_date(birth)
    return sorted({gate_of(lon) for lon in _activations(birth) + _activations(design)})


# --- the recipe ----------------------------------------------------------------------------

def _draw_births(rng: random.Random, count: int) -> list[dt.datetime]:
    span = (BIRTH_END - BIRTH_START).total_seconds()
    return [BIRTH_START + dt.timedelta(seconds=rng.random() * span) for _ in range(count)]


def birth_instants(seed: int, count: int = PEOPLE) -> list[dt.datetime]:
    """The birth instants of a population with this seed: the generator's first draws."""
    return _draw_births(random.Random(seed), count)


def draw(seed: int, label: str, people: int = PEOPLE,
         pairs: int = PAIRS) -> tuple[list[dt.datetime], list[dict[str, object]], list[list[int]]]:
    """Births, people and pairs of the recipe for one seed and identity label."""
    rng = random.Random(seed)
    births = _draw_births(rng, people)
    persons: list[dict[str, object]] = [
        {"gates": gates_utc(birth), "id": str(uuid.uuid5(uuid.NAMESPACE_URL, f"{label}-{seed}-{i}"))}
        for i, birth in enumerate(births)]
    seen: set[tuple[int, int]] = set()
    drawn: list[list[int]] = []
    while len(drawn) < pairs:
        a, b = rng.sample(range(people), 2)
        key = (min(a, b), max(a, b))
        if key in seen:
            continue
        seen.add(key)
        drawn.append([a, b])
    return births, persons, drawn


def population_document() -> dict[str, object]:
    _births, people, pairs = draw(SEED, LABEL)
    return {"schema": SCHEMA, "synthetic": True, "people": people, "pairs": pairs, "provenance": PROVENANCE}


def population_bytes() -> bytes:
    return sercanon(population_document())


# --- preconditions and command line --------------------------------------------------------

def require_closed_rails() -> None:
    """The utility's rails check: the token names each unmet pin with its required value."""
    current = expected_env()
    unmet = {key: value for key, value in DETERMINISM_ENV_PINS.items() if current.get(key) != value}
    if unmet:
        raise Refusal(f"RAILS_CLOSED_REQUIRED:{sorted(unmet.items())}")


def require_repository_root() -> None:
    try:
        here = Path.cwd().resolve()
    except OSError:
        raise Refusal(WORKING_DIRECTORY_INVALID) from None
    if here != ROOT.resolve():
        raise Refusal(WORKING_DIRECTORY_INVALID)


def require_ephemeris() -> None:
    if getattr(ephem, "__version__", None) != EPHEM_VERSION:
        raise Refusal(EPHEMERIS_UNSUPPORTED)


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="generate_observation_population.py",
        description="Generate or check the governed synthetic observation population (HDE-FERM009)",
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true", help="compare the regenerated bytes with the tracked file")
    action.add_argument("--write", action="store_true", help="write the population to its one tracked path")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        require_closed_rails()
        require_repository_root()
        require_ephemeris()
    except Refusal as exc:
        sys.stderr.write(f"{exc.code}\n")
        return REFUSAL_EXIT_CODE
    raw = population_bytes()
    if args.write:
        OUTPUT_PATH.write_bytes(raw)
        sys.stdout.write(f"{WRITTEN}:{hashlib.sha256(raw).hexdigest()}\n")
        sys.stdout.flush()
        return 0
    try:
        tracked = OUTPUT_PATH.read_bytes()
    except OSError:
        tracked = None
    if tracked != raw:
        sys.stderr.write(f"{STALE}\n")
        return STALE_EXIT_CODE
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
