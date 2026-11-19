"""Owner test of the HDE-EPIC042 WU-PR-04 Separation v2 contract evidence generator.

HDE-SEPA007.5. The generator runs on the repository as it is: the governed v2
catalogs and schemas, the labelled non-canon fixtures, the WU-PR-03 loader's
public admission function and the admitted release's real compat path.  One
build is shared by the module; the record-dependent cases read the committed
record.  Expected counts and outcomes are transcribed from the detailed plan
(WU-PR-04 plan v1.0 §6.1.3 and §6.1.5; for the AC-08 re-target at the v2 cut,
HDE-EPIC043 WU-PR-10 plan v1.0 §6.11) and from canon, not read back from the
generator.  Nothing is written under the repository tree; write-mode cases
write to ``tmp_path``.
"""
from __future__ import annotations

import collections
import copy
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path
from types import SimpleNamespace

import pytest

import engine.config.registry_loader as registry_loader
from engine.cli import main as cli_main
from engine.compat.compute import evaluate_pair, evaluation_party
from engine.config.magic10_v2_loader import MAGIC10_V2_CONFIG_ID
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
RESULT_INPUT = "v2 real-path result"
SCHEMA_FAILED = "refused M10V2_SCHEMA_VALIDATION_FAILED"
# HDE-EPIC042's fixed AC-08 history (WU-PR-10 plan v1.0 §6.11): WU-PR-03 to the
# WU-PR-04 squash merge, and WU-PR-01 (WU-PR-02's base) to the CL-05 close.
UNIT_BASE = "330a7e9124c360776fd3c5a2123b24421287c00e"
UNIT_END = "bdcf21d1c8ecb0657a66c786277f60e900933868"
PRE_DELIVERY_BASE = "a0b796bc64fe0f058e69ec81f79e2561a840c71d"
EPIC_END = "a9cf2356360ff93d413396381c3ae8089cc4f631"
V2_CONFIG_ID = "m10-relevance-centers-type-v2.0.0"
AC08_KEYS = (
    "ac08.unchanged_since_unit_base", "ac08.unchanged_since_pre_delivery", "ac08.membership",
    "ac08.determinism_gate_check", "ac08.pr01_generator_check", "ac08.active_identity",
)

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
    evidence = g.build()
    return SimpleNamespace(evidence=evidence, paths=_git_lines("diff", "--name-only", PRE_DELIVERY_BASE, EPIC_END),
                           status_before=before)


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


def _git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=True).stdout


def _git_lines(*args: str) -> list[str]:
    return sorted(line for line in _git(*args).decode("utf-8").splitlines() if line)


def _end_manifest() -> bytes:
    return _git("show", f"{EPIC_END}:catalog/manifest.json")


def _end_release_paths() -> list[str]:
    return [row["path"] for row in json.loads(_end_manifest())["files"]]


def _rows(evidence, family: str | None = None):
    return [row for row in evidence.rows if family is None or row.family == family]


def _stored() -> bytes:
    return (ROOT / g.OUT_REL).read_bytes()


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
    # The AC-08 ranges are fixed history, so the membership lines reproduce too.
    assert g.record_lines(built.evidence, run) == stored
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


def test_t06_actual_bundle_admitted_and_result_instances_are_the_real_v2_output(built, rails):
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
    release_id = hashlib.sha256((ROOT / "catalog/manifest.json").read_bytes()).hexdigest()
    # The admitted release's real path is v2: the instances are its output as produced.
    assert instances == {g.RESULT_SCHEMAS[0]: pure, g.RESULT_SCHEMAS[1]: compat}
    for instance in instances.values():
        assert instance["config_id"] == V2_CONFIG_ID == MAGIC10_V2_CONFIG_ID
        assert instance["release_id"] == release_id
    assert instances[g.RESULT_SCHEMAS[0]]["schema"] == "magic10_result.v2"
    assert instances[g.RESULT_SCHEMAS[1]]["schema"] == "magic10_compat_result.v2"


@pytest.mark.parametrize("field, value", [("schema", "magic10_compat_result.v1"),
                                          ("config_id", "m10-channel-state-v1.0.0")])
def test_t06_a_real_path_result_that_is_not_v2_is_refused_and_nothing_is_written(rails, out, monkeypatch,
                                                                                 field, value):
    real = g.evaluate_pair

    def stale(*args, **kwargs):
        return {**real(*args, **kwargs), field: value}

    monkeypatch.setattr(g, "evaluate_pair", stale)
    with pytest.raises(g.EvidenceError) as raised:
        g.result_instances()
    assert str(raised.value) == "REAL_PATH_RESULT_NOT_V2"
    monkeypatch.setattr(g, "tree_is_clean", lambda: True)
    with pytest.raises(SystemExit) as raised:
        g.main(["--actor", "owner test"])
    assert str(raised.value) == f"{g.FAILED_EXIT}:REAL_PATH_RESULT_NOT_V2"
    assert not out.exists()


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


@pytest.mark.parametrize("absent", [UNIT_BASE, UNIT_END, PRE_DELIVERY_BASE, EPIC_END])
def test_t11_both_modes_refuse_when_any_fixed_history_commit_is_absent(built, rails, out, monkeypatch, absent):
    assert g.HISTORY_COMMITS == (UNIT_BASE, UNIT_END, PRE_DELIVERY_BASE, EPIC_END)
    real = g.commit_present
    monkeypatch.setattr(g, "commit_present", lambda commit: commit != absent and real(commit))
    monkeypatch.setattr(g, "tree_is_clean", lambda: True)
    monkeypatch.setattr(g, "build", lambda **kwargs: pytest.fail("built without the fixed history"))
    with pytest.raises(SystemExit) as raised:
        g.write("owner test")
    assert str(raised.value) == g.HISTORY_EXIT == "V2_CONTRACT_EVIDENCE_HISTORY_UNAVAILABLE"
    assert not out.exists()
    out.parent.mkdir(parents=True)
    out.write_bytes(_record(built))
    with pytest.raises(SystemExit) as raised:
        g.check()
    assert str(raised.value) == g.HISTORY_EXIT


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
    assert (g.UNIT_BASE, g.UNIT_END, g.PRE_DELIVERY_BASE, g.EPIC_END) == (
        UNIT_BASE, UNIT_END, PRE_DELIVERY_BASE, EPIC_END)
    values = dict(built.evidence.ac08)
    for key in AC08_KEYS:
        assert values[key] == "pass", key
    count = int(values["ac08.membership.count"])
    assert values["ac08.membership.changed_since"] == PRE_DELIVERY_BASE
    assert count == len(built.paths) > 0
    end_paths = set(_end_release_paths())
    assert len(end_paths) == 45
    for index, path in enumerate(built.paths, 1):
        assert values[f"ac08.membership.{index}"] == f"not-member {path}"
        assert path not in end_paths
    keys = [key for key, _ in built.evidence.ac08]
    assert keys[-7:] == ["ac08.membership", "ac08.determinism_gate_check", "ac08.pr01_generator_check",
                         "ac08.active_release_id", "ac08.active_config_id", "ac08.prior_release_id",
                         "ac08.active_identity"]
    active = load_active_mechanics_bundle()
    manifest_digest = hashlib.sha256((ROOT / "catalog/manifest.json").read_bytes()).hexdigest()
    prior = hashlib.sha256(_end_manifest()).hexdigest()
    assert values["ac08.active_release_id"] == active.release_id == manifest_digest
    assert values["ac08.active_config_id"] == active.mechanics["config_id"] == MAGIC10_V2_CONFIG_ID == V2_CONFIG_ID
    assert values["ac08.prior_release_id"] == prior != active.release_id


def test_t12_the_ac08_history_is_fixed_and_judged_against_the_end_release_not_the_head_roster(rails):
    end_paths = _end_release_paths()
    assert list(g.end_release_paths()) == end_paths
    assert g._diff_paths() == ("catalog/manifest.json", *end_paths)
    for base, end in ((UNIT_BASE, UNIT_END), (PRE_DELIVERY_BASE, EPIC_END)):
        assert subprocess.run(["git", "diff", "--quiet", base, end, "--", "catalog/manifest.json", *end_paths],
                              cwd=ROOT).returncode == 0
    paths = _git_lines("diff", "--name-only", PRE_DELIVERY_BASE, EPIC_END)
    assert list(g.changed_paths_in_epic042()) == paths
    # HDE-EPIC042 delivered paths that the cut admits: the head's roster would
    # call them members, so membership is judged against EPIC_END's release.
    admitted_since = sorted(set(paths) & set(ADMITTED_RELEASE_ROSTER))
    assert "catalog/centers_v1.json" in admitted_since
    assert set(g.membership_in_process(paths).values()) == {"not-member"}
    assert g.membership_in_process(["engine/core/core.py"]) == {"engine/core/core.py": "member"}


def _fake_active(release_id: str, config_id: str = V2_CONFIG_ID):
    return SimpleNamespace(release_id=release_id, mechanics={"config_id": config_id})


def _ac08_with(monkeypatch, *, active=None, prior=None, tool_rc=0, paths=None):
    """``ac08_lines`` with the two ``--check`` children and, optionally, the identities replaced."""

    monkeypatch.setattr(g, "run_tool", lambda *args: subprocess.CompletedProcess(args, tool_rc, b"", b""))
    if active is not None:
        monkeypatch.setattr(g, "load_active_mechanics_bundle", lambda: active)
    if prior is not None:
        monkeypatch.setattr(g, "prior_release_id", lambda: prior)
    paths = g.changed_paths_in_epic042() if paths is None else paths
    return dict(g.ac08_lines(paths, g.membership_in_process(paths)))


def test_t12_ac08_passes_with_its_own_seams(rails, monkeypatch):
    values = _ac08_with(monkeypatch)
    assert [values[key] for key in AC08_KEYS] == ["pass"] * len(AC08_KEYS)


def _manifest_digest() -> str:
    return hashlib.sha256((ROOT / "catalog/manifest.json").read_bytes()).hexdigest()


@pytest.mark.parametrize("case", ["release_not_manifest", "config_not_v2", "release_equals_prior",
                                  "end_release_member", "determinism_and_tuning_checks"])
def test_t12_ac08_negative_controls_fail_their_named_line_and_write_refuses(built, rails, out, monkeypatch,
                                                                            capsys, case):
    named = {
        "release_not_manifest": ("ac08.active_identity", "fail"),
        "config_not_v2": ("ac08.active_identity", "fail"),
        "release_equals_prior": ("ac08.active_identity", "fail"),
        "end_release_member": ("ac08.membership", "fail"),
        "determinism_and_tuning_checks": ("ac08.determinism_gate_check", "fail rc=1"),
    }[case]
    if case == "release_not_manifest":
        values = _ac08_with(monkeypatch, active=_fake_active("0" * 64))
    elif case == "config_not_v2":
        values = _ac08_with(monkeypatch, active=_fake_active(_manifest_digest(), "m10-channel-state-v1.0.0"))
    elif case == "release_equals_prior":
        values = _ac08_with(monkeypatch, prior=_manifest_digest())
    elif case == "end_release_member":
        values = _ac08_with(monkeypatch, paths=("engine/core/core.py",))
        assert values["ac08.membership.1"] == "member engine/core/core.py"
    else:
        values = _ac08_with(monkeypatch, tool_rc=1)
        assert values["ac08.pr01_generator_check"] == "fail rc=1"
    assert values[named[0]] == named[1]
    failing = sorted(key for key in AC08_KEYS if values[key] != "pass")
    assert failing == (sorted({"ac08.determinism_gate_check", "ac08.pr01_generator_check"})
                       if case == "determinism_and_tuning_checks" else [named[0]])
    lines = tuple(values.items())
    assert not g.ac08_passed(lines)
    evidence = copy.copy(built.evidence)
    object.__setattr__(evidence, "ac08", lines)
    monkeypatch.setattr(g, "tree_is_clean", lambda: True)
    monkeypatch.setattr(g, "build", lambda **kwargs: evidence)
    with pytest.raises(SystemExit) as raised:
        g.write("owner test")
    assert str(raised.value) == f"{g.FAILED_EXIT}:{len(failing)}"
    assert f"{named[0]}: {named[1]}" in capsys.readouterr().err
    assert not out.exists()


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
    lines = g.parse_record(record)
    # Retired at the v2 cut: the pre-cutover limitation, the head-relative ranges,
    # the 45-path head roster and the re-identification of a v1 result.
    for key, value in lines:
        if key.startswith(("limitation.", "command.")):
            assert "before the v2 cutover" not in value and "before the cutover" not in value, key
            assert "re-identified" not in value and "HEAD" not in value and "<45 " not in value, key
    assert not any("prepush_check.py" in value for key, value in lines if key.startswith("command."))
    assert "re-identified" not in text
    for forbidden in (tempfile.gettempdir(), "Traceback", "Error:", str(ROOT)):
        assert forbidden not in text


def test_t14_no_repository_catalog_or_math_file_changes(built):
    assert _status("catalog", "math") == built.status_before
    # The fixtures were placed only in the temporary root: the repository's paths
    # still hold the admitted release's bytes, as its manifest binds them.
    rows = {row["path"]: row for row in json.loads((ROOT / "catalog/manifest.json").read_bytes())["files"]}
    for placed, fixture in g.FIXTURES.items():
        raw = (ROOT / placed).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == rows[placed]["sha256"] and len(raw) == rows[placed]["size"]
        assert raw != (ROOT / fixture).read_bytes()
    leftovers = [path for path in Path(tempfile.gettempdir()).glob("hde-epic042-pr04-*")]
    assert leftovers == []
