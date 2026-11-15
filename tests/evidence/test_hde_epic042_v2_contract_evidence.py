"""Owner test of the HDE-EPIC042 WU-PR-04 Separation v2 contract evidence generator.

HDE-SEPA007.5. The generator runs on the repository as it is: the governed v2
catalogs and schemas, the labelled non-canon fixtures, the WU-PR-03 loader's
public admission function and the real v1 compat path.  One build is shared by
the module; the record-dependent cases read the committed record.  Expected
counts and outcomes are transcribed from the detailed plan (WU-PR-04 plan v1.0
§6.1.3 and §6.1.5) and from canon, not read back from the generator.  Nothing is
written under the repository tree; write-mode cases write to ``tmp_path``.
"""
from __future__ import annotations

import collections
import copy
import json
import subprocess
import tempfile
from pathlib import Path
from types import SimpleNamespace

import pytest

import engine.config.registry_loader as registry_loader
from engine.cli import main as cli_main
from engine.compat.compute import evaluate_pair, evaluation_party
from engine.config.registry_loader import ADMITTED_RELEASE_ROSTER, load_active_mechanics_bundle
from engine.serializer import canon
from tools.evidence import generate_hde_epic042_v2_contract_evidence as g

ROOT = Path(__file__).resolve().parents[2]
CLOSED_RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "test"}
RUN = {
    "run.tested_commit": "0" * 40,
    "run.time_utc": "2026-11-15T00:00:00Z",
    "run.actor": "owner test",
    "run.python": "3.12.0",
}
CENTERS_INPUT = "catalog/centers_v1.json"
PAIRING_INPUT = "catalog/type_pairing_v1.json"
CONFIG_INPUT = "tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json at catalog/magic10_mechanics_v2.json"
THRESHOLDS_INPUT = "tests/fixtures/magic10_v2/thresholds_v2.fixture.json at math/thresholds.json"
RESULT_INPUT = "v1 real-path result re-identified as v2"
SCHEMA_FAILED = "refused M10V2_SCHEMA_VALIDATION_FAILED"

# Plan §6.1.3: mutation rows per schema.
MATRIX_COUNTS = {
    "schemas/centers_v1.schema.json": 6,
    "schemas/type_pairing_v1.schema.json": 19,
    "schemas/magic10_mechanics_v2.schema.json": 140,
    "schemas/thresholds_v2.schema.json": 12,
    "schemas/magic10_result_v2.schema.json": 20,
    "schemas/magic10_compat_result_v2.schema.json": 23,
}
# Plan §6.1.5: (family, mutation text) -> expected outcome tokens.
CLOSURE_EXPECTED = {
    ("catalog_closure", "g marked motor, rebound"): "refused M10V2_CENTER_MOTOR_MISMATCH",
    ("catalog_closure", "first center_id replaced, rebound"): f"{SCHEMA_FAILED} schema=schemas/centers_v1.schema.json",
    ("catalog_closure", "first center row removed, rebound"): f"{SCHEMA_FAILED} schema=schemas/centers_v1.schema.json",
    ("catalog_closure", "first two rules swapped, rebound"): "refused M10V2_PINNED_CONTENT_MISMATCH item=type_pairing",
    ("catalog_closure", "first two aura classes swapped, rebound"):
        "refused M10V2_PINNED_CONTENT_MISMATCH item=type_pairing",
    ("catalog_closure", "generator_projector communication 50 to 0, rebound"):
        "refused M10V2_PINNED_CONTENT_MISMATCH item=type_pairing",
    ("catalog_closure", "same_class harmony 0 to 25, rebound"):
        "refused M10V2_PINNED_CONTENT_MISMATCH item=type_pairing",
    ("catalog_closure", "same_class harmony cell removed, rebound"):
        f"{SCHEMA_FAILED} schema=schemas/type_pairing_v1.schema.json",
    ("catalog_closure", "last rule removed, rebound"): f"{SCHEMA_FAILED} schema=schemas/type_pairing_v1.schema.json",
    ("caps_closure", "signals 0 and 1 swapped"): "refused M10V2_SIGNAL_ORDER_MISMATCH",
    ("caps_closure", "signals 1 and 2 swapped across a category"): "refused M10V2_SIGNAL_ORDER_MISMATCH",
    ("caps_closure", "first signal removed"): f"{SCHEMA_FAILED} schema=schemas/magic10_mechanics_v2.schema.json",
    ("caps_closure", "one harmony input removed, rebound"): "refused MAGIC10_INPUTS_MISMATCH",
    ("caps_closure", "the two harmony inputs swapped, rebound"): "refused MAGIC10_INPUTS_MISMATCH",
    ("caps_closure", "a third harmony input added, rebound"): "refused MAGIC10_INPUTS_MISMATCH",
    ("caps_closure", "harmony max 100 to 99, rebound"): "refused INVALID_MAGIC10",
    ("caps_closure", "harmony min 0 to 1, rebound"): "refused INVALID_MAGIC10",
    ("thresholds_closure", "first category row removed, rebound"): f"{SCHEMA_FAILED} schema=schemas/thresholds_v2.schema.json",
    ("thresholds_closure", "second category_id set to the first, rebound"):
        f"{SCHEMA_FAILED} schema=schemas/thresholds_v2.schema.json",
    ("thresholds_closure", "first row's first two maxima swapped, rebound"): "refused M10V2_MAXIMA_NOT_ASCENDING",
    ("thresholds_closure", "first row's second maximum set equal to its first, rebound"):
        "refused M10V2_MAXIMA_NOT_ASCENDING",
    ("thresholds_closure", "first row's last maximum 100 to 99, rebound"):
        f"{SCHEMA_FAILED} schema=schemas/thresholds_v2.schema.json",
    ("thresholds_closure", "first row's third maximum set to 101, rebound"):
        f"{SCHEMA_FAILED} schema=schemas/thresholds_v2.schema.json",
    ("thresholds_closure", "first row's first maximum removed, rebound"):
        f"{SCHEMA_FAILED} schema=schemas/thresholds_v2.schema.json",
    ("identity", "harmony maxima set to 30 60 90 100 (in domain), rebound"): "admitted identity_differs",
}
GOVERNED = (
    "catalog/centers_v1.json",
    "catalog/type_pairing_v1.json",
    "schemas/centers_v1.schema.json",
    "schemas/magic10_compat_result_v2.schema.json",
    "schemas/magic10_mechanics_v2.schema.json",
    "schemas/magic10_result_v2.schema.json",
    "schemas/thresholds_v2.schema.json",
    "schemas/type_pairing_v1.schema.json",
)


@pytest.fixture(scope="module")
def rails_module():
    with pytest.MonkeyPatch.context() as patch:
        for name, value in CLOSED_RAILS.items():
            patch.setenv(name, value)
        yield


@pytest.fixture
def rails(monkeypatch):
    for name, value in CLOSED_RAILS.items():
        monkeypatch.setenv(name, value)


@pytest.fixture(scope="module")
def built(rails_module):
    """One real build of every family and the AC-08 lines at the current head."""

    before = _status("catalog", "math")
    paths = g.changed_paths_since_pre_delivery()
    evidence = g.build(membership=g.membership_in_process, paths=paths)
    return SimpleNamespace(evidence=evidence, paths=paths, status_before=before)


@pytest.fixture
def out(monkeypatch, tmp_path):
    path = tmp_path / "audit" / "qa" / "hde-epic042" / "pr-04" / "v2_contract_evidence.txt"
    monkeypatch.setattr(g, "OUT", path)
    return path


def _status(*paths: str) -> bytes:
    return subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all", "--", *paths],
        cwd=ROOT, capture_output=True, check=True,
    ).stdout


def _rows(evidence, family: str | None = None):
    return [row for row in evidence.rows if family is None or row.family == family]


def _stored() -> bytes:
    return (ROOT / g.OUT_REL).read_bytes()


def _membership_key(key: str) -> bool:
    return key.startswith("ac08.membership.")


# --- T-01, T-02: the committed record ---------------------------------------------------------

def test_t01_check_passes_on_the_committed_record_and_writes_nothing(rails, capsys):
    committed = _stored()
    g.main(["--check"])
    assert capsys.readouterr().out in {
        "v2 contract evidence check ok (tested commit present)\n",
        "v2 contract evidence check ok (tested commit absent)\n",
    }
    assert _stored() == committed


def test_t02_the_build_reproduces_the_committed_record(built):
    stored = g.parse_record(_stored())
    run = {key: value for key, value in stored if key in g.RUN_FIELDS}
    expected = g.record_lines(built.evidence, run)
    assert [line for line in expected if not _membership_key(line[0])] == [
        line for line in stored if not _membership_key(line[0])
    ]
    values = dict(stored)
    assert values["status"] == "PASS"
    assert all(value.endswith("; result=pass") for key, value in stored if key.startswith("row."))
    assert values["rows.total"] == values["rows.passed"] == "273"


# --- T-03 to T-09: the families on actual bundles ---------------------------------------------

def test_t03_row_counts_per_family_and_schema(built):
    rows = built.evidence.rows
    assert len(rows) == 273
    families = collections.Counter(row.family for row in rows)
    assert families == {
        "schema_matrix": 226, "catalog_closure": 10, "caps_closure": 9,
        "thresholds_closure": 8, "identity": 4, "canonical_bytes": 16,
    }
    per_schema = collections.Counter()
    for row in _rows(built.evidence, "schema_matrix"):
        if row.mutation != "actual":
            per_schema[row.expected.split("schema=")[1]] += 1
    assert per_schema == MATRIX_COUNTS
    actual = [row for row in rows if row.mutation == "actual"]
    assert len(actual) == 19


def test_t04_every_matrix_mutation_is_refused_at_its_own_schema(built):
    for row in _rows(built.evidence, "schema_matrix"):
        if row.mutation == "actual":
            continue
        schema = row.expected.split("schema=")[1]
        assert f"schema={schema}" in row.observed.split(), row.line()
        if row.input == RESULT_INPUT:
            assert row.observed.startswith("refused schema="), row.line()
        else:
            assert row.observed.startswith(f"{SCHEMA_FAILED} schema="), row.line()
        assert row.passed


def test_t05_the_enumeration_rule_on_the_real_centers_schema():
    schema = json.loads((ROOT / "schemas/centers_v1.schema.json").read_bytes())
    instance = json.loads((ROOT / "catalog/centers_v1.json").read_bytes())
    assert g.enumerate_mutations(schema, instance) == [
        ("unknown_field", "/"),
        ("required_dropped", "/centers"),
        ("unknown_field", "/centers/0"),
        ("required_dropped", "/centers/0/center_id"),
        ("required_dropped", "/centers/0/motor"),
        ("out_of_domain", "/centers/0/center_id"),
    ]


def test_t06_actual_bundle_admitted_and_result_instances_are_the_real_v1_output(built, rails):
    actual = [row for row in _rows(built.evidence, "schema_matrix") if row.mutation == "actual"]
    assert [row.observed for row in actual] == ["admitted"] * 4 + ["accepted"] * 2

    def party(rel: str, label: str):
        data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        return evaluation_party(cli_main._resolve_party(cli_main._normalize_party(dict(data), label),
                                                        source_policy="local"))

    class Cache:
        def __init__(self):
            self.values = []

        def get(self, key):
            return None

        def put(self, key, value):
            self.values.append(value)

    cache = Cache()
    compat = evaluate_pair(party("fixtures/charts/alice.json", "left"), party("fixtures/charts/bob.json", "right"),
                           cache=cache)
    pure = cache.values[0]["result"]
    instances = g.result_instances()
    for real, reidentified in ((pure, instances[g.RESULT_SCHEMAS[0]]), (compat, instances[g.RESULT_SCHEMAS[1]])):
        assert set(real) == set(reidentified)
        differing = {key for key in real if real[key] != reidentified[key]}
        assert differing == {"schema", "config_id"}
        assert reidentified["config_id"] == "m10-relevance-centers-type-v2.0.0"
    assert instances[g.RESULT_SCHEMAS[0]]["schema"] == "magic10_result.v2"
    assert instances[g.RESULT_SCHEMAS[1]]["schema"] == "magic10_compat_result.v2"


def test_t07_closure_identity_and_canonical_rows_carry_the_planned_outcomes(built):
    seen = {}
    for row in built.evidence.rows:
        if row.family in {"schema_matrix", "canonical_bytes"} or row.mutation == "actual":
            continue
        seen.setdefault((row.family, row.mutation), []).append(row)
    assert set(seen) == set(CLOSURE_EXPECTED)
    for key, rows in seen.items():
        for row in rows:
            assert row.expected == CLOSURE_EXPECTED[key], row.line()
            assert row.passed, row.line()
    assert len(seen[("identity", "harmony maxima set to 30 60 90 100 (in domain), rebound")]) == 2
    for row in built.evidence.rows:
        if row.mutation == "actual" and row.family != "schema_matrix":
            assert row.observed in {"pass", "canonical=true"}, row.line()
    canonical = [row for row in _rows(built.evidence, "canonical_bytes") if row.mutation != "actual"]
    assert [row.input for row in canonical] == list(GOVERNED)
    assert all(row.observed == "canonical=false refused NONCANONICAL_JSON" for row in canonical)


def test_t08_the_eight_governed_files_are_canonical_bytes():
    for rel in GOVERNED:
        raw = (ROOT / rel).read_bytes()
        assert canon.sercanon(json.loads(raw), sort_keys=True) == raw, rel


def test_t09_tested_inputs_cover_every_file_the_run_reads(rails, monkeypatch):
    reads: list[tuple[str, str]] = []
    original = registry_loader._read_captured_file

    def recording(root, relative_path):
        reads.append((str(root), relative_path))
        return original(root, relative_path)

    monkeypatch.setattr(registry_loader, "_read_captured_file", recording)
    with tempfile.TemporaryDirectory() as raw:
        base = g.assemble(Path(raw))
        bundle, refusal = g.admit(base)
        assert bundle is not None, refusal
        admission = {g.FIXTURES.get(rel, rel) for root, rel in reads if Path(root) == base}
        reads.clear()
        g.result_instances()
        result_path = {rel for root, rel in reads}
    tested = set(g.TESTED_INPUTS)
    assert admission and admission <= tested
    assert result_path <= tested | set(ADMITTED_RELEASE_ROSTER) | {"catalog/manifest.json"}
    assert {"tools/evidence/generate_hde_epic042_v2_contract_evidence.py", "engine/config/magic10_v2_loader.py",
            "engine/config/registry_loader.py", "catalog/manifest.json"} <= tested
    assert all((ROOT / rel).is_file() for rel in tested)
    assert list(g.TESTED_INPUTS) == sorted(tested)


# --- T-10, T-11: the modes --------------------------------------------------------------------

def _record(built) -> bytes:
    return g.render(g.record_lines(built.evidence, RUN))


def _replace(record: bytes, key: str, value: str) -> bytes:
    lines = g.parse_record(record)
    assert key in dict(lines)
    return g.render([(k, value if k == key else v) for k, v in lines])


@pytest.mark.parametrize("key, value, reason", [
    ("row.0001", "family=schema_matrix; changed", "row.0001"),
    ("tested_inputs.sha256", "0" * 64, "tested_inputs.sha256"),
    ("run.tested_commit", "not-a-commit", "run.tested_commit"),
    ("run.time_utc", "2026-11-15 00:00:00", "run.time_utc"),
    ("run.actor", "", "run.actor"),
    ("run.python", "three", "run.python"),
])
def test_t10_check_reports_drift(built, rails, out, monkeypatch, key, value, reason):
    monkeypatch.setattr(g, "build", lambda **kwargs: built.evidence)
    out.parent.mkdir(parents=True)
    out.write_bytes(_replace(_record(built), key, value))
    with pytest.raises(SystemExit) as raised:
        g.check()
    assert str(raised.value) == f"DRIFT:{g.OUT_REL}:{reason}"


def test_t10_check_reports_a_missing_record(rails, out):
    with pytest.raises(SystemExit) as raised:
        g.check()
    assert str(raised.value) == f"DRIFT:{g.OUT_REL}:missing"


def test_t11_write_refuses_a_dirty_tree_and_unavailable_history(rails, out, monkeypatch):
    monkeypatch.setattr(g, "tree_is_clean", lambda: False)
    with pytest.raises(SystemExit) as raised:
        g.write("owner test")
    assert str(raised.value) == g.DIRTY_EXIT
    monkeypatch.setattr(g, "tree_is_clean", lambda: True)
    monkeypatch.setattr(g, "commit_present", lambda commit: False)
    with pytest.raises(SystemExit) as raised:
        g.write("owner test")
    assert str(raised.value) == g.HISTORY_EXIT
    assert not out.exists()


def test_t11_write_refuses_an_invalid_actor_and_bad_arguments(rails, out):
    with pytest.raises(SystemExit) as raised:
        g.write("")
    assert str(raised.value) == "V2_CONTRACT_EVIDENCE_INVALID_ACTOR"
    for argv in ([], ["--check", "--actor", "owner test"]):
        with pytest.raises(SystemExit) as raised:
            g.main(argv)
        assert raised.value.code == 2
    assert not out.exists()


def test_t11_write_refuses_a_failing_row_and_writes_nothing(built, rails, out, monkeypatch, capsys):
    failing = copy.copy(built.evidence)
    broken = g.Row("caps_closure", "HDE-SEPA007.2", "x", "y", "refused NEVER", "admitted")
    object.__setattr__(failing, "rows", built.evidence.rows + (broken,))
    monkeypatch.setattr(g, "tree_is_clean", lambda: True)
    monkeypatch.setattr(g, "build", lambda **kwargs: failing)
    with pytest.raises(SystemExit) as raised:
        g.write("owner test")
    assert str(raised.value) == f"{g.FAILED_EXIT}:1"
    assert "refused NEVER" in capsys.readouterr().err
    assert not out.exists()


def test_t11_write_success_records_run_fields_and_reproducible_lines(built, rails, out, monkeypatch):
    monkeypatch.setattr(g, "tree_is_clean", lambda: True)
    monkeypatch.setattr(g, "build", lambda **kwargs: built.evidence)
    record = g.write("owner test")
    assert out.read_bytes() == record
    lines = g.parse_record(record)
    run = {key: value for key, value in lines if key in g.RUN_FIELDS}
    assert g._run_fields_valid(run) is None
    assert run["run.tested_commit"] == g.head_commit()
    assert run["run.actor"] == "owner test"
    assert lines == g.record_lines(built.evidence, run)


# --- T-12 to T-14: AC-08, layout and the repository tree --------------------------------------

def test_t12_ac08_lines(built, rails):
    values = dict(built.evidence.ac08)
    for key in ("ac08.unchanged_since_unit_base", "ac08.unchanged_since_pre_delivery", "ac08.membership",
                "ac08.determinism_gate_check", "ac08.pr01_generator_check", "ac08.active_identity"):
        assert values[key] == "pass", key
    count = int(values["ac08.membership.count"])
    assert count == len(built.paths) > 0
    for index in range(1, count + 1):
        assert values[f"ac08.membership.{index}"].startswith("not-member ")
    active = load_active_mechanics_bundle()
    assert values["ac08.active_release_id"] == active.release_id == g.EXPECTED_ACTIVE_RELEASE_ID
    assert values["ac08.active_config_id"] == active.mechanics["config_id"] == g.EXPECTED_ACTIVE_CONFIG_ID


def test_t13_the_record_layout_is_closed(built):
    record = _record(built)
    text = record.decode("utf-8")
    assert text.endswith("\n") and not text.endswith("\n\n") and "\r" not in text
    keys = [key for key, _ in g.parse_record(record)]
    assert len(keys) == len(set(keys))
    assert keys[:7] == ["schema", "epic_id", "task_id", "subtask_id", "evidences", "work_unit_id", "evidence_class"]
    assert keys[7:11] == list(g.RUN_FIELDS)
    assert keys[-1] == "status"
    assert keys[-7:-1] == [f"limitation.{index}" for index in range(1, 7)]
    assert text.startswith("schema: hde_epic042_v2_contract_evidence.v1\n")
    for forbidden in (tempfile.gettempdir(), "Traceback", "Error:", str(ROOT)):
        assert forbidden not in text


def test_t14_no_repository_catalog_or_math_file_changes(built):
    assert _status("catalog", "math") == built.status_before
    assert not (ROOT / "catalog" / "magic10_mechanics_v2.json").exists()
    leftovers = [path for path in Path(tempfile.gettempdir()).glob("hde-epic042-pr04-*")]
    assert leftovers == []
