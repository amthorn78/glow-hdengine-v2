"""Owner tests of the Magic-10 v2 proof family record writer (HDE-EPIC043 WU-PR-13; HDE-DIST008.1).

One case runs the committed record's real ``--check`` in a second process (W-1), which runs the
whole family once.  Every other case runs the writer in process over a reduced set, writing only
to a temporary record path: six real index rows (F-01, F-06, F-07, F-08, F-21 and F-24, which
carry every basis and the two non-vacuity cases), the index's own pin replaced by a no-op that the
reduced rows cannot satisfy, a family run built from those rows' nodes with each case passed, the
real golden comparison and the admitted root bundle.  Negative controls break one writer check
each and assert its named refusal, reached after every earlier check passes (PF10 addendum 2.6
R-3; addendum 2.19 LR-2).
"""
from __future__ import annotations

import dataclasses
import json
import os
import subprocess
import sys
from types import SimpleNamespace

import pytest

from engine.config.registry_loader import RegistryConfigError, _load_active_mechanics_bundle_from_root
from engine.runtime.determinism_env import DETERMINISM_ENV_PINS
from tools.evidence import generate_hde_epic043_v2_proof_family_record as writer

ACTOR = "test actor"
REDUCED_IDS = ("F-01", "F-06", "F-07", "F-08", "F-21", "F-24")
REAL_CHECK_TIMEOUT_SECONDS = 1800
F06_CUT_MUTATION = "tests/m10_v2/test_family_signals_calculation.py::test_f06_mutation_exclusive_maxima_at_the_cut_is_refused"
F08_RELEASE_MUTATION = "tests/m10_v2/test_family_identity_and_reader.py::test_f08_mutation_pair_key_without_the_release_is_refused"
SURFACE_MODULE = "tests/m10_v2/test_family_surface.py"


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.chdir(writer.ROOT)


@pytest.fixture(scope="module")
def admitted():
    return _load_active_mechanics_bundle_from_root(writer.ROOT)


@pytest.fixture(scope="module")
def golden_comparison():
    saved = {key: os.environ.get(key) for key in DETERMINISM_ENV_PINS}
    os.environ.update(DETERMINISM_ENV_PINS)
    try:
        return writer.compare_goldens_at_root()
    finally:
        for key, value in saved.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


@pytest.fixture(scope="module")
def reduced_rows():
    rows = {row["id"]: row for row in writer.load_index().rows}
    return tuple(rows[item_id] for item_id in REDUCED_IDS)


def passed_run(rows, *, returncode=0, outcome=None, drop=None, extra=()):
    """A family run over ``rows``' nodes and the non-vacuity pin, one passed case each."""

    nodes = [*writer.indexed_nodes(rows), *writer.NONVACUITY_PIN_NODES]
    cases = [writer.FamilyCase(node, node, (outcome or {}).get(node, "passed")) for node in nodes if node != drop]
    return writer.FamilyRun(returncode, tuple([*cases, *extra]))


class FamilyRunSpy:
    def __init__(self, run):
        self.run, self.calls = run, 0

    def __call__(self, outside_nodes):
        self.calls += 1
        return self.run


@pytest.fixture
def reduced(tmp_path, monkeypatch, admitted, golden_comparison, reduced_rows):
    out = tmp_path / "v2_proof_family_record.txt"
    spy = FamilyRunSpy(passed_run(reduced_rows))
    monkeypatch.setattr(writer, "out_path", lambda: out)
    monkeypatch.setattr(writer, "load_root_bundle", lambda: admitted)
    monkeypatch.setattr(writer, "compare_goldens_at_root", lambda: golden_comparison)
    monkeypatch.setattr(writer, "load_index", lambda: writer.FamilyIndex(reduced_rows, lambda rows: None))
    monkeypatch.setattr(writer, "run_family", spy)
    return SimpleNamespace(out=out, spy=spy, rows=reduced_rows)


def _refused(code_prefix: str):
    return pytest.raises(writer.ProofFamilyRecordRefusal, match=f"^{code_prefix}")


def _record(out) -> dict[str, str]:
    return dict(writer.parse_record(out.read_bytes()))


def _rows_with(rows, item_id, **changes):
    return tuple({**row, **changes} if row["id"] == item_id else row for row in rows)


def _git_status() -> bytes:
    return subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=writer.ROOT,
                          capture_output=True, check=True).stdout


def _read_input_with(monkeypatch, rel, change):
    real = writer.read_input

    def read(path):
        data = real(path)
        return change(data) if path == rel else data

    monkeypatch.setattr(writer, "read_input", read)


# --- W-1: the committed record, by the real --check in a second process ---------------------------

def test_the_committed_record_passes_the_real_check_in_a_second_process() -> None:
    env = {**os.environ, **DETERMINISM_ENV_PINS, "APP_ENV": "dev"}
    result = subprocess.run([sys.executable, writer.GENERATOR_REL, "--check"], cwd=writer.ROOT, env=env,
                            capture_output=True, timeout=REAL_CHECK_TIMEOUT_SECONDS)
    assert result.returncode == 0, result.stderr.decode("utf-8", "replace")[-2000:]
    assert result.stdout == b"v2 proof family record check ok\n"


# --- W-2 and W-3: the PASS path, byte-stable ------------------------------------------------------

def test_write_then_check_twice_is_byte_stable_and_writes_nothing_else(reduced) -> None:
    before = _git_status()
    written = writer.write(ACTOR)
    writer.check()
    writer.check()
    assert reduced.out.read_bytes() == written
    assert _git_status() == before
    assert reduced.spy.calls == 3


def test_each_item_renders_its_cases_basis_and_pass(reduced, admitted) -> None:
    writer.write(ACTOR)
    record = _record(reduced.out)
    for row in reduced.rows:
        item = f"item.{row['id']}"
        assert record[f"{item}.basis"] == row["basis"] and record[f"{item}.result"] == "PASS"
        assert [record[f"{item}.passing.{n}"] for n in range(1, len(row["passing"]) + 1)] == [
            f"{node} cases=1 passed=1" for node in row["passing"]]
        assert [record[f"{item}.mutation.{n}"] for n in range(1, len(row["mutations"]) + 1)] == [
            f"{node} cases=1 refused=1" for node in row["mutations"]]
    assert admitted.release_id in record["item.F-06.ran_against"]
    assert admitted.release_id in record["item.F-24.ran_against"] and "fixture bundle" in record["item.F-24.ran_against"]
    assert record["item.F-01.ran_against"].startswith("the labelled fixture bundle: config_id m10-relevance-centers-type-v2.0.0")
    assert record["item.F-07.ran_against"] == "no release: static source analysis"
    assert record["release.release_id"] == admitted.release_id and record["release.member_count"] == "52"
    assert record["goldens.match"] == "8 of 8" and record["nonvacuity.broad_handlers"] == "0"
    assert record["items.pass"] == str(len(REDUCED_IDS)) and list(record)[-1] == "status"


# --- W-4: a stale or edited record ------------------------------------------------------------------

def test_check_refuses_a_missing_record(reduced) -> None:
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:missing$"):
        writer.check()


def test_check_refuses_an_edited_line(reduced) -> None:
    writer.write(ACTOR)
    data = reduced.out.read_bytes().replace(b"item.F-06.result: PASS", b"item.F-06.result: PASX")
    reduced.out.write_bytes(data)
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:item.F-06.result$"):
        writer.check()


def test_check_refuses_a_changed_tested_input_before_the_family_runs(reduced, monkeypatch) -> None:
    writer.write(ACTOR)
    calls = reduced.spy.calls
    _read_input_with(monkeypatch, "tools/config/artifacts.py", lambda data: data + b"# changed\n")
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:input.tools/config/artifacts.py.sha256$"):
        writer.check()
    assert reduced.spy.calls == calls


def test_check_refuses_a_malformed_run_field(reduced) -> None:
    writer.write(ACTOR)
    lines = reduced.out.read_bytes().decode("utf-8").splitlines(keepends=True)
    lines[5] = "run.time_utc: yesterday\n"
    reduced.out.write_bytes("".join(lines).encode("utf-8"))
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:run.time_utc$"):
        writer.check()


# --- W-5: preconditions ------------------------------------------------------------------------------

def test_open_rails_are_refused_and_nothing_is_written(reduced, monkeypatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    with _refused(writer.RAILS_NOT_CLOSED):
        writer.write(ACTOR)
    assert not reduced.out.exists() and reduced.spy.calls == 0


def test_an_app_env_outside_dev_test_local_is_refused(reduced, monkeypatch) -> None:
    monkeypatch.setenv("APP_ENV", "prod")
    with _refused(writer.APP_ENV_NOT_DEV):
        writer.write(ACTOR)
    assert not reduced.out.exists()


def test_another_working_directory_is_refused(reduced, monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    with _refused(writer.WORKING_DIRECTORY_INVALID):
        writer.write(ACTOR)
    assert not reduced.out.exists()


@pytest.mark.parametrize("actor", ["", " padded", "line\nbreak", "x" * 201])
def test_an_invalid_actor_is_refused(reduced, actor) -> None:
    with _refused(writer.INVALID_ACTOR):
        writer.write(actor)
    assert not reduced.out.exists()


# --- W-6: a non-admitted or v1 release ------------------------------------------------------------------

def _bundle_like(admitted, **changes):
    mechanics = {**admitted.mechanics, **changes.pop("mechanics", {})}
    return SimpleNamespace(release_id=changes.pop("release_id", admitted.release_id), mechanics=mechanics,
                           manifest=admitted.manifest)


def test_the_v1_release_of_main_is_refused(reduced, monkeypatch, admitted) -> None:
    v1 = _bundle_like(admitted, mechanics={"config_id": "m10-channel-state-v1.0.0", "result_schema": "magic10_result.v1"},
                      release_id="2d5a4ec485fde5dd51004e0286fff1cb1211e4ee79fa71bc62b2a5ecd0b6c129")
    monkeypatch.setattr(writer, "load_root_bundle", lambda: v1)
    with _refused(f"{writer.NOT_ADMITTED_V2_PATH}:release"):
        writer.write(ACTOR)
    assert not reduced.out.exists() and reduced.spy.calls == 0


def test_a_release_id_other_than_the_manifest_digest_is_refused(reduced, monkeypatch, admitted) -> None:
    monkeypatch.setattr(writer, "load_root_bundle", lambda: _bundle_like(admitted, release_id="f" * 64))
    with _refused(f"{writer.NOT_ADMITTED_V2_PATH}:release"):
        writer.write(ACTOR)


def test_a_root_that_does_not_admit_is_refused(reduced, monkeypatch) -> None:
    def refuse():
        raise RegistryConfigError("MANIFEST_MEMBER_HASH_MISMATCH", "member bytes differ")

    monkeypatch.setattr(writer, "load_root_bundle", refuse)
    with _refused(f"{writer.RELEASE_REFUSED}:MANIFEST_MEMBER_HASH_MISMATCH"):
        writer.write(ACTOR)


# --- N-1 to N-8: one control per writer check, each reaching it -----------------------------------------

def test_n1_an_indexed_node_with_no_case_is_refused(reduced, monkeypatch) -> None:
    node = reduced.rows[1]["passing"][0]
    monkeypatch.setattr(writer, "run_family", FamilyRunSpy(passed_run(reduced.rows, drop=node)))
    with _refused(f"{writer.NODE_NOT_RUN}:F-06:{node}"):
        writer.write(ACTOR)
    assert not reduced.out.exists()


def test_n2_a_failed_passing_case_is_refused(reduced, monkeypatch) -> None:
    node = reduced.rows[0]["passing"][0]
    monkeypatch.setattr(writer, "run_family", FamilyRunSpy(passed_run(reduced.rows, outcome={node: "failure"})))
    with _refused(f"{writer.ITEM_FAILED}:F-01:{node}"):
        writer.write(ACTOR)


@pytest.mark.parametrize("item_id,node", [("F-06", F06_CUT_MUTATION), ("F-08", F08_RELEASE_MUTATION)])
def test_n3_a_mutation_that_is_not_refused_is_refused(reduced, monkeypatch, item_id, node) -> None:
    monkeypatch.setattr(writer, "run_family", FamilyRunSpy(passed_run(reduced.rows, outcome={node: "failure"})))
    with _refused(f"{writer.MUTATION_NOT_REFUSED}:{item_id}:{node}"):
        writer.write(ACTOR)


def test_n4_an_unindexed_case_not_passed_is_refused(reduced, monkeypatch) -> None:
    extra = writer.FamilyCase("tests/m10_v2/test_signals.py::test_x[a]", "tests/m10_v2/test_signals.py::test_x", "skipped")
    monkeypatch.setattr(writer, "run_family", FamilyRunSpy(passed_run(reduced.rows, extra=(extra,))))
    with _refused(f"{writer.FAMILY_CASE_NOT_PASSED}:tests/m10_v2/test_signals.py::test_x\\[a\\]"):
        writer.write(ACTOR)


def test_n4_a_failing_exit_with_every_case_passed_is_refused(reduced, monkeypatch) -> None:
    monkeypatch.setattr(writer, "run_family", FamilyRunSpy(passed_run(reduced.rows, returncode=1)))
    with _refused(f"{writer.FAMILY_RUN_FAILED}:1$"):
        writer.write(ACTOR)


@pytest.mark.parametrize("item_id,basis", [("F-06", "test maxima"), ("F-08", "fixture bundle")])
def test_n5_an_item_due_here_not_on_the_active_release_is_refused(reduced, monkeypatch, item_id, basis) -> None:
    rows = _rows_with(reduced.rows, item_id, basis=basis)
    monkeypatch.setattr(writer, "load_index", lambda: writer.FamilyIndex(rows, lambda rows: None))
    with _refused(f"{writer.INDEX_INVALID}:{item_id}$"):
        writer.write(ACTOR)
    assert reduced.spy.calls == 0


def test_n5_the_index_pin_refusal_is_refused(reduced, monkeypatch) -> None:
    def pin(rows):
        raise AssertionError("F-15")

    monkeypatch.setattr(writer, "load_index", lambda: writer.FamilyIndex(reduced.rows, pin))
    with _refused(f"{writer.INDEX_INVALID}:pin:F-15$"):
        writer.write(ACTOR)


def test_n6_a_fixture_configuration_differing_from_the_cut_is_refused(reduced, monkeypatch) -> None:
    def change(data):
        configuration = json.loads(data)
        configuration["signals"][0]["channels"][0]["weight"] += 1
        return json.dumps(configuration).encode("utf-8")

    _read_input_with(monkeypatch, writer.FIXTURE_CONFIG_REL, change)
    with _refused(f"{writer.FIXTURE_CONFIGURATION_DIVERGED}$"):
        writer.write(ACTOR)
    assert reduced.spy.calls == 0


def test_n6_fixture_thresholds_differing_beyond_the_maxima_are_refused(reduced, monkeypatch) -> None:
    def change(data):
        thresholds = json.loads(data)
        thresholds["categories"].reverse()
        return json.dumps(thresholds).encode("utf-8")

    _read_input_with(monkeypatch, writer.FIXTURE_THRESHOLDS_REL, change)
    with _refused(f"{writer.FIXTURE_THRESHOLDS_DIVERGED}$"):
        writer.write(ACTOR)


def test_n7_a_golden_mismatch_is_refused(reduced, monkeypatch, golden_comparison) -> None:
    cases = (dataclasses.replace(golden_comparison.cases[0], outcome="mismatch"), *golden_comparison.cases[1:])
    broken = dataclasses.replace(golden_comparison, cases=cases, ok=False)
    monkeypatch.setattr(writer, "compare_goldens_at_root", lambda: broken)
    with _refused(f"{writer.GOLDEN_MISMATCH}:M10-G001$"):
        writer.write(ACTOR)


def test_n8_a_broad_handler_in_a_mutation_module_is_refused(reduced, monkeypatch) -> None:
    _read_input_with(monkeypatch, SURFACE_MODULE,
                     lambda data: data + b"\n\ntry:\n    pass\nexcept Exception:\n    pass\n")
    with _refused(f"{writer.BROAD_HANDLER}:{SURFACE_MODULE}:"):
        writer.write(ACTOR)
    assert not reduced.out.exists()

