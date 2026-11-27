#!/usr/bin/env python3
"""HDE-FERM009 observation report (HDE-EPIC043 WU-PR-14; R-17).

The writer records one governed aggregate record,
``audit/qa/hde-epic043/pr-14/ferm009_observation_report.txt``: the Magic10 v2
recalibration observation over the governed synthetic observation population,
scored by the score-distribution utility against the admitted release.

* The utility runs as its own command line, ``python
  tools/score_distribution/score_distribution.py observation``, in a subprocess
  from the repository root, with a fixed argument list and no shell.  The record
  carries the command, its environment pins, its exit code and the SHA-256 of its
  stdout.  The utility owns scoring and its preconditions: the caller's rail
  values are passed to it unchanged, so open rails are refused by the utility's
  own token, which the writer passes through.
* The record states every field of R-17 and of the FERM009 addendum's R-6 from
  the utility's report: the admitted release, the population with its hash and
  count, the realized band mix per category, the distinct bands per pair, each
  category's tolerance result against 30 / 35 / 25 / 10 within 5 points, and the
  limit, in words, that a synthetic population cannot show how real people fall.
* The population's independence from the reference corpus is recorded from the
  two committed files (their seeds and the count of shared identities) and from
  WU-PR-08's three owner-test nodes, which the writer runs at the head.
* Aggregates only: no person, gate, pair or per-pair value enters the record.
* Outcome-neutral: a category beyond tolerance is recorded as such.  It is a
  recalibration case for the Product Owner's release decision, never a runtime
  adjustment, and it does not fail the record.

The record names its tested state by the SHA-256 and size of each tested input and
one digest over them; it carries no git state.  It also names the responsible
actor, the run time and the interpreter.  ``--check`` compares the tested inputs
first, then re-runs the utility and the basis, re-derives every line and compares
the bytes; it checks the three run fields for shape only, so it is byte-stable and
writes nothing.  A failing check is a named refusal and nothing is written.  It
runs only from the repository root.  No vendor, network or database call is made
by the writer.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS  # noqa: E402
from tools.score_distribution import score_distribution as tool  # noqa: E402

OUT_REL = "audit/qa/hde-epic043/pr-14/ferm009_observation_report.txt"
SCHEMA = "hde_epic043_ferm009_observation_report.v1"
GENERATOR_REL = "tools/evidence/generate_hde_epic043_ferm009_observation_report.py"

MANIFEST_REL = "catalog/manifest.json"
TOOL_REL = "tools/score_distribution/score_distribution.py"
POPULATION_REL = "tools/score_distribution/observation_population_v1.json"
CORPUS_REL = "tools/score_distribution/reference_corpus_v1.json"
POPULATION_GENERATOR_REL = "tools/score_distribution/generate_observation_population.py"
TOOL_TEST_REL = "tests/tools/test_score_distribution.py"

# The tested inputs, in record order (plan v1.1 section 6.6).
TESTED_INPUTS = (
    MANIFEST_REL,
    TOOL_REL,
    POPULATION_REL,
    CORPUS_REL,
    POPULATION_GENERATOR_REL,
    TOOL_TEST_REL,
    "engine/runtime/determinism_env.py",
    "engine/db/__init__.py",
    "engine/db/errors.py",
    "pytest.ini",
    "tests/conftest.py",
    GENERATOR_REL,
)

TOOL_COMMAND = (TOOL_REL, "observation")
# WU-PR-08's owner-test nodes for the population's independence: the pinned bytes are the
# recipe's output for its own seed, the corpus is the recipe's output for the corpus seed, and
# the two share no seed, identity or birth instant and the population is not a subset.
BASIS_NODES = (
    f"{TOOL_TEST_REL}::test_observation_population_regenerates_to_the_pinned_bytes",
    f"{TOOL_TEST_REL}::test_generator_follows_the_reference_corpus_recipe",
    f"{TOOL_TEST_REL}::test_observation_population_is_independent_of_the_corpus",
)
# The utility's report keys (score_distribution_report.v1 with the observation limit).
REPORT_KEYS = frozenset({
    "schema", "mode", "read_only", "release", "population", "comparison", "category_results", "band_counts",
    "band_shares", "band_variety_per_pair", "score_percentiles", "zero_share", "tie_share",
    "channels_formed_per_pair", "limit",
})
NOT_RESTATED = ("score_percentiles", "zero_share", "tie_share", "channels_formed_per_pair")
POPULATION_FLOOR = 400  # the FERM009 addendum, R-1
PASSED_ENVIRONMENT = ("PATH", "HOME", "APP_ENV")
CHILD_FIXED = {"PYTHONDONTWRITEBYTECODE": "1"}

INDEPENDENCE_STATEMENT = ("independent of the reference corpus: its own seed, not a subset, no shared identity "
                          "or birth instant (FERM009 addendum R-2)")
VARIETY_DEFINITION = "the number of pairs whose ten category results have k distinct bands"
OUTCOME = ("A category beyond tolerance is a recalibration case for the Product Owner's release decision, never a "
           "runtime adjustment; it does not fail this record. This record is not a QA verdict.")
LIMITATIONS = (
    "no live run: no production, vendor, database or network access",
    "interpreter: run.python locally; hosted CI's interpreter may differ",
    "evidence of the tested inputs named above only; a later state must pass --check",
    "birth-instant independence rests on WU-PR-08's owner test, run here (independence.basis)",
    "establishes no QA verdict, acceptance, PF09 movement, Ops, deployment or closure",
)

RUN_FIELDS = ("run.time_utc", "run.actor", "run.python")
HEADER_LENGTH = 5
_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
_PYTHON = re.compile(r"\d+\.\d+\.\d+")
TOOL_TIMEOUT_SECONDS = 1800
BASIS_TIMEOUT_SECONDS = 1800

_PREFIX = "FERM009_OBSERVATION_REPORT_"
WORKING_DIRECTORY_INVALID = _PREFIX + "WORKING_DIRECTORY_INVALID"
TEMP_DIRECTORY_INSIDE_REPOSITORY = _PREFIX + "TEMP_DIRECTORY_INSIDE_REPOSITORY"
INVALID_ACTOR = _PREFIX + "INVALID_ACTOR"
INPUT_UNREADABLE = _PREFIX + "INPUT_UNREADABLE"
TOOL_REFUSED = _PREFIX + "TOOL_REFUSED"
TOOL_FAILED = _PREFIX + "TOOL_FAILED"
REPORT_INVARIANT_FAILED = _PREFIX + "REPORT_INVARIANT_FAILED"
INDEPENDENCE_BASIS_NOT_PASSED = _PREFIX + "INDEPENDENCE_BASIS_NOT_PASSED"
INDEPENDENCE_BASIS_RUN_FAILED = _PREFIX + "INDEPENDENCE_BASIS_RUN_FAILED"
RECORD_INVALID = _PREFIX + "RECORD_INVALID"


class ObservationReportRefusal(RuntimeError):
    """A named refusal: no record is written."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


# --- small helpers -----------------------------------------------------------------------------

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(value: object) -> str:
    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def valid_actor(actor: str) -> bool:
    """The HDE-SEPA007.5 writer's actor rule."""

    return 0 < len(actor) <= 200 and actor.isprintable() and actor == actor.strip()


def render_value(value: object, key: str) -> str:
    """One report value as record text; bools as true/false. Any other type breaks the report shape."""

    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, str)):
        return str(value)
    raise ObservationReportRefusal(f"{REPORT_INVARIANT_FAILED}:report_shape:{key}")


# --- seams (the owner test replaces these) -------------------------------------------------------

def out_path() -> Path:
    return ROOT / OUT_REL


def read_input(rel: str) -> bytes:
    try:
        return (ROOT / rel).read_bytes()
    except OSError:
        raise ObservationReportRefusal(f"{INPUT_UNREADABLE}:{rel}") from None


def child_env() -> dict[str, str]:
    """The child's whole environment: PATH, HOME and APP_ENV when set, the caller's own rail values
    unchanged (never forced, so the utility refuses open rails itself), and no bytecode writes.
    Nothing else reaches the child: no database URL, token, proxy or PYTHONPATH."""

    environ = {key: os.environ[key] for key in (*PASSED_ENVIRONMENT, *DETERMINISM_ENV_PINS) if key in os.environ}
    environ.update(CHILD_FIXED)
    return environ


def run_tool() -> tuple[int, bytes, bytes]:
    """The utility's observation command; returns its exit code, stdout and stderr."""

    try:
        proc = subprocess.run([sys.executable, *TOOL_COMMAND], cwd=ROOT, env=child_env(), capture_output=True,
                              timeout=TOOL_TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        raise ObservationReportRefusal(f"{TOOL_FAILED}:timeout") from None
    return proc.returncode, proc.stdout, proc.stderr


def run_basis() -> tuple[int, dict[str, str]]:
    """WU-PR-08's basis nodes in one pytest process; returns its exit code and each node's outcome."""

    with tempfile.TemporaryDirectory(prefix="hde_epic043_pr14_basis_") as tmp:
        here = Path(tmp).resolve()
        report = here / "basis.xml"
        command = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp", str(here / "basetemp"),
                   "--junitxml", str(report), *BASIS_NODES]
        try:
            proc = subprocess.run(command, cwd=ROOT, env=child_env(), capture_output=True,
                                  timeout=BASIS_TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            raise ObservationReportRefusal(f"{INDEPENDENCE_BASIS_RUN_FAILED}:timeout") from None
        if not report.is_file():
            raise ObservationReportRefusal(f"{INDEPENDENCE_BASIS_RUN_FAILED}:{proc.returncode}:no_report")
        try:
            root = ET.parse(report).getroot()
        except ET.ParseError:
            raise ObservationReportRefusal(
                f"{INDEPENDENCE_BASIS_RUN_FAILED}:{proc.returncode}:report_unreadable") from None
        outcomes: dict[str, str] = {}
        for case in root.iter("testcase"):
            node = case.get("classname", "").replace(".", "/") + ".py::" + case.get("name", "").split("[", 1)[0]
            outcome = next((child.tag for child in case if child.tag in ("failure", "error", "skipped")), "passed")
            if outcomes.get(node, "passed") == "passed":
                outcomes[node] = outcome
        return proc.returncode, outcomes


# --- preconditions --------------------------------------------------------------------------------

def preconditions() -> None:
    try:
        here = Path.cwd().resolve()
    except OSError:
        raise ObservationReportRefusal(WORKING_DIRECTORY_INVALID) from None
    root = ROOT.resolve()
    if here != root:
        raise ObservationReportRefusal(WORKING_DIRECTORY_INVALID)
    temp = Path(tempfile.gettempdir()).resolve()
    if temp == root or root in temp.parents:
        raise ObservationReportRefusal(TEMP_DIRECTORY_INSIDE_REPOSITORY)


# --- the record -------------------------------------------------------------------------------------

def tested_input_lines() -> list[tuple[str, str]]:
    lines: list[tuple[str, str]] = []
    digests = []
    for rel in TESTED_INPUTS:
        data = read_input(rel)
        digests.append(f"{rel} {sha256_hex(data)} {len(data)}")
        lines += [(f"input.{rel}.sha256", sha256_hex(data)), (f"input.{rel}.size_bytes", str(len(data)))]
    lines += [
        ("tested_inputs.count", str(len(TESTED_INPUTS))),
        ("tested_inputs.sha256", sha256_hex(("\n".join(digests) + "\n").encode("utf-8"))),
        ("tested_state", "the inputs above; this record carries no git state, and the PR result maps "
                         "tested_inputs.sha256 to the tested head"),
    ]
    return lines


def tool_report() -> tuple[int, bytes, bytes, dict[str, Any]]:
    code, out, err = run_tool()
    if code == tool.REFUSAL_EXIT_CODE:
        raise ObservationReportRefusal(f"{TOOL_REFUSED}:{err.decode('utf-8', 'replace').strip()}")
    if code != 0:
        raise ObservationReportRefusal(f"{TOOL_FAILED}:{code}")
    if err:
        raise ObservationReportRefusal(f"{TOOL_FAILED}:0:stderr")
    try:
        report = json.loads(out.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise ObservationReportRefusal(f"{REPORT_INVARIANT_FAILED}:report_json") from None
    if not isinstance(report, dict) or set(report) != REPORT_KEYS:
        raise ObservationReportRefusal(f"{REPORT_INVARIANT_FAILED}:report_shape")
    return code, out, err, report


def shared_identities() -> tuple[int, int, int]:
    """The two committed populations' seeds and the count of person IDs they share."""

    try:
        population = json.loads(read_input(POPULATION_REL).decode("utf-8"))
        corpus = json.loads(read_input(CORPUS_REL).decode("utf-8"))
        seeds = (population["provenance"]["seed"], corpus["provenance"]["seed"])
        shared = len({p["id"] for p in population["people"]} & {p["id"] for p in corpus["people"]})
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError):
        raise ObservationReportRefusal(f"{REPORT_INVARIANT_FAILED}:independence_inputs") from None
    return seeds[0], seeds[1], shared


def invariant_results(report: Mapping[str, Any], shared: int) -> list[tuple[str, bool]]:
    population, release, comparison = report["population"], report["release"], report["comparison"]
    return [
        ("report_shape", report["schema"] == tool.REPORT_SCHEMA and report["mode"] == "observation"
         and report["read_only"] is True),
        ("release_id_equals_manifest_sha256", release.get("release_id") == sha256_hex(read_input(MANIFEST_REL))),
        ("population_path_pinned", population.get("path") == POPULATION_REL),
        ("population_sha256_equals_pin", population.get("population_sha256") == tool.OBSERVATION_POPULATION_SHA256
         == sha256_hex(read_input(POPULATION_REL))),
        ("population_at_least_400", type(population.get("people")) is int and population["people"] >= POPULATION_FLOOR),
        ("population_synthetic", population.get("synthetic") is True),
        ("comparison_against_target", comparison.get("against") == "target"
         and comparison.get("target_mix_percent") == dict(tool.TARGET_MIX_PERCENT)
         and comparison.get("tolerance_points") == tool.TOLERANCE_POINTS),
        ("limit_verbatim", report["limit"] == tool.OBSERVATION_LIMIT),
        ("no_shared_identity", shared == 0),
    ]


def basis_lines() -> list[tuple[str, str]]:
    code, outcomes = run_basis()
    for node in BASIS_NODES:
        if outcomes.get(node) != "passed":
            raise ObservationReportRefusal(f"{INDEPENDENCE_BASIS_NOT_PASSED}:{node}")
    if code != 0:
        raise ObservationReportRefusal(f"{INDEPENDENCE_BASIS_RUN_FAILED}:{code}")
    return [(f"independence.basis.{number}", f"{node} passed") for number, node in enumerate(BASIS_NODES, 1)]


def report_lines(report: Mapping[str, Any]) -> list[tuple[str, str]]:
    """The R-17 fields, from the utility's report, in its own (canonical JSON) order."""

    counts, shares, comparison = report["band_counts"], report["band_shares"], report["comparison"]
    categories = list(counts["per_category"])
    lines: list[tuple[str, str]] = [
        ("report.category_order", compact(categories)),
        ("report.category_results", render_value(report["category_results"], "category_results")),
    ]
    scopes = [("overall", counts["overall"], shares["overall"])]
    scopes += [(category, counts["per_category"][category], shares["per_category"][category]) for category in categories]
    for scope, scope_counts, scope_shares in scopes:
        for band in tool.BANDS:
            lines += [(f"mix.{scope}.{band}.count", render_value(scope_counts[band], "band_counts")),
                      (f"mix.{scope}.{band}.share", render_value(scope_shares[band], "band_shares"))]
    variety = report["band_variety_per_pair"]
    lines += [(f"distinct_bands_per_pair.{k}", render_value(variety[k], "band_variety_per_pair"))
              for k in sorted(variety, key=int)]
    lines.append(("distinct_bands_per_pair.definition", VARIETY_DEFINITION))
    beyond = list(comparison["categories_beyond_tolerance"])
    lines += [
        ("tolerance.against", render_value(comparison["against"], "comparison")),
        ("tolerance.target_mix_percent", compact(dict(comparison["target_mix_percent"]))),
        ("tolerance.points", render_value(comparison["tolerance_points"], "comparison")),
    ]
    for band in tool.BANDS:
        row = comparison["overall"][band]
        lines += [(f"tolerance.overall.{band}.share_points", render_value(row["share_points"], "comparison")),
                  (f"tolerance.overall.{band}.difference_points", render_value(row["difference_points"], "comparison"))]
    for category in comparison["per_category"]:
        rows = comparison["per_category"][category]
        for band in tool.BANDS:
            for key in ("share_points", "difference_points", "beyond_tolerance"):
                lines.append((f"tolerance.{category}.{band}.{key}", render_value(rows[band][key], "comparison")))
        lines.append((f"tolerance.{category}.result", "beyond" if category in beyond else "within"))
    lines.append(("tolerance.categories_beyond_tolerance", compact(beyond)))
    return lines


def collect() -> list[tuple[str, str]]:
    """Every line of the record after the run fields, in record order."""

    lines = tested_input_lines()
    code, out, err, report = tool_report()
    seed, reference_seed, shared = shared_identities()
    try:
        invariants = invariant_results(report, shared)
        r17_lines = report_lines(report)
    except (KeyError, TypeError, AttributeError, ValueError):
        raise ObservationReportRefusal(f"{REPORT_INVARIANT_FAILED}:report_shape") from None
    failed = [key for key, held in invariants if not held]
    if failed:
        raise ObservationReportRefusal(f"{REPORT_INVARIANT_FAILED}:{failed[0]}")
    independence = basis_lines()
    release, population = report["release"], report["population"]
    lines += [
        ("command", "python " + " ".join(TOOL_COMMAND)),
        ("command.working_directory", "the repository root"),
        ("command.environment", compact({**DETERMINISM_ENV_PINS, **CHILD_FIXED})),
        ("command.environment_passed", ", ".join(PASSED_ENVIRONMENT) + " when set, by name only, with no value "
                                                                       "recorded"),
        ("command.environment_excluded", "every other variable, including database URLs, tokens, proxies and "
                                         "PYTHONPATH"),
        ("command.exit_code", str(code)),
        ("command.stdout_sha256", sha256_hex(out)),
        ("command.stdout_size_bytes", str(len(out))),
        ("command.stderr_size_bytes", str(len(err))),
        ("command.interpreter", "run.python"),
        ("release.release_id", render_value(release["release_id"], "release")),
        ("release.version", render_value(release["version"], "release")),
        ("release.config_id", render_value(release["config_id"], "release")),
        ("release.manifest_sha256", sha256_hex(read_input(MANIFEST_REL))),
    ]
    lines += [(f"invariant.{key}", "true") for key, _held in invariants]
    lines += [
        ("population.path", render_value(population["path"], "population")),
        ("population.sha256", render_value(population["population_sha256"], "population")),
        ("population.pinned_sha256", tool.OBSERVATION_POPULATION_SHA256),
        ("population.people", render_value(population["people"], "population")),
        ("population.pairs", render_value(population["pairs"], "population")),
        ("population.synthetic", render_value(population["synthetic"], "population")),
        ("population.floor", str(POPULATION_FLOOR)),
        ("independence.seed", str(seed)),
        ("independence.reference_path", CORPUS_REL),
        ("independence.reference_seed", str(reference_seed)),
        ("independence.shared_identities", str(shared)),
        *independence,
        ("independence.statement", INDEPENDENCE_STATEMENT),
    ]
    lines += r17_lines
    lines += [
        ("report.not_restated", ", ".join(NOT_RESTATED) + "; bound by command.stdout_sha256"),
        ("limit", render_value(report["limit"], "limit")),
        ("outcome", OUTCOME),
        ("command.write", f"python {GENERATOR_REL} --actor <actor>"),
        ("command.check", f"python {GENERATOR_REL} --check"),
    ]
    lines += [(f"limitation.{number}", text) for number, text in enumerate(LIMITATIONS, 1)]
    lines.append(("status", "COMPLETE"))
    return lines


def header(run: Mapping[str, str]) -> list[tuple[str, str]]:
    return [
        ("schema", SCHEMA),
        ("epic_id", "HDE-EPIC043"),
        ("task_id", "HDE-FERM009"),
        ("requirement_id", "R-17"),
        ("work_unit_id", "WU-PR-14"),
        *((key, run[key]) for key in RUN_FIELDS),
    ]


def render(lines: Sequence[tuple[str, str]]) -> bytes:
    keys = [key for key, _value in lines]
    if len(keys) != len(set(keys)) or keys[0] != "schema" or keys[-1] != "status":
        raise ObservationReportRefusal(RECORD_INVALID)
    for key, value in lines:
        if (not isinstance(value, str) or not key or ": " in key
                or any(char in f"{key}{value}" for char in "\r\n")):
            raise ObservationReportRefusal(RECORD_INVALID)
    return "".join(f"{key}: {value}\n" for key, value in lines).encode("utf-8")


def parse_record(data: bytes) -> list[tuple[str, str]]:
    text = data.decode("utf-8")
    if not text.endswith("\n"):
        raise ValueError("record without a final LF")
    parsed = []
    for line in text.split("\n")[:-1]:
        key, separator, value = line.partition(": ")
        if not separator:
            raise ValueError("record line without a key")
        parsed.append((key, value))
    return parsed


def run_fields_problem(run: Mapping[str, str]) -> str | None:
    if _TIME.fullmatch(run.get("run.time_utc", "")) is None:
        return "run.time_utc"
    if not valid_actor(run.get("run.actor", "")):
        return "run.actor"
    if _PYTHON.fullmatch(run.get("run.python", "")) is None:
        return "run.python"
    return None


def write(actor: str) -> bytes:
    if not valid_actor(actor):
        raise ObservationReportRefusal(INVALID_ACTOR)
    preconditions()
    run = {
        "run.time_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "run.actor": actor,
        "run.python": platform.python_version(),
    }
    record = render([*header(run), *collect()])
    out = out_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(record)
    return record


def check() -> None:
    preconditions()
    out = out_path()
    if not out.is_file():
        raise SystemExit(f"DRIFT:{OUT_REL}:missing")
    stored = out.read_bytes()
    try:
        parsed = parse_record(stored)
    except (UnicodeDecodeError, ValueError):
        raise SystemExit(f"DRIFT:{OUT_REL}:layout") from None
    positions = [key for key, _ in parsed[HEADER_LENGTH:HEADER_LENGTH + len(RUN_FIELDS)]]
    run = {key: value for key, value in parsed if key in RUN_FIELDS}
    if positions != list(RUN_FIELDS) or len(run) != len(RUN_FIELDS):
        raise SystemExit(f"DRIFT:{OUT_REL}:run")
    problem = run_fields_problem(run)
    if problem:
        raise SystemExit(f"DRIFT:{OUT_REL}:{problem}")
    head = header(run)
    # The tested inputs are compared before the utility runs, so a stale record fails fast.
    for (want_key, want), (have_key, have) in zip([*head, *tested_input_lines()], parsed):
        if (want_key, want) != (have_key, have):
            raise SystemExit(f"DRIFT:{OUT_REL}:{want_key}")
    expected = [*head, *collect()]
    for (want_key, want), (have_key, have) in zip(expected, parsed):
        if (want_key, want) != (have_key, have):
            raise SystemExit(f"DRIFT:{OUT_REL}:{want_key}")
    if render(expected) != stored:
        raise SystemExit(f"DRIFT:{OUT_REL}:layout")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--actor", help="the responsible actor of this run; writes the record")
    mode.add_argument("--check", action="store_true",
                      help="compare the tested inputs, re-run the utility and the basis, re-derive every line and "
                           "compare the bytes; write nothing")
    args = parser.parse_args(argv)
    try:
        if args.check:
            check()
            print("ferm009 observation report check ok")
            return 0
        write(args.actor)
    except ObservationReportRefusal as exc:
        raise SystemExit(exc.code) from None
    print("ferm009 observation report written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
