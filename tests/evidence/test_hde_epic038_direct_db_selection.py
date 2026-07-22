from __future__ import annotations

import copy
import json
from collections.abc import Mapping

import pytest

from tools.evidence import generate_hde_epic038_direct_db_selection as generator


def test_direct_selection_generation_is_exact_canonical_and_checkable(tmp_path):
    out = tmp_path / "direct.json"
    assert generator.main(["--out", str(out)]) == 0
    first = out.read_bytes()
    assert generator.main(["--out", str(out), "--check"]) == 0
    second_out = tmp_path / "direct-second.json"
    assert generator.main(["--out", str(second_out)]) == 0
    assert second_out.read_bytes() == first
    raw = out.read_bytes()
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n")
    assert raw == generator.canonical_bytes(json.loads(raw))
    payload = json.loads(raw)
    assert generator.validate_contract(payload) == ()
    assert payload["result"] == "PASS"
    assert [row["case"] for row in payload["cases"]] == [
        "healthy_direct",
        "missing_database_url",
        "unavailable_database_url",
        "retired_keys_present",
    ]
    assert payload["cases"][3]["attempts"] == []
    assert all(row["alternate_transport_attempts"] == 0 for row in payload["cases"])


@pytest.mark.parametrize(
    "mutator",
    [
        lambda value: value.update({"unexpected": True}),
        lambda value: value["cases"][0].update({"unexpected": True}),
        lambda value: value["cases"][0]["attempts"][0].update({"unexpected": True}),
        lambda value: value["cases"][1]["error"].update({"unexpected": True}),
        lambda value: value["predicates"].update({"unexpected": True}),
        lambda value: value.update(
            {"failure": {"code": "predicate_failure", "failed_predicates": [], "unexpected": True}}
        ),
    ],
)
def test_direct_selection_schema_rejects_unknown_keys_at_every_object_level(mutator):
    payload = copy.deepcopy(generator.build())
    mutator(payload)
    assert "schema_invalid" in generator.validate_contract(payload)


def test_direct_selection_producer_writes_schema_valid_negative_receipt(monkeypatch, tmp_path):
    original = generator.run_case

    def mutated(case, environ, *, fail=False):
        row = original(case, environ, fail=fail)
        if case == "healthy_direct":
            row["selected"] = "none"
            row["result"] = "FAIL"
        return row

    monkeypatch.setattr(generator, "run_case", mutated)
    out = tmp_path / "direct.json"
    assert generator.main(["--out", str(out)]) == 1
    payload = json.loads(out.read_bytes())
    assert generator.validate_contract(payload) == ()
    assert payload["result"] == "FAIL"
    assert payload["failure"] == {
        "code": "predicate_failure",
        "failed_predicates": ["direct_only_provider"],
    }
    assert payload["predicates"]["secret_values_absent"] is True
    assert out.read_bytes() == generator.canonical_bytes(payload)
    assert generator.main(["--out", str(out), "--check"]) == 1


def test_direct_selection_validator_rejects_case_and_secret_mutation():
    payload = copy.deepcopy(generator.build())
    payload["cases"][0]["selected"] = "none"
    assert "predicate_value_invalid" in generator.validate_contract(payload)

    payload = copy.deepcopy(generator.build())
    payload["cases"][0]["app_env"] = "postgresql://must-not-survive"
    errors = generator.validate_contract(payload)
    assert "schema_invalid" in errors
    assert "secret_values_present" in errors

    payload = copy.deepcopy(generator.build())
    payload["predicates"]["direct_only_provider"] = False
    errors = generator.validate_contract(payload)
    assert "schema_invalid" in errors
    assert "predicate_value_invalid" in errors
    assert "failure_receipt_invalid" in errors

    payload["cases"][0]["selected"] = "none"
    payload["cases"][0]["result"] = "FAIL"
    payload["result"] = "FAIL"
    payload["failure"] = {
        "code": "predicate_failure",
        "failed_predicates": ["direct_only_provider"],
    }
    assert generator.validate_contract(payload) == ()


def test_retired_case_uses_membership_even_for_empty_values():
    row = generator.run_case(
        "retired_keys_present",
        {
            "APP_ENV": "dev",
            "DATABASE_URL": "not-serialized",
            **{name: "" for name in generator.RETIRED_DB_TRANSPORT_KEYS},
        },
    )
    assert row["attempts"] == []
    assert row["retired_keys_present"] == list(generator.RETIRED_DB_TRANSPORT_KEYS)


def test_retired_case_does_not_read_database_url_value():
    class EndpointTrap(Mapping):
        def __init__(self, values):
            self._values = dict(values)
            self.accessed = []

        def __iter__(self):
            return iter(self._values)

        def __len__(self):
            return len(self._values)

        def __getitem__(self, key):
            self.accessed.append(key)
            if key == "DATABASE_URL":
                raise AssertionError("DATABASE_URL value was read")
            return self._values[key]

    env = EndpointTrap(
        {
            "APP_ENV": "dev",
            "DATABASE_URL": "postgresql://must-not-read",
            "DB_BRIDGE_URL": "https://must-not-read",
        }
    )
    row = generator.run_case(
        "retired_keys_present",
        env,
    )
    assert "DATABASE_URL" not in env.accessed
    assert row["database_url_presence"] == "present_redacted"
    assert row["retired_keys_present"] == ["DB_BRIDGE_URL"]
    assert row["attempts"] == []


@pytest.mark.parametrize(
    ("mutator", "expected"),
    [
        (lambda value: value.__setitem__("retired_keys", []), "schema_invalid"),
        (
            lambda value: value.__setitem__(
                "retired_keys", list(generator.RETIRED_DB_TRANSPORT_KEYS[:2])
            ),
            "schema_invalid",
        ),
        (
            lambda value: value.__setitem__(
                "retired_keys", list(reversed(generator.RETIRED_DB_TRANSPORT_KEYS))
            ),
            "schema_invalid",
        ),
        (
            lambda value: value.__setitem__(
                "retired_keys",
                [
                    "DB_ALLOW_BRIDGE_IN_PROD",
                    "DB_BRIDGE_URL",
                    "DB_BRIDGE_URL",
                ],
            ),
            "schema_invalid",
        ),
        (
            lambda value: value.__setitem__(
                "retired_keys",
                [*generator.RETIRED_DB_TRANSPORT_KEYS, "DB_EXTRA"],
            ),
            "schema_invalid",
        ),
        (
            lambda value: value["cases"][3].__setitem__("retired_keys_present", []),
            "schema_invalid",
        ),
        (
            lambda value: value["cases"][3].__setitem__(
                "retired_keys_present", list(reversed(generator.RETIRED_DB_TRANSPORT_KEYS))
            ),
            "schema_invalid",
        ),
    ],
)
def test_retired_roster_exact_length_and_order_mutations_fail(mutator, expected):
    payload = copy.deepcopy(generator.build())
    mutator(payload)
    assert expected in generator.validate_contract(payload)
