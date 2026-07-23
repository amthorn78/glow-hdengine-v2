from __future__ import annotations

import builtins
import copy
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
import uuid
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

from scripts.ops import hde_epic038_ops03 as runner
from tools.evidence import hde_epic038_ops03 as validator
from tools.evidence import strict_json_schema

NOW = dt.datetime(2026, 7, 21, 12, 0, tzinfo=dt.timezone.utc)
CLEAN_ENV = {
    "APP_ENV": "dev",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "ALLOW_DB_WRITE": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "DATABASE_URL": "fixture-not-serialized",
}
OPS03_SCHEMA_FILES = (
    "hde_epic038_ops03_authorization.v1.json",
    "hde_epic038_ops03_db_posture_summary.v1.json",
    "hde_epic038_ops03_env_presence.v1.json",
    "hde_epic038_ops03_failure_receipt.v1.json",
    "hde_epic038_ops03_nonclaims.v1.json",
    "hde_epic038_ops03_result_summary.v1.json",
    "hde_epic038_ops03_validation_receipt.v1.json",
)


class FixtureProvider:
    name = "psycopg"

    def __init__(
        self,
        *,
        fail_posture: bool = False,
        role_row=None,
        boundary_rows=None,
        partition_rows=None,
    ):
        self.fail_posture = fail_posture
        self.role_row = role_row or (False, False, False, False, False, False, False)
        self.boundary_rows = boundary_rows or (
            ("hde", "body_graphs_current", "NO", "NO", "NO", "NO", "NO"),
            ("public", "hde_body_graphs_current", "NO", "NO", "NO", "NO", "NO"),
        )
        self.partition_rows = (
            partition_rows
            if partition_rows is not None
            else (
                ("hde.pair_evaluation", "r", "RANGE (evaluated_at)"),
                ("hde.public_results", "r", "RANGE (created_at)"),
            )
        )

    def health(self) -> None:
        return None

    def readonly_tx(self, statements):
        assert [item.sql for item in statements] == [item.sql for item in runner.QUERY_STATEMENTS]
        if self.fail_posture:
            raise RuntimeError("fixture failure must not be serialized")
        return [
            None,
            None,
            [(True, True, True)],
            [("hde, public",)],
            [self.role_row],
            [("id", "uuid", "NO", "gen_random_uuid()")],
            [("body_graphs_pkey", "PRIMARY KEY (id)")],
            list(self.boundary_rows),
            list(self.partition_rows),
            [("hde.pair_evaluation", True), ("hde.public_results", True)],
        ]

    def query(self, *_args, **_kwargs):
        return []

    def exec(self, *_args, **_kwargs):
        return None

    def tx(self, *_args, **_kwargs):
        return []

    def introspect(self, *_args, **_kwargs):
        return {}


def _provider_builder(
    *,
    fail_posture: bool = False,
    role_row=None,
    boundary_rows=None,
    partition_rows=None,
):
    def builder(counters):
        def factory(_dsn):
            counters.provider_selections += 1
            return runner.CountingProvider(
                FixtureProvider(
                    fail_posture=fail_posture,
                    role_row=role_row,
                    boundary_rows=boundary_rows,
                    partition_rows=partition_rows,
                ),
                counters,
                count_connections_by_call=True,
            )

        return factory

    return builder


def _contract_node_paths(value, prefix=()):
    if isinstance(value, dict):
        for key, item in value.items():
            path = (*prefix, key)
            yield path
            yield from _contract_node_paths(item, path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            path = (*prefix, index)
            yield path
            yield from _contract_node_paths(item, path)


def _invalid_contract_value(value):
    if isinstance(value, dict):
        return []
    if isinstance(value, list):
        return {}
    if isinstance(value, bool):
        return "invalid-boolean"
    if isinstance(value, int):
        return "invalid-integer"
    if isinstance(value, str):
        return False
    if value is None:
        return "invalid-null"
    raise AssertionError(f"unsupported contract value: {type(value)!r}")


def _replace_contract_node(value, path):
    target = value
    for part in path[:-1]:
        target = target[part]
    leaf = path[-1]
    target[leaf] = _invalid_contract_value(target[leaf])


def _standalone_schema_validator(filename: str) -> Draft202012Validator:
    schema_path = runner.ROOT / "schemas" / filename
    schema = json.loads(schema_path.read_bytes())
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _nested_value(value, path):
    target = value
    for part in path:
        target = target[part]
    return target


def test_ops03_schema_sources_are_canonical_and_well_formed():
    discovered = tuple(
        sorted(
            path.name
            for path in (runner.ROOT / "schemas").glob(
                "hde_epic038_ops03_*.json"
            )
        )
    )
    assert discovered == tuple(sorted(OPS03_SCHEMA_FILES))
    for filename in OPS03_SCHEMA_FILES:
        path = runner.ROOT / "schemas" / filename
        raw = path.read_bytes()
        value = json.loads(raw)
        assert raw == runner.canonical_bytes(value), filename
        Draft202012Validator.check_schema(value)


@pytest.mark.parametrize(
    ("value", "schema", "expected"),
    (
        (True, {"type": "integer"}, False),
        (1, {"type": "integer", "minimum": 1, "maximum": 1}, True),
        (1.0, {"type": "integer"}, True),
        (1.5, {"type": "integer"}, False),
        ("x", {"unknown": True}, False),
        ("x", {"$ref": "https://example.invalid/schema"}, False),
        ("x", {"$ref": "#/$defs/missing", "$defs": {}}, False),
        (
            "x",
            {
                "$ref": "#/$defs/loop",
                "$defs": {"loop": {"$ref": "#/$defs/loop"}},
            },
            False,
        ),
        ("x", {"type": "string", "pattern": "["}, False),
        ("2026-07-21", {"type": "string", "format": "date-time"}, False),
        (
            "2026-07-21t12:00:00.125-07:30",
            {"type": "string", "format": "date-time"},
            True,
        ),
        (
            "2026-02-29T12:00:00Z",
            {"type": "string", "format": "date-time"},
            False,
        ),
        (
            "2026-07-21T12:00:00+24:00",
            {"type": "string", "format": "date-time"},
            False,
        ),
        (
            ["a", "b"],
            {
                "type": "array",
                "prefixItems": [{"const": "a"}],
                "items": False,
            },
            False,
        ),
    ),
)
def test_strict_schema_validator_is_fail_closed(value, schema, expected):
    assert strict_json_schema.is_valid(value, schema) is expected


@pytest.mark.parametrize("value", [1, 1.0, -2.0, 0])
def test_strict_schema_integer_semantics_match_draft_2020(value):
    schema = {"type": "integer"}
    reference = Draft202012Validator(schema)

    assert strict_json_schema.is_valid(value, schema) == reference.is_valid(value)


@pytest.fixture
def authorization(tmp_path):
    runner.RUN_ROOT.mkdir(mode=0o700, parents=True, exist_ok=True)
    runner.RUN_ROOT.chmod(0o700)
    run_id = "ops03-test-" + uuid.uuid4().hex[:24]
    base, _control, candidate, _failure = runner.derived_paths(run_id)
    auth_path = tmp_path / "authorization.json"
    auth = {
        "schema": "hde_epic038.ops03.authorization.v1",
        "run_id": run_id,
        "authorized_at_utc": "2026-07-21T11:00:00Z",
        "expires_at_utc": "2026-07-21T13:00:00Z",
        "source_commit": "0" * 40,
        "runner_sha256": runner.sha256_path(runner.RUNNER),
        "validator_sha256": runner.sha256_path(runner.VALIDATOR),
        "interpreter": {
            "resolved_path": str(Path(sys.executable).resolve()),
            "sha256": runner.sha256_path(Path(sys.executable).resolve()),
        },
        "target": {"app_env": "dev", "database_schema": "hde", "search_path": ["hde", "public"]},
        "rails": {"safe_mode": "1", "allow_network": "0", "allow_db_write": "0", "db_read_authorized": True},
        "retired_keys_required_absent": list(runner.RETIRED_DB_TRANSPORT_KEYS),
        "ordered_query_ids": list(runner.ORDERED_QUERY_IDS),
        "expected_counts": runner.EXPECTED_COUNTS,
        "candidate_root": candidate.as_posix() + "/",
        "exact_argv": {},
        "one_attempt": True,
    }
    auth["exact_argv"] = runner.expected_argv(auth, auth_path, candidate)
    auth_path.write_bytes(runner.canonical_bytes(auth))
    try:
        yield auth_path, auth, base, candidate
    finally:
        shutil.rmtree(base, ignore_errors=True)


def _capture(authorization, *, env=None, builder=None):
    auth_path, _auth, _base, _candidate = authorization
    return runner.capture(
        auth_path,
        ambient=CLEAN_ENV if env is None else env,
        provider_factory_builder=builder or _provider_builder(),
        enforce_source=False,
        invoke_validators=False,
        now=NOW,
    )


def _seal(auth_path: Path, candidate: Path):
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
        emit_receipt=True,
    )
    assert receipt["result"] == "PASS"
    assert (candidate / validator.RECEIPT_FILE).read_bytes() == validator.canonical_bytes(receipt)
    runner.write_checksums(candidate)
    context = runner._context_for_candidate(candidate)
    try:
        files = runner._snapshot_candidate_files(context)
        runner._write_candidate_commit_control(
            context,
            json.loads(auth_path.read_text(encoding="utf-8")),
            runner.sha256_path(auth_path),
            runner._candidate_commit_record(
                files,
                sealed=True,
                finalized=True,
                committed_payload=runner._read_file(
                    context.control_fd,
                    runner.COMMITTED_FILE,
                ),
            ),
        )
    finally:
        context.close()
    return validator.validate_packet(auth_path, candidate, final=True, enforce_source=False, now=NOW)


def test_runner_builds_exact_semantic_packet_and_validator_seals_it(authorization):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    assert tuple(sorted(path.name for path in candidate.iterdir())) == tuple(sorted(runner.PRIMARY_FILES))
    final = _seal(auth_path, candidate)
    assert final["result"] == "PASS"
    assert tuple(sorted(path.name for path in candidate.iterdir())) == validator.FINAL_FILES


def test_ops03_schemas_standalone_accept_canonical_contract_bytes(authorization):
    auth_path, auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    failure = {
        "schema": "hde_epic038.ops03.failure_receipt.v1",
        "run_id": auth["run_id"],
        "authorization_sha256": runner.sha256_path(auth_path),
        "phase": "pre_marker",
        "code": "fixture_failure",
        "launch_consumed": False,
        "candidate_admissible": False,
        "nonclaims": list(runner.NONCLAIMS),
    }
    samples = {
        "hde_epic038_ops03_authorization.v1.json": (
            auth,
            auth_path.read_bytes(),
        ),
        "hde_epic038_ops03_db_posture_summary.v1.json": (
            json.loads((candidate / "db_posture_summary.json").read_bytes()),
            (candidate / "db_posture_summary.json").read_bytes(),
        ),
        "hde_epic038_ops03_env_presence.v1.json": (
            json.loads((candidate / "env_presence.json").read_bytes()),
            (candidate / "env_presence.json").read_bytes(),
        ),
        "hde_epic038_ops03_failure_receipt.v1.json": (
            failure,
            runner.canonical_bytes(failure),
        ),
        "hde_epic038_ops03_nonclaims.v1.json": (
            json.loads((candidate / "nonclaims.json").read_bytes()),
            (candidate / "nonclaims.json").read_bytes(),
        ),
        "hde_epic038_ops03_result_summary.v1.json": (
            json.loads((candidate / "result_summary.json").read_bytes()),
            (candidate / "result_summary.json").read_bytes(),
        ),
    }
    assert _seal(auth_path, candidate)["result"] == "PASS"
    validation_receipt_bytes = (candidate / validator.RECEIPT_FILE).read_bytes()
    samples["hde_epic038_ops03_validation_receipt.v1.json"] = (
        json.loads(validation_receipt_bytes),
        validation_receipt_bytes,
    )

    assert set(samples) == set(OPS03_SCHEMA_FILES)
    for schema_name, (value, raw) in samples.items():
        assert raw == runner.canonical_bytes(value), schema_name
        schema_validator = _standalone_schema_validator(schema_name)
        schema_validator.validate(value)
        assert strict_json_schema.is_valid(value, schema_validator.schema), schema_name


def test_ops03_schemas_standalone_reject_truncated_extra_and_reordered_vectors(
    authorization,
):
    auth_path, auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    posture = json.loads((candidate / "db_posture_summary.json").read_bytes())
    nonclaims = json.loads((candidate / "nonclaims.json").read_bytes())
    result_summary = json.loads((candidate / "result_summary.json").read_bytes())
    failure = {
        "schema": "hde_epic038.ops03.failure_receipt.v1",
        "run_id": auth["run_id"],
        "authorization_sha256": runner.sha256_path(auth_path),
        "phase": "pre_marker",
        "code": "fixture_failure",
        "launch_consumed": False,
        "candidate_admissible": False,
        "nonclaims": list(runner.NONCLAIMS),
    }
    assert _seal(auth_path, candidate)["result"] == "PASS"
    validation_receipt = json.loads(
        (candidate / validator.RECEIPT_FILE).read_bytes()
    )
    contracts = (
        ("hde_epic038_ops03_authorization.v1.json", auth, ("target", "search_path")),
        (
            "hde_epic038_ops03_authorization.v1.json",
            auth,
            ("retired_keys_required_absent",),
        ),
        (
            "hde_epic038_ops03_authorization.v1.json",
            auth,
            ("ordered_query_ids",),
        ),
        (
            "hde_epic038_ops03_authorization.v1.json",
            auth,
            ("exact_argv", "capture"),
        ),
        (
            "hde_epic038_ops03_authorization.v1.json",
            auth,
            ("exact_argv", "receipt"),
        ),
        (
            "hde_epic038_ops03_authorization.v1.json",
            auth,
            ("exact_argv", "validate"),
        ),
        (
            "hde_epic038_ops03_db_posture_summary.v1.json",
            posture,
            ("selection_attempts",),
        ),
        (
            "hde_epic038_ops03_db_posture_summary.v1.json",
            posture,
            ("ordered_query_ids",),
        ),
        (
            "hde_epic038_ops03_db_posture_summary.v1.json",
            posture,
            ("query_results",),
        ),
        (
            "hde_epic038_ops03_db_posture_summary.v1.json",
            posture,
            ("observations", "search_path"),
        ),
        (
            "hde_epic038_ops03_db_posture_summary.v1.json",
            posture,
            ("observations", "boundary_views"),
        ),
        (
            "hde_epic038_ops03_db_posture_summary.v1.json",
            posture,
            ("observations", "partition_posture", "expected_tables"),
        ),
        (
            "hde_epic038_ops03_db_posture_summary.v1.json",
            posture,
            ("observations", "partition_posture", "observed_tables"),
        ),
        (
            "hde_epic038_ops03_failure_receipt.v1.json",
            failure,
            ("nonclaims",),
        ),
        (
            "hde_epic038_ops03_nonclaims.v1.json",
            nonclaims,
            ("nonclaims",),
        ),
        (
            "hde_epic038_ops03_result_summary.v1.json",
            result_summary,
            ("primary_files",),
        ),
        (
            "hde_epic038_ops03_validation_receipt.v1.json",
            validation_receipt,
            ("validated_files",),
        ),
    )

    for schema_name, value, path in contracts:
        schema_validator = _standalone_schema_validator(schema_name)
        schema_validator.validate(value)
        vector = _nested_value(value, path)
        mutations = (vector[:-1], [*vector, copy.deepcopy(vector[-1])])
        if len(vector) > 1:
            mutations = (
                *mutations,
                list(reversed(vector)),
                [copy.deepcopy(vector[0]) for _ in vector],
            )
        for replacement in mutations:
            mutated = copy.deepcopy(value)
            target = _nested_value(mutated, path[:-1]) if path[:-1] else mutated
            target[path[-1]] = replacement
            assert not schema_validator.is_valid(mutated), (
                schema_name,
                path,
                replacement,
            )
            assert not strict_json_schema.is_valid(mutated, schema_validator.schema), (
                schema_name,
                path,
                replacement,
            )


@pytest.mark.parametrize(
    ("phase", "launch_consumed"),
    (
        ("pre_marker", False),
        ("pre_provider", True),
        ("capture", True),
        ("receipt_validation", True),
        ("final_validation", True),
    ),
)
def test_failure_receipt_schema_accepts_phase_consistent_launch_state(
    authorization,
    phase,
    launch_consumed,
):
    auth_path, auth, _base, _candidate = authorization
    receipt = {
        "schema": "hde_epic038.ops03.failure_receipt.v1",
        "run_id": auth["run_id"],
        "authorization_sha256": runner.sha256_path(auth_path),
        "phase": phase,
        "code": "fixture_failure",
        "launch_consumed": launch_consumed,
        "candidate_admissible": False,
        "nonclaims": list(runner.NONCLAIMS),
    }

    _standalone_schema_validator(
        "hde_epic038_ops03_failure_receipt.v1.json"
    ).validate(receipt)
    schema = json.loads(
        (runner.ROOT / "schemas/hde_epic038_ops03_failure_receipt.v1.json").read_bytes()
    )
    assert strict_json_schema.is_valid(receipt, schema)


@pytest.mark.parametrize(
    ("phase", "launch_consumed"),
    (
        ("pre_marker", True),
        ("pre_provider", False),
        ("capture", False),
        ("receipt_validation", False),
        ("final_validation", False),
    ),
)
def test_failure_receipt_schema_rejects_phase_inconsistent_launch_state(
    authorization,
    phase,
    launch_consumed,
):
    auth_path, auth, _base, _candidate = authorization
    receipt = {
        "schema": "hde_epic038.ops03.failure_receipt.v1",
        "run_id": auth["run_id"],
        "authorization_sha256": runner.sha256_path(auth_path),
        "phase": phase,
        "code": "fixture_failure",
        "launch_consumed": launch_consumed,
        "candidate_admissible": False,
        "nonclaims": list(runner.NONCLAIMS),
    }

    with pytest.raises(ValidationError):
        _standalone_schema_validator(
            "hde_epic038_ops03_failure_receipt.v1.json"
        ).validate(receipt)
    schema = json.loads(
        (runner.ROOT / "schemas/hde_epic038_ops03_failure_receipt.v1.json").read_bytes()
    )
    assert not strict_json_schema.is_valid(receipt, schema)


def test_validation_receipt_schema_rejects_fail_with_all_predicates_true(
    authorization,
):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    assert _seal(auth_path, candidate)["result"] == "PASS"
    receipt = json.loads((candidate / validator.RECEIPT_FILE).read_bytes())
    schema_validator = _standalone_schema_validator(
        "hde_epic038_ops03_validation_receipt.v1.json"
    )
    assert strict_json_schema.is_valid(receipt, schema_validator.schema)

    false_negative = copy.deepcopy(receipt)
    false_negative["result"] = "FAIL"
    with pytest.raises(ValidationError):
        schema_validator.validate(false_negative)
    assert not strict_json_schema.is_valid(false_negative, schema_validator.schema)

    legitimate_failure = copy.deepcopy(false_negative)
    legitimate_failure["predicates"]["counts_valid"] = False
    schema_validator.validate(legitimate_failure)
    assert strict_json_schema.is_valid(
        legitimate_failure, schema_validator.schema
    )


def test_runtime_role_query_covers_ownership_and_column_write_grants():
    sql = runner.QUERY_STATEMENTS[4].sql
    assert "information_schema.column_privileges" in sql
    assert "pg_has_role(current_user, nsp.nspowner, 'USAGE')" in sql
    assert "pg_has_role(current_user, cls.relowner, 'USAGE')" in sql


def test_positive_isolated_runner_validator_sealing_path(authorization, tmp_path):
    auth_path, original_auth, base, candidate = authorization
    repo = tmp_path / "sealed-repo"
    (repo / "scripts/ops").mkdir(parents=True)
    (repo / "tools/evidence").mkdir(parents=True)
    (repo / "schemas").mkdir()
    (repo / "engine/db/providers").mkdir(parents=True)
    copied_runner = repo / "scripts/ops/hde_epic038_ops03.py"
    copied_validator = repo / "tools/evidence/hde_epic038_ops03.py"
    shutil.copy2(runner.RUNNER, copied_runner)
    shutil.copy2(runner.VALIDATOR, copied_validator)
    shutil.copy2(
        runner.ROOT / "tools/evidence/retained_evidence_safety.py",
        repo / "tools/evidence/retained_evidence_safety.py",
    )
    shutil.copy2(
        runner.ROOT / "tools/evidence/strict_json_schema.py",
        repo / "tools/evidence/strict_json_schema.py",
    )
    for schema in (
        "hde_epic038_ops03_authorization.v1.json",
        "hde_epic038_ops03_db_posture_summary.v1.json",
        "hde_epic038_ops03_env_presence.v1.json",
        "hde_epic038_ops03_failure_receipt.v1.json",
        "hde_epic038_ops03_nonclaims.v1.json",
        "hde_epic038_ops03_result_summary.v1.json",
        "hde_epic038_ops03_validation_receipt.v1.json",
    ):
        shutil.copy2(runner.ROOT / "schemas" / schema, repo / "schemas" / schema)
    for package in (
        "engine/__init__.py",
        "engine/db/__init__.py",
        "engine/db/providers/__init__.py",
        "tools/__init__.py",
        "tools/evidence/__init__.py",
    ):
        path = repo / package
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")
    (repo / "engine/db/adapter.py").write_text(
        """class DBAccess:
    def __init__(self, provider):
        self._provider = provider
        self.provider_name = "psycopg"
        self.attempts = [{"provider": "psycopg", "status": "ok", "reason": None}]

    @classmethod
    def for_current_env(cls, *, environ, psycopg_factory):
        dsn = next(value for name, value in environ.items() if name == "DATABASE_URL")
        provider = psycopg_factory(dsn)
        provider.health()
        return cls(provider)

    def readonly_tx(self, statements):
        return self._provider.readonly_tx(statements)
""",
        encoding="utf-8",
    )
    (repo / "engine/db/ddl_identity_projection.py").write_text(
        """DDL_IDENTITY_PROJECTION_SCHEMA = "hde.ddl_identity_projection.v1"

def project_ddl_identity(value):
    return {"objects": value}
""",
        encoding="utf-8",
    )
    (repo / "engine/db/providers/psycopg_provider.py").write_text(
        """def validate_readonly_statements(statements):
    if len(statements) != 10:
        raise ValueError("unexpected statement count")

class PsycopgProvider:
    def __init__(self, dsn, *, connection_factory=None):
        self._dsn = dsn
        self._connection_factory = connection_factory

    def health(self):
        self._connection_factory(self._dsn)

    def readonly_tx(self, statements):
        self._connection_factory(self._dsn)
        return [
            None,
            None,
            [(True, True, True)],
            [("hde, public",)],
            [(False, False, False, False, False, False, False)],
            [("id", "uuid", "NO", "gen_random_uuid()")],
            [("body_graphs_pkey", "PRIMARY KEY (id)")],
            [
                ("hde", "body_graphs_current", "NO", "NO", "NO", "NO", "NO"),
                ("public", "hde_body_graphs_current", "NO", "NO", "NO", "NO", "NO"),
            ],
            [("hde.pair_evaluation", "r", "RANGE (evaluated_at)"), ("hde.public_results", "r", "RANGE (created_at)")],
            [("hde.pair_evaluation", True), ("hde.public_results", True)],
        ]
""",
        encoding="utf-8",
    )
    (repo / "psycopg.py").write_text(
        """class Connection:
    pass

def connect(_dsn, *, connect_timeout):
    if connect_timeout != 5:
        raise ValueError("unexpected timeout")
    return Connection()
""",
        encoding="utf-8",
    )
    source_commit = _commit_test_repository(repo)

    auth = copy.deepcopy(original_auth)
    active_now = dt.datetime.now(dt.timezone.utc)
    auth["authorized_at_utc"] = (
        active_now - dt.timedelta(minutes=5)
    ).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    auth["expires_at_utc"] = (
        active_now + dt.timedelta(minutes=30)
    ).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    auth["source_commit"] = source_commit
    auth["runner_sha256"] = runner.sha256_path(copied_runner)
    auth["validator_sha256"] = runner.sha256_path(copied_validator)
    interpreter = str(Path(sys.executable).resolve())
    common = [interpreter, "-I", "-B"]
    auth["exact_argv"] = {
        "capture": [*common, str(copied_runner), "--authorization", str(auth_path)],
        "receipt": [
            *common,
            str(copied_validator),
            "--emit-receipt",
            "--authorization",
            str(auth_path),
            "--candidate",
            str(candidate),
        ],
        "validate": [
            *common,
            str(copied_validator),
            "--validate",
            "--authorization",
            str(auth_path),
            "--candidate",
            str(candidate),
        ],
    }
    auth_path.write_bytes(runner.canonical_bytes(auth))

    try:
        completed = subprocess.run(
            auth["exact_argv"]["capture"],
            check=False,
            cwd=repo,
            env=CLEAN_ENV,
            capture_output=True,
        )
        failure_path = candidate.parent / "failure/failure_receipt.json"
        failure_detail = (
            failure_path.read_text(encoding="utf-8")
            if failure_path.exists()
            else "no failure receipt"
        )
        assert completed.returncode == 0, failure_detail + completed.stderr.decode(
            "utf-8",
            "replace",
        )
        assert not (candidate / runner.PENDING_FILE).exists()
        assert (
            tuple(sorted(path.name for path in candidate.iterdir()))
            == validator.FINAL_FILES
        )
        repeated = subprocess.run(
            auth["exact_argv"]["validate"],
            check=False,
            cwd=repo,
            env=runner._clean_validator_environment(),
            capture_output=True,
        )
        assert repeated.returncode == 0, repeated.stderr.decode("utf-8", "replace")
    finally:
        shutil.rmtree(base, ignore_errors=True)


def test_final_commit_rejects_post_validator_candidate_mutation(authorization):
    auth_path, auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    _seal(auth_path, candidate)
    authorization_sha256 = runner.sha256_path(auth_path)
    pending_token = os.urandom(32)
    context = runner._open_run_context(auth["run_id"], create_base=False, allow_existing=True)
    try:
        context.control_fd = runner._secure_open_dir(context.base_fd, "control")
        context.candidate_fd = runner._secure_open_dir(context.base_fd, "candidate")
        runner._replace_file(
            context.control_fd,
            "authorization_consumed.json",
            runner.canonical_bytes(
                runner._authorization_consumption(auth, authorization_sha256)
            ),
        )
        os.unlink(runner.COMMITTED_FILE, dir_fd=context.control_fd)
        os.fsync(context.control_fd)
        runner._write_new_file(
            context.candidate_fd,
            runner.PENDING_FILE,
            runner._pending_payload(auth, authorization_sha256, pending_token),
        )
        files = runner._snapshot_candidate_files(context)
        retained = {name: files[name] for name in runner.FINAL_FILES}
        attestation = runner._candidate_attestation(auth, authorization_sha256, retained)
        (candidate / "stdout.log").write_text("tampered-after-validation\n", encoding="utf-8")
        with pytest.raises(runner.Ops03Error) as exc:
            runner._commit_candidate(
                context,
                auth,
                auth_path,
                auth_path.read_bytes(),
                authorization_sha256,
                pending_token,
                attestation,
                sealed=True,
                enforce_source=False,
            )
        assert exc.value.code == "candidate_attestation_mismatch"
        assert (candidate / runner.PENDING_FILE).is_file()
    finally:
        context.close()


def test_atomic_commit_move_then_base_exception_is_terminal_commit(monkeypatch, authorization):
    _auth_path, _auth, base, candidate = authorization
    original_rename = runner.os.rename

    def move_then_interrupt(source, destination, *args, **kwargs):
        result = original_rename(source, destination, *args, **kwargs)
        if source == runner.PENDING_FILE and destination == runner.COMMITTED_FILE:
            raise KeyboardInterrupt("fixture post-transition interruption")
        return result

    monkeypatch.setattr(runner.os, "rename", move_then_interrupt)
    assert _capture(authorization) == 0
    assert tuple(sorted(path.name for path in candidate.iterdir())) == tuple(sorted(runner.PRIMARY_FILES))
    assert not (base / "failure").exists()


def test_atomic_commit_transition_retries_target_directory_fsync(
    monkeypatch,
    authorization,
):
    auth_path, _auth, base, candidate = authorization
    original_rename = runner.os.rename
    original_fsync = runner.os.fsync
    original_write_commit = runner._write_candidate_commit_control
    pending_transitioned = False
    candidate_fsync_failed = False
    finalized_control_attempted = False
    transition_fsync_attempts = 0

    def observe_pending_transition(source, destination, *args, **kwargs):
        nonlocal pending_transitioned
        result = original_rename(source, destination, *args, **kwargs)
        if source == runner.PENDING_FILE and destination == runner.COMMITTED_FILE:
            pending_transitioned = True
        return result

    def fail_first_candidate_fsync(fd):
        nonlocal candidate_fsync_failed, transition_fsync_attempts
        if pending_transitioned:
            transition_fsync_attempts += 1
        if pending_transitioned and not candidate_fsync_failed:
            candidate_fsync_failed = True
            raise OSError("fixture candidate directory fsync failure")
        return original_fsync(fd)

    def observe_finalized_control(
        context,
        auth,
        authorization_sha256,
        candidate_commit,
    ):
        nonlocal finalized_control_attempted
        if candidate_commit["finalized"] is True:
            finalized_control_attempted = True
        return original_write_commit(
            context,
            auth,
            authorization_sha256,
            candidate_commit,
        )

    monkeypatch.setattr(runner.os, "rename", observe_pending_transition)
    monkeypatch.setattr(runner.os, "fsync", fail_first_candidate_fsync)
    monkeypatch.setattr(
        runner,
        "_write_candidate_commit_control",
        observe_finalized_control,
    )

    assert _capture(authorization) == 0
    assert candidate_fsync_failed is True
    assert finalized_control_attempted is True
    assert transition_fsync_attempts >= 4
    assert candidate.is_dir()
    assert (base / "control" / runner.COMMITTED_FILE).is_file()
    assert not (base / "failure").exists()
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "PASS"


def test_atomic_commit_transition_fails_closed_when_target_fsync_retry_fails(
    monkeypatch,
    authorization,
):
    _auth_path, _auth, base, _candidate = authorization
    original_rename = runner.os.rename
    original_fsync = runner.os.fsync
    committed_transition_visible = False
    transition_fsync_attempts = 0

    def observe_transition(source, destination, *args, **kwargs):
        nonlocal committed_transition_visible
        result = original_rename(source, destination, *args, **kwargs)
        if source == runner.PENDING_FILE and destination == runner.COMMITTED_FILE:
            committed_transition_visible = True
        elif source == runner.COMMITTED_FILE and destination == runner.PENDING_FILE:
            committed_transition_visible = False
        return result

    def fail_committed_transition_fsync(fd):
        nonlocal transition_fsync_attempts
        if committed_transition_visible:
            transition_fsync_attempts += 1
            raise OSError("fixture persistent committed-transition fsync failure")
        return original_fsync(fd)

    monkeypatch.setattr(runner.os, "rename", observe_transition)
    monkeypatch.setattr(runner.os, "fsync", fail_committed_transition_fsync)

    assert _capture(authorization) == 1
    assert transition_fsync_attempts == 4
    assert not (base / "control" / runner.COMMITTED_FILE).exists()


def test_mutation_during_pending_commit_transition_remains_failed(
    monkeypatch,
    authorization,
):
    auth_path, _auth, base, candidate = authorization
    original_rename = runner.os.rename
    original_mkdir_open = runner._secure_mkdir_open

    def mutate_then_move(source, destination, *args, **kwargs):
        if source == runner.PENDING_FILE and destination == runner.COMMITTED_FILE:
            (candidate / "stdout.log").write_text(
                "mutated-at-commit\n",
                encoding="utf-8",
            )
        return original_rename(source, destination, *args, **kwargs)

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(runner.os, "rename", mutate_then_move)
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)

    assert _capture(authorization) == 1
    assert candidate.is_dir()
    assert (candidate / runner.PENDING_FILE).is_file()
    assert not (base / "failure").exists()
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False


def test_authorization_mutation_during_pending_commit_transition_cannot_commit(
    monkeypatch,
    authorization,
):
    auth_path, _auth, base, candidate = authorization
    original_rename = runner.os.rename
    original_mkdir_open = runner._secure_mkdir_open

    def mutate_authorization_then_move(source, destination, *args, **kwargs):
        if source == runner.PENDING_FILE and destination == runner.COMMITTED_FILE:
            auth_path.write_bytes(auth_path.read_bytes() + b" ")
        return original_rename(source, destination, *args, **kwargs)

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(runner.os, "rename", mutate_authorization_then_move)
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)

    assert _capture(authorization) == 1
    assert candidate.is_dir()
    assert (candidate / runner.PENDING_FILE).is_file()
    assert not (base / "failure").exists()
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False


def test_source_recheck_before_pending_unlink_cannot_be_recovered_as_success(
    monkeypatch,
    authorization,
):
    _auth_path, _auth, base, candidate = authorization
    parent_pid = os.getpid()
    parent_checks = 0
    original_mkdir_open = runner._secure_mkdir_open

    def source_changes_after_commit(_auth, *, enforce_repo=True):
        nonlocal parent_checks
        if os.getpid() != parent_pid:
            return None
        parent_checks += 1
        if parent_checks >= 3:
            raise runner.Ops03Error(
                "final_validation",
                "source_manifest_mismatch",
                consumed=True,
            )
        return None

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(runner, "validate_source_identity", source_changes_after_commit)
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)
    assert _capture(authorization) == 1
    assert parent_checks == 3
    assert candidate.is_dir()
    assert (candidate / runner.PENDING_FILE).is_file()
    assert not (base / "failure").exists()
    receipt = validator.validate_packet(
        _auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False


def test_mutation_during_finalized_control_write_cannot_commit(
    monkeypatch,
    authorization,
):
    auth_path, _auth, base, candidate = authorization
    original_write_commit = runner._write_candidate_commit_control
    original_mkdir_open = runner._secure_mkdir_open

    def mutate_before_finalized_control(
        context,
        auth,
        authorization_sha256,
        candidate_commit,
    ):
        if candidate_commit["finalized"] is True:
            (candidate / "stdout.log").write_text(
                "mutated-before-finalized-control\n",
                encoding="utf-8",
            )
        return original_write_commit(
            context,
            auth,
            authorization_sha256,
            candidate_commit,
        )

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(
        runner,
        "_write_candidate_commit_control",
        mutate_before_finalized_control,
    )
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)
    assert _capture(authorization) == 1
    assert candidate.is_dir()
    assert (candidate / runner.PENDING_FILE).is_file()
    assert not (base / "failure").exists()
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False


def test_authorization_mutation_after_finalized_control_cannot_commit(
    monkeypatch,
    authorization,
):
    auth_path, _auth, base, candidate = authorization
    original_authorization_bytes = auth_path.read_bytes()
    original_write_commit = runner._write_candidate_commit_control
    original_mkdir_open = runner._secure_mkdir_open

    def mutate_after_finalized_control(
        context,
        auth,
        authorization_sha256,
        candidate_commit,
    ):
        original_write_commit(
            context,
            auth,
            authorization_sha256,
            candidate_commit,
        )
        if candidate_commit["finalized"] is True:
            auth_path.write_bytes(auth_path.read_bytes() + b" ")

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(
        runner,
        "_write_candidate_commit_control",
        mutate_after_finalized_control,
    )
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)

    assert _capture(authorization) == 1
    assert candidate.is_dir()
    assert (candidate / runner.PENDING_FILE).is_file()
    assert not (base / "failure").exists()
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["authorization_valid"] is False
    auth_path.write_bytes(original_authorization_bytes)
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False
    consumption = json.loads(
        (base / "control/authorization_consumed.json").read_text(encoding="utf-8")
    )
    assert "candidate_commit" not in consumption


def test_failed_finalized_candidate_remains_poisoned_when_all_cleanup_paths_fail(
    monkeypatch,
    authorization,
):
    auth_path, _auth, base, candidate = authorization
    original_authorization_bytes = auth_path.read_bytes()
    original_write_commit = runner._write_candidate_commit_control
    original_mkdir_open = runner._secure_mkdir_open

    def mutate_after_finalized_control(
        context,
        auth,
        authorization_sha256,
        candidate_commit,
    ):
        original_write_commit(
            context,
            auth,
            authorization_sha256,
            candidate_commit,
        )
        if candidate_commit["finalized"] is True:
            auth_path.write_bytes(auth_path.read_bytes() + b" ")

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(
        runner,
        "_write_candidate_commit_control",
        mutate_after_finalized_control,
    )
    monkeypatch.setattr(
        runner,
        "_invalidate_candidate_commit_control",
        lambda *_args, **_kwargs: False,
    )
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)
    monkeypatch.setattr(
        runner,
        "_retain_candidate_failure_latch",
        lambda *_args, **_kwargs: False,
    )

    assert _capture(authorization) == 1
    assert candidate.is_dir()
    assert (candidate / runner.PENDING_FILE).is_file()
    assert not (candidate / runner.FAILURE_LATCH_FILE).exists()
    assert not (base / "failure").exists()
    auth_path.write_bytes(original_authorization_bytes)
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False


def test_restored_pending_transition_survives_verification_read_failure(
    monkeypatch,
    authorization,
):
    auth_path, _auth, base, candidate = authorization
    original_authorization_bytes = auth_path.read_bytes()
    original_rename = runner.os.rename
    original_fsync = runner.os.fsync
    original_read_file = runner._read_file
    original_mkdir_open = runner._secure_mkdir_open
    restored = False
    restored_fsync_failed = False
    restored_transition_fsync_attempts = 0

    def mutate_then_interrupt_restore(source, destination, *args, **kwargs):
        nonlocal restored
        result = original_rename(source, destination, *args, **kwargs)
        if source == runner.PENDING_FILE and destination == runner.COMMITTED_FILE:
            auth_path.write_bytes(auth_path.read_bytes() + b" ")
        elif source == runner.COMMITTED_FILE and destination == runner.PENDING_FILE:
            restored = True
            raise KeyboardInterrupt("fixture interruption after pending restoration")
        return result

    def interrupt_restored_pending_read(dir_fd, name):
        if restored and name == runner.PENDING_FILE:
            raise KeyboardInterrupt("fixture restored-pending verification interruption")
        return original_read_file(dir_fd, name)

    def fail_first_restored_fsync(fd):
        nonlocal restored_fsync_failed, restored_transition_fsync_attempts
        if restored:
            restored_transition_fsync_attempts += 1
        if restored and not restored_fsync_failed:
            restored_fsync_failed = True
            raise OSError("fixture restored transition fsync failure")
        return original_fsync(fd)

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(runner.os, "rename", mutate_then_interrupt_restore)
    monkeypatch.setattr(runner.os, "fsync", fail_first_restored_fsync)
    monkeypatch.setattr(runner, "_read_file", interrupt_restored_pending_read)
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)
    monkeypatch.setattr(
        runner,
        "_retain_candidate_failure_latch",
        lambda *_args, **_kwargs: False,
    )

    assert _capture(authorization) == 1
    assert restored is True
    assert restored_fsync_failed is True
    assert restored_transition_fsync_attempts >= 4
    assert (candidate / runner.PENDING_FILE).is_file()
    assert not (base / "control" / runner.COMMITTED_FILE).exists()
    assert not (base / "failure").exists()
    auth_path.write_bytes(original_authorization_bytes)
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False


def test_failed_pending_rollback_publishes_control_failure_marker(
    monkeypatch,
    authorization,
):
    auth_path, _auth, base, candidate = authorization
    original_authorization_bytes = auth_path.read_bytes()
    original_rename = runner.os.rename
    original_fsync = runner.os.fsync
    original_mkdir_open = runner._secure_mkdir_open
    rollback_failed = False
    failure_marker_published = False
    failure_marker_fsync_failed = False
    failure_marker_fsync_attempts = 0

    def mutate_then_fail_rollback(source, destination, *args, **kwargs):
        nonlocal failure_marker_published, rollback_failed
        if source == runner.COMMITTED_FILE and destination == runner.PENDING_FILE:
            rollback_failed = True
            raise OSError("fixture pending rollback failure")
        result = original_rename(source, destination, *args, **kwargs)
        if source == runner.PENDING_FILE and destination == runner.COMMITTED_FILE:
            auth_path.write_bytes(auth_path.read_bytes() + b" ")
        elif source == runner.COMMITTED_FILE and destination == runner.FAILED_COMMIT_FILE:
            failure_marker_published = True
        return result

    def fail_first_failure_marker_fsync(fd):
        nonlocal failure_marker_fsync_failed, failure_marker_fsync_attempts
        if failure_marker_published:
            failure_marker_fsync_attempts += 1
        if failure_marker_published and not failure_marker_fsync_failed:
            failure_marker_fsync_failed = True
            raise OSError("fixture failure-marker fsync failure")
        return original_fsync(fd)

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(runner.os, "rename", mutate_then_fail_rollback)
    monkeypatch.setattr(runner.os, "fsync", fail_first_failure_marker_fsync)
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)
    monkeypatch.setattr(
        runner,
        "_invalidate_candidate_commit_control",
        lambda *_args, **_kwargs: False,
    )
    monkeypatch.setattr(
        runner,
        "_retain_candidate_failure_latch",
        lambda *_args, **_kwargs: False,
    )

    assert _capture(authorization) == 1
    assert rollback_failed is True
    assert failure_marker_fsync_failed is True
    assert failure_marker_fsync_attempts >= 2
    assert not (candidate / runner.PENDING_FILE).exists()
    assert not (base / "control" / runner.COMMITTED_FILE).exists()
    assert (base / "control" / runner.FAILED_COMMIT_FILE).is_file()
    assert not (base / "failure").exists()
    auth_path.write_bytes(original_authorization_bytes)
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["authorization_valid"] is False


def test_source_mutation_after_finalized_control_cannot_commit(
    monkeypatch,
    authorization,
):
    _auth_path, _auth, base, candidate = authorization
    original_write_commit = runner._write_candidate_commit_control
    original_source_check = runner.validate_source_identity
    finalized_published = False

    def publish_then_mutate_source(
        context,
        auth,
        authorization_sha256,
        candidate_commit,
    ):
        nonlocal finalized_published
        original_write_commit(
            context,
            auth,
            authorization_sha256,
            candidate_commit,
        )
        if candidate_commit["finalized"] is True:
            finalized_published = True

    def reject_mutated_source(auth, *, enforce_repo=True):
        if finalized_published:
            raise runner.Ops03Error(
                "final_validation",
                "source_manifest_mismatch",
                consumed=True,
            )
        return original_source_check(auth, enforce_repo=enforce_repo)

    monkeypatch.setattr(
        runner,
        "_write_candidate_commit_control",
        publish_then_mutate_source,
    )
    monkeypatch.setattr(runner, "validate_source_identity", reject_mutated_source)

    assert _capture(authorization) == 1
    assert finalized_published is True
    assert not candidate.exists()
    failure = json.loads(
        (base / "failure/failure_receipt.json").read_text(encoding="utf-8")
    )
    assert failure["phase"] == "final_validation"
    assert failure["code"] == "candidate_commit_finalized_state_invalid"
    assert failure["launch_consumed"] is True


@pytest.mark.parametrize("exception_kind", ("ops03_error", "base_exception"))
def test_exception_after_terminal_commit_returns_committed_success(
    monkeypatch,
    authorization,
    exception_kind,
):
    auth_path, _auth, base, candidate = authorization
    original_commit = runner._commit_candidate

    def commit_then_interrupt(*args, **kwargs):
        original_commit(*args, **kwargs)
        if exception_kind == "ops03_error":
            raise runner.Ops03Error(
                "final_validation",
                "fixture_post_commit_error",
                consumed=True,
            )
        raise KeyboardInterrupt("fixture interruption after terminal commit")

    monkeypatch.setattr(runner, "_commit_candidate", commit_then_interrupt)
    monkeypatch.setattr(
        runner,
        "write_failure",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("committed success must not write failure")
        ),
    )
    monkeypatch.setattr(
        runner,
        "_discard_candidate",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("committed success must not discard candidate")
        ),
    )

    assert _capture(authorization) == 0
    assert not (base / "failure").exists()
    assert tuple(sorted(path.name for path in candidate.iterdir())) == tuple(
        sorted(runner.PRIMARY_FILES)
    )
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "PASS"


@pytest.mark.parametrize("failing_helper", ("write_failure", "discard_candidate"))
def test_failure_actions_are_independently_baseexception_contained(
    monkeypatch,
    authorization,
    failing_helper,
):
    _auth_path, _auth, base, candidate = authorization
    original_write_failure = runner.write_failure
    original_discard = runner._discard_candidate
    calls: list[str] = []

    def observed_write_failure(*args, **kwargs):
        calls.append("write_failure")
        if failing_helper == "write_failure":
            raise KeyboardInterrupt("fixture failure receipt interruption")
        return original_write_failure(*args, **kwargs)

    def observed_discard(context):
        calls.append("discard_candidate")
        if failing_helper == "discard_candidate":
            raise KeyboardInterrupt("fixture discard interruption")
        return original_discard(context)

    monkeypatch.setattr(runner, "write_failure", observed_write_failure)
    monkeypatch.setattr(runner, "_discard_candidate", observed_discard)
    assert _capture(authorization, builder=_provider_builder(fail_posture=True)) == 1
    assert calls == ["write_failure", "discard_candidate"]
    if failing_helper == "write_failure":
        assert not candidate.exists()
        assert not (base / "failure").exists()
    else:
        assert candidate.is_dir()
        assert (candidate / runner.PENDING_FILE).is_file()
        assert (base / "failure/failure_receipt.json").is_file()


def test_outer_runner_boundary_contains_authorization_recovery_interrupt(
    monkeypatch,
    authorization,
):
    auth_path, _auth, _base, _candidate = authorization

    def reject_initial_read(_path):
        raise runner.Ops03Error(
            "pre_marker",
            "authorization_unreadable",
            consumed=False,
        )

    def interrupt_recovery(_path):
        raise KeyboardInterrupt("fixture authorization recovery interruption")

    monkeypatch.setattr(runner, "_read_canonical_json", reject_initial_read)
    monkeypatch.setattr(runner, "_read_json_noncanonical", interrupt_recovery)
    assert _capture(authorization) == 1
    assert "DATABASE_URL" not in os.environ


@pytest.mark.parametrize(
    "mutation",
    [
        lambda candidate: (candidate / "stdout.log").write_text("arbitrary\n", encoding="utf-8"),
        lambda candidate: (candidate / "stderr.log").write_text("postgresql://secret\n", encoding="utf-8"),
        lambda candidate: (candidate / "extra.txt").write_text("extra\n", encoding="utf-8"),
        lambda candidate: (candidate / "extra-dir").mkdir(),
    ],
)
def test_validator_rejects_arbitrary_secret_and_extra_content(authorization, mutation):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    mutation(candidate)
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"


@pytest.mark.parametrize(
    "secret_marker",
    (
        "postgresql://user:password@example.invalid/database\n",
        "Authorization: Bearer retained-secret\n",
        "HD-Geocode-Key: retained-secret\n",
        "DATABASE_URL=retained-secret\n",
        "birth_date=2000-01-01\n",
        'raw_vendor_payload: {"retained": "secret"}\n',
    ),
)
def test_validator_rejects_each_retained_secret_marker_class(
    authorization,
    secret_marker,
):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    (candidate / "stderr.log").write_text(secret_marker, encoding="utf-8")

    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["secret_scan_valid"] is False


def test_validator_does_not_import_repo_helper_after_source_failure(
    monkeypatch,
    authorization,
):
    auth_path, _auth, _base, candidate = authorization
    imported_names: list[str] = []
    original_import = builtins.__import__

    def guarded_import(name, *args, **kwargs):
        imported_names.append(name)
        if name == "tools.evidence.retained_evidence_safety":
            raise AssertionError("repository helper imported after source failure")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(
        validator,
        "source_identity_errors",
        lambda *_args, **_kwargs: ("source_manifest_mismatch",),
    )
    monkeypatch.setattr(builtins, "__import__", guarded_import)
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=True,
        now=NOW,
    )

    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["source_identity_valid"] is False
    assert "tools.evidence.retained_evidence_safety" not in imported_names


def test_pending_latch_blocks_when_failure_root_and_cleanup_both_fail(monkeypatch, authorization):
    auth_path, _auth, base, candidate = authorization
    original_source = runner.validate_source_identity
    original_mkdir_open = runner._secure_mkdir_open
    source_checks = 0

    def fail_after_capture(auth, *, enforce_repo=True):
        nonlocal source_checks
        source_checks += 1
        if source_checks == 2:
            raise runner.Ops03Error("capture", "source_manifest_mismatch", consumed=True)
        return original_source(auth, enforce_repo=enforce_repo)

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    monkeypatch.setattr(runner, "validate_source_identity", fail_after_capture)
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)
    assert _capture(authorization) == 1
    assert not (base / "failure").exists()
    assert (candidate / runner.PENDING_FILE).is_file()
    assert (base / "control/authorization_consumed.json").is_file()
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"


def test_pending_latch_requires_ephemeral_runner_token(monkeypatch, authorization):
    auth_path, auth, _base, _candidate = authorization
    authorization_sha256 = runner.sha256_path(auth_path)
    pending_token = b"x" * 32
    raw = runner._pending_payload(auth, authorization_sha256, pending_token)
    monkeypatch.setattr(validator.os, "getppid", lambda: os.getpid())
    assert not validator._pending_latch_authorized(
        raw,
        auth,
        authorization_sha256,
        auth["exact_argv"]["receipt"],
        "receipt",
        b"y" * 32,
    )
    assert validator._pending_latch_authorized(
        raw,
        auth,
        authorization_sha256,
        auth["exact_argv"]["receipt"],
        "receipt",
        pending_token,
    )


@pytest.mark.parametrize(
    "filename",
    (
        "db_posture_summary.json",
        "env_presence.json",
        "nonclaims.json",
        "result_summary.json",
    ),
)
def test_validator_rejects_noncanonical_primary_json(authorization, filename):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    path = candidate / filename
    value = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["canonical_bytes_valid"] is False


def test_validator_binds_exact_mode_argv(authorization):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
        actual_argv=["/tmp/not-python"],
        mode="receipt",
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["authorization_valid"] is False


def test_validator_rejects_candidate_outside_authorized_root(authorization, tmp_path):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    other = tmp_path / "candidate"
    shutil.copytree(candidate, other)
    receipt = validator.validate_packet(
        auth_path,
        other,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["authorization_valid"] is False


def test_runner_rejects_dirty_environment_before_provider_and_marker(authorization):
    _auth_path, auth, base, candidate = authorization
    calls = []

    def builder(_counters):
        return lambda dsn: calls.append(dsn) or FixtureProvider()

    assert _capture(authorization, env={**CLEAN_ENV, "HOME": "/tmp"}, builder=builder) == 1
    assert calls == []
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["code"] == "environment_not_clean"
    assert failure["launch_consumed"] is False
    assert failure["authorization_sha256"] == runner.sha256_path(_auth_path)


def test_post_marker_failure_discards_candidate_and_consumes_authorization(authorization):
    _auth_path, _auth, base, candidate = authorization
    assert _capture(authorization, builder=_provider_builder(fail_posture=True)) == 1
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["candidate_admissible"] is False
    assert failure["launch_consumed"] is True
    assert failure["code"] == "unexpected_failure"


def test_successful_authorization_cannot_be_reused(authorization):
    _auth_path, _auth, base, candidate = authorization
    assert _capture(authorization) == 0
    original = {path.name: path.read_bytes() for path in candidate.iterdir()}
    assert _capture(authorization) == 1
    assert {path.name: path.read_bytes() for path in candidate.iterdir()} == original
    assert not (base / "failure").exists()


def test_invalid_run_id_cannot_escape_failure_root(tmp_path):
    runner.write_failure(
        {"run_id": "../../escape"},
        "0" * 64,
        phase="pre_marker",
        code="authorization_schema_invalid",
        consumed=False,
    )
    assert not (tmp_path / "escape").exists()


@pytest.mark.parametrize(
    "mutator",
    [
        lambda auth: auth.update({"schema": "hde_epic038.ops03.authorization.v0"}),
        lambda auth: auth.update({"run_id": "bad"}),
        lambda auth: auth.update({"authorized_at_utc": "2026-07-21T11:00:00"}),
        lambda auth: auth.update({"expires_at_utc": "2026-07-21T10:00:00Z"}),
        lambda auth: auth["target"].update({"app_env": "prod"}),
        lambda auth: auth["rails"].update({"safe_mode": "0"}),
        lambda auth: auth["retired_keys_required_absent"].pop(),
        lambda auth: auth["ordered_query_ids"].reverse(),
        lambda auth: auth["expected_counts"].update({"provider_selections": 2}),
        lambda auth: auth.update({"candidate_root": "/tmp/not-authorized/"}),
        lambda auth: auth["exact_argv"]["capture"].append("--unexpected"),
        lambda auth: auth.update({"one_attempt": False}),
    ],
)
def test_authorization_rejects_each_bound_contract_mutation(authorization, mutator):
    auth_path, auth, _base, _candidate = authorization
    mutated = copy.deepcopy(auth)
    mutator(mutated)
    auth_path.write_bytes(runner.canonical_bytes(mutated))

    with pytest.raises(runner.Ops03Error):
        runner.validate_authorization(mutated, auth_path, now=NOW)


def test_authorization_schema_rejects_every_field_and_vector_node_mutation(authorization):
    auth_path, auth, _base, _candidate = authorization
    for path in _contract_node_paths(auth):
        mutated = copy.deepcopy(auth)
        _replace_contract_node(mutated, path)
        auth_path.write_bytes(runner.canonical_bytes(mutated))
        with pytest.raises(runner.Ops03Error):
            runner.validate_authorization(mutated, auth_path, now=NOW)
    auth_path.write_bytes(runner.canonical_bytes(auth))


@pytest.mark.parametrize("mode", ("capture", "receipt", "validate"))
def test_authorization_rejects_same_type_mutation_of_each_argv_vector(
    authorization,
    mode,
):
    auth_path, auth, _base, _candidate = authorization
    mutated = copy.deepcopy(auth)
    mutated["exact_argv"][mode][-1] = "/tmp/not-the-authorized-argument"
    auth_path.write_bytes(runner.canonical_bytes(mutated))

    with pytest.raises(runner.Ops03Error):
        runner.validate_authorization(mutated, auth_path, now=NOW)


@pytest.mark.parametrize(
    ("mutator", "expected_code"),
    [
        (lambda auth: auth.update({"runner_sha256": "f" * 64}), "runner_hash_mismatch"),
        (lambda auth: auth.update({"validator_sha256": "f" * 64}), "validator_hash_mismatch"),
        (
            lambda auth: auth["interpreter"].update({"sha256": "f" * 64}),
            "interpreter_hash_mismatch",
        ),
        (
            lambda auth: auth["interpreter"].update({"resolved_path": "/tmp/not-python"}),
            "interpreter_path_mismatch",
        ),
    ],
)
def test_source_identity_rejects_each_bound_hash_or_path(
    authorization,
    mutator,
    expected_code,
):
    _auth_path, auth, _base, _candidate = authorization
    mutated = copy.deepcopy(auth)
    mutator(mutated)

    with pytest.raises(runner.Ops03Error) as exc:
        runner.validate_source_identity(mutated, enforce_repo=False)
    assert exc.value.code == expected_code
    assert expected_code in validator.source_identity_errors(mutated, enforce_repo=False)


@pytest.mark.parametrize("count_name", tuple(runner.EXPECTED_COUNTS))
def test_validator_rejects_each_authorized_count_mutation(authorization, count_name):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    path = candidate / "db_posture_summary.json"
    posture = json.loads(path.read_text(encoding="utf-8"))
    posture["counts"][count_name] += 1
    path.write_bytes(runner.canonical_bytes(posture))

    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["counts_valid"] is False


@pytest.mark.parametrize(
    ("filename", "mutator"),
    [
        ("env_presence.json", lambda value: value.update({"app_env": "prod"})),
        ("nonclaims.json", lambda value: value["nonclaims"].pop()),
        (
            "result_summary.json",
            lambda value: value.update({"authorization_sha256": "f" * 64}),
        ),
        (
            "db_posture_summary.json",
            lambda value: value["ordered_query_ids"].reverse(),
        ),
    ],
)
def test_validator_rejects_bound_primary_field_mutations(
    authorization,
    filename,
    mutator,
):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    path = candidate / filename
    value = json.loads(path.read_text(encoding="utf-8"))
    mutator(value)
    path.write_bytes(runner.canonical_bytes(value))

    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"


def test_validator_rejects_every_primary_json_field_node_mutation(authorization):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    for filename in (
        "db_posture_summary.json",
        "env_presence.json",
        "nonclaims.json",
        "result_summary.json",
    ):
        path = candidate / filename
        original = path.read_bytes()
        value = json.loads(original)
        for node_path in _contract_node_paths(value):
            mutated = copy.deepcopy(value)
            _replace_contract_node(mutated, node_path)
            path.write_bytes(runner.canonical_bytes(mutated))
            receipt = validator.validate_packet(
                auth_path,
                candidate,
                final=False,
                enforce_source=False,
                now=NOW,
            )
            assert receipt["result"] == "FAIL", (filename, node_path)
        path.write_bytes(original)


def test_final_validator_rejects_checksum_and_receipt_tampering(authorization):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    assert _seal(auth_path, candidate)["result"] == "PASS"

    receipt_path = candidate / validator.RECEIPT_FILE
    original_receipt = receipt_path.read_bytes()
    receipt_value = json.loads(original_receipt)
    receipt_value["authorization_sha256"] = "f" * 64
    receipt_path.write_bytes(validator.canonical_bytes(receipt_value))
    runner.write_checksums(candidate)
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=True,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False

    receipt_path.write_bytes(original_receipt)
    runner.write_checksums(candidate)
    checksum = candidate / validator.CHECKSUM_FILE
    checksum.write_text(
        checksum.read_text(encoding="ascii") + "0" * 64 + "  extra.txt\n",
        encoding="ascii",
    )
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=True,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["inventory_valid"] is False


def test_final_validator_rejects_each_checksum_input_mutation(authorization):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    assert _seal(auth_path, candidate)["result"] == "PASS"
    checksum_path = candidate / validator.CHECKSUM_FILE
    original_lines = checksum_path.read_text(encoding="ascii").splitlines()

    for name in validator.CHECKSUM_INPUTS:
        mutated_lines = list(original_lines)
        line_index = next(
            index
            for index, line in enumerate(mutated_lines)
            if line.endswith(f"  {name}")
        )
        original_digest, separator, original_name = mutated_lines[line_index].partition(
            "  "
        )
        replacement_digest = "f" * 64 if original_digest != "f" * 64 else "e" * 64
        mutated_lines[line_index] = f"{replacement_digest}{separator}{original_name}"
        checksum_path.write_text("\n".join(mutated_lines) + "\n", encoding="ascii")

        receipt = validator.validate_packet(
            auth_path,
            candidate,
            final=True,
            enforce_source=False,
            now=NOW,
        )
        assert receipt["result"] == "FAIL", name
        assert receipt["predicates"]["inventory_valid"] is False, name

    checksum_path.write_text("\n".join(original_lines) + "\n", encoding="ascii")


def test_pr_a_missing_ops03_stops_natural_pipeline_at_stage14(
    tmp_path,
    monkeypatch,
):
    from tools.evidence import run_sanity_pipeline as sanity

    log = tmp_path / "sanity.log"
    calls = []

    def pass_command(command):
        calls.append(command)
        return subprocess.CompletedProcess(command, 0, b"", b"")

    for key, value in sanity.DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr(sanity, "SANITY_LOG", log)
    monkeypatch.setattr(sanity, "_run_command", pass_command)
    monkeypatch.setattr(sanity, "validate_pr05_path_proof_prerequisites", lambda: None)
    monkeypatch.setattr(sanity, "validate_direct_selection_contract", lambda: None)
    monkeypatch.setattr(sanity, "validate_historical_bridge_evidence", lambda: None)
    monkeypatch.setattr(sanity, "validate_ops02_package", lambda: None)
    monkeypatch.setattr(
        sanity,
        "validate_ops03_tracked_packet",
        lambda: (_ for _ in ()).throw(
            sanity.Ops03PacketUnavailable(sanity.PR_A_NONFINAL_REASON)
        ),
    )
    monkeypatch.setattr(sanity, "_rebind_failure_log", lambda: 0)

    steps = sanity.default_steps()
    assert len(steps) == 19
    assert steps[13].commands == (("__validate_ops03__",),)
    assert sanity.run_pipeline(log_path=log) == sanity.PR_A_NONFINAL_EXIT
    lines = log.read_text(encoding="utf-8").splitlines()
    assert [line for line in lines if line.startswith("check ")] == [
        f"check {name}:{'OK' if index < 13 else 'FAIL'}"
        for index, name in enumerate(sanity.STAGE_NAMES)
    ]
    for name in sanity.STAGE_NAMES[14:]:
        assert (
            f"not_executed {name}:"
            f"earlier_mandatory_failure={sanity.STAGE_NAMES[13]}"
            in lines
        )
    assert not any(
        command in calls for step in steps[14:] for command in step.commands
    )
    assert f"first_failed_stage:{sanity.STAGE_NAMES[13]}" in lines
    assert "summary:FAIL" in lines
    assert "summary:PASS" not in lines


@pytest.mark.parametrize(
    "ignored_path",
    ("engine/shadow/native.so", "engine/shadow/native.pyd", "jsonschema.py"),
)
def test_source_identity_rejects_ignored_import_modules(
    monkeypatch,
    authorization,
    ignored_path,
):
    _auth_path, auth, _base, _candidate = authorization

    def fake_git(args):
        class Completed:
            returncode = 0
            stdout = ""
        result = Completed()
        if args[:4] == ("ls-files", "--others", "--ignored", "--exclude-standard"):
            result.stdout = ignored_path + "\n"
        elif args[:2] == ("rev-parse", "HEAD"):
            result.stdout = auth["source_commit"] + "\n"
        return result

    monkeypatch.setattr(runner, "_git", fake_git)
    monkeypatch.setattr(validator, "_git", fake_git)
    monkeypatch.setattr(Path, "rglob", lambda self, pattern: iter(()))
    with pytest.raises(runner.Ops03Error) as exc:
        runner.validate_source_identity(auth, enforce_repo=True)
    assert exc.value.code == "ignored_native_module_present"
    assert "ignored_native_module_present" in validator.source_identity_errors(auth, enforce_repo=True)


def test_source_identity_rejects_preimport_dirty_or_shadow_code(monkeypatch, authorization):
    _auth_path, auth, _base, _candidate = authorization

    def fake_git(args):
        class Completed:
            returncode = 0
            stdout = ""
        result = Completed()
        if args[:2] == ("rev-parse", "HEAD"):
            result.stdout = auth["source_commit"] + "\n"
        return result

    monkeypatch.setattr(runner, "_git", fake_git)
    monkeypatch.setattr(runner, "_source_manifest_auxiliary_error", lambda: "source_tree_not_pristine")
    monkeypatch.setattr(Path, "rglob", lambda self, pattern: iter(()))
    with pytest.raises(runner.Ops03Error) as exc:
        runner.validate_source_identity(auth, enforce_repo=True)
    assert exc.value.code == "source_tree_not_pristine"


def test_runner_source_boundary_precedes_schema_imports(monkeypatch, authorization):
    auth_path, _auth, _base, _candidate = authorization
    events = []

    def reject_source(_auth, *, enforce_repo=True):
        events.append("source")
        raise runner.Ops03Error("pre_marker", "source_tree_not_pristine", consumed=False)

    def forbidden_schema(*_args, **_kwargs):
        events.append("schema")
        raise AssertionError("schema validation ran before source authorization")

    monkeypatch.setattr(runner, "validate_source_identity", reject_source)
    monkeypatch.setattr(runner, "validate_authorization", forbidden_schema)
    assert _capture(authorization) == 1
    assert events == ["source"]


def test_validator_source_boundary_precedes_schema_imports(monkeypatch, authorization):
    auth_path, _auth, _base, candidate = authorization
    events = []

    def reject_source(_auth, *, enforce_repo=True):
        events.append("source")
        return ("source_tree_not_pristine",)

    def forbidden_schema(*_args, **_kwargs):
        events.append("schema")
        raise AssertionError("schema validation ran before source authorization")

    monkeypatch.setattr(validator, "source_identity_errors", reject_source)
    monkeypatch.setattr(validator, "authorization_errors", forbidden_schema)
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=True,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert events == ["source"]


def test_validator_terminal_admission_rechecks_authorization_bytes(
    monkeypatch,
    authorization,
):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    assert _seal(auth_path, candidate)["result"] == "PASS"
    original_admission = validator._admission_state_stable
    mutated = False

    def mutate_after_admission(*args, **kwargs):
        nonlocal mutated
        result = original_admission(*args, **kwargs)
        if not mutated:
            mutated = True
            auth_path.write_bytes(auth_path.read_bytes() + b" ")
        return result

    monkeypatch.setattr(
        validator,
        "_admission_state_stable",
        mutate_after_admission,
    )
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=True,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["authorization_valid"] is False


def test_validator_terminal_admission_rechecks_source_identity(
    monkeypatch,
    authorization,
):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    assert _seal(auth_path, candidate)["result"] == "PASS"
    source_checks = 0

    def source_changes_at_terminal_check(*_args, **_kwargs):
        nonlocal source_checks
        source_checks += 1
        return () if source_checks == 1 else ("source_manifest_mismatch",)

    monkeypatch.setattr(
        validator,
        "source_identity_errors",
        source_changes_at_terminal_check,
    )
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=True,
        enforce_source=True,
        now=NOW,
    )
    assert source_checks == 2
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["source_identity_valid"] is False


def test_validator_rechecks_admission_after_terminal_source_identity(
    monkeypatch,
    authorization,
):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    assert _seal(auth_path, candidate)["result"] == "PASS"
    source_checks = 0

    def mutate_candidate_at_terminal_source_check(*_args, **_kwargs):
        nonlocal source_checks
        source_checks += 1
        if source_checks == 2:
            (candidate / "stdout.log").write_text(
                "mutated-during-terminal-source-check\n",
                encoding="utf-8",
            )
        return ()

    monkeypatch.setattr(
        validator,
        "source_identity_errors",
        mutate_candidate_at_terminal_source_check,
    )
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=True,
        enforce_source=False,
        now=NOW,
    )
    assert source_checks == 2
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["authorization_valid"] is False


@pytest.mark.parametrize("mutation", ("missing", "content", "valid_content"))
def test_validator_requires_exact_committed_transition_marker(
    authorization,
    mutation,
):
    auth_path, _auth, base, candidate = authorization
    assert _capture(authorization) == 0
    marker = base / "control" / runner.COMMITTED_FILE
    if mutation == "missing":
        marker.unlink()
    elif mutation == "valid_content":
        value = json.loads(marker.read_text(encoding="utf-8"))
        value["runner_token_sha256"] = "f" * 64
        marker.write_bytes(validator.canonical_bytes(value))
    else:
        marker.write_text("mutated\n", encoding="utf-8")
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["authorization_valid"] is False


def test_parseable_noncanonical_authorization_emits_pre_marker_receipt(authorization):
    auth_path, auth, base, candidate = authorization
    noncanonical = (json.dumps(auth, indent=2) + "\n").encode("utf-8")
    auth_path.write_bytes(noncanonical)
    calls = []

    def builder(_counters):
        return lambda dsn: calls.append(dsn) or FixtureProvider()

    assert _capture(authorization, builder=builder) == 1
    assert calls == []
    assert not (base / "control/launch.marker").exists()
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["code"] == "authorization_not_canonical"
    assert failure["phase"] == "pre_marker"
    assert failure["launch_consumed"] is False
    assert failure["authorization_sha256"] == runner.sha256_bytes(noncanonical)


def test_partial_marker_record_failure_is_consumed(monkeypatch, authorization):
    _auth_path, _auth, base, candidate = authorization
    original = runner._write_new_file

    def flaky_write(dir_fd, name, payload):
        if name == "authorization_consumed.json":
            raise OSError("fixture record failure")
        return original(dir_fd, name, payload)

    monkeypatch.setattr(runner, "_write_new_file", flaky_write)
    assert _capture(authorization) == 1
    assert (base / "control/launch.marker").read_bytes() == b"launch_consumed=true\n"
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["code"] == "authorization_consumption_record_write_failed"
    assert failure["launch_consumed"] is True


def test_control_inventory_read_failure_after_marker_is_consumed(monkeypatch, authorization):
    _auth_path, _auth, base, candidate = authorization
    original_listdir = runner.os.listdir
    failed = False

    def fail_after_control_persisted(path):
        nonlocal failed
        entries = original_listdir(path)
        if not failed and isinstance(path, int) and set(entries) == {
            "authorization_consumed.json",
            "launch.marker",
        }:
            failed = True
            raise OSError("fixture control inventory read failure")
        return entries

    monkeypatch.setattr(runner.os, "listdir", fail_after_control_persisted)
    assert _capture(authorization) == 1
    assert failed is True
    assert not candidate.exists()
    assert (base / "control/launch.marker").is_file()
    assert (base / "control/authorization_consumed.json").is_file()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["phase"] == "pre_provider"
    assert failure["launch_consumed"] is True


@pytest.mark.parametrize("unlink_fails", [False, True])
def test_partial_launch_marker_never_contradicts_consumption(
    monkeypatch,
    authorization,
    unlink_fails,
):
    _auth_path, _auth, base, candidate = authorization
    original_write_all = runner._write_all
    original_unlink = runner.os.unlink
    calls = []

    def partial_marker(fd, payload):
        if payload == b"launch_consumed=true\n":
            runner.os.write(fd, payload[:7])
            raise OSError("partial marker")
        return original_write_all(fd, payload)

    def maybe_deny_unlink(name, *args, **kwargs):
        if unlink_fails and name == "launch.marker":
            raise OSError("marker cleanup denied")
        return original_unlink(name, *args, **kwargs)

    def builder(_counters):
        return lambda dsn: calls.append(dsn) or FixtureProvider()

    monkeypatch.setattr(runner, "_write_all", partial_marker)
    monkeypatch.setattr(runner.os, "unlink", maybe_deny_unlink)
    assert _capture(authorization, builder=builder) == 1
    assert calls == []
    assert not candidate.exists()
    marker = base / "control/launch.marker"
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert marker.exists() is unlink_fails
    assert failure["launch_consumed"] is unlink_fails
    assert failure["phase"] == ("pre_provider" if unlink_fails else "pre_marker")


def test_completed_launch_marker_then_base_exception_is_consumed(monkeypatch, authorization):
    _auth_path, _auth, base, candidate = authorization
    original = runner._write_new_file
    provider_calls = []

    def persist_then_interrupt(dir_fd, name, payload):
        original(dir_fd, name, payload)
        if name == "launch.marker":
            raise KeyboardInterrupt("fixture post-persist interruption")

    def builder(_counters):
        return lambda dsn: provider_calls.append(dsn) or FixtureProvider()

    monkeypatch.setattr(runner, "_write_new_file", persist_then_interrupt)
    assert _capture(authorization, builder=builder) == 1
    assert provider_calls == []
    assert not candidate.exists()
    assert (base / "control/launch.marker").read_bytes() == b"launch_consumed=true\n"
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["phase"] == "pre_provider"
    assert failure["launch_consumed"] is True


def test_child_ops03_error_phase_and_code_are_preserved(monkeypatch, authorization):
    _auth_path, _auth, base, candidate = authorization

    def fail_posture(*_args, **_kwargs):
        raise runner.Ops03Error("capture", "posture_predicate_failed", consumed=True)

    monkeypatch.setattr(runner, "build_posture", fail_posture)
    assert _capture(authorization) == 1
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["phase"] == "capture"
    assert failure["code"] == "posture_predicate_failed"
    assert failure["launch_consumed"] is True


@pytest.mark.parametrize(
    "flag_index",
    range(7),
    ids=(
        "superuser",
        "create-db",
        "create-role",
        "replication",
        "bypass-rls",
        "schema-create",
        "relation-write",
    ),
)
def test_runtime_role_elevated_capability_cannot_pass(flag_index, authorization):
    _auth_path, _auth, base, candidate = authorization
    role = [False] * 7
    role[flag_index] = True
    assert _capture(authorization, builder=_provider_builder(role_row=tuple(role))) == 1
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["code"] == "posture_predicate_failed"


def test_runtime_role_query_detects_sequence_write_privileges():
    sql = runner.QUERY_STATEMENTS[4].sql
    assert "seq.relkind = 'S'" in sql
    assert "aclexplode(COALESCE(seq.relacl, acldefault('s', seq.relowner)))" in sql
    assert "seq_acl.privilege_type <> 'SELECT'" in sql
    assert "seq_acl.grantee = 0" in sql
    assert "pg_has_role(current_user, seq_acl.grantee, 'USAGE')" in sql


@pytest.mark.parametrize(
    "partition_rows",
    (
        (
            ("hde.pair_evaluation", "h", "HASH (evaluated_at)"),
            ("hde.public_results", "r", "RANGE (created_at)"),
        ),
        (
            ("hde.pair_evaluation", "r", "RANGE (release_id)"),
            ("hde.public_results", "r", "RANGE (created_at)"),
        ),
        (
            ("hde.pair_evaluation", "r", "RANGE (evaluated_at)"),
            ("hde.public_results", "r", "RANGE (release_id)"),
        ),
    ),
    ids=("wrong-strategy", "wrong-pair-key", "wrong-results-key"),
)
def test_partition_strategy_or_key_mismatch_cannot_pass(
    partition_rows,
    authorization,
):
    _auth_path, _auth, base, candidate = authorization
    assert _capture(
        authorization,
        builder=_provider_builder(partition_rows=partition_rows),
    ) == 1
    assert not candidate.exists()
    failure = json.loads(
        (base / "failure/failure_receipt.json").read_text(encoding="utf-8")
    )
    assert failure["code"] == "posture_predicate_failed"
    assert failure["launch_consumed"] is True


@pytest.mark.parametrize(
    "capability_index",
    range(2, 7),
    ids=(
        "updatable",
        "insertable",
        "trigger-update",
        "trigger-delete",
        "trigger-insert",
    ),
)
def test_boundary_view_write_capability_cannot_pass(capability_index, authorization):
    _auth_path, _auth, base, candidate = authorization
    first = ["hde", "body_graphs_current", "NO", "NO", "NO", "NO", "NO"]
    first[capability_index] = "YES"
    boundaries = (
        tuple(first),
        ("public", "hde_body_graphs_current", "NO", "NO", "NO", "NO", "NO"),
    )
    assert _capture(
        authorization,
        builder=_provider_builder(boundary_rows=boundaries),
    ) == 1
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["code"] == "posture_predicate_failed"


def test_run_root_symlink_rejected_before_marker(authorization, tmp_path):
    _auth_path, _auth, base, candidate = authorization
    target = tmp_path / "outside"
    target.mkdir()
    base.symlink_to(target, target_is_directory=True)
    try:
        assert _capture(authorization) == 1
        assert not candidate.exists()
        assert not (base / "control/launch.marker").exists()
        assert list(target.iterdir()) == []
    finally:
        base.unlink(missing_ok=True)


def test_failure_root_symlink_never_receives_outside_write(authorization, tmp_path):
    _auth_path, _auth, base, candidate = authorization
    outside = tmp_path / "outside-failure"
    outside.mkdir()

    def builder(_counters):
        def factory(_dsn):
            (base / "failure").symlink_to(outside, target_is_directory=True)
            raise RuntimeError("fixture provider failure")

        return factory

    assert _capture(authorization, builder=builder) == 1
    assert not candidate.exists()
    assert list(outside.iterdir()) == []


def test_stale_failure_receipt_bytes_are_not_reused_or_overwritten(authorization):
    _auth_path, _auth, base, candidate = authorization
    stale = b'{"stale":true}\n'
    failure = base / "failure"
    failure.mkdir(parents=True)
    (failure / "failure_receipt.json").write_bytes(stale)
    assert _capture(authorization) == 1
    assert not candidate.exists()
    assert (failure / "failure_receipt.json").read_bytes() == stale


def test_stale_failure_receipt_makes_final_validation_authoritative(authorization):
    auth_path, _auth, base, candidate = authorization
    assert _capture(authorization) == 0
    failure_dir = base / "failure"
    failure_dir.mkdir()
    (failure_dir / "failure_receipt.json").write_bytes(b'{"stale":true}\n')
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["authorization_valid"] is False


def test_preexisting_and_unwritable_roots_are_contained(authorization, monkeypatch):
    _auth_path, _auth, base, candidate = authorization
    base.mkdir(parents=True)
    assert _capture(authorization) == 1
    assert not candidate.exists()
    assert not (base / "failure").exists()

    shutil.rmtree(base)
    real_mkdir = runner.os.mkdir

    def deny_mkdir(path, *args, **kwargs):
        if path == base.name:
            raise PermissionError("fixture denied")
        return real_mkdir(path, *args, **kwargs)

    monkeypatch.setattr(runner.os, "mkdir", deny_mkdir)
    assert _capture(authorization) == 1


def test_late_failure_cleanup_and_receipt_failure_blocks_readmission(monkeypatch, authorization):
    auth_path, _auth, base, candidate = authorization
    original_source_check = runner.validate_source_identity
    source_checks = 0

    def fail_after_capture(auth, *, enforce_repo=True):
        nonlocal source_checks
        source_checks += 1
        if source_checks == 2:
            raise runner.Ops03Error("capture", "source_manifest_mismatch", consumed=True)
        return original_source_check(auth, enforce_repo=enforce_repo)

    original_write = runner._write_new_file

    def fail_receipt(dir_fd, name, payload):
        if name == "failure_receipt.json":
            raise OSError("receipt denied")
        return original_write(dir_fd, name, payload)

    monkeypatch.setattr(runner, "validate_source_identity", fail_after_capture)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)
    monkeypatch.setattr(runner, "_write_new_file", fail_receipt)
    assert _capture(authorization) == 1
    assert candidate.exists()
    assert tuple(sorted(path.name for path in candidate.iterdir())) == tuple(
        sorted(
            (
                *runner.PRIMARY_FILES,
                runner.PENDING_FILE,
                runner.FAILURE_LATCH_FILE,
            )
        )
    )
    assert (base / "failure").is_dir()
    assert not (base / "failure/failure_receipt.json").exists()
    consumption = json.loads((base / "control/authorization_consumed.json").read_text(encoding="utf-8"))
    assert consumption["launch_consumed"] is True
    assert consumption["authorization_sha256"] == runner.sha256_path(auth_path)
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"


def test_partial_candidate_cleanup_keeps_pending_latch_until_last(monkeypatch, authorization):
    auth_path, _auth, base, candidate = authorization
    original_source = runner.validate_source_identity
    original_mkdir_open = runner._secure_mkdir_open
    original_unlink = runner.os.unlink
    source_checks = 0

    def fail_after_capture(auth, *, enforce_repo=True):
        nonlocal source_checks
        source_checks += 1
        if source_checks == 2:
            raise runner.Ops03Error("capture", "source_manifest_mismatch", consumed=True)
        return original_source(auth, enforce_repo=enforce_repo)

    def deny_failure_root(parent_fd, name):
        if name == "failure":
            raise PermissionError("fixture denies failure root")
        return original_mkdir_open(parent_fd, name)

    def fail_first_primary(name, *args, **kwargs):
        if name == "commands.txt":
            raise OSError("fixture cleanup failure")
        return original_unlink(name, *args, **kwargs)

    monkeypatch.setattr(runner, "validate_source_identity", fail_after_capture)
    monkeypatch.setattr(runner, "_secure_mkdir_open", deny_failure_root)
    monkeypatch.setattr(runner.os, "unlink", fail_first_primary)
    assert _capture(authorization) == 1
    assert not (base / "failure").exists()
    assert (candidate / runner.PENDING_FILE).is_file()
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"


def test_parent_scrubs_database_url_before_bootstrap_and_marker(monkeypatch, authorization):
    auth_path, _auth, _base, _candidate = authorization
    parent_pid = os.getpid()
    observed = []
    original_source = runner.validate_source_identity
    original_marker = runner._write_marker

    class TrapEnvironment(dict):
        def __contains__(self, key):
            if key == "DATABASE_URL":
                raise AssertionError("parent membership must not decode DATABASE_URL")
            return super().__contains__(key)

    process_environment = TrapEnvironment(CLEAN_ENV)

    def source_probe(auth, *, enforce_repo=True):
        if os.getpid() == parent_pid:
            observed.append("source")
            assert "DATABASE_URL" not in set(runner.os.environ)
        return original_source(auth, enforce_repo=enforce_repo)

    def marker_probe(context, auth, authorization_sha256):
        observed.append("marker")
        assert "DATABASE_URL" not in set(runner.os.environ)
        return original_marker(context, auth, authorization_sha256)

    monkeypatch.setattr(runner.os, "environ", process_environment)
    monkeypatch.setattr(runner, "validate_source_identity", source_probe)
    monkeypatch.setattr(runner, "_write_marker", marker_probe)
    assert runner.capture(
        auth_path,
        ambient=None,
        provider_factory_builder=_provider_builder(),
        enforce_source=False,
        invoke_validators=False,
        now=NOW,
    ) == 0
    assert observed[:2] == ["source", "marker"]
    assert "DATABASE_URL" not in set(process_environment)


def test_parent_database_url_scrub_failure_aborts_before_source_or_marker(monkeypatch, authorization):
    auth_path, _auth, base, candidate = authorization
    parent_pid = os.getpid()
    source_calls = []
    provider_calls = []
    original_source = runner.validate_source_identity

    class RefusingEnvironment(dict):
        def __delitem__(self, key):
            if key == "DATABASE_URL":
                raise OSError("fixture refuses DATABASE_URL deletion")
            return super().__delitem__(key)

    def source_probe(auth, *, enforce_repo=True):
        if os.getpid() == parent_pid:
            source_calls.append(True)
        return original_source(auth, enforce_repo=enforce_repo)

    def builder(_counters):
        return lambda dsn: provider_calls.append(dsn) or FixtureProvider()

    process_environment = RefusingEnvironment(CLEAN_ENV)
    monkeypatch.setattr(runner.os, "environ", process_environment)
    monkeypatch.setattr(runner, "validate_source_identity", source_probe)
    assert runner.capture(
        auth_path,
        ambient=None,
        provider_factory_builder=builder,
        enforce_source=False,
        invoke_validators=False,
        now=NOW,
    ) == 1
    assert source_calls == []
    assert provider_calls == []
    assert not (base / "control/launch.marker").exists()
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["code"] == "parent_database_url_scrub_failed"
    assert failure["launch_consumed"] is False


def test_empty_database_url_fails_before_marker_without_provider(authorization):
    _auth_path, _auth, base, candidate = authorization
    calls = []

    def builder(_counters):
        return lambda dsn: calls.append(dsn) or FixtureProvider()

    assert _capture(authorization, env={**CLEAN_ENV, "DATABASE_URL": ""}, builder=builder) == 1
    assert calls == []
    assert not (base / "control/launch.marker").exists()
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["phase"] == "pre_marker"
    assert failure["launch_consumed"] is False


def test_candidate_replacement_failure_is_persisted_before_cleanup(monkeypatch, authorization, tmp_path):
    auth_path, _auth, base, candidate = authorization
    original_source = runner.validate_source_identity
    source_checks = 0
    displaced = tmp_path / "displaced-candidate"

    def replace_after_capture(auth, *, enforce_repo=True):
        nonlocal source_checks
        source_checks += 1
        if source_checks == 2:
            candidate.rename(displaced)
            shutil.copytree(displaced, candidate)
            raise runner.Ops03Error("capture", "source_manifest_mismatch", consumed=True)
        return original_source(auth, enforce_repo=enforce_repo)

    monkeypatch.setattr(runner, "validate_source_identity", replace_after_capture)
    assert _capture(authorization) == 1
    assert candidate.is_dir()
    assert (base / "failure").is_dir()
    assert (base / "control/authorization_consumed.json").is_file()
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"


def test_failure_directory_replacement_retries_visible_state(monkeypatch, authorization):
    auth_path, _auth, base, candidate = authorization
    original_source = runner.validate_source_identity
    original_mkdir_open = runner._secure_mkdir_open
    source_checks = 0
    displaced_once = False

    def fail_after_capture(auth, *, enforce_repo=True):
        nonlocal source_checks
        source_checks += 1
        if source_checks == 2:
            raise runner.Ops03Error("capture", "source_manifest_mismatch", consumed=True)
        return original_source(auth, enforce_repo=enforce_repo)

    def displace_failure(parent_fd, name):
        nonlocal displaced_once
        fd = original_mkdir_open(parent_fd, name)
        if name == "failure" and not displaced_once:
            displaced_once = True
            os.rename("failure", "displaced-failure", src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        return fd

    monkeypatch.setattr(runner, "validate_source_identity", fail_after_capture)
    monkeypatch.setattr(runner, "_secure_mkdir_open", displace_failure)
    monkeypatch.setattr(runner, "_discard_candidate", lambda _context: False)
    assert _capture(authorization) == 1
    assert displaced_once is True
    assert candidate.is_dir()
    assert (base / "failure/failure_receipt.json").is_file()
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"


def test_unwritable_run_base_cannot_validate_surviving_candidate(monkeypatch, authorization):
    auth_path, _auth, base, candidate = authorization
    original_source = runner.validate_source_identity
    source_checks = 0

    def chmod_after_capture(auth, *, enforce_repo=True):
        nonlocal source_checks
        source_checks += 1
        if source_checks == 2:
            base.chmod(0o500)
            raise runner.Ops03Error("capture", "source_manifest_mismatch", consumed=True)
        return original_source(auth, enforce_repo=enforce_repo)

    monkeypatch.setattr(runner, "validate_source_identity", chmod_after_capture)
    try:
        assert _capture(authorization) == 1
        assert candidate.is_dir()
        receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
        assert receipt["result"] == "FAIL"
    finally:
        base.chmod(0o700)


def test_post_capture_source_failure_has_consumed_non_premarker_phase(monkeypatch, authorization):
    _auth_path, _auth, base, candidate = authorization
    original_source = runner.validate_source_identity
    source_checks = 0

    def fail_second_parent_check(auth, *, enforce_repo=True):
        nonlocal source_checks
        source_checks += 1
        if source_checks == 2:
            raise runner.Ops03Error("pre_marker", "source_manifest_mismatch", consumed=False)
        return original_source(auth, enforce_repo=enforce_repo)

    monkeypatch.setattr(runner, "validate_source_identity", fail_second_parent_check)
    assert _capture(authorization) == 1
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["phase"] == "capture"
    assert failure["launch_consumed"] is True
    assert (base / "control/authorization_consumed.json").is_file()


def test_validator_rechecks_inventory_and_failure_state_before_pass(monkeypatch, authorization):
    auth_path, _auth, base, candidate = authorization
    assert _capture(authorization) == 0
    original_snapshot = validator._snapshot_candidate
    calls = 0

    def mutate_after_snapshot(context):
        nonlocal calls
        files, regular = original_snapshot(context)
        calls += 1
        if calls == 2:
            (base / "failure").mkdir()
        return files, regular

    monkeypatch.setattr(validator, "_snapshot_candidate", mutate_after_snapshot)
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert calls == 2
    assert receipt["result"] == "FAIL"


def test_validator_rejects_extra_run_base_entry(authorization):
    auth_path, _auth, base, candidate = authorization
    assert _capture(authorization) == 0
    (base / "extra-root").mkdir()
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"


def test_validator_rechecks_failure_after_last_control_read(monkeypatch, authorization):
    auth_path, _auth, base, candidate = authorization
    assert _capture(authorization) == 0
    original_read = validator._read_file
    consumption_reads = 0

    def mutate_on_last_control_read(dir_fd, name):
        nonlocal consumption_reads
        payload = original_read(dir_fd, name)
        if name == "authorization_consumed.json":
            consumption_reads += 1
            if consumption_reads == 3:
                (base / "failure").mkdir()
        return payload

    monkeypatch.setattr(validator, "_read_file", mutate_on_last_control_read)
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert consumption_reads == 3
    assert receipt["result"] == "FAIL"


def test_validator_rejects_inventory_added_during_snapshot(monkeypatch, authorization):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    original_read = validator._read_bound_file
    last_name = sorted(runner.PRIMARY_FILES)[-1]

    def inject_extra(dir_fd, name):
        result = original_read(dir_fd, name)
        if name == last_name:
            (candidate / "extra.txt").write_text("late\n", encoding="utf-8")
        return result

    monkeypatch.setattr(validator, "_read_bound_file", inject_extra)
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"


def test_ignored_native_pathspec_uses_real_git_repository(monkeypatch, tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    (repo / ".gitignore").write_text("*.so\n*.pyd\n", encoding="utf-8")
    (repo / "engine/shadow").mkdir(parents=True)
    (repo / "engine/shadow/native.so").write_bytes(b"fixture")
    (repo / "engine/shadow/native.pyd").write_bytes(b"fixture")
    monkeypatch.setattr(runner, "ROOT", repo)
    result = runner._git(("ls-files", "--others", "--ignored", "--exclude-standard", "--", "*.so", "*.pyd"))
    assert result.returncode == 0
    assert set(result.stdout.splitlines()) == {"engine/shadow/native.so", "engine/shadow/native.pyd"}


def _commit_test_repository(repo: Path) -> str:
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    subprocess.run(["git", "-C", str(repo), "add", "-A"], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(repo),
            "-c",
            "user.name=OPS-03 Test",
            "-c",
            "user.email=ops03@example.invalid",
            "commit",
            "-qm",
            "fixture",
        ],
        check=True,
    )
    return subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


@pytest.mark.parametrize("flag", ("--skip-worktree", "--assume-unchanged"))
def test_source_manifest_rejects_hidden_index_mutation(monkeypatch, tmp_path, flag):
    repo = tmp_path / "repo"
    repo.mkdir()
    module = repo / "module.py"
    module.write_text("VALUE = 1\n", encoding="utf-8")
    _commit_test_repository(repo)
    subprocess.run(["git", "-C", str(repo), "update-index", flag, "module.py"], check=True)
    module.write_text("VALUE = 2\n", encoding="utf-8")
    monkeypatch.setattr(runner, "ROOT", repo)
    monkeypatch.setattr(validator, "ROOT", repo)
    assert runner._source_manifest_auxiliary_error() == "source_index_flags_unsafe"
    assert validator._source_manifest_auxiliary_error() == "source_index_flags_unsafe"


@pytest.mark.parametrize("module", (runner, validator))
def test_source_manifest_binds_tracked_symlink_without_following_it(
    monkeypatch, tmp_path, module
):
    repo = tmp_path / "repo"
    repo.mkdir()
    target = repo / "target.py"
    target.write_text("VALUE = 1\n", encoding="utf-8")
    linked = repo / "linked.py"
    linked.symlink_to("target.py")
    _commit_test_repository(repo)
    monkeypatch.setattr(module, "ROOT", repo)

    assert module._source_manifest_auxiliary_error() is None
    raw = module._raw_worktree_entry("linked.py")
    assert raw == (b"target.py", "120000")

    linked.unlink()
    linked.symlink_to("other.py")
    assert module._source_manifest_auxiliary_error() == "source_manifest_mismatch"

    linked.unlink()
    linked.write_text("target.py", encoding="utf-8")
    assert module._source_manifest_auxiliary_error() == "source_manifest_mismatch"


@pytest.mark.parametrize("module", (runner, validator))
def test_current_head_tracked_symlink_blobs_match_without_dereference(module):
    result = subprocess.run(
        ["git", "-C", str(module.ROOT), "ls-tree", "-r", "-z", "--full-tree", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    entries = module._manifest_entries(result.stdout, index=False)
    assert entries is not None
    symlinks = {
        relative: object_id
        for relative, (mode, object_id) in entries.items()
        if mode == "120000"
    }
    assert symlinks

    for relative, object_id in symlinks.items():
        worktree = module._raw_worktree_entry(relative)
        assert worktree is not None
        payload, mode = worktree
        blob = hashlib.sha1(
            f"blob {len(payload)}\0".encode("ascii") + payload
        ).hexdigest()
        assert mode == "120000"
        assert blob == object_id


def test_source_manifest_rejects_git_replacement_objects(monkeypatch, tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    module = repo / "module.py"
    module.write_text("VALUE = 'authorized'\n", encoding="utf-8")
    authorized = _commit_test_repository(repo)
    module.write_text("VALUE = 'replacement'\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(repo), "add", "module.py"], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(repo),
            "-c",
            "user.name=OPS-03 Test",
            "-c",
            "user.email=ops03@example.invalid",
            "commit",
            "-qm",
            "replacement",
        ],
        check=True,
    )
    replacement = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    subprocess.run(["git", "-C", str(repo), "replace", authorized, replacement], check=True)
    monkeypatch.setattr(runner, "ROOT", repo)
    monkeypatch.setattr(validator, "ROOT", repo)
    assert runner._source_manifest_auxiliary_error() == "source_replacement_ref_present"
    assert validator._source_manifest_auxiliary_error() == "source_replacement_ref_present"


def test_source_manifest_pins_configured_worktree(monkeypatch, tmp_path):
    repo = tmp_path / "repo"
    alternate = tmp_path / "alternate"
    repo.mkdir()
    alternate.mkdir()
    (repo / "module.py").write_text("VALUE = 'authorized'\n", encoding="utf-8")
    _commit_test_repository(repo)
    shutil.copy2(repo / "module.py", alternate / "module.py")
    subprocess.run(["git", "-C", str(repo), "config", "core.worktree", str(alternate)], check=True)
    (repo / "module.py").write_text("VALUE = 'unauthorized'\n", encoding="utf-8")
    monkeypatch.setattr(runner, "ROOT", repo)
    monkeypatch.setattr(validator, "ROOT", repo)
    assert runner._source_manifest_auxiliary_error() == "source_manifest_mismatch"
    assert validator._source_manifest_auxiliary_error() == "source_manifest_mismatch"


def test_source_manifest_ignores_local_clean_filter_normalization(monkeypatch, tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    module = repo / "module.py"
    module.write_text("VALUE = 'authorized'\n", encoding="utf-8")
    _commit_test_repository(repo)
    info = repo / ".git/info/attributes"
    info.write_text("module.py filter=conceal\n", encoding="utf-8")
    subprocess.run(
        [
            "git",
            "-C",
            str(repo),
            "config",
            "filter.conceal.clean",
            "sed s/unauthorized/authorized/",
        ],
        check=True,
    )
    module.write_text("VALUE = 'unauthorized'\n", encoding="utf-8")
    monkeypatch.setattr(runner, "ROOT", repo)
    monkeypatch.setattr(validator, "ROOT", repo)
    assert runner._source_manifest_auxiliary_error() == "source_manifest_mismatch"
    assert validator._source_manifest_auxiliary_error() == "source_manifest_mismatch"


def test_isolated_runner_rejects_ignored_symlink_package_before_import(tmp_path):
    repo = tmp_path / "repo"
    (repo / "scripts/ops").mkdir(parents=True)
    (repo / "tools/evidence").mkdir(parents=True)
    copied_runner = repo / "scripts/ops/hde_epic038_ops03.py"
    copied_validator = repo / "tools/evidence/hde_epic038_ops03.py"
    shutil.copy2(runner.RUNNER, copied_runner)
    shutil.copy2(runner.VALIDATOR, copied_validator)
    (repo / ".gitignore").write_text(
        "tools/evidence/strict_json_schema.py\n", encoding="utf-8"
    )
    source_commit = _commit_test_repository(repo)
    sentinel = tmp_path / "shadow-imported"
    shadow_target = tmp_path / "strict_json_schema.py"
    shadow_target.write_text(
        f"from pathlib import Path\nPath({str(sentinel)!r}).write_text('imported', encoding='utf-8')\n",
        encoding="utf-8",
    )
    (repo / "tools/evidence/strict_json_schema.py").symlink_to(shadow_target)
    run_id = "ops03-test-" + uuid.uuid4().hex[:24]
    base, _control, candidate, _failure = runner.derived_paths(run_id)
    auth_path = tmp_path / "authorization.json"
    interpreter = Path(sys.executable).resolve()
    common = [str(interpreter), "-I", "-B"]
    auth = {
        "schema": "hde_epic038.ops03.authorization.v1",
        "run_id": run_id,
        "authorized_at_utc": "2026-07-21T11:00:00Z",
        "expires_at_utc": "2026-07-21T13:00:00Z",
        "source_commit": source_commit,
        "runner_sha256": runner.sha256_path(copied_runner),
        "validator_sha256": runner.sha256_path(copied_validator),
        "interpreter": {
            "resolved_path": str(interpreter),
            "sha256": runner.sha256_path(interpreter),
        },
        "target": {"app_env": "dev", "database_schema": "hde", "search_path": ["hde", "public"]},
        "rails": {"safe_mode": "1", "allow_network": "0", "allow_db_write": "0", "db_read_authorized": True},
        "retired_keys_required_absent": list(runner.RETIRED_DB_TRANSPORT_KEYS),
        "ordered_query_ids": list(runner.ORDERED_QUERY_IDS),
        "expected_counts": runner.EXPECTED_COUNTS,
        "candidate_root": candidate.as_posix() + "/",
        "exact_argv": {
            "capture": [*common, str(copied_runner), "--authorization", str(auth_path)],
            "receipt": [*common, str(copied_validator), "--emit-receipt", "--authorization", str(auth_path), "--candidate", str(candidate)],
            "validate": [*common, str(copied_validator), "--validate", "--authorization", str(auth_path), "--candidate", str(candidate)],
        },
        "one_attempt": True,
    }
    auth_path.write_bytes(runner.canonical_bytes(auth))
    try:
        completed = subprocess.run(
            auth["exact_argv"]["capture"],
            check=False,
            cwd=repo,
            env=CLEAN_ENV,
            capture_output=True,
        )
        assert completed.returncode == 1
        assert not sentinel.exists()
        assert not (base / "control/launch.marker").exists()
        assert not candidate.exists()
        failure = json.loads(
            (base / "failure/failure_receipt.json").read_text(encoding="utf-8")
        )
        assert failure["code"] == "ignored_source_symlink_present"
    finally:
        shutil.rmtree(base, ignore_errors=True)


def test_provider_child_has_separate_pid_and_clean_dsn_environment(
    monkeypatch,
    authorization,
    tmp_path,
):
    auth_path, _auth, base, _candidate = authorization
    probe = tmp_path / "provider_probe.json"
    imports_probe = tmp_path / "repo_import_pids.json"
    original_symbols = runner._repo_db_symbols

    def observed_symbols():
        seen = []
        if imports_probe.exists():
            seen = json.loads(imports_probe.read_text(encoding="utf-8"))
        seen.append(os.getpid())
        imports_probe.write_bytes(runner.canonical_bytes(seen))
        return original_symbols()

    def builder(counters):
        def factory(dsn):
            probe.write_bytes(runner.canonical_bytes({
                "parent_pid": os.getppid(),
                "child_pid": os.getpid(),
                "dsn": dsn,
                "python_keys": sorted(k for k in os.environ if k.startswith("PYTHON")),
                "env": dict(os.environ),
            }))
            counters.provider_selections += 1
            return runner.CountingProvider(FixtureProvider(), counters, count_connections_by_call=True)

        return factory

    clean_process_env = dict(CLEAN_ENV)
    monkeypatch.setattr(runner.os, "environ", clean_process_env)
    monkeypatch.setattr(runner, "_repo_db_symbols", observed_symbols)
    assert runner.capture(
        auth_path,
        ambient=None,
        provider_factory_builder=builder,
        enforce_source=False,
        invoke_validators=False,
        now=NOW,
    ) == 0
    seen = json.loads(probe.read_text(encoding="utf-8"))
    assert seen["child_pid"] != os.getpid()
    assert seen["dsn"] == CLEAN_ENV["DATABASE_URL"]
    assert seen["python_keys"] == []
    assert seen["env"] == CLEAN_ENV
    assert "DATABASE_URL" not in clean_process_env
    assert set(json.loads(imports_probe.read_text(encoding="utf-8"))) == {seen["child_pid"]}
    assert tuple(sorted(path.name for path in (base / "control").iterdir())) == (
        runner.COMMITTED_FILE,
        "authorization_consumed.json",
        "launch.marker",
    )


def test_provider_child_rechecks_control_after_final_read(monkeypatch, authorization):
    _auth_path, _auth, base, candidate = authorization
    original_read = runner._read_file
    provider_calls = []

    def mutate_after_consumption_read(dir_fd, name):
        payload = original_read(dir_fd, name)
        if name == "authorization_consumed.json":
            try:
                runner._write_new_file(dir_fd, "extra-control", b"unexpected\n")
            except FileExistsError:
                pass
        return payload

    def builder(_counters):
        return lambda dsn: provider_calls.append(dsn) or FixtureProvider()

    monkeypatch.setattr(runner, "_read_file", mutate_after_consumption_read)
    assert _capture(authorization, builder=builder) == 1
    assert provider_calls == []
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["code"] == "control_state_invalid"
    assert failure["launch_consumed"] is True


def test_provider_child_partial_pipe_setup_closes_owned_fds(monkeypatch, authorization):
    _auth_path, _auth, base, candidate = authorization
    real_pipe = runner.os.pipe
    allocated_fds = []
    pipe_calls = 0
    provider_calls = []

    def fail_second_pipe():
        nonlocal pipe_calls
        pipe_calls += 1
        if pipe_calls == 2:
            raise OSError("fixture pipe allocation failure")
        pair = real_pipe()
        allocated_fds.extend(pair)
        return pair

    def builder(_counters):
        return lambda dsn: provider_calls.append(dsn) or FixtureProvider()

    monkeypatch.setattr(runner.os, "pipe", fail_second_pipe)
    assert _capture(authorization, builder=builder) == 1
    assert provider_calls == []
    assert not (base / "control/launch.marker").exists()
    assert not candidate.exists()
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["phase"] == "pre_marker"
    assert failure["code"] == "provider_child_setup_failed"
    assert failure["launch_consumed"] is False
    for fd in allocated_fds:
        with pytest.raises(OSError):
            os.fstat(fd)


def test_pipe_read_deadline_is_bounded():
    read_fd, write_fd = os.pipe()
    try:
        with pytest.raises(TimeoutError):
            runner._read_pipe(read_fd, timeout_seconds=0.01)
    finally:
        os.close(read_fd)
        os.close(write_fd)


def test_provider_child_status_timeout_is_controlled(
    monkeypatch,
    authorization,
):
    _auth_path, _auth, base, candidate = authorization
    parent_pid = os.getpid()
    original_read_pipe = runner._read_pipe
    parent_reads = 0

    def timeout_parent_status(fd, *args, **kwargs):
        nonlocal parent_reads
        if os.getpid() == parent_pid:
            parent_reads += 1
            if parent_reads == 2:
                raise TimeoutError("fixture provider status timeout")
        return original_read_pipe(fd, *args, **kwargs)

    monkeypatch.setattr(runner, "_read_pipe", timeout_parent_status)
    assert _capture(authorization) == 1
    assert not candidate.exists()
    failure = json.loads(
        (base / "failure/failure_receipt.json").read_text(encoding="utf-8")
    )
    assert failure["code"] == "provider_child_timeout"
    assert failure["launch_consumed"] is True


def test_independent_validator_timeout_is_controlled(monkeypatch):
    argv = ["python", "--emit-receipt"]

    def timeout_run(*args, **kwargs):
        assert kwargs["timeout"] == runner.VALIDATOR_TIMEOUT_SECONDS
        raise subprocess.TimeoutExpired(args[0], kwargs["timeout"])

    monkeypatch.setattr(runner.subprocess, "run", timeout_run)
    with pytest.raises(runner.Ops03Error) as exc:
        runner._run_validator(argv, pending_token=b"x" * 32)
    assert exc.value.phase == "receipt_validation"
    assert exc.value.code == "independent_validator_timeout"
    assert exc.value.consumed is True


def test_git_timeouts_are_bounded_and_fail_closed(monkeypatch, authorization):
    _auth_path, auth, _base, _candidate = authorization
    timeouts = []

    def timeout_run(*args, **kwargs):
        timeouts.append(kwargs.get("timeout"))
        raise subprocess.TimeoutExpired(args[0], kwargs["timeout"])

    monkeypatch.setattr(runner.subprocess, "run", timeout_run)
    with pytest.raises(runner.Ops03Error):
        runner.validate_source_identity(auth, enforce_repo=True)
    assert validator.source_identity_errors(auth, enforce_repo=True)
    assert timeouts
    assert set(timeouts) == {
        runner.GIT_TIMEOUT_SECONDS,
        validator.GIT_TIMEOUT_SECONDS,
    }


def test_provider_abort_is_bounded_and_contains_syscall_failures(monkeypatch):
    kills = []

    monkeypatch.setattr(runner.os, "waitpid", lambda _pid, _options: (0, 0))

    def failing_kill(pid, signal_number):
        kills.append((pid, signal_number))
        raise PermissionError("fixture kill denied")

    monkeypatch.setattr(runner.os, "kill", failing_kill)
    started = runner.time.monotonic()
    assert runner._terminate_and_reap(123456, grace_seconds=0) is False
    assert runner.time.monotonic() - started < 0.25
    assert kills == [(123456, runner.signal.SIGTERM), (123456, runner.signal.SIGKILL)]

    child = runner.ProviderChild(123456, -1, -1, -1)
    monkeypatch.setattr(
        runner,
        "_terminate_and_reap",
        lambda _pid: (_ for _ in ()).throw(KeyboardInterrupt("fixture cleanup interrupt")),
    )
    runner._abort_provider_child(child)
    assert child.completed is True


def test_validator_rejects_authorized_candidate_symlink(authorization, tmp_path):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    outside = tmp_path / "external-candidate"
    candidate.rename(outside)
    candidate.symlink_to(outside, target_is_directory=True)
    receipt = validator.validate_packet(
        auth_path,
        candidate,
        final=False,
        enforce_source=False,
        now=NOW,
    )
    assert receipt["result"] == "FAIL"
    assert tuple(sorted(path.name for path in outside.iterdir())) == tuple(sorted(runner.PRIMARY_FILES))
