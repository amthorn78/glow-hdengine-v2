"""Owner tests of the FERM009 observation report writer (HDE-EPIC043 WU-PR-14; HDE-FERM009; R-17).

The real score-distribution observation command and WU-PR-08's three independence-basis nodes run
once per module, at the head, under closed rails; every PASS-path case feeds those real outputs
through the writer's seams, so the committed record is checked against the real tool. Refusal
cases use the real command where the refusal has a real input (open rails), and the seams only
for the writer's own checks downstream of a real failure class. No case writes the repository:
a written record goes to a temporary path.
"""
from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys

import pytest

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS
from tools.evidence import generate_hde_epic043_ferm009_observation_report as writer
from tools.score_distribution import score_distribution as tool

ACTOR = "test actor"
RECORD = writer.OUT_REL
ROOT = writer.ROOT
RUN_KEYS = set(writer.RUN_FIELDS)
# Every key the writer renders matches one of these.
KEY_PATTERNS = tuple(re.compile(pattern) for pattern in (
    r"schema|epic_id|task_id|requirement_id|work_unit_id|status|limit|outcome",
    r"run\.(time_utc|actor|python)",
    r"input\.[A-Za-z0-9_./-]+\.(sha256|size_bytes)",
    r"tested_inputs\.(count|sha256)|tested_state",
    r"command(\.[a-z0-9_]+)?",
    r"release\.(release_id|version|config_id|manifest_sha256)",
    r"invariant\.[a-z0-9_]+",
    r"population\.(path|sha256|pinned_sha256|people|pairs|synthetic|floor)",
    r"independence\.(seed|reference_path|reference_seed|shared_identities|statement|basis\.[1-3])",
    r"report\.(category_order|category_results|not_restated)",
    r"mix\.[a-z]+\.(Cool|Open|Warm|Glow)\.(count|share)",
    r"distinct_bands_per_pair\.([1-4]|definition)",
    r"tolerance\.(against|target_mix_percent|points|categories_beyond_tolerance)",
    r"tolerance\.[a-z]+\.(Cool|Open|Warm|Glow)\.(share_points|difference_points|beyond_tolerance)",
    r"tolerance\.[a-z]+\.result",
    r"limitation\.[1-9]",
))
FORBIDDEN_IMPORT_ROOTS = ("engine.db", "socket", "ssl", "http", "urllib", "requests", "psycopg")
FORBIDDEN_NAMES = ("DBAccess", "for_current_env", "run_stored", "run_observation", "score_pairs", "shell=True")


def _closed(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.chdir(ROOT)


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    _closed(monkeypatch)


@pytest.fixture(scope="module")
def real_tool():
    """The real observation command at the head (about two minutes)."""

    with pytest.MonkeyPatch.context() as monkeypatch:
        _closed(monkeypatch)
        return writer.run_tool()


@pytest.fixture(scope="module")
def real_basis():
    """WU-PR-08's three basis nodes at the head (about six seconds)."""

    with pytest.MonkeyPatch.context() as monkeypatch:
        _closed(monkeypatch)
        return writer.run_basis()


@pytest.fixture
def real_seams(monkeypatch, real_tool, real_basis):
    monkeypatch.setattr(writer, "run_tool", lambda: real_tool)
    monkeypatch.setattr(writer, "run_basis", lambda: real_basis)


@pytest.fixture
def tmp_record(tmp_path, monkeypatch):
    out = tmp_path / "ferm009_observation_report.txt"
    monkeypatch.setattr(writer, "out_path", lambda: out)
    return out


def _git_status() -> bytes:
    return subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=ROOT,
                          capture_output=True, check=True).stdout


def _record(data: bytes) -> dict[str, str]:
    return dict(writer.parse_record(data))


def _refused(code: str):
    return pytest.raises(SystemExit, match=f"^{re.escape(code)}$")


# --- W-1 to W-4: the PASS path over the real tool ---------------------------------------------------

def test_w1_the_committed_record_passes_check_over_the_real_tool(real_seams, capsys) -> None:
    before = _git_status()
    assert writer.main(["--check"]) == 0
    assert capsys.readouterr().out == "ferm009 observation report check ok\n"
    assert _git_status() == before


def test_w2_write_then_check_twice_is_byte_stable_and_matches_the_committed_record(real_seams, tmp_record) -> None:
    before = _git_status()
    assert writer.main(["--actor", ACTOR]) == 0
    written = tmp_record.read_bytes()
    assert writer.main(["--check"]) == 0
    assert writer.main(["--check"]) == 0
    assert tmp_record.read_bytes() == written
    committed = (ROOT / RECORD).read_bytes()
    strip = lambda data: [(k, v) for k, v in writer.parse_record(data) if k not in RUN_KEYS]  # noqa: E731
    assert strip(written) == strip(committed)
    assert _git_status() == before


def test_w3_every_r17_field_equals_the_real_report(real_tool) -> None:
    code, out, err = real_tool
    assert (code, err) == (0, b"")
    report = json.loads(out)
    record = _record((ROOT / RECORD).read_bytes())
    manifest_sha256 = writer.sha256_hex((ROOT / writer.MANIFEST_REL).read_bytes())
    # The admitted release (acceptance item 4).
    assert record["release.release_id"] == report["release"]["release_id"] == manifest_sha256
    assert record["release.version"] == report["release"]["version"]
    assert record["release.config_id"] == report["release"]["config_id"]
    # The population, its hash and count (acceptance item 2).
    population = report["population"]
    assert record["population.path"] == population["path"] == writer.POPULATION_REL
    assert record["population.sha256"] == population["population_sha256"] == tool.OBSERVATION_POPULATION_SHA256
    assert int(record["population.people"]) == population["people"] >= writer.POPULATION_FLOOR
    assert int(record["population.pairs"]) == population["pairs"]
    assert record["population.synthetic"] == "true" and population["synthetic"] is True
    # The realized band mix per category.
    categories = list(report["band_counts"]["per_category"])
    assert json.loads(record["report.category_order"]) == categories
    for scope in ("overall", *categories):
        counts = report["band_counts"]["overall" if scope == "overall" else "per_category"]
        shares = report["band_shares"]["overall" if scope == "overall" else "per_category"]
        counts = counts if scope == "overall" else counts[scope]
        shares = shares if scope == "overall" else shares[scope]
        for band in tool.BANDS:
            assert int(record[f"mix.{scope}.{band}.count"]) == counts[band]
            assert record[f"mix.{scope}.{band}.share"] == shares[band]
    # The distinct bands per pair.
    for k, value in report["band_variety_per_pair"].items():
        assert int(record[f"distinct_bands_per_pair.{k}"]) == value
    # Each category's tolerance result against the target within 5 points.
    comparison = report["comparison"]
    assert json.loads(record["tolerance.target_mix_percent"]) == tool.TARGET_MIX_PERCENT
    assert int(record["tolerance.points"]) == tool.TOLERANCE_POINTS == 5
    beyond = comparison["categories_beyond_tolerance"]
    assert json.loads(record["tolerance.categories_beyond_tolerance"]) == beyond
    for category, rows in comparison["per_category"].items():
        for band in tool.BANDS:
            assert record[f"tolerance.{category}.{band}.share_points"] == rows[band]["share_points"]
            assert record[f"tolerance.{category}.{band}.difference_points"] == rows[band]["difference_points"]
            assert record[f"tolerance.{category}.{band}.beyond_tolerance"] == str(rows[band]["beyond_tolerance"]).lower()
        assert record[f"tolerance.{category}.result"] == ("beyond" if category in beyond else "within")
    # The limit, in words; the command provenance; the invariants; completion.
    assert record["limit"] == report["limit"] == tool.OBSERVATION_LIMIT
    assert record["command.stdout_sha256"] == writer.sha256_hex(out)
    assert record["command.exit_code"] == "0"
    assert all(record[key] == "true" for key in record if key.startswith("invariant."))
    assert record["status"] == "COMPLETE"


def test_w4_the_record_holds_no_per_person_or_per_pair_value() -> None:
    text = (ROOT / RECORD).read_text(encoding="utf-8")
    ids = set()
    for rel in (writer.POPULATION_REL, writer.CORPUS_REL):
        ids |= {person["id"] for person in json.loads((ROOT / rel).read_bytes())["people"]}
    assert not [person_id for person_id in ids if person_id in text]
    assert "gates" not in text
    for key, _value in writer.parse_record(text.encode("utf-8")):
        assert any(pattern.fullmatch(key) for pattern in KEY_PATTERNS), key


# --- W-5: a stale or edited record ------------------------------------------------------------------

def test_w5_check_refuses_a_missing_record(real_seams, tmp_record) -> None:
    with _refused(f"DRIFT:{RECORD}:missing"):
        writer.main(["--check"])


def test_w5_check_refuses_an_edited_line(real_seams, tmp_record) -> None:
    lines = (ROOT / RECORD).read_text(encoding="utf-8").splitlines(keepends=True)
    edited = [("population.people: 1999\n" if line.startswith("population.people: ") else line) for line in lines]
    tmp_record.write_text("".join(edited), encoding="utf-8")
    with _refused(f"DRIFT:{RECORD}:population.people"):
        writer.main(["--check"])


def test_w5_check_refuses_a_changed_tested_input_before_the_tool_runs(tmp_record, monkeypatch) -> None:
    tmp_record.write_bytes((ROOT / RECORD).read_bytes())
    original = writer.read_input

    def read_input(rel: str) -> bytes:
        data = original(rel)
        return data + b"# changed\n" if rel == writer.TOOL_REL else data

    monkeypatch.setattr(writer, "read_input", read_input)
    monkeypatch.setattr(writer, "run_tool", lambda: pytest.fail("the tool ran before the tested inputs"))
    with _refused(f"DRIFT:{RECORD}:input.{writer.TOOL_REL}.sha256"):
        writer.main(["--check"])


def test_w5_check_refuses_a_malformed_run_field(real_seams, tmp_record) -> None:
    lines = (ROOT / RECORD).read_text(encoding="utf-8").splitlines(keepends=True)
    edited = [("run.time_utc: yesterday\n" if line.startswith("run.time_utc: ") else line) for line in lines]
    tmp_record.write_text("".join(edited), encoding="utf-8")
    with _refused(f"DRIFT:{RECORD}:run.time_utc"):
        writer.main(["--check"])


# --- W-6: open rails, refused by the tool's own token -------------------------------------------------

@pytest.mark.parametrize("key,value,pin", [("SAFE_MODE", "0", "('SAFE_MODE', '1')"),
                                           ("ALLOW_NETWORK", "1", "('ALLOW_NETWORK', '0')")])
def test_w6_open_rails_are_refused_by_the_tools_own_token(tmp_record, monkeypatch, key, value, pin) -> None:
    monkeypatch.setenv(key, value)
    with _refused(f"{writer.TOOL_REFUSED}:RAILS_CLOSED_REQUIRED:[{pin}]"):
        writer.main(["--actor", ACTOR])
    assert not tmp_record.exists()


def test_w6_open_rails_are_refused_through_the_command_line() -> None:
    before = _git_status()
    environ = {key: os.environ[key] for key in ("PATH", "HOME") if key in os.environ}
    environ.update({**DETERMINISM_ENV_PINS, "SAFE_MODE": "0", "PYTHONDONTWRITEBYTECODE": "1"})
    proc = subprocess.run([sys.executable, writer.GENERATOR_REL, "--actor", ACTOR], cwd=ROOT, env=environ,
                          capture_output=True, timeout=600)
    assert proc.returncode == 1 and proc.stdout == b""
    assert proc.stderr == f"{writer.TOOL_REFUSED}:RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]\n".encode()
    assert _git_status() == before


# --- W-7: the writer's own preconditions --------------------------------------------------------------

def test_w7_another_working_directory_is_refused(tmp_record, monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    with _refused(writer.WORKING_DIRECTORY_INVALID):
        writer.main(["--actor", ACTOR])
    assert not tmp_record.exists()


def test_w7_a_temporary_directory_inside_the_repository_is_refused(tmp_record, monkeypatch) -> None:
    monkeypatch.setattr(writer.tempfile, "tempdir", str(ROOT / "tmp-inside-the-repository"))
    with _refused(writer.TEMP_DIRECTORY_INSIDE_REPOSITORY):
        writer.main(["--actor", ACTOR])
    assert not tmp_record.exists()


@pytest.mark.parametrize("actor", ["", " padded", "line\nbreak", "x" * 201])
def test_w7_an_invalid_actor_is_refused(tmp_record, actor) -> None:
    with _refused(writer.INVALID_ACTOR):
        writer.main(["--actor", actor])
    assert not tmp_record.exists()


# --- W-8: no database, network or other secret reaches the writer or its children ---------------------

def test_w8_the_child_environment_passes_only_the_listed_variables(monkeypatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgres://example.invalid/db")
    monkeypatch.setenv("GH_TOKEN", "token")
    monkeypatch.setenv("HTTPS_PROXY", "http://proxy.invalid:3128")
    monkeypatch.setenv("PYTHONPATH", "/elsewhere")
    environ = writer.child_env()
    allowed = {*writer.PASSED_ENVIRONMENT, *DETERMINISM_ENV_PINS, *writer.CHILD_FIXED}
    assert set(environ) <= allowed
    assert {"DATABASE_URL", "GH_TOKEN", "HTTPS_PROXY", "PYTHONPATH"}.isdisjoint(environ)
    assert all(environ[key] == os.environ[key] for key in DETERMINISM_ENV_PINS)
    assert environ["PYTHONDONTWRITEBYTECODE"] == "1"


def test_w8_the_writer_imports_no_database_or_network_module_and_uses_no_shell() -> None:
    source = (ROOT / writer.GENERATOR_REL).read_text(encoding="utf-8")
    imported = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module or "")
    assert not [name for name in imported
                if any(name == root or name.startswith(root + ".") for root in FORBIDDEN_IMPORT_ROOTS)]
    assert not [name for name in FORBIDDEN_NAMES if name in source]


# --- N-1 to N-4: one control per writer check with a real input ----------------------------------------

@pytest.mark.parametrize("result,code", [((1, b"", b"Traceback (most recent call last):\n"), "1"),
                                          ((0, b"{}\n", b"warning\n"), "0:stderr")])
def test_n1_a_tool_failure_is_refused_and_nothing_is_written(tmp_record, monkeypatch, real_basis, result,
                                                             code) -> None:
    monkeypatch.setattr(writer, "run_tool", lambda: result)
    monkeypatch.setattr(writer, "run_basis", lambda: real_basis)
    with _refused(f"{writer.TOOL_FAILED}:{code}"):
        writer.main(["--actor", ACTOR])
    assert not tmp_record.exists()


def test_n2_a_tool_timeout_is_refused(tmp_record, monkeypatch) -> None:
    def timed_out(*args, **kwargs):
        raise subprocess.TimeoutExpired(args[0], writer.TOOL_TIMEOUT_SECONDS)

    monkeypatch.setattr(writer.subprocess, "run", timed_out)
    with _refused(f"{writer.TOOL_FAILED}:timeout"):
        writer.main(["--actor", ACTOR])
    assert not tmp_record.exists()


@pytest.mark.parametrize("index,outcome", [(2, "failure"), (0, None)])
def test_n3_a_basis_node_not_passed_is_refused(tmp_record, monkeypatch, real_tool, index, outcome) -> None:
    outcomes = {node: "passed" for node in writer.BASIS_NODES}
    if outcome is None:
        del outcomes[writer.BASIS_NODES[index]]
    else:
        outcomes[writer.BASIS_NODES[index]] = outcome
    monkeypatch.setattr(writer, "run_tool", lambda: real_tool)
    monkeypatch.setattr(writer, "run_basis", lambda: (1, outcomes))
    with _refused(f"{writer.INDEPENDENCE_BASIS_NOT_PASSED}:{writer.BASIS_NODES[index]}"):
        writer.main(["--actor", ACTOR])
    assert not tmp_record.exists()


def test_n4_a_failing_basis_exit_with_every_node_passed_is_refused(tmp_record, monkeypatch, real_tool) -> None:
    monkeypatch.setattr(writer, "run_tool", lambda: real_tool)
    monkeypatch.setattr(writer, "run_basis", lambda: (1, {node: "passed" for node in writer.BASIS_NODES}))
    with _refused(f"{writer.INDEPENDENCE_BASIS_RUN_FAILED}:1"):
        writer.main(["--actor", ACTOR])
    assert not tmp_record.exists()
