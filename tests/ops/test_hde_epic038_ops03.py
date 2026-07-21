from __future__ import annotations

import datetime as dt
import json
import shutil
import sys
import uuid
from pathlib import Path

import pytest

from scripts.ops import hde_epic038_ops03 as runner
from tools.evidence import hde_epic038_ops03 as validator

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


class FixtureProvider:
    name = "psycopg"

    def __init__(self, *, fail_posture: bool = False):
        self.fail_posture = fail_posture

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
            [(False, False, False)],
            [("id", "uuid", "NO", "gen_random_uuid()")],
            [("body_graphs_pkey", "PRIMARY KEY (id)")],
            [
                ("hde", "body_graphs_current", "NO", "NO", "NO"),
                ("public", "hde_body_graphs_current", "NO", "NO", "NO"),
            ],
            [
                ("hde.pair_evaluation", "r", "release_id"),
                ("hde.public_results", "r", "release_id"),
            ],
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


def _provider_builder(*, fail_posture: bool = False):
    def builder(counters):
        def factory(_dsn):
            counters.provider_selections += 1
            return runner.CountingProvider(
                FixtureProvider(fail_posture=fail_posture),
                counters,
                count_connections_by_call=True,
            )

        return factory

    return builder


@pytest.fixture
def authorization(tmp_path):
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
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "PASS"
    (candidate / validator.RECEIPT_FILE).write_bytes(validator.canonical_bytes(receipt))
    runner.write_checksums(candidate)
    return validator.validate_packet(auth_path, candidate, final=True, enforce_source=False, now=NOW)


def test_runner_builds_exact_semantic_packet_and_validator_seals_it(authorization):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    assert tuple(sorted(path.name for path in candidate.iterdir())) == tuple(sorted(runner.PRIMARY_FILES))
    final = _seal(auth_path, candidate)
    assert final["result"] == "PASS"
    assert tuple(sorted(path.name for path in candidate.iterdir())) == validator.FINAL_FILES


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


def test_validator_rejects_noncanonical_and_schema_mutated_json(authorization):
    auth_path, _auth, _base, candidate = authorization
    assert _capture(authorization) == 0
    path = candidate / "env_presence.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    value["unexpected"] = True
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    receipt = validator.validate_packet(auth_path, candidate, final=False, enforce_source=False, now=NOW)
    assert receipt["result"] == "FAIL"
    assert receipt["predicates"]["schemas_valid"] is False
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
    failure = json.loads((base / "failure/failure_receipt.json").read_text(encoding="utf-8"))
    assert failure["code"] == "authorization_already_consumed"


def test_invalid_run_id_cannot_escape_failure_root(tmp_path):
    runner.write_failure(
        {"run_id": "../../escape"},
        "0" * 64,
        phase="pre_marker",
        code="authorization_schema_invalid",
        consumed=False,
    )
    assert not (tmp_path / "escape").exists()
