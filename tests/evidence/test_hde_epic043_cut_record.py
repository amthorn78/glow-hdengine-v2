"""Owner test of the HDE-EPIC043 WU-PR-10 Magic-10 v2 cut record writer (HDE-DIST008.2).

A full scoring pass over the pinned corpus takes about 1 min 42 s, so the
writer runs here over a small corpus: the pinned corpus's people with its first
``SMALL_PAIRS`` pairs, supplied through ``score_distribution.load_corpus``.  Its
head is a labelled synthetic head in temporary storage: the repository's release
members with ``math/thresholds.json`` cut from that small corpus,
``catalog/magic10_mechanics_v2.json`` rebound to those bytes and a manifest cut
by ``scripts/cut_release_manifest.py``.  It is admitted through the unchanged
admission path; nothing here is the v2 release, and nothing is written under the
repository tree.  The real pass 1, pass 2 and target-mix runs execute once per
module; each negative control changes one input and asserts its named refusal.
"""
from __future__ import annotations

import copy
import dataclasses
import hashlib
import json
import shutil
import subprocess
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

import pytest

from ci.checks import classify_ci_changes as classifier
from engine.config import registry_loader
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root, load_active_mechanics_bundle
from engine.serializer.canon import sercanon
from scripts.cut_release_manifest import cut_manifest
from tools.evidence import generate_hde_epic043_cut_record as g
from tools.evidence import update_evidence_index as updater
from tools.score_distribution import score_distribution as tool

ROOT = Path(__file__).resolve().parents[2]
THIS_TEST = "tests/evidence/test_hde_epic043_cut_record.py"
WRITER = "tools/evidence/generate_hde_epic043_cut_record.py"
CLOSED_RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
SMALL_PAIRS = 120
CHECK_KEYS = (
    "release_id_equals_manifest_digest", "release_id_differs_from_prior", "q02_version_equal",
    "q02_built_at_utc_equal", "reports_bind_the_head_release", "corpus_digest_pinned",
    "thresholds_equal_committed", "categories_within_tolerance", "pass1_root_provisional", "pass1_equals_pass2",
)


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _parse(record: bytes) -> dict[str, str]:
    text = record.decode("utf-8")
    assert "\r" not in text and text.endswith("\n") and not text.endswith("\n\n")
    pairs = [line.split(": ", 1) for line in text.split("\n")[:-1]]
    assert all(len(pair) == 2 for pair in pairs)
    keys = [key for key, _value in pairs]
    assert len(keys) == len(set(keys))
    return dict(pairs)


def _keys(record: bytes) -> list[str]:
    return [line.split(": ", 1)[0] for line in record.decode("utf-8").split("\n")[:-1]]


def _expected_keys(categories: list[str]) -> list[str]:
    keys = [
        "schema", "epic_id", "task_id", "subtask_id", "work_unit_id", "cut_basis",
        "release.release_id", "release.manifest_path", "release.manifest_sha256", "release.version",
        "release.built_at_utc", "release.config_id", "release.member_count", "release.prior_commit",
        "release.prior_release_id", "q02.version", "q02.built_at_utc", "q02.admitted_release_version",
        "q02.admitted_release_built_at_utc", "corpus.path", "corpus.sha256", "corpus.pinned_sha256",
        "corpus.people", "corpus.pairs", "thresholds.path", "thresholds.sha256", "thresholds.size_bytes",
        "configuration.path", "configuration.sha256", "cut.schema", "cut.target_mix_percent",
        "cut.cut_target_percent", "cut.category_order",
    ]
    for category in categories:
        keys += [f"cut.{category}.results", f"cut.{category}.score_histogram"]
        keys += [f"cut.{category}.cut.{index}.{field}" for index in (1, 2, 3)
                 for field in ("target_percent", "maximum", "cumulative_count", "deviation")]
        keys.append(f"cut.{category}.maxima")
    keys += ["cut.score_histograms_sha256", "cut.thresholds_sha256", "mix.schema", "mix.against",
             "mix.target_mix_percent", "mix.tolerance_points"]
    keys += [f"mix.overall.{band}.{field}" for band in tool.BANDS for field in ("share_points", "difference_points")]
    keys += [f"mix.{category}.{band}.{field}" for category in categories for band in tool.BANDS
             for field in ("share_points", "difference_points", "beyond_tolerance")]
    keys += ["mix.categories_beyond_tolerance", "pass1.root", "pass1.thresholds_source",
             "pass1.thresholds_source_sha256", "pass1.configuration_source", "pass1.configuration_source_sha256",
             "pass1.release_id", "pass1.corpus_sha256", "pass1.score_histograms_sha256", "pass1.thresholds_sha256"]
    keys += [f"check.{key}" for key in CHECK_KEYS]
    keys.append("status")
    return keys


def _prior_release_id() -> str:
    """An independent read of the prior release commit's manifest blob."""

    blob = subprocess.run(["git", "cat-file", "blob", f"{g.PRIOR_COMMIT}:catalog/manifest.json"], cwd=ROOT,
                          capture_output=True, check=True).stdout
    return _sha(blob)


def _build_synthetic_head(base: Path, thresholds: dict) -> Path:
    """The release members with the small corpus's cut as governed bytes (labelled, temporary)."""

    head = base / "synthetic-cut-head-only"
    for rel in (*registry_loader.ADMITTED_RELEASE_ROSTER, g.MANIFEST_REL, *g.PASS1_FIXTURES.values()):
        (head / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, head / rel)
    thresholds_bytes = sercanon(thresholds, sort_keys=True)
    (head / g.THRESHOLDS_REL).write_bytes(thresholds_bytes)
    configuration = json.loads((ROOT / g.CONFIGURATION_REL).read_bytes())
    configuration["sources"]["thresholds"]["sha256"] = _sha(thresholds_bytes)
    (head / g.CONFIGURATION_REL).write_bytes(sercanon(configuration, sort_keys=True))
    assert cut_manifest(head / g.MANIFEST_REL, version=registry_loader.ADMITTED_RELEASE_VERSION,
                        built_at_utc=registry_loader.ADMITTED_RELEASE_BUILT_AT_UTC,
                        roster=registry_loader.ADMITTED_RELEASE_ROSTER) == 0
    return head


def _apply(patcher, state) -> None:
    for name, value in CLOSED_RAILS.items():
        patcher.setenv(name, value)
    patcher.chdir(ROOT)
    patcher.setattr(tool, "load_corpus", lambda *a, **k: state.small)
    patcher.setattr(tool, "load_active_mechanics_bundle",
                    lambda: _load_active_mechanics_bundle_from_root(state.head))
    patcher.setattr(g, "ROOT", state.head)


@pytest.fixture(scope="module")
def state(tmp_path_factory):
    with pytest.MonkeyPatch.context() as patcher:
        for name, value in CLOSED_RAILS.items():
            patcher.setenv(name, value)
        patcher.chdir(ROOT)
        bundle = load_active_mechanics_bundle()
        digest, people, pairs = tool.load_corpus()
        small = (digest, people, pairs[:SMALL_PAIRS])
        parties = [tool.reference_party(person) for person in people]
        distribution = tool.score_pairs(bundle, parties, small[2])
        population = {"corpus_sha256": digest, "people": len(people), "pairs": SMALL_PAIRS, "synthetic": True}
        thresholds = tool.cut_report(bundle, population, distribution)["thresholds"]
        head = _build_synthetic_head(tmp_path_factory.mktemp("cut-record"), thresholds)
        result = SimpleNamespace(head=head, small=small, scores=distribution.scores, thresholds=thresholds,
                                 categories=list(bundle.registry.magic10_order))
        _apply(patcher, result)
        result.facts = g.collect()
    return result


@pytest.fixture
def ctx(state, monkeypatch):
    _apply(monkeypatch, state)
    state.fresh = lambda: copy.deepcopy(state.facts)
    return state


def _use_facts(monkeypatch, facts) -> None:
    monkeypatch.setattr(g, "collect", lambda: facts)


def _refused(argv, code) -> None:
    with pytest.raises(SystemExit) as excinfo:
        g.main(argv)
    assert excinfo.value.code == code


# --- the positive record on the synthetic head ------------------------------------------------

def test_every_check_passes_and_the_layout_is_closed(ctx):
    assert g.failed_checks(ctx.fresh()) == []
    record = g.render(g.record_lines(ctx.fresh()))
    assert _keys(record) == _expected_keys(ctx.categories)
    fields = _parse(record)
    assert fields["schema"] == "hde_epic043_v2_cut_record.v1"
    assert all(fields[f"check.{key}"] == "true" for key in CHECK_KEYS)
    assert fields["status"] == "PASS"
    # No clock, git-state, host or actor field: a second run is byte stable.
    assert not [key for key in fields if any(word in key for word in (
        "run.", "time", "date", "tested_commit", "head_commit", "host", "actor", "python"))]
    assert str(ctx.head) not in record.decode("utf-8") and "/tmp" not in record.decode("utf-8")


def test_release_identity_and_q02_values_are_read_at_the_head(ctx):
    fields = _parse(g.render(g.record_lines(ctx.fresh())))
    manifest_bytes = (ctx.head / "catalog/manifest.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    bundle = _load_active_mechanics_bundle_from_root(ctx.head)
    assert fields["release.release_id"] == bundle.release_id == _sha(manifest_bytes) == fields["release.manifest_sha256"]
    assert fields["release.prior_release_id"] == _prior_release_id() != fields["release.release_id"]
    assert fields["release.member_count"] == str(len(registry_loader.ADMITTED_RELEASE_ROSTER))
    assert fields["release.config_id"] == bundle.mechanics["config_id"]
    assert fields["q02.version"] == g.Q02_VERSION == manifest["version"] == registry_loader.ADMITTED_RELEASE_VERSION
    assert (fields["q02.built_at_utc"] == g.Q02_BUILT_AT_UTC == manifest["built_at_utc"]
            == registry_loader.ADMITTED_RELEASE_BUILT_AT_UTC)
    assert fields["release.version"] == fields["q02.admitted_release_version"] == g.Q02_VERSION
    assert fields["release.built_at_utc"] == fields["q02.admitted_release_built_at_utc"] == g.Q02_BUILT_AT_UTC


def test_cut_values_are_the_tools_cut_of_the_corpus(ctx):
    fields = _parse(g.render(g.record_lines(ctx.fresh())))
    assert fields["corpus.sha256"] == fields["corpus.pinned_sha256"] == tool.REFERENCE_CORPUS_SHA256
    assert fields["corpus.pairs"] == str(SMALL_PAIRS)
    assert fields["corpus.people"] == str(len(ctx.small[1]))
    assert fields["cut.cut_target_percent"] == json.dumps(list(tool.cut_targets()), separators=(",", ":"))
    assert fields["cut.category_order"] == json.dumps(ctx.categories, separators=(",", ":"))
    maxima = {row["category_id"]: row["maxima"] for row in ctx.thresholds["categories"]}
    for category in ctx.categories:
        histogram = [0] * 101
        for score, count in Counter(ctx.scores[category]).items():
            histogram[score] += count
        assert fields[f"cut.{category}.score_histogram"] == json.dumps(histogram, separators=(",", ":"))
        assert fields[f"cut.{category}.results"] == str(SMALL_PAIRS)
        assert fields[f"cut.{category}.maxima"] == json.dumps(maxima[category], separators=(",", ":"))
        cumulative = [sum(histogram[:score + 1]) for score in range(101)]
        for index, target in enumerate(tool.cut_targets(), start=1):
            maximum = int(fields[f"cut.{category}.cut.{index}.maximum"])
            assert maximum == maxima[category][index - 1]
            assert fields[f"cut.{category}.cut.{index}.target_percent"] == str(target)
            assert fields[f"cut.{category}.cut.{index}.cumulative_count"] == str(cumulative[maximum])
            assert fields[f"cut.{category}.cut.{index}.deviation"] == str(
                abs(100 * cumulative[maximum] - target * SMALL_PAIRS))
    thresholds_bytes = (ctx.head / "math/thresholds.json").read_bytes()
    assert fields["thresholds.sha256"] == fields["cut.thresholds_sha256"] == _sha(thresholds_bytes)
    assert fields["thresholds.size_bytes"] == str(len(thresholds_bytes))
    assert fields["configuration.sha256"] == _sha((ctx.head / "catalog/magic10_mechanics_v2.json").read_bytes())


def test_realized_mix_is_read_from_the_head_bands_against_the_target(ctx):
    fields = _parse(g.render(g.record_lines(ctx.fresh())))
    assert fields["mix.against"] == "target"
    assert fields["mix.tolerance_points"] == str(tool.TOLERANCE_POINTS)
    assert json.loads(fields["mix.target_mix_percent"]) == tool.TARGET_MIX_PERCENT
    assert fields["mix.categories_beyond_tolerance"] == "[]"
    maxima = {row["category_id"]: row["maxima"] for row in ctx.thresholds["categories"]}
    for category in ctx.categories:
        counts = Counter(next(band for band, top in zip(tool.BANDS, maxima[category]) if score <= top)
                         for score in ctx.scores[category])
        for band in tool.BANDS:
            target = tool.TARGET_MIX_PERCENT[band]
            assert fields[f"mix.{category}.{band}.share_points"] == tool.points(counts[band], SMALL_PAIRS)
            assert fields[f"mix.{category}.{band}.difference_points"] == tool.points(counts[band], SMALL_PAIRS, target)
            assert fields[f"mix.{category}.{band}.beyond_tolerance"] == "false"


def test_pass1_ran_in_a_provisional_root_holding_the_fixtures(ctx):
    facts = ctx.fresh()
    fields = _parse(g.render(g.record_lines(facts)))
    for rel, source in g.PASS1_FIXTURES.items():
        raw = (ROOT / source).read_bytes()
        assert facts["pass1"]["identities"][rel] == [_sha(raw), len(raw)]
        assert facts["pass1"]["identities"][rel] != facts["head"]["identities"][rel]
    assert fields["pass1.thresholds_source"] == "tests/fixtures/magic10_v2/thresholds_v2.fixture.json"
    assert fields["pass1.thresholds_source_sha256"] == _sha((ROOT / fields["pass1.thresholds_source"]).read_bytes())
    assert fields["pass1.configuration_source"] == "tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json"
    assert fields["pass1.release_id"] != fields["release.release_id"]
    assert fields["pass1.corpus_sha256"] == tool.REFERENCE_CORPUS_SHA256
    assert fields["pass1.score_histograms_sha256"] == fields["cut.score_histograms_sha256"]
    assert fields["pass1.thresholds_sha256"] == fields["cut.thresholds_sha256"]


# --- write, byte stability and --check --------------------------------------------------------

def test_write_is_byte_stable_and_check_passes_writing_nothing(ctx, capsys):
    out = ctx.head / g.OUT_REL
    assert not out.exists()
    try:
        assert g.main([]) == 0
        first = out.read_bytes()
        assert g.main(["--check"]) == 0
        assert out.read_bytes() == first
        assert g.main([]) == 0
        assert out.read_bytes() == first
        assert capsys.readouterr().out == "v2 cut record written\nv2 cut record check ok\nv2 cut record written\n"
        assert first == g.render(g.record_lines(ctx.fresh()))
        assert sorted(path.name for path in out.parent.iterdir()) == ["v2_cut_record.txt"]
    finally:
        shutil.rmtree(ctx.head / "audit")


def test_check_names_the_drifted_key_and_writes_nothing(ctx, monkeypatch):
    _use_facts(monkeypatch, ctx.fresh())
    out = ctx.head / g.OUT_REL
    try:
        _refused(["--check"], f"DRIFT:{g.OUT_REL}:missing")
        assert not out.exists()
        record = g.render(g.record_lines(ctx.fresh()))
        marker = b"\ncut.harmony.maxima: "
        start = record.index(marker) + len(marker)
        drifted = record[:start] + b"[1," + record[start + 1:]
        out.parent.mkdir(parents=True)
        out.write_bytes(drifted)
        _refused(["--check"], f"DRIFT:{g.OUT_REL}:cut.harmony.maxima")
        out.write_bytes(record.replace(b"\n", b"\r\n"))
        _refused(["--check"], f"DRIFT:{g.OUT_REL}:schema")
        out.write_bytes(record + b"\n")
        _refused(["--check"], f"DRIFT:{g.OUT_REL}:layout")
        assert out.read_bytes() == record + b"\n"
        out.write_bytes(record)
        assert g.main(["--check"]) == 0
    finally:
        shutil.rmtree(ctx.head / "audit")


def test_render_refuses_a_line_break_or_a_duplicate_key():
    with pytest.raises(g.CutRecordRefusal) as excinfo:
        g.render([("schema", g.SCHEMA), ("a", "b\nc"), ("status", "PASS")])
    assert excinfo.value.code == g.RECORD_INVALID
    with pytest.raises(g.CutRecordRefusal) as excinfo:
        g.render([("schema", g.SCHEMA), ("a", "b"), ("a", "b"), ("status", "PASS")])
    assert excinfo.value.code == g.RECORD_INVALID
    assert g.render([("schema", g.SCHEMA), ("status", "PASS")]) == b"schema: hde_epic043_v2_cut_record.v1\nstatus: PASS\n"


# --- one negative control per check -----------------------------------------------------------

def _release_id_not_the_manifest_digest(ctx, monkeypatch):
    def admitted():
        return dataclasses.replace(_load_active_mechanics_bundle_from_root(ctx.head), release_id="f" * 64)

    monkeypatch.setattr(tool, "load_active_mechanics_bundle", admitted)
    facts = ctx.fresh()
    facts["head"] = g.head_release()
    # Scoring refuses a bundle whose release_id is not its own (ERR_M10_CONFIG_MISMATCH), so
    # the reports carry the admitted release_id as that admission would have named it.
    for report in ("cut", "mix"):
        facts[report]["release"]["release_id"] = facts["head"]["release_id"]
    return facts


def _prior_release_equal(ctx, monkeypatch):
    monkeypatch.setattr(g, "read_prior_manifest", lambda: (ctx.head / "catalog/manifest.json").read_bytes())
    facts = ctx.fresh()
    facts["prior"] = g.prior_release()
    return facts


def _q02_version_differs(ctx, monkeypatch):
    monkeypatch.setattr(g, "Q02_VERSION", "2.0.1")
    return ctx.fresh()


def _q02_built_at_differs(ctx, monkeypatch):
    monkeypatch.setattr(g, "Q02_BUILT_AT_UTC", "2026-11-19T05:48:29Z")
    return ctx.fresh()


def _mix_report_of_another_release(ctx, monkeypatch):
    facts = ctx.fresh()
    facts["mix"]["release"]["release_id"] = facts["prior"]["release_id"]
    return facts


def _corpus_not_pinned(ctx, monkeypatch):
    monkeypatch.setattr(tool, "load_corpus", lambda *a, **k: ("0" * 64, *ctx.small[1:]))
    facts = ctx.fresh()
    facts.update(cut=g.pass2_cut(), mix=g.target_mix(), pass1=g.pass1_cut())
    return facts


def _thresholds_not_the_cut(ctx, monkeypatch):
    facts = ctx.fresh()
    raw = (ROOT / "math/thresholds.json").read_bytes()
    facts["thresholds"] = {"sha256": _sha(raw), "size": len(raw), "bytes": raw}
    return facts


def _mix_beyond_tolerance(ctx, monkeypatch):
    monkeypatch.setattr(tool, "TOLERANCE_POINTS", 0)
    facts = ctx.fresh()
    facts["mix"] = g.target_mix()
    return facts


def _pass1_not_provisional(ctx, monkeypatch):
    # Pass 1 over the head's own bytes instead of the labelled fixtures.
    monkeypatch.setattr(g, "PASS1_FIXTURES", {rel: rel for rel in g.PASS1_FIXTURES})
    facts = ctx.fresh()
    facts["pass1"] = g.pass1_cut()
    return facts


def _pass1_histogram_differs(ctx, monkeypatch):
    facts = ctx.fresh()
    histogram = facts["pass1"]["report"]["categories"][0]["score_histogram"]
    score = max(index for index, count in enumerate(histogram) if count)
    assert score < tool.MAX_SCORE
    histogram[score] -= 1
    histogram[score + 1] += 1
    return facts


def _pass1_maxima_differ(ctx, monkeypatch):
    facts = ctx.fresh()
    report = facts["pass1"]["report"]
    report["categories"][-1]["maxima"][0] -= 1
    report["thresholds"]["categories"][-1]["maxima"][0] -= 1
    return facts


NEGATIVE_CONTROLS = (
    ("release_id_equals_manifest_digest", g.RELEASE_ID_MISMATCH, _release_id_not_the_manifest_digest),
    ("release_id_differs_from_prior", g.RELEASE_ID_UNCHANGED, _prior_release_equal),
    ("q02_version_equal", g.Q02_VERSION_MISMATCH, _q02_version_differs),
    ("q02_built_at_utc_equal", g.Q02_BUILT_AT_MISMATCH, _q02_built_at_differs),
    ("reports_bind_the_head_release", g.REPORTS_INCONSISTENT, _mix_report_of_another_release),
    ("corpus_digest_pinned", g.CORPUS_DIGEST_MISMATCH, _corpus_not_pinned),
    ("thresholds_equal_committed", g.THRESHOLDS_MISMATCH, _thresholds_not_the_cut),
    ("categories_within_tolerance", g.MIX_BEYOND_TOLERANCE, _mix_beyond_tolerance),
    ("pass1_root_provisional", g.PASS1_ROOT_INVALID, _pass1_not_provisional),
    ("pass1_equals_pass2", g.PASS1_MISMATCH, _pass1_histogram_differs),
    ("pass1_equals_pass2", g.PASS1_MISMATCH, _pass1_maxima_differ),
)


def test_every_check_has_a_negative_control():
    assert {key for key, _code, _mutate in NEGATIVE_CONTROLS} == set(CHECK_KEYS)
    assert [key for key, _code, _passed in g.check_results(_placeholder_facts())] == list(CHECK_KEYS)


def _placeholder_facts():
    report = {"release": {}, "population": {}, "categories": [], "thresholds": {},
              "comparison": {"per_category": {}, "categories_beyond_tolerance": []}}
    return {"head": {"identities": {}, "release_id": "", "manifest_sha256": "", "version": "", "built_at_utc": "",
                     "admitted_version": "", "admitted_built_at_utc": "", "config_id": ""},
            "prior": {"release_id": ""}, "thresholds": {"bytes": b""},
            "cut": report, "mix": copy.deepcopy(report),
            "pass1": {"report": copy.deepcopy(report), "identities": {}, "fixtures": {}, "release_id": ""}}


@pytest.mark.parametrize(("key", "code", "mutate"), NEGATIVE_CONTROLS,
                         ids=[mutate.__name__.strip("_") for _key, _code, mutate in NEGATIVE_CONTROLS])
def test_a_failing_check_is_its_named_refusal_and_writes_nothing(ctx, monkeypatch, key, code, mutate):
    facts = mutate(ctx, monkeypatch)
    assert g.failed_checks(facts) == [code]
    fields = _parse(g.render(g.record_lines(facts)))
    assert fields[f"check.{key}"] == "false"
    assert fields["status"] == "FAIL"
    _use_facts(monkeypatch, facts)
    for argv in ([], ["--check"]):
        _refused(argv, code)
    assert not (ctx.head / "audit").exists()


# --- refusals before any record is rendered ---------------------------------------------------

def _no_scoring(monkeypatch):
    for name in ("pass2_cut", "target_mix", "pass1_cut"):
        monkeypatch.setattr(g, name, lambda name=name: pytest.fail(f"{name} ran after a refusal"))


def test_open_rails_refuse_before_any_input_is_read(ctx, monkeypatch):
    _no_scoring(monkeypatch)
    monkeypatch.setattr(g, "head_release", lambda: pytest.fail("admitted with open rails"))
    monkeypatch.setenv("SAFE_MODE", "0")
    _refused([], g.RAILS_NOT_CLOSED)
    monkeypatch.delenv("TZ")
    _refused(["--check"], g.RAILS_NOT_CLOSED)
    assert not (ctx.head / "audit").exists()


def test_a_working_directory_other_than_the_repository_root_refuses(ctx, monkeypatch, tmp_path):
    _no_scoring(monkeypatch)
    monkeypatch.chdir(tmp_path)
    _refused([], f"{g.TOOL_REFUSED}:{tool.WORKING_DIRECTORY_INVALID}")
    assert list(tmp_path.iterdir()) == []


def test_a_head_that_does_not_admit_refuses_with_the_admission_code(ctx, monkeypatch):
    _no_scoring(monkeypatch)
    monkeypatch.setattr(registry_loader, "ADMITTED_RELEASE_VERSION", "2.0.1")
    _refused([], f"{g.TOOL_REFUSED}:{tool.RELEASE_NOT_ADMITTED}:RELEASE_VERSION_MISMATCH")
    assert not (ctx.head / "audit").exists()


def test_an_unavailable_prior_release_refuses(ctx, monkeypatch):
    _no_scoring(monkeypatch)
    monkeypatch.setattr(g, "PRIOR_COMMIT", "0" * 40)
    _refused([], g.PRIOR_RELEASE_UNAVAILABLE)
    assert not (ctx.head / "audit").exists()


def test_an_unreadable_input_refuses(ctx, monkeypatch):
    _no_scoring(monkeypatch)
    monkeypatch.setattr(g, "CONFIGURATION_REL", "catalog/absent_configuration.json")
    _refused([], f"{g.INPUT_UNREADABLE}:catalog/absent_configuration.json")
    assert not (ctx.head / "audit").exists()


def test_a_provisional_root_that_does_not_admit_refuses(ctx, monkeypatch):
    facts = ctx.fresh()
    monkeypatch.setattr(g, "pass2_cut", lambda: facts["cut"])
    monkeypatch.setattr(g, "target_mix", lambda: facts["mix"])
    # The fixture thresholds alone: the head's configuration does not bind them.
    monkeypatch.setattr(g, "PASS1_FIXTURES", {g.THRESHOLDS_REL: "tests/fixtures/magic10_v2/thresholds_v2.fixture.json"})
    with pytest.raises(SystemExit) as excinfo:
        g.main([])
    assert str(excinfo.value.code).startswith(f"{g.PASS1_ROOT_REFUSED}:")
    assert not (ctx.head / "audit").exists()


def test_a_tool_refusal_is_named_and_writes_nothing(ctx, monkeypatch):
    def refuse(*_args, **_kwargs):
        raise tool.Refusal(tool.CORPUS_INVALID)

    monkeypatch.setattr(tool, "load_corpus", refuse)
    _refused([], f"{g.TOOL_REFUSED}:{tool.CORPUS_INVALID}")
    assert not (ctx.head / "audit").exists()


# --- reuse of the governed tool, never a second formula ---------------------------------------

def test_the_writer_reuses_the_score_distribution_tool():
    source = (ROOT / WRITER).read_text(encoding="utf-8")
    for call in ("tool.run_cut", 'tool.run_reference("target")', "tool.cut_report", "tool.score_pairs",
                 "tool.load_corpus", "tool.admit", "cut_manifest("):
        assert call in source, call
    for formula in ("def cut_maxima", "def score_histogram", "def compare_target", "def beyond_tolerance",
                    "def cut_targets", "def points"):
        assert formula not in source, formula


# --- registration ------------------------------------------------------------------------------

def test_the_record_is_registered_in_the_index_without_a_release_label():
    assert updater.EPIC043_PR10_PRIMARY_ARTIFACTS == [{
        "artifact_key": "epic043.pr10.v2_cut_record",
        "discovered_physical_path": g.OUT_REL,
        "epic_id": "HDE-EPIC043",
        "record_type": "epic043_pr10_evidence",
        "schema_version": "1.0",
        "notes": "HDE-EPIC043 WU-PR-10 Magic-10 v2 cut record (HDE-DIST008.2)",
    }]
    assert g.OUT_REL not in updater.CURRENT_RELEASE_CAPTURE_PATHS
    source = (ROOT / "tools/evidence/update_evidence_index.py").read_text(encoding="utf-8")
    loader = source[source.index("def _load_human_index"):source.index("def _render_human_index")]
    assert "*EPIC043_PR10_PRIMARY_ARTIFACTS," in loader
    assert f"`{g.OUT_REL}`" in (ROOT / "docs/EVIDENCE_INDEX.md").read_text(encoding="utf-8")


def test_the_classifier_owns_the_writer_test_and_record():
    assert classifier._EVIDENCE_GENERATOR_TEST_OWNERS[WRITER] == (THIS_TEST,)
    assert classifier._evidence_generator_owner_targets(ROOT, WRITER) == (THIS_TEST,)
    assert THIS_TEST in classifier.changed_test_targets(ROOT, (WRITER,))
    for path in (WRITER, THIS_TEST, g.OUT_REL, f"{g.OUT_REL}.path_proof.txt"):
        assert classifier._lanes_for_path(path) == {"evidence"}, path


# --- the committed record at the repository head ------------------------------------------------

def test_the_committed_record_binds_the_repository_head(monkeypatch):
    """A fast currency check of the stored record; ``--check`` recomputes it in full."""

    for name, value in CLOSED_RAILS.items():
        monkeypatch.setenv(name, value)
    path = ROOT / g.OUT_REL
    assert path.is_file(), "the cut record is written by the writer and committed with the cut"
    record = path.read_bytes()
    fields = _parse(record)
    bundle = load_active_mechanics_bundle()
    categories = list(bundle.registry.magic10_order)
    assert _keys(record) == _expected_keys(categories)
    manifest_bytes = (ROOT / "catalog/manifest.json").read_bytes()
    assert fields["release.release_id"] == bundle.release_id == _sha(manifest_bytes)
    assert fields["release.prior_release_id"] == _prior_release_id()
    assert fields["q02.version"] == registry_loader.ADMITTED_RELEASE_VERSION == g.Q02_VERSION
    assert fields["q02.built_at_utc"] == registry_loader.ADMITTED_RELEASE_BUILT_AT_UTC == g.Q02_BUILT_AT_UTC
    thresholds_bytes = (ROOT / "math/thresholds.json").read_bytes()
    assert fields["thresholds.sha256"] == fields["cut.thresholds_sha256"] == _sha(thresholds_bytes)
    for row in json.loads(thresholds_bytes)["categories"]:
        assert fields[f"cut.{row['category_id']}.maxima"] == json.dumps(row["maxima"], separators=(",", ":"))
    assert fields["corpus.sha256"] == tool.REFERENCE_CORPUS_SHA256
    assert fields["mix.categories_beyond_tolerance"] == "[]"
    assert all(fields[f"check.{key}"] == "true" for key in CHECK_KEYS)
    assert fields["status"] == "PASS"
