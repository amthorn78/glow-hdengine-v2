#!/usr/bin/env python3
"""Magic-10 v2 proof family record on the candidate (HDE-EPIC043 WU-PR-13; HDE-DIST008.1).

The writer records one governed record,
``audit/qa/hde-epic043/pr-13/v2_proof_family_record.txt``: the v2 proof family run
at the head over the repository's own admitted release.

* Every item of the family's pinned index (``FAMILY_INDEX`` in
  ``tests/m10_v2/test_proof_family_index.py``, F-01 to F-28 with F-21b) is run by
  one ``pytest`` process over ``tests/m10_v2`` and the index's nodes outside it.
  Each item's passing cases and refused mutations are recorded with their
  outcome, its basis on the candidate and the release it ran against.
* The v2 goldens ``M10-G001`` to ``M10-G008`` are compared at the root in both
  pair orders.
* The fixture-bundle items stand on the candidate because the labelled fixture
  configuration equals the cut configuration except the thresholds binding, and
  the fixture thresholds equal the cut thresholds except the maxima; both facts
  are checked at every run.
* No module that holds a mutation case has a broad exception handler, so a
  mutation counts as refused only on a failed assertion or the product's own
  typed refusal, never on an unrelated crash (PF10 addendum 2.6 R-3).

The record names its tested state by the SHA-256 and size of each tested input and
one digest over them; it carries no git state, and the PR result maps that digest
to the attested head.  It also names the responsible actor, the run time and the
interpreter.  ``--check`` compares the tested inputs first, then re-runs the family
and re-derives every line and compares the bytes; it checks the three run fields
for shape only, so it is byte-stable and writes nothing.  A failing check is a
named refusal and nothing is written.  It runs only under the closed determinism
rails, with ``APP_ENV`` ``dev``, ``test`` or ``local``, from the repository root.
No vendor, network or database call is made.

The validation and the exact-source attestation of the attested head are not in
this record: the attestation is built from a head that contains the record, so
both are recorded in the unit's ``PR_IMPLEMENTATION_RESULT`` in
``amthorn78/glow-docs`` (C-13).
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import hashlib
import importlib
import json
import os
import platform
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.magic10_v2_loader import MAGIC10_V2_CONFIG_ID  # noqa: E402
from engine.config.registry_loader import (  # noqa: E402
    RegistryConfigError,
    _load_active_mechanics_bundle_from_root,
)
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env  # noqa: E402

OUT_REL = "audit/qa/hde-epic043/pr-13/v2_proof_family_record.txt"
SCHEMA = "hde_epic043_v2_proof_family_record.v1"
GENERATOR_REL = "tools/evidence/generate_hde_epic043_v2_proof_family_record.py"

MANIFEST_REL = "catalog/manifest.json"
CONFIG_REL = "catalog/magic10_mechanics_v2.json"
THRESHOLDS_REL = "math/thresholds.json"
FIXTURE_CONFIG_REL = "tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json"
FIXTURE_THRESHOLDS_REL = "tests/fixtures/magic10_v2/thresholds_v2.fixture.json"
GOLDENS_REL = "tests/fixtures/magic10/v2/goldens.json"
FAMILY_DIR = "tests/m10_v2"
INDEX_MODULE = "tests.m10_v2.test_proof_family_index"
INDEX_REL = "tests/m10_v2/test_proof_family_index.py"
# The two v2 result schemas whose release-member closure F-08 proves on the candidate.
RESULT_SCHEMA_RELS = ("schemas/magic10_compat_result_v2.schema.json", "schemas/magic10_result_v2.schema.json")
V2_RESULT_SCHEMA = "magic10_result.v2"
V2_COMPAT_SCHEMA = "magic10_compat_result.v2"
DEV_APP_ENVS = ("dev", "test", "local")
BASIS_ACTIVE = "active release"
CANDIDATE_DUE = "WU-PR-13"

# The tested inputs besides the family modules, in record order.  The family modules
# (every tests/m10_v2/*.py, ASCII-sorted) follow tests/conftest.py.
LEADING_INPUTS = (MANIFEST_REL, "pytest.ini", "tests/conftest.py")
TRAILING_INPUTS = (
    "tests/config/test_config_artifacts.py",
    "tests/config/helpers.py",
    "tests/support/pr04_fixtures.py",
    FIXTURE_CONFIG_REL,
    FIXTURE_THRESHOLDS_REL,
    GOLDENS_REL,
    "fixtures/charts/bob.json",
    "tools/config/artifacts.py",
    "tools/config/generate_config_artifacts.py",
    "tools/evidence/update_evidence_index.py",
    GENERATOR_REL,
)

# The family's own non-vacuity pin and its control (HDE-EPIC043 WU-PR-13).
NONVACUITY_PIN_NODES = (
    f"{INDEX_REL}::test_no_mutation_module_converts_an_arbitrary_exception",
    f"{INDEX_REL}::test_the_handler_pin_refuses_a_broad_handler",
)
BROAD_HANDLER_NAMES = frozenset({"Exception", "BaseException"})
# The two mutation cases that converted a crash into a refusal before WU-PR-13
# (PF10 addendum 2.6 R-3), and what refuses each one now.
NONVACUITY_CASES = (
    ("F-24", "tests/m10_v2/test_family_surface.py::test_f24_mutation_identity_in_the_pair_preimage_is_refused",
     "refused by the product's own typed refusal: evaluate_pair's fail-closed pair_key guard raises "
     "CompatBoundaryError(result_schema, detail=pair_key), and the case asserts that cause"),
    ("F-21", "tests/m10_v2/test_family_config_rejection.py::test_f21_mutation_unchecked_manifest_rows_is_refused",
     "refused by a genuine assertion: with the row-form, uniqueness and order rules dropped, the not-a-manifest-entry "
     "sub-case gives M10V2_CONFIGURATION_ROW_MISSING where M10V2_INVALID_MANIFEST_ROWS is required"),
)

# What each index basis means on the candidate.  {release_id}, {config_id} and
# {fixture_config_id} are filled at run time from the admitted root and the fixture.
RAN_AGAINST = {
    "active release": "the admitted root: release_id {release_id}, config_id {config_id}",
    "active release and fixture bundle": (
        "the admitted root: release_id {release_id}, config_id {config_id}; and the labelled fixture bundle: "
        "config_id {fixture_config_id}, a synthetic release_id, the fixture maxima"
    ),
    "fixture bundle": "the labelled fixture bundle: config_id {fixture_config_id}, a synthetic release_id, the fixture maxima",
    "temporary root": "a temporary root over the repository's catalog, math and schemas with the labelled fixtures",
    "static": "no release: static source analysis",
}
STANDS_BECAUSE = {
    "active release": "the cases admit the repository root, or compare the goldens at it",
    "active release and fixture bundle": (
        "the surface part admits the repository root; the fixture part's rule depends on neither the maxima nor the "
        "release identity"
    ),
    "fixture bundle": (
        "each item's rule depends on neither the maxima nor the release identity, and the fixture configuration "
        "equals the cut configuration except sources.thresholds.sha256 (checked below)"
    ),
    "temporary root": "loader rules over constructed roots; no release identity is involved",
    "static": "static analysis of the committed source",
}

LIMITATIONS = (
    "no live run: no production, vendor, database or network access",
    "interpreter: run.python locally; hosted CI's interpreter may differ",
    "evidence of the tested inputs named above only; a later state must pass --check (RK-11)",
    "the fixture-bundle items stand on the configuration equality checked here, not on a run over the cut maxima",
    "the validation and the exact-source attestation of the attested head are recorded in the unit's "
    "PR_IMPLEMENTATION_RESULT in amthorn78/glow-docs, not in this record (C-13)",
    "establishes no QA verdict, acceptance, PF09 movement, Ops, deployment or closure",
)
RUN_FIELDS = ("run.time_utc", "run.actor", "run.python")
_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
_PYTHON = re.compile(r"\d+\.\d+\.\d+")
FAMILY_TIMEOUT_SECONDS = 1800

_PREFIX = "V2_PROOF_FAMILY_RECORD_"
RAILS_NOT_CLOSED = _PREFIX + "RAILS_NOT_CLOSED"
APP_ENV_NOT_DEV = _PREFIX + "APP_ENV_NOT_DEV"
WORKING_DIRECTORY_INVALID = _PREFIX + "WORKING_DIRECTORY_INVALID"
TEMP_DIRECTORY_INSIDE_REPOSITORY = _PREFIX + "TEMP_DIRECTORY_INSIDE_REPOSITORY"
INVALID_ACTOR = _PREFIX + "INVALID_ACTOR"
INPUT_UNREADABLE = _PREFIX + "INPUT_UNREADABLE"
RELEASE_REFUSED = _PREFIX + "RELEASE_REFUSED"
NOT_ADMITTED_V2_PATH = _PREFIX + "NOT_ADMITTED_V2_PATH"
INDEX_INVALID = _PREFIX + "INDEX_INVALID"
FIXTURE_CONFIGURATION_DIVERGED = _PREFIX + "FIXTURE_CONFIGURATION_DIVERGED"
FIXTURE_THRESHOLDS_DIVERGED = _PREFIX + "FIXTURE_THRESHOLDS_DIVERGED"
FAMILY_RUN_FAILED = _PREFIX + "FAMILY_RUN_FAILED"
NODE_NOT_RUN = _PREFIX + "NODE_NOT_RUN"
ITEM_FAILED = _PREFIX + "ITEM_FAILED"
MUTATION_NOT_REFUSED = _PREFIX + "MUTATION_NOT_REFUSED"
FAMILY_CASE_NOT_PASSED = _PREFIX + "FAMILY_CASE_NOT_PASSED"
GOLDEN_MISMATCH = _PREFIX + "GOLDEN_MISMATCH"
BROAD_HANDLER = _PREFIX + "BROAD_HANDLER"
RECORD_INVALID = _PREFIX + "RECORD_INVALID"


class ProofFamilyRecordRefusal(RuntimeError):
    """A named refusal: no record is written."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class FamilyIndex:
    rows: tuple[Mapping[str, Any], ...]
    check: Callable[[Sequence[Mapping[str, Any]]], None]


@dataclass(frozen=True)
class FamilyCase:
    case_id: str  # path::name, with any [parameter]
    node: str  # path::function
    outcome: str  # passed, failure, error or skipped


@dataclass(frozen=True)
class FamilyRun:
    returncode: int
    cases: tuple[FamilyCase, ...]


# --- small helpers -----------------------------------------------------------------------------

def out_path() -> Path:
    return ROOT / OUT_REL


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(value: object) -> str:
    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def valid_actor(actor: str) -> bool:
    """The HDE-SEPA007.5 writer's actor rule."""

    return 0 < len(actor) <= 200 and actor.isprintable() and actor == actor.strip()


def read_input(rel: str) -> bytes:
    try:
        return (ROOT / rel).read_bytes()
    except OSError:
        raise ProofFamilyRecordRefusal(f"{INPUT_UNREADABLE}:{rel}") from None


def read_json(rel: str) -> Any:
    try:
        return json.loads(read_input(rel).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise ProofFamilyRecordRefusal(f"{INPUT_UNREADABLE}:{rel}") from None


def family_env() -> dict[str, str]:
    """The CI job's environment for the family run (``.github/workflows/ci.yml``)."""

    environ = {key: os.environ[key] for key in ("PATH", "HOME") if key in os.environ}
    environ.update({"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0",
                    "APP_ENV": os.environ.get("APP_ENV", "dev"), "PYTHONDONTWRITEBYTECODE": "1"})
    return environ


def tested_inputs() -> tuple[str, ...]:
    family = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / FAMILY_DIR).glob("*.py"))
    return (*LEADING_INPUTS, *family, *TRAILING_INPUTS)


# --- seams (the owner test replaces these over a reduced set) -----------------------------------

def load_root_bundle():
    return _load_active_mechanics_bundle_from_root(ROOT)


def load_index() -> FamilyIndex:
    """The family's pinned index and its own pin, imported from the family."""

    module = importlib.import_module(INDEX_MODULE)
    return FamilyIndex(tuple(module.FAMILY_INDEX), module._check_index)


def compare_goldens_at_root():
    from tools.config.artifacts import compare_goldens

    return compare_goldens(ROOT)


def family_command(outside_nodes: Sequence[str], basetemp: Path, report: Path) -> list[str]:
    return [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp", str(basetemp),
            "--junitxml", str(report), FAMILY_DIR, *outside_nodes]


def parse_report(report: Path) -> tuple[FamilyCase, ...]:
    cases = []
    for case in ET.parse(report).iter("testcase"):
        path = case.get("classname", "").replace(".", "/") + ".py"
        name = case.get("name", "")
        outcome = "passed"
        for child in case:
            if child.tag in ("failure", "error", "skipped"):
                outcome = child.tag
                break
        cases.append(FamilyCase(f"{path}::{name}", f"{path}::{name.split('[', 1)[0]}", outcome))
    return tuple(cases)


def run_family(outside_nodes: Sequence[str]) -> FamilyRun:
    """One ``pytest`` process over the family, its report in a temporary directory outside the tree."""

    with tempfile.TemporaryDirectory(prefix="hde_epic043_pr13_family_") as tmp:
        here = Path(tmp).resolve()
        if here == ROOT.resolve() or ROOT.resolve() in here.parents:
            raise ProofFamilyRecordRefusal(TEMP_DIRECTORY_INSIDE_REPOSITORY)
        report = here / "family.xml"
        result = subprocess.run(family_command(outside_nodes, here / "basetemp", report), cwd=ROOT,
                                env=family_env(), capture_output=True, timeout=FAMILY_TIMEOUT_SECONDS)
        if not report.is_file():
            raise ProofFamilyRecordRefusal(f"{FAMILY_RUN_FAILED}:{result.returncode}:no_report")
        try:
            cases = parse_report(report)
        except ET.ParseError:
            raise ProofFamilyRecordRefusal(f"{FAMILY_RUN_FAILED}:{result.returncode}:report_unreadable") from None
        return FamilyRun(result.returncode, cases)


# --- preconditions and admission ------------------------------------------------------------------

def preconditions() -> None:
    try:
        ensure_determinism_env()
    except DeterminismEnvError:
        raise ProofFamilyRecordRefusal(RAILS_NOT_CLOSED) from None
    if os.environ.get("APP_ENV") not in DEV_APP_ENVS:
        raise ProofFamilyRecordRefusal(APP_ENV_NOT_DEV)
    try:
        here = Path.cwd().resolve()
    except OSError:
        raise ProofFamilyRecordRefusal(WORKING_DIRECTORY_INVALID) from None
    if here != ROOT.resolve():
        raise ProofFamilyRecordRefusal(WORKING_DIRECTORY_INVALID)


def admit():
    """The admitted v2 bundle at the repository root, or a named refusal."""

    try:
        bundle = load_root_bundle()
    except RegistryConfigError as exc:
        raise ProofFamilyRecordRefusal(f"{RELEASE_REFUSED}:{exc.code}") from None
    if (bundle.mechanics.get("config_id") != MAGIC10_V2_CONFIG_ID
            or bundle.mechanics.get("result_schema") != V2_RESULT_SCHEMA
            or bundle.release_id != sha256_hex(read_input(MANIFEST_REL))):
        raise ProofFamilyRecordRefusal(f"{NOT_ADMITTED_V2_PATH}:release")
    return bundle


def schema_closure_lines(bundle) -> list[tuple[str, str]]:
    """The two v2 result schemas are release members bound by the admitted manifest."""

    members = {entry.path: entry.sha256 for entry in bundle.manifest.files}
    lines = []
    for rel in RESULT_SCHEMA_RELS:
        digest = sha256_hex(read_input(rel))
        if members.get(rel) != digest:
            raise ProofFamilyRecordRefusal(f"{NOT_ADMITTED_V2_PATH}:schema_closure:{rel}")
        lines.append((f"release.member.{rel}.sha256", digest))
    return lines


# --- the fixture basis ----------------------------------------------------------------------------

def _without_threshold_binding(configuration: Any) -> Any:
    try:
        stripped = json.loads(json.dumps(configuration))
        del stripped["sources"]["thresholds"]["sha256"]
    except (KeyError, TypeError):
        raise ProofFamilyRecordRefusal(FIXTURE_CONFIGURATION_DIVERGED) from None
    return stripped


def _without_maxima(thresholds: Any) -> Any:
    try:
        return {**thresholds, "categories": [{key: value for key, value in row.items() if key != "maxima"}
                                            for row in thresholds["categories"]]}
    except (KeyError, TypeError, AttributeError):
        raise ProofFamilyRecordRefusal(FIXTURE_THRESHOLDS_DIVERGED) from None


def fixture_basis_lines() -> tuple[str, list[tuple[str, str]]]:
    fixture, cut = read_json(FIXTURE_CONFIG_REL), read_json(CONFIG_REL)
    if (not isinstance(fixture, dict) or not isinstance(cut, dict)
            or fixture.get("config_id") != MAGIC10_V2_CONFIG_ID or cut.get("config_id") != MAGIC10_V2_CONFIG_ID
            or _without_threshold_binding(fixture) != _without_threshold_binding(cut)):
        raise ProofFamilyRecordRefusal(FIXTURE_CONFIGURATION_DIVERGED)
    fixture_thresholds, cut_thresholds = read_json(FIXTURE_THRESHOLDS_REL), read_json(THRESHOLDS_REL)
    if (not isinstance(fixture_thresholds, dict) or not isinstance(cut_thresholds, dict)
            or _without_maxima(fixture_thresholds) != _without_maxima(cut_thresholds)):
        raise ProofFamilyRecordRefusal(FIXTURE_THRESHOLDS_DIVERGED)
    fixture_maxima = sorted({tuple(row["maxima"]) for row in fixture_thresholds["categories"]})
    return fixture["config_id"], [
        ("fixture.configuration", FIXTURE_CONFIG_REL),
        ("fixture.configuration.config_id", fixture["config_id"]),
        ("fixture.configuration.equal_to", f"{CONFIG_REL} except sources.thresholds.sha256"),
        ("fixture.thresholds", FIXTURE_THRESHOLDS_REL),
        ("fixture.thresholds.equal_to", f"{THRESHOLDS_REL} except categories[].maxima"),
        ("fixture.thresholds.maxima", compact([list(maxima) for maxima in fixture_maxima])),
    ]


# --- the index, the family run and non-vacuity ---------------------------------------------------

def checked_index() -> tuple[Mapping[str, Any], ...]:
    index = load_index()
    try:
        index.check(index.rows)
    except AssertionError as exc:
        raise ProofFamilyRecordRefusal(f"{INDEX_INVALID}:pin:{str(exc).splitlines()[0] if str(exc) else 'refused'}") from None
    for row in index.rows:
        if row["basis"] not in RAN_AGAINST or row["basis"] == "test maxima":
            raise ProofFamilyRecordRefusal(f"{INDEX_INVALID}:{row['id']}")
        if row["due"] == CANDIDATE_DUE and row["basis"] != BASIS_ACTIVE:
            raise ProofFamilyRecordRefusal(f"{INDEX_INVALID}:{row['id']}")
    return index.rows


def indexed_nodes(rows: Sequence[Mapping[str, Any]]) -> list[str]:
    return sorted({node for row in rows for node in (*row["passing"], *row["mutations"])})


def outside_nodes(rows: Sequence[Mapping[str, Any]]) -> list[str]:
    return [node for node in indexed_nodes(rows) if not node.startswith(f"{FAMILY_DIR}/")]


def node_outcomes(run: FamilyRun) -> dict[str, list[FamilyCase]]:
    outcomes: dict[str, list[FamilyCase]] = {}
    for case in run.cases:
        outcomes.setdefault(case.node, []).append(case)
    return outcomes


def check_family_run(rows: Sequence[Mapping[str, Any]], run: FamilyRun) -> dict[str, list[FamilyCase]]:
    by_node = node_outcomes(run)
    for row in rows:
        for node in (*row["passing"], *row["mutations"]):
            if not by_node.get(node):
                raise ProofFamilyRecordRefusal(f"{NODE_NOT_RUN}:{row['id']}:{node}")
    for row in rows:
        for node in row["passing"]:
            if any(case.outcome != "passed" for case in by_node[node]):
                raise ProofFamilyRecordRefusal(f"{ITEM_FAILED}:{row['id']}:{node}")
        for node in row["mutations"]:
            if any(case.outcome != "passed" for case in by_node[node]):
                raise ProofFamilyRecordRefusal(f"{MUTATION_NOT_REFUSED}:{row['id']}:{node}")
    for case in run.cases:
        if case.outcome != "passed":
            raise ProofFamilyRecordRefusal(f"{FAMILY_CASE_NOT_PASSED}:{case.case_id}")
    for node in NONVACUITY_PIN_NODES:
        if not by_node.get(node):
            raise ProofFamilyRecordRefusal(f"{NODE_NOT_RUN}:nonvacuity:{node}")
    if run.returncode != 0:
        raise ProofFamilyRecordRefusal(f"{FAMILY_RUN_FAILED}:{run.returncode}")
    return by_node


def broad_handlers(source: str) -> list[int]:
    """Lines of handlers for Exception, BaseException or a bare except, tuples included."""

    lines = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.ExceptHandler):
            types = node.type.elts if isinstance(node.type, ast.Tuple) else [node.type]
            if node.type is None or any(isinstance(item, ast.Name) and item.id in BROAD_HANDLER_NAMES for item in types):
                lines.append(node.lineno)
    return lines


def mutation_modules(rows: Sequence[Mapping[str, Any]]) -> list[str]:
    return sorted({node.partition("::")[0] for row in rows for node in row["mutations"]})


def nonvacuity_lines(rows: Sequence[Mapping[str, Any]], by_node: Mapping[str, list[FamilyCase]]) -> list[tuple[str, str]]:
    modules = mutation_modules(rows)
    for rel in modules:
        try:
            lines = broad_handlers(read_input(rel).decode("utf-8"))
        except (UnicodeDecodeError, SyntaxError):
            raise ProofFamilyRecordRefusal(f"{INPUT_UNREADABLE}:{rel}") from None
        if lines:
            raise ProofFamilyRecordRefusal(f"{BROAD_HANDLER}:{rel}:{lines[0]}")
    mutations = {node: row["id"] for row in rows for node in row["mutations"]}
    lines = [
        ("nonvacuity.rule", "a mutation counts as refused only on a failed assertion or the product's own typed "
                            "refusal; no module that holds a mutation case has a handler for Exception, BaseException "
                            "or a bare except"),
        ("nonvacuity.mutation_modules", str(len(modules))),
        ("nonvacuity.mutation_modules.paths", ",".join(modules)),
        ("nonvacuity.broad_handlers", "0"),
    ]
    for item_id, node, basis in NONVACUITY_CASES:
        if mutations.get(node) != item_id:
            raise ProofFamilyRecordRefusal(f"{INDEX_INVALID}:nonvacuity:{item_id}")
        lines += [(f"nonvacuity.{item_id}.case", node), (f"nonvacuity.{item_id}.refused", basis)]
    for number, node in enumerate(NONVACUITY_PIN_NODES, 1):
        cases = by_node[node]
        lines.append((f"nonvacuity.pin.{number}", f"{node} cases={len(cases)} passed={len(cases)}"))
    return lines


def family_lines(rows, by_node, run: FamilyRun, bundle, fixture_config_id: str) -> list[tuple[str, str]]:
    nodes = indexed_nodes(rows)
    command = " ".join(["python", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp", "<temporary>",
                        "--junitxml", "<temporary>", FAMILY_DIR, *outside_nodes(rows)])
    lines = [
        ("family.command", command),
        ("family.environment", "LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV PYTHONDONTWRITEBYTECODE=1"),
        ("family.index", INDEX_REL),
        ("family.items", str(len(rows))),
        ("family.indexed_nodes", str(len(nodes))),
        ("family.cases.total", str(len(run.cases))),
        ("family.cases.passed", str(sum(case.outcome == "passed" for case in run.cases))),
        ("family.cases.failed", "0"),
        ("family.cases.errors", "0"),
        ("family.cases.skipped", "0"),
    ]
    for basis in sorted({row["basis"] for row in rows}):
        lines.append((f"basis.{basis.replace(' ', '_')}.stands_because", STANDS_BECAUSE[basis]))
    values = {"release_id": bundle.release_id, "config_id": bundle.mechanics["config_id"],
              "fixture_config_id": fixture_config_id}
    for row in rows:
        item = f"item.{row['id']}"
        lines += [
            (f"{item}.text", row["item"]),
            (f"{item}.basis", row["basis"]),
            (f"{item}.due", row["due"]),
            (f"{item}.ran_against", RAN_AGAINST[row["basis"]].format(**values)),
        ]
        for number, node in enumerate(row["passing"], 1):
            cases = by_node[node]
            lines.append((f"{item}.passing.{number}", f"{node} cases={len(cases)} passed={len(cases)}"))
        for number, node in enumerate(row["mutations"], 1):
            cases = by_node[node]
            lines.append((f"{item}.mutation.{number}", f"{node} cases={len(cases)} refused={len(cases)}"))
        lines.append((f"{item}.result", "PASS"))
    return lines


def golden_lines(bundle) -> list[tuple[str, str]]:
    result = compare_goldens_at_root()
    outcomes = [(case.case_id, case.outcome) for case in result.cases]
    for case_id, outcome in outcomes:
        if outcome != "match":
            raise ProofFamilyRecordRefusal(f"{GOLDEN_MISMATCH}:{case_id}")
    if not result.ok or not outcomes:
        raise ProofFamilyRecordRefusal(f"{GOLDEN_MISMATCH}:collection")
    if result.candidate_release_id != bundle.release_id or result.goldens_sha256 != sha256_hex(read_input(GOLDENS_REL)):
        raise ProofFamilyRecordRefusal(f"{GOLDEN_MISMATCH}:identity")
    lines = [
        ("goldens.collection", GOLDENS_REL),
        ("goldens.collection_sha256", result.goldens_sha256),
        ("goldens.candidate_release_id", result.candidate_release_id),
        ("goldens.config_id", result.config_id),
        ("goldens.orders", "both pair orders, at the cut maxima, through tools/config/artifacts.py compare_goldens"),
    ]
    lines += [(f"goldens.case.{case_id}", outcome) for case_id, outcome in outcomes]
    lines.append(("goldens.match", f"{len(outcomes)} of {len(outcomes)}"))
    return lines


# --- the record -------------------------------------------------------------------------------------

def tested_input_lines() -> list[tuple[str, str]]:
    lines: list[tuple[str, str]] = []
    digests = []
    inputs = tested_inputs()
    for rel in inputs:
        data = read_input(rel)
        digests.append(f"{rel} {sha256_hex(data)} {len(data)}")
        lines += [(f"input.{rel}.sha256", sha256_hex(data)), (f"input.{rel}.size_bytes", str(len(data)))]
    lines += [
        ("tested_inputs.count", str(len(inputs))),
        ("tested_inputs.sha256", sha256_hex(("\n".join(digests) + "\n").encode("utf-8"))),
        ("tested_state", "the inputs above; this record carries no git state, and the PR result maps "
                         "tested_inputs.sha256 to the attested head"),
    ]
    return lines


def collect() -> list[tuple[str, str]]:
    """Every line of the record after the run fields, in record order."""

    lines = tested_input_lines()
    bundle = admit()
    lines += [
        ("release.release_id", bundle.release_id),
        ("release.manifest_sha256_equals_release_id", "true"),
        ("release.version", bundle.manifest.version),
        ("release.member_count", str(len(bundle.manifest.files))),
        ("release.config_id", bundle.mechanics["config_id"]),
        ("release.result_schema", bundle.mechanics["result_schema"]),
        ("release.compat_result_schema", V2_COMPAT_SCHEMA),
        *schema_closure_lines(bundle),
    ]
    fixture_config_id, fixture_lines = fixture_basis_lines()
    lines += fixture_lines
    rows = checked_index()
    run = run_family(outside_nodes(rows))
    by_node = check_family_run(rows, run)
    lines += family_lines(rows, by_node, run, bundle, fixture_config_id)
    lines += golden_lines(bundle)
    lines += nonvacuity_lines(rows, by_node)
    lines += [
        ("command.write", f"python {GENERATOR_REL} --actor <actor>"),
        ("command.check", f"python {GENERATOR_REL} --check"),
        ("result_record", "the validation pair, admission, the cut, bundle and integration records' --check, the "
                          "unchanged-history proof and the exact-source attestation of the attested head with its "
                          "predicate table are recorded in the unit's PR_IMPLEMENTATION_RESULT in amthorn78/glow-docs"),
    ]
    lines += [(f"limitation.{number}", text) for number, text in enumerate(LIMITATIONS, 1)]
    lines += [("items.pass", str(len(rows))), ("status", "COMPLETE")]
    return lines


def header(run: Mapping[str, str]) -> list[tuple[str, str]]:
    return [
        ("schema", SCHEMA),
        ("epic_id", "HDE-EPIC043"),
        ("task_id", "HDE-DIST008"),
        ("subtask_ids", "HDE-DIST008.1"),
        ("work_unit_id", "WU-PR-13"),
        *((key, run[key]) for key in RUN_FIELDS),
    ]


def render(lines: Sequence[tuple[str, str]]) -> bytes:
    keys = [key for key, _value in lines]
    if len(keys) != len(set(keys)) or keys[0] != "schema" or keys[-1] != "status":
        raise ProofFamilyRecordRefusal(RECORD_INVALID)
    for key, value in lines:
        if (not isinstance(value, str) or not key or ": " in key
                or any(char in f"{key}{value}" for char in "\r\n")):
            raise ProofFamilyRecordRefusal(RECORD_INVALID)
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
        raise ProofFamilyRecordRefusal(INVALID_ACTOR)
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
    run = {key: value for key, value in parsed if key in RUN_FIELDS}
    if [key for key, _ in parsed[5:8]] != list(RUN_FIELDS) or len(run) != len(RUN_FIELDS):
        raise SystemExit(f"DRIFT:{OUT_REL}:run")
    problem = run_fields_problem(run)
    if problem:
        raise SystemExit(f"DRIFT:{OUT_REL}:{problem}")
    head = header(run)
    inputs = tested_input_lines()
    # The tested inputs are compared before the family runs, so a stale record fails fast.
    for (want_key, want), (have_key, have) in zip([*head, *inputs], parsed):
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
                      help="compare the tested inputs, re-run the family, re-derive every line and compare the "
                           "bytes; write nothing")
    args = parser.parse_args(argv)
    try:
        if args.check:
            check()
            print("v2 proof family record check ok")
            return 0
        write(args.actor)
    except ProofFamilyRecordRefusal as exc:
        raise SystemExit(exc.code) from None
    print("v2 proof family record written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
