#!/usr/bin/env python3
"""Separation v2 contract evidence (HDE-EPIC042 WU-PR-04; HDE-SEPA007.5).

The generator proves the Magic-10 v2 contract's behaviour on actual bundles and
records it as one governed record, ``audit/qa/hde-epic042/pr-04/
v2_contract_evidence.txt``, for HDE-SEPA007.1 to HDE-SEPA007.4.

An actual bundle is the tested tree's ``catalog/``, ``math/`` and ``schemas/``
copied into a temporary root, with the labelled non-canon fixtures of
``tests/fixtures/magic10_v2/`` placed at ``math/thresholds.json`` and
``catalog/magic10_mechanics_v2.json``, admitted through the WU-PR-03 loader's
public function.  A mutated bundle is one edit of one real input in a fresh copy
of that root.  Each row of the record passes on the actual bundle and fails on its
mutation:

* the schema mutation matrix over the six v2 schemas (an unknown field added,
  each required field dropped, each bounded field out of domain; the two result
  schemas take the admitted release's real-path v2 result, as produced);
* catalog, caps and thresholds closure checks;
* the configuration and source-bundle identity (HDE-SEPA007.4);
* canonical bytes of the eight governed files.

It also runs the AC-08 checks of the Implementation Audit's EC-13, re-targeted
at the v2 cut (HDE-EPIC043 WU-PR-10; HDE-DIST008.2): the unchanged-history and
membership checks cover HDE-EPIC042's own fixed ranges, judged against the
release of ``EPIC_END``'s manifest, not the tested tree's roster; the active
identity is computed at run time (the SHA-256 of ``catalog/manifest.json`` and
``MAGIC10_V2_CONFIG_ID``) and must differ from that prior release.
The record names the tested commit, the responsible actor and the run time;
``--check`` byte-compares everything reproducible and checks those run-time
fields for shape and consistency.  Nothing is written under the repository's
``catalog/`` or ``math/``, and no maxima value is asserted as canon.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import importlib.metadata
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterator, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import jsonschema  # noqa: E402
from jsonschema import validators  # noqa: E402
from jsonschema.exceptions import SchemaError, best_match  # noqa: E402
from referencing import Registry  # noqa: E402
from referencing.exceptions import NoSuchResource  # noqa: E402

from engine.cli import main as cli_main  # noqa: E402
from engine.compat.compute import evaluate_pair, evaluation_party  # noqa: E402
from engine.config.magic10_v2_loader import (  # noqa: E402
    MAGIC10_V2_COMPAT_RESULT_SCHEMA,
    MAGIC10_V2_CONFIG_ID,
    MAGIC10_V2_CONFIGURATION_PATH,
    MAGIC10_V2_RESULT_SCHEMA,
    load_magic10_v2_bundle_from_root,
    magic10_v2_source_bundle_sha256,
)
from engine.config.registry_loader import (  # noqa: E402
    ManifestEntry,
    RegistryConfigError,
    load_active_mechanics_bundle,
)
from engine.runtime.determinism_env import ensure_determinism_env  # noqa: E402
from engine.serializer import canon  # noqa: E402

OUT_REL = "audit/qa/hde-epic042/pr-04/v2_contract_evidence.txt"
OUT = ROOT / OUT_REL
SCHEMA = "hde_epic042_v2_contract_evidence.v1"
GENERATOR_REL = "tools/evidence/generate_hde_epic042_v2_contract_evidence.py"

# AC-08 ranges (Implementation Audit EC-13), fixed to HDE-EPIC042's own history at the
# v2 cut (HDE-EPIC043 WU-PR-10): the unit base (WU-PR-03) to the unit's squash merge
# (WU-PR-04), and the last commit before any v2 contract file (WU-PR-01, WU-PR-02's
# base) to the Epic's close (CL-05).  The release they are judged against is the one
# EPIC_END's manifest names; the active identity is computed at run time.
UNIT_BASE = "330a7e9124c360776fd3c5a2123b24421287c00e"
UNIT_END = "bdcf21d1c8ecb0657a66c786277f60e900933868"
PRE_DELIVERY_BASE = "a0b796bc64fe0f058e69ec81f79e2561a840c71d"
EPIC_END = "a9cf2356360ff93d413396381c3ae8089cc4f631"
HISTORY_COMMITS = (UNIT_BASE, UNIT_END, PRE_DELIVERY_BASE, EPIC_END)
MANIFEST_REL = "catalog/manifest.json"

# Procedure-proof identity of the fixture bundle (WU-PR-03 result v1.0 §5.3); not
# the cutover identity (Specification TI-03).
PROOF_CONFIG_SHA256 = "8aaaa0c37d545fc267eb3816967b33547562b3f19c804fe963dabb2429c44d41"
PROOF_SOURCE_BUNDLE_SHA256 = "cacd5789dc6956a00fbbb1a91461543511b44eb7fc2cae4184b9e1fef907c96a"

CONFIG_PATH = MAGIC10_V2_CONFIGURATION_PATH
FIXTURE_CONFIG = "tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json"
FIXTURE_THRESHOLDS = "tests/fixtures/magic10_v2/thresholds_v2.fixture.json"
# Root path -> repository path of the labelled fixture placed there.
FIXTURES = {CONFIG_PATH: FIXTURE_CONFIG, "math/thresholds.json": FIXTURE_THRESHOLDS}
BUNDLE_DIRECTORIES = ("catalog", "math", "schemas")
CHARTS = ("fixtures/charts/alice.json", "fixtures/charts/bob.json")

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
RESULT_SCHEMAS = ("schemas/magic10_result_v2.schema.json", "schemas/magic10_compat_result_v2.schema.json")
# Schema -> the root path of the data instance it governs (None: a result schema).
MATRIX_SCHEMAS: tuple[tuple[str, str | None, str], ...] = (
    ("schemas/centers_v1.schema.json", "catalog/centers_v1.json", "HDE-SEPA007.1,HDE-SEPA007.3"),
    ("schemas/type_pairing_v1.schema.json", "catalog/type_pairing_v1.json", "HDE-SEPA007.1,HDE-SEPA007.3"),
    ("schemas/magic10_mechanics_v2.schema.json", CONFIG_PATH, "HDE-SEPA007.2,HDE-SEPA007.3"),
    ("schemas/thresholds_v2.schema.json", "math/thresholds.json", "HDE-SEPA007.2,HDE-SEPA007.3"),
    ("schemas/magic10_result_v2.schema.json", None, "HDE-SEPA007.2"),
    ("schemas/magic10_compat_result_v2.schema.json", None, "HDE-SEPA007.2"),
)
# The configuration's source bindings (rebound when that source is mutated).
SOURCE_NAMES = {
    "catalog/magic10_caps.json": "caps",
    "catalog/magic10.json": "categories",
    "catalog/centers_v1.json": "centers",
    "catalog/channels_v1.json": "channels",
    "math/thresholds.json": "thresholds",
    "catalog/type_pairing_v1.json": "type_pairing",
}

# Expected values transcribed from canon, not read from the module under test:
# HDE Schemas and Artifacts §2.1 (motor centers) and §2.9 ("Type-pairing catalog";
# "Tuning and loader closure"); HDE Build Notes, the offsets addendum (offsets
# table); HDE Math Spec §5.3.7 (maxima).
MOTOR_CENTERS = frozenset({"ego", "root", "sacral", "solar_plexus"})
AURA_CLASSES = ("generator", "projector", "manifestor", "reflector")
PAIR_RULES = (
    "same_class",
    "generator_with_nonsacral",
    "generator_manifestor",
    "generator_projector",
    "projector_manifestor",
    "reflector_present",
)
NONZERO_OFFSETS = {
    ("generator_projector", "communication"): 50,
    ("generator_projector", "alignment"): 50,
    ("projector_manifestor", "alignment"): -50,
}
CAPS_BOUNDS = {"min": 0, "max": 100}

# Every file the run reads as input, by repository path; T-09 checks the list.
# The result-instance path also executes the active release, whose members
# catalog/manifest.json binds.
TESTED_INPUTS = tuple(sorted({
    GENERATOR_REL,
    "engine/config/magic10_v2_loader.py",
    "engine/config/registry_loader.py",
    *CHARTS,
    FIXTURE_CONFIG,
    FIXTURE_THRESHOLDS,
    "catalog/centers_v1.json",
    "catalog/channels_v1.json",
    "catalog/gates_v1.json",
    "catalog/magic10.json",
    "catalog/magic10_caps.json",
    "catalog/magic10_seeds.json",
    "catalog/manifest.json",
    "catalog/type_pairing_v1.json",
    "schemas/centers_v1.schema.json",
    "schemas/channels_v1.schema.json",
    "schemas/gates_v1.schema.json",
    "schemas/magic10_compat_result_v2.schema.json",
    "schemas/magic10_mechanics_v2.schema.json",
    "schemas/magic10_result_v2.schema.json",
    "schemas/thresholds_v2.schema.json",
    "schemas/type_pairing_v1.schema.json",
}))

UNKNOWN_KEY = "x_unknown_field"
DRAFT_2020_12 = "https://json-schema.org/draft/2020-12/schema"
ENV_PIN_KEYS = ("ALLOW_NETWORK", "LANG", "LC_ALL", "SAFE_MODE", "TZ")
RUN_FIELDS = ("run.tested_commit", "run.time_utc", "run.actor", "run.python")
_HEX40 = re.compile(r"[0-9a-f]{40}")
_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
_PYTHON = re.compile(r"\d+\.\d+\.\d+")

DIRTY_EXIT = "V2_CONTRACT_EVIDENCE_DIRTY_TREE"
HISTORY_EXIT = "V2_CONTRACT_EVIDENCE_HISTORY_UNAVAILABLE"
FAILED_EXIT = "V2_CONTRACT_EVIDENCE_FAILED"
REAL_PATH_NOT_V2 = "REAL_PATH_RESULT_NOT_V2"

LIMITATIONS = (
    "the result-schema instances are the admitted release's real-path result (evaluate_pair on "
    f"fixtures/charts/alice.json and bob.json), {MAGIC10_V2_RESULT_SCHEMA} and {MAGIC10_V2_COMPAT_RESULT_SCHEMA} "
    f"under {MAGIC10_V2_CONFIG_ID} as produced; they prove the result schemas' acceptance and refusals, not the "
    "score values; the matrix validates them with this generator's strict Draft 2020-12 validator",
    "the configuration and thresholds under test are the labelled non-canon fixtures of tests/fixtures/magic10_v2/; "
    "no maxima value is canon (C-07) and the identity values are procedure proofs, not the cutover identity (TI-03)",
    "this record is PR evidence, not QA evidence",
    f"the ac08 history and membership lines cover HDE-EPIC042's fixed ranges {UNIT_BASE}..{UNIT_END} and "
    f"{PRE_DELIVERY_BASE}..{EPIC_END}, judged against the release of {EPIC_END}:{MANIFEST_REL}, not the tested "
    "tree's roster; the ac08 active identity is the tested tree's admitted release (the v2 cut, HDE-DIST008.2), "
    "which must differ from that prior release",
    "the only interface exercised is the in-process evaluate_pair call; the CLI, HTTP and vendor interfaces that "
    "reach the v2 contract are not exercised by this record",
    "when the tested commit object is absent (after a squash merge whose branch was deleted), its consistency "
    "check is not applicable and the recomputed tested-inputs digest binds the tested files",
)


class EvidenceError(Exception):
    """A generator failure, as distinct from a row outcome."""


@dataclass(frozen=True)
class Row:
    family: str
    subtasks: str
    input: str
    mutation: str
    expected: str
    observed: str

    @property
    def passed(self) -> bool:
        # Every token the expectation names must appear in the observation.
        return set(self.expected.split()) <= set(self.observed.split())

    def line(self) -> str:
        return (
            f"family={self.family}; subtasks={self.subtasks}; input={self.input}; mutation={self.mutation}; "
            f"expected={self.expected}; observed={self.observed}; result={'pass' if self.passed else 'fail'}"
        )


# --- environment and processes ---------------------------------------------------------------

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def cbytes(obj: object) -> bytes:
    return canon.sercanon(obj, sort_keys=True)


def child_env() -> dict[str, str]:
    """Closed-rails environment for every child process."""

    environ = os.environ.copy()
    environ.update({
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "APP_ENV": "test",
        "PIP_NO_INDEX": "1",
    })
    ensure_determinism_env(environ=environ)
    return environ


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(["git", *args], cwd=ROOT, env=child_env(), capture_output=True)
    if check and proc.returncode:
        raise EvidenceError(f"git {args[0]} failed rc={proc.returncode}")
    return proc


def run_tool(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], cwd=ROOT, env=child_env(), capture_output=True)


def tree_is_clean() -> bool:
    return git("status", "--porcelain", "--untracked-files=all").stdout == b""


def commit_present(commit: str) -> bool:
    return git("cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode == 0


def head_commit() -> str:
    return git("rev-parse", "HEAD").stdout.decode("ascii").strip()


# --- the actual bundle -----------------------------------------------------------------------

def assemble(directory: Path) -> Path:
    """The actual bundle: the tested tree's catalog/math/schemas plus the placed fixtures."""

    root = directory / "root"
    for name in BUNDLE_DIRECTORIES:
        shutil.copytree(ROOT / name, root / name)
    for placed, source in FIXTURES.items():
        (root / placed).write_bytes((ROOT / source).read_bytes())
    return root


def manifest_rows(root: Path) -> tuple[ManifestEntry, ...]:
    data = (root / CONFIG_PATH).read_bytes()
    return (ManifestEntry(CONFIG_PATH, sha256_hex(data), len(data)),)


def admit(root: Path):
    """Return (bundle, None) when admitted, or (None, refusal) when refused."""

    try:
        return load_magic10_v2_bundle_from_root(root, manifest_rows(root)), None
    except RegistryConfigError as exc:
        return None, exc


def describe_refusal(exc: RegistryConfigError) -> str:
    parts = [f"refused {exc.code}"]
    for key in ("schema", "instance_path", "keyword", "item", "category", "source"):
        value = exc.details.get(key)
        if isinstance(value, str):
            parts.append(f"{key}={value}")
    return " ".join(parts)


def write_mutated(root: Path, rel: str, obj: object) -> None:
    """Write canonical bytes; rebind the configuration's source binding for a source."""

    (root / rel).write_bytes(cbytes(obj))
    name = SOURCE_NAMES.get(rel)
    if name is not None:
        config = json.loads((root / CONFIG_PATH).read_bytes())
        config["sources"][name]["sha256"] = sha256_hex((root / rel).read_bytes())
        (root / CONFIG_PATH).write_bytes(cbytes(config))


class Mutator:
    """Fresh copies of the actual root, one per mutation, removed afterwards."""

    def __init__(self, base: Path, scratch: Path) -> None:
        self.base = base
        self.scratch = scratch
        self.count = 0

    def root(self) -> Path:
        self.count += 1
        target = self.scratch / f"m{self.count:04d}"
        shutil.copytree(self.base, target)
        return target

    def admit_json(self, rel: str, edit: Callable[[object], object | None]):
        target = self.root()
        try:
            obj = json.loads((target / rel).read_bytes())
            edited = edit(obj)
            write_mutated(target, rel, obj if edited is None else edited)
            return admit(target)
        finally:
            shutil.rmtree(target)

    def admit_raw(self, rel: str, raw: bytes):
        target = self.root()
        try:
            (target / rel).write_bytes(raw)
            return admit(target)
        finally:
            shutil.rmtree(target)


def input_label(rel: str) -> str:
    source = FIXTURES.get(rel)
    return f"{source} at {rel}" if source else rel


# --- the schema mutation matrix --------------------------------------------------------------

def _reject_retrieval(uri: str):
    raise NoSuchResource(ref=uri)


def strict_validator(schema: Mapping[str, object]):
    """Draft 2020-12, integers exclude booleans, no remote retrieval."""

    base = jsonschema.Draft202012Validator
    strict = validators.extend(
        base, type_checker=base.TYPE_CHECKER.redefine("integer", lambda checker, value: type(value) is int)
    )
    strict.check_schema(schema)
    return strict(schema, registry=Registry(retrieve=_reject_retrieval))


def _resolve(schema: Mapping[str, object], node: object) -> object:
    while isinstance(node, dict) and "$ref" in node:
        ref = node["$ref"]
        if not isinstance(ref, str) or not ref.startswith("#/"):
            raise EvidenceError(f"non-local $ref in schema: {ref!r}")
        target: object = schema
        for part in ref[2:].split("/"):
            target = target[part]  # type: ignore[index]
        node = target
    return node


def _branch(schema: Mapping[str, object], node: object, instance: object, pointer: str):
    """Resolve ``node``; at oneOf/anyOf take the one branch the actual node satisfies."""

    node = _resolve(schema, node)
    if not isinstance(node, dict):
        return {}, pointer
    for keyword in ("oneOf", "anyOf"):
        if keyword in node:
            for index, branch in enumerate(node[keyword]):
                resolved = _resolve(schema, branch)
                candidate = {**schema, **resolved}
                if strict_validator(candidate).is_valid(instance):
                    merged = {key: value for key, value in node.items() if key != keyword}
                    merged.update(resolved)
                    return _branch(schema, merged, instance, f"{pointer}/{keyword}/{index}")
            raise EvidenceError(f"actual instance matches no {keyword} branch at {pointer}")
    return node, pointer


def enumerate_mutations(schema: Mapping[str, object], instance: object) -> list[tuple[str, str]]:
    """(kind, instance pointer) once per distinct schema location, first occurrence."""

    seen: set[str] = set()
    found: list[tuple[str, str]] = []

    def walk(node: object, value: object, pointer: str, schema_pointer: str) -> None:
        node, schema_pointer = _branch(schema, node, value, schema_pointer)
        if isinstance(value, dict):
            if schema_pointer not in seen:
                seen.add(schema_pointer)
                if node.get("additionalProperties") is False:
                    found.append(("unknown_field", pointer or "/"))
                for member in node.get("required", ()):
                    if member in value:
                        found.append(("required_dropped", f"{pointer}/{member}"))
            for key, sub in node.get("properties", {}).items():
                if key in value:
                    walk(sub, value[key], f"{pointer}/{key}", f"{schema_pointer}/properties/{key}")
        elif isinstance(value, list):
            prefix = node.get("prefixItems", [])
            for index, item in enumerate(value):
                if index < len(prefix):
                    walk(prefix[index], item, f"{pointer}/{index}", f"{schema_pointer}/prefixItems/{index}")
                elif isinstance(node.get("items"), dict):
                    walk(node["items"], item, f"{pointer}/{index}", f"{schema_pointer}/items")
        elif schema_pointer not in seen and any(key in node for key in ("minimum", "maximum", "enum", "const")):
            seen.add(schema_pointer)
            found.append(("out_of_domain", pointer))

    walk(schema, instance, "", "#")
    return found


def _parts(pointer: str) -> list[str]:
    return [part for part in pointer.split("/") if part]


def _child(container: object, part: str) -> object:
    return container[int(part)] if isinstance(container, list) else container[part]  # type: ignore[index]


def _leaf_schema(schema: Mapping[str, object], instance: object, pointer: str) -> Mapping[str, object]:
    node: object = schema
    value = instance
    walked = ""
    for part in _parts(pointer):
        node, _ = _branch(schema, node, value, walked)
        if isinstance(value, list):
            index = int(part)
            prefix = node.get("prefixItems", [])  # type: ignore[union-attr]
            node = prefix[index] if index < len(prefix) else node["items"]  # type: ignore[index]
        else:
            node = node["properties"][part]  # type: ignore[index]
        value = _child(value, part)
        walked += f"/{part}"
    return _branch(schema, node, value, walked)[0]


def out_of_domain_value(node: Mapping[str, object], value: object) -> object:
    if "maximum" in node:
        return node["maximum"] + 1  # type: ignore[operator]
    if "minimum" in node:
        return node["minimum"] - 1  # type: ignore[operator]
    allowed = list(node["enum"]) if "enum" in node else [node["const"]]
    if isinstance(value, str):
        return f"{value}_out_of_domain"
    integers = [item for item in allowed if type(item) is int]
    if type(value) is int and integers:
        return max(integers) + 1
    return "out_of_domain"


def apply_mutation(schema: Mapping[str, object], instance: object, kind: str, pointer: str) -> object:
    mutated = copy.deepcopy(instance)
    if kind == "unknown_field":
        target = mutated
        for part in _parts(pointer):
            target = _child(target, part)
        target[UNKNOWN_KEY] = 0  # type: ignore[index]
        return mutated
    *parent_parts, last = _parts(pointer)
    parent = mutated
    for part in parent_parts:
        parent = _child(parent, part)
    if kind == "required_dropped":
        del parent[last]  # type: ignore[union-attr]
        return mutated
    value = _child(parent, last)
    new = out_of_domain_value(_leaf_schema(schema, instance, pointer), value)
    if isinstance(parent, list):
        parent[int(last)] = new
    else:
        parent[last] = new  # type: ignore[index]
    return mutated


def validate_result(schema: Mapping[str, object], schema_rel: str, instance: object) -> str:
    error = best_match(strict_validator(schema).iter_errors(instance))
    if error is None:
        return "accepted"
    pointer = "/" + "/".join(str(part) for part in error.absolute_path)
    return f"refused schema={schema_rel} instance_path={pointer} keyword={error.validator}"


def result_instances() -> dict[str, dict]:
    """The admitted release's real pure and compat v2 results of the fixture pair, as produced.

    Refuses with ``REAL_PATH_RESULT_NOT_V2`` unless both carry the v2 schema and
    ``MAGIC10_V2_CONFIG_ID``: nothing is re-identified.
    """

    def party(rel: str, label: str):
        data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        normalized = cli_main._normalize_party(dict(data), label)
        return evaluation_party(cli_main._resolve_party(normalized, source_policy="local"))

    class RecordingCache:
        def __init__(self) -> None:
            self.entries: list[Mapping[str, object]] = []

        def get(self, key: str) -> None:
            return None

        def put(self, key: str, value: Mapping[str, object]) -> None:
            self.entries.append(value)

    cache = RecordingCache()
    compat = evaluate_pair(party(CHARTS[0], "left"), party(CHARTS[1], "right"), cache=cache)
    if len(cache.entries) != 1:
        raise EvidenceError("the real path did not hand exactly one pure result to the cache")
    pure = copy.deepcopy(dict(cache.entries[0]["result"]))  # type: ignore[arg-type]
    compat = copy.deepcopy(dict(compat))
    if ((pure.get("schema"), pure.get("config_id")) != (MAGIC10_V2_RESULT_SCHEMA, MAGIC10_V2_CONFIG_ID)
            or (compat.get("schema"), compat.get("config_id")) != (MAGIC10_V2_COMPAT_RESULT_SCHEMA,
                                                                    MAGIC10_V2_CONFIG_ID)):
        raise EvidenceError(REAL_PATH_NOT_V2)
    return {RESULT_SCHEMAS[0]: pure, RESULT_SCHEMAS[1]: compat}


def schema_matrix(base: Path, mutator: Mutator, results: Mapping[str, dict]) -> list[Row]:
    rows: list[Row] = []
    for schema_rel, instance_rel, subtasks in MATRIX_SCHEMAS:
        schema = json.loads((base / schema_rel).read_bytes())
        if instance_rel is None:
            instance = results[schema_rel]
            label = "v2 real-path result"
            observed = validate_result(schema, schema_rel, instance)
            rows.append(Row("schema_matrix", subtasks, label, "actual", "accepted", observed))
        else:
            instance = json.loads((base / instance_rel).read_bytes())
            label = input_label(instance_rel)
            bundle, refusal = admit(base)
            observed = "admitted" if bundle is not None else describe_refusal(refusal)
            rows.append(Row("schema_matrix", subtasks, label, "actual", "admitted", observed))
        for kind, pointer in enumerate_mutations(schema, instance):
            mutated = apply_mutation(schema, instance, kind, pointer)
            if instance_rel is None:
                observed = validate_result(schema, schema_rel, mutated)
                expected = f"refused schema={schema_rel}"
            else:
                bundle, refusal = mutator.admit_json(instance_rel, lambda obj, mutated=mutated: mutated)
                observed = "admitted" if bundle is not None else describe_refusal(refusal)
                expected = f"refused M10V2_SCHEMA_VALIDATION_FAILED schema={schema_rel}"
            rows.append(Row("schema_matrix", subtasks, label, f"{kind} {pointer}", expected, observed))
    return rows


# --- closure, identity and canonical bytes ----------------------------------------------------

def _set(path: Sequence[object], value: object) -> Callable[[object], None]:
    def edit(obj: object) -> None:
        target = obj
        for part in path[:-1]:
            target = target[part]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]
    return edit


def _rule(obj: Mapping[str, object], rule_id: str) -> dict:
    return next(rule for rule in obj["rules"] if rule["rule_id"] == rule_id)  # type: ignore[union-attr]


def _swap(sequence: list, first: int, second: int) -> None:
    sequence[first], sequence[second] = sequence[second], sequence[first]


def catalog_closure_failures(bundle) -> list[str]:
    failures = []
    if set(bundle.centers) != set(bundle.registry.centers) or len(bundle.centers) != 9:
        failures.append("centers_not_the_nine_gate_derived")
    if {center for center, motor in bundle.centers.items() if motor} != MOTOR_CENTERS:
        failures.append("motor_set")
    if tuple(bundle.aura_classes) != AURA_CLASSES:
        failures.append("aura_classes")
    if tuple(bundle.type_pairing) != PAIR_RULES:
        failures.append("rule_order")
    order = tuple(bundle.registry.magic10_order)
    cells = {(rule, category): value for rule, offsets in bundle.type_pairing.items()
             for category, value in offsets.items()}
    # Offsets are a JSON object keyed by category: every rule has every category.
    if any(set(offsets) != set(order) for offsets in bundle.type_pairing.values()) or len(cells) != 60:
        failures.append("cells")
    if {cell: value for cell, value in cells.items() if value} != NONZERO_OFFSETS:
        failures.append("offsets")
    return failures


def caps_closure_failures(bundle) -> list[str]:
    registry = bundle.registry
    order = tuple(registry.magic10_order)
    failures = []
    signals = [row["signal_id"] for row in bundle.configuration["signals"]]
    if signals != [signal for category in order for signal in registry.magic10_caps[category].inputs]:
        failures.append("signal_roster")
    if len(signals) != 20 or len(order) != 10:
        failures.append("counts")
    if any(len(registry.magic10_caps[category].inputs) != 2 for category in order):
        failures.append("two_inputs")
    if any(dict(registry.magic10_caps[category].bounds) != CAPS_BOUNDS for category in order):
        failures.append("bounds")
    return failures


def thresholds_closure_failures(bundle) -> list[str]:
    failures = []
    if tuple(bundle.maxima) != tuple(bundle.registry.magic10_order) or len(bundle.maxima) != 10:
        failures.append("one_set_per_category")
    for category, maxima in bundle.maxima.items():
        values = tuple(maxima)
        if (len(values) != 4 or any(type(value) is not int for value in values)
                or any(not 0 <= value <= 100 for value in values)
                or any(earlier >= later for earlier, later in zip(values, values[1:]))
                or values[-1] != 100):
            failures.append(f"maxima:{category}")
    return failures


def _check_row(family: str, subtasks: str, label: str, failures: list[str]) -> Row:
    observed = "pass" if not failures else "fail " + ",".join(failures)
    return Row(family, subtasks, label, "actual", "pass", observed)


def _mutation_row(family: str, subtasks: str, mutator: Mutator, rel: str, text: str,
                  edit: Callable[[object], object | None], expected: str) -> Row:
    bundle, refusal = mutator.admit_json(rel, edit)
    observed = "admitted" if bundle is not None else describe_refusal(refusal)
    rebound = ", rebound" if rel in SOURCE_NAMES else ""
    return Row(family, subtasks, input_label(rel), f"{text}{rebound}", expected, observed)


SCHEMA_REFUSAL = "refused M10V2_SCHEMA_VALIDATION_FAILED schema="
PINNED = "refused M10V2_PINNED_CONTENT_MISMATCH item=type_pairing"


def closure_rows(bundle, mutator: Mutator) -> list[Row]:
    centers, pairing = "catalog/centers_v1.json", "catalog/type_pairing_v1.json"
    caps, thresholds = "catalog/magic10_caps.json", "math/thresholds.json"
    sub_catalog, sub_config = "HDE-SEPA007.1,HDE-SEPA007.3", "HDE-SEPA007.2,HDE-SEPA007.3"

    def motor_g(obj):
        next(row for row in obj["centers"] if row["center_id"] == "g")["motor"] = True

    def drop_cell(obj):
        del obj["rules"][0]["offsets"]["harmony"]

    def drop_last_rule(obj):
        obj["rules"].pop()

    def drop_harmony_input(obj):
        obj["harmony"]["inputs"].pop()

    def add_harmony_input(obj):
        obj["harmony"]["inputs"].append("signal_clarity")

    def duplicate_category(obj):
        obj["categories"][1]["category_id"] = obj["categories"][0]["category_id"]

    def drop_first_maximum(obj):
        obj["categories"][0]["maxima"].pop(0)

    def equal_maxima(obj):
        maxima = obj["categories"][0]["maxima"]
        maxima[1] = maxima[0]

    def drop_first(key):
        def edit(obj):
            del obj[key][0]
        return edit

    rows = [_check_row("catalog_closure", sub_catalog, "the actual bundle", catalog_closure_failures(bundle))]
    catalog = (
        (centers, "g marked motor", motor_g, "refused M10V2_CENTER_MOTOR_MISMATCH"),
        (centers, "first center_id replaced", _set(("centers", 0, "center_id"), "spleen_x"),
         SCHEMA_REFUSAL + "schemas/centers_v1.schema.json"),
        (centers, "first center row removed", drop_first("centers"), SCHEMA_REFUSAL + "schemas/centers_v1.schema.json"),
        (pairing, "first two rules swapped", lambda obj: _swap(obj["rules"], 0, 1), PINNED),
        (pairing, "first two aura classes swapped", lambda obj: _swap(obj["aura_classes"], 0, 1), PINNED),
        (pairing, "generator_projector communication 50 to 0",
         lambda obj: _rule(obj, "generator_projector")["offsets"].__setitem__("communication", 0), PINNED),
        (pairing, "same_class harmony 0 to 25",
         lambda obj: _rule(obj, "same_class")["offsets"].__setitem__("harmony", 25), PINNED),
        (pairing, "same_class harmony cell removed", drop_cell, SCHEMA_REFUSAL + "schemas/type_pairing_v1.schema.json"),
        (pairing, "last rule removed", drop_last_rule, SCHEMA_REFUSAL + "schemas/type_pairing_v1.schema.json"),
    )
    rows += [_mutation_row("catalog_closure", sub_catalog, mutator, *item) for item in catalog]

    rows.append(_check_row("caps_closure", sub_config, "the actual bundle", caps_closure_failures(bundle)))
    caps_rows = (
        (CONFIG_PATH, "signals 0 and 1 swapped", lambda obj: _swap(obj["signals"], 0, 1),
         "refused M10V2_SIGNAL_ORDER_MISMATCH"),
        (CONFIG_PATH, "signals 1 and 2 swapped across a category", lambda obj: _swap(obj["signals"], 1, 2),
         "refused M10V2_SIGNAL_ORDER_MISMATCH"),
        (CONFIG_PATH, "first signal removed", drop_first("signals"),
         SCHEMA_REFUSAL + "schemas/magic10_mechanics_v2.schema.json"),
        (caps, "one harmony input removed", drop_harmony_input, "refused MAGIC10_INPUTS_MISMATCH"),
        (caps, "the two harmony inputs swapped", lambda obj: _swap(obj["harmony"]["inputs"], 0, 1),
         "refused MAGIC10_INPUTS_MISMATCH"),
        (caps, "a third harmony input added", add_harmony_input, "refused MAGIC10_INPUTS_MISMATCH"),
        (caps, "harmony max 100 to 99", _set(("harmony", "bounds", "max"), 99), "refused INVALID_MAGIC10"),
        (caps, "harmony min 0 to 1", _set(("harmony", "bounds", "min"), 1), "refused INVALID_MAGIC10"),
    )
    rows += [_mutation_row("caps_closure", sub_config, mutator, *item) for item in caps_rows]

    rows.append(_check_row("thresholds_closure", sub_config, "the actual bundle", thresholds_closure_failures(bundle)))
    thresholds_schema = SCHEMA_REFUSAL + "schemas/thresholds_v2.schema.json"
    threshold_rows = (
        (thresholds, "first category row removed", drop_first("categories"), thresholds_schema),
        (thresholds, "second category_id set to the first", duplicate_category, thresholds_schema),
        (thresholds, "first row's first two maxima swapped",
         lambda obj: _swap(obj["categories"][0]["maxima"], 0, 1), "refused M10V2_MAXIMA_NOT_ASCENDING"),
        (thresholds, "first row's second maximum set equal to its first", equal_maxima,
         "refused M10V2_MAXIMA_NOT_ASCENDING"),
        (thresholds, "first row's last maximum 100 to 99", _set(("categories", 0, "maxima", 3), 99),
         thresholds_schema),
        (thresholds, "first row's third maximum set to 101", _set(("categories", 0, "maxima", 2), 101),
         thresholds_schema),
        (thresholds, "first row's first maximum removed", drop_first_maximum, thresholds_schema),
    )
    rows += [_mutation_row("thresholds_closure", sub_config, mutator, *item) for item in threshold_rows]
    return rows


def identity_rows(base: Path, bundle, mutator: Mutator) -> list[Row]:
    subtasks = "HDE-SEPA007.4"
    config_bytes = (base / CONFIG_PATH).read_bytes()
    repeat, _ = admit(base)
    i1 = [] if bundle.config_sha256 == sha256_hex(config_bytes) == PROOF_CONFIG_SHA256 else ["config_sha256"]
    i2 = []
    if not (bundle.source_bundle_sha256 == magic10_v2_source_bundle_sha256(bundle.source_identities)
            == PROOF_SOURCE_BUNDLE_SHA256):
        i2.append("source_bundle_sha256")
    if repeat is None or (repeat.config_sha256, repeat.source_bundle_sha256) != (
            bundle.config_sha256, bundle.source_bundle_sha256):
        i2.append("repeat")
    mutated, refusal = mutator.admit_json("math/thresholds.json",
                                          _set(("categories", 0, "maxima"), [30, 60, 90, 100]))
    text = "harmony maxima set to 30 60 90 100 (in domain), rebound"

    def observed(field: str, proof: str) -> str:
        if mutated is None:
            return describe_refusal(refusal)
        return "admitted identity_differs" if getattr(mutated, field) != proof else "admitted identity_equal"

    label = input_label("math/thresholds.json")
    return [
        _check_row("identity", subtasks, "I-1 config_sha256 of the actual bundle", i1),
        Row("identity", subtasks, label, text, "admitted identity_differs",
            observed("config_sha256", PROOF_CONFIG_SHA256)),
        _check_row("identity", subtasks, "I-2 source_bundle_sha256 of the actual bundle", i2),
        Row("identity", subtasks, label, text, "admitted identity_differs",
            observed("source_bundle_sha256", PROOF_SOURCE_BUNDLE_SHA256)),
    ]


def is_canonical(raw: bytes) -> bool:
    try:
        return canon.sercanon(json.loads(raw), sort_keys=True) == raw
    except ValueError:
        return False


def canonical_rows(mutator: Mutator) -> list[Row]:
    rows = []
    for rel in GOVERNED:
        subtasks = ("HDE-SEPA007.1,HDE-SEPA007.3" if rel in {"catalog/centers_v1.json", "catalog/type_pairing_v1.json",
                                                             "schemas/centers_v1.schema.json",
                                                             "schemas/type_pairing_v1.schema.json"}
                    else "HDE-SEPA007.2,HDE-SEPA007.3")
        raw = (ROOT / rel).read_bytes()
        rows.append(Row("canonical_bytes", subtasks, rel, "actual", "canonical=true",
                        f"canonical={'true' if is_canonical(raw) else 'false'}"))
        pretty = (json.dumps(json.loads(raw), indent=2, sort_keys=True) + "\n").encode("utf-8")
        bundle, refusal = mutator.admit_raw(rel, pretty)
        admitted = "admitted" if bundle is not None else describe_refusal(refusal)
        rows.append(Row("canonical_bytes", subtasks, rel, "rewritten with indent 2 (same data)",
                        "canonical=false refused NONCANONICAL_JSON",
                        f"canonical={'true' if is_canonical(pretty) else 'false'} {admitted}"))
    return rows


# --- AC-08 (Implementation Audit EC-13) -------------------------------------------------------

def history_present() -> bool:
    return all(commit_present(commit) for commit in HISTORY_COMMITS)


def end_manifest_bytes() -> bytes:
    """``catalog/manifest.json`` as HDE-EPIC042 closed it (``EPIC_END``)."""

    return git("show", f"{EPIC_END}:{MANIFEST_REL}").stdout


def end_release_paths() -> tuple[str, ...]:
    """The release member paths of ``EPIC_END``'s manifest; never the tested tree's roster."""

    try:
        rows = json.loads(end_manifest_bytes())["files"]
        return tuple(row["path"] for row in rows)
    except (ValueError, KeyError, TypeError) as exc:
        raise EvidenceError(f"{EPIC_END}:{MANIFEST_REL} is not a release manifest") from exc


def prior_release_id() -> str:
    return sha256_hex(end_manifest_bytes())


def _diff_paths() -> tuple[str, ...]:
    return (MANIFEST_REL, *end_release_paths())


def ac08_unchanged(base: str, end: str) -> str:
    proc = git("diff", "--quiet", base, end, "--", *_diff_paths(), check=False)
    return "pass" if proc.returncode == 0 else f"fail rc={proc.returncode}"


def changed_paths_in_epic042() -> tuple[str, ...]:
    out = git("diff", "--name-only", PRE_DELIVERY_BASE, EPIC_END).stdout.decode("utf-8")
    return tuple(sorted(line for line in out.splitlines() if line))


def membership_in_process(paths: Sequence[str]) -> dict[str, str]:
    roster = set(end_release_paths())
    return {path: "member" if path in roster else "not-member" for path in paths}


def ac08_lines(paths: Sequence[str], membership: Mapping[str, str]) -> list[tuple[str, str]]:
    determinism = run_tool("tools/evidence/generate_determinism_gate_proofs.py", "--check").returncode
    pr01 = run_tool("tools/evidence/generate_hde_epic042_tuning_identity_hash.py", "--check").returncode
    active = load_active_mechanics_bundle()
    expected_release_id = sha256_hex((ROOT / MANIFEST_REL).read_bytes())
    prior = prior_release_id()
    identity = (active.release_id == expected_release_id and active.mechanics["config_id"] == MAGIC10_V2_CONFIG_ID
                and active.release_id != prior)
    lines = [
        ("ac08.unchanged_since_unit_base", ac08_unchanged(UNIT_BASE, UNIT_END)),
        ("ac08.unchanged_since_pre_delivery", ac08_unchanged(PRE_DELIVERY_BASE, EPIC_END)),
        ("ac08.membership.changed_since", PRE_DELIVERY_BASE),
        ("ac08.membership.count", str(len(paths))),
    ]
    lines += [(f"ac08.membership.{index}", f"{membership[path]} {path}") for index, path in enumerate(paths, 1)]
    lines += [
        ("ac08.membership", "pass" if all(membership[path] == "not-member" for path in paths) else "fail"),
        ("ac08.determinism_gate_check", "pass" if determinism == 0 else f"fail rc={determinism}"),
        ("ac08.pr01_generator_check", "pass" if pr01 == 0 else f"fail rc={pr01}"),
        ("ac08.active_release_id", active.release_id),
        ("ac08.active_config_id", str(active.mechanics["config_id"])),
        ("ac08.prior_release_id", prior),
        ("ac08.active_identity", "pass" if identity else "fail"),
    ]
    return lines


def ac08_passed(lines: Sequence[tuple[str, str]]) -> bool:
    keys = ("ac08.unchanged_since_unit_base", "ac08.unchanged_since_pre_delivery", "ac08.membership",
            "ac08.determinism_gate_check", "ac08.pr01_generator_check", "ac08.active_identity")
    values = dict(lines)
    return all(values[key] == "pass" for key in keys)


# --- the record ------------------------------------------------------------------------------

def tested_inputs_lines() -> list[tuple[str, str]]:
    return [(path, sha256_hex((ROOT / path).read_bytes())) for path in TESTED_INPUTS]


def tested_inputs_digest(pairs: Sequence[tuple[str, str]]) -> str:
    return sha256_hex("".join(f"{path} {digest}\n" for path, digest in pairs).encode("utf-8"))


def commit_tested_inputs_digest(commit: str) -> str:
    pairs = [(path, sha256_hex(git("show", f"{commit}:{path}").stdout)) for path in TESTED_INPUTS]
    return tested_inputs_digest(pairs)


COMMANDS = (
    "in-process load_magic10_v2_bundle_from_root(<temporary root>, (ManifestEntry("
    "catalog/magic10_mechanics_v2.json, <sha256 of the root's bytes>, <size>),)), once per row's root",
    "in-process evaluate_pair(fixtures/charts/alice.json, fixtures/charts/bob.json, cache=<recording cache>), "
    "resolved with source_policy local",
    "in-process strict Draft 2020-12 validation of each result instance against the admitted root's result schema",
    f"git show {EPIC_END}:{MANIFEST_REL} (the prior release: its sha256 and its member paths)",
    f"git diff --quiet {UNIT_BASE} {UNIT_END} -- {MANIFEST_REL} <the member paths of {EPIC_END}:{MANIFEST_REL}>",
    f"git diff --quiet {PRE_DELIVERY_BASE} {EPIC_END} -- {MANIFEST_REL} "
    f"<the member paths of {EPIC_END}:{MANIFEST_REL}>",
    f"git diff --name-only {PRE_DELIVERY_BASE} {EPIC_END}",
    f"in-process membership of each changed path in the member paths of {EPIC_END}:{MANIFEST_REL}",
    "python tools/evidence/generate_determinism_gate_proofs.py --check",
    "python tools/evidence/generate_hde_epic042_tuning_identity_hash.py --check",
    f"in-process load_active_mechanics_bundle(), against the sha256 of {MANIFEST_REL} and MAGIC10_V2_CONFIG_ID",
    f"python {GENERATOR_REL} --actor <run.actor>",
)


@dataclass(frozen=True)
class Evidence:
    rows: tuple[Row, ...]
    bundle_lines: tuple[tuple[str, str], ...]
    ac08: tuple[tuple[str, str], ...]
    tested: tuple[tuple[str, str], ...]

    @property
    def passed(self) -> bool:
        return all(row.passed for row in self.rows) and ac08_passed(self.ac08)


def compute_rows() -> tuple[tuple[Row, ...], tuple[tuple[str, str], ...]]:
    """Run every family on actual bundles; return the rows and the bundle identity lines."""

    results = result_instances()
    with tempfile.TemporaryDirectory(prefix="hde-epic042-pr04-") as raw:
        scratch = Path(raw)
        base = assemble(scratch / "actual")
        bundle, refusal = admit(base)
        if bundle is None:
            raise EvidenceError(f"the actual bundle was refused: {describe_refusal(refusal)}")
        mutator = Mutator(base, scratch)
        rows = (
            schema_matrix(base, mutator, results)
            + closure_rows(bundle, mutator)
            + identity_rows(base, bundle, mutator)
            + canonical_rows(mutator)
        )
        bundle_lines = [
            ("bundle.config_id", str(bundle.configuration["config_id"])),
            ("bundle.config_sha256", bundle.config_sha256),
        ]
        bundle_lines += [
            (f"bundle.source.{index}", f"{identity.path} {identity.sha256} {identity.size}")
            for index, identity in enumerate(bundle.source_identities, 1)
        ]
        bundle_lines.append(("bundle.source_bundle_sha256", bundle.source_bundle_sha256))
    return tuple(rows), tuple(bundle_lines)


def build() -> Evidence:
    rows, bundle_lines = compute_rows()
    paths = changed_paths_in_epic042()
    ac08 = ac08_lines(paths, membership_in_process(paths))
    return Evidence(rows, bundle_lines, tuple(ac08), tuple(tested_inputs_lines()))


def record_lines(evidence: Evidence, run: Mapping[str, str]) -> list[tuple[str, str]]:
    lines: list[tuple[str, str]] = [
        ("schema", SCHEMA),
        ("epic_id", "HDE-EPIC042"),
        ("task_id", "HDE-SEPA007"),
        ("subtask_id", "HDE-SEPA007.5"),
        ("evidences", "HDE-SEPA007.1, HDE-SEPA007.2, HDE-SEPA007.3, HDE-SEPA007.4"),
        ("work_unit_id", "WU-PR-04"),
        ("evidence_class", "PR evidence, not QA evidence"),
    ]
    lines += [(key, run[key]) for key in RUN_FIELDS]
    lines += [
        ("config.env", " ".join(f"{key}={os.environ.get(key, '')}" for key in ENV_PIN_KEYS)),
        ("config.jsonschema", importlib.metadata.version("jsonschema")),
        ("config.bundle_root", "temporary root: catalog/, math/ and schemas/ copied from the tested tree; "
         f"{FIXTURE_THRESHOLDS} at math/thresholds.json; {FIXTURE_CONFIG} at {CONFIG_PATH}"),
        ("config.manifest_rows", f"one ManifestEntry for {CONFIG_PATH} from the root's bytes"),
        *evidence.bundle_lines,
    ]
    for index, rel in enumerate(GOVERNED, 1):
        raw = (ROOT / rel).read_bytes()
        lines.append((f"governed.{index}", f"{rel} {sha256_hex(raw)} {len(raw)}"))
    lines += [(f"tested_input.{index}", f"{path} {digest}") for index, (path, digest) in enumerate(evidence.tested, 1)]
    lines += [
        ("tested_inputs.count", str(len(evidence.tested))),
        ("tested_inputs.sha256", tested_inputs_digest(evidence.tested)),
    ]
    lines += [(f"command.{index}", text) for index, text in enumerate(COMMANDS, 1)]
    lines += [(f"row.{index:04d}", row.line()) for index, row in enumerate(evidence.rows, 1)]
    families: dict[str, int] = {}
    for row in evidence.rows:
        families[row.family] = families.get(row.family, 0) + 1
    lines += [
        ("rows.total", str(len(evidence.rows))),
        ("rows.passed", str(sum(row.passed for row in evidence.rows))),
        *((f"rows.{family}", str(count)) for family, count in families.items()),
    ]
    lines += list(evidence.ac08)
    lines += [(f"limitation.{index}", text) for index, text in enumerate(LIMITATIONS, 1)]
    lines.append(("status", "PASS" if evidence.passed else "FAIL"))
    return lines


def render(lines: Sequence[tuple[str, str]]) -> bytes:
    return "".join(f"{key}: {value}\n" for key, value in lines).encode("utf-8")


def parse_record(data: bytes) -> list[tuple[str, str]]:
    parsed = []
    for line in data.decode("utf-8").split("\n")[:-1]:
        key, separator, value = line.partition(": ")
        if not separator:
            raise EvidenceError("record line without a key")
        parsed.append((key, value))
    return parsed


def valid_actor(actor: str) -> bool:
    return 0 < len(actor) <= 200 and actor.isprintable() and actor == actor.strip()


# --- modes -----------------------------------------------------------------------------------

def write(actor: str) -> bytes:
    if not valid_actor(actor):
        raise SystemExit("V2_CONTRACT_EVIDENCE_INVALID_ACTOR")
    if not tree_is_clean():
        raise SystemExit(DIRTY_EXIT)
    if not history_present():
        raise SystemExit(HISTORY_EXIT)
    run = {
        "run.tested_commit": head_commit(),
        "run.time_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "run.actor": actor,
        "run.python": platform.python_version(),
    }
    evidence = build()
    if not evidence.passed:
        failing = [row.line() for row in evidence.rows if not row.passed]
        failing += [f"{key}: {value}" for key, value in evidence.ac08 if value.startswith("fail")]
        for line in failing:
            print(line, file=sys.stderr)
        raise SystemExit(f"{FAILED_EXIT}:{len(failing)}")
    record = render(record_lines(evidence, run))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(record)
    return record


def _run_fields_valid(run: Mapping[str, str]) -> str | None:
    if _HEX40.fullmatch(run.get("run.tested_commit", "")) is None:
        return "run.tested_commit"
    if _TIME.fullmatch(run.get("run.time_utc", "")) is None:
        return "run.time_utc"
    if not valid_actor(run.get("run.actor", "")):
        return "run.actor"
    if _PYTHON.fullmatch(run.get("run.python", "")) is None:
        return "run.python"
    return None


def check() -> str:
    if not OUT.is_file():
        raise SystemExit(f"DRIFT:{OUT_REL}:missing")
    stored = OUT.read_bytes()
    try:
        parsed = parse_record(stored)
    except (EvidenceError, UnicodeDecodeError):
        raise SystemExit(f"DRIFT:{OUT_REL}:layout") from None
    keys = [key for key, _ in parsed]
    run = {key: value for key, value in parsed if key in RUN_FIELDS}
    if keys[7:11] != list(RUN_FIELDS) or len(run) != len(RUN_FIELDS):
        raise SystemExit(f"DRIFT:{OUT_REL}:run")
    bad = _run_fields_valid(run)
    if bad:
        raise SystemExit(f"DRIFT:{OUT_REL}:{bad}")
    if not history_present():
        raise SystemExit(HISTORY_EXIT)
    evidence = build()
    expected = record_lines(evidence, run)
    for (want_key, want), (have_key, have) in zip(expected, parsed):
        if (want_key, want) != (have_key, have):
            raise SystemExit(f"DRIFT:{OUT_REL}:{want_key}")
    if render(expected) != stored:
        raise SystemExit(f"DRIFT:{OUT_REL}:layout")
    commit = run["run.tested_commit"]
    if not commit_present(commit):
        return "absent"
    if commit_tested_inputs_digest(commit) != dict(parsed)["tested_inputs.sha256"]:
        raise SystemExit(f"DRIFT:{OUT_REL}:tested_commit_inputs")
    committed = dt.datetime.fromisoformat(git("show", "-s", "--format=%cI", commit).stdout.decode().strip())
    ran = dt.datetime.strptime(run["run.time_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
    if ran < committed:
        raise SystemExit(f"DRIFT:{OUT_REL}:run.time_utc")
    return "present"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--actor", help="the responsible actor of this run; writes the record")
    mode.add_argument("--check", action="store_true", help="compare the stored record with recomputation; write nothing")
    args = parser.parse_args(argv)
    ensure_determinism_env()
    try:
        if args.check:
            state = check()
            print(f"v2 contract evidence check ok (tested commit {state})")
            return
        write(args.actor)
    except EvidenceError as exc:
        raise SystemExit(f"{FAILED_EXIT}:{exc}") from None
    print("v2 contract evidence written")


if __name__ == "__main__":
    main()
