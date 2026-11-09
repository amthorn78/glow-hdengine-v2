#!/usr/bin/env python3
"""Score-distribution utility (HDE-CRD-0003 S16).

Reports how the admitted release's compat results fall into bands over a population.
Every pair is scored through ``engine.compat.compute.evaluate_pair`` with the admitted
bundle, and every band is read from its result, so the tool adds no second scoring
surface.

Modes:

* ``reference`` scores the governed synthetic reference corpus
  (``reference_corpus_v1.json``, pinned by SHA-256) and compares it with the frozen
  baseline (``reference_baseline_v1.json``, exact counts) or with the Magic10 v2
  target mix.
* ``stored`` scores every pair of an explicit selection of stored people, read through
  the production Reader's read-only path, and compares it with the target mix. It
  emits aggregates only: no identity and no per-person or per-pair value.

It runs only under the closed determinism rails and only from the repository root,
and it writes nothing. Exit codes: ``0`` -- a report on stdout (canonical JSON, one
LF); ``5`` -- refusal, one value-free token on stderr; argparse usage errors keep the
parser's exit status.
"""
from __future__ import annotations

import argparse
import decimal
import hashlib
import json
import os
import stat
import sys
from collections import Counter
from pathlib import Path
from typing import Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.mapped_cache import MappedCacheError, read_current_mapped_bodygraph  # noqa: E402
from engine.bodygraph.projection import (  # noqa: E402
    BodyGraphProjectionError, is_gate_ingress_code, strict_canonical_uuid,
)
from engine.bodygraph.resolver import ResolvedCompatChart, resolve_compat_chart  # noqa: E402
from engine.compat.compute import EvaluationParty, evaluate_pair, evaluation_party  # noqa: E402
from engine.compat.error_tokens import CompatBoundaryError  # noqa: E402
from engine.config.registry_loader import (  # noqa: E402
    AdmittedMechanicsBundle, RegistryConfigError, load_active_mechanics_bundle,
)
from engine.db import DBAccess  # noqa: E402
from engine.db.errors import AdapterError  # noqa: E402
from engine.magic10.composite import _classify_channels  # noqa: E402
from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, expected_env  # noqa: E402
from engine.serializer.canon import sercanon  # noqa: E402

REPORT_SCHEMA = "score_distribution_report.v1"
CORPUS_SCHEMA = "score_distribution_reference_corpus.v1"
BASELINE_SCHEMA = "score_distribution_baseline.v1"
CORPUS_PATH = ROOT / "tools/score_distribution/reference_corpus_v1.json"
BASELINE_PATH = ROOT / "tools/score_distribution/reference_baseline_v1.json"
# P-5.5: the corpus is a governed input; only these bytes are accepted.
REFERENCE_CORPUS_SHA256 = "740d1a3acc2557832431ac4fd14f69223ed6c2cb402329619af97e8e66c8a873"

BANDS = ("Cool", "Open", "Warm", "Glow")
# The Magic10 v2 target mix and its recalibration tolerance (HDE Build Notes, the
# Magic10 v2 adoption decision, "Bands"; HDE Build Checklist -- Fermentation HDE-FERM009).
TARGET_MIX_PERCENT = {"Cool": 30, "Open": 35, "Warm": 25, "Glow": 10}
TOLERANCE_POINTS = 5
PERCENTILES = (10, 25, 50, 75, 90, 95, 99)
EXCLUSION_KEYS = ("duplicate", "gates_invalid", "missing", "payload_invalid", "row_invalid")
MIN_SCORED_PEOPLE = 2
MAX_STORED_PEOPLE = 1000
SELECTION_FILE_MAX_BYTES = 1_048_576
# ``read_current_mapped_bodygraph`` folds a multi-row current view into its row-contract
# refusal with this exact message (the readiness tool pins the same text).
DUPLICATE_ROW_MESSAGE = "current view returned more than one row"
REFUSAL_EXIT_CODE = 5

WORKING_DIRECTORY_INVALID = "SCORE_DISTRIBUTION_WORKING_DIRECTORY_INVALID"
CORPUS_INVALID = "SCORE_DISTRIBUTION_CORPUS_INVALID"
BASELINE_INVALID = "SCORE_DISTRIBUTION_BASELINE_INVALID"
RELEASE_NOT_ADMITTED = "SCORE_DISTRIBUTION_RELEASE_NOT_ADMITTED"
SELECTION_EMPTY = "SCORE_DISTRIBUTION_SELECTION_EMPTY"
SELECTION_INVALID = "SCORE_DISTRIBUTION_SELECTION_INVALID"
SELECTION_TOO_LARGE = "SCORE_DISTRIBUTION_SELECTION_TOO_LARGE"
UNAVAILABLE = "SCORE_DISTRIBUTION_UNAVAILABLE"
POPULATION_TOO_SMALL = "SCORE_DISTRIBUTION_POPULATION_TOO_SMALL"
SCORING_FAILED = "SCORE_DISTRIBUTION_SCORING_FAILED"

_SHARE_QUANTUM = decimal.Decimal("0.000001")
_POINTS_QUANTUM = decimal.Decimal("0.01")


class Refusal(RuntimeError):
    """Value-free refusal: no report is emitted."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


# --- statistics (exact and platform-independent) --------------------------------------

def share(count: int, total: int) -> str:
    """``count / total`` as a six-decimal string, rounded half to even."""
    with decimal.localcontext() as context:
        context.prec = 50
        return str((decimal.Decimal(count) / decimal.Decimal(total)).quantize(
            _SHARE_QUANTUM, rounding=decimal.ROUND_HALF_EVEN))


def points(count: int, total: int, minus: int = 0) -> str:
    """``100 * count / total - minus`` in percentage points, two decimals, half to even."""
    with decimal.localcontext() as context:
        context.prec = 50
        value = decimal.Decimal(100 * count) / decimal.Decimal(total) - decimal.Decimal(minus)
        return str(value.quantize(_POINTS_QUANTUM, rounding=decimal.ROUND_HALF_EVEN))


def beyond_tolerance(count: int, total: int, target_percent: int) -> bool:
    """True when the band share differs from the target by more than the tolerance."""
    return abs(100 * count - target_percent * total) > TOLERANCE_POINTS * total


def nearest_rank(sorted_values: Sequence[int], percentile: int) -> int:
    """The record's percentile: index ``min(n - 1, p * n // 100)`` of the sorted values."""
    n = len(sorted_values)
    return sorted_values[min(n - 1, percentile * n // 100)]


def percentiles(values: Sequence[int]) -> dict[str, int]:
    ordered = sorted(values)
    result = {"min": ordered[0], "max": ordered[-1]}
    result.update({f"p{p}": nearest_rank(ordered, p) for p in PERCENTILES})
    return result


def zero_share(values: Sequence[int]) -> dict[str, object]:
    count = sum(1 for value in values if value == 0)
    return {"count": count, "share": share(count, len(values))}


def tie_share(values: Sequence[int]) -> dict[str, object]:
    """The largest share of results with one exact non-zero score (lowest score on a tie)."""
    non_zero = Counter(value for value in values if value != 0)
    if not non_zero:
        return {"score": None, "count": 0, "share": share(0, len(values))}
    top = max(non_zero.values())
    return {"score": min(score for score, count in non_zero.items() if count == top),
            "count": top, "share": share(top, len(values))}


def histogram_summary(counts: Sequence[int]) -> dict[str, object]:
    """Nearest-rank summary of values given as a histogram (index = value)."""
    total = sum(counts)

    def at(rank: int) -> int:
        seen = 0
        for value, count in enumerate(counts):
            seen += count
            if seen > rank:
                return value
        raise ValueError("rank outside the histogram")

    return {"counts": list(counts), "min": at(0), "p50": at(min(total - 1, 50 * total // 100)),
            "p90": at(min(total - 1, 90 * total // 100)), "max": at(total - 1)}


class Distribution:
    """Aggregates of scored pairs; holds no identity."""

    def __init__(self, bundle: AdmittedMechanicsBundle) -> None:
        self.categories = tuple(bundle.registry.magic10_order)
        self.scores: dict[str, list[int]] = {category: [] for category in self.categories}
        self.bands: dict[str, Counter[str]] = {category: Counter() for category in self.categories}
        self.variety: Counter[int] = Counter()
        self.channels = [0] * (len(bundle.registry.channels) + 1)
        self.pairs = 0

    def add(self, result: Mapping[str, object], channels_formed: int) -> None:
        rows = result["categories"]
        if [row["category_id"] for row in rows] != list(self.categories):
            raise Refusal(f"{SCORING_FAILED}:category_order")
        for row in rows:
            self.scores[row["category_id"]].append(row["score"])
            self.bands[row["category_id"]][row["band"]] += 1
        self.variety[len({row["band"] for row in rows})] += 1
        self.channels[channels_formed] += 1
        self.pairs += 1

    def band_counts(self) -> dict[str, object]:
        per_category = {category: {band: self.bands[category][band] for band in BANDS}
                        for category in self.categories}
        overall = {band: sum(per_category[category][band] for category in self.categories) for band in BANDS}
        return {"overall": overall, "per_category": per_category}

    def report_body(self) -> dict[str, object]:
        counts = self.band_counts()
        results = self.pairs
        all_scores = [score for category in self.categories for score in self.scores[category]]
        return {
            "category_results": results * len(self.categories),
            "band_counts": counts,
            "band_shares": {
                "overall": {band: share(counts["overall"][band], len(all_scores)) for band in BANDS},
                "per_category": {category: {band: share(counts["per_category"][category][band], results)
                                            for band in BANDS} for category in self.categories},
            },
            "band_variety_per_pair": {str(k): self.variety[k] for k in range(1, len(BANDS) + 1)},
            "score_percentiles": {
                "overall": percentiles(all_scores),
                "per_category": {category: percentiles(self.scores[category]) for category in self.categories},
            },
            "zero_share": {
                "overall": zero_share(all_scores),
                "per_category": {category: zero_share(self.scores[category]) for category in self.categories},
            },
            "tie_share": {"per_category": {category: tie_share(self.scores[category])
                                           for category in self.categories}},
            "channels_formed_per_pair": histogram_summary(self.channels),
        }


def compare_baseline(counts: Mapping[str, object], baseline: Mapping[str, object],
                     bundle: AdmittedMechanicsBundle) -> dict[str, object]:
    """Exact count equality with the frozen baseline, overall and per category (P-5.4)."""
    frozen = baseline["band_counts"]

    def rows(measured: Mapping[str, int], expected: Mapping[str, int]) -> dict[str, object]:
        return {band: {"baseline": expected[band], "measured": measured[band],
                       "difference": measured[band] - expected[band]} for band in BANDS}

    overall = rows(counts["overall"], frozen["overall"])
    per_category = {category: rows(counts["per_category"][category], frozen["per_category"][category])
                    for category in counts["per_category"]}
    equal = all(row["difference"] == 0 for row in overall.values()) and all(
        row["difference"] == 0 for bands in per_category.values() for row in bands.values())
    return {
        "against": "baseline",
        "baseline_release": dict(baseline["release"]),
        "release_equal": baseline["release"]["release_id"] == bundle.release_id,
        "equal": equal,
        "overall": overall,
        "per_category": per_category,
    }


def compare_target(counts: Mapping[str, object]) -> dict[str, object]:
    """Band shares against the target mix, with the per-category tolerance."""
    overall_counts = counts["overall"]
    overall_total = sum(overall_counts.values())
    overall = {band: {"share_points": points(overall_counts[band], overall_total),
                      "difference_points": points(overall_counts[band], overall_total, TARGET_MIX_PERCENT[band])}
               for band in BANDS}
    per_category: dict[str, object] = {}
    beyond: list[str] = []
    for category, category_counts in counts["per_category"].items():
        total = sum(category_counts.values())
        rows = {band: {"share_points": points(category_counts[band], total),
                       "difference_points": points(category_counts[band], total, TARGET_MIX_PERCENT[band]),
                       "beyond_tolerance": beyond_tolerance(category_counts[band], total, TARGET_MIX_PERCENT[band])}
                for band in BANDS}
        per_category[category] = rows
        if any(row["beyond_tolerance"] for row in rows.values()):
            beyond.append(category)
    return {
        "against": "target",
        "target_mix_percent": dict(TARGET_MIX_PERCENT),
        "tolerance_points": TOLERANCE_POINTS,
        "overall": overall,
        "per_category": per_category,
        "categories_beyond_tolerance": beyond,
    }


# --- preconditions -----------------------------------------------------------------

def require_closed_rails() -> None:
    """Refuse unless every determinism pin is closed; the token names each unmet pin
    with its required value, never the value found in the environment."""
    current = expected_env()
    unmet = {key: value for key, value in DETERMINISM_ENV_PINS.items() if current.get(key) != value}
    if unmet:
        raise Refusal(f"RAILS_CLOSED_REQUIRED:{sorted(unmet.items())}")


def require_repository_root() -> None:
    """The narrative router loads ``catalog/narratives`` relative to the working directory."""
    try:
        here = Path.cwd().resolve()
    except OSError:
        raise Refusal(WORKING_DIRECTORY_INVALID) from None
    if here != ROOT.resolve():
        raise Refusal(WORKING_DIRECTORY_INVALID)


def admit() -> AdmittedMechanicsBundle:
    try:
        return load_active_mechanics_bundle()
    except RegistryConfigError as exc:
        raise Refusal(f"{RELEASE_NOT_ADMITTED}:{exc.code}") from None


# --- scoring -------------------------------------------------------------------------

def score_pairs(bundle: AdmittedMechanicsBundle, parties: Sequence[EvaluationParty],
                pairs: Sequence[Sequence[int]]) -> Distribution:
    distribution = Distribution(bundle)
    channels = bundle.registry.channels

    def provider() -> AdmittedMechanicsBundle:
        return bundle

    for a, b in pairs:
        left, right = parties[a], parties[b]
        try:
            result = evaluate_pair(left, right, bundle_provider=provider)
        except CompatBoundaryError as exc:
            raise Refusal(f"{SCORING_FAILED}:{exc.token}") from None
        if result.get("eligible") is False:
            raise Refusal(f"{SCORING_FAILED}:ineligible_self")
        formed = sum(1 for row in _classify_channels(left.gates.mask, right.gates.mask, channels)
                     if row.state != "none")
        distribution.add(result, formed)
    return distribution


def build_report(mode: str, bundle: AdmittedMechanicsBundle, population: Mapping[str, object],
                 distribution: Distribution, comparison: Mapping[str, object]) -> dict[str, object]:
    report: dict[str, object] = {
        "schema": REPORT_SCHEMA,
        "mode": mode,
        "read_only": True,
        "release": {"release_id": bundle.release_id, "version": bundle.manifest.version,
                    "config_id": bundle.mechanics["config_id"]},
        "population": dict(population),
        "comparison": dict(comparison),
    }
    report.update(distribution.report_body())
    return report


# --- reference mode ------------------------------------------------------------------

def _is_int(value: object) -> bool:
    return type(value) is int


def load_corpus(path: Path | None = None) -> tuple[str, list[dict[str, object]], list[list[int]]]:
    """Return the pinned corpus (digest, people, pairs) or refuse before parsing other bytes."""
    try:
        raw = (CORPUS_PATH if path is None else path).read_bytes()
    except OSError:
        raise Refusal(CORPUS_INVALID) from None
    digest = hashlib.sha256(raw).hexdigest()
    if digest != REFERENCE_CORPUS_SHA256:
        raise Refusal(CORPUS_INVALID)
    try:
        corpus = json.loads(raw.decode("utf-8"))
    except (UnicodeError, ValueError):
        raise Refusal(CORPUS_INVALID) from None
    if not isinstance(corpus, dict) or corpus.get("schema") != CORPUS_SCHEMA or corpus.get("synthetic") is not True:
        raise Refusal(CORPUS_INVALID)
    people, pairs = corpus.get("people"), corpus.get("pairs")
    if not isinstance(people, list) or not isinstance(pairs, list) or len(people) < MIN_SCORED_PEOPLE:
        raise Refusal(CORPUS_INVALID)
    for person in people:
        if (not isinstance(person, dict) or not isinstance(person.get("id"), str)
                or not isinstance(person.get("gates"), list)):
            raise Refusal(CORPUS_INVALID)
    for pair in pairs:
        if (not isinstance(pair, list) or len(pair) != 2 or not all(_is_int(i) for i in pair)
                or not all(0 <= i < len(people) for i in pair) or pair[0] == pair[1]):
            raise Refusal(CORPUS_INVALID)
    return digest, people, pairs


def load_baseline(bundle: AdmittedMechanicsBundle, corpus_sha256: str, path: Path | None = None) -> dict[str, object]:
    """Return the frozen baseline for this corpus, or refuse."""
    try:
        baseline = json.loads((BASELINE_PATH if path is None else path).read_bytes().decode("utf-8"))
    except (OSError, UnicodeError, ValueError):
        raise Refusal(BASELINE_INVALID) from None
    categories = list(bundle.registry.magic10_order)

    def band_row(row: object) -> bool:
        return isinstance(row, dict) and set(row) == set(BANDS) and all(
            _is_int(row[band]) and row[band] >= 0 for band in BANDS)

    if not isinstance(baseline, dict) or baseline.get("schema") != BASELINE_SCHEMA:
        raise Refusal(BASELINE_INVALID)
    if baseline.get("corpus_sha256") != corpus_sha256:
        raise Refusal(BASELINE_INVALID)
    release = baseline.get("release")
    if not isinstance(release, dict) or set(release) != {"release_id", "version", "config_id"} or not all(
            isinstance(value, str) for value in release.values()):
        raise Refusal(BASELINE_INVALID)
    counts = baseline.get("band_counts")
    if not isinstance(counts, dict) or not band_row(counts.get("overall")):
        raise Refusal(BASELINE_INVALID)
    per_category = counts.get("per_category")
    if not isinstance(per_category, dict) or sorted(per_category) != sorted(categories) or not all(
            band_row(per_category[category]) for category in categories):
        raise Refusal(BASELINE_INVALID)
    for band in BANDS:
        if sum(per_category[category][band] for category in categories) != counts["overall"][band]:
            raise Refusal(BASELINE_INVALID)
    return baseline


def reference_party(person: Mapping[str, object]) -> EvaluationParty:
    """A corpus person as an evaluation party: the gate set and the identity, nothing else."""
    person_id = person["id"]
    chart = {"bodygraph": {"gates": list(person["gates"])}, "person": {"person_uid": person_id},
             "person_uid": person_id}
    try:
        return evaluation_party(ResolvedCompatChart(person_id, chart, "reference_corpus", None, None, None, None))
    except CompatBoundaryError as exc:
        raise Refusal(f"{SCORING_FAILED}:{exc.token}") from None


def run_reference(compare: str) -> dict[str, object]:
    digest, people, pairs = load_corpus()
    bundle = admit()
    baseline = load_baseline(bundle, digest) if compare == "baseline" else None
    parties = [reference_party(person) for person in people]
    distribution = score_pairs(bundle, parties, pairs)
    counts = distribution.band_counts()
    comparison = compare_baseline(counts, baseline, bundle) if baseline is not None else compare_target(counts)
    population = {"corpus_sha256": digest, "people": len(people), "pairs": len(pairs), "synthetic": True}
    return build_report("reference", bundle, population, distribution, comparison)


# --- stored-population mode ----------------------------------------------------------

def read_selection_file(path: Path) -> str:
    """Return the text of a regular, non-symlinked selection file within the size bound.

    The file is opened without following a final symlink and without blocking, and its
    type is checked on the opened descriptor, so nothing but a regular file is read.
    """
    try:
        descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except OSError:
        raise Refusal(SELECTION_INVALID) from None
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise Refusal(SELECTION_INVALID)
        with os.fdopen(descriptor, "rb", closefd=False) as handle:
            raw = handle.read(SELECTION_FILE_MAX_BYTES + 1)
    except OSError:
        raise Refusal(SELECTION_INVALID) from None
    finally:
        os.close(descriptor)
    if len(raw) > SELECTION_FILE_MAX_BYTES:
        raise Refusal(SELECTION_INVALID)
    try:
        return raw.decode("utf-8")
    except UnicodeError:
        raise Refusal(SELECTION_INVALID) from None


def parse_selection(user_ids: Sequence[str], selection_file: Path | None) -> tuple[str, ...]:
    """Return the sorted, duplicate-free canonical selection, or refuse."""
    raw = list(user_ids)
    if selection_file is not None:
        for line in read_selection_file(selection_file).splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                raw.append(stripped)
    if not raw:
        raise Refusal(SELECTION_EMPTY)
    if any(strict_canonical_uuid(value) is None for value in raw) or len(set(raw)) != len(raw):
        raise Refusal(SELECTION_INVALID)
    if len(raw) > MAX_STORED_PEOPLE:
        raise Refusal(SELECTION_TOO_LARGE)
    if len(raw) < MIN_SCORED_PEOPLE:
        raise Refusal(POPULATION_TOO_SMALL)
    return tuple(sorted(raw))


def selection_digest(selection: Sequence[str]) -> str:
    return hashlib.sha256(sercanon(list(selection), sort_keys=True)).hexdigest()


def _projection_exclusion(exc: BodyGraphProjectionError) -> str:
    return "gates_invalid" if is_gate_ingress_code(exc.code) else "payload_invalid"


def read_population(db: DBAccess, selection: Sequence[str]) -> tuple[list[EvaluationParty], Counter[str]]:
    """Read each selected person once, as the production Reader reads and resolves them.

    A person whose row is missing or refused is excluded and counted by reason; a
    database failure refuses the whole run.
    """
    parties: list[EvaluationParty] = []
    excluded: Counter[str] = Counter()
    for user_id in selection:
        try:
            row = read_current_mapped_bodygraph(db, user_id)
        except MappedCacheError as exc:
            if exc.code == "DB_QUERY_FAILED":
                raise Refusal(UNAVAILABLE) from None
            if exc.code == "DB_ROW_CONTRACT_VIOLATED" and str(exc) == DUPLICATE_ROW_MESSAGE:
                excluded["duplicate"] += 1
            elif exc.code == "DB_ROW_CONTRACT_VIOLATED":
                excluded["row_invalid"] += 1
            else:
                excluded["payload_invalid"] += 1
            continue
        except BodyGraphProjectionError as exc:
            excluded[_projection_exclusion(exc)] += 1
            continue
        except RecursionError:
            excluded["payload_invalid"] += 1
            continue
        except AdapterError:
            raise Refusal(UNAVAILABLE) from None
        if row is None:
            excluded["missing"] += 1
            continue
        rows = {user_id: row}
        try:
            resolved = resolve_compat_chart({"user_id": user_id}, source_policy="local", env=None,
                                            local_lookup=rows.get)
            parties.append(evaluation_party(resolved))
        except BodyGraphProjectionError as exc:
            excluded[_projection_exclusion(exc)] += 1
        except CompatBoundaryError as exc:
            excluded["gates_invalid" if exc.reason in ("gates_missing", "gates_invalid") else "payload_invalid"] += 1
    return parties, excluded


def run_stored(user_ids: Sequence[str], selection_file: Path | None) -> dict[str, object]:
    selection = parse_selection(user_ids, selection_file)
    bundle = admit()
    try:
        db = DBAccess.for_current_env()
    except AdapterError:
        raise Refusal(UNAVAILABLE) from None
    parties, excluded = read_population(db, selection)
    if len(parties) < MIN_SCORED_PEOPLE:
        raise Refusal(POPULATION_TOO_SMALL)
    pairs = [(i, j) for i in range(len(parties)) for j in range(i + 1, len(parties))]
    distribution = score_pairs(bundle, parties, pairs)
    population = {
        "selection_sha256": selection_digest(selection),
        "requested": len(selection),
        "scored": len(parties),
        "excluded": {key: excluded[key] for key in EXCLUSION_KEYS},
        "pairs": len(pairs),
        "provider": str(getattr(db, "provider_name", "unknown")),
    }
    return build_report("stored", bundle, population, distribution, compare_target(distribution.band_counts()))


# --- command line --------------------------------------------------------------------

def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="score_distribution.py",
        description="Score distribution of the admitted release, through evaluate_pair (HDE-CRD-0003 S16)",
    )
    modes = parser.add_subparsers(dest="mode", required=True)
    reference = modes.add_parser("reference", help="score the governed synthetic reference corpus")
    reference.add_argument("--compare", choices=("baseline", "target"), default="baseline",
                           help="compare with the frozen baseline (exact counts) or the target mix")
    stored = modes.add_parser("stored", help="score every pair of an explicit selection of stored people")
    stored.add_argument("--user-id", action="append", default=[], metavar="UUID",
                        help="canonical lowercase hyphenated UUID; repeatable")
    stored.add_argument("--selection-file", type=Path, metavar="PATH",
                        help="file with one canonical UUID per line; blank lines and '#' comments ignored")
    stored.add_argument("--compare", choices=("target",), default="target",
                        help="compare with the target mix")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        require_closed_rails()
        require_repository_root()
        if args.mode == "reference":
            report = run_reference(args.compare)
        else:
            report = run_stored(args.user_id, args.selection_file)
    except Refusal as exc:
        sys.stderr.write(f"{exc.code}\n")
        return REFUSAL_EXIT_CODE
    sys.stdout.buffer.write(sercanon(report, sort_keys=True))
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
