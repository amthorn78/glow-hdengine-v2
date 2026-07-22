from __future__ import annotations

import copy
import json

import pytest

from tools.evidence import generate_hde_epic038_direct_db_selection as generator


def test_direct_selection_generation_is_exact_canonical_and_checkable(tmp_path):
    out = tmp_path / "direct.json"
    assert generator.main(["--out", str(out)]) == 0
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
    assert "schema_invalid" in generator.validate_contract(payload)


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
    class EndpointTrap(dict):
        def __getitem__(self, key):
            if key == "DATABASE_URL":
                raise AssertionError("DATABASE_URL value was read")
            return super().__getitem__(key)

        def get(self, key, default=None):
            if key == "DATABASE_URL":
                raise AssertionError("DATABASE_URL value was read")
            return super().get(key, default)

    row = generator.run_case(
        "retired_keys_present",
        EndpointTrap(
            {
                "APP_ENV": "dev",
                "DATABASE_URL": "postgresql://must-not-read",
                "DB_BRIDGE_URL": "https://must-not-read",
            }
        ),
    )
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
