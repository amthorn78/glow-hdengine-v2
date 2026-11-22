#!/usr/bin/env python3
"""Magic-10 v2 integration goldens and parity evidence (HDE-EPIC043 WU-PR-12; HDE-CONJ010.6).

The writer records one governed record,
``audit/qa/hde-epic043/pr-12/v2_integration_evidence.txt``, proving eight proof
classes on the admitted v2 release at the head:

1. full matrix: the complete intrinsic result of every pair of the pinned
   reference corpus, its digest, and its band counts against the frozen
   baseline;
2. AB/BA and two-run identity, over the corpus, the surface set and the golden
   collection;
3. pair and cache identity: each ``pair_key`` rebuilt from the HDE Math Spec
   preimage, the ``magic10:v2:`` cache key, and distinctness from the prior
   release's v1 identity;
4. UID-independence: equal Gate masks under other user IDs give the same
   intrinsic bytes and ``pair_key``;
5. result schema: every result validated against both release-member schemas,
   and malformed results refused;
6. Reader projection: the Reader v1 and v2 projections of v2 results, bands
   only and numeric-free, against their schemas and the Reader goldens;
7. failure tokens: each request-reachable refusal at three surfaces against
   the CLI/API canon's Magic10 failure table, with the Gate-data disagreement
   disclosed;
8. internal parity: ``hdctl showcompat --pair-file``, the dev compat HTTP
   handler, ``evaluate_pair`` and the Reader projection agree byte for byte.

It also discloses the baseline failures of six existing tools under closed
rails, and names the live parts (HDE-COAG003.8 and .9) as deferred.

The record names its tested state by the SHA-256 and size of each tested input
and one digest over them; it carries no git state, and the PR result maps that
digest to the tested commit.  It also names the responsible actor, the run time
and the interpreter.  ``--check`` compares the tested inputs first, then
re-derives every class and compares the bytes; it checks the three run fields
for shape only, so it is byte-stable and writes nothing.  A failing check is a
named refusal and nothing is written.  It runs only under the closed
determinism rails, with ``APP_ENV`` ``dev``, ``test`` or ``local``, from the
repository root.  No vendor, network or database call is made.
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
import uuid
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import jsonschema  # noqa: E402
from jsonschema import validators  # noqa: E402

from engine.config.magic10_v2_loader import (  # noqa: E402
    MAGIC10_V2_CONFIG_ID,
    MAGIC10_V2_INTRINSIC_CACHE_PREFIX,
    magic10_v2_intrinsic_cache_key,
)
from engine.config.registry_loader import (  # noqa: E402
    RegistryConfigError,
    _load_active_mechanics_bundle_from_root,
)
from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env  # noqa: E402
from engine.serializer.canon import sercanon  # noqa: E402

OUT_REL = "audit/qa/hde-epic043/pr-12/v2_integration_evidence.txt"
SCHEMA = "hde_epic043_v2_integration_evidence.v1"
GENERATOR_REL = "tools/evidence/generate_hde_epic043_v2_integration_evidence.py"

MANIFEST_REL = "catalog/manifest.json"
CORPUS_REL = "tools/score_distribution/reference_corpus_v1.json"
BASELINE_REL = "tools/score_distribution/reference_baseline_v1.json"
GOLDENS_REL = "tests/fixtures/magic10/v2/goldens.json"
TOKEN_MAP_REL = "errors/token_map/token_map.json"
RESULT_SCHEMA_REL = "schemas/magic10_result_v2.schema.json"
COMPAT_SCHEMA_REL = "schemas/magic10_compat_result_v2.schema.json"
READER_V1_SCHEMA_REL = "schemas/reader.v1.schema.json"
READER_V2_SCHEMA_REL = "schemas/reader.v2.schema.json"

# The Reader goldens this record reproduces from v2 results (the projection goldens
# whose selection a declared v2 result yields; HDE Math Spec §9.5, Reader v1 and v2).
READER_V1_BAND_GOLDENS = (
    ("Open", "goldens/reader/v1/g03_harmony_open.json"),
    ("Warm", "goldens/reader/v1/g04_harmony_warm.json"),
    ("Cool", "goldens/reader/v1/g05_harmony_cool.json"),
    ("Glow", "goldens/reader/v1/g07_harmony_glow.json"),
)
READER_V1_ABBA_GOLDENS = (
    "goldens/reader/v1/g02_ab_ba_parity_A.jsonl",
    "goldens/reader/v1/g02_ab_ba_parity_B.jsonl",
)
READER_V1_INELIGIBLE_GOLDEN = "goldens/reader/v1/g01_minimal_ineligible.json"
READER_V2_INELIGIBLE_GOLDEN = "goldens/reader/v2/g01_ineligible.json"
READER_GOLDEN_META = {"engine_tag": "Isis5", "invocation_tag": "INV-000000"}
READER_GOLDEN_RELEASE_ID = "a" * 64

# The six Audit P-10 tools that refuse under closed rails (identically on main
# 26158fcb).  (path, arguments, declared exit, declared refusal, cause, run here)
BASELINE_FAILURES = (
    (
        "tools/presenter/generate_presenter_artifacts.py", ("--check",), 1,
        "showcompat ab failed: rc=1, stderr=b'PROVIDER_REFUSED\\n'",
        "it drives showcompat with birth arguments, which need a chart provider that closed rails refuse (Audit M-5)",
        True,
    ),
    (
        "tools/cli/generate_showcompat_parity_artifacts.py", ("--check",), 1,
        "showcompat ab failed: rc=1, stderr=b'PROVIDER_REFUSED\\n'",
        "it drives showcompat with birth arguments, which need a chart provider that closed rails refuse",
        True,
    ),
    (
        "tools/evidence/run_showcompat_artifacts.py", ("--check",), 1,
        "showcompat failed (rc=1): ERR_M10_LEGACY_INPUT_UNSUPPORTED",
        "it sends birth-only stdin parties, which showcompat refuses as legacy input",
        False,
    ),
    (
        "scripts/cli/canonical_harness.py", (), 1,
        "showcompat failed during harness",
        "it sends birth-only stdin parties, which showcompat refuses as legacy input",
        False,
    ),
    (
        "scripts/validate/public_bytes_check.py", (), 1,
        "CalledProcessError",
        "it calls showcompat with flags hdctl no longer has (--birthdate --birthtime --place --tz ...), refused with exit 64",
        True,
    ),
    (
        "scripts/validate/sidecar_check.py", (), 2,
        "unrecognized arguments",
        "it calls showcompat with flags hdctl no longer has (--birthdate ... --showmath --admin-out --admin)",
        True,
    ),
)
NOT_RUN_OBSERVATION = (
    "not run by this writer: it writes into the repository (its QA log and path proof, or its artifacts); "
    "measured by the WU-PR-12 PR-30 session in a throwaway worktree at the tested inputs"
)

TESTED_INPUTS = (
    MANIFEST_REL,
    CORPUS_REL,
    BASELINE_REL,
    GOLDENS_REL,
    READER_V1_INELIGIBLE_GOLDEN,
    *READER_V1_ABBA_GOLDENS,
    *(path for _band, path in READER_V1_BAND_GOLDENS),
    READER_V2_INELIGIBLE_GOLDEN,
    "tools/score_distribution/score_distribution.py",
    "tools/config/artifacts.py",
    "scripts/hdctl.py",
    *(row[0] for row in BASELINE_FAILURES),
    GENERATOR_REL,
)

BANDS = ("Cool", "Open", "Warm", "Glow")
V2_RESULT_SCHEMA = "magic10_result.v2"
V2_COMPAT_SCHEMA = "magic10_compat_result.v2"
# The prior identity on main 26158fcb (release 1.3.0): its configuration, its
# release_id (the cut record's release.prior_release_id) and its result schema.
V1_CONFIG_ID = "m10-channel-state-v1.0.0"
V1_RESULT_SCHEMA = "magic10_result.v1"
V1_CACHE_PREFIX = "magic10:v1:"
PRIOR_RELEASE_ID = "2d5a4ec485fde5dd51004e0286fff1cb1211e4ee79fa71bc62b2a5ecd0b6c129"
DEV_APP_ENVS = ("dev", "test", "local")
UID_NAMESPACE = "hde-epic043/wu-pr-12/uid"
UID_VARIANTS = ("variant_1", "variant_2")
SURFACE_GOLDEN_PARTIES = ("M10-G005.pair_1", "M10-G005.pair_2", "M10-G007", "M10-G008")
HTTP_CONTENT_TYPE = "application/json; charset=utf-8"

# Failure-token rows: the request-reachable conditions of the CLI/API canon's Magic10
# failure table (HDE CLI, API and Vendor Ref §5.2.3) for an internal or CLI input.
# (row, input, governed token, governed status, observed token, disclosed cause)
GATE_DATA_CAUSE = (
    "BOUNDARY_REASONS in engine/compat/error_tokens.py (a release member, since HDE-EPIC040-PR04) maps "
    "gates_missing to ERR_READER_MISSING_PARAM and gates_invalid to ERR_READER_INVALID_CHART on the "
    "application surfaces; the CLI/API canon names ERR_M10_GATES_MISSING and ERR_M10_GATES_INVALID (422) "
    "for an internal or CLI complete-chart input; not fixed here (a release-member change)"
)
FAILURE_ROWS = (
    ("FT-1", "legacy birth-only party", "ERR_M10_LEGACY_INPUT_UNSUPPORTED", 422, "ERR_M10_LEGACY_INPUT_UNSUPPORTED", None),
    ("FT-2", "legacy ID-only party", "ERR_M10_LEGACY_INPUT_UNSUPPORTED", 422, "ERR_M10_LEGACY_INPUT_UNSUPPORTED", None),
    ("FT-3", "complete chart with no gates key", "ERR_M10_GATES_MISSING", 422, "ERR_READER_MISSING_PARAM", GATE_DATA_CAUSE),
    ("FT-4", "complete chart with an empty Gate array", "ERR_M10_GATES_MISSING", 422, "ERR_READER_MISSING_PARAM", GATE_DATA_CAUSE),
    ("FT-5", "Gate 65", "ERR_M10_GATES_INVALID", 422, "ERR_READER_INVALID_CHART", GATE_DATA_CAUSE),
    ("FT-6", "a duplicate Gate", "ERR_M10_GATES_INVALID", 422, "ERR_READER_INVALID_CHART", GATE_DATA_CAUSE),
    ("FT-7", "a non-integer Gate", "ERR_M10_GATES_INVALID", 422, "ERR_READER_INVALID_CHART", GATE_DATA_CAUSE),
    ("FT-8", "the same UUID with unequal complete projections", "ERR_READER_INVALID_CHART", 422, "ERR_READER_INVALID_CHART", None),
)
FAILURE_PARTY_A_UID = "00000000-0000-0000-0000-000000000001"
FAILURE_PARTY_B_UID = "00000000-0000-0000-0000-000000000002"

DEFERRED = (
    ("HDE-COAG003.8", "live current-row Gate readiness: DEFERRED; not represented as achieved (C-09)"),
    ("HDE-COAG003.9", "live DB Reader success: DEFERRED; not represented as achieved (C-09)"),
)
LIMITATIONS = (
    "no live run: no production, vendor, database or network access; the live parts are DEFERRED",
    "interpreter: run.python locally; hosted CI's interpreter may differ",
    "evidence of the tested inputs named above only; a later state must pass --check (RK-11, WU-PR-13)",
    "cache identity is the key and its preimage; no production surface passes an intrinsic cache to evaluate_pair",
    "failure tokens: the request-reachable conditions only; the configuration, manifest, result-schema, "
    "stale-result and stored-row tokens are pinned by tests/cli/test_errors_parity.py, "
    "tests/http/test_compat_endpoint_contract.py and tests/m10_v2/test_*_refusals.py",
    "Reader v2 g02 and g03 (a band vector no declared v2 result yields) and the Reader-route error goldens "
    "stay with tests/reader_v1/test_goldens.py",
    "internal HTTP is the dev app; the selected factory and WSGI apps are pinned to it by "
    "tests/adapter/test_compat_http_parity.py",
    "establishes no QA verdict, acceptance, PF09 movement, Ops, deployment or closure",
)
RUN_FIELDS = ("run.time_utc", "run.actor", "run.python")
_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
_PYTHON = re.compile(r"\d+\.\d+\.\d+")

_PREFIX = "V2_INTEGRATION_EVIDENCE_"
RAILS_NOT_CLOSED = _PREFIX + "RAILS_NOT_CLOSED"
APP_ENV_NOT_DEV = _PREFIX + "APP_ENV_NOT_DEV"
WORKING_DIRECTORY_INVALID = _PREFIX + "WORKING_DIRECTORY_INVALID"
TEMP_DIRECTORY_INSIDE_REPOSITORY = _PREFIX + "TEMP_DIRECTORY_INSIDE_REPOSITORY"
INVALID_ACTOR = _PREFIX + "INVALID_ACTOR"
INPUT_UNREADABLE = _PREFIX + "INPUT_UNREADABLE"
RELEASE_REFUSED = _PREFIX + "RELEASE_REFUSED"
NOT_ADMITTED_V2_PATH = _PREFIX + "NOT_ADMITTED_V2_PATH"
CORPUS_INVALID = _PREFIX + "CORPUS_INVALID"
MATRIX_INCOMPLETE = _PREFIX + "MATRIX_INCOMPLETE"
MATRIX_BASELINE_MISMATCH = _PREFIX + "MATRIX_BASELINE_MISMATCH"
ABBA_MISMATCH = _PREFIX + "ABBA_MISMATCH"
TWO_RUN_MISMATCH = _PREFIX + "TWO_RUN_MISMATCH"
PAIR_KEY_MISMATCH = _PREFIX + "PAIR_KEY_MISMATCH"
CACHE_KEY_MISMATCH = _PREFIX + "CACHE_KEY_MISMATCH"
IDENTITY_NOT_DISTINCT = _PREFIX + "IDENTITY_NOT_DISTINCT"
UID_DEPENDENT = _PREFIX + "UID_DEPENDENT"
RESULT_SCHEMA_REFUSED = _PREFIX + "RESULT_SCHEMA_REFUSED"
SCHEMA_ADVERSE_ACCEPTED = _PREFIX + "SCHEMA_ADVERSE_ACCEPTED"
READER_MISMATCH = _PREFIX + "READER_MISMATCH"
READER_GOLDEN_MISMATCH = _PREFIX + "READER_GOLDEN_MISMATCH"
GOLDEN_MISMATCH = _PREFIX + "GOLDEN_MISMATCH"
FAILURE_TOKEN_MISMATCH = _PREFIX + "FAILURE_TOKEN_MISMATCH"
PARITY_MISMATCH = _PREFIX + "PARITY_MISMATCH"
BASELINE_FAILURE_CHANGED = _PREFIX + "BASELINE_FAILURE_CHANGED"
RECORD_INVALID = _PREFIX + "RECORD_INVALID"


class IntegrationEvidenceRefusal(RuntimeError):
    """A named refusal: no record is written."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


# --- small helpers -----------------------------------------------------------------------------

def out_path() -> Path:
    return ROOT / OUT_REL


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(value: object) -> str:
    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def canonical(value: object) -> bytes:
    return sercanon(value, sort_keys=True)


def valid_actor(actor: str) -> bool:
    """The HDE-SEPA007.5 writer's actor rule."""

    return 0 < len(actor) <= 200 and actor.isprintable() and actor == actor.strip()


def read_input(rel: str) -> bytes:
    try:
        return (ROOT / rel).read_bytes()
    except OSError:
        raise IntegrationEvidenceRefusal(f"{INPUT_UNREADABLE}:{rel}") from None


def read_json(rel: str) -> Any:
    try:
        return json.loads(read_input(rel).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise IntegrationEvidenceRefusal(f"{INPUT_UNREADABLE}:{rel}") from None


def json_numbers(value: object) -> int:
    """The count of JSON number values (not booleans) in a parsed document."""

    if isinstance(value, bool):
        return 0
    if isinstance(value, (int, float)):
        return 1
    if isinstance(value, dict):
        return sum(json_numbers(item) for item in value.values())
    if isinstance(value, list):
        return sum(json_numbers(item) for item in value)
    return 0


def child_env() -> dict[str, str]:
    environ = os.environ.copy()
    environ.update({"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    return environ


def strict_validator(rel: str):
    """A Draft 2020-12 validator over the committed schema bytes, with strict integers."""

    schema = json.loads((ROOT / rel).read_bytes().decode("utf-8"))
    strict = validators.extend(
        jsonschema.Draft202012Validator,
        type_checker=jsonschema.Draft202012Validator.TYPE_CHECKER.redefine(
            "integer", lambda checker, value: type(value) is int
        ),
    )
    strict.check_schema(schema)
    return strict(schema)


def reader_validator(rel: str):
    schema = json.loads((ROOT / rel).read_bytes().decode("utf-8"))
    cls = jsonschema.validators.validator_for(schema)
    cls.check_schema(schema)
    return cls(schema)


# --- seams (the owner test replaces these over a reduced set) -----------------------------------

def load_root_bundle():
    return _load_active_mechanics_bundle_from_root(ROOT)


def corpus() -> tuple[str, list[dict[str, Any]], list[list[int]]]:
    """The pinned reference corpus: (digest, people, pairs), refused unless its pin holds."""

    from tools.score_distribution import score_distribution

    try:
        return score_distribution.load_corpus()
    except score_distribution.Refusal as exc:
        raise IntegrationEvidenceRefusal(f"{CORPUS_INVALID}:{exc.code}") from None


def baseline_counts(bundle, corpus_sha256: str) -> tuple[dict[str, int], dict[str, dict[str, int]]]:
    """The frozen baseline's band counts, refused unless it binds this corpus and release."""

    baseline = read_json(BASELINE_REL)
    release = baseline.get("release") if isinstance(baseline, dict) else None
    expected_release = {"release_id": bundle.release_id, "version": bundle.manifest.version,
                        "config_id": bundle.mechanics["config_id"]}
    if release != expected_release:
        raise IntegrationEvidenceRefusal(f"{MATRIX_BASELINE_MISMATCH}:release")
    if baseline.get("corpus_sha256") != corpus_sha256:
        raise IntegrationEvidenceRefusal(f"{MATRIX_BASELINE_MISMATCH}:corpus")
    counts = baseline["band_counts"]
    return dict(counts["overall"]), {key: dict(value) for key, value in counts["per_category"].items()}


def evaluate(left, right, bundle) -> dict[str, Any]:
    """``evaluate_pair`` with the once-admitted bundle as its provider (P-08)."""

    from engine.compat.compute import evaluate_pair

    return evaluate_pair(left, right, bundle_provider=lambda: bundle)


def compare_goldens_at_root():
    from tools.config.artifacts import compare_goldens

    return compare_goldens(ROOT)


def run_cli(arguments: Sequence[str]) -> subprocess.CompletedProcess:
    """``python scripts/hdctl.py <arguments>`` from the repository root."""

    return subprocess.run([sys.executable, "scripts/hdctl.py", *arguments], cwd=ROOT, env=child_env(),
                          capture_output=True)


def http_client():
    """A test client of the dev app (``adapter.http_reader.create_app``)."""

    from adapter.http_reader import create_app

    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def run_tool(path: str, arguments: Sequence[str]) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, path, *arguments], cwd=ROOT, env=child_env(),
                          capture_output=True, timeout=600)


# --- preconditions and admission ------------------------------------------------------------------

def preconditions() -> None:
    try:
        ensure_determinism_env()
    except DeterminismEnvError:
        raise IntegrationEvidenceRefusal(RAILS_NOT_CLOSED) from None
    if os.environ.get("APP_ENV") not in DEV_APP_ENVS:
        raise IntegrationEvidenceRefusal(APP_ENV_NOT_DEV)
    try:
        here = Path.cwd().resolve()
    except OSError:
        raise IntegrationEvidenceRefusal(WORKING_DIRECTORY_INVALID) from None
    if here != ROOT.resolve():
        raise IntegrationEvidenceRefusal(WORKING_DIRECTORY_INVALID)


def admit():
    """The admitted v2 bundle at the repository root, or a named refusal."""

    try:
        bundle = load_root_bundle()
    except RegistryConfigError as exc:
        raise IntegrationEvidenceRefusal(f"{RELEASE_REFUSED}:{exc.code}") from None
    if (bundle.mechanics.get("config_id") != MAGIC10_V2_CONFIG_ID
            or bundle.mechanics.get("result_schema") != V2_RESULT_SCHEMA
            or bundle.release_id != sha256_hex(read_input(MANIFEST_REL))):
        raise IntegrationEvidenceRefusal(f"{NOT_ADMITTED_V2_PATH}:release")
    return bundle


def require_v2(value: Mapping[str, Any], bundle, where: str) -> None:
    """Every value a class reads carries the admitted release and the v2 configuration."""

    if (not isinstance(value, Mapping) or value.get("release_id") != bundle.release_id
            or value.get("config_id") != bundle.mechanics["config_id"]
            or value.get("schema") != V2_COMPAT_SCHEMA):
        raise IntegrationEvidenceRefusal(f"{NOT_ADMITTED_V2_PATH}:{where}")


# --- identities (HDE Math Spec §5.2.2) ------------------------------------------------------------

def chart_fingerprint(mask_hex: str) -> str:
    return sha256_hex(canonical({"schema": "magic10_chart_fingerprint.v1", "gate_mask_hex": mask_hex}))


def pair_key_for(party_a, party_b, *, config_id: str, release_id: str, result_schema: str) -> str:
    members = sorted((party_a, party_b), key=lambda party: party.gates.mask)
    return sha256_hex(canonical({
        "schema": "magic10_pair_preimage.v1",
        "members": [chart_fingerprint(member.gates.mask_hex) for member in members],
        "config_id": config_id,
        "release_id": release_id,
        "result_schema": result_schema,
    }))


def intrinsic(value: Mapping[str, Any]) -> dict[str, Any]:
    """The ``magic10_result.v2`` projection of one compat value."""

    return {
        "schema": V2_RESULT_SCHEMA,
        "config_id": value["config_id"],
        "release_id": value["release_id"],
        "pair_key": value["pair_key"],
        "signals": [{"signal_id": row["signal_id"], "q": row["q"]} for row in value["signals"]],
        "categories": [{"category_id": row["category_id"], "score": row["score"], "band": row["band"]}
                       for row in value["categories"]],
    }


def complete(value: Mapping[str, Any], signal_order: Sequence[str], category_order: Sequence[str]) -> bool:
    signals, categories = value.get("signals"), value.get("categories")
    return (isinstance(signals, list) and isinstance(categories, list)
            and [row.get("signal_id") for row in signals] == list(signal_order)
            and [row.get("category_id") for row in categories] == list(category_order))


def adverse_variants(value: Mapping[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    """Five malformed variants of one valid result (instruction §4: a malformed result is refused)."""

    def mutate(change: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
        copy = json.loads(json.dumps(value))
        change(copy)
        return copy

    return [
        ("score_101", mutate(lambda doc: doc["categories"][0].__setitem__("score", 101))),
        ("band_hot", mutate(lambda doc: doc["categories"][0].__setitem__("band", "Hot"))),
        ("signal_missing", mutate(lambda doc: doc["signals"].pop())),
        ("extra_key", mutate(lambda doc: doc.__setitem__("extra", "x"))),
        ("bool_score", mutate(lambda doc: doc["categories"][0].__setitem__("score", True))),
    ]


# --- sets ---------------------------------------------------------------------------------------

def complete_chart(fields: Mapping[str, Any], person_uid: str, gates: Sequence[object]) -> dict[str, Any]:
    """A complete mapped chart: the golden collection's synthetic projection fields, Gates and identity."""

    bodygraph = json.loads(json.dumps(dict(fields)))
    bodygraph["gates"] = list(gates)
    return {"bodygraph": bodygraph, "person": {"person_uid": person_uid}, "person_uid": person_uid}


def golden_parties(goldens: Mapping[str, Any]) -> list[tuple[str, tuple, tuple]]:
    """The golden application parties of the surface set: (label, (uid, gates), (uid, gates))."""

    cases = {case["case_id"]: case for case in goldens["cases"]}
    parties = []
    for pair in cases["M10-G005"]["inputs"]["pairs"]:
        parties.append((f"M10-G005.{pair['pair_id']}", (pair["a"]["person_uid"], pair["a"]["gates"]),
                        (pair["b"]["person_uid"], pair["b"]["gates"])))
    for case_id in ("M10-G007", "M10-G008"):
        inputs = cases[case_id]["inputs"]
        parties.append((case_id, (inputs["a"]["person_uid"], inputs["a"]["gates"]),
                        (inputs["b"]["person_uid"], inputs["b"]["gates"])))
    if [label for label, _a, _b in parties] != list(SURFACE_GOLDEN_PARTIES):
        raise IntegrationEvidenceRefusal(f"{INPUT_UNREADABLE}:{GOLDENS_REL}")
    return parties


def variant_uid(label: str, variant: str, side: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{UID_NAMESPACE}/{label}/{variant}/{side}"))


# --- the corpus classes (1, 2, 3 and 5) ---------------------------------------------------------

def corpus_classes(bundle) -> tuple[list[tuple[str, str]], list[int], dict[str, Any]]:
    from engine.compat.compute import INTRINSIC_CACHE_PREFIX
    from tools.score_distribution.score_distribution import reference_party

    digest, people, pairs = corpus()
    parties = [reference_party(person) for person in people]
    registry = bundle.registry
    category_order = list(registry.magic10_order)
    signal_order = [signal for category in category_order for signal in registry.magic10_caps[category].inputs]
    result_validator = strict_validator(RESULT_SCHEMA_REL)
    compat_validator = strict_validator(COMPAT_SCHEMA_REL)
    overall = {band: 0 for band in BANDS}
    per_category = {category: {band: 0 for band in BANDS} for category in category_order}
    first: dict[tuple[str, str], int] = {}
    matrix = hashlib.sha256()
    pair_keys: set[str] = set()
    mask_pairs: set[tuple[int, int]] = set()
    first_value: dict[str, Any] | None = None
    for index, (a, b) in enumerate(pairs):
        label = f"corpus[{index}]"
        ab = evaluate(parties[a], parties[b], bundle)
        ba = evaluate(parties[b], parties[a], bundle)
        for value in (ab, ba):
            require_v2(value, bundle, "full_matrix")
            if not complete(value, signal_order, category_order):
                raise IntegrationEvidenceRefusal(MATRIX_INCOMPLETE)
        ab_bytes = canonical(ab)
        if ab_bytes != canonical(ba):
            raise IntegrationEvidenceRefusal(f"{ABBA_MISMATCH}:{label}")
        projection = intrinsic(ab)
        try:
            result_validator.validate(projection)
        except jsonschema.ValidationError:
            raise IntegrationEvidenceRefusal(f"{RESULT_SCHEMA_REFUSED}:{RESULT_SCHEMA_REL}") from None
        try:
            compat_validator.validate(ab)
        except jsonschema.ValidationError:
            raise IntegrationEvidenceRefusal(f"{RESULT_SCHEMA_REFUSED}:{COMPAT_SCHEMA_REL}") from None
        pair_key = ab["pair_key"]
        expected_key = pair_key_for(parties[a], parties[b], config_id=bundle.mechanics["config_id"],
                                    release_id=bundle.release_id, result_schema=V2_RESULT_SCHEMA)
        if pair_key != expected_key:
            raise IntegrationEvidenceRefusal(PAIR_KEY_MISMATCH)
        cache_key = magic10_v2_intrinsic_cache_key(pair_key)
        if cache_key != "magic10:v2:" + pair_key or cache_key != INTRINSIC_CACHE_PREFIX + pair_key:
            raise IntegrationEvidenceRefusal(CACHE_KEY_MISMATCH)
        v1_key = pair_key_for(parties[a], parties[b], config_id=V1_CONFIG_ID, release_id=PRIOR_RELEASE_ID,
                              result_schema=V1_RESULT_SCHEMA)
        if v1_key == pair_key or V1_CACHE_PREFIX + v1_key == cache_key:
            raise IntegrationEvidenceRefusal(IDENTITY_NOT_DISTINCT)
        pair_keys.add(pair_key)
        mask_pairs.add(tuple(sorted((parties[a].gates.mask, parties[b].gates.mask))))
        matrix.update(canonical(projection) + b"\n")
        for row in ab["categories"]:
            overall[row["band"]] += 1
            per_category[row["category_id"]][row["band"]] += 1
            first.setdefault((row["category_id"], row["band"]), index)
        if first_value is None:
            first_value = ab
    if not pairs or first_value is None:
        raise IntegrationEvidenceRefusal(MATRIX_INCOMPLETE)
    if len(pair_keys) != len(mask_pairs):
        raise IntegrationEvidenceRefusal(f"{IDENTITY_NOT_DISTINCT}:collision")
    expected_overall, expected_per_category = baseline_counts(bundle, digest)
    for category in category_order:
        if per_category[category] != expected_per_category.get(category):
            raise IntegrationEvidenceRefusal(f"{MATRIX_BASELINE_MISMATCH}:{category}")
    if overall != expected_overall:
        raise IntegrationEvidenceRefusal(f"{MATRIX_BASELINE_MISMATCH}:overall")
    adverse = []
    for rel, validator, document in ((RESULT_SCHEMA_REL, result_validator, intrinsic(first_value)),
                                     (COMPAT_SCHEMA_REL, compat_validator, first_value)):
        for variant, mutated in adverse_variants(document):
            if validator.is_valid(mutated):
                raise IntegrationEvidenceRefusal(f"{SCHEMA_ADVERSE_ACCEPTED}:{rel}:{variant}")
            adverse.append(f"{rel}:{variant}")
    count = str(len(pairs))
    lines: list[tuple[str, str]] = [
        ("set.corpus.path", CORPUS_REL),
        ("set.corpus.sha256", digest),
        ("set.corpus.people", str(len(people))),
        ("set.corpus.pairs", count),
        ("class.full_matrix.owning_source", "HDE Math Spec §5.2 and §9.5"),
        ("class.full_matrix.entrypoint", "engine.compat.compute.evaluate_pair, the once-admitted bundle as bundle_provider"),
        ("class.full_matrix.set", "corpus"),
        ("class.full_matrix.pairs", count),
        ("class.full_matrix.results_complete", count),
        ("class.full_matrix.result_fields", "schema,config_id,release_id,pair_key,signals(20),categories(10: category_id,score,band)"),
        ("class.full_matrix.matrix_sha256", matrix.hexdigest()),
        ("class.full_matrix.band_counts.overall", compact(overall)),
        *((f"class.full_matrix.band_counts.{category}", compact(per_category[category])) for category in category_order),
        ("class.full_matrix.baseline.path", BASELINE_REL),
        ("class.full_matrix.baseline.release_id", bundle.release_id),
        ("class.full_matrix.baseline.equal", "true"),
        ("class.full_matrix.result", "PASS"),
    ]
    corpus_facts = {
        "pairs": count,
        "distinct_pair_keys": str(len(pair_keys)),
        "distinct_mask_pairs": str(len(mask_pairs)),
        "adverse": adverse,
        "people": people,
        "pairs_list": pairs,
    }
    surface_indices = sorted(set(first.values()))
    return lines, surface_indices, corpus_facts


# --- the surface classes (2, 3, 4, 6 and 8) ----------------------------------------------------

def surface_pairs(goldens: Mapping[str, Any], people: Sequence[Mapping[str, Any]], pairs: Sequence[Sequence[int]],
                  surface_indices: Sequence[int]) -> list[tuple[str, dict[str, Any], dict[str, Any]]]:
    fields = goldens["constants"]["synthetic_projection_fields"]
    rows = []
    for index in surface_indices:
        a, b = pairs[index]
        rows.append((f"corpus[{index}]", complete_chart(fields, people[a]["id"], people[a]["gates"]),
                     complete_chart(fields, people[b]["id"], people[b]["gates"])))
    for label, (uid_a, gates_a), (uid_b, gates_b) in golden_parties(goldens):
        rows.append((label, complete_chart(fields, uid_a, gates_a), complete_chart(fields, uid_b, gates_b)))
    return rows


def resolved_party(chart: Mapping[str, Any]):
    from engine.bodygraph.resolver import resolve_compat_chart
    from engine.compat.compute import evaluation_party

    return evaluation_party(resolve_compat_chart(dict(chart), source_policy="local", env=None))


def viewer_prefs() -> dict[str, Any]:
    from engine.compat.categories import CATEGORIES_ORDER_V1

    return {"top_category": CATEGORIES_ORDER_V1[0], "weights": {category: 10 for category in CATEGORIES_ORDER_V1}}


def post_compat(client, body: Mapping[str, Any]):
    return client.post("/api/compat/v1", data=json.dumps(body, sort_keys=True),
                       headers={"Content-Type": HTTP_CONTENT_TYPE})


def surface_classes(bundle, goldens: Mapping[str, Any], corpus_facts: Mapping[str, Any],
                    surface_indices: Sequence[int], workdir: Path) -> tuple[list[tuple[str, str]], dict[str, Any]]:
    from engine.compat.compute import is_ineligible_carrier, orient
    from engine.core.core import compute_core
    from engine.magic10_v2.compat import intrinsic_cache_key_v2, reader_projection_v2
    from engine.presenter import emit_public

    rows = surface_pairs(goldens, corpus_facts["people"], corpus_facts["pairs_list"], surface_indices)
    fields = goldens["constants"]["synthetic_projection_fields"]
    client = http_client()
    prefs = viewer_prefs()
    v1_validator = reader_validator(READER_V1_SCHEMA_REL)
    v2_validator = reader_validator(READER_V2_SCHEMA_REL)
    counts = {key: 0 for key in ("runs", "eligible_runs", "in_process_two_run", "cli_two_run", "http_two_run",
                                 "cli_equal", "http_equal", "reader_dump_equal", "reader_validated", "cache_key_equal",
                                 "uid_pairs", "uid_variants")}
    harmony_bodies: dict[str, Mapping[str, Any]] = {}
    warm_pair: tuple[str, str] | None = None
    ineligible_seen = False
    reader_ab: dict[str, tuple[bytes, bytes]] = {}
    pair_file = workdir / "pair.json"
    dump_file = workdir / "reader.json"
    for label, chart_a, chart_b in rows:
        for order, (left, right) in (("ab", (chart_a, chart_b)), ("ba", (chart_b, chart_a))):
            tag = f"{label}.{order}"
            party_l, party_r = resolved_party(left), resolved_party(right)
            value = evaluate(party_l, party_r, bundle)
            expected = emit_public(value)
            ineligible = is_ineligible_carrier(value)
            if not ineligible:
                require_v2(value, bundle, "internal_parity")
            pair_file.write_text(json.dumps({"left": left, "right": right}, sort_keys=True), encoding="utf-8")
            if dump_file.exists():
                dump_file.unlink()
            cli = run_cli(["showcompat", "--pair-file", str(pair_file), "--dump-reader", str(dump_file)])
            if cli.returncode != 0 or cli.stderr != b"" or cli.stdout != expected:
                raise IntegrationEvidenceRefusal(f"{PARITY_MISMATCH}:cli:{tag}")
            response = post_compat(client, {"a": left, "b": right, "viewer_prefs": prefs})
            if (response.status_code != 200 or response.data != expected
                    or response.headers.get("Content-Type") != HTTP_CONTENT_TYPE):
                raise IntegrationEvidenceRefusal(f"{PARITY_MISMATCH}:http:{tag}")
            counts["cli_equal"] += 1
            counts["http_equal"] += 1
            try:
                dump = dump_file.read_bytes()
            except OSError:
                raise IntegrationEvidenceRefusal(f"{PARITY_MISMATCH}:reader:{tag}") from None
            if order == "ab":
                if emit_public(evaluate(party_l, party_r, bundle)) != expected:
                    raise IntegrationEvidenceRefusal(f"{TWO_RUN_MISMATCH}:in_process:{tag}")
                again = run_cli(["showcompat", "--pair-file", str(pair_file)])
                if again.returncode != 0 or again.stdout != cli.stdout:
                    raise IntegrationEvidenceRefusal(f"{TWO_RUN_MISMATCH}:cli:{tag}")
                if post_compat(client, {"a": left, "b": right, "viewer_prefs": prefs}).data != response.data:
                    raise IntegrationEvidenceRefusal(f"{TWO_RUN_MISMATCH}:http:{tag}")
                counts["in_process_two_run"] += 1
                counts["cli_two_run"] += 1
                counts["http_two_run"] += 1
            counts["runs"] += 1
            if ineligible:
                ineligible_seen = True
                parsed = json.loads(dump)
                if parsed.get("eligible") is not False or parsed.get("categories") != []:
                    raise IntegrationEvidenceRefusal(f"{PARITY_MISMATCH}:reader:{tag}")
                v1_validator.validate(parsed)
                counts["reader_dump_equal"] += 1
                continue
            counts["eligible_runs"] += 1
            low, high = orient(party_l, party_r)
            core = compute_core(low.gates, high.gates, bundle, bundle.release_id)
            if intrinsic_cache_key_v2(core) != MAGIC10_V2_INTRINSIC_CACHE_PREFIX + value["pair_key"]:
                raise IntegrationEvidenceRefusal(CACHE_KEY_MISMATCH)
            counts["cache_key_equal"] += 1
            body_v1, envelope_v1 = reader_projection_v2(core, "v1")
            body_v2, envelope_v2 = reader_projection_v2(core, "v2")
            check_reader(value, body_v1, envelope_v1, body_v2, envelope_v2, v1_validator, v2_validator, tag)
            counts["reader_validated"] += 1
            if dump != body_v1:
                raise IntegrationEvidenceRefusal(f"{PARITY_MISMATCH}:reader:{tag}")
            counts["reader_dump_equal"] += 1
            if order == "ab":
                reader_ab[label] = (body_v1, body_v2)
                harmony = envelope_v1["categories"][0]["band"]
                harmony_bodies.setdefault(harmony, value)
                if harmony == "Warm" and warm_pair is None:
                    warm_pair = (label, harmony)
                counts["uid_pairs"] += check_uid_independence(bundle, fields, label, left, right, value)
                counts["uid_variants"] += len(UID_VARIANTS)
            elif reader_ab.get(label) != (body_v1, body_v2):
                raise IntegrationEvidenceRefusal(f"{READER_MISMATCH}:ab_ba:{label}")
    if not ineligible_seen:
        raise IntegrationEvidenceRefusal(f"{READER_MISMATCH}:ineligible")
    golden_files = check_reader_goldens(harmony_bodies, warm_pair is not None)
    facts = {"counts": counts, "pairs": len(rows), "golden_files": golden_files}
    lines = [
        ("set.surface.rule", "for each (category, band), the first corpus pair in corpus order whose AB result has "
                             "that band in that category; then the golden application parties"),
        ("set.surface.corpus_indices", compact(list(surface_indices))),
        ("set.surface.golden_parties", ",".join(SURFACE_GOLDEN_PARTIES)),
        ("set.surface.pairs", str(len(rows))),
        ("set.surface.orders", "ab,ba"),
        ("set.surface.party_form", "complete mapped chart: the golden collection's constants.synthetic_projection_fields "
                                   "with the party's Gates and identity"),
    ]
    return lines, facts


def check_reader(value, body_v1, envelope_v1, body_v2, envelope_v2, v1_validator, v2_validator, tag) -> None:
    for name, body, envelope, validator in (("v1", body_v1, envelope_v1, v1_validator),
                                            ("v2", body_v2, envelope_v2, v2_validator)):
        parsed = json.loads(body)
        try:
            validator.validate(parsed)
        except jsonschema.ValidationError:
            raise IntegrationEvidenceRefusal(f"{READER_MISMATCH}:{name}_schema:{tag}") from None
        if json_numbers(parsed):
            raise IntegrationEvidenceRefusal(f"{READER_MISMATCH}:{name}_numeric:{tag}")
        preimage = {key: item for key, item in parsed.items() if key != "idempotence_hash"}
        if parsed.get("idempotence_hash") != sha256_hex(sercanon(preimage)) or envelope != parsed:
            raise IntegrationEvidenceRefusal(f"{READER_MISMATCH}:{name}_hash:{tag}")
        if parsed.get("release_id") != value["release_id"] or parsed.get("eligible") is not True:
            raise IntegrationEvidenceRefusal(f"{READER_MISMATCH}:{name}_identity:{tag}")
    harmony = [row["band"] for row in value["categories"] if row["category_id"] == "harmony"]
    if json.loads(body_v1)["categories"] != [{"id": "harmony", "band": harmony[0]}]:
        raise IntegrationEvidenceRefusal(f"{READER_MISMATCH}:v1_band:{tag}")
    if json.loads(body_v2)["categories"] != [{"id": row["category_id"], "band": row["band"]}
                                            for row in value["categories"]]:
        raise IntegrationEvidenceRefusal(f"{READER_MISMATCH}:v2_bands:{tag}")


def check_uid_independence(bundle, fields, label, left, right, value) -> int:
    original = canonical(intrinsic(value))
    for variant in UID_VARIANTS:
        uid_l = variant_uid(label, variant, "left")
        uid_r = variant_uid(label, variant, "right")
        moved = evaluate(resolved_party(complete_chart(fields, uid_l, left["bodygraph"]["gates"])),
                         resolved_party(complete_chart(fields, uid_r, right["bodygraph"]["gates"])), bundle)
        require_v2(moved, bundle, "uid_independence")
        if canonical(intrinsic(moved)) != original or moved["pair_key"] != value["pair_key"]:
            raise IntegrationEvidenceRefusal(f"{UID_DEPENDENT}:{label}")
    return 1


def reader_golden_bytes(version: str, eligible: bool, band: str | None) -> bytes:
    from presenter.reader_v1.emitter import emit_reader_v1, emit_reader_v2

    enriched = {"eligible": eligible, "categories": [{"id": "harmony", "band": band}] if eligible else [],
                "meta": dict(READER_GOLDEN_META), "release_id": READER_GOLDEN_RELEASE_ID}
    body, _envelope = (emit_reader_v1 if version == "v1" else emit_reader_v2)(enriched)
    return body


def check_reader_goldens(harmony_bodies: Mapping[str, Any], warm_seen: bool) -> list[str]:
    matched = []
    for band, rel in READER_V1_BAND_GOLDENS:
        if band not in harmony_bodies or reader_golden_bytes("v1", True, band) != read_input(rel):
            raise IntegrationEvidenceRefusal(f"{READER_GOLDEN_MISMATCH}:{rel}")
        matched.append(rel)
    warm = reader_golden_bytes("v1", True, "Warm")
    for rel in READER_V1_ABBA_GOLDENS:
        if not warm_seen or warm + warm != read_input(rel):
            raise IntegrationEvidenceRefusal(f"{READER_GOLDEN_MISMATCH}:{rel}")
        matched.append(rel)
    for version, rel in (("v1", READER_V1_INELIGIBLE_GOLDEN), ("v2", READER_V2_INELIGIBLE_GOLDEN)):
        if reader_golden_bytes(version, False, None) != read_input(rel):
            raise IntegrationEvidenceRefusal(f"{READER_GOLDEN_MISMATCH}:{rel}")
        matched.append(rel)
    return matched


# --- failure tokens (class 7) -------------------------------------------------------------------

def failure_inputs(goldens: Mapping[str, Any]) -> tuple[dict[str, tuple[dict, dict]], dict]:
    fields = goldens["constants"]["synthetic_projection_fields"]
    cases = {case["case_id"]: case for case in goldens["cases"]}
    good = complete_chart(fields, FAILURE_PARTY_B_UID, cases["M10-G004"]["inputs"]["gates_b"])
    no_gates = complete_chart(fields, FAILURE_PARTY_A_UID, [])
    del no_gates["bodygraph"]["gates"]
    unequal = complete_chart(fields, FAILURE_PARTY_A_UID, [1])
    unequal["bodygraph"]["profile"] = "2/4"
    inputs = {
        "FT-1": ({"person_uid": FAILURE_PARTY_A_UID, "birthdate": "1990-01-10", "birthtime": "14:05",
                  "location": "Chicago, US"}, good),
        "FT-2": ({"person_uid": FAILURE_PARTY_A_UID}, good),
        "FT-3": (no_gates, good),
        "FT-4": (complete_chart(fields, FAILURE_PARTY_A_UID, []), good),
        "FT-5": (complete_chart(fields, FAILURE_PARTY_A_UID, [5, 65]), good),
        "FT-6": (complete_chart(fields, FAILURE_PARTY_A_UID, [5, 5, 19]), good),
        "FT-7": (complete_chart(fields, FAILURE_PARTY_A_UID, ["x", 19]), good),
        "FT-8": (complete_chart(fields, FAILURE_PARTY_A_UID, [1]), unequal),
    }
    return inputs, good


def failure_token_class(bundle, goldens: Mapping[str, Any], workdir: Path) -> list[tuple[str, str]]:
    from engine.compat.error_tokens import CompatBoundaryError
    from engine.compat.errors import error_envelope
    from engine.presenter import emit_public

    inputs, _good = failure_inputs(goldens)
    messages = {row["code"]: row["message"] for row in read_json(TOKEN_MAP_REL)}
    client = http_client()
    prefs = viewer_prefs()
    pair_file = workdir / "failure.json"
    lines: list[tuple[str, str]] = []
    disclosed = 0
    for row, description, governed, status, observed_expected, cause in FAILURE_ROWS:
        left, right = inputs[row]
        try:
            evaluate(resolved_party(left), resolved_party(right), bundle)
            in_process = None
        except CompatBoundaryError as exc:
            in_process = exc.token
        if in_process != observed_expected:
            raise IntegrationEvidenceRefusal(f"{FAILURE_TOKEN_MISMATCH}:{row}:in_process")
        pair_file.write_text(json.dumps({"left": left, "right": right}, sort_keys=True), encoding="utf-8")
        cli = run_cli(["showcompat", "--pair-file", str(pair_file)])
        if cli.returncode != 1 or cli.stdout != b"" or cli.stderr != f"{observed_expected}\n".encode("ascii"):
            raise IntegrationEvidenceRefusal(f"{FAILURE_TOKEN_MISMATCH}:{row}:cli")
        response = post_compat(client, {"a": left, "b": right, "viewer_prefs": prefs})
        body = response.data
        try:
            parsed = json.loads(body)
        except ValueError:
            parsed = None
        if (response.status_code != status or response.headers.get("Cache-Control") != "no-store"
                or response.headers.get("Content-Type") != HTTP_CONTENT_TYPE
                or body != emit_public(error_envelope(observed_expected))
                or not isinstance(parsed, dict) or set(parsed) != {"schema", "ok", "code", "error"}
                or parsed.get("code") != observed_expected or parsed.get("error") != messages.get(observed_expected)
                or json_numbers(parsed)):
            raise IntegrationEvidenceRefusal(f"{FAILURE_TOKEN_MISMATCH}:{row}:http")
        result = "PASS" if observed_expected == governed else "BASELINE_FAILURE_DISCLOSED"
        disclosed += result != "PASS"
        lines += [
            (f"class.failure_tokens.{row}.input", description),
            (f"class.failure_tokens.{row}.governed", f"{governed} {status}"),
            (f"class.failure_tokens.{row}.observed.in_process", observed_expected),
            (f"class.failure_tokens.{row}.observed.cli", f"exit 1; stdout empty; stderr {observed_expected}"),
            (f"class.failure_tokens.{row}.observed.http",
             f"{response.status_code} {observed_expected}; Cache-Control no-store; error_v1 four keys; no number"),
            (f"class.failure_tokens.{row}.result", result),
        ]
        if cause is not None:
            lines.append((f"class.failure_tokens.{row}.cause", cause))
    lines = [
        ("class.failure_tokens.owning_source", "errors/token_map/token_map.json; HDE CLI, API and Vendor Ref §§3.3, 4.1.4 and 5.2.3"),
        ("class.failure_tokens.surfaces", "in process (resolve_compat_chart, evaluation_party, evaluate_pair); "
                                          "hdctl showcompat --pair-file; POST /api/compat/v1 (dev app test client)"),
        ("class.failure_tokens.rows", str(len(FAILURE_ROWS))),
        *lines,
        ("class.failure_tokens.rows_pass", str(len(FAILURE_ROWS) - disclosed)),
        ("class.failure_tokens.rows_disclosed", str(disclosed)),
        ("class.failure_tokens.cause", GATE_DATA_CAUSE if disclosed else "none"),
        ("class.failure_tokens.result", "BASELINE_FAILURE_DISCLOSED" if disclosed else "PASS"),
    ]
    return lines


# --- the golden comparison ------------------------------------------------------------------------

def golden_comparison(bundle) -> tuple[list[tuple[str, str]], dict[str, Any]]:
    try:
        comparison = compare_goldens_at_root()
    except Exception as exc:  # a refusal of the comparison is never equality
        raise IntegrationEvidenceRefusal(f"{GOLDEN_MISMATCH}:{getattr(exc, 'code', type(exc).__name__)}") from None
    if comparison.candidate_release_id != bundle.release_id or comparison.config_id != bundle.mechanics["config_id"]:
        raise IntegrationEvidenceRefusal(f"{NOT_ADMITTED_V2_PATH}:goldens")
    outcomes = {case.case_id: case for case in comparison.cases}
    for case_id, case in outcomes.items():
        if case.outcome != "match":
            raise IntegrationEvidenceRefusal(f"{GOLDEN_MISMATCH}:{case_id}")
    if not comparison.ok or len(outcomes) != 8:
        raise IntegrationEvidenceRefusal(f"{GOLDEN_MISMATCH}:comparison")
    observed = {case_id: case.observed for case_id, case in outcomes.items()}
    lines = [
        ("goldens.path", GOLDENS_REL),
        ("goldens.sha256", comparison.goldens_sha256),
        ("goldens.entrypoint", "tools/config/artifacts.py compare_goldens(<repository root>)"),
        *((f"goldens.{case_id}", "match") for case_id in outcomes),
        ("goldens.comparison", "match"),
    ]
    return lines, observed


# --- disclosed baseline failures ------------------------------------------------------------------

def baseline_failure_lines() -> list[tuple[str, str]]:
    lines: list[tuple[str, str]] = []
    for number, (path, arguments, exit_code, refusal, cause, run_here) in enumerate(BASELINE_FAILURES, start=1):
        command = " ".join(("python", path, *arguments))
        if run_here:
            result = run_tool(path, arguments)
            output = (result.stdout + result.stderr).decode("utf-8", "replace")
            if result.returncode != exit_code or refusal not in output:
                raise IntegrationEvidenceRefusal(f"{BASELINE_FAILURE_CHANGED}:{path}")
            observation = "run by this writer under closed rails; exit and refusal as declared"
        else:
            observation = NOT_RUN_OBSERVATION
        lines += [
            (f"baseline_failure.{number}.command", command),
            (f"baseline_failure.{number}.exit", str(exit_code)),
            (f"baseline_failure.{number}.refusal", refusal),
            (f"baseline_failure.{number}.cause", cause),
            (f"baseline_failure.{number}.observed", observation),
        ]
    lines += [
        ("baseline_failure.count", str(len(BASELINE_FAILURES))),
        ("baseline_failure.also_on_main", "each fails identically at main 26158fcb (release 1.3.0)"),
        ("baseline_failure.fixed_here", "none"),
    ]
    return lines


# --- collection ---------------------------------------------------------------------------------

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
                         "tested_inputs.sha256 to the tested commit"),
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
        ("release.result_schema", V2_RESULT_SCHEMA),
        ("release.compat_result_schema", V2_COMPAT_SCHEMA),
        ("release.admission", "_load_active_mechanics_bundle_from_root at the repository root"),
    ]
    goldens = read_json(GOLDENS_REL)
    matrix_lines, surface_indices, corpus_facts = corpus_classes(bundle)
    golden_lines, observed = golden_comparison(bundle)
    workspace = tempfile.mkdtemp(prefix="hde-epic043-wu-pr-12-")
    workdir = Path(workspace).resolve()
    try:
        if workdir == ROOT.resolve() or ROOT.resolve() in workdir.parents:
            raise IntegrationEvidenceRefusal(TEMP_DIRECTORY_INSIDE_REPOSITORY)
        surface_lines, surface = surface_classes(bundle, goldens, corpus_facts, surface_indices, workdir)
        failure_lines = failure_token_class(bundle, goldens, workdir)
    finally:
        for child in workdir.iterdir():
            child.unlink()
        workdir.rmdir()
    counts = surface["counts"]
    runs = str(counts["runs"])
    eligible = str(counts["eligible_runs"])
    g008 = observed["M10-G008"]
    lines += [
        ("set.goldens.path", GOLDENS_REL),
        ("set.goldens.cases", "M10-G001,M10-G002,M10-G003,M10-G004,M10-G005,M10-G006,M10-G007,M10-G008"),
        *matrix_lines[:4],
        *surface_lines,
        ("set.failure_rows", ",".join(row[0] for row in FAILURE_ROWS)),
        *matrix_lines[4:],
        ("class.ab_ba_two_run.owning_source", "HDE Math Spec §9.5 Prove"),
        ("class.ab_ba_two_run.ab_ba.corpus.pairs", corpus_facts["pairs"]),
        ("class.ab_ba_two_run.ab_ba.corpus.byte_identical", corpus_facts["pairs"]),
        ("class.ab_ba_two_run.ab_ba.surface.pairs", str(surface["pairs"])),
        ("class.ab_ba_two_run.ab_ba.surface.byte_identical_at", "evaluate_pair,cli,http,reader_v1,reader_v2"),
        ("class.ab_ba_two_run.ab_ba.goldens", "every case checked in both pair orders (pair_order); "
                                              "M10-G002 and M10-G004 ab_ba_identity true"),
        ("class.ab_ba_two_run.two_run.surface.in_process", str(counts["in_process_two_run"])),
        ("class.ab_ba_two_run.two_run.surface.cli", str(counts["cli_two_run"])),
        ("class.ab_ba_two_run.two_run.surface.http", str(counts["http_two_run"])),
        ("class.ab_ba_two_run.two_run.goldens", "M10-G002 and M10-G004 two_run_identity true; "
                                                "M10-G008 two_run_bytes_identical true"),
        ("class.ab_ba_two_run.two_run.corpus", "reproduced by every --check of this record, a second process over the "
                                               "same inputs, through class.full_matrix.matrix_sha256"),
        ("class.ab_ba_two_run.result", "PASS"),
        ("class.pair_cache_identity.owning_source", "HDE Math Spec §5.2.2"),
        ("class.pair_cache_identity.construction", "chart_fingerprint and magic10_pair_preimage.v1 rebuilt by this writer: "
                                                   "members by numeric Gate mask, config_id, release_id, result_schema magic10_result.v2"),
        ("class.pair_cache_identity.pair_key_equal", corpus_facts["pairs"]),
        ("class.pair_cache_identity.cache_key_form", "magic10:v2:<pair_key>"),
        ("class.pair_cache_identity.cache_key_equal.corpus", corpus_facts["pairs"]),
        ("class.pair_cache_identity.cache_key_equal.surface", str(counts["cache_key_equal"])),
        ("class.pair_cache_identity.stable_across_order_and_runs", "true (class ab_ba_two_run)"),
        ("class.pair_cache_identity.distinct_pair_keys", corpus_facts["distinct_pair_keys"]),
        ("class.pair_cache_identity.distinct_mask_pairs", corpus_facts["distinct_mask_pairs"]),
        ("class.pair_cache_identity.prior_identity", f"config {V1_CONFIG_ID}, release {PRIOR_RELEASE_ID}, "
                                                     f"result_schema {V1_RESULT_SCHEMA}, cache prefix {V1_CACHE_PREFIX}"),
        ("class.pair_cache_identity.distinct_from_prior", corpus_facts["pairs"]),
        ("class.pair_cache_identity.result", "PASS"),
        ("class.uid_independence.owning_source", "HDE Math Spec §9.5 M10-G005"),
        ("class.uid_independence.goldens", "M10-G005 match"),
        ("class.uid_independence.surface.eligible_pairs", str(counts["uid_pairs"])),
        ("class.uid_independence.surface.variants_per_pair", str(len(UID_VARIANTS))),
        ("class.uid_independence.surface.identical", str(counts["uid_variants"])),
        ("class.uid_independence.scope", "intrinsic content and pair_key; not eligibility, narrative orientation or Reader bytes"),
        ("class.uid_independence.result", "PASS"),
        ("class.result_schema.owning_source", f"{RESULT_SCHEMA_REL} and {COMPAT_SCHEMA_REL} (release members)"),
        ("class.result_schema.path_validated", corpus_facts["pairs"]),
        (f"class.result_schema.{RESULT_SCHEMA_REL}.validated", corpus_facts["pairs"]),
        (f"class.result_schema.{COMPAT_SCHEMA_REL}.validated", corpus_facts["pairs"]),
        ("class.result_schema.validator", "Draft 2020-12 over the committed schema bytes, strict integers"),
        ("class.result_schema.adverse_refused", ",".join(corpus_facts["adverse"])),
        ("class.result_schema.result", "PASS"),
        ("class.reader_projection.owning_source", f"Reader v1 and v2 contracts; {READER_V1_SCHEMA_REL}; {READER_V2_SCHEMA_REL}; goldens/reader/"),
        ("class.reader_projection.entrypoint", "engine.magic10_v2.compat.reader_projection_v2 over compute_core; "
                                               "presenter/reader_v1/emitter.py for the goldens"),
        ("class.reader_projection.eligible_runs", eligible),
        ("class.reader_projection.validated", str(counts["reader_validated"])),
        ("class.reader_projection.numeric_free", "true"),
        ("class.reader_projection.hash_rule", "idempotence_hash equals the SHA-256 of the canonical preimage"),
        ("class.reader_projection.cli_dump_equal", str(counts["reader_dump_equal"])),
        ("class.reader_projection.goldens_equal", ",".join(surface["golden_files"])),
        ("class.reader_projection.m10_g007_v1_hash", observed["M10-G007"]["reader"]["idempotence_hash"]),
        ("class.reader_projection.m10_g008_v1_hash", g008["reader"]["idempotence_hash"]),
        ("class.reader_projection.m10_g008_v2_hash", g008["reader_v2"]["idempotence_hash"]),
        ("class.reader_projection.result", "PASS"),
        *failure_lines,
        ("class.internal_parity.owning_source", "the Plan's four surfaces: CLI, internal HTTP, compat and Reader projection"),
        ("class.internal_parity.cli", "python scripts/hdctl.py showcompat --pair-file <temporary> --dump-reader <temporary>"),
        ("class.internal_parity.http", "POST /api/compat/v1 through a test client of adapter.http_reader.create_app"),
        ("class.internal_parity.runs", runs),
        ("class.internal_parity.cli_stdout_equal", str(counts["cli_equal"])),
        ("class.internal_parity.http_body_equal", str(counts["http_equal"])),
        ("class.internal_parity.reader_dump_equal", str(counts["reader_dump_equal"])),
        ("class.internal_parity.result", "PASS"),
        *golden_lines,
        *baseline_failure_lines(),
        *((f"deferred.{subtask}", text) for subtask, text in DEFERRED),
        ("command.writer", f"python {GENERATOR_REL} --actor <run.actor>"),
        ("command.check", f"python {GENERATOR_REL} --check"),
        *((f"limitation.{index}", text) for index, text in enumerate(LIMITATIONS, start=1)),
        ("classes.pass", "7"),
        ("classes.baseline_failure_disclosed", "1"),
        ("status", "COMPLETE"),
    ]
    results = [value for key, value in lines if key.startswith("class.") and key.endswith(".result")
               and key.count(".") == 2]
    passed = sum(value == "PASS" for value in results)
    if len(results) != 8 or passed + results.count("BASELINE_FAILURE_DISCLOSED") != 8:
        raise IntegrationEvidenceRefusal(RECORD_INVALID)
    lines[-3] = ("classes.pass", str(passed))
    lines[-2] = ("classes.baseline_failure_disclosed", str(8 - passed))
    return lines


# --- record -------------------------------------------------------------------------------------

def header(run: Mapping[str, str]) -> list[tuple[str, str]]:
    return [
        ("schema", SCHEMA),
        ("epic_id", "HDE-EPIC043"),
        ("task_id", "HDE-CONJ010"),
        ("subtask_ids", "HDE-CONJ010.6"),
        ("work_unit_id", "WU-PR-12"),
        *((key, run[key]) for key in RUN_FIELDS),
    ]


def render(lines: Sequence[tuple[str, str]]) -> bytes:
    keys = [key for key, _value in lines]
    if len(keys) != len(set(keys)) or keys[0] != "schema" or keys[-1] != "status":
        raise IntegrationEvidenceRefusal(RECORD_INVALID)
    for key, value in lines:
        if (not isinstance(value, str) or not key or ": " in key
                or any(char in f"{key}{value}" for char in "\r\n")):
            raise IntegrationEvidenceRefusal(RECORD_INVALID)
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
        raise IntegrationEvidenceRefusal(INVALID_ACTOR)
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
    # The tested inputs are compared before any class runs, so a stale record fails fast.
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
                      help="compare the tested inputs, re-derive every class and compare the bytes; write nothing")
    args = parser.parse_args(argv)
    try:
        if args.check:
            check()
            print("v2 integration evidence check ok")
            return 0
        write(args.actor)
    except IntegrationEvidenceRefusal as exc:
        raise SystemExit(exc.code) from None
    print("v2 integration evidence written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
