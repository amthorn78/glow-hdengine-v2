"""HDE-CRD-0003 S16 (WU-PR-03): the score-distribution utility, its corpus and its baseline.

The reference gate runs the real command twice; the stored-population mode runs only
against the PR04 current-view DB fake. No database, vendor or network is reached, and
nothing is written.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tomllib
import uuid
from collections import Counter
from types import SimpleNamespace
from pathlib import Path

import pytest

from ci.checks import classify_ci_changes as classifier
from engine.bodygraph import mapped_cache
from engine.bodygraph import resolver
from engine.bodygraph import vendor_client
from engine.bodygraph.resolver import ResolvedCompatChart
from engine.compat.compute import evaluate_pair, evaluation_party
from engine.config.registry_loader import load_active_mechanics_bundle
from engine.db.errors import PrimaryUnavailable, SqlExecError
from engine.serializer.canon import sercanon
from tests.support.pr04_fixtures import FakeCurrentViewDB, complete_chart
from tools.config import artifacts as config_artifacts
from tools.score_distribution import generate_observation_population as generator
from tools.score_distribution import score_distribution as tool

ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = "tools/score_distribution/score_distribution.py"
GENERATOR_PATH = "tools/score_distribution/generate_observation_population.py"
OBSERVATION_PATH = "tools/score_distribution/observation_population_v1.json"
TOOL_FILES = (
    GENERATOR_PATH,
    OBSERVATION_PATH,
    "tools/score_distribution/reference_baseline_v1.json",
    "tools/score_distribution/reference_corpus_v1.json",
    TOOL_PATH,
)
THIS_TEST = "tests/tools/test_score_distribution.py"
# The frozen reference measure: the v2 release's mix over the pinned corpus, measured at the
# HDE-EPIC043 WU-PR-10 cut (release 2.0.0) and re-frozen in reference_baseline_v1.json.
RECORD_COUNTS = {"Cool": 59379, "Open": 70026, "Warm": 51360, "Glow": 19235}
POPULATION_SHA256 = "cc31b34794f3d990b0fc98d8c9caee20d04b0610030c57839d0283caed9741e3"
REPORT_KEYS = {
    "schema", "mode", "read_only", "release", "population", "category_results", "band_counts", "band_shares",
    "band_variety_per_pair", "score_percentiles", "zero_share", "tie_share", "channels_formed_per_pair", "comparison",
}
STORED_POPULATION_KEYS = {"selection_sha256", "requested", "scored", "excluded", "pairs", "provider"}


def _uid(name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"s16-owner-test-{name}"))


STORED_UIDS = tuple(_uid(f"person-{i}") for i in range(5))
MISSING_UID = _uid("missing")
FORBIDDEN_STRINGS = (*STORED_UIDS, MISSING_UID, "person_uid", "bodygraph", "birthDateUtc", "Emotional",
                     "Manifesting", "2000-01-01", "\"gates\"", "DATABASE_URL", "postgres")


@pytest.fixture(autouse=True)
def _rails_and_spies(monkeypatch):
    for key, value in {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev"}.items():
        monkeypatch.setenv(key, value)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(resolver.HdApiClient, "from_env", lambda **kwargs: pytest.fail("vendor client constructed"))
    monkeypatch.setattr(resolver, "ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("ingest attempted"))
    monkeypatch.setattr(resolver, "persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr(mapped_cache, "persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr(vendor_client.HdApiClient, "__init__", lambda self, *a, **k: pytest.fail("vendor client constructed"))


@pytest.fixture(scope="module")
def bundle():
    return load_active_mechanics_bundle()


@pytest.fixture(scope="module")
def corpus():
    return json.loads((ROOT / "tools/score_distribution/reference_corpus_v1.json").read_bytes())


def _run(argv, capfdbinary):
    code = tool.main(argv)
    out, err = capfdbinary.readouterr()
    return code, out, err


def _git_status() -> str:
    return subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout


def _stored_charts(corpus) -> dict[str, dict]:
    """Five complete charts whose Gates are the first five corpus people's, as strings."""
    return {uid: complete_chart(uid, [str(g) for g in corpus["people"][i]["gates"]])
            for i, uid in enumerate(STORED_UIDS)}


# --- T-1, T-2: the governed inputs ----------------------------------------------------

def test_reference_corpus_is_the_pinned_synthetic_population(corpus) -> None:
    raw = (ROOT / "tools/score_distribution/reference_corpus_v1.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == tool.REFERENCE_CORPUS_SHA256
    assert raw == sercanon(corpus)
    assert corpus["schema"] == tool.CORPUS_SCHEMA and corpus["synthetic"] is True
    provenance = corpus["provenance"]
    assert set(provenance) == {"record", "seed", "births", "identities", "pairs", "chart_builder", "validation"}
    assert provenance["seed"] == 20261101
    assert provenance["record"]["path"] == "docs/ephemeral/HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md"
    assert provenance["chart_builder"]["sha256"] == "5969513b1177b9b9086dc7abb2a38e0a7eca5f365d7ad3472bb6e25285d3b159"
    assert provenance["chart_builder"]["ephemeris"] == "PyEphem 4.2.1"
    assert provenance["chart_builder"]["lunar_node"] == "mean"
    people, pairs = corpus["people"], corpus["pairs"]
    assert [person["id"] for person in people] == [
        str(uuid.uuid5(uuid.NAMESPACE_URL, f"scorerange-synthetic-20261101-{i}")) for i in range(2000)]
    for person in people:
        assert set(person) == {"id", "gates"}
        gates = person["gates"]
        assert gates and gates == sorted(set(gates)) and all(type(g) is int and 1 <= g <= 64 for g in gates)
    assert len(pairs) == 20000
    assert all(len(pair) == 2 and pair[0] != pair[1] and all(0 <= i < 2000 for i in pair) for pair in pairs)
    assert len({(min(pair), max(pair)) for pair in pairs}) == 20000
    assert hashlib.sha256(sercanon({"people": people, "pairs": pairs})).hexdigest() == POPULATION_SHA256


def test_frozen_baseline_is_the_records_measured_mix(bundle) -> None:
    baseline = tool.load_baseline(bundle, tool.REFERENCE_CORPUS_SHA256)
    raw = (ROOT / "tools/score_distribution/reference_baseline_v1.json").read_bytes()
    assert raw == sercanon(baseline)
    assert baseline["schema"] == tool.BASELINE_SCHEMA
    assert baseline["corpus_sha256"] == tool.REFERENCE_CORPUS_SHA256
    assert baseline["release"] == {"version": "2.0.0", "config_id": "m10-relevance-centers-type-v2.0.0",
                                   "release_id": bundle.release_id}
    counts = baseline["band_counts"]
    assert counts["overall"] == RECORD_COUNTS
    assert list(counts["per_category"]) == sorted(bundle.registry.magic10_order)
    assert sum(sum(row.values()) for row in counts["per_category"].values()) == 200000


# --- T-3: the gate (criteria 1 and 2) ------------------------------------------------

def _closed_env(hash_seed: int) -> dict[str, str]:
    return {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.environ.get("HOME", str(ROOT)),
        "LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev",
        "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": str(hash_seed), "PYTHONPATH": str(ROOT),
    }


def test_reference_run_reproduces_the_frozen_counts_twice_byte_identically(bundle) -> None:
    before = _git_status()
    runs = [subprocess.Popen([sys.executable, TOOL_PATH, "reference"], cwd=ROOT, env=_closed_env(seed),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE) for seed in (1, 2)]
    outputs = [run.communicate(timeout=1800) for run in runs]
    assert [run.returncode for run in runs] == [0, 0]
    assert [err for _out, err in outputs] == [b"", b""]
    first, second = (out for out, _err in outputs)
    assert first == second and first.endswith(b"\n") and first.count(b"\n") == 1
    report = json.loads(first)
    assert set(report) == REPORT_KEYS and report["mode"] == "reference"
    assert report["band_counts"]["overall"] == RECORD_COUNTS
    assert report["category_results"] == 200000
    assert report["population"] == {"corpus_sha256": tool.REFERENCE_CORPUS_SHA256, "people": 2000,
                                    "pairs": 20000, "synthetic": True}
    assert report["release"]["release_id"] == bundle.release_id
    assert report["comparison"]["against"] == "baseline" and report["comparison"]["equal"] is True
    assert _git_status() == before


# --- T-4: the measures on known inputs -------------------------------------------------

def test_report_statistics_are_defined_on_known_inputs() -> None:
    values = [0, 0, 5, 5, 7, 7, 9, 12, 30, 99]
    assert tool.percentiles(values) == {"min": 0, "p10": 0, "p25": 5, "p50": 7, "p75": 12, "p90": 99,
                                        "p95": 99, "p99": 99, "max": 99}
    assert tool.zero_share(values) == {"count": 2, "share": "0.200000"}
    # 5 and 7 each occur twice: the lowest score wins the tie.
    assert tool.tie_share(values) == {"score": 5, "count": 2, "share": "0.200000"}
    assert tool.tie_share([0, 0, 0]) == {"score": None, "count": 0, "share": "0.000000"}
    assert tool.share(1, 3) == "0.333333" and tool.share(2, 3) == "0.666667"
    assert tool.share(1, 8_000_000) == "0.000000"
    assert tool.share(3, 2_000_000) == "0.000002" and tool.share(5, 2_000_000) == "0.000002"  # half to even
    assert tool.points(1, 8) == "12.50" and tool.points(1, 8, 30) == "-17.50" and tool.points(1, 3) == "33.33"
    # Exactly 5 points from the target is not beyond the tolerance; just above it is.
    assert tool.beyond_tolerance(35, 100, 30) is False and tool.beyond_tolerance(25, 100, 30) is False
    assert tool.beyond_tolerance(351, 1000, 30) is True and tool.beyond_tolerance(249, 1000, 30) is True
    assert tool.histogram_summary([0, 0, 3, 5, 2]) == {"counts": [0, 0, 3, 5, 2], "min": 2, "p50": 3,
                                                       "p90": 4, "max": 4}
    counts = {"overall": {"Cool": 6, "Open": 2, "Warm": 2, "Glow": 0},
              "per_category": {"harmony": {"Cool": 3, "Open": 1, "Warm": 1, "Glow": 0},
                               "heat": {"Cool": 3, "Open": 1, "Warm": 1, "Glow": 0}}}
    target = tool.compare_target(counts)
    assert target["overall"]["Cool"] == {"share_points": "60.00", "difference_points": "30.00"}
    assert target["per_category"]["harmony"]["Glow"] == {"share_points": "0.00", "difference_points": "-10.00",
                                                         "beyond_tolerance": True}
    assert target["categories_beyond_tolerance"] == ["harmony", "heat"]
    assert target["target_mix_percent"] == {"Cool": 30, "Open": 35, "Warm": 25, "Glow": 10}


# --- T-5, T-6: the stored-population mode (criterion 4) ----------------------------------

class _DuplicateRowDB(FakeCurrentViewDB):
    """The PR04 fake, returning two current rows for one identity."""

    def __init__(self, charts, duplicate):
        super().__init__(charts)
        self.duplicate = duplicate

    def query(self, sql, params=None):
        rows = super().query(sql, params)
        return rows * 2 if params[0] == self.duplicate else rows


def _use(monkeypatch, fake) -> None:
    monkeypatch.setattr(tool.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: fake))


def _assert_no_leak(*streams: bytes) -> None:
    for stream in streams:
        text = stream.decode("utf-8")
        for forbidden in FORBIDDEN_STRINGS:
            assert forbidden not in text, forbidden


def test_stored_population_mode_with_a_fake_governed_reader_returns_aggregates_only(
        monkeypatch, capfdbinary, corpus, bundle) -> None:
    charts = _stored_charts(corpus)
    fake = FakeCurrentViewDB(charts)
    _use(monkeypatch, fake)
    argv = ["stored", *(arg for uid in (*STORED_UIDS, MISSING_UID) for arg in ("--user-id", uid))]
    code, out, err = _run(argv, capfdbinary)
    assert (code, err) == (0, b"") and out.endswith(b"\n") and out.count(b"\n") == 1
    _assert_no_leak(out, err)
    report = json.loads(out)
    assert set(report) == REPORT_KEYS and report["mode"] == "stored" and report["read_only"] is True
    population = report["population"]
    assert set(population) == STORED_POPULATION_KEYS
    assert (population["requested"], population["scored"], population["pairs"]) == (6, 5, 10)
    assert population["excluded"] == {"duplicate": 0, "gates_invalid": 0, "missing": 1, "payload_invalid": 0,
                                      "row_invalid": 0}
    assert population["selection_sha256"] == tool.selection_digest(sorted((*STORED_UIDS, MISSING_UID)))
    assert report["comparison"]["against"] == "target"
    # The same scoring surface: evaluate_pair on the same five charts gives the same counts.
    parties = [evaluation_party(ResolvedCompatChart(uid, charts[uid], "resolved", None, None, None, None))
               for uid in sorted(STORED_UIDS)]
    expected = Counter()
    for i in range(5):
        for j in range(i + 1, 5):
            for row in evaluate_pair(parties[i], parties[j])["categories"]:
                expected[row["band"]] += 1
    assert report["band_counts"]["overall"] == {band: expected[band] for band in tool.BANDS}
    assert {sql for sql, _params in fake.queries} == {mapped_cache.CURRENT_ROW_SQL}
    assert len(fake.queries) == 6 and fake.writes == []


def test_stored_population_mode_counts_a_duplicate_row_as_excluded(monkeypatch, capfdbinary, corpus) -> None:
    _use(monkeypatch, _DuplicateRowDB(_stored_charts(corpus), STORED_UIDS[0]))
    code, out, err = _run(["stored", *(arg for uid in STORED_UIDS for arg in ("--user-id", uid))], capfdbinary)
    assert (code, err) == (0, b"")
    _assert_no_leak(out)
    population = json.loads(out)["population"]
    assert (population["scored"], population["pairs"], population["excluded"]["duplicate"]) == (4, 6, 1)


def test_stored_population_mode_refuses_value_free(monkeypatch, capfdbinary, corpus, tmp_path) -> None:
    def refused(argv, token):
        code, out, err = _run(argv, capfdbinary)
        assert (code, out, err) == (tool.REFUSAL_EXIT_CODE, b"", f"{token}\n".encode())
        _assert_no_leak(err)

    two = [arg for uid in STORED_UIDS[:2] for arg in ("--user-id", uid)]
    _use(monkeypatch, FakeCurrentViewDB(_stored_charts(corpus),
                                        fail=SqlExecError("sql_query_failed", attempts=["DATABASE_URL"], code="sql_query_failed")))
    refused(["stored", *two], tool.UNAVAILABLE)

    def unavailable(cls, *a, **k):
        raise PrimaryUnavailable("missing_database_url", attempts=["DATABASE_URL"], code="missing_database_url")

    monkeypatch.setattr(tool.DBAccess, "for_current_env", classmethod(unavailable))
    refused(["stored", *two], tool.UNAVAILABLE)
    _use(monkeypatch, FakeCurrentViewDB(_stored_charts(corpus)))
    refused(["stored"], tool.SELECTION_EMPTY)
    refused(["stored", "--user-id", STORED_UIDS[0].upper(), "--user-id", STORED_UIDS[1]], tool.SELECTION_INVALID)
    refused(["stored", "--user-id", STORED_UIDS[0], "--user-id", STORED_UIDS[0]], tool.SELECTION_INVALID)
    refused(["stored", "--user-id", STORED_UIDS[0]], tool.POPULATION_TOO_SMALL)
    refused(["stored", "--user-id", STORED_UIDS[0], "--user-id", MISSING_UID], tool.POPULATION_TOO_SMALL)
    many = tmp_path / "many.txt"
    many.write_text("".join(f"{_uid(f'bulk-{i}')}\n" for i in range(tool.MAX_STORED_PEOPLE + 1)))
    refused(["stored", "--selection-file", str(many)], tool.SELECTION_TOO_LARGE)
    link = tmp_path / "link.txt"
    link.symlink_to(many)
    refused(["stored", "--selection-file", str(link)], tool.SELECTION_INVALID)
    oversized = tmp_path / "oversized.txt"
    oversized.write_bytes(b"#" * (tool.SELECTION_FILE_MAX_BYTES + 1))
    refused(["stored", "--selection-file", str(oversized)], tool.SELECTION_INVALID)
    with pytest.raises(SystemExit) as usage:
        tool.main(["stored", *two, "--compare", "baseline"])
    assert usage.value.code == 2


# --- T-7: refusals before any read ---------------------------------------------------

def test_refusals_before_any_read(monkeypatch, capfdbinary, tmp_path) -> None:
    def refused(argv, token):
        assert _run(argv, capfdbinary) == (tool.REFUSAL_EXIT_CODE, b"", f"{token}\n".encode())

    original_load_corpus = tool.load_corpus
    monkeypatch.setattr(tool, "load_corpus", lambda *a, **k: pytest.fail("corpus read before the rails check"))
    monkeypatch.setenv("SAFE_MODE", "0")
    code, out, err = _run(["reference"], capfdbinary)
    assert (code, out) == (tool.REFUSAL_EXIT_CODE, b"") and err.startswith(b"RAILS_CLOSED_REQUIRED:")
    assert b"'SAFE_MODE', '1'" in err and b"'0'" not in err
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.chdir(tmp_path)
    refused(["reference"], tool.WORKING_DIRECTORY_INVALID)
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(tool, "load_corpus", original_load_corpus)
    tampered = tmp_path / "corpus.json"
    raw = bytearray((ROOT / "tools/score_distribution/reference_corpus_v1.json").read_bytes())
    raw[-2] = ord(" ")
    tampered.write_bytes(bytes(raw))
    monkeypatch.setattr(tool, "CORPUS_PATH", tampered)
    refused(["reference"], tool.CORPUS_INVALID)
    monkeypatch.setattr(tool, "CORPUS_PATH", ROOT / "tools/score_distribution/reference_corpus_v1.json")
    other = json.loads((ROOT / "tools/score_distribution/reference_baseline_v1.json").read_bytes())
    other["corpus_sha256"] = "0" * 64
    other_path = tmp_path / "baseline.json"
    other_path.write_bytes(sercanon(other))
    monkeypatch.setattr(tool, "BASELINE_PATH", other_path)
    monkeypatch.setattr(tool, "score_pairs", lambda *a, **k: pytest.fail("scored with an invalid baseline"))
    refused(["reference"], tool.BASELINE_INVALID)


def test_reference_mode_never_constructs_a_database_provider(monkeypatch, capfdbinary, corpus) -> None:
    small = (tool.REFERENCE_CORPUS_SHA256, corpus["people"][:3], [[0, 1], [1, 2], [0, 2]])
    monkeypatch.setattr(tool, "load_corpus", lambda *a, **k: small)
    monkeypatch.setattr(tool.DBAccess, "for_current_env",
                        classmethod(lambda cls, *a, **k: pytest.fail("reference mode constructed DBAccess")))
    code, out, err = _run(["reference", "--compare", "target"], capfdbinary)
    assert (code, err) == (0, b"")
    report = json.loads(out)
    assert report["comparison"]["against"] == "target" and report["population"]["pairs"] == 3


# --- T-8: never a public surface (criterion 5) -----------------------------------------

def test_the_tool_is_never_a_public_surface() -> None:
    tree = ast.parse((ROOT / TOOL_PATH).read_text(encoding="utf-8"))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module)
    allowed = {"__future__", "argparse", "decimal", "hashlib", "json", "os", "stat", "sys", "collections", "pathlib",
               "typing", "engine.bodygraph.mapped_cache", "engine.bodygraph.projection", "engine.bodygraph.resolver",
               "engine.compat.compute", "engine.compat.error_tokens", "engine.config.registry_loader", "engine.db",
               "engine.db.errors", "engine.magic10_v2.kernel", "engine.runtime.determinism_env",
               "engine.serializer.canon"}
    assert imported <= allowed, sorted(imported - allowed)
    forbidden_roots = ("flask", "werkzeug", "adapter", "engine.cli", "engine.http", "presenter", "psycopg",
                       "requests", "urllib", "http", "socket", "subprocess", "tests")
    assert not [name for name in imported if name.split(".")[0] in forbidden_roots or name.startswith(forbidden_roots)]
    tracked = subprocess.run(["git", "ls-files", "-z", "--", "*.py"], cwd=ROOT, capture_output=True,
                             check=True).stdout.decode("utf-8").split("\0")
    referencing = []
    for path in tracked:
        if not path or path.startswith("tests/") or path == TOOL_PATH:
            continue
        text = (ROOT / path).read_text(encoding="utf-8", errors="replace")
        if "tools.score_distribution" in text or "tools/score_distribution" in text or "score_distribution import" in text:
            referencing.append(path)
    # HDE-EPIC043 WU-PR-08: the observation-population generator names its own output path;
    # it is an allowed referencing file, and the tool never imports it.  HDE-EPIC043 WU-PR-10:
    # the cut-record evidence writer reuses the tool's functions in process; it is not a surface.
    assert referencing == ["ci/checks/classify_ci_changes.py", "tools/evidence/generate_hde_epic043_cut_record.py",
                           GENERATOR_PATH]
    scripts = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["scripts"]
    assert scripts == {"hdctl": "engine.cli.main:cli"}
    assert "score_distribution" not in (ROOT / "docs/ENDPOINTS_CATALOG.json").read_text(encoding="utf-8")


# --- T-9: the classifier's tool block -------------------------------------------------

def test_classifier_tool_block_fails_closed() -> None:
    for path in TOOL_FILES:
        assert classifier.changed_test_targets(ROOT, (path,)) == (THIS_TEST,), path
        assert classifier._lanes_for_path(path) == {"db", "product"}, path
    with pytest.raises(ValueError, match="CI_SCORE_DISTRIBUTION_OWNER_TEST_MISSING:tools/score_distribution/notes.txt"):
        classifier.changed_test_targets(ROOT, ("tools/score_distribution/notes.txt",))


# --- HDE-EPIC043 WU-PR-05 (HDE-DIST008.2; HDE Math Spec 5.3.7): the cut mode ----------------
# The cut rule is tested on constructed score lists; they are test inputs, not maxima. The one
# real run scores the pinned corpus under the active release and records no maxima value.

def _oracle(scores, targets=(30, 65, 90)):
    """HDE Math Spec 5.3.7 restated independently: N(s) counted from the score list itself."""
    n, previous, maxima = len(scores), -1, []
    for p in targets:
        candidates = range(previous + 1, 100)
        best = min(candidates, key=lambda s: (abs(100 * sum(1 for x in scores if x <= s) - p * n), s))
        maxima.append(best)
        previous = best
    return maxima + [100]


def _cut(scores):
    rows = tool.cut_maxima(tool.score_histogram(scores))
    return [row["maximum"] for row in rows] + [100], rows


def test_cut_targets_derive_from_the_target_mix() -> None:
    assert tool.cut_targets() == (30, 65, 90)
    assert tool.TARGET_MIX_PERCENT == {"Cool": 30, "Open": 35, "Warm": 25, "Glow": 10}


def test_cut_compares_in_exact_integers_and_takes_the_lower_score_on_a_tie() -> None:
    # n = 3: 100*N(s) against 30*3 = 90, 65*3 = 195, 90*3 = 270. A rounded share would see 33.3%.
    maxima, rows = _cut([0, 1, 2])
    assert maxima == [0, 1, 2, 100]
    assert [(r["cumulative_count"], r["deviation"]) for r in rows] == [(1, 10), (2, 5), (3, 30)]
    # n = 20: N(s) = 5 at s = 0..9 and 7 at s = 10: |500-600| = 100 = |700-600|; the lower (0) wins.
    scores = [0] * 5 + [10, 10] + [50] * 13
    maxima, rows = _cut(scores)
    assert maxima[0] == 0 and rows[0]["deviation"] == 100
    # A flat region above the previous maximum: the lowest s in it.
    assert _cut([0] * 30 + [60] * 35 + [80] * 25 + [100] * 10)[0] == [0, 60, 80, 100]
    assert _cut([5] * 30 + [40] * 35 + [70] * 25 + [99] * 10)[0] == [5, 40, 70, 100]


def test_cut_rule_code_is_integer_only() -> None:
    tree = ast.parse((ROOT / TOOL_PATH).read_text(encoding="utf-8"))
    functions = {node.name: node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
    for name in ("cut_targets", "score_histogram", "cut_maxima"):
        for node in ast.walk(functions[name]):
            assert not isinstance(node, (ast.Div, ast.Pow)), name
            assert not (isinstance(node, ast.Constant) and type(node.value) is float), name
            assert not (isinstance(node, ast.Name) and node.id in {"float", "Decimal", "decimal"}), name
            assert not (isinstance(node, ast.Attribute) and node.attr in {"Decimal"}), name


@pytest.mark.parametrize("scores", [
    list(range(101)) * 3,                       # uniform
    [50] * 99 + [7],                            # one spike
    [10] * 40 + [90] * 60,                      # bimodal
    [33] * 50,                                  # all equal
    [0] * 10 + [100] * 90,                      # mass at the ends
    [95, 96, 97, 98, 99, 100],                  # crowded at the top
], ids=["uniform", "spike", "bimodal", "all-equal", "ends", "top"])
def test_cut_order_bounds_and_cumulative_counts(scores) -> None:
    maxima, rows = _cut(scores)
    assert maxima == _oracle(scores)
    assert maxima[0] < maxima[1] < maxima[2] <= 99 and maxima[3] == 100
    for row in rows:
        assert row["cumulative_count"] == sum(1 for x in scores if x <= row["maximum"])
    # The search starts above the previous maximum, never at 0.
    assert _cut([33] * 50)[0] == [0, 33, 34, 100]


def test_cut_refuses_exhaustion_value_free(monkeypatch, capfdbinary, bundle) -> None:
    scores = [0] * 40 + [99] * 25 + [100] * 35
    with pytest.raises(tool.Refusal) as refused:
        _cut(scores)
    assert refused.value.code == tool.CUT_EXHAUSTED
    distribution = SimpleNamespace(categories=("harmony",), scores={"harmony": scores})
    monkeypatch.setattr(tool, "run_cut", lambda: tool.cut_report(bundle, {}, distribution))
    assert _run(["cut"], capfdbinary) == (tool.REFUSAL_EXIT_CODE, b"", f"{tool.CUT_EXHAUSTED}\n".encode())


@pytest.mark.parametrize("scores", [[], [1, True], [1, 2.0], [1, -1], [1, 101], [1, "5"]],
                         ids=["empty", "bool", "float", "negative", "above-100", "string"])
def test_cut_refuses_values_outside_the_domain(scores) -> None:
    with pytest.raises(tool.Refusal) as refused:
        tool.score_histogram(scores)
    assert refused.value.code == tool.CUT_INVALID


def test_cut_reads_scores_only(bundle) -> None:
    categories = tuple(bundle.registry.magic10_order)

    def distribution(band):
        result = tool.Distribution(bundle)
        for score in (0, 10, 20, 30, 40, 50, 60, 70, 80, 90):
            result.add({"categories": [{"category_id": c, "score": score, "band": band} for c in categories]}, 0)
        return result

    population = {"corpus_sha256": "0" * 64, "people": 2, "pairs": 10, "synthetic": True}
    first, second = (tool.cut_report(bundle, population, distribution(band)) for band in ("Cool", "Glow"))
    assert first == second
    assert first["categories"][0]["score_histogram"][10] == 1


def test_cut_refuses_outside_closed_rails_or_the_repository_root(monkeypatch, capfdbinary, tmp_path) -> None:
    monkeypatch.setattr(tool, "load_corpus", lambda *a, **k: pytest.fail("corpus read before a precondition"))
    monkeypatch.setenv("SAFE_MODE", "0")
    code, out, err = _run(["cut"], capfdbinary)
    assert (code, out) == (tool.REFUSAL_EXIT_CODE, b"") and err.startswith(b"RAILS_CLOSED_REQUIRED:")
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.chdir(tmp_path)
    assert _run(["cut"], capfdbinary) == (tool.REFUSAL_EXIT_CODE, b"", f"{tool.WORKING_DIRECTORY_INVALID}\n".encode())


def test_cut_thresholds_object_builds_band_edges_v2(bundle, tmp_path) -> None:
    # A temporary root with the inputs build_band_edges reads; no governed path is written.
    for name in ("catalog/channels_v1.json", "catalog/gates_v1.json", "catalog/magic10.json",
                 "catalog/magic10_caps.json", "catalog/magic10_seeds.json", "catalog/manifest.json",
                 "catalog/magic10_mechanics_v1.json", "schemas/channels_v1.schema.json",
                 "schemas/gates_v1.schema.json", "schemas/magic10_mechanics_v1.schema.json",
                 "schemas/magic10_result_v1.schema.json", "schemas/magic10_compat_result_v1.schema.json",
                 "schemas/thresholds_v2.schema.json"):
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / name, tmp_path / name)
    categories = tuple(bundle.registry.magic10_order)
    distribution = SimpleNamespace(categories=categories, scores={
        category: [i % 101 for i in range(k, k + 400)] for k, category in enumerate(categories)})
    report = tool.cut_report(bundle, {}, distribution)
    thresholds = report["thresholds"]
    assert list(thresholds) == ["categories", "version"] and thresholds["version"] == "2"
    (tmp_path / "math").mkdir()
    (tmp_path / "math/thresholds.json").write_bytes(sercanon(thresholds, sort_keys=True))
    edges = config_artifacts.build_band_edges(tmp_path)
    assert edges["schema"] == "band_edges.v2"
    assert edges["categories"] == [{"category_id": r["category_id"], "maxima": r["maxima"]} for r in report["categories"]]


def test_cut_real_run_on_the_pinned_corpus(monkeypatch, capfdbinary, bundle, tmp_path) -> None:
    before = _git_status()
    captured = {}
    real_score_pairs = tool.score_pairs

    def spy(*args, **kwargs):
        captured["distribution"] = real_score_pairs(*args, **kwargs)
        return captured["distribution"]

    monkeypatch.setattr(tool, "score_pairs", spy)
    code, out, err = _run(["cut"], capfdbinary)
    assert (code, err) == (0, b"") and out.endswith(b"\n") and out.count(b"\n") == 1
    report = json.loads(out)
    assert out == sercanon(report, sort_keys=True)
    assert report["mode"] == "cut" and report["schema"] == tool.CUT_SCHEMA
    assert report["release"]["release_id"] == bundle.release_id
    assert report["population"] == {"corpus_sha256": tool.REFERENCE_CORPUS_SHA256, "people": 2000,
                                    "pairs": 20000, "synthetic": True}
    distribution = captured["distribution"]
    assert [row["category_id"] for row in report["categories"]] == list(bundle.registry.magic10_order)
    for row in report["categories"]:
        scores = distribution.scores[row["category_id"]]
        assert row["results"] == len(scores) == 20000
        assert row["score_histogram"] == [scores.count(s) for s in range(101)]
        assert row["maxima"] == _oracle(scores)
    assert _git_status() == before
    _assert_no_leak(out)
    tampered = tmp_path / "corpus.json"
    raw = bytearray((ROOT / "tools/score_distribution/reference_corpus_v1.json").read_bytes())
    raw[-2] = ord(" ")
    tampered.write_bytes(bytes(raw))
    monkeypatch.setattr(tool, "CORPUS_PATH", tampered)
    assert _run(["cut"], capfdbinary) == (tool.REFUSAL_EXIT_CODE, b"", f"{tool.CORPUS_INVALID}\n".encode())


# --- HDE-EPIC043 WU-PR-08 (HDE-FERM009; the FERM009 addendum): the observation population ----
# The population is a second governed input, independent of the corpus. The generator is
# rerun in memory or into tmp_path; the tracked file is never written. The one real run
# scores the pinned population under the active release and pins no band value.

GENERATOR_ALLOWED_IMPORTS = {"__future__", "argparse", "datetime", "hashlib", "math", "random", "sys", "uuid",
                             "pathlib", "typing", "ephem", "engine.runtime.determinism_env",
                             "engine.serializer.canon"}
OBSERVATION_POPULATION_KEYS = {"path", "population_sha256", "people", "pairs", "synthetic"}
PROVENANCE_KEYS = {"births", "chart_builder", "generator", "identities", "independence", "pairs", "record", "seed",
                   "synthetic"}


@pytest.fixture(scope="module")
def observation():
    return json.loads((ROOT / OBSERVATION_PATH).read_bytes())


def _tampered_observation(tmp_path) -> Path:
    tampered = tmp_path / "observation.json"
    raw = bytearray((ROOT / OBSERVATION_PATH).read_bytes())
    raw[-2] = ord(" ")
    tampered.write_bytes(bytes(raw))
    return tampered


def test_observation_population_regenerates_to_the_pinned_bytes(monkeypatch, capfdbinary, tmp_path) -> None:
    before = _git_status()
    raw = (ROOT / OBSERVATION_PATH).read_bytes()
    assert generator.population_bytes() == raw
    assert hashlib.sha256(raw).hexdigest() == tool.OBSERVATION_POPULATION_SHA256
    assert generator.main(["--check"]) == 0
    assert capfdbinary.readouterr() == (b"", b"")
    written = tmp_path / "observation_population_v1.json"
    monkeypatch.setattr(generator, "OUTPUT_PATH", written)
    assert generator.main(["--write"]) == 0
    out, err = capfdbinary.readouterr()
    assert (out, err) == (f"{generator.WRITTEN}:{tool.OBSERVATION_POPULATION_SHA256}\n".encode(), b"")
    assert written.read_bytes() == raw
    assert _git_status() == before


def test_generator_follows_the_reference_corpus_recipe(corpus) -> None:
    _births, people, pairs = generator.draw(generator.REFERENCE_SEED, "scorerange-synthetic")
    assert people == corpus["people"]
    assert pairs == corpus["pairs"]
    assert hashlib.sha256(sercanon({"people": people, "pairs": pairs})).hexdigest() == POPULATION_SHA256


def test_observation_population_is_independent_of_the_corpus(corpus, observation) -> None:
    assert generator.REFERENCE_SEED == corpus["provenance"]["seed"] == 20261101
    assert generator.SEED == observation["provenance"]["seed"] != generator.REFERENCE_SEED
    corpus_ids = {person["id"] for person in corpus["people"]}
    observation_ids = {person["id"] for person in observation["people"]}
    assert not corpus_ids & observation_ids
    assert not observation_ids <= corpus_ids
    # The corpus file carries no birth instants; the recipe yields them for both seeds.
    corpus_births = generator.birth_instants(generator.REFERENCE_SEED)
    observation_births = generator.birth_instants(generator.SEED)
    assert len(set(observation_births)) == len(observation["people"])
    assert not set(corpus_births) & set(observation_births)


def test_observation_population_shape_and_provenance(observation) -> None:
    raw = (ROOT / OBSERVATION_PATH).read_bytes()
    assert raw == sercanon(observation)
    assert set(observation) == {"schema", "synthetic", "people", "pairs", "provenance"}
    assert observation["schema"] == tool.OBSERVATION_SCHEMA == generator.SCHEMA
    assert observation["synthetic"] is True
    people, pairs = observation["people"], observation["pairs"]
    assert len(people) == 2000 >= 400
    assert [person["id"] for person in people] == [
        str(uuid.uuid5(uuid.NAMESPACE_URL, f"observation-synthetic-20261118-{i}")) for i in range(2000)]
    for person in people:
        assert set(person) == {"id", "gates"}
        gates = person["gates"]
        assert gates and gates == sorted(set(gates)) and all(type(g) is int and 1 <= g <= 64 for g in gates)
    assert len(pairs) == 20000
    assert all(len(pair) == 2 and pair[0] != pair[1] and all(type(i) is int and 0 <= i < 2000 for i in pair)
               for pair in pairs)
    assert len({(min(pair), max(pair)) for pair in pairs}) == 20000
    provenance = observation["provenance"]
    assert provenance == generator.PROVENANCE
    assert set(provenance) == PROVENANCE_KEYS
    assert provenance["seed"] == 20261118
    assert provenance["generator"] == GENERATOR_PATH
    assert provenance["record"] == {"git_blob": "cbef6c7b4f9c787c60e81efee2c1053075644e81",
                                    "path": "docs/ephemeral/HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md",
                                    "repository": "amthorn78/glow-docs"}
    builder = provenance["chart_builder"]
    assert builder["sha256"] == "5969513b1177b9b9086dc7abb2a38e0a7eca5f365d7ad3472bb6e25285d3b159"
    assert builder["ephemeris"] == "PyEphem 4.2.1" and builder["lunar_node"] == "mean"
    assert "observation-synthetic-20261118" in provenance["identities"]


def test_observation_mode_refuses_before_scoring(monkeypatch, capfdbinary, tmp_path) -> None:
    def refused(token):
        assert _run(["observation"], capfdbinary) == (tool.REFUSAL_EXIT_CODE, b"", f"{token}\n".encode())

    original = tool.load_observation_population
    monkeypatch.setattr(tool, "load_observation_population",
                        lambda *a, **k: pytest.fail("population read before the preconditions"))
    monkeypatch.setenv("SAFE_MODE", "0")
    code, out, err = _run(["observation"], capfdbinary)
    assert (code, out) == (tool.REFUSAL_EXIT_CODE, b"") and err.startswith(b"RAILS_CLOSED_REQUIRED:")
    assert b"'SAFE_MODE', '1'" in err and b"'0'" not in err
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.chdir(tmp_path)
    refused(tool.WORKING_DIRECTORY_INVALID)
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(tool, "load_observation_population", original)
    monkeypatch.setattr(tool, "OBSERVATION_POPULATION_PATH", _tampered_observation(tmp_path))
    monkeypatch.setattr(tool.json, "loads", lambda *a, **k: pytest.fail("unpinned bytes parsed"))
    monkeypatch.setattr(tool, "admit", lambda *a, **k: pytest.fail("release admitted for unpinned bytes"))
    monkeypatch.setattr(tool, "score_pairs", lambda *a, **k: pytest.fail("unpinned bytes scored"))
    refused(tool.OBSERVATION_POPULATION_INVALID)


def test_generator_refuses_value_free(monkeypatch, capfdbinary, tmp_path) -> None:
    output = tmp_path / "observation_population_v1.json"
    monkeypatch.setattr(generator, "OUTPUT_PATH", output)

    def refused(token):
        assert generator.main(["--write"]) == generator.REFUSAL_EXIT_CODE
        assert capfdbinary.readouterr() == (b"", f"{token}\n".encode())
        assert not output.exists()

    monkeypatch.setenv("ALLOW_NETWORK", "1")
    assert generator.main(["--write"]) == generator.REFUSAL_EXIT_CODE
    out, err = capfdbinary.readouterr()
    assert out == b"" and err.startswith(b"RAILS_CLOSED_REQUIRED:") and b"'ALLOW_NETWORK', '0'" in err
    assert b"'1'" not in err and not output.exists()
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.chdir(tmp_path)
    refused(generator.WORKING_DIRECTORY_INVALID)
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(generator.ephem, "__version__", "4.2.0")
    refused(generator.EPHEMERIS_UNSUPPORTED)
    monkeypatch.setattr(generator.ephem, "__version__", generator.EPHEM_VERSION)
    monkeypatch.setattr(generator, "OUTPUT_PATH", _tampered_observation(tmp_path))
    assert generator.main(["--check"]) == generator.STALE_EXIT_CODE
    assert capfdbinary.readouterr() == (b"", f"{generator.STALE}\n".encode())


def test_observation_mode_never_constructs_a_database_provider(monkeypatch, capfdbinary, observation) -> None:
    small = (tool.OBSERVATION_POPULATION_SHA256, observation["people"][:3], [[0, 1], [1, 2], [0, 2]])
    monkeypatch.setattr(tool, "load_observation_population", lambda *a, **k: small)
    monkeypatch.setattr(tool.DBAccess, "for_current_env",
                        classmethod(lambda cls, *a, **k: pytest.fail("observation mode constructed DBAccess")))
    code, out, err = _run(["observation"], capfdbinary)
    assert (code, err) == (0, b"")
    report = json.loads(out)
    assert report["mode"] == "observation" and report["population"]["pairs"] == 3
    assert report["comparison"]["against"] == "target" and report["limit"] == tool.OBSERVATION_LIMIT


def test_observation_real_run_on_the_pinned_population(monkeypatch, capfdbinary, bundle, observation) -> None:
    before = _git_status()
    monkeypatch.setattr(tool.DBAccess, "for_current_env",
                        classmethod(lambda cls, *a, **k: pytest.fail("observation mode constructed DBAccess")))
    code, out, err = _run(["observation"], capfdbinary)
    assert (code, err) == (0, b"") and out.endswith(b"\n") and out.count(b"\n") == 1
    report = json.loads(out)
    assert out == sercanon(report, sort_keys=True)
    assert set(report) == REPORT_KEYS | {"limit"}
    assert report["schema"] == tool.REPORT_SCHEMA and report["mode"] == "observation" and report["read_only"] is True
    assert set(report["population"]) == OBSERVATION_POPULATION_KEYS
    assert report["population"] == {"path": OBSERVATION_PATH, "population_sha256": tool.OBSERVATION_POPULATION_SHA256,
                                    "people": 2000, "pairs": 20000, "synthetic": True}
    assert report["release"] == {"release_id": bundle.release_id, "version": bundle.manifest.version,
                                 "config_id": bundle.mechanics["config_id"]}
    assert report["category_results"] == 200000
    variety = report["band_variety_per_pair"]
    assert set(variety) == {"1", "2", "3", "4"} and sum(variety.values()) == 20000
    comparison = report["comparison"]
    categories = list(bundle.registry.magic10_order)
    assert comparison["against"] == "target" and comparison["tolerance_points"] == tool.TOLERANCE_POINTS == 5
    assert comparison["target_mix_percent"] == tool.TARGET_MIX_PERCENT
    assert sorted(comparison["per_category"]) == sorted(categories)
    for rows in comparison["per_category"].values():
        assert set(rows) == set(tool.BANDS) and all(type(row["beyond_tolerance"]) is bool for row in rows.values())
    assert set(comparison["categories_beyond_tolerance"]) <= set(categories)
    assert report["limit"] == tool.OBSERVATION_LIMIT
    _assert_no_leak(out, err)
    text = out.decode("utf-8")
    assert '"gates"' not in text and "observation-synthetic" not in text
    assert not [person["id"] for person in observation["people"] if person["id"] in text]
    assert _git_status() == before


def test_the_generator_is_offline_and_outside_the_product() -> None:
    tree = ast.parse((ROOT / GENERATOR_PATH).read_text(encoding="utf-8"))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module)
    assert imported <= GENERATOR_ALLOWED_IMPORTS, sorted(imported - GENERATOR_ALLOWED_IMPORTS)
    forbidden_roots = ("flask", "werkzeug", "adapter", "engine.cli", "engine.http", "engine.db", "presenter",
                       "psycopg", "requests", "urllib", "http", "socket", "ssl", "subprocess", "tests",
                       "tools.score_distribution")
    assert not [name for name in imported if name.split(".")[0] in forbidden_roots or name.startswith(forbidden_roots)]
    tracked = subprocess.run(["git", "ls-files", "-z", "--", "adapter/*.py", "engine/*.py", "presenter/*.py"],
                             cwd=ROOT, capture_output=True, check=True).stdout.decode("utf-8").split("\0")
    assert not [path for path in tracked
                if path and "generate_observation_population" in (ROOT / path).read_text(encoding="utf-8",
                                                                                         errors="replace")]
