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
import subprocess
import sys
import tomllib
import uuid
from collections import Counter
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
from tools.score_distribution import score_distribution as tool

ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = "tools/score_distribution/score_distribution.py"
TOOL_FILES = (
    "tools/score_distribution/reference_baseline_v1.json",
    "tools/score_distribution/reference_corpus_v1.json",
    TOOL_PATH,
)
THIS_TEST = "tests/tools/test_score_distribution.py"
# The S16 measure (Specification v1.1): the score-range record's counts at release 1.3.0.
RECORD_COUNTS = {"Cool": 157045, "Open": 42093, "Warm": 859, "Glow": 3}
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
    assert baseline["release"] == {"version": "1.3.0", "config_id": "m10-channel-state-v1.0.0",
                                   "release_id": "77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e"}
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
               "engine.db.errors", "engine.magic10.composite", "engine.runtime.determinism_env",
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
    assert referencing == ["ci/checks/classify_ci_changes.py"]
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
